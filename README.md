# GenAI Systems Playground

> A practical, hands-on sandbox for learning and experimenting with Generative AI systems — from prompt engineering basics to AI agents and LLMOps.

## Quick Start

```bash
# 1. Clone and setup
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your configuration (LM Studio, API keys, etc.)

# 2. Verify setup
python 01_setup/verify_setup.py

# 3. Run your first example
python 05_prompt_engineering_fundamentals/code/01_zero_shot.py
```

## Repository Structure

This repository is organized into 21 progressive topics, from fundamentals to specialized areas:

### Foundation (Topics 1-4)
| Topic | Folder | Description |
|-------|--------|-------------|
| 1 | [`01_setup/`](01_setup/) | Development environment, LM Studio, Docker |
| 2 | [`02_genai_fundamentals/`](02_genai_fundamentals/) | LLM basics, tokens, embeddings, sampling |
| 3 | [`03_llm_landscape/`](03_llm_landscape/) | Comparing models, benchmarks, selection |
| 4 | [`04_ethics_and_safety/`](04_ethics_and_safety/) | Bias, safety, prompt injection, red teaming |

### Core Skills (Topics 5-6)
| Topic | Folder | Description |
|-------|--------|-------------|
| 5 | [`05_prompt_engineering_fundamentals/`](05_prompt_engineering_fundamentals/) | Zero-shot, few-shot, role prompting |
| 6 | [`06_advanced_prompting/`](06_advanced_prompting/) | CoT, self-consistency, structured output, ToT |

### Applications (Topics 7-11)
| Topic | Folder | Description |
|-------|--------|-------------|
| 7 | [`07_text_generation_apps/`](07_text_generation_apps/) | Email writers, content expanders |
| 8 | [`08_chat_applications/`](08_chat_applications/) | Conversational interfaces with memory |
| 9 | [`09_search_with_vectors/`](09_search_with_vectors/) | Semantic search, FAISS, Chroma |
| 10 | [`10_image_generation/`](10_image_generation/) | Text-to-image, prompt enhancement |
| 11 | [`11_low_code_genai/`](11_low_code_genai/) | Gradio, Streamlit, Chainlit |

### Integration & Systems (Topics 12-16)
| Topic | Folder | Description |
|-------|--------|-------------|
| 12 | [`12_function_calling/`](12_function_calling/) | Tool use, function calling, orchestration |
| 13 | [`13_ux_for_ai/`](13_ux_for_ai/) | Streaming, confidence indicators, HITL |
| 14 | [`14_security/`](14_security/) | OWASP LLM, sandboxing, defenses |
| 15 | [`15_llmops_lifecycle/`](15_llmops_lifecycle/) | Prompt versioning, A/B testing, observability |
| 16 | [`16_rag_systems/`](16_rag_systems/) | RAG pipelines, chunking, evaluation |

### Specialized Topics (Topics 17-21)
| Topic | Folder | Description |
|-------|--------|-------------|
| 17 | [`17_huggingface_ecosystem/`](17_huggingface_ecosystem/) | Open-source models, Transformers, quantization |
| 18 | [`18_ai_agents/`](18_ai_agents/) | ReAct, LangGraph, multi-agent systems |
| 19 | [`19_fine_tuning/`](19_fine_tuning/) | LoRA, PEFT, dataset preparation |
| 20 | [`20_small_language_models/`](20_small_language_models/) | Phi-3, Gemma, edge deployment |
| 21 | [`21_mistral_meta_families/`](21_mistral_meta_families/) | Mistral, Mixtral, Llama 3.1 |

### Shared Infrastructure
| Folder | Purpose |
|--------|---------|
| [`shared/`](shared/) | LLM providers, configuration, common utilities |
| [`data/`](data/) | Datasets, embeddings cache (gitignored) |
| [`tests/`](tests/) | Unit and integration tests |

## Design Principles

### Raw SDK First, Frameworks Second
- **Fundamentals**: Raw OpenAI-style SDK usage for transparency and learning
- **Frameworks**: LangChain, LangGraph where orchestration adds value
- **Explicit**: Documentation of what each framework abstracts away

### Progressive Complexity
```
Topics 1-4:   Foundation (concepts, ethics, setup)
Topics 5-6:   Core Skills (prompt engineering)
Topics 7-11:  Applications (building things)
Topics 12-16: Systems (integration, lifecycle)
Topics 17-21: Specialized (OSS, agents, fine-tuning)
```

### Local-First with Cloud Options
- **Default**: Local LLMs via LM Studio or Ollama (privacy, cost, control)
  - LM Studio: GUI-based, great for experimentation
  - Ollama: CLI-based, simple model management
- **Optional**: Cloud APIs (OpenAI, Groq, Together) when specified
- All examples work with OpenAI-compatible endpoints

## Running Examples

### Prerequisites

Choose **one** of the following local LLM options:

**Option A: LM Studio** (GUI-based, recommended for beginners)
- Download from [lmstudio.ai](https://lmstudio.ai/)
- Load a model (e.g., `openai/gpt-oss-20b`, `Llama-3.1-8B`)
- Start the local server on port 1234

**Option B: Ollama** (CLI-based, simpler setup)
- Install from [ollama.com](https://ollama.com/)
- Pull a model: `ollama pull llama3.1`
- Server runs automatically at port 11434

2. **Python Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. **Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

### Example Commands

```bash
# Prompt Engineering
python 05_prompt_engineering_fundamentals/code/01_zero_shot.py
python 05_prompt_engineering_fundamentals/code/02_few_shot.py

# Advanced Techniques
python 06_advanced_prompting/code/01_chain_of_thought.py
python 06_advanced_prompting/code/04_structured_output.py

# Agents
python 18_ai_agents/fundamentals/01_react_pattern.py

# RAG (requires additional setup)
python 16_rag_systems/fundamentals/01_basic_rag_pipeline.py
```

## Key Dependencies

```
langchain>=0.3.0          # Framework for chains and agents
langchain-openai>=0.2.0   # OpenAI-compatible interface
langgraph>=0.2.0          # State machine agents
chromadb>=0.5.0           # Vector database (Topic 9, 16)
transformers>=4.40.0      # Hugging Face (Topic 17)
```

See [`requirements.txt`](requirements.txt) for complete list.

## Cross-References

Topics are interconnected. Key pathways:

```
05_prompt_engineering → 06_advanced_prompting → 12_function_calling
                                              ↓
18_ai_agents ← 16_rag_systems ← 09_search_with_vectors
```

Each topic's README.md includes:
- Prerequisites (what to know first)
- Related topics (what connects to this)
- Next steps (where to go after)

## Contributing

This is a personal study sandbox. Structure follows these principles:
1. **Minimal abstractions first** — show the raw mechanism
2. **Explicit over implicit** — document what frameworks hide
3. **Runnable code** — every example should execute
4. **Clear cross-references** — link related concepts

## License

MIT License — See [LICENSE](LICENSE) for details.

## Resources

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [LangChain Documentation](https://python.langchain.com/)
- [LM Studio](https://lmstudio.ai/)
- [Ollama](https://ollama.com/)
- [Hugging Face](https://huggingface.co/docs)
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
