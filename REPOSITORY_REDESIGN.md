# GenAI Systems Playground — Repository Redesign

> A practical, hands-on sandbox for learning and experimenting with Generative AI systems.

---

## 1. Directory Structure (Proposed)

```
genai-systems-playground/
│
├── README.md                          # Main entry point
├── requirements.txt                   # Base dependencies
├── requirements-dev.txt               # Dev/test dependencies
├── .env.example                       # Template for environment variables
├── Makefile                           # Common commands (optional)
│
├── 01_setup/                          # TOPIC 1: Course Setup & Development Environment
│   ├── README.md
│   ├── python_env_setup.md
│   ├── lm_studio_guide.md
│   ├── docker/                        # Optional containerized environments
│   │   ├── Dockerfile.dev
│   │   └── docker-compose.yml
│   └── verify_setup.py                # Script to test connectivity
│
├── 02_genai_fundamentals/             # TOPIC 2: Introduction to Generative AI and LLMs
│   ├── README.md
│   ├── notes/
│   │   ├── what_are_llms.md
│   │   ├── transformer_basics.md
│   │   ├── tokens_and_embeddings.md
│   │   └── inference_vs_training.md
│   └── experiments/
│       ├── token_counting.py          # Count tokens in prompts
│       ├── explore_temperature.py     # Visualize temperature effects
│       └── top_p_sampling_demo.py     # Nucleus sampling exploration
│
├── 03_llm_landscape/                  # TOPIC 3: Exploring and Comparing LLMs
│   ├── README.md
│   ├── model_registry.yaml            # Catalog of models to try
│   ├── comparison_framework/
│   │   ├── benchmark_runner.py        # Run same prompt across models
│   │   ├── latency_benchmark.py       # Measure response times
│   │   └── quality_evaluator.py       # Simple side-by-side comparison
│   └── experiments/
│       ├── compare_creative_writing.py
│       ├── compare_reasoning.py       # Logic puzzles across models
│       └── compare_code_generation.py
│
├── 04_ethics_and_safety/              # TOPIC 4: Responsible and Ethical Use
│   ├── README.md
│   ├── notes/
│   │   ├── bias_in_llms.md
│   │   ├── hallucinations.md
│   │   ├── data_privacy.md
│   │   └── content_safety.md
│   └── experiments/
│       ├── detect_toxicity.py         # Content moderation examples
│       ├── bias_detection_demo.py     # Measure stereotypical associations
│       ├── prompt_injection_test.py   # Basic security testing
│       └── red_teaming_basics.py      # Simple adversarial prompts
│
├── 05_prompt_engineering_fundamentals/# TOPIC 5: Prompt Engineering Fundamentals
│   ├── README.md
│   ├── notes/
│   │   ├── prompt_structure.md
│   │   ├── context_window_management.md
│   │   └── instruction_vs_completion.md
│   └── code/
│       ├── 01_zero_shot.py            # ← MAPPED from src/01_zero_shot.py
│       ├── 02_few_shot.py             # ← MAPPED from src/02_few_shot.py
│       ├── 03_role_prompting.py       # ← MAPPED from src/05_role_prompting.py
│       └── utils/
│           ├── prompt_builder.py      # Reusable prompt templates
│           └── llm_client.py          # Unified LLM interface
│
├── 06_advanced_prompting/             # TOPIC 6: Advanced Prompt Engineering Techniques
│   ├── README.md
│   ├── notes/
│   │   ├── reasoning_patterns.md
│   │   ├── output_formatting.md
│   │   └── prompt_optimization.md
│   └── code/
│       ├── 01_chain_of_thought.py     # ← MAPPED from src/03_chain_of_thought.py
│       ├── 02_self_consistency.py     # ← MAPPED from src/07_self_consistency.py
│       ├── 03_prompt_chaining.py      # ← MAPPED from src/08_prompt_chaining.py
│       ├── 04_structured_output.py    # ← MAPPED from src/06_structured_output.py
│       ├── 05_tree_of_thoughts.py     # ToT implementation
│       ├── 06_auto_prompt_engineering.py  # APE basics
│       └── 07_system2_activations.py  # Reflection, critique
│
├── 07_text_generation_apps/           # TOPIC 7: Building Text Generation Applications
│   ├── README.md
│   ├── apps/
│   │   ├── email_writer/              # End-to-end email assistant
│   │   ├── content_expander/          # Bullet points → paragraphs
│   │   └── code_documenter/           # Auto-generate docstrings
│   └── shared/
│       ├── streaming_handler.py       # Token-by-token display
│       └── output_validators.py       # Post-processing utilities
│
├── 08_chat_applications/              # TOPIC 8: Building Chat Applications
│   ├── README.md
│   ├── implementations/
│   │   ├── 01_basic_chat_cli.py       # Simple conversation loop
│   │   ├── 02_chat_with_memory.py     # In-memory context
│   │   ├── 03_chat_with_history_db.py # Persistent conversations
│   │   └── 04_multi_turn_reasoning.py # Complex dialog patterns
│   └── frameworks/
│       ├── langchain_chat.py          # Framework comparison
│       └── streamlit_chat_ui/         # Optional web UI
│
├── 09_search_with_vectors/            # TOPIC 9: Building Search Applications with Vector Databases
│   ├── README.md
│   ├── notes/
│   │   ├── vector_embeddings_explained.md
│   │   └── similarity_metrics.md
│   ├── code/
│   │   ├── 01_basic_semantic_search.py
│   │   ├── 02_faiss_indexing.py       # Local vector store
│   │   ├── 03_chroma_integration.py   # Persistent vector DB
│   │   └── 04_hybrid_search.py        # Keyword + semantic
│   └── datasets/
│       └── sample_documents.json      # Test data for indexing
│
├── 10_image_generation/               # TOPIC 10: Building Image Generation Applications
│   ├── README.md
│   ├── local_models/                  # SDXL, Flux, etc. via local tools
│   │   └── comfyui_integration.md
│   ├── api_integrations/
│   │   ├── openai_dalle.py
│   │   └── stability_ai.py
│   └── apps/
│       ├── prompt_enhancer.py         # LLM → better image prompts
│       └── batch_generator.py         # Bulk image creation
│
├── 11_low_code_genai/                 # TOPIC 11: Building Low-Code Generative AI Applications
│   ├── README.md
│   ├── examples/
│   │   ├── gradio_hello_world/        # Quick UIs
│   │   ├── streamlit_quickstart/
│   │   └── chainlit_basics/           # Chat UI framework
│   └── integrations/
│       └── n8n_workflows/             # Workflow automation examples
│
├── 12_function_calling/               # TOPIC 12: Function Calling and Tool Integration
│   ├── README.md
│   ├── fundamentals/
│   │   ├── 01_native_function_calling.py   # OpenAI-style tool use
│   │   ├── 02_manual_tool_parsing.py       # Parse tool calls from text
│   │   └── 03_multi_tool_orchestration.py  # Tool selection logic
│   ├── implementations/
│   │   ├── calculator_tool.py
│   │   ├── weather_tool.py
│   │   └── file_system_tools.py
│   └── framework/
│       └── langchain_tools_integration.py  # Compare raw vs framework
│
├── 13_ux_for_ai/                      # TOPIC 13: UX Design for AI Applications
│   ├── README.md
│   ├── patterns/
│   │   ├── progressive_disclosure.md  # Show confidence scores
│   │   ├── human_in_the_loop.md       # Approval workflows
│   │   ├── streaming_responses.md     # Perceived performance
│   │   └── error_recovery.md          # Graceful failures
│   └── experiments/
│       ├── typing_indicator_sim.py
│       └── confidence_indicators.py
│
├── 14_security/                       # TOPIC 14: Securing Generative AI Applications
│   ├── README.md
│   ├── vulnerabilities/
│   │   ├── prompt_injection.md
│   │   ├── data_exfiltration.md
│   │   ├── insecure_output_handling.md
│   │   └── owasp_llm_top_10.md
│   ├── defenses/
│   │   ├── input_sanitization.py
│   │   ├── output_filtering.py
│   │   ├── rate_limiting.py
│   │   └── sandboxing_tools.py
│   └── experiments/
│       ├── jailbreak_attempts.py      # Controlled testing only
│       └── defense_testing.py
│
├── 15_llmops_lifecycle/               # TOPIC 15: Generative AI Application Lifecycle (LLMOps)
│   ├── README.md
│   ├── notes/
│   │   ├── prompt_versioning.md
│   │   ├── evaluation_frameworks.md
│   │   ├── monitoring_and_observability.md
│   │   └── ci_cd_for_prompts.md
│   ├── experiments/
│   │   ├── prompt_versioning_system.py
│   │   ├── a_b_testing_framework.py
│   │   └── response_logging.py
│   └── configs/
│       └── prompt_registry.yaml       # Centralized prompt management
│
├── 16_rag_systems/                    # TOPIC 16: Retrieval-Augmented Generation (RAG) and Vector Databases
│   ├── README.md
│   ├── fundamentals/
│   │   ├── 01_basic_rag_pipeline.py   # Ingest → Retrieve → Generate
│   │   ├── 02_chunking_strategies.py  # Text splitting methods
│   │   ├── 03_embedding_models.py     # Compare embedding providers
│   │   └── 04_rag_evaluation.py       # Metrics for RAG quality
│   ├── advanced/
│   │   ├── 01_hybrid_retrieval.py     # Sparse + dense retrieval
│   │   ├── 02_reranking.py            # Cross-encoder reranking
│   │   ├── 03_query_expansion.py      # HyDE, multi-query
│   │   ├── 04_contextual_compression.py
│   │   └── 05_parent_document_retrieval.py
│   └── apps/
│       ├── document_qa/
│       └── code_assistant/
│
├── 17_huggingface_ecosystem/          # TOPIC 17: Open-Source Models and Hugging Face Ecosystem
│   ├── README.md
│   ├── setup/
│   │   ├── transformers_basics.md
│   │   └── local_inference_options.md
│   ├── code/
│   │   ├── 01_pipeline_api.py         # Simple HF pipelines
│   │   ├── 02_model_loading.py        # From pretrained
│   │   ├── 03_tokenizers.py           # HF tokenizers deep dive
│   │   └── 04_quantization_basics.py  # GGUF, AWQ, GPTQ intro
│   ├── integrations/
│   │   ├── ollama_integration.py
│   │   └── llama_cpp_integration.py   # Local inference
│   └── experiments/
│       └── model_comparison_hf.py
│
├── 18_ai_agents/                      # TOPIC 18: AI Agents and Agent Frameworks
│   ├── README.md
│   ├── fundamentals/
│   │   ├── 01_react_pattern.py        # ← MAPPED from src/04_react_agent.py
│   │   ├── 02_react_from_scratch.py   # Manual implementation
│   │   ├── 03_plan_and_execute.py     # Decomposition agents
│   │   └── 04_multi_agent_patterns.md # Agent collaboration
│   ├── frameworks/
│   │   ├── langgraph_agents.py        # LangGraph state machines
│   │   ├── autogen_basics.py          # Microsoft AutoGen
│   │   └── crewai_intro.py            # Role-based agents
│   └── apps/
│       ├── research_assistant/        # Web search + synthesis agent
│       ├── coding_agent/              # File operations + code gen
│       └── personal_assistant/        # Multi-tool coordinator
│
├── 19_fine_tuning/                    # TOPIC 19: Fine-Tuning Large Language Models
│   ├── README.md
│   ├── notes/
│   │   ├── when_to_finetune.md
│   │   ├── data_preparation.md
│   │   ├── peft_lora_explained.md     # Parameter-efficient methods
│   │   └── evaluation_after_finetune.md
│   ├── code/
│   │   ├── 01_prepare_dataset.py      # Format conversations
│   │   ├── 02_lora_finetune.py        # PEFT/LoRA training
│   │   └── 03_inference_finetuned.py  # Load and test
│   └── configs/
│       └── lora_config.yaml           # Training hyperparameters
│
├── 20_small_language_models/          # TOPIC 20: Building with Small Language Models (SLMs)
│   ├── README.md
│   ├── models/
│   │   ├── phi_3_examples.py          # Microsoft's Phi-3
│   │   ├── gemma_examples.py          # Google's Gemma
│   │   ├── qwen_examples.py           # Alibaba's Qwen
│   │   └── llama_3_1b_8b.py           # Meta's smaller models
│   ├── optimizations/
│   │   ├── quantization_comparison.py # 4-bit vs 8-bit
│   │   ├── onnx_export.py             # Runtime optimization
│   │   └── edge_deployment.md         # Mobile/edge considerations
│   └── apps/
│       ├── on_device_chat.py          # Offline chat
│       └── embedded_assistant.py      # Raspberry Pi/edge demo
│
├── 21_mistral_meta_families/          # TOPIC 21: Building with Mistral and Meta Model Families
│   ├── README.md
│   ├── mistral/
│   │   ├── mistral_7b_examples.py
│   │   ├── mixtral_moe_explained.py   # Mixture of Experts
│   │   ├── mistral_large_api.py       # Via La Plateforme
│   │   └── codestral_examples.py      # Code-specialized model
│   ├── meta_llama/
│   │   ├── llama_3_1_explained.md
│   │   ├── llama_3_1_8b_local.py      # Local inference
│   │   ├── llama_3_1_70b_groq.py      # Cloud inference
│   │   └── llama_guard_safety.py      # Safety classifier
│   └── comparisons/
│       └── llama_vs_mistral_benchmark.py
│
├── shared/                            # SHARED UTILITIES (cross-cutting)
│   ├── __init__.py
│   ├── llm_providers.py               # Unified interface for OpenAI, local, etc.
│   ├── embeddings.py                  # Common embedding interface
│   ├── vector_stores.py               # Abstracted vector DB client
│   ├── config.py                      # Centralized configuration
│   └── logging_utils.py               # Structured logging for experiments
│
├── data/                              # DATA ASSETS (gitignored or sampled)
│   ├── raw/                           # Original datasets
│   ├── processed/                     # Cleaned/transformed
│   └── embeddings/                    # Pre-computed embeddings cache
│
└── tests/                             # TESTS (per-topic or shared)
    ├── test_prompt_engineering.py
    ├── test_rag_pipeline.py
    └── conftest.py                    # Pytest fixtures
```

