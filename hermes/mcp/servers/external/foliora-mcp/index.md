---
title: "Foliora MCP - Managed AI Search Preview for Agents"
description: "Read-only Streamable HTTP MCP from Foliora, a managed AI-search (GEO/AEO) service that improves the public sources a company owns so it can be found on Google and cited by ChatGPT, Gemini, Claude and AI Overviews: 3 tools let an agent explain the product, build a preview link and fetch a snapshot a human started. No API key."
category: SEO
stars: n/a (hosted; docs-only)
added: 2026-08-27
source: "chatmcp/mcpso issue #3794"
relevance: ★★
tags: [geo, aeo, ai-search, llm-visibility, citations, preview, remote-mcp]
---

# Foliora MCP

**Hosted remote MCP server (Streamable HTTP, no auth at v0, read-only by design) for Foliora's managed AI-search service.** Foliora improves the public sources a company owns so it can be found on Google and cited by ChatGPT, Gemini, Claude, Grok and Google AI Overviews. Its MCP surface is deliberately narrow and safe: an agent can read what Foliora is, hand a human a preview link, or fetch a snapshot the human already started. It cannot crawl, take credentials or publish - humans still start the work.

```
Server type: Remote (Streamable HTTP)
Auth: None for v0
Endpoint: https://www.foliora.ai/mcp
Registry: ai.foliora/search (0.3.0)
Tools: 3 (all read-only)
Pricing: Free preview; see foliora.ai/pricing
Docs: https://www.foliora.ai/mcp · Skill: foliora.ai/skills/foliora/SKILL.md
Category: SEO
```

## Why This Matters for Operators

AI-search visibility (GEO/AEO) is becoming a revenue channel, but the work still needs a human to kick off a crawl and review findings. Foliora's MCP makes the agent the front door: it explains the service, creates a `/preview` link for any public website, and reads back the snapshot once the human starts it in a browser. **The guardrail is the feature - the agent can never crawl, hold credentials or publish, so handing an agent a Foliora connection is risk-free while the human does the judgment work.** Operators get GEO/AEO previews into their existing agent workflows without standing up audit infrastructure.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `get_product` | Foliora product facts: brand, plans, canonical URLs and what the server will not do |
| `get_snapshot` | Fetch a preview snapshot the human already started (32-character hex token from /preview/{token}); public findings and pages only |
| `create_preview_link` | Build a Foliora /preview URL for a public website and send the human there to start the snapshot |

REST names match MCP tool names exactly; the same handlers serve `/api/v1`.

## Installation

```bash
claude mcp add --transport http foliora https://www.foliora.ai/mcp
```

No key, no signup for the MCP surface. The human completes previews in the browser; the agent polls `get_snapshot` for the results.

## Configuration

```json
{
  "mcpServers": {
    "foliora": {
      "url": "https://www.foliora.ai/mcp"
    }
  }
}
```

## Business Relevance

- **Founders and marketing leads** get AI-citation previews into the agent they already use daily
- **SEO teams** hand a preview link to stakeholders instead of exporting reports
- **Agencies** let clients self-serve previews while the agency runs the actual GEO program
- **Operators new to GEO** get a zero-risk read-only entry point - the agent cannot change anything

## Integration with CorpusIQ

Foliora previews AI-search visibility; CorpusIQ measures what that visibility earns. An operator can run a Foliora preview on a landing page, apply the fixes, then track the resulting traffic and revenue through CorpusIQ's GA4 and Google Ads connectors - closing the loop from "are we citable" to "did citations move revenue". For CorpusIQ's own GEO program (docs.corpusiq.io), a Foliora snapshot on the docs domain gives a second read on AI-citability alongside the platform's internal checks.

## Limitations

- Brand new - v0 registry version, no public adoption track record yet
- Read-only by design: the agent cannot start a crawl itself, so workflows are human-gated
- Preview snapshots only - no full audit API over MCP yet
- No auth at v0 means the surface is product-facts plus preview plumbing, not account data

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
