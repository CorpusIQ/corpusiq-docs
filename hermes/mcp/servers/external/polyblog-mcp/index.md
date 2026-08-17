---
title: "Polyblog MCP - CorpusIQ Docs"
description: Manage multilingual articles, localization coverage, and editorial plans over MCP with OAuth — the content-ops layer for international sites.
category: Content
stars: n/a (new listing)
added: 2026-08-15
source: mcpservers.org
relevance: ★★
tags: [multilingual-content, localization, editorial-planning, content-ops, international-seo, oauth, remote-mcp]
---

# Polyblog MCP

**Remote MCP server (Streamable HTTP, OAuth)** — Polyblog is a multilingual publishing platform, and its MCP server hands agents the content-ops layer: manage articles across languages, track localization coverage, and maintain editorial plans. A parallel REST API lives at api.polyblog.io for non-MCP integrations.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth
Endpoint: https://mcp.polyblog.io/mcp
Tools: Article management, localization coverage, editorial plans (mirrors the REST API)
Pricing: Commercial platform (polyblog.io)
Category: Content / Multilingual Publishing
Built by: Polyblog (polyblog.io)
```

## Why This Matters for Operators

Running a site in ten languages usually means ten times the editorial bookkeeping — which article exists in which locale, what is still machine-only, what the human review queue looks like. Polyblog's MCP gives an agent that state directly, so a multilingual content program can be planned, tracked, and updated from inside any MCP client instead of a translation spreadsheet.

**The mechanism that matters is the localization-coverage view** — an agent can ask which locales are missing a given article and schedule the work, rather than discovering the gap after a reader bounces.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| Article management | Create, update, and read multilingual articles via OAuth |
| Localization coverage | Which articles exist in which locales, and where the gaps are |
| Editorial planning | Maintain and query the editorial calendar across locales |

The vendor publishes machine-readable discovery at `/.well-known/ai-catalog.json` and an agent plugin at `/.well-known/agent-plugins/polyblog/plugin.json`; the REST API at api.polyblog.io covers the same surface for non-MCP workflows.

## Installation

```bash
claude mcp add polyblog --transport http https://mcp.polyblog.io/mcp
```

First connect opens the OAuth browser flow; the session is reused afterward.

## Configuration

```json
{
  "mcpServers": {
    "polyblog": {
      "type": "http",
      "url": "https://mcp.polyblog.io/mcp"
    }
  }
}
```

Auth notes: OAuth only — no API-key mode published for the MCP endpoint.

## Business Relevance

- **International content teams** get localization gaps surfaced as queries instead of spreadsheet audits
- **SEO operators** get hreflang-scale coverage tracking without exporting CSVs
- **Editorial managers** get the calendar and the coverage state in one agent-queryable surface
- **Founders going multi-market** get a content-ops API their agent can drive end to end

## Integration with CorpusIQ

Polyblog composes with CorpusIQ's content and analytics connectors. A closed loop: GA4 and Search Console connectors identify which locales underperform, Polyblog MCP checks coverage and schedules the missing articles, and the Semrush connector verifies the international keywords actually start ranking after publication. For teams running the CorpusIQ worldwide-affiliate and localization programs, the editorial-plan tools give the agent the same calendar view the docs pipeline already maintains for llms.txt and sitemap coverage — one content-ops surface across both.

## Limitations

- Brand new MCP listing — no long track record yet
- OAuth only, so it is tied to the Polyblog platform account
- Tool list is described by the vendor, not independently enumerated — treat the REST API at api.polyblog.io as the contract
- Commercial SaaS; no self-host option published
- Useful mainly to teams already publishing (or planning) multilingual content

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