---

## 2. Existing Code Mapping

| Original File | New Location | Notes |
|---------------|--------------|-------|
| `src/01_zero_shot.py` | `05_prompt_engineering_fundamentals/code/01_zero_shot.py` | Core fundamentals |
| `src/02_few_shot.py` | `05_prompt_engineering_fundamentals/code/02_few_shot.py` | Core fundamentals |
| `src/05_role_prompting.py` | `05_prompt_engineering_fundamentals/code/03_role_prompting.py` | Core fundamentals |
| `src/03_chain_of_thought.py` | `06_advanced_prompting/code/01_chain_of_thought.py` | Advanced reasoning |
| `src/07_self_consistency.py` | `06_advanced_prompting/code/02_self_consistency.py` | Advanced reasoning |
| `src/08_prompt_chaining.py` | `06_advanced_prompting/code/03_prompt_chaining.py` | Advanced composition |
| `src/06_structured_output.py` | `06_advanced_prompting/code/04_structured_output.py` | Output formatting |
| `src/04_react_agent.py` | `18_ai_agents/fundamentals/01_react_pattern.py` | Agent foundations |
| `src/09_advanced_techniques.py` | Split across `06_advanced_prompting/code/` | ToT → `05_`, APE → `06_`, System-2 → `07_` |

### Refactoring Notes for Existing Code:

