# Topic 1: Course Setup & Development Environment

> Configure your environment for local LLM development with LM Studio, Ollama, or optional cloud APIs.

## Learning Objectives

By the end of this topic, you will:
- Set up Python environment with required dependencies
- Configure LM Studio or Ollama for local LLM inference
- Understand environment variable management
- Verify connectivity to LLM endpoints

## Folder Structure

```
01_setup/
├── README.md                    # This file
├── python_env_setup.md          # Virtual environment guide
├── lm_studio_guide.md           # LM Studio configuration
├── ollama_guide.md              # Ollama configuration
├── docker/                      # Optional containerized setup
│   ├── Dockerfile.dev
│   └── docker-compose.yml
└── verify_setup.py              # Connectivity test script
```

## Quick Setup

### 1. Python Environment

```bash
# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

For detailed setup instructions, see [`python_env_setup.md`](python_env_setup.md).

### 2. Local LLM Setup

Choose **one** of the following:

#### Option A: LM Studio (GUI-based)

1. Download from [lmstudio.ai](https://lmstudio.ai/)
2. Load a model (recommendations below)
3. Start the local server on port 1234

**Recommended Models:**
| Model | Size | Use Case |
|-------|------|----------|
| Llama-3.1-8B-Instruct | ~5GB | General purpose, fast |
| Qwen2.5-7B-Instruct | ~5GB | Multilingual, reasoning |
| Mistral-7B-Instruct | ~5GB | Good instruction following |
| openai/gpt-oss-20b | ~13GB | Higher quality, slower |

#### Option B: Ollama (CLI-based)

1. Install from [ollama.com](https://ollama.com/)
2. Pull a model: `ollama pull llama3.1`
3. Server runs automatically at port 11434

**Recommended Models:**
| Model | Size | Use Case |
|-------|------|----------|
| llama3.1 | 4.7GB | General purpose, fast |
| mistral | 4.1GB | Good instruction following |
| qwen2.5 | 4.7GB | Multilingual, reasoning |
| phi3 | 2.3GB | Lightweight, efficient |

### 3. Environment Configuration

```bash
# Copy template
cp .env.example .env

# Edit .env with your settings
cat .env
```

Key settings in `.env` (for LM Studio):
```
LMSTUDIO_BASE_URL=http://127.0.0.1:1234/v1
LMSTUDIO_API_KEY=lm-studio
DEFAULT_MODEL=openai/gpt-oss-20b
```

Or for Ollama:
```
OLLAMA_BASE_URL=http://localhost:11434/v1
OLLAMA_API_KEY=ollama
OLLAMA_DEFAULT_MODEL=llama3.1
```

**Switching Providers in Code:**
All examples use the `LLM_PROVIDER` environment variable to select the provider:
```bash
# Use LM Studio (default)
uv run python 05_prompt_engineering_fundamentals/code/01_zero_shot.py

# Use Ollama
LLM_PROVIDER=ollama uv run python 05_prompt_engineering_fundamentals/code/01_zero_shot.py

# Use OpenAI (requires API key)
LLM_PROVIDER=openai uv run python 05_prompt_engineering_fundamentals/code/01_zero_shot.py

# Auto-detect (tries LM Studio → Ollama → OpenAI)
LLM_PROVIDER=auto uv run python 05_prompt_engineering_fundamentals/code/01_zero_shot.py
```

Or set it permanently in `.env`:
```
LLM_PROVIDER=ollama
```

### 4. Verify Setup

```bash
uv run python 01_setup/verify_setup.py
```

Expected output:
```
✓ Python version: 3.10+
✓ All packages installed
✓ LM Studio server reachable
✓ Model loaded and responding
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `Connection refused` (LM Studio) | Ensure server is running on port 1234 |
| `Connection refused` (Ollama) | Run `ollama serve` or check if service is running |
| `Model not found` | Check model ID matches loaded/pulled model |
| `Out of memory` | Use smaller model (8B instead of 20B, or phi3) |
| `Import errors` | Re-run `uv sync` |
| `Python version error` | Ensure you're using Python 3.10+ |

## Next Steps

Proceed to [02_genai_fundamentals/](../02_genai_fundamentals/) to understand how LLMs work.
