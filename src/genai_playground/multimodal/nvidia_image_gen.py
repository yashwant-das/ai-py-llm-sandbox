"""NVIDIA text-to-image quickstart.

Provider-specific example.
Set NVIDIA_API_KEY in .env.
"""

from __future__ import annotations

import base64
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NVIDIA_API_KEY", os.getenv("LLM_API_KEY"))
OUTPUT_PATH = Path("data/generated/nvidia_image.png")


def generate_image(prompt: str) -> bytes | None:
    if not API_KEY:
        print("Missing NVIDIA_API_KEY (or LLM_API_KEY).")
        return None

    url = "https://ai.api.nvidia.com/v1/genai/stabilityai/stable-diffusion-xl"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload = {
        "text_prompts": [{"text": prompt, "weight": 1}],
        "cfg_scale": 5,
        "sampler": "K_EULER_ANCESTRAL",
        "steps": 25,
        "seed": 7,
    }

    resp = requests.post(url, headers=headers, json=payload, timeout=90)
    if resp.status_code != 200:
        print(f"API error {resp.status_code}: {resp.text}")
        return None

    body = resp.json()
    if "artifacts" not in body:
        print("Unexpected response format.")
        return None
    return base64.b64decode(body["artifacts"][0]["base64"])


if __name__ == "__main__":
    image = generate_image("A clean desk setup for coding, natural light, minimal style")
    if image:
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_PATH.write_bytes(image)
        print(f"Saved: {OUTPUT_PATH}")
