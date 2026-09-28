---
title: "Cortex MCP - Shared Knowledge Base for Human-Agent Teams"
description: "Cortex is a shared knowledge base humans and AI agents read and write together, with 70+ permission-checked MCP tools."
category: Productivity
stars: n/a (new listing)
added: 2026-09-28
source: "mcpservers.org server page (cortex.page)"
relevance: ★★★
tags: [knowledge-base, notes, semantic-search, embeddings, knowledge-management, productivity, remote-mcp]
---

# Cortex MCP

**A knowledge substrate your whole agent fleet can share.** Cortex, built on the Nuclear Notes product at cortex.page, is a shared knowledge base where notes, links, embeddings and revision history live outside any single model vendor. Pages and reusable atoms carry typed metadata, and seventy-plus MCP tools mount at the instance with every action permission-checked, audited and reversible.

```
Server type: Remote (per-instance MCP, granted by the workspace owner)
Auth: instance grant, no integration code required
Endpoint: https://<your-instance>.cortex.page (per-instance)
Tools: 70+ (pages, atoms, semantic search, metadata, revisions, code docs)
Pricing: 1 private workspace free forever, 1 GB storage
Category: Productivity / Knowledge Management
Built by: Cortex / Nuclear Notes (cortex.page)
```

## Why This Matters for Operators

The knowledge operators accumulate, notes from calls, architecture decisions, runbooks, research libraries, dies with the chat thread when it lives in a model vendor. Cortex separates the substrate from the weights: your notes survive model swaps, and every agent you grant access to reads and writes the same corpus.

The atom model is the interesting part: reusable fragments transclude across pages and update everywhere they appear, so a pricing fact or a support runbook changes in one place and every document that cites it stays current.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Pages and atoms | Create and link knowledge fragments that update everywhere |
| Semantic search | Embeddings on every page and atom, neighbors without rereading |
| Structured metadata | Typed key-value data per page, filterable and queryable |
| Revisions | Full history with permission-checked, reversible actions |
| Code documentation | Agent watches a repo diff and keeps docs current |

Tool names are served from the instance endpoint; the table reflects the vendor's published capability set.

## Installation

```bash
claude mcp add cortex --transport http https://YOUR-INSTANCE.cortex.page
```

An agent can create the workspace on a human's behalf through the signup flow at cortex.page, the human claims it by magic link, then grants MCP access per agent.

## Configuration

```json
{
  "mcpServers": {
    "cortex": {
      "type": "http",
      "url": "https://YOUR-INSTANCE.cortex.page"
    }
  }
}
```

## Business Relevance

- **Founders** keep decisions and context in one place across every agent and model
- **Ops teams** maintain runbooks that update everywhere they are cited
- **Research-heavy teams** navigate libraries by semantic neighbors instead of rereading
- **Engineering leads** get living docs that follow the repo as agents review diffs

## Integration with CorpusIQ

Cortex is the memory layer between CorpusIQ's connectors and the operator. An agent pulls GA4 or Stripe findings, writes the analysis to Cortex with typed metadata, and every other agent in the fleet can query that conclusion later instead of recomputing it.

For runbook-style operations, Cortex pages can hold the canonical answers while CorpusIQ connectors supply the live data each time the question is asked, keeping the knowledge stable and the numbers fresh.

## Limitations

- New listing, no track record yet
- Endpoint is per-instance, provisioned at signup, not a single public URL
- Free tier limited to 1 GB and community support
- Tool names are not published; live catalog is served per instance

## FAQ

### Does my data leave my workspace?

Knowledge lives in your instance, not in a model vendor's weights. You grant MCP access per agent and can revoke it.

### How do I get an instance?

An agent can reserve one via the public signup flow, then you claim it by magic link and grant MCP access.

### What is an atom?

A reusable knowledge fragment that transcludes across pages and updates everywhere it appears, mirroring how small definitions compose into long-form work.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
