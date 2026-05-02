"""
Render router — endpoints for submitting, tracking, and downloading render jobs.
"""

import json
import uuid
import logging

from fastapi import APIRouter, File, Form, UploadFile, HTTPException
from fastapi.responses import FileResponse

from app.config import settings
from app.models.job import RenderResponse, RenderSettings, RenderStatusResponse
from app.services.storage import storage_service
from worker.celery_app import celery_app
from worker.tasks import render_glb_task

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "",
    response_model=RenderResponse,
    summary="Submit a render job",
    description="Upload a .glb/.gltf/.skp file and enqueue it for Cycles rendering.",
)
async def submit_render(
    file: UploadFile = File(..., description="3D model file (.glb, .gltf, or .skp)"),
    samples: int = Form(default=None, description="Number of render samples"),
    resolution_x: int = Form(default=None, description="Output width in pixels"),
    resolution_y: int = Form(default=None, description="Output height in pixels"),
    device: str = Form(default=None, description="Render device: CPU or GPU"),
    camera_angle: str = Form(default=None, description="Camera preset: auto, front, top, side, perspective"),
    material_overrides: str = Form(default=None, description="JSON list of material_ids to apply"),
):
    """Submit a .glb/.gltf/.skp file for rendering via Blender Cycles."""

    # Validate file extension
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is required")

    ext = file.filename.rsplit(".", 1)[-1].lower() if "." in file.filename else ""
    if ext not in ("glb", "gltf", "obj", "dae"):
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported format '.{ext}'. Only .glb, .gltf, .obj, .dae files are supported.",
        )

    # Check file size
    content = await file.read()
    if len(content) > settings.max_upload_size_bytes:
        raise HTTPException(
            status_code=413,
            detail=f"File too large. Maximum size: {settings.max_upload_size_mb}MB",
        )

    # Save upload
    try:
        input_path = storage_service.save_upload(content, file.filename)
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


@router.get(
    "/status/{job_id}",
    response_model=RenderStatusResponse,
    summary="Get job status",
    description="Check the current status of a render job.",
)
async def get_render_status(job_id: str):
    """Get the current status of a render job."""

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

    response = RenderStatusResponse(
        job_id=job_id,
        status=status,
        created_at="",  # Celery doesn't track this natively
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

    result = celery_app.AsyncResult(job_id)

    if result.state != "SUCCESS":
        raise HTTPException(
            status_code=404,
            detail=f"Job {job_id} is not completed (status: {result.state})",
        )

    try:
        output_file = storage_service.get_output_file(job_id)
    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail=f"Output file not found for job {job_id}",
        )

    return FileResponse(
        path=str(output_file),
        media_type="image/png",
        filename=f"render_{job_id}.png",
    )


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