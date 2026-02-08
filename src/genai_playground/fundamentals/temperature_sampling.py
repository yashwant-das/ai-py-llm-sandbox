"""How temperature changes output variability."""

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

prompt = "Suggest a memorable product name for a study-planning app. Return only one name."
shown_reasoning_note = False


def extract_display_text(message) -> str:
    text = (message.content or "").strip()
    if text:
        return text

    reasoning = getattr(message, "reasoning", None)
    if reasoning:
        compact = " ".join(str(reasoning).split())
        return f"[reasoning-only] {compact[:120]}..."

    return "[empty response]"

for temp in [0.0, 0.3, 0.8]:
    print(f"\nTemperature = {temp}")
    print("-" * 50)
    for run in range(1, 4):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "Return only the final answer. Do not include reasoning text.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=temp,
                max_tokens=200,
            )
            text = extract_display_text(resp.choices[0].message)
            if text.startswith("[reasoning-only]"):
                if not shown_reasoning_note:
                    print(
                        "Note: this model returned reasoning-only output; "
                        "for clean final text use a non-reasoning chat model."
                    )
                    shown_reasoning_note = True
            print(f"Run {run}: {text}")
        except Exception as exc:
            print(f"Run {run}: request failed ({exc})")

print("\nRule of thumb:")
print("- 0.0 to 0.3: factual or deterministic tasks")
print("- 0.6 to 1.0: brainstorming and creativity")
