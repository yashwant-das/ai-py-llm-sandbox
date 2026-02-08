# Topic 14: Securing Generative AI Applications

> Understand and mitigate security risks in LLM applications.

## Learning Objectives

By the end of this topic, you will:
- Understand OWASP LLM Top 10
- Test for prompt injection vulnerabilities
- Implement input/output filtering
- Design sandboxed execution

## Folder Structure

```
14_security/
├── README.md
├── vulnerabilities/
│   ├── prompt_injection.md
│   ├── data_exfiltration.md
│   ├── insecure_output_handling.md
│   └── owasp_llm_top_10.md
├── defenses/
│   ├── input_sanitization.py
│   ├── output_filtering.py
│   ├── rate_limiting.py
│   └── sandboxing_tools.py
└── experiments/
    ├── jailbreak_attempts.py
    └── defense_testing.py
```

## OWASP LLM Top 10 (2025)

1. Prompt Injection
2. Sensitive Information Disclosure
3. Supply Chain Vulnerabilities
4. Data and Model Poisoning
5. Improper Output Handling
6. Excessive Agency
7. System Prompt Leakage
8. Vector and Embedding Weaknesses
9. Misinformation
10. Unbounded Consumption

## Running Examples

```bash
# Test defenses
python 14_security/experiments/defense_testing.py

# Input sanitization demo
python 14_security/defenses/input_sanitization.py
```

## Cross-References

- **Previous**: [13_ux_for_ai/](../13_ux_for_ai/)
- **Next**: [15_llmops_lifecycle/](../15_llmops_lifecycle/)
- **Related**: [04_ethics_and_safety/](../04_ethics_and_safety/)

## Resources

- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [AI Incident Database](https://incidentdatabase.ai/)
