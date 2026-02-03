"""Reusable prompt templates and builders.

This module provides helper functions for constructing common prompt patterns.
"""

from typing import List, Dict, Any, Optional


class PromptBuilder:
    """Build structured prompts with consistent formatting."""
    
    @staticmethod
    def zero_shot(
        task: str,
        context: Optional[str] = None,
        output_format: Optional[str] = None,
        constraints: Optional[str] = None
    ) -> str:
        """Build a zero-shot prompt.
        
        Args:
            task: The main instruction
            context: Background information
            output_format: Expected output structure
            constraints: Limitations or rules
            
        Returns:
            Formatted prompt string
        """
        parts = []
        if context:
            parts.append(f"Context:\n{context}")
        parts.append(f"Task:\n{task}")
        if output_format:
            parts.append(f"Output Format:\n{output_format}")
        if constraints:
            parts.append(f"Constraints:\n{constraints}")
        return "\n\n".join(parts)
    
    @staticmethod
    def few_shot(
        task: str,
        examples: List[Dict[str, str]],
        input_key: str = "input",
        output_key: str = "output",
        context: Optional[str] = None,
        test_input: Optional[str] = None
    ) -> str:
        """Build a few-shot prompt with examples.
        
        Args:
            task: Description of the task
            examples: List of {input: ..., output: ...} dicts
            input_key: Key for input in examples
            output_key: Key for output in examples
            context: Background information
            test_input: The actual input to process
            
        Returns:
            Formatted few-shot prompt
        """
        parts = []
        if context:
            parts.append(f"Context:\n{context}")
        parts.append(f"Task: {task}\n")
        parts.append("Examples:")
        
        for i, ex in enumerate(examples, 1):
            parts.append(f"\nExample {i}:")
            parts.append(f"Input: {ex.get(input_key, '')}")
            parts.append(f"Output: {ex.get(output_key, '')}")
        
        if test_input:
            parts.append(f"\nNow process this input:\n{test_input}")
            parts.append("Output:")
        
        return "\n".join(parts)
    
    @staticmethod
    def role_based(
        role: str,
        task: str,
        expertise: Optional[str] = None,
        tone: Optional[str] = None,
        context: Optional[str] = None
    ) -> str:
        """Build a role-based prompt.
        
        Args:
            role: The role/persona (e.g., "expert Python developer")
            task: What to do
            expertise: Specific expertise areas
            tone: Communication style
            context: Additional context
            
        Returns:
            Formatted role prompt
        """
        parts = [f"You are a {role}."]
        if expertise:
            parts.append(f"Expertise: {expertise}")
        if tone:
            parts.append(f"Tone: {tone}")
        if context:
            parts.append(f"\nContext:\n{context}")
        parts.append(f"\nTask:\n{task}")
        return "\n".join(parts)


def format_chat_history(messages: List[Dict[str, str]]) -> str:
    """Format a list of messages into a conversation string.
    
    Args:
        messages: List of {'role': 'user'|'assistant', 'content': '...'}
        
    Returns:
        Formatted conversation
    """
    lines = []
    for msg in messages:
        role = msg.get('role', 'user').capitalize()
        content = msg.get('content', '')
        lines.append(f"{role}: {content}")
    return "\n".join(lines)
