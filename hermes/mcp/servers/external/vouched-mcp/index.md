---
title: "Vouched MCP - SEO Data with Provenance for Agents"
description: "Open-source MCP server for Search Console, GA4, keywords, backlinks, live SERPs and AI answer visibility, every fact carrying its source and confidence."
category: SEO
stars: 0 (MIT, muditjuneja/vouched)
added: 2026-09-30
source: "mcpservers.org server page (muditjuneja/vouched)"
relevance: ★★★
tags: [seo, search-console, ga4, keywords, backlinks, ai-visibility, open-source, remote-mcp]
---

# Vouched MCP

**SEO data your AI can cite.** Vouched is an open-source MCP server for Search Console, GA4, keywords, backlinks, live Google results and AI answer visibility. Every tool returns the same JSON envelope where each fact states where it came from, how confident it is and when it was observed, so an agent can tell a Search Console number from an index estimate. Hosted at vouchedhq.com or self-hosted on Cloudflare Workers with your own DataForSEO key.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (hosted) or bearer token (self-hosted)
Endpoint: https://vouchedhq.com/mcp
Tools: 19, all read-only
Pricing: free for your own Google data; Pro or Team plan for market data
Category: SEO
Built by: muditjuneja, open source (MIT)
```

## Why This Matters for Operators

SEO questions today get answered with guesses or with numbers pulled from five different dashboards. Vouched puts the question and the data in one place. Ask why clicks dropped last month, which keywords a competitor ranks for that you do not, or where a domain shows up in AI answers, and the agent answers from real data with provenance on every fact.

The envelope matters as much as the data. Each result carries a source class, a confidence value, an observation timestamp and a delta against the previous period. An operator can audit an agent's answer line by line instead of trusting a summary, and the server is read-only by construction: nothing is ever written to Google or to any site.

## Tools & Capabilities

| Tool | What it answers |
|---|---|
| get_search_performance | Clicks, impressions, CTR and position by query, page, date, country or device, with period-over-period deltas |
| inspect_indexing | Whether a URL is indexed, which canonical Google picked, last crawl |
| list_sitemaps | Submitted sitemaps with errors, warnings and URL counts |
| get_website_analytics | Sessions, users and engagement from GA4 |
| inspect_domain | A domain's organic traffic, ranking keywords and main competitors |
| discover_competitors | Who competes with a site for the same keywords |
| research_keywords | Keyword ideas with volume, difficulty, CPC and intent |
| inspect_serp | Who ranks on Google right now, plus AI Overviews and other features |
| inspect_backlinks | Authority, referring domains, anchors and individual backlinks |
| compare_backlink_gap | Sites linking to competitors but not to you |
| discover_ai_citations | Which sites AI answers cite for a topic |
| inspect_ai_visibility | How often a domain appears in AI answers versus competitors |
| describe_capabilities | What is enabled on this server and what each tool costs |

Plus inspect_keyword, inspect_search_visibility, inspect_page, compare_keyword_coverage, list_websites and export_dataset, the full result behind a truncated response kept for 7 days.

## Installation

```bash
claude mcp add --transport http vouched https://vouchedhq.com/mcp
```

Claude Code also ships a plugin with an SEO analysis skill via the plugin marketplace. Gemini CLI installs from the repo. The client opens a sign-in page on first connect (standard MCP OAuth); clients that can only send a header use an API key from the dashboard instead.

## Configuration

```json
{
  "mcpServers": {
    "vouched": {
      "url": "https://vouchedhq.com/mcp"
    }
  }
}
```

Self-hosted deployments point the client at your Worker's /mcp URL with your bearer token. Both run the same code and expose the same tools.

## Business Relevance

- **Founders and operators** answer why-traffic-moved questions from GSC and GA4 in one conversation
- **SEO and content teams** run competitor keyword and backlink gap analysis without switching dashboards
- **AEO and GEO teams** track which sites AI answers cite and how often their domain appears
- **Agencies** self-host to avoid per-seat SaaS markup and keep client data in their own Cloudflare account

## Integration with CorpusIQ

Vouched adds the public-search picture to CorpusIQ's private business picture. A composed workflow: CorpusIQ answers revenue and churn questions from Stripe, QuickBooks and GA4 connectors, while Vouched answers why organic traffic changed, which keywords the competitors own and where the brand appears in AI answers. The operator correlates organic visibility with revenue in one session, and Vouched's provenance envelope matches CorpusIQ's evidence-first answering style.

## Limitations

- Brand new listing with no track record yet (0 GitHub stars at catalog time)
- Market data needs a DataForSEO key (self-host) or a paid plan (hosted)
- Google data is read-only and covered by Google's Limited Use requirements
- SEO class is well served in this catalog, but the AI-answer visibility tools are the differentiator

## FAQ

### What makes Vouched different from other SEO MCP servers?

Provenance. Every fact carries its source, confidence and observation time, and the AI citation and AI visibility tools cover the AEO side that keyword-only servers miss.

### Is my Google data safe?

Google data is read only when asked for, never sold, never used for ads and never used to train models. Self-hosting keeps everything in your own Cloudflare account.

### Is there a free tier?

Your own Google data is free on the hosted service. Live market data needs a Pro or Team plan, or a self-hosted setup with your own DataForSEO key.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [HarborRank MCP - Live SEO Data for AI Agents](/hermes/mcp/servers/external/harborrank-mcp/)
- [seodraft MCP - Drafted SEO Content with Rule Checks](/hermes/mcp/servers/external/seodraft-mcp/)
- [AgentGrown MCP - Google Search Console and GA4 for Coding Agents](/hermes/mcp/servers/external/agentgrown-mcp/)
