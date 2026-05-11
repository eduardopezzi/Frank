import os
import logging
from typing import List, Dict, Any, Optional
import numpy as np
from ai_services.alibaba_adapter import get_alibaba_service

logger = logging.getLogger(__name__)

class EmbeddingEngine:
    """
    Handles multimodal embeddings for material matching.
    Refactored to use Alibaba Cloud DashScope API instead of local CLIP.
    """

    def __init__(self, model_name: Optional[str] = None):
        from app.config import settings
        self.model_name = model_name or settings.dashscope_embedding_model
        self.service = get_alibaba_service()
        logger.info(f"EmbeddingEngine initialized with Alibaba API ({self.model_name})")

    def get_text_embedding(self, text: str) -> np.ndarray:
        """Returns normalized embedding for text."""
        emb = self.service.get_multimodal_embedding(text=text)
        return np.array(emb) if emb else np.array([])

    def get_image_embedding(self, image_path: str) -> np.ndarray:
        """Returns normalized embedding for an image."""
        emb = self.service.get_multimodal_embedding(image_path=image_path)
        return np.array(emb) if emb else np.array([])

    def find_best_matches(self, query_text: str, candidate_materials: List[Dict[str, Any]], top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Ranks materials based on semantic similarity between query text and material metadata.
        """
        query_emb = self.get_text_embedding(query_text)
        if query_emb.size == 0: return []
        
        results = []

        for mat in candidate_materials:
            # We combine name, category and tags for the match string
            mat_info = f"{mat.get('name', '')} {mat.get('category', '')} {' '.join(mat.get('tags', []))}"
            mat_emb = self.get_text_embedding(mat_info)
            
            if mat_emb.size == 0:
                continue

            # Cosine similarity
            score = np.dot(query_emb, mat_emb) / (np.linalg.norm(query_emb) * np.linalg.norm(mat_emb) + 1e-8)
            
            results.append({
                "material_id": mat.get("material_id"),
                "score": float(score),
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
