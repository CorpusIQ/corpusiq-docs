---
title: SEOmatic MCP - Real Search Console Data with Approval-Gated
description: "Hosted SEO agent MCP from SEOmatic: 13 consolidated tools for Google Search Console performance and indexing, keyword research and clusters, backlink profiles, SERP competitors, traffic analytics, local presence, AI visibility and staged fix tasks with human approval gates. OAuth 2.1 or API key, free tier."
category: SEO
stars: "0 (new listing, Minh42/seomatic-mcp)"
added: 2026-09-02
source: "mcpservers.org /all JSON-LD (Sep 2, 2026 morning sweep)"
relevance: ★★★
tags: [mcp-server, seo, google-search-console, keywords, backlinks, ai-visibility, rank-tracking]
---

# SEOmatic MCP

**SEO agent for your own site, built so the agent reads real data and stages fixes that always wait for your approval.** SEOmatic connects Claude, Cursor, Cline or Claude Code to your actual Search Console, keyword, backlink and AI-visibility data. Read tools answer questions like "which keywords am I close to ranking for" and "what backlinks did we gain this month"; acting tools stage fix tasks, content campaigns and article drafts that a human approves in SEOmatic before anything changes, with before-and-after results shown on every change.

```
Server type: Hosted (app.seomatic.ai/api/mcp)
Endpoint: https://app.seomatic.ai/api/mcp (Streamable HTTP)
Auth: OAuth 2.1 (interactive clients) or API key sent in the Authorization header (headless); keys minted in workspace settings
Repo: github.com/Minh42/seomatic-mcp (MIT, created Sep 2026; docs-only connector repo)
Website: seomatic.ai
Tools: 13 consolidated, annotated read-only vs staging, scoped to the connected site
```

## Why This Matters for Operators

SEO tools split into reporters that describe problems and fixers that act blind. SEOmatic is the connector that closes the loop with a human gate in the middle.

First, **the data is the account data, not a scrape.** Search Console performance and indexing come from the connected property, so "which pages are losing traffic" is answered from your own numbers, and no domain parameter is ever passed - tools are scoped to the connected site.

Second, **fixes are staged, not applied.** Acting tools queue SEO fix tasks, content campaigns and article drafts that a human approves in SEOmatic. The approval gate converts "agent rewrote my title tags overnight" into a review workflow with before-and-after results.

Third, **AI visibility is first-class.** The strategy insight surface answers "does ChatGPT mention our site when people ask about our topic" - the AEO question legacy SEO stacks do not even ask, let alone answer from data.

## Tools and Capabilities

13 consolidated tools from the vendor README (verified against the repo). Endpoint 401-verified live on anonymous probe (API-key gate, expected).

| Area | Tools | What they do |
|------|-------|--------------|
| Search Console | `gsc_performance`, `gsc_indexing` | Real performance and indexing data from the connected property |
| Keywords | `keyword_research`, `keyword_clusters` | Keyword opportunities and cluster grouping for content planning |
| Backlinks | `backlink_profile`, `serp_competitors` | Link profile gains and who links to competitors but not you |
| Traffic | `traffic_analytics` | Traffic trends and decay diagnosis |
| Visibility | `local_presence`, `strategy_insights` | Local search visibility and AI-visibility signals |
| Inventory | `site_pages`, `dataset_library` | Site page inventory and saved datasets |
| Staging | `task_manage`, `campaign_manage` | Staged fix tasks, content campaigns and article drafts - approval-gated |

The roster shown to a session depends on plan and connected data sources.

## Installation

Create an account at app.seomatic.ai (free tier works) and mint an API key in Settings, API Keys, then add the connector:

```json
{
  "mcpServers": {
    "seomatic": {
      "url": "https://app.seomatic.ai/api/mcp",
      "type": "streamableHttp"
    }
  }
}
```

Headless clients send the `smk_live_...` key in the Authorization header. Claude and Claude Code connect with the URL alone (OAuth, no key needed). The repo also ships a companion Agent Skill (`skills/seomatic-seo-audit`) that turns the connector into a guided senior-SEO-grade audit: baseline, CTR mismatches, striking-distance keywords, decay diagnosis, indexation, backlinks, AI visibility, with a verdict-first report ranked by business impact.

## Configuration

Free tier includes the insight tools with a monthly question quota shared with SEOmatic chat. Acting tools (staging tasks, campaigns, articles) need a paid plan and always keep the human-approval gate. Every tool is annotated read-only vs staging, so assistants know which calls need a confirmation prompt.

## Business Relevance

- **SEO operators** get real Search Console, keyword and backlink data in the editor with staged, reviewable fixes.
- **Content teams** get keyword clusters and striking-distance queries without leaving the chat.
- **Anyone answering "why are we invisible to ChatGPT"** gets AI-visibility strategy signals alongside classic SEO data.

## Integration with CorpusIQ

SEOmatic composes with CorpusIQ as the acquisition-to-revenue loop. CorpusIQ answers from the conversion side (Stripe, HubSpot, Google Ads) while SEOmatic reads the organic surface (Search Console, backlinks, AI visibility) and stages fixes with approval gates. An operator can ask "stage a fix plan for our decaying pages, then tell me which of those pages actually drive revenue" and get the staged task list and the revenue answer in one workflow. Pairs with Ranki for audit-and-fix recipes and CiteRank for AI-search visibility benchmarking.

## Limitations

- Brand-new repo (created Sep 1, 2026), zero stars; the repo is a docs-only connector - the hosted server is the product.
- Acting tools are paid-plan only; free tier carries a monthly question quota.
- Tools are scoped to the connected workspace site; no multi-site reads from one connector.
- Anonymous tool enumeration is refused (API-key or OAuth required), so the table above is from the vendor README, not a live probe.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [Ranki MCP - SEO and AEO Audits](/hermes/mcp/servers/external/ranki-mcp)
- [CiteRank MCP - AI Search Visibility & GEO Audits for AI Agents](/hermes/mcp/servers/external/citerank-mcp)
- [Seomely MCP](/hermes/mcp/servers/external/seomely-mcp)
