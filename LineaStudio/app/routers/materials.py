"""
Materials router — CRUD endpoints for the PBR material catalog.
"""

import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, Query

from app.models.material import Material, MaterialCreate, MaterialUpdate
from app.services.material_catalog import material_catalog

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
    summary="Delete material",
    description="Remove a material from the catalog.",
)
async def delete_material(material_id: str):
    """Delete a material by ID."""
    deleted = material_catalog.delete_material(material_id)
    if not deleted:
        raise HTTPException(
            status_code=404,
            detail=f"Material '{material_id}' not found",
        )
    logger.info(f"Material deleted: {material_id}")
    return {"deleted": True, "material_id": material_id}
