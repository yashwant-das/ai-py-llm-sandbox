# Topic 10: Building Image Generation Applications

> Text-to-image pipelines: prompt engineering for images, local models, and APIs.

## Learning Objectives

By the end of this topic, you will:
- Engineer effective prompts for image generation
- Compare local models vs cloud APIs
- Use LLMs to enhance image prompts
- Build batch generation workflows

## Folder Structure

```
10_image_generation/
├── README.md
├── local_models/
│   └── comfyui_integration.md
├── api_integrations/
│   ├── openai_dalle.py
│   └── stability_ai.py
└── apps/
    ├── prompt_enhancer.py         # LLM → better image prompts
    └── batch_generator.py         # Bulk image creation
```

## Approaches

### Local Models
- Stable Diffusion XL (SDXL)
- FLUX
- ComfyUI workflows

### Cloud APIs
- OpenAI DALL-E 3
- Stability AI
- Midjourney (via API)

### Prompt Engineering for Images
- Subject description
- Style references
- Lighting and composition
- Negative prompts

## Running Examples

```bash
# Prompt enhancement with LLM
python 10_image_generation/apps/prompt_enhancer.py

# Batch generation workflow
python 10_image_generation/apps/batch_generator.py
```

## Cross-References

- **Previous**: [09_search_with_vectors/](../09_search_with_vectors/)
- **Next**: [11_low_code_genai/](../11_low_code_genai/)
