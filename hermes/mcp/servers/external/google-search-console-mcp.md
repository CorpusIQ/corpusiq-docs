---
title: "Google Search Console MCP — Integration Guide"
description: "Hosted MCP server for Google Search Console analytics. Connect Claude, Cursor, or any MCP client to query clicks, impressions, rankings, indexing status, and sitemaps."
category: mcp
tags: [mcp-server, seo, google-search-console, marketing, analytics]
last_updated: 2026-07-14
---

# Google Search Console MCP Server

**Repository:** [AKzar1el/mcp-gsc](https://github.com/AKzar1el/mcp-gsc)
**By:** digestseo.com / AKzar1el
**Stars:** 2
**Category:** Marketing, SEO, Analytics
**Auth:** OAuth (Sign in with Google)
**Transport:** Streamable HTTP
**Hosting:** Hosted + self-hostable on Cloudflare Workers

## Overview

The Google Search Console MCP server gives AI agents direct access to GSC analytics. Instead of logging into the GSC dashboard, operators can ask their AI assistant about site performance — clicks, impressions, CTR, average position, indexing status, and sitemap health — all through natural language.

This is one of the first MCP servers targeting SEO professionals, bridging the gap between AI coding agents and search performance data. Built on Cloudflare Workers with OAuth authentication, it requires no API key management — users sign in with their Google account.

## What You Can Do

- Query search analytics: clicks, impressions, CTR, and average position by query, page, country, or device
- Inspect URLs for indexing status, crawl errors, and mobile usability
- List and manage sitemaps
- Get site-level performance summaries
- Filter by date range and dimension

## Installation

### Hosted (Recommended)

The server is hosted and available through the MCP marketplace. Add it to your MCP client:

```json
{
  "mcpServers": {
    "google-search-console": {
      "type": "url",
      "url": "https://mcp-gsc.digestseo.com/mcp"
    }
  }
}
```

### Self-Hosted (Cloudflare Workers)

```bash
git clone https://github.com/AKzar1el/mcp-gsc.git
cd mcp-gsc
npm install
npx wrangler deploy
```

Requires a Google Cloud OAuth 2.0 client ID configured for the Search Console API.

## Use Cases for Business Operators

1. **Daily SEO monitoring:** Ask your agent "How did our top pages perform this week?" instead of logging into GSC
2. **Content gap analysis:** Cross-reference GSC query data with content production workflows
3. **Indexing health checks:** Automate URL inspection after site changes or migrations
4. **Competitor keyword discovery:** Identify queries where you rank but don't yet have dedicated content
5. **Sitemap management:** Verify sitemap submission and coverage after content updates

## Integration with CorpusIQ

CorpusIQ can connect to this MCP server alongside its existing 36+ business data sources. Operators using CorpusIQ for Shopify/QuickBooks/GA4 analytics can add GSC data for a unified view of business + search performance.

## Limitations

- 2 GitHub stars — very new, community validation pending
- OAuth flow requires browser interaction for initial setup
- Self-hosted version requires Cloudflare Workers account
- Query filtering depends on GSC API limitations (16 months of data, sampling on large sites)

## Verdict

HIGH VALUE for any business operator doing SEO. The hosted + OAuth model eliminates API key friction. Serverless architecture (Cloudflare Workers) means zero maintenance for self-hosters. Watch for adoption growth — this fills a genuine gap in the MCP ecosystem.

---

*Discovered: July 14, 2026 via mcp.so. Guide by CorpusIQ MCP Discovery Engine.*
