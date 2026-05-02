"""
Storage service — manages upload/output file operations.
"""

import os
import shutil
import uuid
from datetime import datetime, timedelta
from pathlib import Path

from app.config import settings


class StorageService:
    """Handles file storage for uploads and rendered outputs."""

    def __init__(self):
        self.upload_dir = Path(settings.upload_dir)
        self.output_dir = Path(settings.output_dir)
        self.upload_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def save_upload(self, file_content: bytes, original_filename: str) -> str:
        """
        Save an uploaded file with a unique name.
        Returns the full path to the saved file.
        """
        ext = Path(original_filename).suffix.lower()
        if ext not in (".glb", ".gltf", ".obj", ".dae", ".skp"):
            raise ValueError(f"Unsupported file format: {ext}. Use .glb, .gltf, .obj, .dae, or .skp")

        unique_name = f"{uuid.uuid4()}{ext}"
        file_path = self.upload_dir / unique_name
        file_path.write_bytes(file_content)

        return str(file_path)

    def get_output_path(self, job_id: str, ext: str = ".png") -> str:
        """Generate an output path for a render job."""
        return str(self.output_dir / f"{job_id}{ext}")

    def output_exists(self, job_id: str, ext: str = ".png") -> bool:
        """Check if the output file exists for a given job."""
        output_path = self.output_dir / f"{job_id}{ext}"
        return output_path.exists()

    def get_output_file(self, job_id: str, ext: str = ".png") -> Path:
        """Get the output file path. Raises FileNotFoundError if not found."""
        output_path = self.output_dir / f"{job_id}{ext}"
        if not output_path.exists():
            raise FileNotFoundError(f"Output not found for job {job_id}")
        return output_path

    def cleanup_upload(self, file_path: str) -> None:
        """Remove an uploaded file after processing."""
        path = Path(file_path)
        if path.exists():
            path.unlink()

    def cleanup_old_files(self, max_age_hours: int = 24) -> int:
        """
        Remove files older than max_age_hours from both directories.
        Returns the number of files removed.
        """
        cutoff = datetime.utcnow() - timedelta(hours=max_age_hours)
        removed = 0

        for directory in [self.upload_dir, self.output_dir]:
            for file_path in directory.iterdir():
                if file_path.name == ".gitkeep":
                    continue
                if file_path.is_file():
                    mtime = datetime.utcfromtimestamp(file_path.stat().st_mtime)
                    if mtime < cutoff:
                        file_path.unlink()
                        removed += 1

        return removed

    def get_storage_stats(self) -> dict:
        """Return storage usage statistics."""
        def dir_size(path: Path) -> tuple[int, int]:
            total_size = 0
            file_count = 0
            for f in path.iterdir():
                if f.is_file() and f.name != ".gitkeep":
                    total_size += f.stat().st_size
                    file_count += 1
            return total_size, file_count

        upload_size, upload_count = dir_size(self.upload_dir)
        output_size, output_count = dir_size(self.output_dir)

        return {
            "uploads": {
                "count": upload_count,
                "size_mb": round(upload_size / (1024 * 1024), 2),
            },
            "outputs": {
                "count": output_count,
                "size_mb": round(output_size / (1024 * 1024), 2),
            },
            "total_size_mb": round((upload_size + output_size) / (1024 * 1024), 2),
        }


# Singleton
storage_service = StorageService()
