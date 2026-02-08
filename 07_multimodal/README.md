# 07. Multimodal AI

Working with images and other modalities beyond text.

## Capabilities

1.  **Text-to-Image Generation**: Creating images from descriptions (e.g., Stable Diffusion XL, Flux).
2.  **Vision (Image-to-Text)**: Analyzing images and answering questions about them (e.g., Llama 3.2 Vision, Neva).

## Setup

This module requires extra dependencies:

```bash
uv sync --extra image
```

## Examples

*   **Generate Images**:
    ```bash
    uv run python 07_multimodal/api_integrations/nvidia_image_gen.py
    ```

*   **Analyze Images**:
    ```bash
    uv run python 07_multimodal/api_integrations/nvidia_vision.py
    ```
