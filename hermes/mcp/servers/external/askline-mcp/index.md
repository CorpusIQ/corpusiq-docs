---
title: "Askline MCP - AI Search Visibility and Brand Monitoring"
description: "Hosted MCP server that shows what ChatGPT says about a brand and the SEO that feeds it: 22 tools for keyword research, SERP and competitor analysis, backlinks, AI citations, AI share of voice, and Search Console data, with per-user URL token auth at 35 dollars a month."
category: SEO
stars: n/a (hosted product)
added: 2026-08-28
source: "mcp.so GitHub issue #3807"
relevance: ★★★
tags: [mcp-server, seo, geo, aeo, chatgpt, brand-monitoring, remote-mcp]
---

# Askline MCP

**Hosted MCP server that answers the GEO question operators actually have: what does ChatGPT say about my brand, and what SEO is feeding that answer.** 22 tools span keyword research, live SERP snapshots, competitor keyword gaps, backlink profiles, and a dedicated AI-visibility family (chatgpt_answer, ai_search_volume, llm_citations, ai_mentions, ai_share_of_voice) that measures how often Google AI Overviews and ChatGPT name a brand or its competitors. The catalog surface is open (initialize and tools/list answer anonymously, verified live); data calls require a per-user URL token.

```
Server type: Remote (Streamable HTTP), hosted
Auth: Per-user URL token (issued at askline.ai/account after signup)
Endpoint: https://askline.ai/mcp
Tools: 22 (verified anonymously at the catalog surface)
Pricing: $35/mo (data calls cost credits; Search Console tools are free)
Category: SEO / AI search visibility (GEO/AEO)
Built by: Askline (askline.ai)
```

## Why This Matters for Operators

AI search is now a traffic channel, and most operators cannot see it. Askline closes that gap in one endpoint: the assistant asks chatgpt_answer what ChatGPT currently recommends for a category, reads llm_citations to see which pages ChatGPT quotes, then pulls ranked_keywords and competitor_keywords to understand why those pages win. The loop between the AI answer and the classic SEO that produces it is the whole point of the product.

Two details separate it from a generic SEO API. First, ai_search_volume and ai_mentions quantify demand in AI-assistant search specifically, a metric absent from classic keyword tools. Second, the zero-credit Search Console tools (gsc_performance, gsc_queries, gsc_pages) and the research_memory and pin_finding tools make the MCP session a compounding research workspace rather than a stateless query pipe.

**One conversation can audit what AI assistants say about a brand, attribute it to pages, and track it over time.**

## Tools & Capabilities

| Area | Capability |
|---|---|
| Keyword research | keyword_research (related keywords with volume and difficulty), keyword_difficulty (top-10 ranking score) |
| SERP | serp_overview (live Google organic results with SERP features), domain_overview (traffic, ranking keywords, domain rank) |
| Competitors | ranked_keywords, competitor_keywords (keywords competitors rank for that you do not, plus overlap), link_gap |
| Backlinks | backlink_overview (count, referring domains, spam score), referring_domains |
| On-page | site_audit (instant on-page audit, reports what changed since the last run) |
| AI visibility | chatgpt_answer (live ChatGPT or Gemini answer with recommended brands and cited URLs), ai_search_volume, llm_citations, ai_mentions, ai_share_of_voice |
| Search Console | gsc_performance, gsc_queries, gsc_pages (zero credits) |
| Workspace | research_memory, pin_finding, get_project, set_project (primary domain and market) |

## Installation

```bash
claude mcp add askline --transport http https://askline.ai/mcp/<your-token>
```

Sign up at askline.ai, then copy the per-user MCP URL with your embedded token from the account page (askline.ai/account).

## Configuration

```json
{
  "mcpServers": {
    "askline": {
      "type": "http",
      "url": "https://askline.ai/mcp/<your-token>"
    }
  }
}
```

The token lives in the URL path rather than a header. Call set_project once per brand to fix the primary domain and market (country plus language), after which keyword, SERP, and competitor tools default to the saved project.

## Business Relevance

- **Marketing operators** audit AI-search visibility per brand and track AI share of voice against named competitors.
- **SEO teams** join classic SERP and keyword data with AI citations to explain why ChatGPT recommends specific pages.
- **Agencies** run client visibility checks from one chat thread using the zero-credit Search Console tools for reporting.
- **Founders** see what ChatGPT currently says about their category before product or content decisions.
- **Content operators** find cited pages and keyword gaps, then re-audit after publishing to confirm movement.

## Integration with CorpusIQ

Askline measures search and AI visibility; CorpusIQ carries the business results behind them. A composed workflow: the assistant pulls Shopify revenue and GA4 traffic by landing page via CorpusIQ connectors, correlates them with Askline's ranked_keywords and ai_mentions to find which visible topics actually convert, then re-runs site_audit after content changes. CorpusIQ's read-only business data closes the loop Askline's search telemetry opens.

## Limitations

- Data calls require the per-user token and cost credits; the anonymous catalog surface only exposes tool metadata.
- ChatGPT mention data is US/English-focused per the vendor's tool notes.
- Young listing: submitted to mcp.so on Aug 28, 2026; hosted product without a public repo.
- Live Google SERP data depends on the vendor's scraping infrastructure, subject to change.
- Single-project workspace per token: one primary domain and market at a time.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CiteRank MCP - AI Search Visibility Audits](/docs/hermes/mcp/servers/external/citerank-mcp)
- [Foliora MCP - Managed AI Search Preview for Agents](/docs/hermes/mcp/servers/external/foliora-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
