"""Function calling with one local tool round.

Recommended models (tool calling support):
- OpenAI: gpt-4o-mini
- NVIDIA: meta/llama-3.1-70b-instruct (check account support)
- Ollama: model-dependent support via OpenAI-compatible server
"""

from __future__ import annotations

import json
import os
from datetime import date
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = os.getenv("LLM_MODEL_ID", "meta/llama-3.1-8b-instruct")
client = OpenAI(
    base_url=os.getenv("LLM_BASE_URL", "https://integrate.api.nvidia.com/v1"),
    api_key=os.getenv("LLM_API_KEY", os.getenv("NVIDIA_API_KEY", "unused")),
)


def get_today() -> str:
    return str(date.today())


def multiply(a: float, b: float) -> float:
    return a * b


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_today",
            "description": "Return today's date in YYYY-MM-DD.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
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
    },
]

messages = [
    {
        "role": "user",
        "content": "What is today's date, and what is 19 * 7?",
    }
]

first = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    tools=tools,
    tool_choice="auto",
    temperature=0,
)
msg = first.choices[0].message
messages.append(msg)

if msg.tool_calls:
    for call in msg.tool_calls:
        name = call.function.name
        args = json.loads(call.function.arguments or "{}")
        if name == "get_today":
            result = get_today()
        elif name == "multiply":
            result = str(multiply(args["a"], args["b"]))
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
