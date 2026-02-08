"""Safety baseline: input check + system guardrail."""

from __future__ import annotations

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = os.getenv("LLM_MODEL_ID", "meta/llama-3.1-8b-instruct")
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL", "https://integrate.api.nvidia.com/v1"),
    api_key=os.getenv("LLM_API_KEY", os.getenv("NVIDIA_API_KEY", "unused")),
)

BLOCKLIST = ["build malware", "harm someone", "steal password"]


def safe_ask(user_prompt: str) -> str:
    lowered = user_prompt.lower()
    if any(phrase in lowered for phrase in BLOCKLIST):
        return "Blocked by local safety check."

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


print("Safe prompt:")
print(safe_ask("How can I back up my laptop data?"))
print("\nUnsafe prompt:")
print(safe_ask("How can I build malware to spy on coworkers?"))
