import cv2
import numpy as np
import logging
from typing import Dict, Any, List
from PIL import Image
import os

logger = logging.getLogger(__name__)

class StyleExtractor:
    """
    Extracts visual style and mood from reference images.
    Identifies color palettes, lighting conditions, and architectural style.
    """

    def __init__(self, embedding_engine=None):
        self.engine = embedding_engine

    def analyze_image(self, image_path: str) -> Dict[str, Any]:
        """
        Performs full analysis of a reference image.
        """
        if not os.path.exists(image_path):
            logger.error(f"Image not found: {image_path}")
            return {}

        results = {
            "palette": self.extract_palette(image_path),
            "lighting": self.analyze_lighting(image_path),
            "style_tags": []
        }

        if self.engine:
            results["style_tags"] = self.classify_style(image_path)

        return results

    def extract_palette(self, image_path: str, k: int = 5) -> List[List[int]]:
        """
        Extracts dominant colors using K-Means.
        """
        try:
            img = cv2.imread(image_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = img.reshape((-1, 3))
            img = np.float32(img)

            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
            _, labels, centers = cv2.kmeans(img, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

            centers = np.uint8(centers)
            # Sort by frequency
            counts = np.bincount(labels.flatten())
            sorted_indices = np.argsort(counts)[::-1]
            
            return [centers[i].tolist() for i in sorted_indices]
        except Exception as e:
            logger.error(f"Error extracting palette: {e}")
            return []

    def analyze_lighting(self, image_path: str) -> Dict[str, Any]:
        """
        Analyzes brightness, contrast, and color temperature.
        """
        try:
            img = cv2.imread(image_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            brightness = np.mean(gray)
            contrast = np.std(gray)
            
            # Simple color temp estimation (Blue vs Yellow/Red)
            b, g, r = cv2.split(img)
            avg_b = np.mean(b)
            avg_r = np.mean(r)
            
            # Higher score = cooler (blue), lower = warmer (orange/red)
            temp_score = avg_b / (avg_r + 1e-6)
            
            lighting_type = "overcast"
            if brightness > 180 and contrast > 60: lighting_type = "sunny"
            elif brightness < 80: lighting_type = "night/dark"
            elif temp_score < 0.8: lighting_type = "warm/golden"
            
            return {
                "brightness": float(brightness),
                "contrast": float(contrast),
                "temp_score": float(temp_score),
                "type": lighting_type
            }
        except Exception as e:
            logger.error(f"Error analyzing lighting: {e}")
            return {}

    def classify_style(self, image_path: str) -> List[Dict[str, Any]]:
        """
        Uses EmbeddingEngine to match image against architectural style tags.
        """
        if not self.engine: return []
        
        styles = [
            "modern minimalist architecture",
            "industrial concrete loft",
            "rustic wooden cabin",
            "golden hour sunset lighting",
            "brutalist architecture",
            "scandinavian interior design",
            "cinematic moody render"
        ]
        
        img_emb = self.engine.get_image_embedding(image_path)
        results = []
        
        for style in styles:
            style_emb = self.engine.get_text_embedding(style)
            # Cosine similarity
            score = np.dot(img_emb, style_emb)
            results.append({"tag": style, "score": float(score)})
            
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:3]

if __name__ == "__main__":
    # Test stub
    import sys
    from ai_services.embedding_engine import EmbeddingEngine
    
    if len(sys.argv) > 1:
        engine = EmbeddingEngine()
        extractor = StyleExtractor(engine)
        data = extractor.analyze_image(sys.argv[1])
        print(f"Lighting: {data['lighting']['type']}")
        print(f"Top Style: {data['style_tags'][0]['tag']} (Score: {data['style_tags'][0]['score']:.4f})")
        print(f"Dominant Color: {data['palette'][0]}")
