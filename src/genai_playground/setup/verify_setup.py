"""Setup verification for the learning repo.

Run:
    uv run python src/genai_playground/setup/verify_setup.py
"""

from __future__ import annotations

import os
import sys
from importlib import import_module


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

        base_url = os.getenv("LLM_BASE_URL", "https://integrate.api.nvidia.com/v1")
        model = os.getenv("LLM_MODEL_ID", "meta/llama-3.1-8b-instruct")
        api_key = os.getenv("LLM_API_KEY", os.getenv("NVIDIA_API_KEY"))

        if "localhost" in base_url and api_key is None:
            api_key = "ollama"

        print(f"Provider URL: {base_url}")
        print(f"Model: {model}")

        if not api_key and "nvidia" in base_url.lower():
            print("LLM API key missing for NVIDIA provider.")
            return False

        client = OpenAI(base_url=base_url, api_key=api_key or "unused")
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "Reply with: setup-ok"}],
            max_tokens=12,
            temperature=0,
        )
        text = (response.choices[0].message.content or "").strip().lower()
        success = "setup-ok" in text
        print(f"Connection test: {'OK' if success else 'FAILED'}")
        if not success:
            print(f"Raw response: {text}")
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
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
