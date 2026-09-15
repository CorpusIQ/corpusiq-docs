---
title: "Agentic Atlas MCP - Field-Tested Agent-System Design Patterns"
description: "Read-only MCP consultation surface for field-tested agent-system design patterns. Five keyless tools (orient, cards, read, links, navigate) over one versioned Release v1.0.6, served stateless at agentic-atlas.dev/mcp."
category: AI Agents
stars: n/a (new listing)
added: 2026-08-24
source: "mcp.so feed + live endpoint probe — refreshed 2026-09-08 for Release v1.0.6 (5 tools verified)"
relevance: ★★
tags: [agents, design-patterns, architecture, knowledge, agent-engineering, read-only, remote-mcp]
---

# Agentic Atlas MCP

**Public, read-only consultation surface for field-tested agent-system design patterns** - a hosted knowledge corpus that both people and agents can read, published by [agentic-atlas.dev](https://agentic-atlas.dev/). Five keyless tools map ordinary design vocabulary to canonical patterns, read the corpus at card, section, or full-node depth, and traverse relationships between nodes. Live-probed Release v1.0.6, served stateless at [https://agentic-atlas.dev/mcp/](https://agentic-atlas.dev/mcp/) (protocol 2025-06-18) - no account, no credentials.

```
Server type: Remote (Streamable HTTP, hosted, stateless)
Auth: None
Release: v1.0.6 (serverInfo; registry: dev.agentic-atlas/atlas)
Website: https://agentic-atlas.dev/
Endpoint: https://agentic-atlas.dev/mcp/
Tools: 5 (live-probed 2026-09-08; protocol 2025-06-18)
Pricing: free
Category: AI & Agents
Built by: Avery Jones (github.com/aj604/agentic-atlas-plugin)
```

## Why This Matters for Operators

Agent systems fail in predictable ways - unbounded context, unclear ownership of decisions, drift between what was designed and what was shipped. Agentic Atlas is the reference layer for those failures: patterns that have been field-tested, with every card claim carrying its source address. **The corpus is served as one active Release (v1.0.6): the endpoint serves exactly that release, and a promotion replaces it wholesale** - no silent drift between what a caller read last week and what it reads now.

For a team building or buying agent infrastructure, this is a cheap, keyless way to have an agent consult established design practice before it invents one.

## Tools & Capabilities

5 read-only tools confirmed by live probe of Release v1.0.6 (2026-09-08):

| Tool | Purpose |
|---|---|
| atlas_orient | Entry point: discover canonical identity from an ordinary-language query (e.g. "context window budget") when no canonical id is known; ranks whole-word matches by how few subjects carry them |
| atlas_cards | Read 1-4 canonical ids as one ordered Card per id: identity, Hook, and sealed claims with source addresses |
| atlas_read | Read a complete Node - bare id: identity, hierarchy, Hook, and every Section |
| atlas_links | Page one subject's relationship occurrences, outbound then inbound, with direction and reference context |
| atlas_navigate | Read "tree" (canonical ordered traversal of every published node) or "tour" (publisher-curated path) |

The former `atlas_provenance`, `atlas_define`, and `atlas_decisions` tools were retired in Release v1.0.6; their capabilities are recovered through this five-tool grammar (provenance and publication decisions surface as source addresses on sealed card claims; glossary terms resolve through `atlas_orient` vocabulary matching). The endpoint also publishes a consultation contract and three companion workflow skills (`designing-agent-systems`, `reviewing-agent-designs`, `applying-a-pattern`) as resources for hosts implementing the draft MCP Skills Extension.

Calls are idempotent and read-only (annotated `readOnlyHint`), and results carry `scope` metadata (total/returned/truncated) with cursor pagination. An empty result is a successful empty payload, not an error.

## Installation

```bash
claude mcp add agentic-atlas --transport http https://agentic-atlas.dev/mcp/
```

No local installation, no account, no credentials. Works with Claude Code, Cursor, VS Code, Codex and any MCP-compatible client.

## Configuration

```json
{
  "mcpServers": {
    "agentic-atlas": {
      "type": "http",
      "url": "https://agentic-atlas.dev/mcp/"
    }
  }
}
```

The server is stateless: initialize returned no session ID and tools/list succeeds without one (MCP '26-style stateless transport). No API key of any kind.

## Business Relevance

- **Operators building agent systems** get a consultation surface for design decisions - when to add memory, how to structure approval gates, which patterns have held up in the field.
- **Architects reviewing agent stacks** get a source address on every card claim, so a design choice can be traced to its published evidence.
- **Teams onboarding agents** get a stable vocabulary and canonical naming layer that a new agent can read on first contact.

## Integration with CorpusIQ

CorpusIQ is the business-data layer (QuickBooks, Stripe, HubSpot, GA4 and 40+ more connectors); Agentic Atlas is the design-practice layer. A Hermes agent composing a workflow can consult Agentic Atlas for the pattern (how should approval gates and read-only contracts be structured?) and then execute against CorpusIQ for the data (what do the numbers say?). Design wisdom from Agentic Atlas, business truth from CorpusIQ.

## Limitations

- New listing (added Aug 24, 2026; refreshed Sep 8, 2026 for Release v1.0.6) - no long-term track record yet.
- Read-only consultation surface: it provides design guidance, not transactional APIs or execution.
- Single-source corpus: patterns reflect the publisher's curation and field testing, not an open contribution pool.
- No authentication means no personalization - every caller reads the same active Release.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [MCP Integration Guide](/docs/hermes/mcp) - connecting MCP servers to Hermes Agent
- [Truth Bear GAUGE MCP](/docs/hermes/mcp/servers/external/truth-bear-gauge) - verifiable government data with the same proof-first discipline
