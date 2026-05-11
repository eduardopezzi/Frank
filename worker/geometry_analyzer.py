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
        Stage 2: Geometric Feature Extraction
        Stage 3 Layer 1: Heuristic-based classification (Geometry Engine)
        """
        # 1. Feature Extraction (Stage 2)
        centroid = mesh.centroid
        min_z = scene_bbox[0][2]
        max_z = scene_bbox[1][2]
        total_height = max_z - min_z
        
        # Extents and Dimensions
        extents = mesh.extents
        width, depth, height = extents[0], extents[1], extents[2]
        surface_area = mesh.area
        
        # Relative height (0 to 1)
        rel_z = (centroid[2] - min_z) / total_height if total_height > 0 else 0
        
        # Slopes and Normals
        face_normals = mesh.face_normals
        # Calculate avg slope (angle with UP vector [0,0,1])
        up_vector = np.array([0, 0, 1])
        # Use dot product to find angle with up vector
        cos_angles = np.clip(np.dot(face_normals, up_vector), -1.0, 1.0)
        angles = np.arccos(cos_angles)
        avg_slope_deg = np.degrees(np.mean(angles))
        
        # Normal variance (to detect complexity vs flat surfaces)
        normal_variance = float(np.var(face_normals, axis=0).mean())
        
        # Spatial Context (simplified)
        is_at_top = rel_z > 0.8
        is_at_bottom = rel_z < 0.2
        is_flat_horizontal = height < 0.1 * max(width, depth)
        is_flat_vertical = width < 0.1 * max(depth, height) or depth < 0.1 * max(width, height)

        # 2. Heuristics (Stage 3 Layer 1: Geometry Engine)
        label = "other"
        confidence = 0.5
        
        if is_at_top and avg_slope_deg > 5 and surface_area > 1.0:
            label = "roof"
            confidence = 0.85
        elif is_at_bottom and is_flat_horizontal and surface_area > 2.0:
            label = "floor"
            confidence = 0.95
        elif is_flat_vertical and height > 1.0:
            label = "wall"
            confidence = 0.8
        elif is_flat_vertical and height < 3.0 and width < 2.0:
            if rel_z > 0.2 and rel_z < 0.8:
                label = "window"
            else:
                label = "door"
            confidence = 0.7

        return {
            "label": label,
            "confidence": min(confidence, 1.0),
            "features": {
                "height": float(height),
                "width": float(width),
                "depth": float(depth),
                "surface_area": float(surface_area),
                "avg_slope": float(avg_slope_deg),
                "normal_variance": normal_variance,
                "rel_z": float(rel_z),
                "is_at_top": bool(is_at_top),
                "is_at_bottom": bool(is_at_bottom)
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
