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

# Initialize AI engines
# Note: In production, these should be managed as singletons or injected
embedding_engine = EmbeddingEngine()
style_extractor = StyleExtractor(embedding_engine)
geometry_analyzer = GeometryAnalyzer()

class MeshAnalysisResult(BaseModel):
    mesh_id: str
    label: str
    confidence: float
    features: Dict[str, Any]

class StyleProfile(BaseModel):
    palette: List[List[int]]
    lighting: Dict[str, Any]
    style_tags: List[Dict[str, Any]]

class MaterialSuggestion(BaseModel):
    mesh_id: str
    suggested_material_id: str
    score: float
    reason: str

@router.post("/analyze-scene", response_model=List[MeshAnalysisResult])
async def analyze_scene(file_path: str):
    """
    Analyzes a 3D model file for semantic classification of its meshes.
    """
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Model file not found")
    
    results = geometry_analyzer.analyze_scene(file_path)
    return results

@router.post("/match-materials", response_model=List[MaterialSuggestion])
async def match_materials(analysis_results: List[MeshAnalysisResult]):
    """
    Suggests materials from the catalog based on mesh analysis labels.
    """
    suggestions = []
    all_materials = material_catalog.list_materials()
    
    for mesh in analysis_results:
        # Construct a query based on the semantic label
        # Example: "weathered roof tiles" if label is "roof"
        query = f"{mesh.label} material architectural"
        
        matches = embedding_engine.find_best_matches(query, [m.dict() for m in all_materials], top_k=1)
        
        if matches:
            suggestions.append(MaterialSuggestion(
                mesh_id=mesh.mesh_id,
                suggested_material_id=matches[0]["material_id"],
                score=matches[0]["score"],
                reason=f"Semantic match for detected {mesh.label}"
            ))
            
    return suggestions

@router.post("/analyze-reference", response_model=StyleProfile)
async def analyze_reference(file: UploadFile = File(...)):
    """
    Extracts style and mood from a reference image.
    """
    # Save temp file
    temp_id = str(uuid.uuid4())
    temp_path = Path(settings.UPLOADS_DIR) / f"ref_{temp_id}_{file.filename}"
    
    with temp_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        profile = style_extractor.analyze_image(str(temp_path))
        return profile
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Style extraction failed: {e}")
    finally:
        # Optional: cleanup or keep for future reference
        pass
