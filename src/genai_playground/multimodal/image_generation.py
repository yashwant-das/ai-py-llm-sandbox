"""Image generation via OpenAI-compatible Images API.

Required env vars:
- LLM_BASE_URL
- LLM_API_KEY
- LLM_IMAGE_MODEL
"""

from __future__ import annotations

import base64
import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required env var: {name}")
    return value


BASE_URL = require_env("LLM_BASE_URL")
API_KEY = require_env("LLM_API_KEY")
IMAGE_MODEL = require_env("LLM_IMAGE_MODEL")
OUTPUT_PATH = Path("data/generated/image_gen.png")

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


def generate_image(prompt: str) -> bytes | None:
    try:
        response = client.images.generate(
            model=IMAGE_MODEL,
            prompt=prompt,
            size="1024x1024",
        )
    except Exception as exc:
        print(f"Image generation request failed: {exc}")
        return None

    if not response.data:
        print("No image data returned by provider.")
        return None

    item = response.data[0]

    if getattr(item, "b64_json", None):
        return base64.b64decode(item.b64_json)

    if getattr(item, "url", None):
        try:
            image_response = requests.get(item.url, timeout=30)
            image_response.raise_for_status()
            return image_response.content
        except requests.RequestException as exc:
            print(f"Failed to download image URL: {exc}")
            return None

    print("Provider returned unsupported image format.")
    return None


if __name__ == "__main__":
    image = generate_image("A clean desk setup for coding, natural light, minimal style")
    if image:
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT_PATH.write_bytes(image)
        print(f"Saved: {OUTPUT_PATH}")
