# Quick Start Guide - NVIDIA Image Generation

## Setup (5 minutes)

### 1. Get NVIDIA API Key
- Visit: https://build.nvidia.com/
- Sign up for free account
- Get your API key (starts with `nvapi-`)

### 2. Configure Environment
```bash
# Copy example to .env
cp .env.example .env

# Edit .env and add:
NVIDIA_API_KEY=nvapi-your-actual-key-here
```

### 3. Install Dependencies
```bash
# Install image generation dependencies
uv sync --extra image
```

**Note**: All functionality uses NVIDIA's cloud APIs - no local setup required!

## Run Examples

### Example 1: Generate Images (NVIDIA API)
```bash
uv run python 10_image_generation/api_integrations/nvidia_image_gen.py
```
**Output**: 4 images saved to `10_image_generation/output/`
**Requires**: NVIDIA_API_KEY

### Example 2: Analyze Images (NVIDIA API)
```bash
uv run python 10_image_generation/api_integrations/nvidia_vision.py
```
**Note**: Run Example 1 first to have images to analyze
**Requires**: NVIDIA_API_KEY

### Example 3: Enhance Prompts (NVIDIA LLMs)
```bash
uv run python 10_image_generation/apps/prompt_enhancer.py
```
**Output**: Enhanced prompts for better image generation
**Requires**: NVIDIA_API_KEY

### Example 4: Batch Generate (NVIDIA API)
```bash
uv run python 10_image_generation/apps/batch_generator.py
```
**Output**: Multiple images saved to `10_image_generation/output/batch/`
**Requires**: NVIDIA_API_KEY

## File Structure

```
10_image_generation/
├── api_integrations/
│   ├── nvidia_image_gen.py    # Generate images from text
│   └── nvidia_vision.py       # Understand/analyze images
├── apps/
│   ├── prompt_enhancer.py     # Improve prompts with LLMs
│   └── batch_generator.py     # Generate multiple images
└── output/                    # Generated images (created automatically)
```

## Common Issues

### "NVIDIA_API_KEY not found"
- Make sure you copied `.env.example` to `.env`
- Check that the key is in the `.env` file
- Ensure the `.env` file is in the project root

### "API request failed" (NVIDIA)
- Check your internet connection
- Verify your API key is valid
- Check if you have API credits remaining

### "No images found" (vision.py)
- Run `nvidia_image_gen.py` first to generate some images
- Or place your own images in `10_image_generation/output/`

## Tips

1. **Start Simple**: Run `nvidia_image_gen.py` first
2. **Experiment**: Try different prompts and models
3. **Enhance**: Use `prompt_enhancer.py` to improve prompts with NVIDIA LLMs
4. **Batch**: Use `batch_generator.py` for multiple images
5. **Analyze**: Use `nvidia_vision.py` to understand generated images
6. **Compare**: Try different NVIDIA models (Llama, Nemotron, DeepSeek, Gemma)

## Next Steps

- Read the full [README.md](README.md) for detailed information
- Explore different NVIDIA models available to you
- Try combining prompt enhancement with image generation
- Experiment with batch generation for your projects
