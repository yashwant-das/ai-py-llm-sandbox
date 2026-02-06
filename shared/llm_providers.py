"""Unified LLM provider interface.

Provides consistent initialization for NVIDIA's API using the OpenAI SDK.
This removes the need for LangChain and provides a raw, transparent
interface perfect for interview prep and learning.

Usage:
    from shared import get_nvidia_client

    client = get_nvidia_client()
    response = client.chat.completions.create(
        model="meta/llama-3.1-405b-instruct",
        messages=[{"role": "user", "content": "Hello!"}]
    )
"""

from typing import Optional, Any
from openai import OpenAI

from shared.config import get_settings


def get_nvidia_client(
    api_key: Optional[str] = None, base_url: Optional[str] = None, **kwargs: Any
) -> OpenAI:
    """Initialize OpenAI client for NVIDIA API.

    Args:
        api_key: Optional API key override
        base_url: Optional Base URL override
        **kwargs: Additional arguments passed to OpenAI client

    Returns:
        Configured OpenAI client instance

    Raises:
        ValueError: If NVIDIA_API_KEY is not configured
    """
    settings = get_settings()

    key = api_key or settings.nvidia_api_key
    url = base_url or settings.nvidia_base_url

    if not key:
        raise ValueError(
            "NVIDIA_API_KEY not configured. "
            "Get a key from https://build.nvidia.com/ and add it to .env"
        )

    return OpenAI(api_key=key, base_url=url, **kwargs)


# Function to get the singleton-like client or factory, compatible with old "get_llm" ideas
# but returning the raw client now.
def get_client() -> OpenAI:
    """Convenience alias for get_nvidia_client."""
    return get_nvidia_client()