1. **Unify LLM Client**: Extract the repeated LM Studio initialization into `shared/llm_providers.py`:
   ```python
   # shared/llm_providers.py
   def get_lmstudio_llm(model="openai/gpt-oss-20b", temperature=0.1):
       return ChatOpenAI(...)
   ```

2. **Environment Configuration**: Move hardcoded values to `.env`:
   ```
   LMSTUDIO_BASE_URL=http://127.0.0.1:1234/v1
   LMSTUDIO_API_KEY=lm-studio
   DEFAULT_MODEL=openai/gpt-oss-20b
   ```

3. **Preserve Documentation**: Each migrated file keeps its docstring header but adds cross-references to related topics.

---

## 3. Topic Details

### Topic 1: Course Setup & Development Environment
**Folder:** `01_setup/`  
**Type:** Learn + Configure  
**Purpose:** Ensure reproducible environments across local, Docker, and cloud setups.

**Content:**
- Python virtual environment setup guide
- LM Studio installation and configuration
- Alternative: Ollama setup
- Alternative: Docker-based setup
- Environment variable management
- Verification scripts

**Example Code:**
- `verify_setup.py` — Tests connectivity to LM Studio, counts available models
- `test_imports.py` — Verifies all required packages installed

---

### Topic 2: Introduction to Generative AI and LLMs
**Folder:** `02_genai_fundamentals/`  
**Type:** Learn + Experiment  
**Purpose:** Build intuition for how LLMs work without diving into training.

