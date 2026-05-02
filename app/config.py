"""
Centralized configuration via pydantic-settings.
Loads from .env file and environment variables.
"""

from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # Blender
    blender_path: str = "blender"
    blender_timeout: int = 600  # seconds

    # Storage
    upload_dir: str = "./uploads"
    output_dir: str = "./outputs"

    # Render defaults
    render_samples: int = 64
    render_resolution_x: int = 1920
    render_resolution_y: int = 1080
    render_device: str = "CPU"  # CPU or GPU

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    max_upload_size_mb: int = 100

    # Material catalog
    catalog_path: str = "./catalog/materials.json"

    @property
    def max_upload_size_bytes(self) -> int:
        return self.max_upload_size_mb * 1024 * 1024

    def ensure_directories(self) -> None:
        """Create upload and output directories if they don't exist."""
        Path(self.upload_dir).mkdir(parents=True, exist_ok=True)
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)


# Singleton instance
settings = Settings()
