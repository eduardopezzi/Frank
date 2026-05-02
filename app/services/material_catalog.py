"""
Material catalog service — CRUD operations for PBR materials.
Persists to a JSON file (migrable to a database later).
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Optional

from app.config import settings
from app.models.material import Material, MaterialCreate, MaterialUpdate


class MaterialCatalogService:
    """Manages the PBR material catalog with JSON file persistence."""

    def __init__(self):
        self.catalog_path = Path(settings.catalog_path)
        self._ensure_catalog_exists()

    def _ensure_catalog_exists(self) -> None:
        """Create the catalog file if it doesn't exist."""
        self.catalog_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.catalog_path.exists():
            self._save_catalog([])

    def _load_catalog(self) -> list[dict]:
        """Load the catalog from the JSON file."""
        with open(self.catalog_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save_catalog(self, materials: list[dict]) -> None:
        """Save the catalog to the JSON file."""
        with open(self.catalog_path, "w", encoding="utf-8") as f:
            json.dump(materials, f, indent=2, ensure_ascii=False, default=str)

    def list_materials(
        self,
        category: Optional[str] = None,
        tag: Optional[str] = None,
    ) -> list[Material]:
        """List all materials, optionally filtered by category or tag."""
        data = self._load_catalog()
        materials = [Material(**m) for m in data]

        if category:
            materials = [m for m in materials if m.category == category]
        if tag:
            materials = [m for m in materials if tag in m.tags]

        return materials

    def get_material(self, material_id: str) -> Optional[Material]:
        """Get a material by its ID."""
        data = self._load_catalog()
        for m in data:
            if m["material_id"] == material_id:
                return Material(**m)
        return None

    def create_material(self, material_data: MaterialCreate) -> Material:
        """Create a new material in the catalog."""
        data = self._load_catalog()

        # Check for duplicate ID
        if any(m["material_id"] == material_data.material_id for m in data):
            raise ValueError(
                f"Material with ID '{material_data.material_id}' already exists"
            )

        material = Material(
            **material_data.model_dump(),
            created_at=datetime.utcnow(),
        )

        data.append(material.model_dump())
        self._save_catalog(data)

        return material

    def update_material(
        self, material_id: str, update_data: MaterialUpdate
    ) -> Optional[Material]:
        """Update an existing material. Returns None if not found."""
        data = self._load_catalog()

        for i, m in enumerate(data):
            if m["material_id"] == material_id:
                # Merge update fields
                update_dict = update_data.model_dump(exclude_none=True)
                for key, value in update_dict.items():
                    if key == "pbr_properties" and value is not None:
                        # Merge PBR properties instead of replacing
                        if "pbr_properties" not in m:
                            m["pbr_properties"] = {}
                        if isinstance(value, dict):
                            m["pbr_properties"].update(value)
                        else:
                            m["pbr_properties"] = value.model_dump() if hasattr(value, 'model_dump') else value
                    else:
                        m[key] = value

                m["updated_at"] = datetime.utcnow().isoformat()
                data[i] = m
                self._save_catalog(data)
                return Material(**m)

        return None

    def delete_material(self, material_id: str) -> bool:
        """Delete a material by ID. Returns True if deleted."""
        data = self._load_catalog()
        original_len = len(data)
        data = [m for m in data if m["material_id"] != material_id]

        if len(data) < original_len:
            self._save_catalog(data)
            return True
        return False

    def get_categories(self) -> list[str]:
        """List all distinct categories in the catalog."""
        data = self._load_catalog()
        return sorted(set(m.get("category", "") for m in data))

    def get_tags(self) -> list[str]:
        """List all distinct tags used across materials."""
        data = self._load_catalog()
        tags = set()
        for m in data:
            tags.update(m.get("tags", []))
        return sorted(tags)

    def search_materials(self, query: str) -> list[Material]:
        """Search materials by name, category, tags, or description."""
        query_lower = query.lower()
        data = self._load_catalog()
        results = []

        for m in data:
            searchable = " ".join([
                m.get("name", ""),
                m.get("category", ""),
                m.get("description", "") or "",
                " ".join(m.get("tags", [])),
                m.get("material_id", ""),
            ]).lower()

            if query_lower in searchable:
                results.append(Material(**m))

        return results

    def get_materials_by_ids(self, material_ids: list[str]) -> list[Material]:
        """Get multiple materials by their IDs (for render jobs)."""
        data = self._load_catalog()
        return [
            Material(**m)
            for m in data
            if m["material_id"] in material_ids
        ]


# Singleton
material_catalog = MaterialCatalogService()
