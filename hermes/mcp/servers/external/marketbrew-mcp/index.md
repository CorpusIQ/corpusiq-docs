---
title: "Market Brew MCP - Search Engine Modeling for Agents"
description: "Read-only hosted MCP server over Market Brew: ranking-model analysis, content alignment, knowledge bases, crawl data and AI-visibility history, over OAuth on an enabled account."
category: SEO
stars: n/a (new listing)
added: 2026-10-08
source: "mcpservers.org /all (October 8, 2026 night sweep)"
relevance: ★★★
tags: [seo, search-engine-modeling, ai-visibility, content, crawl, analytics]
---

# Market Brew MCP

**Read-only MCP access to Market Brew's search engine modeling and AI-visibility data** - ranking models, content alignment, knowledge bases, crawl data and AI visibility history, worked from chat instead of a dashboard. An established platform (US Patents 8,447,751 and 9,245,037) behind one Streamable HTTP endpoint.

```
Server type: Remote (Streamable HTTP at https://brew.marketbrew.ai/mcp)
Auth: OAuth on an enabled Market Brew account
Docs: https://brew.marketbrew.ai/customer-manual.htm#api-and-chatgpt-read-access
Tools: read-only data surface (live handshake reports server market-brew-readonly v1.0.0)
Pricing: requires an enabled Market Brew account (vendor pricing)
Category: SEO
Built by: Market Brew
```

## Why This Matters for Operators

Most SEO tooling reports on keywords. Market Brew models search engines themselves: it calibrates ranking models against your site's structure and templates, then shows where the structure - not the copy - is holding pages back. The platform's operating model is See, Hear, Speak: Ranking Sensors, Flight Plans and Top Tasks for structural issues; Ask, Listen, Keyword Fueler, Bridge and EyesOver for demand signals; the AI Content Dashboard and Content Booster for content action. The MCP server opens that analysis to an agent, so "why does this template underperform, and what would we change first" becomes a conversation over your own modeled data.

## Tools & Capabilities

- **Ranking models and structural calibration:** read modeled ranking environments, ranking factors, calibration results and Flight Plan groupings.
- **Content alignment:** inspect how pages align with the demand and intent the model captures (AI Content Dashboard and Content Booster surfaces).
- **Knowledge bases:** query the entity and knowledge-base layer Market Brew builds from your site.
- **Crawl data:** site map, templates, internal links and crawl behavior as the model sees them.
- **AI visibility history:** review how the site has appeared across AI answer surfaces over time.

## Installation

```bash
npx add-mcp 'https://brew.marketbrew.ai/mcp'
```

```json
{
  "mcpServers": {
    "market-brew": {
      "url": "https://brew.marketbrew.ai/mcp"
    }
  }
}
```

## Configuration

Access runs read-only against an enabled Market Brew account over OAuth. Live probe: POST initialize returns 200 with a live handshake (server `market-brew-readonly` v1.0.0) whose instructions describe asking for Market Brew data in ordinary language.

## Example Prompts

- "Which templates in our Flight Plan show repeated structural issues, and what do the Top Tasks recommend first?"
- "Summarize the ranking factors contributing to the product-page slide we saw this month."
- "What demand signals are sitting in Launchpad that we have not converted into content?"
- "How has our AI visibility changed over the last quarter, and which pages carry it?"

## Integration with CorpusIQ

CorpusIQ reads your first-party performance (Search Console, GA4, Shopify) read-only and cited. Market Brew adds the modeled layer above it - pairing what actually happened in your analytics with the structural model of why, in the same conversation.

## Limitations

- Read-only by design; it analyzes, it does not edit pages.
- Requires an existing enabled Market Brew account; this is an access layer for the platform, not a standalone tool.
- Modeling is statistical guidance - the vendor's own manual says not to treat a single sensor as truth; corroborate across a Flight Plan.
- Interface details live in Market Brew's customer manual.

## FAQ

### Is this an official Market Brew server?

Yes - it is the vendor's hosted MCP endpoint at brew.marketbrew.ai, documented in the Market Brew customer manual.

### What can an agent actually ask it?

Questions over the modeled data: ranking models, content alignment, knowledge bases, crawl data and AI visibility history, phrased in ordinary language.

### Does it work without a Market Brew subscription?

No. The endpoint reads an enabled Market Brew account; the account is the source of the modeled data.

## See Also

- [MisarSEO MCP - SEO Research for AI Agents](/hermes/mcp/servers/external/misarseo-mcp/)
- [RankControl MCP - SEO Content Program for Agents](/hermes/mcp/servers/external/rankcontrol-mcp/)
- [IndexLinks MCP - Page Submission and Crawl Receipts](/hermes/mcp/servers/external/indexlinks-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
