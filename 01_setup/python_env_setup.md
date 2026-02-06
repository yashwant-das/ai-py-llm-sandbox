# Python Environment Setup

## Recommended Python Version

- **Python 3.10+** (3.11 recommended for best compatibility)

## Virtual Environment

### Using uv (Recommended - Fast & Modern)

```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create environment and install dependencies
uv sync

# Install all optional dependencies
uv sync --all-extras

# Install specific topic dependencies
uv sync --extra image       # For Topic 10 (Image Generation)
uv sync --extra vector      # For Topic 9, 16 (Vector Search)
uv sync --extra huggingface # For Topic 17 (Hugging Face)
```

### Using venv (Standard)

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows PowerShell)
venv\Scripts\Activate.ps1

# Activate (Windows CMD)
venv\Scripts\activate.bat

# Install uv and use it for dependency management
pip install uv
uv sync
```

### Using conda

```bash
# Create environment
conda create -n genai python=3.11

# Activate
conda activate genai

# Install uv and use it for dependency management
pip install uv
uv sync
```

## Verify Installation

```bash
# Run verification script
uv run python 01_setup/verify_setup.py

# Or manually check
uv run python -c "import langchain; print(f'LangChain: {langchain.__version__}')"
uv run python -c "import pydantic; print(f'Pydantic: {pydantic.__version__}')"
```

## Deactivating

```bash
deactivate  # for venv
conda deactivate  # for conda
```

## Running Scripts

```bash
# Use uv run to execute scripts with the correct environment
uv run python 05_prompt_engineering_fundamentals/code/01_zero_shot.py
uv run python 10_image_generation/api_integrations/nvidia_image_gen.py
```

For more details, see [`UV_SETUP.md`](../../UV_SETUP.md)
