"""Centralized configuration management.

Uses pydantic-settings for environment variable loading.
Copy .env.example to .env and customize for your setup.
"""

import os
from functools import lru_cache
from typing import Optional

try:
    from pydantic_settings import BaseSettings
except ImportError:
    # Fallback for older pydantic versions
    from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # LM Studio Configuration (Local LLM)
    lmstudio_base_url: str = "http://127.0.0.1:1234/v1"
    lmstudio_api_key: str = "lm-studio"
    default_model: str = "openai/gpt-oss-20b"
    default_temperature: float = 0.1
    
    # Ollama Configuration (Local LLM alternative)
    ollama_base_url: str = "http://localhost:11434/v1"
    ollama_api_key: str = "ollama"
    ollama_default_model: str = "llama3.1"
    
    # OpenAI Configuration (Optional - for cloud models)
    openai_api_key: Optional[str] = None
    openai_base_url: Optional[str] = None  # For OpenAI-compatible APIs
    
    # SerpAPI for search examples
    serpapi_api_key: Optional[str] = None
    
    # Hugging Face (for Topic 17)
    huggingface_token: Optional[str] = None
    
    # Application Settings
    log_level: str = "INFO"
    llm_provider: str = "lmstudio"  # lmstudio, ollama, openai, auto
    project_root: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance.
    
    Returns:
        Settings: Application configuration
    """
    return Settings()


def get_data_path(subpath: str = "") -> str:
    """Get absolute path to data directory.
    
    Args:
        subpath: Optional subdirectory within data/
        
    Returns:
        Absolute path to data directory or subdirectory
    """
    settings = get_settings()
    base_path = os.path.join(settings.project_root, "data")
    if subpath:
        return os.path.join(base_path, subpath)
    return base_path
