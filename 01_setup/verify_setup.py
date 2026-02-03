"""
Setup Verification Script
=========================
Test connectivity to LM Studio and Ollama, verify environment configuration.

Run this after setup to ensure everything is working:
    python 01_setup/verify_setup.py

Checks:
- Python version (3.9+)
- Required packages installed
- LM Studio or Ollama server reachable
- Model responding to queries
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

def check_python_version():
    """Verify Python 3.9+ is installed."""
    print("Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 9:
        print(f"  ✓ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"  ✗ Python {version.major}.{version.minor} (requires 3.9+)")
        return False


def check_packages():
    """Verify required packages are installed."""
    print("\nChecking required packages...")
    required = [
        "langchain",
        "langchain_openai",
        "pydantic",
    ]
    
    all_ok = True
    for package in required:
        try:
            __import__(package)
            print(f"  ✓ {package}")
        except ImportError:
            print(f"  ✗ {package} (not installed)")
            all_ok = False
    
    return all_ok


def check_lmstudio_connection():
    """Test connection to LM Studio server."""
    print("\nChecking LM Studio connectivity...")
    
    try:
        from shared import get_lmstudio_llm, get_settings
        
        settings = get_settings()
        print(f"  Base URL: {settings.lmstudio_base_url}")
        print(f"  Default Model: {settings.default_model}")
        
        # Try to initialize LLM
        llm = get_lmstudio_llm()
        
        # Simple test prompt
        response = llm.invoke("Say 'Setup verified!' and nothing else.")
        
        if "verified" in response.content.lower():
            print(f"  ✓ LM Studio responding")
            print(f"  Response: {response.content.strip()}")
            return True
        else:
            print(f"  ✗ Unexpected response: {response.content[:100]}")
            return False
            
    except Exception as e:
        print(f"  ✗ Connection failed: {e}")
        print("\n  Troubleshooting:")
        print("  1. Ensure LM Studio is running")
        print("  2. Check server is enabled on port 1234")
        print("  3. Verify .env configuration")
        return False


def check_ollama_connection():
    """Test connection to Ollama server."""
    print("\nChecking Ollama connectivity...")
    
    try:
        from shared import get_ollama_llm, get_settings
        
        settings = get_settings()
        print(f"  Base URL: {settings.ollama_base_url}")
        print(f"  Default Model: {settings.ollama_default_model}")
        
        # Try to initialize LLM
        llm = get_ollama_llm()
        
        # Simple test prompt
        response = llm.invoke("Say 'Ollama ready!' and nothing else.")
        
        if "ready" in response.content.lower():
            print(f"  ✓ Ollama responding")
            print(f"  Response: {response.content.strip()}")
            return True
        else:
            print(f"  ✗ Unexpected response: {response.content[:100]}")
            return False
            
    except Exception as e:
        print(f"  ✗ Connection failed: {e}")
        print("\n  Troubleshooting:")
        print("  1. Ensure Ollama is installed: https://ollama.com/")
        print("  2. Run: ollama serve")
        print(f"  3. Pull a model: ollama pull {get_settings().ollama_default_model}")
        print("  4. Verify .env configuration")
        return False


def main():
    """Run all verification checks."""
    print("=" * 60)
    print("GenAI Systems Playground - Setup Verification")
    print("=" * 60)
    
    results = []
    
    results.append(("Python Version", check_python_version()))
    results.append(("Required Packages", check_packages()))
    
    # Check at least one LLM provider
    lmstudio_ok = check_lmstudio_connection()
    ollama_ok = check_ollama_connection()
    
    if lmstudio_ok or ollama_ok:
        results.append(("LLM Provider", True))
    else:
        results.append(("LLM Provider (LM Studio or Ollama)", False))
    
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
        print("  python 05_prompt_engineering_fundamentals/code/01_zero_shot.py")
        return 0
    else:
        print("\n⚠️  Some checks failed. Please fix the issues above.")
        print("\nNote: You need at least one LLM provider configured:")
        print("  - LM Studio: https://lmstudio.ai/")
        print("  - Ollama: https://ollama.com/")
        return 1


if __name__ == "__main__":
    sys.exit(main())
