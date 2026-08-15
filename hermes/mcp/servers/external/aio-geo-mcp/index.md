---
title: AIO.GEO MCP
description: Structural AI search readiness over MCP — audit how AI engines see your site, dry-run fixes, rescore, and doctor, with receipts instead of LLM-ranking theater.
category: SEO
stars: n/a (new listing)
added: 2026-08-15
source: mcpservers.org
relevance: ★★★
tags: [geo, aeo, ai-search, ai-visibility, seo-audit, llms-txt, agent-skills, self-hosted]
---

# AIO.GEO MCP

**MCP server (stdio, self-hosted via npx)** — AIO.GEO is a structural AI Search Readiness platform: it audits what AI engines can see of your site, dry-runs fixes, rescores, and doctors the gaps. The positioning is explicitly anti-vanity-metrics — "we do not sell LLM rankings; nobody can measure them honestly. We sell what can be measured: structure, accessibility, and receipts to prove it."

```
Server type: Self-hosted (stdio via npx)
Auth: None published for the MCP server
Endpoint: npx -y @aio-geo/mcp-server (local)
Tools: audit, dry-run fixes, rescore, doctor
Pricing: Free CLI + MCP; hosted API at aiogeoprotocol.com
Category: SEO / GEO (Generative Engine Optimization)
Built by: AIO.GEO (aiogeoprotocol.com)
```

## Why This Matters for Operators

AI answer engines decide what to cite from machine-readable structure — llms.txt, clean markup, schema, and accessibility — not from backlink counts. Most teams are flying blind on whether their site is legible to those engines at all. AIO.GEO audits the structural layer, shows the agent exactly what is missing, dry-runs the fixes before anything ships, and rescues the score after.

**The mechanism that matters is the dry-run** — fixes are validated before they touch production, and every pass produces receipts an operator can hand a client or a board, instead of a ranking score nobody can reproduce.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `audit` | Structural audit of what AI engines can see — run via MCP, CLI (`npx @aio-geo/cli@0.3.4 audit example.com`), or the public API |
| `dry-run fixes` | Simulate remediation before applying it to the live site |
| `rescore` | Re-measure after fixes, with a machine-readable record of the delta |
| `doctor` | Diagnose specific blockers (accessibility, schema, llms.txt coverage) |

## Installation

```bash
# MCP server
npx -y @aio-geo/mcp-server
# CLI audit
npx @aio-geo/cli@0.3.4 audit example.com
```

Hosted equivalents: `POST https://www.aiogeoprotocol.com/api/v1/public/audit` and `/api/v1/public/brief`. The platform publishes a full machine catalog — `/.well-known/mcp/server-card.json`, `/.well-known/api-catalog`, `/.well-known/agent-skills/index.json`, plus `/llms.txt` and `/openapi.json`.

## Configuration

```json
{
  "mcpServers": {
    "aio-geo": {
      "command": "npx",
      "args": ["-y", "@aio-geo/mcp-server"]
    }
  }
}
```

Auth notes: the MCP server is local and requires no key. The public hosted API accepts direct POST calls for one-off audits and briefs.

## Business Relevance

- **SEO and content operators** get an honest, structural AI-visibility baseline instead of LLM-ranking theater
- **Agencies** get receipts — dry-run diffs and rescore records they can show clients
- **Docs and developer-relations teams** get llms.txt and machine-catalog coverage checks that most SEO tooling ignores
- **Founders competing in AI answers** get a fix list their agent can execute and re-verify in the same session

## Integration with CorpusIQ

AIO.GEO is the natural companion to CorpusIQ's own SEO/AEO/GEO stack. The CorpusIQ docs pipeline already ships llms.txt, JSON-LD, and sitemaps — run AIO.GEO's audit against the docs site after every deploy to catch regressions before the AI engines do, and use the Search Console and Bing Webmaster connectors to watch whether AI-referral traffic moves after each structural fix. For consulting-style engagements, compose the audit receipts with the Google Ads and GA4 connectors to show a client the full loop: structural fix → crawl delta → visible traffic change.

## Limitations

- Brand new listing — no long track record yet
- stdio/local server — the hosted API is the commercial product, and it is separate from the MCP surface
- Scope is structural AI readiness — it will not tell you why humans convert
- No LLM rankings by design — if your team needs ranking numbers, pair with Semrush or Ahrefs connectors
- Fixes are dry-run by default; applying them to production is still your pipeline's job

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
