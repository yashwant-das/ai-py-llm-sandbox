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

## Philosophy & Structure

This repository is designed specifically for **rapid learning** and **interview reference**. 

*   **Self-Contained Scripts**: Each file is a complete, runnable lesson. There are no hidden `utils.py` files or complex class hierarchies to untangle. You can read a single file from top to bottom and understand the entire concept.
*   **Flat Directory Structure**: We avoid deep nesting to keep navigation simple. Every topic is one click away.
*   **Minimal Dependencies**: We stick to the essentials (`openai`, `dotenv`, `requests`) to show how things work under the hood, rather than hiding logic behind heavy frameworks.
*   **Platform Agnostic**: Whether you use NVIDIA, Ollama, or OpenAI, the code works the same way.
*   **OpenAI API Standard**: We focus on the industry-standard OpenAI-style API, which is supported by nearly every major LLM provider and inference engine today. Mastering this specific interface is high-leverage knowledge.

## License
MIT License — See [LICENSE](LICENSE) for details.
