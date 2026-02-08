# 09. AI Safety & Ethics

Building responsible AI systems.

## Key Risks

1.  **Bias**: Models reflecting societal prejudices.
2.  **Hallucinations**: Confidently stating false information.
3.  **Prompt Injection**: Users tricking the model into ignoring instructions.
4.  **Jailbreaking**: Bypassing safety guardrails.

## Defenses

1.  **System Prompts**: Strong instructions defining boundaries.
2.  **Guardrails**: External filters (input/output) to block harmful content (e.g., NeMo Guardrails).
3.  **Red Teaming**: Actively trying to break your own system to find vulnerabilities.

## Experiments

See `experiments/` for demonstrations of prompt injection and basic defense patterns.
