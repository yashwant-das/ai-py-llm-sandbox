# GenAI LLM Sandbox

Practical, low-code tutorials for learning core OpenAI-style model capabilities.

This repo is optimized for:
- Fast learning
- Interview revision
- Self-contained scripts
- Beginner-to-semi-advanced progression

## What This Repo Covers

1. LLM fundamentals (first call, tokens, temperature, streaming)
2. Prompting essentials (zero-shot, few-shot, structured output, chaining)
3. Tool calling (function calling)
4. Embeddings and basic RAG
5. Safety basics
6. Multimodal basics (vision + optional image generation)
7. Local inference with Ollama

## Setup

```bash
uv sync
cp .env.example .env
# edit .env for your provider
uv run python src/genai_playground/setup/verify_setup.py
```

## Recommended Models By Use Case

| Use Case | OpenAI | NVIDIA | Ollama / Local |
|---|---|---|---|
| General chat + prompting | `gpt-4o-mini` | `meta/llama-3.1-8b-instruct` | `llama3.1:8b` |
| Function calling | `gpt-4o-mini` | `meta/llama-3.1-8b-instruct` | model-dependent |
| Vision | `gpt-4o-mini` | `meta/llama-3.2-11b-vision-instruct` | model-dependent |
| Embeddings | `text-embedding-3-small` | `nvidia/llama-3.2-nemoretriever-300m-embed-v2` | `nomic-embed-text` |
| Image generation | `gpt-image-1` | `stabilityai/stable-diffusion-xl`* | model-dependent |

\* Availability depends on your NVIDIA account/model catalog.

## Learning Path

### 01 Fundamentals

```bash
uv run python src/genai_playground/fundamentals/model_basics.py
uv run python src/genai_playground/fundamentals/token_counting.py
uv run python src/genai_playground/fundamentals/temperature_sampling.py
uv run python src/genai_playground/fundamentals/streaming_responses.py
```

### 02 Prompting

```bash
uv run python src/genai_playground/prompting/zero_shot.py
uv run python src/genai_playground/prompting/few_shot.py
uv run python src/genai_playground/prompting/structured_output.py
uv run python src/genai_playground/prompting/prompt_chaining.py
```

### 03 Tools and Agents (Minimal)

```bash
uv run python src/genai_playground/tools_agents/function_calling.py
```

### 04 Embeddings and RAG

```bash
uv run python src/genai_playground/rag_embeddings/embeddings_basics.py
uv run python src/genai_playground/rag_embeddings/basic_rag.py
```

### 05 Safety

```bash
uv run python src/genai_playground/safety/safety_demo.py
```

### 06 Multimodal

```bash
# requires VISION_IMAGE_PATH in .env
uv run python src/genai_playground/multimodal/vision_basics.py

# OpenAI-compatible image generation (provider-dependent support)
uv run python src/genai_playground/multimodal/image_generation.py
```

### 07 Local Inference

```bash
ollama serve
ollama pull llama3.1:8b
uv run python src/genai_playground/local_inference/ollama_demo.py
```

## Design Rules Used In This Repo

- Every script is runnable on its own.
- No framework-heavy abstractions.
- Short examples over feature-complete systems.
- Interview-ready patterns first, production concerns later.

## License

MIT. See `LICENSE`.
