import json
import logging
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, HTTPException, UploadFile, File, BackgroundTasks
from pydantic import BaseModel
import os
import uuid
import shutil
from pathlib import Path

from ai_services.embedding_engine import EmbeddingEngine
from ai_services.style_extractor import StyleExtractor
from worker.geometry_analyzer import GeometryAnalyzer
from app.config import settings
from app.services.material_catalog import material_catalog

logger = logging.getLogger(__name__)

router = APIRouter()

# Lazy-loaded engines
_embedding_engine = None
_style_extractor = None
_geometry_analyzer = None

def get_embedding_engine():
    global _embedding_engine
    if _embedding_engine is None:
        _embedding_engine = EmbeddingEngine()
    return _embedding_engine

def get_style_extractor():
    global _style_extractor
    if _style_extractor is None:
        _style_extractor = StyleExtractor(get_embedding_engine())
    return _style_extractor

def get_geometry_analyzer():
    global _geometry_analyzer
    if _geometry_analyzer is None:
        _geometry_analyzer = GeometryAnalyzer()
    return _geometry_analyzer

class MeshAnalysisResult(BaseModel):
    mesh_id: str
    label: str
    confidence: float
    features: Dict[str, Any]

class StyleProfile(BaseModel):
    palette: List[Any]
    lighting: Dict[str, Any]
    tags: Optional[List[str]] = None
    style_tags: List[Dict[str, Any]]

class MaterialSuggestion(BaseModel):
    mesh_id: str
    suggested_material_id: str
    score: float
    reason: str

@router.post("/analyze-scene", response_model=List[MeshAnalysisResult])
async def analyze_scene(file: UploadFile = File(...)):
    """
    Analyzes an uploaded 3D model file for semantic classification of its meshes.
    """
    # Save temp file
    temp_id = str(uuid.uuid4())
    temp_path = Path(settings.upload_dir) / f"analyze_{temp_id}_{file.filename}"
    
    with temp_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    import time
    start_time = time.time()
    
    try:
        # 1. Base geometric analysis (Heuristics)
        geo_start = time.time()
        results = get_geometry_analyzer().analyze_scene(str(temp_path))
        geo_time = time.time() - geo_start
        logger.info(f"Geometric analysis took {geo_time:.2f}s for {len(results)} meshes.")
        
        # 2. LLM Refinement (Semantic enhancement)
        # OPTIMIZATION: Group meshes by name and heuristic to avoid redundant API calls
        unique_profiles = {}
        for r in results:
            # Create a key based on name and heuristic label
            # We strip numbers from the end of the name to group instances (e.g., Wall.001 -> Wall)
            base_name = ''.join([c for c in r["mesh_id"].split('.')[0] if not c.isdigit()]).strip('_')
            key = (base_name, r["label"])
            
            if key not in unique_profiles:
                f = r["features"]
                unique_profiles[key] = {
                    "sample_id": r["mesh_id"],
                    "base_name": base_name,
                    "heuristic": r["label"],
                    "geometric_profile": {
                        "dimensions": f"{f['width']:.1f}x{f['depth']:.1f}x{f['height']:.1f}m",
                        "area": f"{f['surface_area']:.1f}m2",
                        "slope": f"{f['avg_slope']:.1f}deg",
                        "pos_z": "top" if f["is_at_top"] else ("bottom" if f["is_at_bottom"] else "middle"),
                    },
                    "instances": []
                }
            unique_profiles[key]["instances"].append(r["mesh_id"])

        logger.info(f"Grouped {len(results)} meshes into {len(unique_profiles)} unique architectural profiles.")

        from ai_services.alibaba_adapter import get_alibaba_service
        llm = get_alibaba_service()
        
        # Process in batches of 50 unique profiles to avoid token limits
        all_unique_keys = list(unique_profiles.keys())
        batch_size = 50
        
        for i in range(0, len(all_unique_keys), batch_size):
            batch_keys = all_unique_keys[i:i+batch_size]
            batch_data = [unique_profiles[k] for k in batch_keys]
            
            # Remove 'instances' from the data sent to LLM to save tokens
            llm_input = []
            for item in batch_data:
                copy_item = item.copy()
                del copy_item["instances"]
                llm_input.append(copy_item)

            prompt = f"""
            Analyze these architectural mesh profiles (Batch {i//batch_size + 1}). 
            Goal: Categorize into 'Wall', 'Floor', 'Roof', 'Ceiling', 'Window', 'Door', or 'Furniture'.
            
            Input Data:
            {llm_input}
            
            Return ONLY a JSON array: [{{"sample_id": "...", "refined_label": "...", "reasoning": "..."}}]
            """
            
            try:
                refinement_raw = llm.get_completion(prompt)
                
                # Robust JSON extraction: look for the first '[' and last ']'
                start_idx = refinement_raw.find('[')
                end_idx = refinement_raw.rfind(']')
                
                if start_idx != -1 and end_idx != -1:
                    clean_json = refinement_raw[start_idx:end_idx+1]
                    # Fix common LLM trailing comma issue if present
                    clean_json = clean_json.replace(",\n]", "\n]").replace(",]", "]")
                    refined_data = json.loads(clean_json)
                else:
                    logger.warning(f"No JSON array found in LLM response for batch {i//batch_size + 1}")
                    continue
                
                refinement_map = {item["sample_id"]: item for item in refined_data if "sample_id" in item}
                
                # Apply refined labels to all instances in this profile group
                for r in results:
                    # Find which profile this mesh belongs to
                    mesh_base_name = ''.join([c for c in r["mesh_id"].split('.')[0] if not c.isdigit()]).strip('_')
                    mesh_key = (mesh_base_name, r["label"])
                    
                    if mesh_key in batch_keys:
                        sample_id = unique_profiles[mesh_key]["sample_id"]
                        if sample_id in refinement_map:
                            item = refinement_map[sample_id]
                            r["label"] = item["refined_label"]
                            r["confidence"] = min(r["confidence"] + 0.15, 1.0)
                            r["features"]["ai_reasoning"] = item.get("reasoning", "")
            except Exception as llm_err:
                logger.error(f"LLM Semantic Inference failed for batch {i//batch_size + 1}: {llm_err}")
                # Continue to next batch instead of failing entirely
                continue

        total_time = time.time() - start_time
        logger.info(f"Total scene analysis took {total_time:.2f}s")
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Scene analysis failed: {e}")
    finally:
        if temp_path.exists():
            os.remove(temp_path)

