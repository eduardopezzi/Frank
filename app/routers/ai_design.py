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
        
    try:
        # 1. Base geometric analysis (Heuristics)
        results = get_geometry_analyzer().analyze_scene(str(temp_path))
        
        # 2. LLM Refinement (Semantic enhancement)
        # We send the mesh names and the heuristic guesses to the LLM to refine them
        from ai_services.alibaba_adapter import get_alibaba_service
        llm = get_alibaba_service()
        
        mesh_data_for_llm = []
        for r in results:
            f = r["features"]
            mesh_data_for_llm.append({
                "id": r["mesh_id"],
                "heuristic": r["label"],
                "geometric_profile": {
                    "dimensions": f"{f['width']:.1f}x{f['depth']:.1f}x{f['height']:.1f}m",
                    "area": f"{f['surface_area']:.1f}m2",
                    "slope": f"{f['avg_slope']:.1f}deg",
                    "pos_z": "top" if f["is_at_top"] else ("bottom" if f["is_at_bottom"] else "middle"),
                    "complexity": "complex" if f["normal_variance"] > 0.05 else "flat"
                }
            })
        
        prompt = f"""
        Analyze these 3D meshes for an architectural project. 
        Goal: Categorize each mesh into 'Wall', 'Floor', 'Roof', 'Ceiling', 'Window', 'Door', or 'Furniture'.
        
        Guidelines:
        - 'Roof': High position, sloped, large area.
        - 'Wall': Vertical, large area, often flat.
        - 'Window': Vertical, small to medium area, often repetitive, mid-height.
        - 'Furniture': Complex geometry, varied positions, smaller than structure.
        
        Input Data (Heuristics + Geometry):
        {mesh_data_for_llm}
        
        Return ONLY a JSON array of objects: [{{"mesh_id": "...", "refined_label": "...", "reasoning": "..."}}]
        """
        
        try:
            refinement_raw = llm.get_completion(prompt)
            clean_json = refinement_raw.strip().replace("```json", "").replace("```", "").strip()
            refined_data = json.loads(clean_json)
            
            refinement_map = {item["mesh_id"]: item for item in refined_data if "mesh_id" in item}
            
            for r in results:
                if r["mesh_id"] in refinement_map:
                    item = refinement_map[r["mesh_id"]]
                    r["label"] = item["refined_label"]
                    r["confidence"] = min(r["confidence"] + 0.15, 1.0)
                    # Store reasoning for UI/UX debugging
                    r["features"]["ai_reasoning"] = item.get("reasoning", "")
        except Exception as llm_err:
            logger.error(f"LLM Semantic Inference failed: {llm_err}")

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
    
    for mesh in request.analysis_results:
        # Construct a query based on the semantic label and style
        query = f"{mesh.label} material {style_tags}".strip()
        if not style_tags:
            query = f"{mesh.label} material architectural"
            
        matches = get_embedding_engine().find_best_matches(query, [m.model_dump() for m in all_materials], top_k=1)
        
        if matches:
            suggestions.append(MaterialSuggestion(
                mesh_id=mesh.mesh_id,
                suggested_material_id=matches[0]["material_id"],
                score=matches[0]["score"],
                reason=f"Matched '{mesh.label}' with {style_tags or 'architectural style'}"
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
