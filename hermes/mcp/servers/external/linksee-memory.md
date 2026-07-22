---
title: "Linksee Memory MCP — 6-Layer Cross-Agent Memory with Forgetting Curve"
description: "Linksee Memory MCP server — local-first cross-agent memory with 6-layer structure, Ebbinghaus-style forgetting curve, and drift detection. Catches when code diverges from past decisions."
category: mcp
tags: [mcp-server, memory, knowledge-management, cross-agent, local-first]
last_updated: 2026-07-19
---

# Linksee Memory MCP Server

Linksee Memory is a local-first cross-agent memory server that gives multiple AI agents shared persistent memory with a 6-layer structure. It implements an Ebbinghaus-style forgetting curve — memories decay over time unless reinforced — and drift detection that catches when your codebase or decisions diverge from what was previously agreed.

**Source:** awesome-mcp-servers PR #9079 (discovered July 19, 2026)
**Category:** Knowledge & Memory
**Author:** michielinksee
**Repo:** https://github.com/michielinksee/linksee-memory
**Status:** Active

## Why This Matters

The problem with most memory solutions is they're either too rigid (exact-match retrieval) or too shallow (single-layer storage). Linksee's 6-layer model mirrors how human teams actually remember things: some facts are hot (active sprint decisions), some warm (project conventions), some cold (historical rationale). The forgetting curve ensures stale information doesn't pollute retrieval — a memory that's never accessed naturally fades, just like in a real team.

The drift detection is the killer feature. It monitors whether your codebase still aligns with past architectural decisions recorded in memory. If it detects drift, it surfaces the original decision context so your agent can reconcile.

## Installation

```bash
# Via npm
npm install -g linksee-memory

# Or run directly
npx linksee-memory
```

## Claude Desktop / Hermes Configuration

```json
{
  "mcpServers": {
    "linksee-memory": {
      "command": "npx",
      "args": ["linksee-memory"],
      "env": {
        "LINKSEE_STORAGE_PATH": "~/.linksee-memory"
      }
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `store_memory` | Write a memory with layer assignment (1-6) and decay rate |
| `retrieve_memory` | Search across all layers with relevance scoring |
| `reinforce_memory` | Reset decay timer on an existing memory |
| `detect_drift` | Compare current state against stored architectural decisions |
| `list_layers` | Browse memory distribution across the 6 layers |

## 6-Layer Structure

| Layer | Name | Retention | Example |
|-------|------|-----------|---------|
| 1 | Ephemeral | Hours | Current debugging state |
| 2 | Session | Days | What I'm working on today |
| 3 | Task | Weeks | Feature implementation details |
| 4 | Project | Months | Architecture decisions, conventions |
| 5 | Domain | Years | Industry knowledge, patterns |
| 6 | Persistent | Forever | Core identity, immutable facts |

## CorpusIQ Relevance

Directly relevant to Hermes' multi-session memory problem. Linksee's forgetting curve + drift detection could complement Honcho (session context) and GBrain (knowledge graph) to create a 3-tier memory architecture: Honcho for hot session state → Linksee for decaying cross-session memory → GBrain for permanent knowledge.

## See Also

- [[sweeps/sweep-july19-2026]]
- Engram MCP