**Content:**
- Conceptual notes on transformers, tokens, context windows
- Tokenization experiments
- Temperature and sampling visualizations
- Cost estimation basics

**Example Code:**
- `token_counting.py` — Use tiktoken to count tokens in prompts
- `explore_temperature.py` — Same prompt, varying temperature, collect responses
- `context_window_demo.py` — Show degradation as context fills

---

### Topic 3: Exploring and Comparing LLMs
**Folder:** `03_llm_landscape/`  
**Type:** Learn + Experiment  
**Purpose:** Understand differences between model families, sizes, and providers.

**Content:**
- Model registry (YAML catalog)
- Benchmarking framework
- Latency vs quality trade-offs
- Open vs closed source considerations

**Example Code:**
- `benchmark_runner.py` — Run standardized prompts across multiple endpoints
- `latency_benchmark.py` — Measure time-to-first-token vs total generation
- `quality_evaluator.py` — Side-by-side comparison UI (CLI)

---

### Topic 4: Responsible and Ethical Use of Generative AI
**Folder:** `04_ethics_and_safety/`  
**Type:** Learn + Experiment  
**Purpose:** Understand risks and mitigation strategies for safe deployment.

**Content:**
- Bias and fairness in LLMs
- Hallucination detection strategies
- Content moderation and safety classifiers
- Data privacy considerations
- Red teaming basics

