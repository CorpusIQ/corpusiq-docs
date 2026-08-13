---
title: "Orcha MCP — Unified Context Layer for Organizations"
description: "Store, index, and expose organizational knowledge to AI agents. Files, structured databases, and connected sources in one workspace with permissions"
date: 2026-08-12
source: mcp.so
source_url: https://mcp.so/servers/orcha
category: Memory & Knowledge
rating: ★★★
status: active
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/orcha-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# Orcha MCP Server

## What is Orcha?

Orcha is a unified context layer for AI tools and agents. It stores, indexes, and exposes organizational, team, or individual knowledge. Files, structured databases, and connected sources live in one workspace, and agents reach them through MCP, CLI with virtual file system, or REST API — with permissions, citations, and provenance.

**Category:** Memory & Knowledge  
**Author:** westonhancock  
**Added:** August 12, 2026

## Why It Matters for Operators

The "context problem" is the #1 blocker for AI agents in business operations. Every session starts with amnesia — operators re-explain their business, products, customers, and processes. Orcha solves this by providing a persistent, permissioned knowledge layer that agents query directly.

This is fundamentally different from:
- **PLUR/AgenticMemory**: Session-level memory for coding agents
- **Notion MCP**: Document-level access to Notion pages
- **Groundwork**: Company memory with public proof

Orcha provides a *structured* knowledge layer with databases, typed queries, and connected sources — not just documents, but queryable business data.

## Connection Details

```json
{
  "mcpServers": {
    "orcha": {
      "type": "streamable-http",
      "url": "https://app.tryorcha.com/mcp"
    }
  }
}
```

**Transport:** Streamable HTTP (remote)  
**Auth:** Required (workspace-scoped)  
**Pricing:** Not yet published (early stage)

## Key Features

| Feature | Description |
|---------|-------------|
| **File System** | Read, create, update, organize, and delete files (permission-scoped) |
| **Context Bundles** | Curated sets of context with usage guidance (`list_bundles`, `get_bundle`) |
| **Structured Databases** | Typed queries against business data (`list_databases`, `query_database`, record CRUD) |
| **Connected Sources** | Direct read-only access to external sources (`query_source`, `fetch_source_document`) |
| **Virtual Filesystem** | Browse workspace as a tree: `ls`, `tree`, `find`, `cat`, `grep`, `stat` |
| **Permissions** | Role-based access control scoped to workspace members |
| **Citations** | Every response includes source provenance |

## Verified Use Cases

1. **Operator Knowledge Base** — Store SOPs, pricing, product specs, and customer data that agents query during every session
2. **Team Context Sharing** — Multiple agents across different tools (Claude, Cursor, ChatGPT) access the same organizational truth
3. **Agent-Ready Business Data** — Structured databases of customers, products, or deals that agents query via typed tools
4. **Source-Grounded Answers** — Agents cite specific files or database records in responses, eliminating hallucination

## CorpusIQ Integration Opportunity

**Priority: MEDIUM-HIGH.** Orcha could serve as the canonical knowledge layer for CorpusIQ operators:
- Product knowledge (features, pricing, roadmap)
- Customer data (segments, feedback, churn signals)
- Competitive intelligence (stored research, battlecards)
- Content guidelines (voice, positioning, compliance)

However, we already have Honcho + GBrain for agent memory and Git-based docs for product knowledge. Orcha would be most valuable for operators who want a GUI-managed knowledge base their agents query — a different use case than our current pipeline.

## Verdict

**★★★★☆ Strong concept, early execution.** The unified context layer approach — files + databases + sources, all permission-scoped — is the right architecture for organizational AI. Currently early-stage with thin public documentation. Worth monitoring, especially as it adds more structured database capabilities and source connectors.

## Resources

- **Homepage:** https://www.tryorcha.com/
- **Documentation:** https://www.tryorcha.com/docs
- **Repository:** https://github.com/westonhancock/orcha-mcp
- **mcp.so:** https://mcp.so/servers/orcha
