"""
Shared utilities for image generation examples.
"""

from .nvidia_api import NVIDIA_API_KEY, NVIDIA_BASE_URL, generate_image

__all__ = ["generate_image", "NVIDIA_API_KEY", "NVIDIA_BASE_URL"]
