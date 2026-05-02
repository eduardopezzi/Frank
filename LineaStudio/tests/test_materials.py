"""
Material catalog tests.
Tests CRUD operations on the PBR material catalog.
"""

import json
import os
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# Use a temporary catalog file for tests
@pytest.fixture(autouse=True)
def temp_catalog(tmp_path):
    """Create a temporary catalog file for each test."""
    catalog_file = tmp_path / "test_materials.json"

    # Initial test data
    initial_materials = [
        {
            "material_id": "test_wood_01",
            "name": "Test Wood",
            "category": "wood",
            "tags": ["test", "floor"],
            "description": "A test wood material",
            "pbr_properties": {
                "base_color": [0.5, 0.3, 0.1, 1.0],
                "metallic": 0.0,
                "roughness": 0.4,
                "emission": 0.0,
                "alpha": 1.0,
                "ior": 1.45,
                "transmission": 0.0
            },
            "sketchup_material_name": None,
            "created_at": "2025-01-01T00:00:00"
        },
        {
            "material_id": "test_metal_01",
            "name": "Test Metal",
            "category": "metal",
            "tags": ["test", "exterior"],
            "description": "A test metal material",
            "pbr_properties": {
                "base_color": [0.8, 0.8, 0.8, 1.0],
                "metallic": 0.9,
                "roughness": 0.2,
                "emission": 0.0,
                "alpha": 1.0,
                "ior": 1.45,
                "transmission": 0.0
            },
            "sketchup_material_name": "Metal_Chrome",
            "created_at": "2025-01-01T00:00:00"
        },
    ]

    catalog_file.write_text(json.dumps(initial_materials, indent=2))

    with patch("app.services.material_catalog.settings") as mock_settings:
        mock_settings.catalog_path = str(catalog_file)
        # Re-initialize the service with the temp catalog
        from app.services.material_catalog import MaterialCatalogService
        temp_service = MaterialCatalogService()

        with patch("app.routers.materials.material_catalog", temp_service):
            yield temp_service


class TestListMaterials:
    """Test material listing and filtering."""

    def test_list_all_materials(self, temp_catalog):
        response = client.get("/materials")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2

    def test_filter_by_category(self, temp_catalog):
        response = client.get("/materials?category=wood")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["category"] == "wood"

    def test_filter_by_tag(self, temp_catalog):
        response = client.get("/materials?tag=exterior")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert "exterior" in data[0]["tags"]

    def test_search_materials(self, temp_catalog):
        response = client.get("/materials?search=metal")
        assert response.status_code == 200
        data = response.json()
        assert len(data) >= 1


class TestGetMaterial:
    """Test getting individual materials."""

    def test_get_existing_material(self, temp_catalog):
        response = client.get("/materials/test_wood_01")
        assert response.status_code == 200
        data = response.json()
        assert data["material_id"] == "test_wood_01"
        assert data["name"] == "Test Wood"

    def test_get_nonexistent_material(self, temp_catalog):
        response = client.get("/materials/nonexistent_99")
        assert response.status_code == 404


class TestCreateMaterial:
    """Test material creation."""

    def test_create_material_success(self, temp_catalog):
        new_material = {
            "material_id": "test_glass_01",
            "name": "Test Glass",
            "category": "glass",
            "tags": ["transparent", "window"],
            "pbr_properties": {
                "base_color": [0.9, 0.9, 1.0, 0.1],
                "metallic": 0.0,
                "roughness": 0.02,
                "transmission": 0.95,
                "ior": 1.52,
            },
        }

        response = client.post("/materials", json=new_material)
        assert response.status_code == 201
        data = response.json()
        assert data["material_id"] == "test_glass_01"
        assert data["name"] == "Test Glass"

    def test_create_duplicate_material(self, temp_catalog):
        duplicate = {
            "material_id": "test_wood_01",  # Already exists
            "name": "Duplicate",
            "category": "wood",
        }

        response = client.post("/materials", json=duplicate)
        assert response.status_code == 409  # Conflict


class TestUpdateMaterial:
    """Test material updates."""

    def test_update_material_success(self, temp_catalog):
        update = {
            "name": "Updated Wood Name",
            "tags": ["updated", "floor", "interior"],
        }

        response = client.put("/materials/test_wood_01", json=update)
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Updated Wood Name"
        assert "updated" in data["tags"]

    def test_update_nonexistent_material(self, temp_catalog):
        response = client.put(
            "/materials/nonexistent_99",
            json={"name": "Nothing"},
        )
        assert response.status_code == 404


class TestDeleteMaterial:
    """Test material deletion."""

    def test_delete_material_success(self, temp_catalog):
        response = client.delete("/materials/test_wood_01")
        assert response.status_code == 200
        data = response.json()
        assert data["deleted"] is True

        # Verify it's gone
        response = client.get("/materials/test_wood_01")
        assert response.status_code == 404

    def test_delete_nonexistent_material(self, temp_catalog):
        response = client.delete("/materials/nonexistent_99")
        assert response.status_code == 404


class TestCategoriesAndTags:
    """Test category and tag listing."""

    def test_list_categories(self, temp_catalog):
        response = client.get("/materials/categories")
        assert response.status_code == 200
        data = response.json()
        assert "wood" in data
        assert "metal" in data

    def test_list_tags(self, temp_catalog):
        response = client.get("/materials/tags")
        assert response.status_code == 200
        data = response.json()
        assert "test" in data
