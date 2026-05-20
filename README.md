# GenAI LLM Sandbox

A collection of self-contained, runnable Python scripts for learning OpenAI-compatible LLM APIs — from fundamentals through multimodal and local inference.

Each script is independent, uses the `openai` Python SDK directly, and demonstrates one core concept with minimal code.

## Prerequisites

- Python >= 3.10
- `uv` (package manager)
- An OpenAI-compatible API endpoint (OpenAI, NVIDIA, Ollama, LM Studio, etc.)

## Quick Start

```bash
uv sync
cp .env.example .env
# edit .env for your provider
uv run python src/genai_playground/setup/verify_setup.py
```

## Modules

### 01 Fundamentals

| Script | Concept |
|--------|---------|
| `model_basics.py` | First chat completion, message roles, token usage |
| `token_counting.py` | Tokenization with tiktoken, context window budgeting |
| `temperature_sampling.py` | Temperature parameter, output variability |
| `streaming_responses.py` | Streaming vs. non-streaming, time-to-first-token |

### 02 Prompting

| Script | Concept |
|--------|---------|
| `zero_shot.py` | Zero-shot classification |
| `few_shot.py` | In-context learning via examples |
| `structured_output.py` | JSON schema prompting |
| `prompt_chaining.py` | Multi-step task decomposition |

### 03 Tools & Agents

| Script | Concept |
|--------|---------|
| `function_calling.py` | Tool definition, function execution loop |

### 04 Embeddings & RAG

| Script | Concept |
|--------|---------|
| `embeddings_basics.py` | Vector embeddings, cosine similarity |
| `basic_rag.py` | Retrieval-Augmented Generation pipeline |

### 05 Safety

| Script | Concept |
|--------|---------|
| `safety_demo.py` | Input blocklist, system guardrails |

### 06 Multimodal

| Script | Concept |
|--------|---------|
| `vision_basics.py` | Image understanding via base64 data URIs |
| `image_generation.py` | Text-to-image generation |

### 07 Local Inference

| Script | Concept |
|--------|---------|
| `ollama_demo.py` | Connecting to a local Ollama instance |

## Running Scripts

```bash
uv run python src/genai_playground/fundamentals/model_basics.py
uv run python src/genai_playground/prompting/zero_shot.py
uv run python src/genai_playground/tools_agents/function_calling.py
```

See each module directory for all available scripts.

## Recommended Models By Use Case

| Use Case | OpenAI | NVIDIA | Ollama / Local |
|---|---|---|---|
| General chat + prompting | `gpt-4o-mini` | `meta/llama-3.1-8b-instruct` | `llama3.1:8b` |
| Function calling | `gpt-4o-mini` | `meta/llama-3.1-8b-instruct` | model-dependent |
| Vision | `gpt-4o-mini` | `meta/llama-3.2-11b-vision-instruct` | model-dependent |
| Embeddings | `text-embedding-3-small` | `nvidia/llama-3.2-nemoretriever-300m-embed-v2` | `nomic-embed-text` |
| Image generation | `gpt-image-1` | `stabilityai/stable-diffusion-xl`* | model-dependent |

\* Availability depends on your NVIDIA account/model catalog.

## Project Design

- **Self-contained:** Every script runs independently with no shared state.
- **Minimal dependencies:** Only `openai`, `python-dotenv`, `tiktoken`, `requests`.
- **No framework abstractions:** Scripts use the SDK directly — no wrappers, no orchestration layer.
- **Provider-agnostic:** All scripts read `LLM_BASE_URL` and `LLM_API_KEY` from `.env`.

## License

MIT. See [LICENSE](./LICENSE).
