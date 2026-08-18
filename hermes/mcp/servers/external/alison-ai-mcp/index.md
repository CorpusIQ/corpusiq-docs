---
title: "Alison AI MCP - CorpusIQ Docs - CorpusIQ Docs"
description: Read creative-performance analytics from your ad accounts — spend, KPIs, creative tags, and competitor intelligence — inside any MCP client
category: Marketing
stars: n/a (new listing)
added: 2026-08-13
source: mcpservers.org
relevance: ★★★
tags: [ad-analytics, creative-intelligence, marketing, competitive-intelligence, kpi, oauth, remote-mcp]
---

# Alison AI MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1) for Alison AI's Evo — creative intelligence from your ad accounts inside any MCP client.** Point Claude Code, Claude, Cursor, or Codex at Evo and it reads the creative-performance warehouse directly: spend and KPIs, creative tags, competitor intelligence sourced from SensorTower and Pathmatics, and creative previews. The surface is the same analytics engine Evo's own analyst agent runs on. Read-only by design — 14 tools, no write path, no SQL to author.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 PKCE + RFC 7591 dynamic client registration (one browser sign-in)
Endpoint: https://evo.alison.ai/mcp
Tools: 14 (13 analytics + creative previews)
Pricing: Included with Evo product access (alison.ai)
Category: Marketing Analytics
Built by: Alison AI (alison.ai)
```

## Why This Matters for Operators

The creative-performance question — "which creative is actually driving the spend we're paying for" — normally lives in a BI dashboard that nobody opens during a campaign review. Evo's MCP puts the same numbers inside the agent that is already writing the recap. The agent asks, the warehouse answers, and the analysis lands in chat with the numbers attached.

**The grant is the security model.** OAuth 2.1 with PKCE and dynamic client registration means no API key ever leaves the platform. On sign-in you pick which product the client may read, and that choice is the ceiling on everything the client can ever see. Every request re-resolves authorization from the store — revocation is immediate, and a token scoped to accounts with no servable data is refused outright rather than handed zeroes.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `scope_overview` | One call to orient: what you can measure, what you can group by, and the rules that apply. Start here. |
| `list_integrations` | Ad-network connections in scope, with metadata |
| `describe_integrations` | Per-integration coverage, freshness, MMP and custom metrics |
| `list_kpis` | Available KPIs, raw metrics and dimensions, tiered to keep context small |
| `list_features` | Annotation features and their tag values for given integrations |
| `discover_filters` | Real filter values available for a scope and date range |
| `describe_marketing_entity` | Campaign / ad-group / ad metadata from the marketing catalog |
| `get_asset_labels` | Annotation labels for specific assets |
| `run_report` | Compose and execute a report: metrics × dimensions × filters over a date range |
| `run_recipe` | Run a pre-composed analysis from the recipe catalog in one call (tag pairs, KPI trend, top performers, annotation coverage, banded uplift) |
| `list_competition_metrics` | SensorTower / Pathmatics measures and dimensions |
| `discover_competition_filters` | Distinct competition values: country, OS, ad type, competitor name |
| `run_competition_report` | Query competitor creatives and share of voice |
| `get_creative` | Public thumbnail / preview URLs for creative ids you already hold (batch up to 25 per call) |

Report rows carry creative ids, not images — pass the ids from `run_report`, `run_recipe`, or `run_competition_report` into one batched `get_creative` call to see the creatives.

## Installation

```bash
claude mcp add --transport http evo https://evo.alison.ai/mcp
```

Then run `/mcp`, pick `evo`, and authenticate — the browser opens on the Evo sign-in page, you choose a product and approve, and the client keeps the token it is handed. Pre-approving every tool is safe: all 14 are read-only and none spends model budget.

## Configuration

```json
{
  "mcpServers": {
    "evo": {
      "type": "http",
      "url": "https://evo.alison.ai/mcp"
    }
  }
}
```

The client's first call returns `401` with a `WWW-Authenticate` header pointing at `/.well-known/oauth-protected-resource/mcp` — the client registers itself, opens the Evo approval page, and the server mints the token. Revoke any client from `GET /api/keys` and `DELETE /api/keys/{id}`; revocation is immediate, never cached.

## Business Relevance

- **Growth leads** get creative-tag analysis (winning hooks, formats, angles) inside the agent that writes the ad briefs — the loop from data to next creative closes in one chat
- **Performance marketers** run KPI reports and banded-uplift recipes without learning a BI tool, and never touch a SQL editor
- **Brand teams** see competitor creatives and share of voice through `run_competition_report` — SensorTower/Pathmatics data through a chat interface
- **Agency account managers** connect once per client product; the grant keeps each client's data isolated to its own approval
- **Finance stakeholders** get read-only access with no spend capability — the surface cannot mutate, cannot launch, cannot spend model budget

## Integration with CorpusIQ

Alison AI and CorpusIQ answer the two halves of the same question. CorpusIQ connectors — Meta Ads, Google Ads, LinkedIn Ads — pull cross-channel spend and revenue into one view with CorpusIQ's read-only external-source retrieval model. Evo's MCP adds the creative layer those connectors don't carry: which tags, hooks, and formats are moving the numbers, plus SensorTower/Pathmatics competition metrics.

The composed workflow: CorpusIQ resolves "what did we spend and what did it return across Meta, Google, and LinkedIn," while the Evo MCP inside the same agent session resolves "which creatives drove it, which tags repeat across winners, and what competitors are running." Both surfaces are read-only and grant-scoped, so a growth analyst can be given both without handing over campaign edit rights or spend capability.

## Limitations

- Brand new listing — no track record yet (Aug 13, 2026)
- Requires an Evo (alison.ai) product account; the MCP is not a standalone subscription
- Read-only: no campaign edits, no budget changes through this surface
- Commercial platform — no self-host option
- Browser OAuth flow per client; multiple clients mean multiple approvals to manage

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
