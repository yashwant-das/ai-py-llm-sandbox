"""Vision chat with a local image file.

Recommended vision models:
- OpenAI: gpt-4o-mini
- NVIDIA: meta/llama-3.2-90b-vision-instruct
"""

from __future__ import annotations

import base64
import mimetypes
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = os.getenv("LLM_VISION_MODEL", "meta/llama-3.2-90b-vision-instruct")
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL", "https://integrate.api.nvidia.com/v1"),
    api_key=os.getenv("LLM_API_KEY", os.getenv("NVIDIA_API_KEY", "unused")),
)

image_path = Path(os.getenv("VISION_IMAGE_PATH", "data/sample.jpg"))
if not image_path.exists():
    raise SystemExit(f"Image not found: {image_path}")

mime = mimetypes.guess_type(str(image_path))[0] or "image/jpeg"
b64 = base64.b64encode(image_path.read_bytes()).decode("utf-8")

resp = client.chat.completions.create(
    model=MODEL,
    messages=[
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
