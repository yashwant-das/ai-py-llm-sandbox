# Topic 10: Building Image Generation Applications

> Text-to-image pipelines: prompt engineering for images and vision-language models using NVIDIA APIs.

## Learning Objectives

By the end of this topic, you will:

- Engineer effective prompts for image generation
- Use NVIDIA's cloud APIs for image generation and vision tasks
- Use LLMs to enhance image prompts
- Build batch generation workflows

## Prerequisites

1. **Python 3.10+**
2. **NVIDIA API Key**: Get your free API key from [build.nvidia.com/](https://build.nvidia.com/)
3. **Dependencies**:
   ```bash
   uv sync --extra image
   ```
4. **Environment**: Ensure `NVIDIA_API_KEY` is in your `.env`.

## Folder Structure

```
10_image_generation/
├── README.md
├── shared/
│   └── nvidia_api.py            # Shared API wrapper
├── api_integrations/
│   ├── nvidia_image_gen.py      # NVIDIA image generation & Vision
│   └── nvidia_vision.py         # (Merged/Related functionality)
└── apps/
    ├── prompt_enhancer.py       # LLM → better image prompts
    └── batch_generator.py       # Bulk image creation
```

## Running Examples

### 1. Image Generation & Vision

```bash
# Generate images and analyze them
uv run python 10_image_generation/api_integrations/nvidia_vision.py
```

### 2. Prompt Enhancement

```bash
# Enhance prompts using NVIDIA's LLMs
uv run python 10_image_generation/apps/prompt_enhancer.py
```

## Prompt Engineering for Images

### Key Elements

1. **Subject**: What's in the image
2. **Style**: Artistic style (photorealistic, oil painting, etc.)
3. **Lighting**: How light affects the scene
4. **Composition**: How elements are arranged
5. **Details**: Specific textures, patterns, features

### Negative Prompts

Things to avoid in the image:

- `blurry, low quality, distorted`
- `cartoonish, low resolution`

## Cross-References

- **Previous**: [09_search_with_vectors/](../09_search_with_vectors/)
- **Next**: [11_low_code_genai/](../11_low_code_genai/)
