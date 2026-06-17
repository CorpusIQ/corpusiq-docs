---
title: NVIDIA DGX Spark — Primary Compute
description: Running Hermes Agent on NVIDIA DGX Spark for production inference, model routing, and 24/7 autonomous operations
---

# NVIDIA DGX Spark — Primary Compute

The DGX Spark serves as the primary inference and orchestration node for the CorpusIQ agent platform. It handles model inference, cron scheduling, memory management, and the majority of operational workloads.

## Hardware

NVIDIA GPU with CUDA support. Local inference eliminates API latency and cost for lightweight tasks. The machine runs 24/7 with automatic recovery for any agent process failures.

## Software Stack

### Hermes Agent
Primary orchestration framework. Upgraded from v0.15.1 to v0.16.0, incorporating 426 commits of new capabilities: model switching, fallback chains, browser tooling, skill bundles, and gateway integrations.

### Ollama Local Inference
```
ollama pull qwen3.6:27b
ollama pull deepseek-r1:32b
```
Local models handle routine tasks at zero cost with sub-100ms latency.

### Multi-Model Router
Task complexity determines model selection. Defaults to local models (Qwen, Ollama). Escalates to DeepSeek for complex reasoning and Claude Opus for strategic decisions. Approximately 65% cost savings compared to premium-model-only routing.

### GBrain Memory
Persistent knowledge layer: 729 indexed files, pglite database, nomic-embed-text embeddings at 768 dimensions. Nightly dream cycle consolidates knowledge at 03:00.

### Cron Infrastructure
24 scheduled processes: email monitoring, social publishing, video generation, knowledge consolidation, GitHub monitoring, reporting, and self-improvement cycles.

## Why DGX Spark
- Zero-cost local inference for routine tasks
- Data privacy — sensitive operations never leave the machine
- Sub-100ms latency for local models
- Silent 24/7 operation in workspace environment


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*
