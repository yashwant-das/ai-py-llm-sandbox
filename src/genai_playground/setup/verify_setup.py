"""Verify dependencies and the configured NVIDIA chat endpoint.

Run:
    uv run python src/genai_playground/setup/verify_setup.py
"""

from __future__ import annotations

import os
import sys
from importlib import import_module

NVIDIA_LEARNING_MODELS = {
    "chat": "nvidia/nemotron-3.5-lightning-30b-a3b",
    "vision": "meta/llama-3.2-11b-vision-instruct",
    "embedding": "nvidia/nemotron-3-embed-1b",
    "image": "black-forest-labs/flux.1-dev",
}


def required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required env var: {name}")
    return value


def check_python() -> bool:
    version = sys.version_info
    ok = version.major == 3 and version.minor >= 10
    print(f"Python: {version.major}.{version.minor}.{version.micro} ({'OK' if ok else 'Needs 3.10+'})")
    return ok


def check_packages() -> bool:
    required = ["openai", "dotenv", "tiktoken", "requests"]
    ok = True
    for name in required:
        try:
            import_module(name)
            print(f"Package: {name} (OK)")
        except ImportError:
            print(f"Package: {name} (MISSING)")
            ok = False
    return ok


def check_llm_connection() -> bool:
    try:
        from dotenv import load_dotenv
        from openai import OpenAI

        load_dotenv()

        base_url = required_env("LLM_BASE_URL")
        model = required_env("LLM_MODEL_ID")
        api_key = required_env("LLM_API_KEY")

        print(f"Provider URL: {base_url}")
        print(f"Model: {model}")

        client = OpenAI(base_url=base_url, api_key=api_key)
        response = client.chat.completions.create(
            extra_body={"chat_template_kwargs": {"enable_thinking": False}},
            model=model,
            messages=[
                {"role": "system", "content": "Return only the final answer. Do not include reasoning text."},
                {"role": "user", "content": "Reply with: setup-ok"},
            ],
            max_tokens=12,
            temperature=0,
        )
        text = (response.choices[0].message.content or "").strip().lower()
        success = text == "setup-ok"
        print(f"Connection test: {'OK' if success else 'FAILED'}")
        if not success:
            print(f"Expected setup-ok; received: {text or '[no final answer]'}")
        return success
    except Exception as exc:
        print(f"Connection test: FAILED ({exc})")
        return False


def main() -> int:
    print("=" * 60)
    print("GenAI Playground Setup Verification")
    print("=" * 60)

    checks = [
        ("Python", check_python()),
        ("Packages", check_packages()),
        ("LLM Connection", check_llm_connection()),
    ]

    print("\nSummary")
    print("-" * 60)
    for name, passed in checks:
        print(f"{name:<20} {'PASS' if passed else 'FAIL'}")

    all_ok = all(passed for _, passed in checks)
    if all_ok:
        print("\nNext:")
        print("uv run python src/genai_playground/fundamentals/model_basics.py")
        print("\nNVIDIA demo models:")
        print(f"- Chat/Prompting: {NVIDIA_LEARNING_MODELS['chat']}")
        print(f"- Vision: {NVIDIA_LEARNING_MODELS['vision']}")
        print(f"- Embeddings: {NVIDIA_LEARNING_MODELS['embedding']}")
        print(f"- Image generation: {NVIDIA_LEARNING_MODELS['image']}")
        return 0
    print("\nNVIDIA demo models:")
    print(f"- LLM_MODEL_ID={NVIDIA_LEARNING_MODELS['chat']}")
    print(f"- LLM_VISION_MODEL={NVIDIA_LEARNING_MODELS['vision']}")
    print(f"- LLM_EMBEDDING_MODEL={NVIDIA_LEARNING_MODELS['embedding']}")
    print(f"- LLM_IMAGE_MODEL={NVIDIA_LEARNING_MODELS['image']}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
