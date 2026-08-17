---
title: "AdWhispr MCP - CorpusIQ Docs"
description: Complete ad workflow MCP — research any brand's live Facebook/TikTok ads, clone the proven winners, and launch real campaigns on Google, TikTok, and Meta — all from AI chat
category: Marketing / Advertising
stars: featured
added: 2026-08-11
source: mcp.so
relevance: ★★★
tags: [ads, meta, google-ads, tiktok-ads, competitor-research, ad-creative, campaign-launch, marketing]
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/adwhispr-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"

---

# AdWhispr MCP

**Remote MCP server (Streamable HTTP, OAuth) for the full advertising loop.** Turn Claude, ChatGPT, or Cursor into a complete ad workflow: research any brand's live Facebook and TikTok ads (ranked by days running), clone the proven winners for your own brand, and launch real campaigns on Google, TikTok, and Meta — all through natural language.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in)
Endpoint: https://adwhispr.com/api/mcp
Pricing: Free tier → Pro $39/mo (unlimited research) → Agency $149/mo
Category: Marketing / Advertising
```

## Why This Matters for Operators

The ad creative supply chain is broken for small operators. Top brands run 2,000-4,000 concurrent ads with dedicated creative teams. Small operators ship 10-15 ads/month and guess at what works. AdWhispr MCP solves this with three capabilities no other MCP combines:

1. **Competitor ad intelligence** — See what ads your competitors are actually running (ranked by days running — the honest proxy for ad performance), with AI classification of hooks, formats, tones, and offers
2. **Creative cloning** — Take a winning competitor ad, customize it to your brand (image or video), and get a ready-to-launch creative
3. **Multi-platform launch** — Push campaigns to Google Search, Performance Max, TikTok, and Meta with a preview step before anything spends

This is the first MCP that closes the full loop: research → creative → launch. Combined with our existing AdMake AI guide (creative generation + Meta publishing), operators can now build an AI-driven ad studio.

## Tools & Capabilities

| Capability | Description |
|---|---|
| **Competitor Ad Research** | Search any brand's live Facebook ads, ranked by days running |
| **Competitor Discovery** | Find verified competitors running ads in your niche right now |
| **AI Ad Classification** | Automatic classification of hooks, formats, tones, and offers |
| **Semantic Ad Search** | Search ads by concept ("social proof", "urgency", "founder story") |
| **Creative Cloning** | Clone a winning competitor ad (image or video), customized to your brand |
| **Multi-Platform Launch** | Launch on Google Search, Performance Max, TikTok, and Meta Ads |
| **TikTok Ad Research** | Research TikTok ads alongside Facebook |
| **Google Keyword Intelligence** | Keyword data for search campaigns |

## Configuration

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "adwhispr": {
      "type": "streamableHttp",
      "url": "https://adwhispr.com/api/mcp"
    }
  }
}
```

Or via Claude Code:
```
claude mcp add adwhispr --transport http https://adwhispr.com/api/mcp
```

First connection opens a browser for OAuth sign-in (free account, no card required). Credentials are reused for subsequent sessions.

## Use Cases for Business Operators

- **Competitive intelligence:** "Find the longest-running ad from my 3 biggest competitors and tell me what hooks and formats they're using"
- **Rapid creative iteration:** "Clone Gymshark's top-performing ad but switch it to my supplement brand, change the hook to a problem/solution angle"
- **Campaign deployment:** "Launch this cloned ad on TikTok at $50/day and Google Performance Max at $30/day"
- **Market research:** "Who's running the best ads in the meal delivery niche right now?"
- **Competitive briefs:** "Generate a competitive ad brief for [Brand]: longevity curve, top hooks, format mix, offer patterns"

## Verdict

★★★ **Catalogue immediately.** AdWhispr is the most complete ad workflow MCP observed to date — it covers the full creative lifecycle (research → clone → launch) across three ad platforms. The "days running" ranking as a proxy for ad performance is a genuinely useful heuristic that raw ad libraries don't provide. Combined with AdMake AI MCP (for net-new creative generation), operators now have a two-tool ad studio: AdWhispr for competitive cloning + AdMake AI for original creative. Pro tier at $39/mo is accessible for serious operators.

**CorpusIQ angle:** This directly serves the operator use case of "I don't have a creative team — help me compete." Operators who use CorpusIQ for business analytics can now also run ad campaigns through the same AI interface.

## Additional Resources

- [AdWhispr Homepage](https://adwhispr.com/connect)
- [AdWhispr Integrations](https://adwhispr.com/integrations)
- [GitHub: adwhispr/mcp-server](https://github.com/adwhispr/mcp-server)
- MCP.so listing: `https://mcp.so/servers/adwhispr-research-clone-launch-ads-from-claude-chatgpt`
