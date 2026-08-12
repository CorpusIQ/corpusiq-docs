---
title: Agentic Memory MCP — Persistent Memory for AI Agents
description: "Setup and usage guide for Agentic Memory MCP — Persistent Memory for AI Agents. Part of the Hermes resource directory."
last_updated: 2026-08-12
---

# Agentic Memory MCP — Persistent Memory for AI Agents

**Priority:** MEDIUM | **Category:** Knowledge & Memory / Infrastructure  
**Transport:** Remote SSE + stdio fallback | **Auth:** API key (Bearer)  
**Repository:** [jyswee/agenticmemory](https://github.com/jyswee/agenticmemory)  
**Website:** https://agenticmemory.ai  
**npm:** `agmry`  
**Pricing:** 7-day free trial → $24.99/mo Pro  
**Discovered:** July 27, 2026 (chatmcp/mcpso #3295)

## What It Does for Operators

Persistent memory for AI agents with ordered conversation history, key-value context, semantic search across sessions, and FIFO queues for agent-to-agent work handoff. Redis on the hot path (sub-ms reads) with durable storage behind it. Per-tenant isolation so an entire fleet of agents shares one memory space.

**For operators running multi-agent workflows:** This is the shared memory layer that lets agents hand off work, share context, and maintain state across sessions without a custom database.

## Installation

```bash
# Remote SSE (zero install):
# Endpoint: https://mcp.agenticmemory.ai/sse

# Local stdio:
npx -y agmry mcp-serve

# Quick signup (no browser, no card):
npx agmry signup my-project
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "agentic-memory": {
      "url": "https://mcp.agenticmemory.ai/sse",
      "transport": "sse",
      "headers": {
        "Authorization": "Bearer amk_YOUR_KEY"
      }
    }
  }
}
```

## Tools (17)

| Category | Tools | Description |
|----------|-------|-------------|
| Memory | `store`, `recall`, `search` | Persistent key-value + semantic search |
| Context | `context_set`, `context_get`, `context_list` | Session-scoped context management |
| History | `history_add`, `history_get`, `history_search` | Ordered conversation history |
| Queue | `queue_push`, `queue_pop`, `queue_peek` | FIFO work handoff between agents |
| Management | `create_space`, `list_spaces`, `bootstrap` | Tenant/space isolation |

## Operator Use Cases

1. **Multi-agent orchestration:** Agent A processes leads → pushes qualified leads to queue → Agent B picks up and sends proposals. Shared memory ensures no double-handling
2. **Customer context persistence:** Support agent recalls full conversation history + preferences when a returning customer reaches out, regardless of which agent handled the previous interaction
3. **Cross-session project state:** Operator's agent remembers project milestones, decisions, and action items across sessions without re-prompting
4. **Agent fleet management:** All agents share one memory space with per-tenant isolation — update company info once, all agents immediately have it
5. **Compliance audit trail:** Ordered history provides a complete audit trail of what each agent knew and did

## CorpusIQ Angle

**Infrastructure complement.** CorpusIQ's agent fleet (growth, support, dev, BD) could use Agentic Memory as the shared state layer — replacing session-DB workarounds with a purpose-built memory fabric. The queue system could formalize handoffs between agents (e.g., growth agent qualifies lead → BD agent receives via queue).

## Limitations

- $24.99/mo Pro after 7-day trial
- Remote SSE depends on agenticmemory.ai uptime
- New product (v1.8.0), may have growing pains
- Queue system is FIFO only (no priority queues, dead-letter queues)
