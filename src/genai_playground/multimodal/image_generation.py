"""Generate an image using NVIDIA's dedicated Visual GenAI API."""

from __future__ import annotations

import base64
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required env var: {name}")
    return value


API_KEY = require_env("LLM_API_KEY")
IMAGE_MODEL = require_env("LLM_IMAGE_MODEL")
IMAGE_BASE_URL = os.getenv(
    "LLM_IMAGE_BASE_URL", "https://ai.api.nvidia.com/v1/genai"
).rstrip("/")
OUTPUT_PATH = Path("data/generated/image_gen.png")


def generate_image(prompt: str) -> bytes | None:
    payload = {"height": 1024, "width": 1024, "samples": 1, "seed": 1}
    if IMAGE_MODEL == "stabilityai/stable-diffusion-xl":
        payload.update(
            text_prompts=[{"text": prompt, "weight": 1}], steps=30, cfg_scale=5
        )
    elif IMAGE_MODEL == "black-forest-labs/flux.1-schnell":
        payload.update(prompt=prompt, mode="base", steps=4, cfg_scale=0)
    elif IMAGE_MODEL == "black-forest-labs/flux.1-dev":
        payload.update(prompt=prompt, mode="base", steps=20, cfg_scale=5)
    else:
        print(f"Unsupported NVIDIA image model: {IMAGE_MODEL}")
        return None

    try:
        response = requests.post(
            f"{IMAGE_BASE_URL}/{IMAGE_MODEL}",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Accept": "application/json",
            },
            json=payload,
            timeout=90,
            allow_redirects=False,
        )
        response.raise_for_status()
        if response.status_code != 200:
            raise ValueError(
                f"Image generation has not completed (HTTP {response.status_code})"
            )
        artifact = response.json()["artifacts"][0]
        if artifact.get("finishReason", "SUCCESS") != "SUCCESS":
            raise ValueError(
                f"Image generation did not succeed: {artifact['finishReason']}"
            )
        image = base64.b64decode(artifact["base64"], validate=True)
        if not image.startswith((b"\x89PNG\r\n\x1a\n", b"\xff\xd8\xff")):
            raise ValueError("Provider response is not a PNG or JPEG image")
        return image
    except (
        requests.RequestException,
        ValueError,
        KeyError,
        IndexError,
        TypeError,
    ) as exc:
        print(f"Image generation request failed: {exc}")
        return None


if __name__ == "__main__":
    image = generate_image(
        "A clean desk setup for coding, natural light, minimal style"
    )
    if image is None:
        raise SystemExit(1)
    output = (
        OUTPUT_PATH.with_suffix(".jpg")
        if image.startswith(b"\xff\xd8\xff")
        else OUTPUT_PATH
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(image)
    print(f"Saved: {output}")
