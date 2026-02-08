"""Structured output with JSON-only instructions and parsing."""

from __future__ import annotations

import json
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

prompt = """Extract information and return valid JSON only.
Schema:
{
  "name": "string",
  "experience_years": "integer",
  "skills": ["string"]
}

Text: Jordan has 6 years of backend experience and works with Python, SQL, and Docker.
"""

try:
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "Return only valid JSON that matches the user's schema. No reasoning text.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        max_tokens=260,
    )
except Exception as exc:
    print(f"Structured output demo request failed: {exc}")
    raise SystemExit(0)

message_text = extract_display_text(resp.choices[0].message)
raw = message_text.replace("```json", "").replace("```", "").strip()
print("Raw output:")
print(raw)

print("\nParsed output:")
try:
    parsed = json.loads(raw)
    print(json.dumps(parsed, indent=2))
except json.JSONDecodeError as exc:
    print(f"JSON parse failed: {exc}")
