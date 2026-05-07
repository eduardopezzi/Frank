import os
import logging
from typing import List, Dict, Any, Optional
import numpy as np
from PIL import Image
from sentence_transformers import SentenceTransformer, util

logger = logging.getLogger(__name__)

class EmbeddingEngine:
    """
    Handles multimodal embeddings for material matching.
    Uses CLIP (Contrastive Language-Image Pre-training).
    """

    def __init__(self, model_name: str = "clip-ViT-B-32"):
        self.model_name = model_name
        self.model = None
        self._load_model()

    def _load_model(self):
        try:
            logger.info(f"Loading CLIP model: {self.model_name}...")
            self.model = SentenceTransformer(self.model_name)
            logger.info("Model loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load embedding model: {e}")

    def get_text_embedding(self, text: str) -> np.ndarray:
        """Returns normalized embedding for text."""
        if not self.model: return np.array([])
        return self.model.encode(text, convert_to_numpy=True, normalize_embeddings=True)

    def get_image_embedding(self, image_path: str) -> np.ndarray:
        """Returns normalized embedding for an image."""
        if not self.model: return np.array([])
        try:
            img = Image.open(image_path)
            return self.model.encode(img, convert_to_numpy=True, normalize_embeddings=True)
        except Exception as e:
            logger.error(f"Error encoding image {image_path}: {e}")
            return np.array([])

    def find_best_matches(self, query_text: str, candidate_materials: List[Dict[str, Any]], top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Ranks materials based on semantic similarity between query text and material metadata.
        """
        if not self.model: return []
        
        query_emb = self.get_text_embedding(query_text)
        results = []

        for mat in candidate_materials:
            # We combine name, category and tags for the match string
            mat_info = f"{mat.get('name', '')} {mat.get('category', '')} {' '.join(mat.get('tags', []))}"
            mat_emb = self.get_text_embedding(mat_info)
            
            score = util.cos_sim(query_emb, mat_emb).item()
            results.append({
                "material_id": mat.get("material_id"),
                "score": score,
                "material": mat
            })

        # Sort by score descending
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]

if __name__ == "__main__":
    # Test stub
    logging.basicConfig(level=logging.INFO)
    engine = EmbeddingEngine()
    
    sample_catalog = [
        {"material_id": "red_bricks", "name": "Red Clay Bricks", "category": "wall", "tags": ["rough", "industrial"]},
        {"material_id": "modern_concrete", "name": "Polished Concrete", "category": "floor", "tags": ["grey", "minimalist"]},
        {"material_id": "old_oak", "name": "Weathered Oak Wood", "category": "wood", "tags": ["brown", "vintage"]}
    ]
    
    query = "old wooden beam"
    matches = engine.find_best_matches(query, sample_catalog)
    for m in matches:
        print(f"Match: {m['material_id']} - Score: {m['score']:.4f}")
