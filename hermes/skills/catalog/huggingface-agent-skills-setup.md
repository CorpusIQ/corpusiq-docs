---
title: HuggingFace Agent Skills — Datasets, papers, vision, and ML tools for Hermes Agents
description: 6 ML/AI skills from HuggingFace covering datasets API, papers research, Transformers.js, vision training, and tool building. 7.9K+ combined installs, 10.8K GitHub stars.
---

# HuggingFace Agent Skills — Setup Guide

**Source:** [huggingface/skills](https://github.com/huggingface/skills) (10,876⭐, 7,900+ combined installs)
**Category:** AI Media / Research
**Quality Tier:** 🟢 Production

HuggingFace's official agent skills give Hermes agents direct access to the HuggingFace ecosystem — the world's largest repository of ML models, datasets, and research. These skills cover dataset exploration, academic paper discovery, browser-side ML with Transformers.js, vision model training, and custom tool building on the Hub.

---

## Installation

```bash
npx skills add huggingface/skills --skill huggingface-datasets
npx skills add huggingface/skills --skill huggingface-papers
npx skills add huggingface/skills --skill transformers-js
npx skills add huggingface/skills --skill huggingface-vision-trainer
npx skills add huggingface/skills --skill huggingface-trackio
npx skills add huggingface/skills --skill huggingface-tool-builder
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **huggingface-datasets** | 1.5K | Query the Dataset Viewer API — fetch metadata, paginate rows, search text, apply filters, download parquet URLs, and read statistics for any public dataset |
| **huggingface-papers** | 1.4K | Discover trending ML papers, search by keyword/category, read paper metadata. Hooks into HuggingFace's daily papers feed |
| **transformers-js** | 1.4K | Run Transformer models directly in the browser or Node.js — no server required. Covers pipelines, tokenizers, and model loading |
| **huggingface-vision-trainer** | 1.3K | Fine-tune vision models (image classification, object detection, segmentation) using HuggingFace's Trainer API |
| **huggingface-trackio** | 1.2K | Track model training runs, log metrics, compare experiments. Integration with HuggingFace's experiment tracking |
| **huggingface-tool-builder** | 1.1K | Build and publish custom tools on the HuggingFace Hub — create Spaces, deploy Gradio/Streamlit apps, manage model cards |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **HuggingFace account** | Free at [huggingface.co](https://huggingface.co) |
| **HF token** | Required for private/gated datasets and model publishing. Set as `HF_TOKEN` or `HUGGINGFACE_HUB_TOKEN` |
| **Python 3.8+** | Required for datasets, vision-trainer, and tool-builder skills |
| **Node.js 18+** | Required for Transformers.js |

---

## Key Capabilities

### Dataset Explorer
Query any of the 200K+ public datasets on HuggingFace without downloading. The Dataset Viewer API provides metadata, pagination, text search, and parquet export. Perfect for research, data discovery, and quick analysis.

### Paper Discovery
Stay current with ML research. The papers skill hooks into HuggingFace's daily trending papers — surfaced from arXiv, conferences, and community highlights. Search by keyword, category, or date range.

### Browser-Side ML
Transformers.js runs models directly in the browser or Node.js using ONNX Runtime. No Python, no server, no GPU needed. Supports text generation, embeddings, translation, image classification, and speech recognition.

### Vision Training
Fine-tune vision models with the Trainer API. Supports image classification, object detection, and semantic segmentation. Handles data loading, augmentation, training loops, and evaluation.

---

## Quick Start

```bash
# Search datasets
curl "https://datasets-server.huggingface.co/is-valid?dataset=imdb"

# List splits
curl "https://datasets-server.huggingface.co/splits?dataset=imdb"

# Get first rows
curl "https://datasets-server.huggingface.co/first-rows?dataset=imdb&config=default&split=train"

# Browse trending papers
curl -s "https://huggingface.co/papers" | grep -oP '<h3[^>]*>\s*<a[^>]*>\K[^<]+' | head -10
```

---

## Verification

```bash
npx skills list | grep huggingface
```

---

## Notes

- Gated datasets require `Authorization: Bearer <HF_TOKEN>` header on API calls
- Transformers.js uses quantized models for browser efficiency — model quality vs. size tradeoff
- Vision training skill requires CUDA-capable GPU for practical training times (or use HF Spaces with GPU)
- All skills are read-only by default; tool-builder and vision-trainer require write access to the Hub
- Papers search is complementary to arxiv-setup — HuggingFace papers have community discussion and model links that arXiv doesn't
