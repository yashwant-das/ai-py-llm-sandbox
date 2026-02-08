"""Ollama via OpenAI-compatible /v1 endpoint.

Run first:
    ollama serve
    ollama pull llama3.1:8b
"""

from __future__ import annotations

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"Missing required env var: {name}")
    return value


OLLAMA_BASE_URL = require_env("OLLAMA_BASE_URL").rstrip("/")
OLLAMA_MODEL = require_env("OLLAMA_MODEL_ID")

client = OpenAI(
    base_url=f"{OLLAMA_BASE_URL}/v1",
    api_key=require_env("OLLAMA_API_KEY"),
)

try:
    resp = client.chat.completions.create(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": "Explain in 2 bullets why local inference is useful.",
            }
        ],
        temperature=0.2,
        max_tokens=120,
    )
    print(resp.choices[0].message.content)
except Exception as exc:
    print(f"Connection failed: {exc}")
    print("Check that Ollama is running and model is pulled.")
