---
title: AutoLoRA — Self-Fine-Tuning Hermes Skill Setup Guide
description: Install and configure autolora — a Hermes skill that fine-tunes the agent on its own traces and hot-swaps the new model. Uses RunPod + Unsloth LoRA with Stripe-paid cost control.
---

# AutoLoRA — Setup Guide

**Source:** [DJLougen/autolora](https://github.com/DJLougen/autolora) · 1★
**Category:** Agent Infrastructure / Model Optimization
**License:** MIT · **Published:** June 28, 2026

AutoLoRA lets Hermes fine-tune itself. It curates successful agent traces (AUC-based selection), trains a LoRA adapter on RunPod using Unsloth, and hot-swaps the improved model into the active agent — all while keeping costs capped via Stripe payment thresholds. Set your benchmark targets, and AutoLoRA iterates until the agent meets them.

---

## How It Works

```
1. AUC TRACE CURATION
   Agent sessions scored → top-N traces extracted → formatted as training data

2. RUNPOD + UNSLOTH LORA
   Training job launched on RunPod GPU → Unsloth QLoRA fine-tune → adapter weights returned

3. STRIPE-PAID COST CONTROL
   Training costs charged to Stripe → hard cap prevents runaway spend

4. HOT-SWAP
   New LoRA adapter loaded → agent uses improved model immediately

5. BENCHMARK VERIFICATION
   User-defined benchmarks checked → if passed, keep; if not, iterate
```

---

## Installation

```bash
npx skills add DJLougen/autolora
```

### Prerequisites

| Requirement | Details |
|-------------|---------|
| **RunPod account** | API key with GPU access ([runpod.io](https://runpod.io)) |
| **Stripe account** | Payment method for training costs |
| **Hermes Agent** | v0.16.0+ with LoRA adapter support |
| **Training data** | At least 50+ successful agent sessions for meaningful fine-tuning |

```bash
export RUNPOD_API_KEY="<your-key>"
export STRIPE_API_KEY="<your-stripe-key>"
export AUTOLORA_SPEND_CAP="25"  # USD max per training run
```

Or in `~/.hermes/config.yaml`:

```yaml
env:
  RUNPOD_API_KEY: "<key>"
  STRIPE_API_KEY: "<key>"
  AUTOLORA_SPEND_CAP: "25"

skills:
  autolora:
    benchmark_threshold: 0.85
    max_iterations: 3
```

---

## Usage with Hermes Agent

```
"Run autolora — fine-tune on my last 100 sessions with a 0.90 benchmark target"
"Show autolora training status"
"Hot-swap to the latest autolora adapter"
```

### Commands

```bash
# Start a fine-tuning run
hermes skill run autolora --sessions 100 --target 0.85

# Check training status
hermes skill run autolora --status

# List available LoRA adapters
hermes skill run autolora --list-adapters

# Hot-swap to a specific adapter
hermes skill run autolora --swap adapter-2026-06-29-v3
```

---

## Cost Estimates

| Sessions | GPU Hours | Estimated Cost |
|----------|-----------|----------------|
| 50 | ~0.5 | ~$2-4 |
| 100 | ~1.0 | ~$4-8 |
| 500 | ~3.0 | ~$12-25 |
| 1000 | ~5.0 | ~$20-40 |

*Based on RunPod A6000 pricing. Set `AUTOLORA_SPEND_CAP` conservatively.*

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Domain adaptation | Fine-tune on customer-specific workflows |
| Style consistency | Train on preferred code patterns and documentation style |
| Error reduction | Curate only successful traces to reduce mistakes |
| Cost optimization | Better models → fewer tokens → lower API costs |

---

## Pitfalls

- Requires 50+ high-quality sessions before first run
- RunPod cold start adds 2-5 minutes to training time
- LoRA adapters are model-specific — won't transfer between base models
- Over-training on a narrow task can reduce general capability
- Benchmark against holdout tasks before deploying to production

---

*This guide is part of the [Hermes Skills Catalog](/hermes/skills/catalog/). Discovered June 29, 2026. Powered by CorpusIQ.*