**Example Code:**
- `bias_detection_demo.py` — Measure associations with demographic terms
- `prompt_injection_test.py` — Controlled tests for injection vulnerabilities
- `content_moderation.py` — Use moderation APIs or local classifiers

---

### Topic 5: Prompt Engineering Fundamentals
**Folder:** `05_prompt_engineering_fundamentals/`  
**Type:** Learn + Build  
**Purpose:** Master the basics of effective prompting.

**Content:**
- Zero-shot and few-shot patterns
- Role/persona assignment
- Prompt structure (instruction, context, examples, output format)
- Context window management

**Mapped from Existing:**
| New File | Source |
|----------|--------|
| `code/01_zero_shot.py` | `src/01_zero_shot.py` |
| `code/02_few_shot.py` | `src/02_few_shot.py` |
| `code/03_role_prompting.py` | `src/05_role_prompting.py` |

**New Additions:**
- `utils/prompt_builder.py` — Template system for reusable prompts
- `utils/llm_client.py` — Refactored shared client

---

### Topic 6: Advanced Prompt Engineering Techniques
**Folder:** `06_advanced_prompting/`  
**Type:** Learn + Build  
**Purpose:** Advanced patterns for complex reasoning and reliable outputs.

**Content:**
- Chain-of-Thought (CoT) and variants
- Self-consistency and voting
- Prompt chaining and decomposition
- Structured outputs (JSON, XML, Pydantic)
- Tree of Thoughts (ToT)
- Automatic Prompt Engineering (APE)
- System-2 thinking (reflection, critique)

**Mapped from Existing:**
| New File | Source |
|----------|--------|
| `code/01_chain_of_thought.py` | `src/03_chain_of_thought.py` |
| `code/02_self_consistency.py` | `src/07_self_consistency.py` |
| `code/03_prompt_chaining.py` | `src/08_prompt_chaining.py` |
| `code/04_structured_output.py` | `src/06_structured_output.py` |

