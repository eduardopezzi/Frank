"""
Render router — endpoints for submitting, tracking, downloading render jobs,
and browsing the persistent gallery.
"""

import json
import os
import uuid
import logging
from datetime import datetime

from fastapi import APIRouter, File, Form, UploadFile, HTTPException, Depends, Query
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.models.job import RenderResponse, RenderSettings, RenderStatusResponse
from app.models.orm import RenderJob
from app.services.storage import storage_service
from worker.celery_app import celery_app
from worker.tasks import render_glb_task, convert_to_glb_task

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "",
    response_model=RenderResponse,
    summary="Submit a render job",
    description="Upload a .glb/.gltf/.skp file and enqueue it for Frank rendering.",
)
async def submit_render(
    file: UploadFile = File(..., description="3D model file (.glb, .gltf, or .skp)"),
    extra_files: list[UploadFile] = File(None, description="Optional extra files (like .mtl and textures)"),
    samples: int = Form(default=None, description="Number of render samples"),
    resolution_x: int = Form(default=None, description="Output width in pixels"),
    resolution_y: int = Form(default=None, description="Output height in pixels"),
    device: str = Form(default=None, description="Render device: CPU or GPU"),
    camera_angle: str = Form(default=None, description="Camera preset: auto, front, top, side, perspective, custom"),
    camera_position: str = Form(default=None, description="Camera [x,y,z] position as JSON array (Blender coords)"),
    camera_target: str = Form(default=None, description="Camera look-at [x,y,z] target as JSON array (Blender coords)"),
    camera_fov: float = Form(default=None, description="Camera field of view in degrees"),
    material_overrides: str = Form(default=None, description="JSON list of material_ids to apply"),
    db: Session = Depends(get_db),
):
    """Submit a .glb/.gltf/.skp file for rendering via Blender Cycles."""
    
    logger.info(f"[Frank] Received extra_files: {extra_files}")

    # Validate file extension
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is required")

    ext = file.filename.rsplit(".", 1)[-1].lower() if "." in file.filename else ""
    if ext not in ("glb", "gltf", "obj", "dae", "skp"):
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported format '.{ext}'. Only .glb, .gltf, .obj, .dae, .skp files are supported.",
        )

    # Check file size
    content = await file.read()
    
    # Normalize line endings for OBJ/MTL to avoid Blender path resolution issues
    if file.filename.lower().endswith(('.obj', '.mtl')):
        content = content.replace(b'\r\n', b'\n').replace(b'\r', b'\n')
        
    if len(content) > settings.max_upload_size_bytes:
        raise HTTPException(
            status_code=413,
            detail=f"File too large. Maximum size: {settings.max_upload_size_mb}MB",
        )

    # Save upload
    try:
        input_path = storage_service.save_upload(content, file.filename)
        
        # Save extra files if provided
        if extra_files:
            target_dir = os.path.dirname(input_path)
            for extra in extra_files:
                if not extra.filename: continue
                extra_content = await extra.read()
                
                # Fix DOS line endings in MTL/OBJ files to avoid Blender path issues
                if extra.filename.lower().endswith(('.mtl', '.obj')):
                    extra_content = extra_content.replace(b'\r\n', b'\n').replace(b'\r', b'\n')
                
                extra_path = os.path.join(target_dir, extra.filename)
                with open(extra_path, "wb") as f:
                    f.write(extra_content)
                logger.info(f"Extra file saved: {extra_path}")
            
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Build render settings
    render_settings = RenderSettings(
        samples=samples or settings.render_samples,
        resolution_x=resolution_x or settings.render_resolution_x,
        resolution_y=resolution_y or settings.render_resolution_y,
        device=device or settings.render_device,
        camera_angle=camera_angle or "auto",
    )

    # Parse custom camera parameters from 3D preview
    if camera_angle == "custom" and camera_position:
        try:
            render_settings.camera_position = json.loads(camera_position)
        except json.JSONDecodeError:
            raise HTTPException(
                status_code=400,
                detail="camera_position must be a valid JSON array [x, y, z]",
            )
        if camera_target:
            try:
                render_settings.camera_target = json.loads(camera_target)
            except json.JSONDecodeError:
                raise HTTPException(
                    status_code=400,
                    detail="camera_target must be a valid JSON array [x, y, z]",
                )
        if camera_fov:
            render_settings.camera_fov = camera_fov

    # Parse material overrides
    if material_overrides:
        try:
            render_settings.material_overrides = json.loads(material_overrides)
        except json.JSONDecodeError:
            raise HTTPException(
                status_code=400,
                detail="material_overrides must be a valid JSON list of material IDs",
            )

    # Generate job ID
    job_id = str(uuid.uuid4())

    # Output path
    output_path = storage_service.get_output_path(job_id)

    # ─── Persist job to database ─────────────────────────────────
    db_job = RenderJob(
        id=job_id,
        status="pending",
        original_filename=file.filename,
        file_size=len(content),
        input_path=input_path,
        output_path=output_path,
        render_settings=render_settings.model_dump(),
    )
    db.add(db_job)
    db.commit()

    # Enqueue Celery task
    render_glb_task.apply_async(
        args=[job_id, input_path, output_path],
        kwargs={"render_settings": render_settings.model_dump()},
        task_id=job_id,
    )

    logger.info(f"Render job enqueued: {job_id} | file={file.filename}")

    return RenderResponse(
        job_id=job_id,
        status="pending",
        message="Render job enqueued successfully",
    )
