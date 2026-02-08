"""Ollama via OpenAI-compatible /v1 endpoint.

Run first:
    ollama serve
    ollama pull gpt-oss:20b
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


LLM_BASE_URL = require_env("LLM_BASE_URL").rstrip("/")
LLM_MODEL = require_env("LLM_MODEL_ID")

# Accept either:
# - http://localhost:11434
# - http://localhost:11434/v1
if LLM_BASE_URL.endswith("/v1"):
    api_base_url = LLM_BASE_URL
else:
    api_base_url = f"{LLM_BASE_URL}/v1"

client = OpenAI(
    base_url=api_base_url,
    api_key=require_env("LLM_API_KEY"),
)

try:
    resp = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {
                "role": "system",
                "content": "Return only the final answer. Do not include reasoning text.",
            },
            {
                "role": "user",
                "content": "Explain in 2 bullets why local inference is useful.",
            }
        ],
        temperature=0.2,
        max_tokens=120,
    )
    message = resp.choices[0].message
    text = (message.content or "").strip()
    if text:
        print(text)
    else:
        reasoning = str(getattr(message, "reasoning", "") or "").strip()
        if reasoning:
            compact = " ".join(reasoning.split())
            print(f"[reasoning-only output] {compact[:240]}...")
        else:
            print("[empty response]")
except Exception as exc:
    print(f"Connection failed: {exc}")
    print("Check that Ollama is running and model is pulled.")
