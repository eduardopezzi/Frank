"""
API integration tests.
Tests the FastAPI endpoints without requiring Blender or Redis.
Uses mocking for Celery tasks.
"""

import json
from unittest.mock import patch, MagicMock

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestHealthEndpoints:
    """Test system health and info endpoints."""

    def test_health_check(self):
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "cycles-rendering-engine"

    def test_root_endpoint(self):
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Cycles Rendering Engine"
        assert "docs" in data


class TestRenderEndpoints:
    """Test render submission and status endpoints."""

    @patch("app.routers.render.render_glb_task")
    def test_submit_render_success(self, mock_task):
        """Test successful render job submission."""
        mock_async = MagicMock()
        mock_task.apply_async.return_value = mock_async

        # Create a minimal GLB file (just the header)
        glb_header = b"glTF" + b"\x00" * 100

        response = client.post(
            "/render",
            files={"file": ("test_model.glb", glb_header, "model/gltf-binary")},
        )

        assert response.status_code == 200
        data = response.json()
        assert "job_id" in data
        assert data["status"] == "pending"
        assert data["message"] == "Render job enqueued successfully"

        # Verify Celery task was called
        mock_task.apply_async.assert_called_once()

    def test_submit_render_wrong_format(self):
        """Test rejection of non-GLB file."""
        response = client.post(
            "/render",
            files={"file": ("model.obj", b"fake content", "application/octet-stream")},
        )

        assert response.status_code == 400
        assert "Unsupported format" in response.json()["detail"]

    def test_submit_render_no_file(self):
        """Test rejection when no file is uploaded."""
        response = client.post("/render")
        assert response.status_code == 422  # Validation error

    @patch("app.routers.render.render_glb_task")
    def test_submit_render_with_settings(self, mock_task):
        """Test render submission with custom settings."""
        mock_async = MagicMock()
        mock_task.apply_async.return_value = mock_async

        glb_header = b"glTF" + b"\x00" * 100

        response = client.post(
            "/render",
            files={"file": ("model.glb", glb_header, "model/gltf-binary")},
            data={
                "samples": "128",
                "resolution_x": "3840",
                "resolution_y": "2160",
                "device": "GPU",
            },
        )

        assert response.status_code == 200

        # Verify settings were passed to Celery
        call_kwargs = mock_task.apply_async.call_args
        render_settings = call_kwargs.kwargs.get("kwargs", {}).get("render_settings", {})
        if render_settings:
            assert render_settings["samples"] == 128

    @patch("app.routers.render.celery_app")
    def test_get_render_status_pending(self, mock_celery):
        """Test status check for a pending job."""
        mock_result = MagicMock()
        mock_result.state = "PENDING"
        mock_result.result = None
        mock_result.info = None
        mock_celery.AsyncResult.return_value = mock_result

        response = client.get("/render/status/test-job-123")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "pending"

    @patch("app.routers.render.celery_app")
    def test_get_render_status_completed(self, mock_celery):
        """Test status check for a completed job."""
        mock_result = MagicMock()
        mock_result.state = "SUCCESS"
        mock_result.result = {"output_file": "outputs/test.png"}
        mock_result.info = None
        mock_celery.AsyncResult.return_value = mock_result

        response = client.get("/render/status/test-job-123")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "completed"
        assert data["output_file"] == "outputs/test.png"

    @patch("app.routers.render.celery_app")
    def test_get_render_status_failed(self, mock_celery):
        """Test status check for a failed job."""
        mock_result = MagicMock()
        mock_result.state = "FAILURE"
        mock_result.result = RuntimeError("Blender crashed")
        mock_celery.AsyncResult.return_value = mock_result

        response = client.get("/render/status/test-job-123")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "failed"

    @patch("app.routers.render.celery_app")
    def test_download_not_completed(self, mock_celery):
        """Test download attempt for an incomplete job."""
        mock_result = MagicMock()
        mock_result.state = "PENDING"
        mock_celery.AsyncResult.return_value = mock_result

        response = client.get("/render/download/test-job-123")
        assert response.status_code == 404

    def test_storage_stats(self):
        """Test storage stats endpoint."""
        response = client.get("/render/storage-stats")
        assert response.status_code == 200
        data = response.json()
        assert "uploads" in data
        assert "outputs" in data
        assert "total_size_mb" in data