@router.post(
    "/preview",
    summary="Get a browser-compatible preview",
    description="Converts non-browser formats (like .skp) to .glb for 3D preview.",
)
async def get_preview(
    file: UploadFile = File(...),
):
    """Convert an uploaded file to GLB for browser preview."""
    ext = file.filename.rsplit(".", 1)[-1].lower()
    content = await file.read()
    
    # Save input
    input_path = storage_service.save_upload(content, file.filename)
    
    if ext in ("glb", "gltf"):
        # Already compatible, just return it
        return FileResponse(input_path, media_type="model/gltf-binary")
    
    # Need conversion
    job_id = f"preview_{uuid.uuid4().hex[:8]}"
    output_path = os.path.join(settings.output_dir, f"{job_id}.glb")
    
    # Run conversion task synchronously (wait for it)
    task = convert_to_glb_task.delay(input_path, output_path)
    try:
        # Wait up to 30 seconds for preview conversion
        result = task.get(timeout=30)
        if result.get("status") == "success":
            return FileResponse(output_path, media_type="model/gltf-binary")
    except Exception as e:
        logger.error(f"Preview conversion failed: {e}")
        raise HTTPException(status_code=500, detail="Preview conversion failed")
    
    raise HTTPException(status_code=500, detail="Conversion timed out")

@router.get(
    "/status/{job_id}",
    response_model=RenderStatusResponse,
    summary="Get job status",
    description="Check the current status of a render job.",
)
async def get_render_status(job_id: str, db: Session = Depends(get_db)):
    """Get the current status of a render job and sync it to the database."""

    result = celery_app.AsyncResult(job_id)

    # Map Celery states to our JobStatus
    status_map = {
        "PENDING": "pending",
        "STARTED": "processing",
        "PROGRESS": "processing",
        "SUCCESS": "completed",
        "FAILURE": "failed",
        "REVOKED": "failed",
    }

    status = status_map.get(result.state, "pending")

    # ─── Sync status to database ─────────────────────────────────
    db_job = db.query(RenderJob).filter(RenderJob.id == job_id).first()
    if db_job and db_job.status != status:
        db_job.status = status
        if status == "completed":
            db_job.completed_at = datetime.utcnow()
            if result.result:
                db_job.output_path = result.result.get("output_file", db_job.output_path)
        elif status == "failed":
            db_job.error_message = str(result.result) if result.result else "Unknown error"
        db.commit()

    response = RenderStatusResponse(
        job_id=job_id,
        status=status,
        created_at=db_job.created_at.isoformat() if db_job else "",
    )

    if result.state == "SUCCESS" and result.result:
        response.output_file = result.result.get("output_file")
    elif result.state == "FAILURE":
        response.error = str(result.result) if result.result else "Unknown error"
    elif result.state == "PROGRESS" and result.info:
        response.progress = result.info.get("progress", 0)

    return response


@router.get(
    "/download/{job_id}",
    summary="Download rendered image",
    description="Download the rendered PNG image for a completed job.",
)
async def download_render(job_id: str):
    """Download the rendered image for a completed job."""

    # Try filesystem first (works for both DB and Celery-only jobs)
    try:
        output_file = storage_service.get_output_file(job_id)
        return FileResponse(
            path=str(output_file),
            media_type="image/png",
            filename=f"render_{job_id}.png",
        )
    except FileNotFoundError:
        pass

    # Fallback: check Celery
    result = celery_app.AsyncResult(job_id)
    if result.state != "SUCCESS":
        raise HTTPException(
            status_code=404,
            detail=f"Job {job_id} is not completed (status: {result.state})",
        )

    raise HTTPException(
        status_code=404,
        detail=f"Output file not found for job {job_id}",
    )


