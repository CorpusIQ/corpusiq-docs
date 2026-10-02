---
title: Litescrape MCP - Keyless Google, Bing and Maps Search
description: "Litescrape's official MCP server wraps the Litescrape API in eight search tools: Google, Bing, DuckDuckGo and Google Maps run with no API key from a free daily allowance, while AI Mode, AI Overview and Shopping need a key that also removes the limits. stdio via npx."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-09-15
source: "chatmcp/mcpso issues #4152/#4153 + vendor site litescrape.com"
relevance: ★★
tags: [search, serp, google, bing, duckduckgo, google-maps, keyless, stdio]
---

# Litescrape MCP

**Search results as JSON, keyless to start.** The official Litescrape MCP server gives agents eight search tools over the Litescrape API: Google Search, Bing, DuckDuckGo and Google Maps work with no API key and no account, served from a free daily allowance per network; Google AI Mode, AI Overview and Google Shopping need an API key, which also removes the limits. Every tool returns the API's JSON unchanged after a one-line summary, with `result_groups` to keep only the groups the model needs, and links come back as real destinations rather than redirects.

```
Server type: Local (stdio via npx)
Auth: none for the keyless tools (free daily allowance); optional LITESCRAPE_API_KEY for key-only tools and unlimited calls
Package: litescrape-mcp-server (npm)
Endpoint: npx -y litescrape-mcp-server
Tools: 8
Pricing: free daily allowance per network; API credits top-up from $10
Category: Data & Analytics / Search
Built by: Litescrape (litescrape.com; repo github.com/litescrape/litescrape-mcp-server)
```

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search` | Unified search entry across the API's engines |
| `google_search` | Google organic results as JSON |
| `bing_search` | Bing organic results and rich SERP modules |
| `duckduckgo_search` | DuckDuckGo results |
| `google_maps` | Places, reviews and local results |
| `google_ai_mode` | Google AI Mode results (key required) |
| `google_ai_overview` | AI Overview data (key required) |
| `google_shopping` | Shopping products and offers (key required) |

Free daily allowance per network with no key: 25 Google Search calls, 50 each for Bing, DuckDuckGo and Google Maps. An API key unlocks the three AI tools and removes the limits.

## Installation

```bash
npx -y litescrape-mcp-server
```

## Configuration

```json
{
  "mcpServers": {
    "litescrape": {
      "command": "npx",
      "args": ["-y", "litescrape-mcp-server"],
      "env": { "LITESCRAPE_API_KEY": "ls_live_..." }
    }
  }
}
```

The key is optional: omit the `env` block to run the keyless tools from the free allowance.

## Business Relevance

- **SEO and content operators** pull SERP and AI-surface snapshots (AI Mode, AI Overview) into research and monitoring workflows.
- **Local businesses and marketers** query Google Maps results with ratings, reviews and contact details in structured JSON.
- **Analysts** collect search data for competitive and keyword research without managing scraping infrastructure.
- **Developers** get a clean npm package plus a plain HTTP API (`api.litescrape.com`) for the same endpoints.

## Integration with CorpusIQ

CorpusIQ holds the business data (GA4, Search Console-adjacent analytics, Shopify, Stripe); Litescrape supplies the outside view of the search landscape. A composed pattern: track your AI-surface presence with search data via Litescrape while CorpusIQ reports what the business actually did, then connect the two in one analysis session. For content operations, Litescrape feeds the research step and CorpusIQ verifies the business impact.

## Limitations

- stdio only: needs Node available on the machine running the agent.
- Free allowances are per network per day; the three AI tools require a key.
- Results come from the search engines' own pages; treat output as search data and review each engine's terms for production use.
- The npm package is young (0.1.1 at publication).
- Brand new to this catalog.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
