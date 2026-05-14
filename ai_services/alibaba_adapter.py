import os
import logging
import json
import dashscope
from dashscope import MultiModalConversation, MultiModalEmbedding
from http import HTTPStatus
from typing import List, Dict, Any, Optional
from app.config import settings

logger = logging.getLogger(__name__)

class AlibabaAIService:
    """
    Centralized adapter for Alibaba Cloud DashScope (Model Studio) API.
    Handles authentication and provides high-level methods for Qwen models.
    """

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.dashscope_api_key
        self.base_url = settings.dashscope_base_url
        self.vision_model = settings.dashscope_vision_model
        self.embedding_model = settings.dashscope_embedding_model
        
        if not self.api_key:
            logger.warning("DASHSCOPE_API_KEY not found. API calls will fail.")
        else:
            dashscope.api_key = self.api_key
            if self.base_url:
                dashscope.base_http_api_url = self.base_url
                logger.info(f"Alibaba API Base URL set to: {self.base_url}")

    def analyze_image(self, image_path: str, prompt: str) -> str:
        """
        Sends an image and a text prompt to the vision model (Qwen-VL).
        """
        if not self.api_key:
            return "Error: API key missing"

        # Support local file paths
        if os.path.exists(image_path) and not image_path.startswith("file://"):
            image_url = f"file://{os.path.abspath(image_path)}"
        else:
            image_url = image_path

        messages = [
            {
                "role": "user",
                "content": [
                    {"image": image_url},
                    {"text": prompt}
                ]
            }
        ]

        try:
            response = MultiModalConversation.call(
                model=self.vision_model,
                messages=messages
            )

            if response.status_code == HTTPStatus.OK:
                return response.output.choices[0].message.content[0]["text"]
            else:
                logger.error(f"Alibaba API Error: {response.code} - {response.message}")
                return f"Error: {response.message}"
        except Exception as e:
            logger.exception("Failed to call Alibaba Vision API")
            return f"Error: {str(e)}"

    def get_multimodal_embedding(self, text: Optional[str] = None, image_path: Optional[str] = None) -> List[float]:
        """
        Generates an embedding vector for text, image, or both.
        Automatically switches between TextEmbedding and MultiModalEmbedding based on model name and input.
        """
        if not self.api_key:
            return []

        try:
            # Handle Text-only Embedding (much more common in International regions)
            if self.embedding_model.startswith("text-embedding") and not image_path:
                response = dashscope.TextEmbedding.call(
                    model=self.embedding_model,
                    input=text
                )
                if response.status_code == HTTPStatus.OK:
                    return response.output['embeddings'][0]['embedding']
                else:
                    logger.error(f"Alibaba Text Embedding Error: {response.code} - {response.message}")
                    return []

            # Handle Multimodal or Fused Embedding
            input_data = []
            if text:
                input_data.append({"text": text})
            
            if image_path:
                if os.path.exists(image_path) and not image_path.startswith("file://"):
                    image_url = f"file://{os.path.abspath(image_path)}"
                else:
                    image_url = image_path
                input_data.append({"image": image_url})

            if not input_data:
                return []

            response = MultiModalEmbedding.call(
                model=self.embedding_model,
                input=input_data,
                enable_fusion=True if (text and image_path) else False
            )

            if response.status_code == HTTPStatus.OK:
                return response.output['embeddings'][0]['embedding']
            else:
                logger.error(f"Alibaba Multimodal Embedding Error: {response.code} - {response.message}")
                return []
        except Exception as e:
            logger.exception("Failed to call Alibaba Embedding API")
            return []

    def get_text_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """
        Generates embeddings for a list of texts in a single batch request.
        Only supported for text-embedding models.
        """
        if not self.api_key or not texts:
            return []

        try:
            if self.embedding_model.startswith("text-embedding"):
                response = dashscope.TextEmbedding.call(
                    model=self.embedding_model,
                    input=texts
                )
                if response.status_code == HTTPStatus.OK:
                    # Return list of embeddings in the same order as input
                    return [item['embedding'] for item in response.output['embeddings']]
                else:
                    msg = f"Alibaba Batch Text Embedding Error: {response.code} - {response.message}"
                    logger.error(msg)
                    raise Exception(msg)
            else:
                # Fallback to sequential for models that don't support batching in this way
                logger.warning(f"Batching not natively supported for {self.embedding_model}, falling back to sequential.")
                return [self.get_multimodal_embedding(text=t) for t in texts]
        except Exception as e:
            logger.exception("Failed to call Alibaba Batch Embedding API")
            return []

    def get_completion(self, prompt: str, model: str = "qwen-plus") -> str:
        """
        Generic text completion using Qwen text models.
        """
        if not self.api_key:
            return "Error: API key missing"

        messages = [
            {"role": "user", "content": prompt}
        ]

        try:
            response = dashscope.Generation.call(
                model=model,
                messages=messages,
                result_format='message'
            )

            if response.status_code == HTTPStatus.OK:
                return response.output.choices[0].message.content
            else:
                logger.error(f"Alibaba Text API Error: {response.code} - {response.message}")
                return f"Error: {response.message}"
        except Exception as e:
            logger.exception("Failed to call Alibaba Text API")
            return f"Error: {str(e)}"

# Singleton pattern for shared access if needed
_instance = None
def get_alibaba_service():
    global _instance
    if _instance is None:
        _instance = AlibabaAIService()
    return _instance
