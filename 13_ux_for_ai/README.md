# Topic 13: UX Design for AI Applications

> Design patterns for trustworthy, usable AI interfaces.

## Learning Objectives

By the end of this topic, you will:
- Implement streaming responses
- Show confidence scores and citations
- Design human-in-the-loop workflows
- Handle errors gracefully

## Folder Structure

```
13_ux_for_ai/
├── README.md
├── patterns/
│   ├── progressive_disclosure.md  # Confidence scores
│   ├── human_in_the_loop.md       # Approval workflows
│   ├── streaming_responses.md     # Perceived performance
│   └── error_recovery.md          # Graceful failures
└── experiments/
    ├── typing_indicator_sim.py
    └── confidence_indicators.py
```

## UX Patterns

### Streaming
- Token-by-token display
- Perceived performance improvement
- Cancellation support

### Confidence Indicators
- Show certainty scores
- Cite sources (for RAG)
- Highlight uncertain claims

### Human-in-the-Loop
- Approval for high-stakes actions
- Edit suggestions before applying
- Feedback collection

## Running Examples

```bash
# Confidence indicators
python 13_ux_for_ai/experiments/confidence_indicators.py
```

## Cross-References

- **Previous**: [12_function_calling/](../12_function_calling/)
- **Next**: [14_security/](../14_security/)