# ─── Gallery Endpoints ───────────────────────────────────────────

@router.get(
    "/gallery",
    summary="List rendered images",
    description="Get a paginated list of completed render jobs for the gallery.",
)
async def get_gallery(
    page: int = Query(default=1, ge=1, description="Page number"),
    per_page: int = Query(default=20, ge=1, le=100, description="Items per page"),
    status: str = Query(default=None, description="Filter by status: completed, failed, pending"),
    db: Session = Depends(get_db),
):
    """Return a paginated list of render jobs for the gallery."""

    query = db.query(RenderJob).order_by(RenderJob.created_at.desc())

    # Filter by status if provided, default to only completed
    if status:
        query = query.filter(RenderJob.status == status)
    else:
        query = query.filter(RenderJob.status == "completed")

    total = query.count()
    jobs = query.offset((page - 1) * per_page).limit(per_page).all()

    items = []
    for job in jobs:
        item = {
            "job_id": job.id,
            "status": job.status,
            "original_filename": job.original_filename,
            "file_size": job.file_size,
            "rating": job.rating or 0,
            "created_at": job.created_at.isoformat() if job.created_at else None,
            "completed_at": job.completed_at.isoformat() if job.completed_at else None,
            "has_output": storage_service.output_exists(job.id),
            "render_settings": job.render_settings,
        }
        items.append(item)

    return {
        "items": items,
        "total": total,
        "page": page,
        "per_page": per_page,
        "pages": (total + per_page - 1) // per_page,
    }


@router.get(
    "/gallery/all",
    summary="List all render jobs",
    description="Get all render jobs regardless of status (for the processing queue).",
)
async def get_all_jobs(
    limit: int = Query(default=50, ge=1, le=200, description="Max items to return"),
    db: Session = Depends(get_db),
):
    """Return recent render jobs of all statuses."""

    jobs = (
        db.query(RenderJob)
        .order_by(RenderJob.created_at.desc())
        .limit(limit)
        .all()
    )

    items = []
    for job in jobs:
        items.append({
            "job_id": job.id,
            "status": job.status,
            "original_filename": job.original_filename,
            "file_size": job.file_size,
            "rating": job.rating or 0,
            "created_at": job.created_at.isoformat() if job.created_at else None,
            "completed_at": job.completed_at.isoformat() if job.completed_at else None,
            "has_output": storage_service.output_exists(job.id),
        })

    return {"items": items, "total": len(items)}


@router.patch(
    "/gallery/{job_id}/rate",
    summary="Rate a rendered image",
    description="Set a rating (0-5) for a completed render.",
)
async def rate_render(
    job_id: str,
    rating: int = Query(..., ge=0, le=5, description="Rating from 0 to 5"),
    db: Session = Depends(get_db),
):
    """Update the rating of a render job."""

    db_job = db.query(RenderJob).filter(RenderJob.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")

    db_job.rating = rating
    db.commit()

    return {"job_id": job_id, "rating": rating}


@router.delete(
    "/gallery/{job_id}",
    summary="Delete a render from gallery",
    description="Remove a render job and its output file.",
)
async def delete_render(job_id: str, db: Session = Depends(get_db)):
    """Delete a render job and clean up its files."""

    db_job = db.query(RenderJob).filter(RenderJob.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail=f"Job {job_id} not found")

    # Clean up output file
    try:
        output_file = storage_service.get_output_file(job_id)
        output_file.unlink()
    except FileNotFoundError:
        pass

    # Clean up input file
    if db_job.input_path:
        storage_service.cleanup_upload(db_job.input_path)

    # Remove from DB
    db.delete(db_job)
    db.commit()

    return {"message": f"Job {job_id} deleted", "job_id": job_id}


# ─── Storage Endpoints ───────────────────────────────────────────

@router.get(
    "/storage-stats",
    summary="Storage statistics",
    description="Get storage usage stats for uploads and outputs.",
)
async def storage_stats():
    """Return storage usage statistics."""
    return storage_service.get_storage_stats()


@router.post(
    "/cleanup",
    summary="Cleanup old files",
    description="Remove uploaded and rendered files older than the specified hours.",
)
async def cleanup_files(max_age_hours: int = 24):
    """Remove old files from storage."""
    removed = storage_service.cleanup_old_files(max_age_hours)
    return {"removed_files": removed, "max_age_hours": max_age_hours}