**New Additions:**
- `code/05_tree_of_thoughts.py` — Explore multiple reasoning paths
- `code/06_auto_prompt_engineering.py` — Meta-prompting for optimization
- `code/07_system2_activations.py` — Self-correction and verification

---

### Topic 7: Building Text Generation Applications
**Folder:** `07_text_generation_apps/`  
**Type:** Build  
**Purpose:** End-to-end applications focused on text output.

**Content:**
- Streaming responses for UX
- Output validation and sanitization
- Template-based generation
- Batch processing patterns

**Example Apps:**
- `email_writer/` — Professional email generator with tone selection
- `content_expander/` — Bullet points to prose
- `code_documenter/` — Auto-generate docstrings from function signatures

---

### Topic 8: Building Chat Applications
**Folder:** `08_chat_applications/`  
**Type:** Build  
**Purpose:** Conversational interfaces with memory and context.

**Content:**
- Message history management
- Context window pruning strategies
- Conversation summarization
- Multi-turn reasoning patterns

**Example Code:**
- `01_basic_chat_cli.py` — Simple input/output loop
- `02_chat_with_memory.py` — In-memory conversation buffer
- `03_chat_with_history_db.py` — SQLite/Chroma persistence
- `04_multi_turn_reasoning.py` — Clarifying questions, plan refinement

---

### Topic 9: Building Search Applications with Vector Databases
**Folder:** `09_search_with_vectors/`  
**Type:** Learn + Build  
**Purpose:** Semantic search without the full RAG complexity.

**Content:**
- Embedding models overview
- Vector similarity concepts
- Local (FAISS) vs persistent (Chroma) stores
- Hybrid search combining keyword + semantic

**Example Code:**
- `01_basic_semantic_search.py` — Encode and search documents
- `02_faiss_indexing.py` — FAISS flat and IVF indexes
- `03_chroma_integration.py` — Persistent collections
- `04_hybrid_search.py` — BM25 + embeddings

---

### Topic 10: Building Image Generation Applications
**Folder:** `10_image_generation/`  
**Type:** Build  
**Purpose:** Text-to-image pipelines and integrations.

**Content:**
- Prompt engineering for images
- Local models (ComfyUI, SDXL) vs APIs
- LLM-based prompt enhancement
- Batch generation workflows

**Example Code:**
- `prompt_enhancer.py` — LLM expands terse prompts into detailed descriptions
- `batch_generator.py` — Generate variations programmatically

---

### Topic 11: Building Low-Code Generative AI Applications
**Folder:** `11_low_code_genai/`  
**Type:** Build  
**Purpose:** Rapid prototyping with minimal code frameworks.

**Content:**
- Gradio for quick UIs
- Streamlit for data apps
- Chainlit for chat interfaces
- n8n/Zapier for workflow automation

**Example Code:**
- `gradio_hello_world/` — Single-file UI examples
- `streamlit_quickstart/` — Multi-page app structure
- `chainlit_basics/` — Async chat handlers

---

### Topic 12: Function Calling and Tool Integration
**Folder:** `12_function_calling/`  
**Type:** Learn + Build  
**Purpose:** Extend LLM capabilities with external tools.

**Content:**
- Native function calling (OpenAI-style)
- Manual tool parsing (for models without native support)
- Tool selection and routing
- Error handling in tool execution

**Example Code:**
- `01_native_function_calling.py` — OpenAI tools API
- `02_manual_tool_parsing.py` — Parse JSON from text for local models
- `03_multi_tool_orchestration.py` — Router pattern for tool selection
- `calculator_tool.py`, `weather_tool.py` — Concrete tool implementations

---

### Topic 13: UX Design for AI Applications
**Folder:** `13_ux_for_ai/`  
**Type:** Learn + Experiment  
**Purpose:** Design patterns for trustworthy, usable AI interfaces.

**Content:**
- Streaming and progress indicators
- Confidence scoring and citations
- Human-in-the-loop patterns
- Error recovery and graceful degradation

**Example Code:**
- `typing_indicator_sim.py` — Simulate typing for natural feel
- `confidence_indicators.py` — Show uncertainty estimates

