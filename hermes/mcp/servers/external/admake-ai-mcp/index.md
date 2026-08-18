---
title: "AdMake AI MCP - CorpusIQ Docs - CorpusIQ Docs"
description: AI-powered ad creative generation, competitor research, and publishing to Meta, TikTok, and Pinterest — all from MCP-compatible AI agents
category: Marketing
stars: 0 (brand new)
added: 2026-08-11
source: mcpservers.org
relevance: ★★★
tags: [ads, meta, tiktok, pinterest, creative, ugc, marketing, ecommerce]
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/admake-ai-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"

---

# AdMake AI MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1) for AdMake AI.** Generate Facebook, Instagram and TikTok ad creatives and UGC-style video ads, research competitor ads from the Meta Ad Library, and publish finished ads to Meta via the Marketing API — all from any MCP client.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1
Endpoint: https://admakeai.com/api/mcp
Pricing: Plans from $39/mo (5 free ads, no card)
Category: Marketing / Ad Creative
```

## Why This Matters for Operators

Brands testing 20+ new ads/month see 65% higher ROAS than those testing under 10 (Common Thread Collective Statlas, May 2026). But most small operators ship 10-15 ads/month — top DTC brands run 2,000-4,000 concurrent ads. AdMake AI MCP closes this gap by letting AI agents:

1. **Generate ad creatives** — images and UGC-style videos in batches
2. **Research competitors** — pull ads from Meta Ad Library through the MCP
3. **Publish directly** — push finished ads to Meta Ads Manager via Marketing API

This is the first MCP server that connects the full ad creative lifecycle (research → generate → publish) in a single agent-accessible flow. Previously, operators needed separate tools for each step.

## Tools & Capabilities

The MCP server exposes the AdMake AI platform capabilities:

| Capability | Description |
|---|---|
| **Ad Generation** | Generate Facebook, Instagram, TikTok ad creatives (images + UGC video) |
| **Competitor Research** | Search Meta Ad Library for competitor ads by brand, keyword, or category |
| **Creative Analysis** | Analyze what's working — hook types, formats, angles |
| **Publishing** | Push approved creatives to Meta Ads Manager via Marketing API |
| **Batch Operations** | Generate 10 ads per batch, ~30s per ad |

## Configuration

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "admake-ai": {
      "type": "streamableHttp",
      "url": "https://admakeai.com/api/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_ADMAKEAI_API_KEY>"
      }
    }
  }
}
```

## Getting Started

1. **Sign up** at [admakeai.com/register](https://admakeai.com/register) — 5 free ads, no credit card
2. **Get API key** from your AdMake AI dashboard
3. **Add config** to your MCP client (Claude Desktop, Claude Code, Cursor, etc.)
4. **Start prompting**: "Research what ads Gymshark is running this week, generate 5 UGC-style variations for our product, and push the top 2 to our Meta ad account"

## Use Cases for Business Operators

- **E-commerce brands**: Ship 20+ new ad variants/week instead of 5
- **Agencies**: Generate client ad creatives without a design team
- **DTC operators**: Research competitor ad strategies before launching campaigns
- **Growth teams**: A/B test creative angles at scale through AI agents

## Pricing

- **Free**: 5 free ads on signup (no card required)
- **Paid plans**: From $39/month

Note: Meta ad spend is separate and managed through your Meta Ads account.

## Limitations

- Brand new server (August 2026) — may have rough edges
- Ad quality depends on prompt quality and product assets
- Meta Ad Library access may have regional limitations
- Not open source (commercial product)

## See Also

- [Meta Ads MCP (Pipeboard)](/hermes/mcp/servers/external/meta-ads-mcp/) — campaign management, ad set optimization, performance reporting
- [OpusGrowth MCP](/hermes/mcp/servers/external/opusgrowth-mcp/) — cross-platform ad management (Google, Microsoft, TikTok, LinkedIn)
- [AdMake AI Homepage](https://admakeai.com)
- [AdMake AI MCP Docs](https://admakeai.com/api/mcp)
