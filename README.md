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

# 3. Run your first example
uv run python 05_prompt_engineering_fundamentals/code/01_zero_shot.py
```

**For topic-specific dependencies:**

```bash
# Install all optional dependencies
uv sync --all-extras

# Or install specific topic dependencies
uv sync --extra vector      # For Topic 3, 9, 16 (Vector Search)
uv sync --extra image       # For Topic 10 (Image Generation)
uv sync --extra huggingface # For Topic 17 (Hugging Face)
```

See [`UV_SETUP.md`](UV_SETUP.md) for detailed UV instructions.

## Repository Structure

This repository is organized into 21 progressive topics, from fundamentals to specialized areas:

### Foundation (Topics 1-4)

| Topic | Folder                                             | Description                                 |
| ----- | -------------------------------------------------- | ------------------------------------------- |
| 1     | [`01_setup/`](01_setup/)                           | Development environment, Nvidia API Setup   |
| 2     | [`02_genai_fundamentals/`](02_genai_fundamentals/) | LLM basics, tokens, embeddings, sampling    |
| 3     | [`03_llm_landscape/`](03_llm_landscape/)           | Comparing models, benchmarks, selection     |
| 4     | [`04_ethics_and_safety/`](04_ethics_and_safety/)   | Bias, safety, prompt injection, red teaming |

### Core Skills (Topics 5-6)

| Topic | Folder                                                                       | Description                                   |
| ----- | ---------------------------------------------------------------------------- | --------------------------------------------- |
| 5     | [`05_prompt_engineering_fundamentals/`](05_prompt_engineering_fundamentals/) | Zero-shot, few-shot, role prompting           |
| 6     | [`06_advanced_prompting/`](06_advanced_prompting/)                           | CoT, self-consistency, structured output, ToT |

### Applications (Topics 7-11)

| Topic | Folder                                                 | Description                           |
| ----- | ------------------------------------------------------ | ------------------------------------- |
| 7     | [`07_text_generation_apps/`](07_text_generation_apps/) | Email writers, content expanders      |
| 8     | [`08_chat_applications/`](08_chat_applications/)       | Conversational interfaces with memory |
| 9     | [`09_search_with_vectors/`](09_search_with_vectors/)   | Semantic search, FAISS, Chroma        |
| 10    | [`10_image_generation/`](10_image_generation/)         | Text-to-image, prompt enhancement     |
| 11    | [`11_low_code_genai/`](11_low_code_genai/)             | Gradio, Streamlit, Chainlit           |

### Integration & Systems (Topics 12-16)

| Topic | Folder                                         | Description                                   |
| ----- | ---------------------------------------------- | --------------------------------------------- |
| 12    | [`12_function_calling/`](12_function_calling/) | Tool use, function calling, orchestration     |
| 13    | [`13_ux_for_ai/`](13_ux_for_ai/)               | Streaming, confidence indicators, HITL        |
| 14    | [`14_security/`](14_security/)                 | OWASP LLM, sandboxing, defenses               |
| 15    | [`15_llmops_lifecycle/`](15_llmops_lifecycle/) | Prompt versioning, A/B testing, observability |
| 16    | [`16_rag_systems/`](16_rag_systems/)           | RAG pipelines, chunking, evaluation           |

### Specialized Topics (Topics 17-21)

| Topic | Folder                                                   | Description                                    |
| ----- | -------------------------------------------------------- | ---------------------------------------------- |
| 17    | [`17_huggingface_ecosystem/`](17_huggingface_ecosystem/) | Open-source models, Transformers, quantization |
| 18    | [`18_ai_agents/`](18_ai_agents/)                         | ReAct, Modern Agent Patterns                   |
| 19    | [`19_fine_tuning/`](19_fine_tuning/)                     | LoRA, PEFT, dataset preparation                |
| 20    | [`20_small_language_models/`](20_small_language_models/) | Phi-3, Gemma, edge deployment                  |
| 21    | [`21_mistral_meta_families/`](21_mistral_meta_families/) | Mistral, Mixtral, Llama 3.1                    |

### Shared Infrastructure

| Folder               | Purpose                                        |
| -------------------- | ---------------------------------------------- |
| [`shared/`](shared/) | LLM providers, configuration, common utilities |
| [`data/`](data/)     | Datasets, embeddings cache (gitignored)        |
| [`tests/`](tests/)   | Unit and integration tests                     |

## Design Principles

### Raw SDK First

- **Fundamentals**: Raw OpenAI-style SDK usage for transparency and learning.
- **Nvidia-Powered**: We use NVIDIA's API to access open-weights models (Llama 3, etc.) without local hardware requirements.
- **Framework-Free Core**: We avoid heavy frameworks like LangChain for the core examples to ensure you understand the underlying mechanics.

### Progressive Complexity

```
Topics 1-4:   Foundation (concepts, ethics, setup)
Topics 5-6:   Core Skills (prompt engineering)
Topics 7-11:  Applications (building things)
Topics 12-16: Systems (integration, lifecycle)
Topics 17-21: Specialized (OSS, agents, fine-tuning)
```

## Running Examples

### Prerequisites

1. **NVIDIA API Key**
   - Get one for free at [build.nvidia.com](https://build.nvidia.com/)

2. **Python Environment**

   ```bash
   # Install UV (if not already installed)
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install dependencies (requires Python 3.10+)
   uv sync
   ```

3. **Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env and set NVIDIA_API_KEY
   ```

### Example Commands

```bash
# Prompt Engineering
uv run python 05_prompt_engineering_fundamentals/code/01_zero_shot.py
uv run python 05_prompt_engineering_fundamentals/code/02_few_shot.py

# Advanced Techniques
uv run python 06_advanced_prompting/code/01_chain_of_thought.py
uv run python 06_advanced_prompting/code/04_structured_output.py

# Agents
uv run python 18_ai_agents/fundamentals/01_react_pattern.py

# Image Generation (requires --extra image)
uv run python 10_image_generation/api_integrations/nvidia_vision.py
```

## Key Dependencies

```
openai>=1.0.0             # Core SDK
pydantic-settings>=2.0.0  # Configuration
python-dotenv>=1.0.0      # Env vars
```

See [`pyproject.toml`](pyproject.toml) for complete list with optional dependencies organized by topic.

## Resources

- [Nvidia Build](https://build.nvidia.com/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## License

MIT License — See [LICENSE](LICENSE) for details.
