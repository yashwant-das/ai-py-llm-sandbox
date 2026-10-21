"""Few-shot prompting: teach output pattern with examples."""

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

prompt = """Extract Name | Role from each sentence.

Sentence: Maya leads backend engineering.
Output: Maya | Backend Engineering Lead

Sentence: Ali manages hiring and onboarding.
Output: Ali | Hiring and Onboarding Manager

Sentence: Priya owns product analytics.
Output:"""

try:
    resp = client.chat.completions.create(
        extra_body={"chat_template_kwargs": {"enable_thinking": False}},
        model=MODEL,
        messages=[
            {"role": "system", "content": "Return only the final answer. Do not include reasoning text."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        max_tokens=200,
    )
    print(extract_display_text(resp.choices[0].message))
except Exception as exc:
    print(f"Few-shot demo request failed: {exc}")
