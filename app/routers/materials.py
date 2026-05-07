"""
Materials router — CRUD endpoints for the PBR material catalog.
"""

import logging
from typing import Optional

import uuid
import shutil
import os
import httpx
from pathlib import Path
from fastapi import APIRouter, HTTPException, Query, UploadFile, File, Form

from app.models.material import Material, MaterialCreate, MaterialUpdate
from app.services.material_catalog import material_catalog
from app.utils.pbr_generator import PBRGenerator
from app.config import settings

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "",
    response_model=list[Material],
    summary="List materials",
    description="List all PBR materials in the catalog, with optional filtering.",
)
async def list_materials(
    category: Optional[str] = Query(default=None, description="Filter by category"),
    tag: Optional[str] = Query(default=None, description="Filter by tag"),
    search: Optional[str] = Query(default=None, description="Search query"),
):
    """List materials with optional filters."""
    if search:
        return material_catalog.search_materials(search)
    return material_catalog.list_materials(category=category, tag=tag)


@router.get(
    "/categories",
    response_model=list[str],
    summary="List categories",
    description="Get all distinct material categories.",
)
async def list_categories():
    """List all material categories."""
    return material_catalog.get_categories()


@router.get(
    "/tags",
    response_model=list[str],
    summary="List tags",
    description="Get all distinct tags used across materials.",
)
async def list_tags():
    """List all material tags."""
    return material_catalog.get_tags()


@router.get(
    "/{material_id}",
    response_model=Material,
    summary="Get material",
    description="Get a specific material by its ID.",
)
async def get_material(material_id: str):
    """Get a material by ID."""
    material = material_catalog.get_material(material_id)
    if not material:
        raise HTTPException(
            status_code=404,
            detail=f"Material '{material_id}' not found",
        )
    return material


@router.post(
    "",
    response_model=Material,
    status_code=201,
    summary="Create material",
    description="Add a new PBR material to the catalog.",
)
async def create_material(material_data: MaterialCreate):
    """Create a new material."""
    try:
        material = material_catalog.create_material(material_data)
        logger.info(f"Material created: {material.material_id}")
        return material
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))


@router.put(
    "/{material_id}",
    response_model=Material,
    summary="Update material",
    description="Update an existing material's properties.",
)
async def update_material(material_id: str, update_data: MaterialUpdate):
    """Update a material by ID."""
    material = material_catalog.update_material(material_id, update_data)
    if not material:
        raise HTTPException(
            status_code=404,
            detail=f"Material '{material_id}' not found",
        )
    logger.info(f"Material updated: {material_id}")
    return material


@router.delete(
    "/{material_id}",
    status_code=204,
    summary="Delete material",
)
async def delete_material(material_id: str):
    """Delete a material."""
    success = material_catalog.delete_material(material_id)
    if not success:
        raise HTTPException(status_code=404, detail="Material not found")
    return None

@router.post(
    "/generate",
    summary="Generate PBR maps from image",
    description="Processes an image to generate Albedo, Normal, Roughness and Height maps."
)
async def generate_from_image(file: UploadFile = File(...)):
    """Generate PBR textures from a single image."""
    # 1. Save temp input file
    temp_id = str(uuid.uuid4())[:8]
    ext = file.filename.split('.')[-1].lower()
    temp_path = Path(settings.upload_dir) / f"gen_{temp_id}.{ext}"
    
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        # 2. Generate maps
        base_name = f"mat_{temp_id}"
        maps = PBRGenerator.generate_maps(
            str(temp_path),
            settings.textures_dir,
            base_name
        )
        
        # 3. Cleanup temp
        os.remove(temp_path)
        
        # 4. Return suggested material data
        return {
            "name": "Novo Material Gerado",
            "pbr_properties": {
                "base_color_map": maps["albedo"],
                "normal_map": maps["normal"],
                "roughness_map": maps["roughness"],
                "displacement_map": maps["height"],
                "metallic": 0.0,
                "roughness": 0.5
            }
        }
    except Exception as e:
        if temp_path.exists(): os.remove(temp_path)
        logger.error(f"PBR Generation failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Generation failed: {str(e)}")

@router.get("/polyhaven/search")
async def search_polyhaven(q: str = Query(None)):
    """Proxy to search Poly Haven assets"""
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get("https://api.polyhaven.com/assets?t=textures")
            res.raise_for_status()
            data = res.json()
            
            results = []
            for asset_id, info in data.items():
                if q and q.lower() not in info['name'].lower() and q.lower() not in str(info.get('tags', [])).lower():
                    continue
                results.append({
                    "id": asset_id,
                    "name": info['name'],
                    "thumbnail": info['thumbnail_url'],
                    "categories": info.get('categories', [])
                })
            
            results.sort(key=lambda x: x['name'])
            return results[:100]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/polyhaven/import")
async def import_polyhaven(asset_id: str = Form(...), resolution: str = Form("1k")):
    """Import an asset from Poly Haven: downloads maps and creates material"""
    try:
        async with httpx.AsyncClient() as client:
            # 1. Get file list
            res = await client.get(f"https://api.polyhaven.com/files/{asset_id}")
            res.raise_for_status()
            files = res.json()

            map_keys = {
                "Diffuse": "base_color_map",
                "nor_gl": "normal_map",
                "Rough": "roughness_map",
                "Displacement": "displacement_map"
            }
            
            # Prepare payload for material creation
            pbr_props = {
                "metallic": 0.0,
                "roughness": 0.5
            }
            
            for ph_key, pbr_key in map_keys.items():
                if ph_key in files:
                    formats = files[ph_key].get(resolution, {})
                    target_format = "jpg" if "jpg" in formats else "png"
                    if target_format in formats:
                        url = formats[target_format]["url"]
                        ext = target_format
                        
                        # Download
                        file_res = await client.get(url)
                        file_res.raise_for_status()
                        
                        local_name = f"ph_{asset_id}_{pbr_key}.{ext}"
                        local_path = os.path.join(settings.textures_dir, local_name)
                        
                        with open(local_path, "wb") as f:
                            f.write(file_res.content)
                        
                        pbr_props[pbr_key] = local_name

            # 3. Create material entry
            from app.models.material import MaterialCreate
            asset_info_res = await client.get("https://api.polyhaven.com/assets?t=textures")
            asset_info = asset_info_res.json().get(asset_id, {"name": asset_id, "categories": ["other"]})
            
            mat_create = MaterialCreate(
                material_id=f"ph_{asset_id}",
                name=asset_info["name"],
                category=asset_info["categories"][0] if asset_info.get("categories") else "other",
                pbr_properties=pbr_props
            )
            
            new_mat = material_catalog.create_material(mat_create)
            return {"status": "success", "material": new_mat}

    except Exception as e:
        logger.error(f"Poly Haven import failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))
@router.post("/upload-texture")
async def upload_texture(file: UploadFile = File(...)):
    """Upload a texture file and return its stored name."""
    try:
        ext = file.filename.split('.')[-1].lower()
        if ext not in ["jpg", "jpeg", "png", "tga", "exr", "hdr"]:
            raise HTTPException(status_code=400, detail="Unsupported image format")
            
        unique_id = str(uuid.uuid4())[:8]
        local_name = f"up_{unique_id}_{file.filename}"
        local_path = os.path.join(settings.textures_dir, local_name)
        
        with open(local_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        return {"filename": local_name}
    except Exception as e:
        logger.error(f"Texture upload failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))
