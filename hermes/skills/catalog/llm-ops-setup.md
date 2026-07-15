---
title: LLM-OPS — Setup Guide
description: LLM Operations skill covering RAG, embeddings, vector databases, fine-tuning, prompt engineering, cost management, and production AI architectures.
---

# LLM-OPS — Setup Guide

## Prerequisites
- **Node.js 18+** (for npx)
- Any supported agent: Claude Code, Antigravity, Cursor, Gemini CLI, or Codex CLI
- Basic understanding of LLM concepts (RAG, embeddings, vector DBs)

## Capabilities

| Capability | Description |
|-----------|-------------|
| **RAG Implementation** | Build retrieval-augmented generation pipelines |
| **Embeddings** | Create and manage embeddings with Pinecone, Chroma, pgvector |
| **Vector Databases** | Select and configure the right vector store for your use case |
| **Fine-Tuning** | Fine-tuning workflows for domain-specific models |
| **Prompt Engineering** | Advanced prompt design patterns |
| **Cost Management** | Track and reduce LLM API costs |
| **Quality Evaluations** | Eval frameworks for model output quality |
| **Semantic Caching** | Cache LLM responses to reduce latency and cost |
| **Streaming** | Real-time streaming response architectures |
| **Agent Architectures** | Production AI agent design patterns |

## Installation

```bash
npx skills add sickn33/antigravity-awesome-skills/llm-ops
```

## Quick Start

Trigger the skill when you need specialized LLM operations assistance:

- "Set up a RAG pipeline for our documentation"
- "Compare Pinecone vs Chroma for our use case"
- "Optimize our LLM costs — we're spending too much on API calls"
- "Design an eval framework for our agent responses"
- "Implement semantic caching for repeated queries"

## Key Patterns

### RAG Pipeline Architecture

```
Documents → Chunking → Embeddings → Vector Store → Retrieval → LLM → Response
```

### Cost Optimization Strategies

| Strategy | Savings | Complexity |
|----------|---------|------------|
| Semantic caching | 30-60% | Low |
| Prompt compression | 20-40% | Medium |
| Model routing (cheap model for easy queries) | 40-70% | Medium |
| Batch processing | 50% | Low (if latency-tolerant) |
| Fine-tuned small models | 60-80% | High |

### Vector Database Selection

| Database | Best For | Limitations |
|----------|----------|-------------|
| **Pinecone** | Managed, zero-ops, fast | Cost at scale, vendor lock-in |
| **Chroma** | Local dev, open source | Not production-hardened |
| **pgvector** | Postgres-native, SQL queries | Slower than purpose-built |
| **Weaviate** | Hybrid search, GraphQL | Complex setup |
| **Qdrant** | Rust performance, filtering | Smaller ecosystem |

## CorpusIQ Use Cases

1. **Agent Knowledge Base:** Build RAG pipelines over the CorpusIQ docs, Hermes operating protocols, and governance rules — agents query their own knowledge base instead of relying on training data.

2. **Cost Tracking:** Monitor and optimize LLM spend across all CorpusIQ agents (Sonnet, Opus, DeepSeek, Qwen). Route queries to the cheapest capable model.

3. **Quality Evaluations:** Implement eval suites for agent responses — measure accuracy, helpfulness, and safety before deploying new agent versions.

4. **Semantic Caching:** Cache frequent agent queries (e.g., "What's the preflight gate?") to reduce API costs by 30-60%.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Embeddings dimension mismatch | Wrong model selected | Match embedding dimension to vector DB config |
| RAG returns irrelevant chunks | Chunk size too large/small | Tune chunk size (500-1000 tokens optimal) |
| Cost still high after caching | Cache miss rate too high | Widen cache key matching (semantic, not exact) |
| Fine-tuning job fails | Insufficient training data | Minimum 100 examples for LoRA fine-tuning |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
*↑ [Skills Home](/hermes/skills/)*

---

*Curated by CorpusIQ — one MCP endpoint, all your business tools. Content remains attributed to original authors and repositories.*
