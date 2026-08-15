---
title: Seomely MCP
description: Google index monitoring with history over MCP — which pages are indexed, which dropped out and when, and why the rest are not, with an honesty flag on every submission recommendation.
category: SEO
stars: n/a (new listing)
added: 2026-08-15
source: mcpservers.org
relevance: ★★★
tags: [seo, index-monitoring, google-index, indexnow, search-visibility, sitemaps, technical-seo, remote-mcp]
---

# Seomely MCP

**Remote MCP server (Streamable HTTP, bearer API key)** — Seomely tracks Google indexing with history: which pages are indexed, which dropped out and when, and why the rest are not. The entire dashboard is available over REST and MCP with one API key and one shared monthly allowance, and the MCP tools mirror the REST endpoints one to one.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer API key (sk_live_...)
Endpoint: https://seomely.com/api/mcp
Tools: 12+ mirroring the REST endpoints (investigate, regressions, unindexed, orphans, indexnow, submit)
Pricing: Free 1,000 calls/mo · Pro 25,000 · Agency 250,000
Category: SEO / Index Monitoring
Built by: Seomely (seomely.com)
```

## Why This Matters for Operators

Search Console tells you what is indexed today. It does not tell you what quietly fell out of the index last week, or whether resubmitting a URL can possibly help. Seomely keeps per-URL observation history, correlates regressions with their shared cause, and ranks the remaining work by priority with reasons.

**The mechanism that matters is the `submission_helps` field** — every diagnosis carries it. When it is false, the cause is content or configuration, and resubmitting cannot change the outcome. Tools that promise indexing rely on people not knowing that; Seomely refuses to.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `investigate_indexing` | Correlate regressions with their shared cause, ranked by priority with reasons — start here |
| `get_regressions` | Pages that were indexed and are not now |
| `get_unindexed` | Everything not in the index, each with a cause and whether submitting helps |
| `get_orphans` | Pages with no inbound links from your own site |
| `get_url_status` | Current index state for one URL |
| `get_url_history` | Every observation held for one URL, newest first |
| `get_stats` | Coverage totals per property |
| `indexnow_setup` / `indexnow_autopilot` | Generate or register IndexNow keys; toggle nightly submission |
| `submit_urls` | Submit URLs to the IndexNow network; unhelpful submissions are reported as skipped |

## Installation

```bash
claude mcp add --transport http seomely https://seomely.com/api/mcp \
  --header "Authorization: Bearer sk_live_..."
```

Keys are minted at seomely.com/app/api-keys, shown once, and stored only as a hash. The server publishes a machine-readable card at `/.well-known/mcp.json` and an agent-facing overview at `/llms.txt`.

## Configuration

```json
{
  "mcpServers": {
    "seomely": {
      "type": "http",
      "url": "https://seomely.com/api/mcp",
      "headers": { "Authorization": "Bearer sk_live_..." }
    }
  }
}
```

Auth notes: one credential covers REST and MCP. Calls are metered per month per account — every response carries `x-api-calls-used` and `x-api-calls-limit`. Past the ceiling you get `429 quota_exceeded` until the 1st; there is no per-second throttle. Google's 2,000-URLs-per-property-per-day inspection allowance is respected (Seomely stays under 1,500) so it never exhausts the quota your other tools share.

## Business Relevance

- **SEO operators** get regression detection with root causes instead of raw console data
- **Content teams** get orphan and unindexed lists with per-URL causes and submission guidance
- **Agencies** get a 250K-call plan and multi-property coverage from one key
- **Anyone who has been burned by indexing tools** gets the `submission_helps` honesty flag instead of resubmit theater

## Integration with CorpusIQ

Seomely slots into CorpusIQ's SEO/visibility stack as the index-health layer. A composed workflow: the CorpusIQ Search Console connector reports clicks, impressions, and positions, while Seomely explains the underlying index state — run `investigate_indexing` on the same property, join the regressions against Search Console query data, and you get both the traffic symptoms and the index cause in one pass. For the CorpusIQ docs site itself, Seomely's IndexNow autopilot pairs with the sitemap and llms.txt publishing already in the docs pipeline, and the Semrush and Ahrefs connectors can validate that pages Seomely marks recovered actually start ranking.

## Limitations

- Brand new listing — no long track record yet
- Google-only index monitoring — no Bing coverage (pair with the Bing Webmaster connector for parity)
- Commercial cloud service; no self-host option
- Monthly call ceilings apply across REST and MCP together
- Fresh-data speed is governed by Google's inspection allowance, which no API call can hurry

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
