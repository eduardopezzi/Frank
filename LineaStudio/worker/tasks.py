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

    # Serialize render settings for the Blender script
    settings_json = json.dumps(render_settings or {})

    # Build Blender CLI command
    # blender -b (background) -P script.py -- input output settings
    # NOTA: Removido --factory-startup para permitir carregamento de addons (sketchup_importer)
    cmd = [
        BLENDER_PATH,
        "-b",                      # Background mode (no GUI)
        "-P", BLENDER_SCRIPT,      # Python script to execute
        "--",                      # Separator for script arguments
        input_path,
        output_path,
        settings_json,
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
            f"Blender render failed: {e.stderr[-200:] if e.stderr else 'unknown error'}"
        )

    except SoftTimeLimitExceeded:
        logger.error(f"Celery soft time limit exceeded: {job_id}")
        raise RuntimeError("Render exceeded the time limit")

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
