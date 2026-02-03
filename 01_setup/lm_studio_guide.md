# LM Studio Setup Guide

## Installation

1. Download from [lmstudio.ai](https://lmstudio.ai/)
2. Available for macOS, Windows, Linux
3. Free for personal use

## Loading a Model

1. **Download a model:**
   - Go to the "Discover" tab
   - Search for recommended models:
     - `lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF`
     - `Qwen/Qwen2.5-7B-Instruct-GGUF`
     - `microsoft/Phi-3-mini-4k-instruct-GGUF`

2. **Select quantization:**
   - Q4_K_M: Good balance (recommended)
   - Q5_K_M: Higher quality, larger
   - Q8_0: Best quality, largest

## Starting the Server

1. Go to "Developer" tab
2. Click "Start Server"
3. Default port: 1234
4. Verify it's running: http://localhost:1234/v1/models

## Configuration in .env

```bash
LMSTUDIO_BASE_URL=http://127.0.0.1:1234/v1
LMSTUDIO_API_KEY=lm-studio
DEFAULT_MODEL=lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Slow responses | Use smaller model or Q4 quantization |
| Out of VRAM | Close other apps or use smaller model |
| Server won't start | Check port 1234 is not in use |
| Model not found | Ensure model ID matches exactly |
