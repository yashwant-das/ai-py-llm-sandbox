# Topic 11: Building Low-Code Generative AI Applications

> Rapid prototyping with minimal code: Gradio, Streamlit, Chainlit.

## Learning Objectives

By the end of this topic, you will:
- Build UIs with Gradio in minutes
- Create data apps with Streamlit
- Implement chat interfaces with Chainlit
- Integrate with workflow tools (n8n)

## Folder Structure

```
11_low_code_genai/
├── README.md
├── examples/
│   ├── gradio_hello_world/
│   ├── streamlit_quickstart/
│   └── chainlit_basics/
└── integrations/
    └── n8n_workflows/
```

## Framework Comparison

| Framework | Best For | Complexity |
|-----------|----------|------------|
| Gradio | ML demos, quick UIs | Low |
| Streamlit | Data apps, dashboards | Medium |
| Chainlit | Chat interfaces | Low |
| n8n | Workflow automation | Visual |

## Running Examples

```bash
# Gradio demo
python 11_low_code_genai/examples/gradio_hello_world/app.py

# Streamlit app
streamlit run 11_low_code_genai/examples/streamlit_quickstart/app.py

# Chainlit chat
chainlit run 11_low_code_genai/examples/chainlit_basics/app.py
```

## Cross-References

- **Previous**: [10_image_generation/](../10_image_generation/)
- **Next**: [12_function_calling/](../12_function_calling/)
