import cv2
import numpy as np
import os
from PIL import Image
from skimage import exposure
from pathlib import Path

class PBRGenerator:
    @staticmethod
    def generate_maps(input_path: str, output_dir: str, base_filename: str):
        """
        Generates Albedo, Normal, Roughness, and Height maps from a single image.
        Adapted from user's suggested CV2 logic.
        """
        # 1. LOAD IMAGE
        img = cv2.imread(input_path)
        if img is None:
            raise ValueError(f"Could not read image at {input_path}")
            
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_float = img.astype(np.float32) / 255.0

        # 2. REMOVE LIGHTING (Delighting)
        # Heavy blur represents the average lighting across the surface
        blur = cv2.GaussianBlur(img_float, (101, 101), 0)
        albedo = img_float / (blur + 1e-5)
        albedo = np.clip(albedo, 0, 1)

        # 3. HEIGHT MAP (Grayscale + CLAHE)
        gray = cv2.cvtColor((albedo * 255).astype(np.uint8), cv2.COLOR_RGB2GRAY)
        height = gray.astype(np.float32) / 255.0
        
        # Improve contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization)
        height = exposure.equalize_adapthist(height)

        # 4. NORMAL MAP
        normal = PBRGenerator._height_to_normal(height, strength=2.0)

        # 5. ROUGHNESS MAP
        # Heuristic: inverted contrast (lighter areas are rougher, darker are smoother)
        roughness = 1.0 - height
        roughness = cv2.GaussianBlur(roughness, (9, 9), 0)
        roughness = np.clip(roughness, 0, 1)

        # 6. SAVE MAPS
        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)

        results = {
            "albedo": f"{base_filename}_albedo.jpg",
            "normal": f"{base_filename}_normal.jpg",
            "roughness": f"{base_filename}_roughness.jpg",
            "height": f"{base_filename}_height.jpg"
        }

        def save_img(filename, data, is_gray=False):
            data_uint8 = np.clip(data * 255, 0, 255).astype(np.uint8)
            if is_gray:
                Image.fromarray(data_uint8).save(out_path / filename)
            else:
                Image.fromarray(data_uint8).save(out_path / filename)

        save_img(results["albedo"], albedo)
        save_img(results["normal"], normal)
        save_img(results["roughness"], roughness, is_gray=True)
        save_img(results["height"], height, is_gray=True)

        return results

    @staticmethod
    def _height_to_normal(height, strength=2.0):
        # Sobel filters for gradients
        sobelx = cv2.Sobel(height, cv2.CV_32F, 1, 0, ksize=5)
        sobely = cv2.Sobel(height, cv2.CV_32F, 0, 1, ksize=5)

        normal = np.zeros((height.shape[0], height.shape[1], 3), dtype=np.float32)
        # Vector (x, y, z)
        normal[..., 0] = -sobelx * strength
        normal[..., 1] = -sobely * strength
        normal[..., 2] = 1.0

        # Normalize
        norm = np.linalg.norm(normal, axis=2, keepdims=True)
        normal /= (norm + 1e-8)

        # Transform from [-1, 1] to [0, 1] for image storage
        normal = (normal * 0.5 + 0.5)
        return normal
