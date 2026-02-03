# Ollama Setup Guide

> CLI-based local LLM server with simple model management

## Installation

### macOS
```bash
# Using Homebrew
brew install ollama

# Or download from https://ollama.com/download
```

### Linux
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Windows
Download installer from [ollama.com](https://ollama.com/download)

## Pulling Models

```bash
# List available models on your system
ollama list

# Pull a model
ollama pull llama3.1
ollama pull mistral
ollama pull qwen2.5
ollama pull phi3

# Pull a specific size (if available)
ollama pull llama3.1:8b
```

## Running the Server

```bash
# Start the server (runs on port 11434 by default)
ollama serve

# On macOS/Windows, this often runs automatically as a service
# Check if running:
curl http://localhost:11434/api/tags
```

## Quick Test

```bash
# Command line interaction
ollama run llama3.1

# Or test the API
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ollama" \
  -d '{
    "model": "llama3.1",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## Configuration in .env

```bash
# Ollama Configuration
OLLAMA_BASE_URL=http://localhost:11434/v1
OLLAMA_API_KEY=ollama
OLLAMA_DEFAULT_MODEL=llama3.1
```

## Common Commands

| Command | Description |
|---------|-------------|
| `ollama list` | Show installed models |
| `ollama pull <model>` | Download a model |
| `ollama rm <model>` | Remove a model |
| `ollama run <model>` | Interactive chat with model |
| `ollama serve` | Start API server |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `Error: could not connect to server` | Run `ollama serve` |
| `model not found` | Run `ollama pull <model>` first |
| Slow responses | Check available RAM/VRAM |
| Port conflict | Set `OLLAMA_HOST=0.0.0.0:11435` |

## Model Recommendations

| Model | Size | Best For |
|-------|------|----------|
| llama3.1 | 4.7GB | General use, reasoning |
| mistral | 4.1GB | Instruction following |
| qwen2.5 | 4.7GB | Multilingual tasks |
| phi3 | 2.3GB | Limited resources |
| codellama | 3.8GB | Code generation |