class StyleMatchRequest(BaseModel):
    analysis_results: List[MeshAnalysisResult]
    style_profile: Optional[StyleProfile] = None

@router.post("/match-materials", response_model=List[MaterialSuggestion])
async def match_materials(request: StyleMatchRequest):
    """
    Suggests materials from the catalog based on mesh analysis and optional style profile.
    """
    suggestions = []
    all_materials = material_catalog.list_materials()
    
    style_tags = ""
    if request.style_profile:
        # Extract tag names from the list of tag dictionaries
        tags = [t.get("tag", "") if isinstance(t, dict) else str(t) for t in request.style_profile.style_tags]
        style_tags = " ".join(tags)
    
    # OPTIMIZATION: Group meshes by label to match once per type
    label_to_meshes = {}
    for mesh in request.analysis_results:
        if mesh.label not in label_to_meshes:
            label_to_meshes[mesh.label] = []
        label_to_meshes[mesh.label].append(mesh.mesh_id)

    logger.info(f"Matching materials for {len(label_to_meshes)} unique labels (representing {len(request.analysis_results)} meshes)")

    # Material list as plain dicts for the engine
    mat_list = [m.model_dump() for m in all_materials]
    
    # Pre-cache catalog embeddings in a single pass using the optimized batch method
    engine = get_embedding_engine()
    engine.process_catalog_batch(mat_list)

    for label, mesh_ids in label_to_meshes.items():
        # Construct a query based on the semantic label and style
        query = f"{label} material {style_tags}".strip()
        if not style_tags:
            query = f"{label} material architectural"
            
        matches = engine.find_best_matches(query, mat_list, top_k=1)
        
        if matches:
            best_mat = matches[0]
            for m_id in mesh_ids:
                suggestions.append(MaterialSuggestion(
                    mesh_id=m_id,
                    suggested_material_id=best_mat["material_id"],
                    score=best_mat["score"],
                    reason=f"Matched '{label}' with {style_tags or 'architectural style'}"
                ))
            
    return suggestions

@router.post("/analyze-reference", response_model=StyleProfile)
async def analyze_reference(file: UploadFile = File(...)):
    """
    Extracts style and mood from a reference image.
    """
    # Save temp file
    temp_id = str(uuid.uuid4())
    temp_path = Path(settings.upload_dir) / f"ref_{temp_id}_{file.filename}"
    
    with temp_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        profile = get_style_extractor().analyze_image(str(temp_path))
        return profile
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Style extraction failed: {e}")
    finally:
        # Optional: cleanup or keep for future reference
        pass
