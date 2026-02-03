# Topic 19: Fine-Tuning Large Language Models

> Customize models for specific tasks with domain data: LoRA, PEFT, evaluation.

## Learning Objectives

By the end of this topic, you will:
- Decide when to fine-tune vs prompt engineer
- Prepare datasets for instruction tuning
- Implement LoRA/QLoRA training
- Evaluate fine-tuned models

## Folder Structure

```
19_fine_tuning/
├── README.md
├── notes/
│   ├── when_to_finetune.md
│   ├── data_preparation.md
│   ├── peft_lora_explained.md
│   └── evaluation_after_finetune.md
├── code/
│   ├── 01_prepare_dataset.py
│   ├── 02_lora_finetune.py
│   └── 03_inference_finetuned.py
└── configs/
    └── lora_config.yaml
```

## When to Fine-Tune

### Prompt Engineering Better For:
- Few examples available (<100)
- Task fits existing knowledge
- Rapid iteration needed
- Multiple similar tasks

### Fine-Tuning Better For:
- Specific style/voice needed
- Consistent output format
- Large domain-specific dataset
- Reducing token usage

## PEFT Methods

| Method | Parameters | VRAM |
|--------|------------|------|
| Full Fine-tuning | 100% | Very High |
| LoRA | 1-2% | Medium |
| QLoRA | 1-2% | Low |
| Prefix Tuning | 0.1% | Low |

## Running Examples

```bash
# Prepare dataset
python 19_fine_tuning/code/01_prepare_dataset.py

# LoRA training
python 19_fine_tuning/code/02_lora_finetune.py
```

## Cross-References

- **Previous**: [18_ai_agents/](../18_ai_agents/)
- **Next**: [20_small_language_models/](../20_small_language_models/)

## Resources

- [PEFT Documentation](https://huggingface.co/docs/peft/)
- [LoRA Paper](https://arxiv.org/abs/2106.09685)
