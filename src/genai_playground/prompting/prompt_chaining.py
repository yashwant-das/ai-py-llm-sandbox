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

note = "Customer says checkout is slow, payment fails on mobile, and error messages are unclear."

def run_step(user_prompt: str, temperature: float, max_tokens: int) -> str:
    try:
        message = client.chat.completions.create(
            extra_body={"chat_template_kwargs": {"enable_thinking": False}},
            model=MODEL,
            messages=[
                {"role": "system", "content": "Return only the final answer. Do not include reasoning text."},
                {"role": "user", "content": user_prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        ).choices[0].message
    except Exception as exc:
        return f"[request failed: {exc}]"

    return extract_display_text(message)


step1 = run_step(
    (
        "Extract exactly 3 distinct issues from this note. "
        "Return exactly 3 bullet points and nothing else.\n"
        f"Note: {note}"
    ),
    temperature=0,
    max_tokens=220,
)
step2 = run_step(
    (
        "Prioritize these issues as High/Medium/Low with one-line reason each. "
        "Return exactly 3 bullet points and nothing else.\n"
        f"Issues:\n{step1}"
    ),
    temperature=0,
    max_tokens=260,
)
step3 = run_step(
    (
        "Write a concise action plan from this prioritization. "
        "Return exactly 3 bullet points and nothing else.\n"
        f"Prioritization:\n{step2}"
    ),
    temperature=0.2,
    max_tokens=280,
)

print("Step 1: Extract")
print(step1)
print("\nStep 2: Prioritize")
print(step2)
print("\nStep 3: Action Plan")
print(step3)
