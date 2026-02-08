"""Zero-shot prompting: instruction only, no examples."""

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


def extract_display_text(message) -> str:
    text = (message.content or "").strip()
    if text:
        return text

    reasoning = str(getattr(message, "reasoning", "") or "").strip()
    if reasoning:
        compact = " ".join(reasoning.split())
        return f"[reasoning-only] {compact[:200]}..."

    return "[empty response]"

MODEL = require_env("LLM_MODEL_ID")
client = OpenAI(
    base_url=require_env("LLM_BASE_URL"),
    api_key=require_env("LLM_API_KEY"),
)

prompt = "Classify sentiment as Positive, Neutral, or Negative: 'The onboarding was fast and clear.'"

resp = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "Return only the final answer. Do not include reasoning text."},
        {"role": "user", "content": prompt},
    ],
    temperature=0,
    max_tokens=120,
)

print("Prompt:")
print(prompt)
print("\nModel output:")
print(extract_display_text(resp.choices[0].message))
