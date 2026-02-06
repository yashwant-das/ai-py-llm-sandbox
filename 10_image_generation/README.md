# Topic 10: Building Image Generation Applications

> Text-to-image pipelines: prompt engineering for images, local models, and APIs.

## Learning Objectives

By the end of this topic, you will:
- Engineer effective prompts for image generation
- Use NVIDIA's cloud APIs for image generation and vision tasks
- Use LLMs to enhance image prompts
- Build batch generation workflows
- Understand vision-language models for image analysis

## Prerequisites

1. **Python 3.10+**: This project requires Python 3.10 or higher
2. **NVIDIA API Key**: Get your free API key from [build.nvidia.com](https://build.nvidia.com/)
3. **Python Dependencies**: Install required packages
   ```bash
   uv sync --extra image
   ```
4. **Environment Setup**: Copy `.env.example` to `.env` and add your NVIDIA API key
   ```bash
   cp .env.example .env
   # Edit .env and add: NVIDIA_API_KEY=nvapi-your-key-here
   ```

## Folder Structure

```
10_image_generation/
├── README.md
├── local_models/
│   └── .gitkeep
├── api_integrations/
│   ├── nvidia_image_gen.py      # NVIDIA image generation
│   └── nvidia_vision.py         # NVIDIA vision/understanding
└── apps/
    ├── prompt_enhancer.py       # LLM → better image prompts
    └── batch_generator.py       # Bulk image creation
```

## NVIDIA API Models

### Image Generation
- **Stable Diffusion XL**: `stabilityai/stable-diffusion-xl` (default)
- High-quality text-to-image generation
- 1024x1024 resolution by default

### Vision/Understanding Models
From your available NVIDIA models:
- `nvidia/neva-22b` - General vision understanding
- `nvidia/vila` - Vision-language assistant
- `nvidia/llama-3.1-nemotron-nano-vl-8b-v1` - Small vision model
- `meta/llama-3.2-90b-vision-instruct` - Large vision model

### Prompt Enhancement LLMs
From your available models:
- `meta/llama-3.1-8b-instruct` - Fast, good quality
- `meta/llama-3.1-70b-instruct` - High quality
- `nvidia/llama-3.1-nemotron-70b-instruct` - NVIDIA optimized
- `deepseek-ai/deepseek-v3.2` - Strong reasoning
- `google/gemma-2-27b-it` - Good balance

## Running Examples

### 1. Image Generation
```bash
# Generate single images with NVIDIA API
python 10_image_generation/api_integrations/nvidia_image_gen.py
```

**What it does:**
- Generates 4 example images (landscape, cyberpunk, coffee shop, dragon)
- Saves images to `10_image_generation/output/`
- Demonstrates basic and negative prompts

### 2. Vision/Understanding
```bash
# Analyze images with NVIDIA vision models
python 10_image_generation/api_integrations/nvidia_vision.py
```

**What it does:**
- Describes images in detail
- Answers questions about image content
- Compares different vision models
- Requires images in `10_image_generation/output/` (run image_gen first)

### 3. Prompt Enhancement
```bash
# Enhance prompts using LLMs
python 10_image_generation/apps/prompt_enhancer.py
```

**What it does:**
- Takes simple prompts and enhances them
- Supports different styles (detailed, artistic, photorealistic, cinematic)
- Generates multiple variations of a prompt
- Compares different LLM models

### 4. Batch Generation
```bash
# Generate multiple images at once
python 10_image_generation/apps/batch_generator.py
```

**What it does:**
- Generates multiple images from a list of prompts
- Organizes output with clear filenames
- Handles errors gracefully
- Tracks progress and statistics

## Prompt Engineering for Images

### Key Elements
1. **Subject**: What's in the image
2. **Style**: Artistic style (photorealistic, oil painting, etc.)
3. **Lighting**: How light affects the scene
4. **Composition**: How elements are arranged
5. **Colors**: Color palette and mood
6. **Details**: Specific textures, patterns, features

### Negative Prompts
Things to avoid in the image:
- `blurry, low quality, distorted`
- `cartoonish, low resolution`
- `dark, scary, horror`

### Example Prompts

**Simple:**
```
A cat sitting on a windowsill
```

**Enhanced:**
```
A fluffy orange tabby cat sitting on a wooden windowsill, 
sunlight streaming through lace curtains, cozy afternoon atmosphere, 
warm golden lighting, photorealistic, highly detailed fur texture
```

## Tips for Better Results

1. **Start Simple**: Begin with basic prompts, then enhance
2. **Use Specific Details**: Be specific about colors, lighting, style
3. **Experiment with Models**: Try different NVIDIA models
4. **Use Negative Prompts**: Specify what to avoid
5. **Batch Test**: Generate multiple variations to compare
6. **Enhance with LLMs**: Use prompt_enhancer.py to improve prompts

## Cross-References

- **Previous**: [09_search_with_vectors/](../09_search_with_vectors/)
- **Next**: [11_low_code_genai/](../11_low_code_genai/)
- **Related**: [05_prompt_engineering_fundamentals/](../05_prompt_engineering_fundamentals/) - For prompt techniques
- **Related**: [06_advanced_prompting/](../06_advanced_prompting/) - For advanced prompting strategies
