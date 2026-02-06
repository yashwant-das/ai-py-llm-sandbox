"""
NVIDIA API Shared Functions
============================
Common functions for interacting with NVIDIA's cloud APIs.
"""

import base64
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# NVIDIA API Configuration
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"


def generate_image(
    prompt, model="stabilityai/stable-diffusion-xl", negative_prompt=None
):
    """
    Generate an image from text prompt using NVIDIA API.

    Args:
        prompt: Text description of the image to generate
        model: Model to use (default: stabilityai/stable-diffusion-xl)
        negative_prompt: Things to avoid in the image (optional)

    Returns:
        Image data (bytes) or None if failed
    """
    if not NVIDIA_API_KEY:
        print("❌ Error: NVIDIA_API_KEY not found in .env file")
        print("   Get your API key from: https://build.nvidia.com/")
        return None

    # API endpoint for image generation
    url = f"{NVIDIA_BASE_URL}/images/generations"

    # Request headers
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json",
    }

    # Request body
    payload = {
        "model": model,
        "prompt": prompt,
        "num_inference_steps": 50,
        "guidance_scale": 7.5,
        "width": 1024,
        "height": 1024,
        "num_images": 1,
    }

    if negative_prompt:
        payload["negative_prompt"] = negative_prompt

    try:
        # Make API request
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()

        # Parse response
        result = response.json()

        # Get image data (base64 encoded)
        if "data" in result and len(result["data"]) > 0:
            image_data = base64.b64decode(result["data"][0]["b64_json"])
            return image_data
        else:
            return None

    except Exception as e:
        print(f"   ❌ Error: {e}")
        return None
