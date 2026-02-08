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
uv run python 01_setup/verify_setup.py

# 3. Running Examples
uv run python 04_prompting/01_zero_shot.py
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

## Repository Structure

The repository is organized into a clean, progressive learning path:

### 1. Foundations
*   [`01_setup/`](01_setup/): Environment setup and API configuration.
*   [`02_fundamentals/`](02_fundamentals/): LLM basics, tokens, parameters (temp, top_p).
*   [`03_models/`](03_models/): Understanding model families (Llama, Mistral) and selection.

### 2. Core Skills
*   [`04_prompting/`](04_prompting/): From zero-shot to advanced Chain-of-Thought (CoT).
*   [`05_embeddings_rag/`](05_embeddings_rag/): Vector search and Retrieval Augmented Generation.

### 3. Building Applications
*   [`06_tools_agents/`](06_tools_agents/): Function calling and ReAct agents.
*   [`07_multimodal/`](07_multimodal/): Image generation and vision capabilities.

### 4. Advanced & Local
*   [`08_local_inference/`](08_local_inference/): Running models locally (HuggingFace, Ollama).
*   [`09_safety/`](09_safety/): Core AI safety and ethics concepts.

> **Note:** Older or specific application examples have been moved to `_archive/` to keep the learning path clear.

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
uv run python 02_fundamentals/01_token_counting.py

# prompting
uv run python 04_prompting/01_zero_shot.py

# agents
uv run python 06_tools_agents/01_react_pattern.py

# multimodal
uv run python 07_multimodal/nvidia_vision.py
```

## License
MIT License — See [LICENSE](LICENSE) for details.
