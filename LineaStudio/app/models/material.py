"""
PBR Material models — aligned with glTF 2.0 PBR Metallic-Roughness workflow.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PBRProperties(BaseModel):
    """
    Physically Based Rendering properties.
    Follows the glTF 2.0 Metallic-Roughness model.
    """

    # Base color (RGBA, 0.0–1.0)
    base_color: tuple[float, float, float, float] = Field(
        default=(0.8, 0.8, 0.8, 1.0),
        description="Base color as RGBA tuple (0.0–1.0)",
    )
    metallic: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Metallic factor (0=dielectric, 1=metal)",
    )
    roughness: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
        description="Roughness factor (0=smooth/glossy, 1=rough/matte)",
    )
    emission: float = Field(
        default=0.0,
        ge=0.0,
        description="Emission strength",
    )
    emission_color: tuple[float, float, float] = Field(
        default=(1.0, 1.0, 1.0),
        description="Emission color as RGB tuple",
    )
    alpha: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="Opacity (0=transparent, 1=opaque)",
    )
    ior: float = Field(
        default=1.45,
        ge=1.0,
        le=3.0,
        description="Index of refraction (glass=1.5, water=1.33)",
    )
    transmission: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Transmission factor for transparent materials",
    )

    # Texture maps (file paths or URLs)
    base_color_map: Optional[str] = Field(
        default=None, description="Path to albedo/diffuse texture"
    )
    roughness_map: Optional[str] = Field(
        default=None, description="Path to roughness texture"
    )
    metallic_map: Optional[str] = Field(
        default=None, description="Path to metallic texture"
    )
    normal_map: Optional[str] = Field(
        default=None, description="Path to normal map texture"
    )
    displacement_map: Optional[str] = Field(
        default=None, description="Path to displacement map texture"
    )
    ao_map: Optional[str] = Field(
        default=None, description="Path to ambient occlusion texture"
    )


class Material(BaseModel):
    """A PBR material in the catalog."""

    material_id: str = Field(description="Unique identifier (e.g., wood_taco_01)")
    name: str = Field(description="Human-readable name")
    category: str = Field(description="Category (wood, metal, concrete, glass, wall, floor)")
    tags: list[str] = Field(default_factory=list, description="Search tags")
    description: Optional[str] = Field(default=None, description="Material description")
    pbr_properties: PBRProperties = Field(default_factory=PBRProperties)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None

    # SketchUp mapping
    sketchup_material_name: Optional[str] = Field(
        default=None,
        description="Corresponding material name in SketchUp for auto-mapping",
    )


class MaterialCreate(BaseModel):
    """Schema for creating a new material (no auto-generated fields)."""

    material_id: str
    name: str
    category: str
    tags: list[str] = Field(default_factory=list)
    description: Optional[str] = None
    pbr_properties: PBRProperties = Field(default_factory=PBRProperties)
    sketchup_material_name: Optional[str] = None


class MaterialUpdate(BaseModel):
    """Schema for updating an existing material (all fields optional)."""

    name: Optional[str] = None
    category: Optional[str] = None
    tags: Optional[list[str]] = None
    description: Optional[str] = None
    pbr_properties: Optional[PBRProperties] = None
    sketchup_material_name: Optional[str] = None
