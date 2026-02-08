"""Function calling with one local tool.

Recommended models (tool calling support):
- OpenAI: gpt-4o-mini
- NVIDIA: meta/llama-3.1-8b-instruct
- Ollama: model-dependent support via OpenAI-compatible server
"""

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


def multiply(a: float, b: float) -> float:
    return a * b


def as_float(value: object) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).replace(",", "").strip()
    return float(text)


def main() -> int:
    tools = [
        {
            "type": "function",
            "function": {
                "name": "multiply",
                "description": "Multiply two numbers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {"type": "number"},
                        "b": {"type": "number"},
                    },
                    "required": ["a", "b"],
                },
            },
        }
    ]

    messages = [
        {"role": "system", "content": "Return only the final answer. Do not include reasoning text."},
        {"role": "user", "content": "What is 19 * 7?"},
    ]

    try:
        first = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools,
            tool_choice="auto",
            temperature=0,
        )
    except Exception as exc:
        print(f"Tool-calling request failed for model '{MODEL}': {exc}")
        print("Try a tool-capable model (for example gpt-4o-mini).")
        return 0

    msg = first.choices[0].message
    messages.append(msg)

    if msg.tool_calls:
        for call in msg.tool_calls:
            name = call.function.name
            args = json.loads(call.function.arguments or "{}")
            if name == "multiply":
                result = str(multiply(as_float(args.get("a", 0)), as_float(args.get("b", 0))))
            else:
                result = "unsupported tool"
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "name": name,
                    "content": result,
                }
            )

    second = client.chat.completions.create(model=MODEL, messages=messages, temperature=0)
    print(second.choices[0].message.content)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
