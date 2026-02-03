# Topic 1: Course Setup & Development Environment

> Configure your environment for local LLM development with LM Studio and optional cloud APIs.

## Learning Objectives

By the end of this topic, you will:
- Set up Python environment with required dependencies
- Configure LM Studio for local LLM inference
- Understand environment variable management
- Verify connectivity to LLM endpoints

## Folder Structure

```
01_setup/
├── README.md                    # This file
├── python_env_setup.md          # Virtual environment guide
├── lm_studio_guide.md           # LM Studio configuration
├── docker/                      # Optional containerized setup
│   ├── Dockerfile.dev
│   └── docker-compose.yml
└── verify_setup.py              # Connectivity test script
```

## Quick Setup

### 1. Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. LM Studio Setup

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

### 3. Environment Configuration

```bash
# Copy template
cp .env.example .env

# Edit .env with your settings
cat .env
```

Key settings in `.env`:
```
LMSTUDIO_BASE_URL=http://127.0.0.1:1234/v1
LMSTUDIO_API_KEY=lm-studio
DEFAULT_MODEL=openai/gpt-oss-20b
```

### 4. Verify Setup

```bash
python 01_setup/verify_setup.py
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
| `Connection refused` | Ensure LM Studio server is running on port 1234 |
| `Model not found` | Check model ID matches loaded model |
| `Out of memory` | Use smaller model (8B instead of 20B) |
| `Import errors` | Re-run `pip install -r requirements.txt` |

## Next Steps

Proceed to [02_genai_fundamentals/](../02_genai_fundamentals/) to understand how LLMs work.
