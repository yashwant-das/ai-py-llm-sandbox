"""Unified LLM client for prompt engineering examples.

This module re-exports the shared LLM providers for convenience.
"""

# Re-export from shared utilities
from shared import get_lmstudio_llm, get_openai_llm, get_llm

__all__ = ["get_lmstudio_llm", "get_openai_llm", "get_llm"]
