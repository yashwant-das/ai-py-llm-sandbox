"""Unified LLM provider interface.

Provides consistent initialization for:
- Local LLMs via LM Studio
- OpenAI API (and compatible endpoints)

Usage:
    from shared import get_lmstudio_llm
    
    llm = get_lmstudio_llm(temperature=0.5)
    response = llm.invoke("Hello, world!")
"""

from typing import Optional, Any

from langchain_openai import ChatOpenAI

from shared.config import get_settings


def get_lmstudio_llm(
    model: Optional[str] = None,
    temperature: float = 0.1,
    max_tokens: Optional[int] = None,
    **kwargs: Any
) -> ChatOpenAI:
    """Initialize LLM client for LM Studio (local inference).
    
    Assumes LM Studio is running with server enabled on the configured port.
    
    Args:
        model: Model identifier (e.g., "openai/gpt-oss-20b")
        temperature: Sampling temperature (0.0 = deterministic, 1.0 = creative)
        max_tokens: Maximum tokens to generate
        **kwargs: Additional arguments passed to ChatOpenAI
        
    Returns:
        Configured ChatOpenAI instance pointing to LM Studio
        
    Example:
        >>> llm = get_lmstudio_llm(temperature=0.7)
        >>> response = llm.invoke("Explain quantum computing")
        
    Raises:
        ConnectionError: If LM Studio server is not accessible (at runtime)
    """
    settings = get_settings()
    
    return ChatOpenAI(
        model=model or settings.default_model,
        temperature=temperature,
        max_tokens=max_tokens,
        openai_api_key=settings.lmstudio_api_key,
        openai_api_base=settings.lmstudio_base_url,
        **kwargs
    )


def get_openai_llm(
    model: str = "gpt-4o-mini",
    temperature: float = 0.1,
    max_tokens: Optional[int] = None,
    **kwargs: Any
) -> ChatOpenAI:
    """Initialize LLM client for OpenAI API.
    
    Requires OPENAI_API_KEY to be set in environment or .env file.
    
    Args:
        model: OpenAI model identifier (default: gpt-4o-mini)
        temperature: Sampling temperature
        max_tokens: Maximum tokens to generate
        **kwargs: Additional arguments passed to ChatOpenAI
        
    Returns:
        Configured ChatOpenAI instance for OpenAI API
        
    Example:
        >>> llm = get_openai_llm(model="gpt-4o")
        >>> response = llm.invoke("Write a poem about AI")
        
    Raises:
        ValueError: If OPENAI_API_KEY is not configured
    """
    settings = get_settings()
    
    if not settings.openai_api_key:
        raise ValueError(
            "OPENAI_API_KEY not configured. "
            "Add it to your .env file: OPENAI_API_KEY=sk-..."
        )
    
    return ChatOpenAI(
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        api_key=settings.openai_api_key,
        base_url=settings.openai_base_url or None,
        **kwargs
    )


def get_llm(provider: str = "lmstudio", **kwargs: Any) -> ChatOpenAI:
    """Factory function to get LLM by provider name.
    
    Args:
        provider: "lmstudio", "openai", or "auto" (tries lmstudio first)
        **kwargs: Arguments passed to specific provider function
        
    Returns:
        Configured ChatOpenAI instance
        
    Raises:
        ValueError: If provider is unknown
    """
    provider = provider.lower()
    
    if provider == "lmstudio":
        return get_lmstudio_llm(**kwargs)
    elif provider == "openai":
        return get_openai_llm(**kwargs)
    elif provider == "auto":
        # Try LM Studio first, fall back to OpenAI
        try:
            return get_lmstudio_llm(**kwargs)
        except Exception:
            return get_openai_llm(**kwargs)
    else:
        raise ValueError(f"Unknown provider: {provider}. Use 'lmstudio' or 'openai'.")