---

### Topic 14: Securing Generative AI Applications
**Folder:** `14_security/`  
**Type:** Learn + Experiment  
**Purpose:** Understand and mitigate security risks.

**Content:**
- OWASP LLM Top 10
- Prompt injection (direct and indirect)
- Data exfiltration risks
- Output filtering and sandboxing

**Example Code:**
- `input_sanitization.py` — Clean user inputs
- `output_filtering.py` — Post-process LLM outputs
- `sandboxing_tools.py` — Restricted execution environments

---

### Topic 15: Generative AI Application Lifecycle (LLMOps)
**Folder:** `15_llmops_lifecycle/`  
**Type:** Learn + Build  
**Purpose:** Production-adjacent concerns for prompt management and evaluation.

**Content:**
- Prompt versioning strategies
- A/B testing frameworks
- Observability and logging
- Evaluation metrics and benchmarks

**Example Code:**
- `prompt_versioning_system.py` — Git-like versioning for prompts
- `a_b_testing_framework.py` — Compare prompt variants
- `response_logging.py` — Structured logging for analysis

---

### Topic 16: Retrieval-Augmented Generation (RAG) and Vector Databases
**Folder:** `16_rag_systems/`  
**Type:** Learn + Build  
**Purpose:** Ground LLM outputs in external knowledge.

**Content:**
- Document ingestion pipelines
- Chunking strategies
- Embedding model selection
- Retrieval optimization
- Evaluation metrics

**Example Code:**
- `01_basic_rag_pipeline.py` — End-to-end RAG
- `02_chunking_strategies.py` — Fixed, semantic, recursive
- `03_embedding_models.py` — Compare providers
- `04_rag_evaluation.py` — Faithfulness, relevance metrics
- Advanced: Hybrid retrieval, reranking, query expansion

---

### Topic 17: Open-Source Models and Hugging Face Ecosystem
**Folder:** `17_huggingface_ecosystem/`  
**Type:** Learn + Build  
**Purpose:** Work with open models outside the OpenAI ecosystem.

**Content:**
- Transformers library basics
- Local inference options (transformers, llama.cpp, ollama)
- Tokenizers and model loading
- Quantization techniques

**Example Code:**
- `01_pipeline_api.py` — Simple HF pipelines
- `02_model_loading.py` — Manual model/tokenizer loading
- `03_tokenizers.py` — Encoding/decoding deep dive
- `04_quantization_basics.py` — 4-bit loading with bitsandbytes

---

### Topic 18: AI Agents and Agent Frameworks
**Folder:** `18_ai_agents/`  
**Type:** Learn + Build  
**Purpose:** Autonomous systems that reason and act.

**Content:**
- ReAct pattern (raw implementation)
- Planning and decomposition
- Multi-agent collaboration
- Framework comparison

**Mapped from Existing:**
| New File | Source |
|----------|--------|
| `fundamentals/01_react_pattern.py` | `src/04_react_agent.py` |

**New Additions:**
- `fundamentals/02_react_from_scratch.py` — Manual loop without LangChain
- `fundamentals/03_plan_and_execute.py` — Decomposition strategies
- `frameworks/langgraph_agents.py` — State machine agents
- `apps/research_assistant/` — End-to-end agent application

---

### Topic 19: Fine-Tuning Large Language Models
**Folder:** `19_fine_tuning/`  
**Type:** Learn + Build  
**Purpose:** Customize models for specific tasks with domain data.

**Content:**
- When to fine-tune vs prompt engineer
- Data preparation and formatting
- LoRA/QLoRA parameter-efficient methods
- Evaluation post-fine-tuning

**Example Code:**
- `01_prepare_dataset.py` — Format conversations for training
- `02_lora_finetune.py` — Training loop with PEFT
- `03_inference_finetuned.py` — Load and test adapter weights

---

### Topic 20: Building with Small Language Models (SLMs)
**Folder:** `20_small_language_models/`  
**Type:** Learn + Build  
**Purpose:** Efficient models for edge and resource-constrained environments.

**Content:**
- Phi-3, Gemma, Qwen, Llama-3.1-8B families
- Quantization impact on quality
- On-device inference
- Edge deployment considerations

