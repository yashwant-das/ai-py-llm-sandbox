"""Prompt chaining: break one task into simple steps."""

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


MODEL = require_env("LLM_MODEL_ID")
client = OpenAI(
    base_url=require_env("LLM_BASE_URL"),
    api_key=require_env("LLM_API_KEY"),
)

note = "Customer says checkout is slow, payment fails on mobile, and error messages are unclear."

def run_step(user_prompt: str, temperature: float, max_tokens: int) -> str:
    try:
        return client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": user_prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        ).choices[0].message.content or ""
    except Exception as exc:
        return f"[request failed: {exc}]"


step1 = run_step(
    f"Extract the 3 distinct issues from this note as bullets: {note}",
    temperature=0,
    max_tokens=120,
)
step2 = run_step(
    f"Prioritize these issues as High/Medium/Low with one line reason each:\n{step1}",
    temperature=0,
    max_tokens=140,
)
step3 = run_step(
    f"Write a concise action plan from this prioritization:\n{step2}",
    temperature=0.2,
    max_tokens=140,
)

print("Step 1: Extract")
print(step1)
print("\nStep 2: Prioritize")
print(step2)
print("\nStep 3: Action Plan")
print(step3)
