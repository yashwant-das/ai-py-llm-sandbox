# 01. Setup & Environment

This module covers the essential setup required to run the experiments in this repository.

## Contents

*   **`verify_setup.py`**: A script to verify your Python environment, API keys, and connection to NVIDIA's API.
*   **`python_env_setup.md`**: Detailed instructions on setting up Python and UV.

## Usage

1.  **Configure Environment**:
    Ensure you have a `.env` file in the root directory with your `NVIDIA_API_KEY`.
    
    ```bash
    cp .env.example .env
    # Edit .env
    ```

2.  **Verify Configuration**:
    Run the verification script to check everything is working.

    ```bash
    uv run python 01_setup/verify_setup.py
    ```

## Troubleshooting

*   **API Key Error**: Ensure your key starts with `nvapi-`.
*   **Module Not Found**: Make sure you ran `uv sync` in the root directory.
