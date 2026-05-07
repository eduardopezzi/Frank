import trimesh
import numpy as np
import logging
from typing import List, Dict, Any, Tuple

logger = logging.getLogger(__name__)

class GeometryAnalyzer:
    """
    Analyzes 3D geometry to extract semantic information without relying on names.
    Uses spatial heuristics, face orientations, and bounding box context.
    """

    def __init__(self):
        pass

    def analyze_scene(self, scene_path: str) -> List[Dict[str, Any]]:
        """
        Loads a scene and analyzes each mesh for semantic classification.
        """
        try:
            scene = trimesh.load(scene_path)
            
            # Handle both single mesh and Scene objects
            if isinstance(scene, trimesh.Scene):
                geometries = scene.geometry
            else:
                geometries = {"main": scene}

            scene_bbox = scene.bounds
            results = []

            for name, mesh in geometries.items():
                if not isinstance(mesh, trimesh.Trimesh):
                    continue
                
                classification = self.classify_mesh(mesh, scene_bbox)
                results.append({
                    "mesh_id": name,
                    "label": classification["label"],
                    "confidence": classification["confidence"],
                    "features": classification["features"]
                })
            
            return results
        except Exception as e:
            logger.error(f"Error analyzing scene {scene_path}: {e}")
            return []

    def classify_mesh(self, mesh: trimesh.Trimesh, scene_bbox: np.ndarray) -> Dict[str, Any]:
        """
        Heuristic-based classification of a single mesh.
        """
        # 1. Feature Extraction
        centroid = mesh.centroid
        min_z = scene_bbox[0][2]
        max_z = scene_bbox[1][2]
        total_height = max_z - min_z
        
        # Relative height (0 to 1)
        rel_z = (centroid[2] - min_z) / total_height if total_height > 0 else 0
        
        # Normals analysis
        face_normals = mesh.face_normals
        avg_normal = np.mean(face_normals, axis=0)
        
        # Bounding box of the mesh itself
        mesh_extents = mesh.extents
        is_flat_horizontal = mesh_extents[2] < 0.1 * max(mesh_extents[0], mesh_extents[1])
        is_flat_vertical = mesh_extents[0] < 0.1 * max(mesh_extents[1], mesh_extents[2]) or \
                           mesh_extents[1] < 0.1 * max(mesh_extents[0], mesh_extents[2])

        # 2. Heuristics
        label = "other"
        confidence = 0.5
        
        # ROOF: High up, horizontal-ish or slanted, pointing UP
        if rel_z > 0.6 and avg_normal[2] > 0.4:
            label = "roof"
            confidence = 0.85
            if is_flat_horizontal: confidence += 0.1
            
        # FLOOR: Low down, flat, horizontal, pointing UP
        elif rel_z < 0.3 and avg_normal[2] > 0.9 and is_flat_horizontal:
            label = "floor"
            confidence = 0.95
            
        # WALL: Vertical, usually spanning multiple heights
        elif abs(avg_normal[2]) < 0.3 and is_flat_vertical:
            label = "wall"
            confidence = 0.8
            
        # WINDOW/DOOR: Vertical, smaller areas, often repeated
        elif is_flat_vertical and (mesh_extents[0] * mesh_extents[1] * mesh_extents[2] < 2.0):
            # Complex logic for windows vs doors (size/position)
            if rel_z > 0.2 and rel_z < 0.8:
                label = "window"
                confidence = 0.7
            else:
                label = "door"
                confidence = 0.6

        return {
            "label": label,
            "confidence": min(confidence, 1.0),
            "features": {
                "rel_z": float(rel_z),
                "avg_normal": avg_normal.tolist(),
                "extents": mesh_extents.tolist()
            }
        }

if __name__ == "__main__":
    # Test stub
    import sys
    if len(sys.argv) > 1:
        analyzer = GeometryAnalyzer()
        results = analyzer.analyze_scene(sys.argv[1])
        for r in results:
            print(f"Mesh {r['mesh_id']}: {r['label']} ({r['confidence']:.2f})")
