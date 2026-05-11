import os
import logging
import json
from typing import Dict, Any, List
from ai_services.alibaba_adapter import get_alibaba_service

logger = logging.getLogger(__name__)

class StyleExtractor:
    """
    Extracts visual style and mood from reference images using Alibaba Qwen-VL.
    Identifies color palettes, lighting conditions, and architectural style via multimodal analysis.
    """

    def __init__(self, embedding_engine=None):
        # We keep the engine param for compatibility with the router, 
        # but we use AlibabaAIService directly for style analysis.
        self.service = get_alibaba_service()

    def analyze_image(self, image_path: str) -> Dict[str, Any]:
        """
        Performs full analysis of a reference image using Qwen-VL.
        """
        if not os.path.exists(image_path):
            logger.error(f"Image not found: {image_path}")
            return {}

        prompt = """
        Analyze this architectural/design reference image and provide a JSON response with the following fields:
        1. "palette": A list of the top 5 dominant colors as [R, G, B] integer arrays.
        2. "lighting": A dictionary with:
           - "type": (e.g., "sunny", "overcast", "night", "warm", "cinematic")
           - "brightness": (0.0 to 1.0)
           - "contrast": (0.0 to 1.0)
           - "description": A brief description of the lighting mood.
        3. "style_tags": A list of dictionaries with "tag" (string) and "score" (0.0 to 1.0). 
           Identify the architectural style (e.g., Modern, Industrial, Brutalist, Scandinavian).
        4. "materials": A list of main materials identified in the scene (e.g., Concrete, Wood, Glass).

        Respond ONLY with the JSON object.
        """

        response_text = self.service.analyze_image(image_path, prompt)
        
        try:
            # Clean response if it contains markdown code blocks
            clean_json = response_text.strip()
            if clean_json.startswith("```json"):
                clean_json = clean_json[7:-3].strip()
            elif clean_json.startswith("```"):
                clean_json = clean_json[3:-3].strip()
                
            data = json.loads(clean_json)
            
            # Extract tags as strings for the frontend
            raw_tags = data.get("style_tags", [])
            tags_list = []
            style_tags_dicts = []
            
            for t in raw_tags:
                if isinstance(t, dict):
                    tag_name = t.get("tag", str(t))
                    score = t.get("score", 1.0)
                else:
                    tag_name = str(t)
                    score = 1.0
                
                tags_list.append(tag_name)
                style_tags_dicts.append({"tag": tag_name, "score": score})

            # Format palette for CSS compatibility if they are lists
            palette = data.get("palette", [])
            formatted_palette = []
            for color in palette:
                if isinstance(color, list) and len(color) == 3:
                    formatted_palette.append(f"rgb({color[0]},{color[1]},{color[2]})")
                else:
                    formatted_palette.append(str(color))

            return {
                "palette": formatted_palette,
                "lighting": data.get("lighting", {}),
                "tags": tags_list,           # For legacy frontend support (script.js:329)
                "style_tags": style_tags_dicts, # For Pydantic model (ai_design.py:49)
                "materials": data.get("materials", [])
            }
        except Exception as e:
            logger.error(f"Failed to parse Qwen-VL response: {e}")
            logger.debug(f"Raw response: {response_text}")
            # Fallback empty structure
            return {
                "palette": [],
                "lighting": {"type": "unknown", "description": "Failed to analyze"},
                "style_tags": [],
                "materials": []
            }

if __name__ == "__main__":
    # Test stub
    import sys
    logging.basicConfig(level=logging.INFO)
    
    if len(sys.argv) > 1:
        extractor = StyleExtractor()
        data = extractor.analyze_image(sys.argv[1])
        print(json.dumps(data, indent=2))
