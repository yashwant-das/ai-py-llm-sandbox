"""Unified LLM provider interface.

Provides consistent initialization for:
- Local LLMs via LM Studio
- Local LLMs via Ollama
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


def get_ollama_llm(
    model: Optional[str] = None,
    temperature: float = 0.1,
    max_tokens: Optional[int] = None,
    **kwargs: Any
) -> ChatOpenAI:
    """Initialize LLM client for Ollama (local inference).
    
    Assumes Ollama is running (`ollama serve` or as a service).
    Uses OpenAI-compatible API endpoint.
    
    Args:
        model: Model identifier (e.g., "llama3.1", "mistral", "qwen2.5")
               Run `ollama list` to see available models
        temperature: Sampling temperature (0.0 = deterministic, 1.0 = creative)
        max_tokens: Maximum tokens to generate
        **kwargs: Additional arguments passed to ChatOpenAI
        
    Returns:
        Configured ChatOpenAI instance pointing to Ollama
        
    Example:
        >>> llm = get_ollama_llm(model="llama3.1", temperature=0.7)
        >>> response = llm.invoke("Explain quantum computing")
        
    Raises:
        ConnectionError: If Ollama server is not accessible (at runtime)
        
    Notes:
        - Install Ollama: https://ollama.com/
        - Pull models: `ollama pull llama3.1`
        - Start server: `ollama serve` (or runs automatically)
        - OpenAI-compatible API at http://localhost:11434/v1
    """
    settings = get_settings()
    
    return ChatOpenAI(
        model=model or settings.ollama_default_model,
        temperature=temperature,
        max_tokens=max_tokens,
        api_key=settings.ollama_api_key,  # Usually "ollama" or empty
        base_url=settings.ollama_base_url,
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
        provider: One of "lmstudio", "ollama", "openai", or "auto" 
                  ("auto" tries lmstudio, then ollama, then openai)
        **kwargs: Arguments passed to specific provider function
        
    Returns:
        Configured ChatOpenAI instance
        
    Raises:
        ValueError: If provider is unknown
    """
    provider = provider.lower()
    
    if provider == "lmstudio":
        return get_lmstudio_llm(**kwargs)
    elif provider == "ollama":
        return get_ollama_llm(**kwargs)
    elif provider == "openai":
        return get_openai_llm(**kwargs)
    elif provider == "auto":
        # Try LM Studio first, then Ollama, then OpenAI
        errors = []
        
        try:
            return get_lmstudio_llm(**kwargs)
        except Exception as e:
            errors.append(f"LM Studio: {e}")
        
        try:
            return get_ollama_llm(**kwargs)
        except Exception as e:
            errors.append(f"Ollama: {e}")
        
        try:
            return get_openai_llm(**kwargs)
        except Exception as e:
            errors.append(f"OpenAI: {e}")
            
        raise ConnectionError(
            f"Could not connect to any LLM provider. Errors: {'; '.join(errors)}"
        )
    else:
        raise ValueError(
            f"Unknown provider: {provider}. "
            f"Use 'lmstudio', 'ollama', 'openai', or 'auto'."
        )
