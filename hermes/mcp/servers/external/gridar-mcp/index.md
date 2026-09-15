---
title: "Gridar MCP - Quebec SEO Toolkit and AI Visibility for Agents"
description: "Hosted SEO toolkit MCP focused on Quebec and google.ca: technical audits, keyword tracking, Search Console data, AI-search visibility and topic clusters across 69 tools over OAuth 2.1, endpoint mcp.gridar.app/mcp 401-verified live Sep 1, 2026."
category: SEO
stars: "0 (new listing, TokDar2410621/blog-dashboard)"
added: 2026-09-01
source: "chatmcp/mcpso issue #3868 (Sep 1, 2026)"
relevance: ★★★
tags: [mcp-server, seo, geo, ai-visibility, keyword-tracking, google-search-console, quebec, french-canadian]
---

# Gridar MCP

**Hosted Streamable HTTP MCP server that gives an agent real SEO data for a website, tuned to the Quebec and French-Canadian market.** One endpoint covers technical audits, google.ca rank tracking and Search Console queries, keyword research, competitor analysis, AI-answer visibility and topic-cluster architecture, plus IndexNow submission, across 69 tools authenticated over OAuth 2.1.

```
Server type: Hosted, remote (Streamable HTTP)
Endpoint: https://mcp.gridar.app/mcp
Auth: OAuth 2.1 (RFC 8414 discovery + RFC 7591 dynamic client registration; bearer token option for headless agents)
Registry: app.gridar/gridar v0.7.0 (official registry, active)
Repo: github.com/TokDar2410621/blog-dashboard, subfolder mcp-server (license not declared)
Website: gridar.app
Tools: 69 (technical audits, rank tracking, GSC, keyword research, AI visibility, clusters, IndexNow)
```

## Why This Matters for Operators

Quebec operators compete in a market where google.ca rankings, French-language content and AI-answer citations each behave differently from the US SERPs most SEO tools assume.

First, **geo-tuned rank tracking.** track_keyword and gsc_queries read real google.ca positions and Search Console data, so an agent can answer "which of our French landing pages lost positions in Quebec this month" with actual market data instead of generic advice.

Second, **AI visibility is measured, not guessed.** run_ai_visibility and ai_overview_readiness test whether the brand actually shows up in ChatGPT, Perplexity and Google AI Overview answers, which matters most for French-Canadian queries where AI assistants are the fastest-growing discovery surface.

Third, **the whole loop is agent-native.** From audits (site_seo_score, page_speed, find_broken_links) through keyword work (keyword_research, classify_intent, people_also_ask) to topic architecture (build_cluster, detect_cannibalization) and indexing (IndexNow, submit_sitemap), the toolkit covers the full SEO workflow a Canadian operator would otherwise pay two or three subscriptions to assemble.

## Tools and Capabilities

The submission documents 69 tools. Anonymous enumeration is refused by design (OAuth 2.1 gate), so this table is capability-level from the submission plus the official registry record, which confirms the server, version and endpoint.

| Area | Representative tools | What they do |
|------|---------------------|--------------|
| Technical audits | `site_seo_score`, `bulk_audit`, `page_speed`, `check_renderability`, `find_broken_links` | Scorecard and crawl-level technical checks with fix recipes |
| Rank tracking | `track_keyword`, `snapshot_keywords`, `list_keywords`, `gsc_queries` | google.ca positions and Search Console query data |
| Keyword research | `keyword_research`, `suggest_keywords`, `serp_analyze`, `people_also_ask`, `classify_intent` | Query expansion, SERP analysis and intent classification |
| Competitive analysis | `analyze_competitors`, `suggest_competitors` | Competitor discovery and gap analysis |
| AI visibility | `run_ai_visibility`, `ai_visibility_summary`, `ai_overview_readiness` | Whether the brand appears in AI answers, and how ready it is |
| Topic architecture | `build_cluster`, `cluster_map`, `suggest_internal_links`, `detect_cannibalization` | Content-cluster planning and internal linking |
| Indexing | `indexnow_setup`, `indexnow_submit`, `submit_sitemap`, `index_coverage` | Fast indexing via IndexNow and sitemap submission |

## Installation

Point any MCP client at the hosted endpoint. The first connection runs the OAuth 2.1 flow (discovery document published per RFC 8414):

```json
{
  "mcpServers": {
    "gridar": {
      "url": "https://mcp.gridar.app/mcp"
    }
  }
}
```

Headless setups (CI jobs, background agents) can skip the browser flow by passing a bearer token instead. Setup pages per client exist for ChatGPT, Claude and agent flows on gridar.app.

## Configuration

OAuth 2.1 with discovery and dynamic client registration. The submission states headless agents can pass a bearer token; obtain it from the Gridar dashboard after sign-in. No anonymous tier is advertised.

## Business Relevance

- **Quebec and French-Canadian site owners** get SERP and Search Console data from the market they actually compete in, not US-proxy estimates.
- **Marketing agencies with Canadian clients** run audits, keyword tracking and AI-visibility reports per client from one endpoint.
- **E-commerce operators targeting google.ca** watch position changes and cannibalization without manual rank checks.
- **Any operator asking "are we cited in AI answers"** gets a measurable answer instead of an opinion.

## Integration with CorpusIQ

Gridar composes with CorpusIQ as the acquisition-side half of a marketing measurement loop. CorpusIQ answers from the systems you run (Shopify orders, Google Ads spend, HubSpot pipeline) while Gridar answers from the search market: positions, impressions, clicks and AI citations in the Canadian market an operator is buying into. An operator can ask "did the French landing pages that rank improved convert into more Shopify orders this month" and get both sides, market and revenue, in one conversation. Pairs naturally with CiteRank for general AI-search visibility and with the ni-c Search Console MCP when working outside the Quebec market.

## Limitations

- Quebec and google.ca focus first; general-market SERPs are covered but the toolkit is optimized for the French-Canadian market.
- Brand new listing: repo shows zero stars and no declared license; treat as an early-stage vendor.
- OAuth 2.1 gate means anonymous tool enumeration is refused; exact per-tool schemas require a signed-in client.
- 69 tools is the submission count; the live surface may differ slightly after registry updates.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [CiteRank MCP - AI Search Visibility & GEO Audits for AI Agents](/docs/hermes/mcp/servers/external/citerank-mcp)
- [Google Search Console MCP (ni-c) - Property Setup and Search Analytics](/docs/hermes/mcp/servers/external/google-search-console-ni-c-mcp)
