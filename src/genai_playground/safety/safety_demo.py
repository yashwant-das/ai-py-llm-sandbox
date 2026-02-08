"""Safety baseline: input check + system guardrail."""

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

BLOCKLIST = ["build malware", "harm someone", "steal password"]


def safe_ask(user_prompt: str) -> str:
    lowered = user_prompt.lower()
    if any(phrase in lowered for phrase in BLOCKLIST):
        return "Blocked by local safety check."

    try:
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant. Refuse illegal, violent, or unsafe requests "
                        "and offer safer alternatives."
                    ),
                },
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.2,
            max_tokens=180,
        )
        return resp.choices[0].message.content or ""
    except Exception as exc:
        return f"Safety demo request failed: {exc}"


print("Safe prompt:")
print(safe_ask("How can I back up my laptop data?"))
print("\nUnsafe prompt:")
print(safe_ask("How can I build malware to spy on coworkers?"))
