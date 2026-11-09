---
title: AI Agent Memory Systems - August 2026 Landscape
description: "TencentDB Agent Memory is a local-first team memory hub for AI agents: four memory assets, a layered recall pyramid, and a Hermes plugin path."
last_updated: 2026-11-08
canonical: "https://www.corpusiq.io/docs/hermes/guides/ai-agent-memory-landscape-aug2026/"
robots: "index,follow"
tags: ["hermes agent", "ai agent", "nous research"]

---

# AI Agent Memory Systems - August 2026 Landscape

## TencentDB Agent Memory

Tencent Cloud open-sourced [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) (repository created April 2026, v2.0.3 released October 2026, roughly 30,600 stars). It is a team-level memory hub that turns conversations, documents and code into four reusable assets: Chat Memory, Skills, LLM-Wiki and a Code-Graph.

Numbers from the repository's own benchmark table, measured with OpenClaw:

- 61.38 percent fewer tokens (221.31M to 85.64M)
- 51.52 percent relative pass-rate gain on WideSearch (33 percent to 50 percent)
- PersonaMem accuracy 48 percent to 76 percent, a 59 percent relative gain

The architecture is a semantic pyramid rather than a flat vector pile: L0 Conversation (raw dialogue) to L1 Atom (atomic facts) to L2 Scenario (scene blocks) to L3 Persona (user profile). Raw evidence is persisted in databases for full-text retrieval, and the distilled persona and scene layers are stored as human-readable Markdown, so every abstraction has a drill-down path back to the source text.

It ships a Hermes plugin as well as the OpenClaw one: the `memory_tencentdb` provider installs from npm, or as a Docker image that bundles hermes-agent and the gateway.

## How It Compares to Existing Memory Systems

### Sibyl-Memory (CorpusIQ stack)
- SQLite-backed FTS5 search with four tiers (warm entities, hot state, cold journal, reference docs)
- 95.6 percent LongMemEval score - ranked second globally
- Survives restarts, crashes, and model switches
- CorpusIQ integration: canonical facts, metric specs, source-of-truth registry

### Honcho (Nous Research)
- Session-based memory derivation with peer-aware context
- Dream cycles for memory consolidation
- Conversation-level granularity with semantic search

### GBrain
- Knowledge graph layer with embedded search
- Session handoff pages for cross-session continuity
- Works alongside Sibyl and Honcho as the third memory tier

### Mem0 / MemGPT
- Earlier generation cloud-dependent memory
- API-based retrieval with managed embedding stores
- Higher latency, lower privacy

## What Tencent DB Changes

Tencent entering the local memory space validates the approach CorpusIQ has been using since June 2026. The architecture patterns are converging:

1. Local-first storage - no customer data leaves the machine
2. Vector + keyword hybrid retrieval - FTS5 plus embeddings
3. Tiered recall - working memory, recent context, long-term archive
4. Cross-session persistence - memory survives restarts

The 51.52 percent pass-rate gain lines up with what we see in practice: structured memory removes the repeated context recovery that burns turns. The 61.38 percent token reduction comes from the same place - smaller working contexts because the agent recalls the distilled layer instead of re-reading the transcript.

## Competitive Positioning

Tencent DB Agent Memory is open source and developer-focused. It does not ship with:
- Business tool connectors
- Canonical fact registry
- Source-of-truth manifest
- Metric specification DSL
- Cross-source validation

CorpusIQ combines the memory layer with the business data layer. The memory system remembers what the AI learned. The integration layer gives it live data to learn from.
