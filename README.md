# GenAI Systems Playground

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![NVIDIA API](https://img.shields.io/badge/NVIDIA%20API-Powered-green.svg)](https://build.nvidia.com/)

> A practical, hands-on sandbox for learning and experimenting with Generative AI systems — from prompt engineering basics to AI agents and LLMOps.

## Quick Start

```bash
# 1. Clone and setup with UV
uv sync
cp .env.example .env
# Edit .env with your NVIDIA_API_KEY

# 2. Verify setup
uv run python src/genai_playground/setup/verify_setup.py

# 3. Running Examples
uv run python src/genai_playground/prompting/zero_shot.py
```

**For topic-specific dependencies:**

```bash
# Install all optional dependencies
uv sync --all-extras

# Or install specific topic dependencies
uv sync --extra vector      # For RAG & Embeddings
uv sync --extra image       # For Multimodal
uv sync --extra huggingface # For Local Inference
```

See [`UV_SETUP.md`](UV_SETUP.md) for detailed UV instructions.


## Running Examples

### Prerequisites
1.  **NVIDIA API Key**: Free at [build.nvidia.com](https://build.nvidia.com/)
2.  **UV Installed**: `curl -LsSf https://astral.sh/uv/install.sh | sh`

### Setup
```bash
uv sync
cp .env.example .env
# Edit .env and set NVIDIA_API_KEY
```

### Quick Start Commands
```bash
# fundamentals
uv run python src/genai_playground/fundamentals/token_counting.py

# prompting
uv run python src/genai_playground/prompting/zero_shot.py

# agents
uv run python src/genai_playground/agents/react_pattern.py

# multimodal
uv run python src/genai_playground/multimodal/nvidia_vision.py
```

## License
MIT License — See [LICENSE](LICENSE) for details.
