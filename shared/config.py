"""Centralized configuration management.

Uses pydantic-settings for environment variable loading.
Copy .env.example to .env and customize for your setup.
"""

import os
from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # NVIDIA Configuration (Main Provider)
    nvidia_api_key: Optional[str] = None
    nvidia_base_url: str = "https://integrate.api.nvidia.com/v1"

    # Default Models
    # Llama 3.3 70B Instruct is the current best balance of speed and intelligence
    default_model: str = "meta/llama-3.3-70b-instruct"
    default_temperature: float = 0.5

    # Application Settings
    log_level: str = "INFO"
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
