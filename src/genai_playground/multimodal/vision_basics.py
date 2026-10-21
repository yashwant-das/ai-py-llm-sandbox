"""NVIDIA vision chat with an image file.

NVIDIA-hosted model: meta/llama-3.2-11b-vision-instruct
"""

from __future__ import annotations

import base64
import mimetypes
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required env var: {name}")
    return value


MODEL = require_env("LLM_VISION_MODEL")
client = OpenAI(
    base_url=require_env("LLM_BASE_URL"),
    api_key=require_env("LLM_API_KEY"),
)

image_path_env = os.getenv("VISION_IMAGE_PATH")
if not image_path_env:
    raise SystemExit("Missing required env var: VISION_IMAGE_PATH")

image_path = Path(image_path_env)
if not image_path.exists():
    print(
        f"Image not found: {image_path}. Set VISION_IMAGE_PATH in .env "
        "or place an image at data/sample.jpg."
    )
    raise SystemExit(1)

mime = mimetypes.guess_type(str(image_path))[0] or "image/jpeg"
b64 = base64.b64encode(image_path.read_bytes()).decode("utf-8")

resp = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": "Return only the final answer in concise bullet points. Do not include reasoning text.",
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image in 4 concise bullets."},
                {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}},
            ],
        }
    ],
    max_tokens=220,
)

print(resp.choices[0].message.content)
