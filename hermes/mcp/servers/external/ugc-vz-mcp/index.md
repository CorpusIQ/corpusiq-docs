---
title: UGC VZ MCP - DACH UGC Creator Discovery for Agents
description: Free directory of real UGC creators in Germany, Austria and Switzerland for AI agents - search profiles, compare pricing and reach, and trigger gated brand outreach requests.
category: Content
stars: 2 (new listing)
added: 2026-08-26
source: "mcp.so GitHub issue #3759"
relevance: ★★
tags: [ugc, creators, influencer-marketing, dach, germany, content, marketing, remote-mcp]
---

# UGC VZ MCP

**Remote MCP server (Streamable HTTP, no key)** - UGC VZ is a free directory of real UGC creators in the DACH region (Germany, Austria, Switzerland): people with portfolios and social proof, not AI avatars. Agents search profiles, compare pricing and reach, and trigger a brand outreach request. Search results never contain private contact data - a brand receives creator contact details by email only after an explicit `request_outreach` call. 5 tools, no API key, no account. Published in the official MCP registry as `de.ugc-vz/creator-search`; endpoint verified live (stateless initialize answered, server version 1.0.2).

```
Server type: Remote (Streamable HTTP)
Auth: None - no key, no account; rate-limited per caller
Endpoint: https://ugc-vz.de/api/mcp
Tools: 5 (search, profiles, outreach, status, vocabulary)
Pricing: Free for both sides, no commission
Category: Content
Built by: UGC VZ (repo github.com/ugcvz/ugc-vz-mcp, MIT)
```

## Why This Matters for Operators

Sourcing UGC creators usually means platform marketplaces with commission fees, or spreadsheets of cold pitches to accounts that turn out to be AI-generated or bought-follower shells. The discovery step alone eats a day per campaign.

**UGC VZ makes creator discovery an agent task with a built-in privacy gate.** Search works in German or English with filters for city, topic and human-verification level; profiles carry portfolios and social proof so you can compare pricing and reach before committing. Contact data flows only after an explicit outreach request, which keeps the directory free of scraped-email noise and protects creators - and the brand's outreach stays a real, tracked request with a status lifecycle.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_creators` | Free-text search with city, topic, verification-level and result filters |
| `get_creator` | Full public profile by creator ID |
| `request_outreach` | Send a real outreach email for selected creators - a live action, not a test endpoint |
| `get_outreach_status` | Lifecycle status of an outreach request |
| `get_vocab` | Valid topics, cities and verification levels for structured queries |

## Installation

```bash
claude mcp add ugc-vz --transport http https://ugc-vz.de/api/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "ugc-vz": {
      "type": "http",
      "url": "https://ugc-vz.de/api/mcp"
    }
  }
}
```

No credentials. stdio clients can use the npm bridge: `npx -y ugc-vz-mcp`. Calls are rate-limited per caller; agents signing requests with Web Bot Auth get a higher tier. Machine access terms: ugc-vz.de/agb, section 10.

## Business Relevance

- **DACH marketing teams** replace spreadsheet creator sourcing with filterable, verified profiles.
- **E-commerce brands** find product-review creators with real portfolios and social proof.
- **Agencies** run creator searches for clients and track outreach through status lifecycle.
- **Content teams** compare pricing and reach in one surface before committing budget.

## Integration with CorpusIQ

UGC VZ feeds creator discovery into CorpusIQ's marketing workflows. An operator can pull campaign context from CorpusIQ's Google Ads, GA4 or Shopify connectors, use UGC VZ to find DACH creators matching the product's audience, and route the outreach request through the same agent that tracks performance - so creator selection is tied to the actual customer and revenue data rather than guesswork. The gated outreach model also keeps contact data out of the AI until the brand explicitly requests it, matching CorpusIQ's governance posture.

## Limitations

- Brand new - two stars, early-stage directory.
- DACH region only - German-speaking creator market.
- No analytics on creator performance - discovery and outreach, not campaign tracking.
- request_outreach sends real emails - there is no test mode for that tool.
- Free service - no SLA published; rate limits apply per caller.

## See Also

- [Shotstack MCP - Video Editing API for AI Agents](/hermes/mcp/servers/external/shotstack-mcp)
- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
