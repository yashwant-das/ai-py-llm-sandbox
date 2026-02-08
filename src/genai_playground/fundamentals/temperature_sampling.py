"""How temperature changes output variability."""

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

prompt = "Suggest a memorable product name for a study-planning app."

for temp in [0.0, 0.3, 0.8]:
    print(f"\nTemperature = {temp}")
    print("-" * 50)
    for run in range(1, 4):
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=temp,
            max_tokens=30,
        )
        text = (resp.choices[0].message.content or "").strip()
        print(f"Run {run}: {text}")

print("\nRule of thumb:")
print("- 0.0 to 0.3: factual or deterministic tasks")
print("- 0.6 to 1.0: brainstorming and creativity")
