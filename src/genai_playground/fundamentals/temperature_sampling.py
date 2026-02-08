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

prompt = "Suggest a memorable product name for a study-planning app."

for temp in [0.0, 0.3, 0.8]:
    print(f"\nTemperature = {temp}")
    print("-" * 50)
    for run in range(1, 4):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=temp,
                max_tokens=30,
            )
            text = (resp.choices[0].message.content or "").strip()
            print(f"Run {run}: {text}")
        except Exception as exc:
            print(f"Run {run}: request failed ({exc})")

print("\nRule of thumb:")
print("- 0.0 to 0.3: factual or deterministic tasks")
print("- 0.6 to 1.0: brainstorming and creativity")
