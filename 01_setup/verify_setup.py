"""
Setup Verification Script
=========================
Test connectivity to NVIDIA API and verify environment configuration.

Run this after setup to ensure everything is working:
    uv run python 01_setup/verify_setup.py

Checks:
- Python version (3.10+)
- Required packages installed
- NVIDIA API Key configured
- Connection to NVIDIA API
"""

import sys




def check_python_version():
    """Verify Python 3.10+ is installed."""
    print("Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 10:
        print(f"  ✓ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"  ✗ Python {version.major}.{version.minor} (requires 3.10+)")
        return False


def check_packages():
    """Verify required packages are installed."""
    print("\nChecking required packages...")
    required = [
        "openai",
        "pydantic",
        "dotenv",
    ]

    all_ok = True
    for package in required:
        try:
            # Map package names to import names
            import_name = package
            if package == "dotenv":
                import_name = "dotenv"

            __import__(import_name)
            print(f"  ✓ {package}")
        except ImportError:
            print(f"  ✗ {package} (not installed)")
            all_ok = False

    return all_ok


def check_nvidia_connection():
    """Test connection to NVIDIA API."""
    print("\nChecking NVIDIA API connectivity...")

    try:
        import os
        from openai import OpenAI
        from dotenv import load_dotenv
        
        load_dotenv()
        
        api_key = os.getenv("NVIDIA_API_KEY")

        if not api_key or "nvapi" not in api_key:
            print("  ✗ API Key appears missing or invalid (should start with 'nvapi-')")
            print("    Check your .env file.")
            return False

        base_url = "https://integrate.api.nvidia.com/v1"
        model = "meta/llama-3.1-405b-instruct"

        print(f"  Base URL: {base_url}")
        print(f"  Model: {model}")

        # Try to initialize Client
        client = OpenAI(
            base_url=base_url,
            api_key=api_key
        )

        # Simple test prompt
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": "Say 'NVIDIA setup verified!' and nothing else.",
                }
            ],
            max_tokens=20,
        )

        content = response.choices[0].message.content

        if content:
            print("  ✓ NVIDIA API responding")
            print(f"  Response: {content.strip()}")
            return True
        else:
            print("  ✗ Empty response from API")
            return False

    except Exception as e:
        print(f"  ✗ Connection failed: {e}")
        print("\n  Troubleshooting:")
        print("  1. Verify NVIDIA_API_KEY in .env")
        print("  2. Check internet connection")
        print("  3. Ensure you have credits/access at build.nvidia.com")
        return False


def main():
    """Run all verification checks."""
    print("=" * 60)
    print("GenAI Systems Playground - Setup Verification")
    print("=" * 60)

    results = []

    results.append(("Python Version", check_python_version()))
    results.append(("Required Packages", check_packages()))
    results.append(("NVIDIA API Connection", check_nvidia_connection()))

    print("\n" + "=" * 60)
    print("Verification Summary")
    print("=" * 60)

    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"  {status}: {name}")

    all_passed = all(r[1] for r in results)

    if all_passed:
        print("\n🎉 Setup verified! You're ready to start.")
        print("\nNext: Try running an example:")
        print(
            "  uv run python 05_prompt_engineering_fundamentals/code/01_zero_shot.py (Updated needed there too)"
        )
        return 0
    else:
        print("\n⚠️  Some checks failed. Please fix the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
