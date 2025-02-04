"""OpenAI TTS provider implementation."""
import os

import openai
from typing import List, Optional
from ..base import TTSProvider
from ...utils.logger import setup_logger

logger = setup_logger(__name__)

class OpenAITTS(TTSProvider):
    """OpenAI Text-to-Speech provider."""
    
    # Provider-specific SSML tags
    PROVIDER_SSML_TAGS: List[str] = ['break', 'emphasis']
    
    def __init__(self, api_key: Optional[str] = None, model: str = "tts-1-hd"):
        """
        Initialize OpenAI TTS provider.
        
        Args:
            api_key: OpenAI API key. If None, expects OPENAI_API_KEY env variable
            model: Model name to use. Defaults to "tts-1-hd"
        """
        if api_key:
            openai.api_key = api_key
        elif not openai.api_key:
            raise ValueError("OpenAI API key must be provided or set in environment")
        openai.api_base = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
        self.model = model
            
    def get_supported_tags(self) -> List[str]:
        """Get all supported SSML tags including provider-specific ones."""
        return self.PROVIDER_SSML_TAGS
        
    def generate_audio(self, text: str, voice: str, model: str, voice2: str = None) -> bytes:
        """Generate audio using OpenAI API."""
        self.validate_parameters(text, voice, model)
        
        try:
            logger.info("start to generate audio")
            logger.info(f"Generating audio for text: {text}")
            logger.info(f"Using model: {model}")
            logger.info(f"Using voice: {voice}")
            response = openai.audio.speech.create(
                model=model,
                voice=voice,
                input=text
            )
            return response.content
        except Exception as e:
            raise RuntimeError(f"Failed to generate audio: {str(e)}") from e