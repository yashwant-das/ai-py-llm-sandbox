# Topic 1: Course Setup & Development Environment

> Configure your environment for Enterprise-grade GenAI development using NVIDIA's API.

## Learning Objectives

By the end of this topic, you will:

- Set up Python environment with required dependencies
- Configure connection to NVIDIA's AI Foundation Models
- Verify connectivity to the API

## Quick Setup

### 1. Python Environment

```bash
# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies (Nvidia/OpenAI SDK support)
uv sync
```

### 2. NVIDIA API Setup

This course uses NVIDIA's managed API which provides access to state-of-the-art open models like Llama 3.1, Mixtral, and Nemotron.

1.  **Get an API Key**:
    - Go to [build.nvidia.com](https://build.nvidia.com/)
    - Sign in or Create an account (free credits available)
    - Generate an API Key

2.  **Configure Environment**:

    ```bash
    # Copy template
    cp .env.example .env
    ```

3.  **Add Key**:
    Open `.env` and paste your key:
    ```bash
    NVIDIA_API_KEY=nvapi-your-key-here
    ```

### 3. Verify Setup

Run the verification script to test your environment and connection:

```bash
uv run python 01_setup/verify_setup.py
```

Expected output:

```
✓ Python version: 3.10+
✓ All packages installed
✓ NVIDIA API responding
```

## Useful Links

- [NVIDIA Build](https://build.nvidia.com/) - Model Catalog
- [OpenAI Python SDK](https://github.com/openai/openai-python) - The client library we use

## Next Steps

Proceed to [05_prompt_engineering_fundamentals/](../05_prompt_engineering_fundamentals/) to start building!
