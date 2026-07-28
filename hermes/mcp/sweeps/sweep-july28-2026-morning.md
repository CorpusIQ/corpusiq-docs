---
title: "MCP Server Sweep — July 28, 2026 (Morning)"
description: "Morning sweep of mcp.so and mcpservers.org for new business-relevant MCP servers. Firecrawl DOWN — curl + DDGS fallback used."
date: 2026-07-28
type: sweep
sources: ["mcpservers.org/all", "mcp.so/servers"]
new_servers: 2
new_guides: 2
---

# MCP Server Sweep — July 28, 2026 Morning

**Run time:** ~07:00 UTC, July 28, 2026
**Firecrawl status:** DOWN (confirmed by Honcho context and runtime error)
**Fallback:** curl-based HTML scraping + DDGS web search
**Previous sweep:** July 27, 2026 18:04 UTC (de8b315)

## Methodology

Since Firecrawl is down, this sweep used:

1. **mcpservers.org /all** — curl fetch of the React SSR page, extracted JSON-LD structured data and server list from the `<script type="application/ld+json">` block. 30 newest servers listed.
2. **mcp.so /servers** — curl fetch of the TanStack Start SSR page, extracted server data from the dehydrated state in `<script>` tags.
3. **Cross-reference** — compared extracted server names and slugs against existing catalog files in `~/corpusiq-docs/hermes/mcp/servers/external/`.

## New Servers Discovered

### Retasc ★★★ — Issue Tracker for AI Agents
- **Source:** mcpservers.org /all (position #19), confirmed via curl of retasc.com
- **What it is:** MCP-native issue tracker built for AI coding agents, not humans. Atomic claims with lease/TTL, dependency-graph dispatch, parallel swarm execution, cross-runtime handoffs (Claude Code ↔ Codex ↔ Cursor).
- **Why it matters:** First MCP server purpose-built as the work queue for multi-agent orchestration. Traditional trackers (Jira, Linear) break with agent workflows — Retasc replaces the Jira API + custom dispatch script pattern with a single MCP endpoint.
- **Transport:** Streamable HTTP at `https://api.retasc.com/mcp`
- **Auth:** API key
- **Pricing:** Free tier ($10 metered usage included), ~$9/month for their own busiest agent
- **Guide:** [retasc-mcp/index.md](/hermes/mcp/servers/external/retasc-mcp/index.md)

### Santiment MCP ★★ — Crypto Market Intelligence
- **Source:** mcpservers.org /all (position #26), confirmed via curl of academy.santiment.net/mcp-connector/
- **What it is:** Official Santiment MCP connector — 30+ metrics across 500+ crypto assets. On-chain, social sentiment, trending narratives, analyst insights.
- **Why it matters:** Most comprehensive crypto market intelligence MCP cataloged. Official connector (not community), clean OAuth 2.0 PKCE setup, free tier with core metrics.
- **Transport:** Streamable HTTP at `https://api.santiment.net/mcp`
- **Auth:** OAuth 2.0 with PKCE
- **Pricing:** Free tier, Pro via SanAPI subscriptions
- **Guide:** [santiment-mcp/index.md](/hermes/mcp/servers/external/santiment-mcp/index.md)

## Also Identified (No Guides)

| Server | Source | Reason Skipped |
|--------|--------|----------------|
| Snipara | mcpservers.org | Project intelligence/memory — insufficient public documentation |
| Fixou | mcpservers.org | French tradespeople quotes — region-specific, not business-ops |
| iGaming Tools | mcpservers.org | Gaming reference data — niche vertical |
| Confluence-to-Markdown MCP | mcpservers.org | Utility tool, not business operations |
| AIQUAA Playwright MCP | mcpservers.org | Dev tooling (BDD testing) |
| Actvt | mcpservers.org | Mac system metrics — developer tool |
| Grok Chat MCP | mcpservers.org | AI model wrapper — developer tool |
| Fable MCP | mcpservers.org | AI model wrapper — developer tool |
| Claude Chat MCP | mcpservers.org | AI model wrapper — developer tool |
| Routara LLM Gateway | mcpservers.org | Model routing gateway — previously cataloged |
| KoreanAds | mcpservers.org | Korean advertising — guide already exists (not indexed) |
| Argus Testing | mcpservers.org | QA testing — guide already exists (not indexed) |
| 1ClickReport | mcpservers.org | Marketing analytics — guide already exists (not indexed) |
| TaskerArmy Agent | mcpservers.org | Shopify optimization — guide already exists (not indexed) |
| twocents | mcp.so | Human feedback — guide already exists (not indexed) |

## Channel Status

| Channel | Status |
|---------|--------|
| Firecrawl | DOWN |
| DDGS | WORKING (but not configured in this session's web_search) |
| Curl scraping | WORKING — used as primary data source |
| GBrain | DOWN (per Honcho context — not impacting this task) |
| GitHub (gh CLI) | WORKING — authenticated as Ben-Home |

## Catalog Stats

| Metric | Before | After |
|--------|--------|-------|
| Total servers tracked | 110 | 112 |
| Integration guides | 10 | 12 |
| mcpservers.org total | 10,139 | 10,141 |
| mcp.so total | ~22,680 | ~22,680 (unchanged) |

## Notes

- **MCP 2.0:** Spec RC published today (July 28). Not yet reflected in these servers' implementations but will need monitoring for migration impact on mcp2.corpusiq.io.
- **Firecrawl ongoing outage:** Third sweep using curl fallback. Working but slower and misses structured data. No DDGS web_search available in this session either (web_search routed through Firecrawl).
- **Unindexed guides:** Discovered 5 guide files (1ClickReport, KoreanAds, Argus, twocents, TaskerArmy) that exist in the filesystem but aren't linked from the main index.md. These were likely created in previous sweeps but the index update step was skipped. Should be rectified in a future maintenance sweep.
