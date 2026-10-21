# GenAI LLM Sandbox

Self-contained Python demos for NVIDIA's hosted AI APIs, from chat and prompting to retrieval, vision, and image generation. Each script calls NVIDIA endpoints directly using Python.

## Quick start

You need Python 3.10+, uv, and an NVIDIA API key with access to the selected models.

```bash
uv sync
cp .env.example .env
# Set LLM_API_KEY in .env.
uv run python src/genai_playground/setup/verify_setup.py
```

## Models configured in `.env`

`.env` and `.env.example` have a dedicated models section. The current demo configuration uses these four models, all accessed through NVIDIA-hosted services:

| Environment variable | Model ID | Used for |
|---|---|---|
| `LLM_MODEL_ID` | `nvidia/nemotron-3.5-lightning-30b-a3b` | Setup verification, chat, streaming, temperature sampling, prompting, tool calling, safety, and RAG answers |
| `LLM_VISION_MODEL` | `meta/llama-3.2-11b-vision-instruct` | Image understanding in `vision_basics.py` |
| `LLM_EMBEDDING_MODEL` | `nvidia/nemotron-3-embed-1b` | Document and query vectors in `embeddings_basics.py` and `basic_rag.py` |
| `LLM_IMAGE_MODEL` | `black-forest-labs/flux.1-dev` | Image creation in `image_generation.py` |

The model IDs identify their publishers; NVIDIA hosts every model used by these demos.

| Environment variable | Value | Purpose |
|---|---|---|
| `LLM_BASE_URL` | `https://integrate.api.nvidia.com/v1` | NVIDIA chat, vision, and embedding API |
| `LLM_IMAGE_BASE_URL` | `https://ai.api.nvidia.com/v1/genai` | NVIDIA Visual GenAI image API |
| `LLM_API_KEY` | Your NVIDIA API key | Authentication for both endpoints |
| `VISION_IMAGE_PATH` | `data/sample.png` | Input file for the vision demo |

Keep the real API key in `.env`, which Git ignores. `.env.example` contains a placeholder. Model access and availability depend on NVIDIA and your account.

Chat demos disable thinking with `chat_template_kwargs.enable_thinking=false`, so their short token budgets produce final answers. Vision requests omit that setting. Embedding demos send documents as `passage` and questions as `query`. The image demo decodes NVIDIA's image artifacts and saves a PNG or JPEG under `data/generated/`.

## Demos

| Area | Scripts |
|---|---|
| Setup | `setup/verify_setup.py` |
| Fundamentals | `fundamentals/model_basics.py`, `fundamentals/token_counting.py`, `fundamentals/temperature_sampling.py`, `fundamentals/streaming_responses.py` |
| Prompting | `prompting/zero_shot.py`, `prompting/few_shot.py`, `prompting/structured_output.py`, `prompting/prompt_chaining.py` |
| Tools | `tools_agents/function_calling.py` |
| Retrieval | `rag_embeddings/embeddings_basics.py`, `rag_embeddings/basic_rag.py` |
| Safety | `safety/safety_demo.py` |
| Multimodal | `multimodal/vision_basics.py`, `multimodal/image_generation.py` |

Paths in the table are under `src/genai_playground/`. For example:

```bash
uv run python src/genai_playground/rag_embeddings/basic_rag.py
uv run python src/genai_playground/multimodal/vision_basics.py
uv run python src/genai_playground/multimodal/image_generation.py
```

`data/sample.png` is a synthetic red-and-blue image for testing vision. Replace `VISION_IMAGE_PATH` in `.env` to use your own image.

Token counting uses tiktoken as an offline tokenizer example. It does not measure the NVIDIA models' tokenization; the chat demos' returned usage fields report actual API token usage.

## Tests

The regression tests check NVIDIA request payloads and error handling without calling external services:

```bash
uv run python -m unittest discover -s tests -v
uv run ruff check src tests
```

Running the demos calls NVIDIA's services using the key in `.env`. Dependencies remain locked in `uv.lock`.

## License

MIT. See [LICENSE](./LICENSE).
