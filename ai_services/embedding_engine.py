import os
import logging
import json
from pathlib import Path
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
        self._material_cache = {} # Cache for catalog embeddings: {mat_id: vector}
        
        # Define cache path
        self.cache_path = Path(settings.upload_dir).parent / "catalog" / "embeddings_cache.json"
        self._load_cache()
        
        logger.info(f"EmbeddingEngine initialized with Alibaba API ({self.model_name})")

    def _load_cache(self):
        """Loads embeddings from persistent disk cache."""
        if self.cache_path.exists():
            try:
                with open(self.cache_path, "r") as f:
                    data = json.load(f)
                    # Convert lists back to numpy arrays
                    self._material_cache = {k: np.array(v) for k, v in data.items()}
                logger.info(f"Loaded {len(self._material_cache)} embeddings from cache.")
            except Exception as e:
                logger.error(f"Failed to load embedding cache: {e}")

    def _save_cache(self):
        """Saves current embeddings to disk cache."""
        try:
            self.cache_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.cache_path, "w") as f:
                # Convert numpy arrays to lists for JSON serialization
                data = {k: v.tolist() for k, v in self._material_cache.items()}
                json.dump(data, f)
            logger.info(f"Saved {len(self._material_cache)} embeddings to cache.")
        except Exception as e:
            logger.error(f"Failed to save embedding cache: {e}")

    def get_text_embedding(self, text: str) -> np.ndarray:
        """Returns normalized embedding for text."""
        emb = self.service.get_multimodal_embedding(text=text)
        return np.array(emb) if emb else np.array([])

    def process_catalog_batch(self, materials: List[Dict[str, Any]]):
        """
        Processes entire catalog using batch embedding calls for speed.
        Only processes materials not already in cache.
        """
        to_process = []
        for mat in materials:
            if mat.get("material_id") not in self._material_cache:
                mat_info = f"{mat.get('name', '')} {mat.get('category', '')} {' '.join(mat.get('tags', []))}"
                to_process.append((mat.get("material_id"), mat_info))
        
        if not to_process:
            return

        logger.info(f"Batch processing {len(to_process)} new materials for embeddings...")
        
        # DashScope supports up to 25 texts per batch for text-embedding-v3
        batch_size = 25
        for i in range(0, len(to_process), batch_size):
            batch = to_process[i:i+batch_size]
            batch_ids = [item[0] for item in batch]
            batch_texts = [item[1] for item in batch]
            
            try:
                embeddings = self.service.get_text_embeddings_batch(batch_texts)
                
                if not embeddings:
                    logger.warning(f"Batch {i//batch_size + 1} returned no embeddings.")
                    continue

                for mat_id, emb in zip(batch_ids, embeddings):
                    if emb:
                        self._material_cache[mat_id] = np.array(emb)
                
                # Progress log for large catalogs
                if len(to_process) > 50:
                    logger.info(f"Processed batch {i//batch_size + 1}/{(len(to_process) + batch_size - 1)//batch_size}")
                    
            except Exception as e:
                logger.error(f"Error processing batch {i//batch_size + 1}: {e}")
                # Wait a bit before next batch if it's a rate limit or transient error
                import time
                time.sleep(1)
        
        self._save_cache()

    def _get_material_embedding(self, mat: Dict[str, Any]) -> np.ndarray:
        """Helper to get/cache material embeddings."""
        mat_id = mat.get("material_id")
        if mat_id in self._material_cache:
            return self._material_cache[mat_id]
        
        mat_info = f"{mat.get('name', '')} {mat.get('category', '')} {' '.join(mat.get('tags', []))}"
        emb = self.get_text_embedding(mat_info)
        if emb.size > 0:
            self._material_cache[mat_id] = emb
            self._save_cache() # Save on each new addition
        return emb

    def find_best_matches(self, query_text: str, candidate_materials: List[Dict[str, Any]], top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Ranks materials based on semantic similarity.
        Optimized to use local cache for material embeddings.
        """
        query_emb = self.get_text_embedding(query_text)
        if query_emb.size == 0: return []
        
        results = []

        for mat in candidate_materials:
            mat_emb = self._get_material_embedding(mat)
            
            if mat_emb.size == 0:
                continue

            # Cosine similarity (local dot product - very fast)
            score = np.dot(query_emb, mat_emb) / (np.linalg.norm(query_emb) * np.linalg.norm(mat_emb) + 1e-8)
            
            results.append({
                "material_id": mat.get("material_id"),
                "score": float(score),
                "material": mat
            })

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
