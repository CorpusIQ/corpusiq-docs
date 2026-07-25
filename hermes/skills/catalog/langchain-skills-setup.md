---
title: LangChain Agent Skills — Memory, RAG, Persistence, and Middleware for Hermes Agents
description: LangChain's official agent skills — deep agents memory, LangGraph persistence, RAG, fundamentals, human-in-the-loop, and middleware. 71K+ combined installs across 6 skills. Essential for Hermes agents building production AI workflows.
---

# LangChain Agent Skills — Setup Guide

**Source:** [langchain-ai/langchain-skills](https://skills.sh/langchain-ai/langchain-skills) (71K+ combined installs)
**GitHub:** [langchain-ai/langchain-skills](https://github.com/langchain-ai/langchain-skills) (996 ⭐)
**Category:** Agent Infrastructure / Memory & Orchestration
**Quality Tier:** 🟢 Production

LangChain is the dominant framework for building AI agent applications. Their official agent skills teach agents how to implement production-grade memory systems, retrieval-augmented generation (RAG), LangGraph persistence, human-in-the-loop workflows, and middleware patterns. For Hermes agents building or operating AI workflows, these skills provide the canonical implementation patterns from the team that defined modern agent architecture.

---

## Installation

```bash
# Core agent infrastructure
npx skills add langchain-ai/langchain-skills --skill deep-agents-memory
npx skills add langchain-ai/langchain-skills --skill langchain-fundamentals

# Persistence & state management
npx skills add langchain-ai/langchain-skills --skill langgraph-persistence

# Knowledge & retrieval
npx skills add langchain-ai/langchain-skills --skill langchain-rag

# Advanced patterns
npx skills add langchain-ai/langchain-skills --skill langgraph-human-in-the-loop
npx skills add langchain-ai/langchain-skills --skill langchain-middleware
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **deep-agents-memory** | 13.1K | Pluggable memory backends — ephemeral, persistent, filesystem, and composite routing |
| **langgraph-persistence** | 11.8K | Durable state persistence for LangGraph workflows — checkpointing, replay, branching |
| **langchain-rag** | 11.7K | Retrieval-augmented generation — document loading, chunking, embedding, retrieval chains |
| **langchain-fundamentals** | 11.6K | Core LangChain concepts — chains, prompts, models, output parsers, and LCEL |
| **langgraph-human-in-the-loop** | 11.3K | Approval gates, interrupt points, and human review workflows in agent pipelines |
| **langchain-middleware** | 10.8K | Request/response middleware — logging, rate limiting, caching, error handling |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python 3.9+** | LangChain ecosystem requires Python |
| **langchain + langgraph** | `pip install langchain langgraph` |
| **API keys** | OpenAI, Anthropic, or local LLM (Ollama) for agent execution |
| **Vector store (for RAG)** | ChromaDB, Pinecone, or pgvector for production RAG |

---

## Key Capabilities

### Deep Agents Memory (13.1K installs)
Pluggable memory architecture for AI agents — the most critical infrastructure decision for any agent project. Four backend strategies: `StateBackend` (ephemeral, per-thread), `StoreBackend` (persistent, cross-session), `FilesystemMiddleware` (file-based storage with automatic serialization), and `CompositeBackend` (intelligent routing across backends). Choose the right memory architecture for your agent's persistence requirements. Previously documented as a standalone guide — this publisher-level guide supersedes and expands that coverage.

### LangGraph Persistence (11.8K installs)
Production-grade state persistence for multi-step agent workflows. LangGraph's checkpointing system enables workflow resumption, branching (try alternative paths from any checkpoint), replay (re-execute with modified parameters), and cross-session state continuity. Essential for Hermes agents running long-running workflows that span multiple sessions or require recovery from interruptions.

### LangChain RAG (11.7K installs)
Complete retrieval-augmented generation pipeline: document loaders (PDF, HTML, Markdown, code), chunking strategies (fixed-size, semantic, recursive), embedding models (OpenAI, Cohere, local), vector stores, and retrieval chains. The most-installed RAG implementation pattern — canonical reference for building knowledge-grounding systems.

### LangChain Fundamentals (11.6K installs)
Core concepts every agent builder needs: chains (sequential, parallel, conditional), prompt templates, model abstraction layer (unified interface across 30+ LLM providers), output parsers (structured JSON, Pydantic models), and LangChain Expression Language (LCEL) for declarative pipeline composition.

### Human-in-the-Loop (11.3K installs)
Patterns for inserting human judgment into autonomous agent workflows: approval gates before destructive actions, interrupt points for ambiguous decisions, review-and-approve cycles for generated content, and escalation triggers when confidence drops below thresholds. Critical for deploying agents in production environments where full autonomy isn't appropriate.

### Middleware (10.8K installs)
Cross-cutting concerns for agent pipelines: request/response logging, rate limiting protection, caching layers (reduce redundant LLM calls), error handling and retry logic, and telemetry hooks. Applies to any LangChain pipeline regardless of the specific tools or models used.

---

## Quick Start

```bash
# 1. Install the skills your agent needs most
npx skills add langchain-ai/langchain-skills --skill langchain-fundamentals
npx skills add langchain-ai/langchain-skills --skill deep-agents-memory

# 2. Verify installation
npx skills list | grep langchain

# 3. Use in an agent session — the skills auto-register
# Your agent now has canonical LangChain patterns for memory and pipelines
```

---

## Verification

```bash
# Check installed LangChain skills
npx skills list | grep langchain

# Expected output (example):
#   langchain-ai/langchain-skills@deep-agents-memory
#   langchain-ai/langchain-skills@langchain-fundamentals
```

---

## Notes

- **Industry standard**: LangChain is the most widely adopted agent framework. These skills encode battle-tested patterns from millions of production deployments.
- **Supersedes standalone guide**: The `deep-agents-memory-setup.md` catalog entry documented one skill. This publisher-level guide covers all 6 LangChain agent skills.
- **Complementary to GBrain**: LangChain's memory backends provide agent-level persistence; GBrain provides semantic/knowledge-graph level persistence. They work at different layers.
- **Local LLM support**: LangChain's model abstraction works with Ollama and other local LLMs — no cloud API required for development.
- **Python-only**: These skills assume Python runtime. For TypeScript/Node.js agents, see the LangChain.js ecosystem separately.
