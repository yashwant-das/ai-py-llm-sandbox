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
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=160,
    )
except Exception as exc:
    print(f"Structured output demo request failed: {exc}")
    raise SystemExit(0)

raw = (resp.choices[0].message.content or "").replace("```json", "").replace("```", "").strip()
print("Raw output:")
print(raw)

print("\nParsed output:")
try:
    parsed = json.loads(raw)
    print(json.dumps(parsed, indent=2))
except json.JSONDecodeError as exc:
    print(f"JSON parse failed: {exc}")
