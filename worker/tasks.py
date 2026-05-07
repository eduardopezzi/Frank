"""
Celery tasks — render job execution via Blender CLI.
Each task spawns a fresh Blender process for complete memory isolation.
"""

import json
import logging
import os
import subprocess
from pathlib import Path

from celery import Task
from celery.exceptions import SoftTimeLimitExceeded

from worker.celery_app import celery_app

logger = logging.getLogger(__name__)

# Path to the Blender render script
BLENDER_SCRIPT = str(
    Path(__file__).parent / "blender_scripts" / "render_gltf.py"
)
BLENDER_PATH = os.getenv("BLENDER_PATH", "blender")
BLENDER_TIMEOUT = int(os.getenv("BLENDER_TIMEOUT", "600"))

CONVERT_SCRIPT = str(
    Path(__file__).parent / "blender_scripts" / "convert_to_glb.py"
)


class RenderTask(Task):
    """Base class for render tasks with error handling."""

    autoretry_for = (subprocess.CalledProcessError,)
    retry_backoff = True
    retry_kwargs = {"max_retries": 2}


@celery_app.task(
    bind=True,
    base=RenderTask,
    name="worker.tasks.render_glb",
)
def render_glb_task(
    self,
    job_id: str,
    input_path: str,
    output_path: str,
    render_settings: dict | None = None,
):
    """
    Execute a Blender Cycles render job.

    Args:
        job_id: Unique job identifier
        input_path: Path to the uploaded .glb file
        output_path: Path where the rendered PNG will be saved
        render_settings: Dict with render configuration (samples, resolution, etc.)
    """
    logger.info(f"Starting render job: {job_id}")

    # Update task state to PROGRESS
    self.update_state(
        state="PROGRESS",
        meta={"progress": 0, "stage": "initializing"},
    )

    # Validate input file exists
    if not Path(input_path).exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Ensure output directory exists
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    # Serialize render settings to a temporary file to avoid "Argument list too long" error
    settings_tmp_path = Path(input_path).parent / f"settings_{job_id}.json"
    
    # Enrich settings with paths for the worker
    enhanced_settings = (render_settings or {}).copy()
    enhanced_settings["textures_dir"] = str(Path("/app/catalog/textures").absolute())
    
    with open(settings_tmp_path, "w") as f:
        json.dump(enhanced_settings, f)
    
    # Build Blender CLI command
    cmd = [
        BLENDER_PATH,
        "-b",                      # Background mode (no GUI)
        "-P", BLENDER_SCRIPT,      # Python script to execute
        "--",                      # Separator for script arguments
        input_path,
        output_path,
        str(settings_tmp_path),    # Pass file path instead of raw JSON
    ]

    logger.info(f"Executing: {' '.join(cmd)}")

    self.update_state(
        state="PROGRESS",
        meta={"progress": 10, "stage": "launching_blender"},
    )

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=BLENDER_TIMEOUT,
            check=True,
        )

        logger.info(f"Blender stdout:\n{result.stdout[-500:]}")

        if result.stderr:
            logger.warning(f"Blender stderr:\n{result.stderr[-500:]}")

    except subprocess.TimeoutExpired:
        logger.error(f"Render timeout after {BLENDER_TIMEOUT}s: {job_id}")
        raise RuntimeError(
            f"Render timed out after {BLENDER_TIMEOUT} seconds"
        )
    except subprocess.CalledProcessError as e:
        logger.error(f"Blender process failed: {e.stderr[-500:] if e.stderr else 'no stderr'}")
        raise RuntimeError(
            f"Blender render failed: {e.stderr[-500:] if e.stderr else 'unknown error'}"
        )
    except SoftTimeLimitExceeded:
        logger.error(f"Celery soft time limit exceeded: {job_id}")
        raise RuntimeError("Render exceeded the time limit")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise e
    finally:
        # Cleanup settings file
        if 'settings_tmp_path' in locals() and settings_tmp_path.exists():
            settings_tmp_path.unlink()

    # Verify output was created
    if not Path(output_path).exists():
        raise RuntimeError(
            f"Render completed but output file not found at {output_path}"
        )

    output_size = Path(output_path).stat().st_size
    logger.info(
        f"Render completed: {job_id} | output={output_path} | size={output_size} bytes"
    )

    return {
        "job_id": job_id,
        "status": "completed",
        "output_file": output_path,
        "output_size_bytes": output_size,
    }
@celery_app.task(
    bind=True,
    base=RenderTask,
    name="worker.tasks.convert_to_glb",
)
def convert_to_glb_task(self, input_path: str, output_path: str):
    """Convert any supported 3D format to GLB for preview."""
    logger.info(f"Converting for preview: {input_path}")
    
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    cmd = [
        BLENDER_PATH,
        "-b",
        "-P", CONVERT_SCRIPT,
        "--",
        input_path,
        output_path,
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120, check=True)
        logger.info(f"Blender conversion output:\n{result.stdout[-500:]}")
        if result.stderr:
            logger.warning(f"Blender conversion stderr:\n{result.stderr[-500:]}")
        
        if not Path(output_path).exists():
            raise RuntimeError(f"Blender conversion completed but output file not found at {output_path}")
            
        return {"status": "success", "output": output_path}
    except subprocess.CalledProcessError as e:
        logger.error(f"Conversion failed (exit {e.returncode}): {e.stderr[-500:] if e.stderr else 'no stderr'}")
        raise RuntimeError(f"Blender conversion failed: {e.stderr[-200:] if e.stderr else 'unknown error'}")
    except Exception as e:
        logger.error(f"Conversion error: {str(e)}")
        raise e
