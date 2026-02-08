"""Structured output with JSON-only instructions and parsing."""

from __future__ import annotations

import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = os.getenv("LLM_MODEL_ID", "meta/llama-3.1-8b-instruct")
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL", "https://integrate.api.nvidia.com/v1"),
    api_key=os.getenv("LLM_API_KEY", os.getenv("NVIDIA_API_KEY", "unused")),
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

resp = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}],
    temperature=0,
    max_tokens=160,
)
raw = (resp.choices[0].message.content or "").replace("```json", "").replace("```", "").strip()
print("Raw output:")
print(raw)

print("\nParsed output:")
try:
    parsed = json.loads(raw)
    print(json.dumps(parsed, indent=2))
except json.JSONDecodeError as exc:
    print(f"JSON parse failed: {exc}")
