# UV Setup Guide

This guide explains how to use `uv` with the GenAI Systems Playground project.

## Quick Start

### Option 1: Install Core Dependencies Only

```bash
# Install core dependencies (required for most topics)
uv sync
```

### Option 2: Install All Dependencies

```bash
# Install all optional dependencies
uv sync --all-extras
```

### Option 3: Install Specific Topic Dependencies

```bash
# Install dependencies for specific topics
uv sync --extra vector        # For Topic 3, 9, 16 (Vector Search)
uv sync --extra safety        # For Topic 4, 14 (Safety & Security)
uv sync --extra huggingface   # For Topic 17 (Hugging Face Ecosystem)
uv sync --extra finetuning    # For Topic 19 (Fine-Tuning)
uv sync --extra edge          # For Topic 20 (Small Language Models)
uv sync --extra lowcode       # For Topic 11 (Low-Code Frameworks)
uv sync --extra image         # For Topic 10 (Image Generation)
```

### Option 4: Install Multiple Extras

```bash
# Install multiple topic dependencies at once
uv sync --extra vector --extra huggingface --extra image
```

## Running Scripts with UV

```bash
# Run any Python script with uv
uv run python 01_setup/verify_setup.py
uv run python 05_prompt_engineering_fundamentals/code/01_zero_shot.py
uv run python 10_image_generation/api_integrations/nvidia_image_gen.py
```

## Common UV Commands

```bash
# Sync dependencies (install/update)
uv sync

# Add a new dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Remove a dependency
uv remove package-name

# List installed packages
uv pip list

# Update dependencies
uv lock --upgrade-package package-name

# Check for outdated packages
uv pip list --outdated
```

## Topic-Specific Setup

### Topic 10: Image Generation

```bash
# Install image generation dependencies
uv sync --extra image

# Run image generation examples
uv run python 10_image_generation/api_integrations/nvidia_image_gen.py
uv run python 10_image_generation/api_integrations/nvidia_vision.py
uv run python 10_image_generation/apps/prompt_enhancer.py
uv run python 10_image_generation/apps/batch_generator.py
```

### Topic 9 & 16: Vector Search (RAG)

```bash
# Install vector search dependencies
uv sync --extra vector

# Run vector search examples
uv run python 09_search_with_vectors/code/your_script.py
```

### Topic 17: Hugging Face Ecosystem

```bash
# Install Hugging Face dependencies
uv sync --extra huggingface

# Run Hugging Face examples
uv run python 17_huggingface_ecosystem/code/your_script.py
```

### Topic 19: Fine-Tuning

```bash
# Install fine-tuning dependencies
uv sync --extra finetuning

# Run fine-tuning examples
uv run python 19_fine_tuning/code/your_script.py
```

## Virtual Environment

UV automatically manages a virtual environment in `.venv/`:

```bash
# Activate the virtual environment (optional, uv run handles this)
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows

# Deactivate
deactivate
```

## Troubleshooting

### "Module not found" errors

```bash
# Make sure dependencies are installed
uv sync

# Or install specific extras
uv sync --extra <topic-name>
```

### Python version issues

```bash
# Check Python version
uv python list

# Set specific Python version (requires 3.10+)
uv python pin 3.11
```

**Note**: This project requires Python 3.10 or higher due to dependency requirements.

### Dependency conflicts

```bash
# Update lock file
uv lock --upgrade

# Or rebuild from scratch
rm uv.lock
uv sync
```

## Benefits of Using UV

- **Fast**: UV is 10-100x faster than pip
- **Reliable**: Better dependency resolution
- **Simple**: Single command for most operations
- **Modern**: Built for modern Python workflows
- **Standard**: Uses pyproject.toml (PEP 621)

## Next Steps

1. Install core dependencies: `uv sync`
2. Run setup verification: `uv run python 01_setup/verify_setup.py`
3. Install extras for topics you want to explore
4. Run examples with `uv run python <path-to-script>`

For more information about UV, visit: https://github.com/astral-sh/uv
