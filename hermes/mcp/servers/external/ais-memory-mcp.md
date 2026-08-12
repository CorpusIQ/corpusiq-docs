---
title: AIS Memory MCP
description: "Setup and usage guide for AIS Memory MCP. Part of the Hermes resource directory."
last_updated: 2026-08-12
---

# AIS Memory MCP

**Category:** Knowledge / Memory / Identity  
**Transport:** Remote Streamable HTTP (+ stdio fallback via npx)  
**Auth:** OAuth (RFC 9728 discovery); zero API key to start — agent self-registers  
**Website:** https://aismemory.com  
**Pricing:** Free tier: 3 agents, 100MB, 10K API calls/month  
**npm:** aismemory  

## What It Does for Operators

AIS Memory gives AI agents persistent memory that survives every session, combined with W3C DID (Decentralized Identifier) identity. For business operators, this means AI agents can remember context across sessions, maintain identity across platforms, and build long-term knowledge about business operations — without losing everything when a session ends or a model switches.

## Installation

```bash
# Remote (recommended)
# Endpoint: https://ais.agentsandswarms.ai/mcp

# Local stdio fallback
npx aismemory
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "ais-memory": {
      "url": "https://ais.agentsandswarms.ai/mcp",
      "transport": "streamable-http"
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| Persistent memory store | Save/retrieve agent knowledge across sessions |
| W3C DID identity | Self-sovereign identity for AI agents |
| Memory search | Semantic search across stored agent memories |
| Agent registration | Self-registration on first contact (zero config) |
| Memory management | Organize, update, and prune agent knowledge |

## Operator Use Cases

1. **Cross-session agent continuity** — AI agents remember business context, decisions, and preferences across sessions
2. **Multi-agent knowledge sharing** — Share business intelligence across a fleet of specialized agents
3. **Compliance memory** — Store audit trails and compliance decisions with verifiable identity
4. **Customer context persistence** — Agents remember customer history, preferences, and past interactions
5. **Business knowledge base** — Build a persistent, queryable knowledge store from agent interactions over time

## CorpusIQ Angle

AIS Memory addresses a core challenge CorpusIQ operators face: agent amnesia between sessions. While CorpusIQ has internal memory systems (Honcho, GBrain, session DB), AIS Memory provides a standardized, MCP-native approach with W3C DID identity — potentially useful as an alternative or supplement to existing memory infrastructure. The free tier (3 agents, 100MB) makes it accessible for operators to test.

## Limitations

- Free tier limited to 3 agents, 100MB — may not scale for large operator deployments
- W3C DID identity adds complexity if not needed
- New service (July 2026), unproven at scale
- Part of agentsandswarms.ai ecosystem — vendor lock-in risk
- Remote-only for full features; stdio is fallback only
