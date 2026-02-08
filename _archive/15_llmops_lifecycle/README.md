# Topic 15: Generative AI Application Lifecycle (LLMOps)

> Production-adjacent concerns: versioning, evaluation, monitoring.

## Learning Objectives

By the end of this topic, you will:
- Version and track prompt changes
- Implement A/B testing for prompts
- Set up observability and logging
- Design evaluation frameworks

## Folder Structure

```
15_llmops_lifecycle/
├── README.md
├── notes/
│   ├── prompt_versioning.md
│   ├── evaluation_frameworks.md
│   ├── monitoring_and_observability.md
│   └── ci_cd_for_prompts.md
├── experiments/
│   ├── prompt_versioning_system.py
│   ├── a_b_testing_framework.py
│   └── response_logging.py
└── configs/
    └── prompt_registry.yaml
```

## LLMOps Concerns

### Prompt Management
- Version control for prompts
- A/B testing framework
- Rollback capabilities

### Evaluation
- Automated metrics
- Human evaluation workflows
- Regression testing

### Observability
- Request/response logging
- Latency tracking
- Error monitoring

## Running Examples

```bash
# Prompt versioning
python 15_llmops_lifecycle/experiments/prompt_versioning_system.py

# A/B testing
python 15_llmops_lifecycle/experiments/a_b_testing_framework.py
```

## Cross-References

- **Previous**: [14_security/](../14_security/)
- **Next**: [16_rag_systems/](../16_rag_systems/)