**Example Code:**
- `phi_3_examples.py` — Microsoft's compact models
- `quantization_comparison.py` — Quality vs size trade-offs
- `on_device_chat.py` — Fully offline chat

---

### Topic 21: Building with Mistral and Meta Model Families
**Folder:** `21_mistral_meta_families/`  
**Type:** Learn + Build  
**Purpose:** Deep dive into two major open model ecosystems.

**Content:**
- Mistral 7B, Mixtral MoE, Codestral
- Llama 3.1 family (8B, 70B, 405B)
- Llama Guard for safety
- La Plateforme and Groq APIs

**Example Code:**
- `mistral/codestral_examples.py` — Code generation specialized model
- `meta_llama/llama_3_1_8b_local.py` — Local inference
- `meta_llama/llama_3_1_70b_groq.py` — Cloud inference
- `meta_llama/llama_guard_safety.py` — Content classification

---

## 4. Design Principles Applied

### Raw SDK vs Framework Separation

```
topic_XX/
├── fundamentals/          # Raw OpenAI-style SDK, minimal abstraction
│   └── 01_basic.py        # Clear, debuggable, educational
└── frameworks/            # LangChain, LangGraph, etc.
    └── 01_with_langchain.py  # Shows what the framework abstracts
```

### Progression Markers

| Marker | Meaning |
|--------|---------|
| `📖 Learn` | Conceptual notes, explanations |
| `🔬 Experiment` | Jupyter notebooks, exploratory code |
| `🔨 Build` | Runnable applications, CLI tools |
| `⚙️ System` | Infrastructure, lifecycle, observability |

### Topic Categories

| Category | Topics |
|----------|--------|
| **Foundation** | 1-4 (Setup, Fundamentals, Landscape, Ethics) |
| **Core Skills** | 5-6 (Prompt Engineering) |
| **Applications** | 7-11 (Text, Chat, Search, Image, Low-Code) |
| **Integration** | 12-14 (Tools, UX, Security) |
| **Systems** | 15 (LLMOps), 16 (RAG) |
| **Specialized** | 17-21 (OSS, Agents, Fine-tuning, SLMs, Model Families) |

---

## 5. Shared Infrastructure

### `shared/llm_providers.py`
```python
"""Unified interface for LLM providers."""
from langchain_openai import ChatOpenAI

def get_lmstudio_llm(model=None, temperature=0.1):
    """Get LM Studio LLM with consistent configuration."""
    import os
    return ChatOpenAI(
        model=model or os.getenv("DEFAULT_MODEL", "openai/gpt-oss-20b"),
        temperature=temperature,
        openai_api_key=os.getenv("LMSTUDIO_API_KEY", "lm-studio"),
        openai_api_base=os.getenv("LMSTUDIO_BASE_URL", "http://127.0.0.1:1234/v1"),
    )

def get_openai_llm(temperature=0.1):
    """Get OpenAI API LLM."""
    ...
```

### `shared/config.py`
```python
"""Centralized configuration."""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    lmstudio_base_url: str = "http://127.0.0.1:1234/v1"
    default_model: str = "openai/gpt-oss-20b"
    # ... other settings
```

---

## 6. Migration Checklist

- [ ] Create new directory structure
- [ ] Move existing files with preservation of git history
- [ ] Extract shared utilities (`shared/`)
- [ ] Create `.env.example` template
- [ ] Update `requirements.txt` with sectioned dependencies
- [ ] Add README files to each topic folder
- [ ] Verify all existing scripts still run after refactoring
- [ ] Add topic cross-references in documentation

---

## 7. Quick Start (Post-Migration)

```bash
# 1. Setup environment
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your configuration

# 2. Verify setup
python 01_setup/verify_setup.py

# 3. Run fundamentals
python 05_prompt_engineering_fundamentals/code/01_zero_shot.py

# 4. Explore agents
python 18_ai_agents/fundamentals/01_react_pattern.py

# 5. Build a RAG app
cd 16_rag_systems && python 01_basic_rag_pipeline.py
```

---

*End of Repository Redesign Document*
