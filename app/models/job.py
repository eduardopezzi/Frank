"""
Render job models — status tracking and render settings.
"""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class JobStatus(str, Enum):
    """Possible states of a render job."""

    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class RenderSettings(BaseModel):
    """Per-job render configuration (overrides defaults)."""

    samples: int = Field(default=64, ge=1, le=4096, description="Number of render samples")
    resolution_x: int = Field(default=1920, ge=100, le=7680, description="Output width in pixels")
    resolution_y: int = Field(default=1080, ge=100, le=4320, description="Output height in pixels")
    device: str = Field(default="CPU", pattern="^(CPU|GPU)$", description="Render device")
    camera_angle: str = Field(
        default="auto",
        description="Camera angle preset: auto, front, top, side, perspective",
    )
    camera_position: Optional[list[float]] = Field(
        default=None,
        description="Camera [x, y, z] position in Blender coordinates",
    )
    camera_target: Optional[list[float]] = Field(
        default=None,
        description="Camera look-at target [x, y, z] in Blender coordinates",
    )
    camera_fov: Optional[float] = Field(
        default=None,
        ge=10,
        le=120,
        description="Camera field of view in degrees",
    )
    material_overrides: Optional[dict[str, str]] = Field(
        default=None,
        description="Mapping of model part names to material_ids from the catalog",
    )


class RenderJob(BaseModel):
    """Represents a render job with its current state."""

    job_id: str
    status: JobStatus = JobStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    input_file: str
    output_file: Optional[str] = None
    error: Optional[str] = None
    render_settings: RenderSettings = Field(default_factory=RenderSettings)
    progress: Optional[float] = Field(default=None, ge=0.0, le=100.0)

    def to_status_response(self) -> dict:
        """Return a clean status dict for API responses."""
        response = {
            "job_id": self.job_id,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
        }
        if self.updated_at:
            response["updated_at"] = self.updated_at.isoformat()
        if self.output_file:
            response["output_file"] = self.output_file
        if self.error:
            response["error"] = self.error
        if self.progress is not None:
            response["progress"] = self.progress
        return response


class RenderResponse(BaseModel):
    """Response model for render submission."""

    job_id: str
    status: str
    message: str


class RenderStatusResponse(BaseModel):
    """Response model for status queries."""

    job_id: str
    status: str
    created_at: str
    updated_at: Optional[str] = None
    output_file: Optional[str] = None
    error: Optional[str] = None
    progress: Optional[float] = None
