---
title: "Xpoz MCP — Social media intelligence for AI agents"
description: "3B+ posts indexed across Twitter/X, Instagram, Reddit, and TikTok. Brand monitoring, social listening, lead generation, and competitive intelligence — no"
category: mcp
tags: [mcp-server, social-media, brand-monitoring, lead-generation, competitive-intelligence]
source: mcp.so GitHub issues (#3507)
discovered: 2026-08-11
stars: 10
author: Xpoz (IdoXpoz)
github: github.com/xpozpublic/xpoz-mcp
mcp_endpoint: https://mcp.xpoz.ai/mcp
transport: Streamable HTTP
auth: OAuth 2.1
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/xpoz-mcp/"
robots: "index,follow"
last_updated: "2026-08-12"

---

# Xpoz MCP Server

**The social data API for AI agents.** Xpoz gives AI agents natural-language access to 3 billion+ indexed posts across Twitter/X, Instagram, Reddit, and TikTok — no platform API keys required. Brand monitoring, social listening, lead generation, and competitive intelligence through one MCP endpoint.

## Why It Matters for Operators

Social media intelligence has traditionally required juggling multiple platform APIs (Twitter API, Instagram Graph API, Reddit API, TikTok API) — each with separate auth, rate limits, and data formats. Xpoz abstracts all four behind a single MCP endpoint:

- **Brand monitoring:** *"Find tweets about 'CorpusIQ' with more than 500 retweets this month"*
- **Social listening:** *"Who are the most influential Instagram accounts posting about AI business tools?"*
- **Lead generation:** *"Show me Reddit discussions where people are asking for alternatives to HubSpot"*
- **Competitive intel:** *"Track TikTok mentions of [competitor] over the past 30 days"*
- **Trend detection:** *"What's the sentiment around 'MCP servers' on Twitter this week?"*

For business operators, this replaces manual social monitoring with conversational intelligence — ask your agent what's happening across platforms and get answers in seconds.

## Technical Details

| Field | Value |
|-------|-------|
| **Transport** | Streamable HTTP |
| **Auth** | OAuth 2.1 |
| **Endpoint** | `https://mcp.xpoz.ai/mcp` |
| **Platforms** | Twitter/X, Instagram, Reddit, TikTok |
| **Posts indexed** | 3B+ |
| **Setup time** | ~2 minutes |
| **Free tier** | Yes (trial available) |
| **SDKs** | Python (`pip install xpoz`), TypeScript, CLI |
| **GitHub** | [xpozpublic/xpoz-mcp](https://github.com/xpozpublic/xpoz-mcp) (MIT, 10⭐) |

## Setup

### Claude Desktop

```json
{
  "mcpServers": {
    "xpoz": {
      "url": "https://mcp.xpoz.ai/mcp"
    }
  }
}
```

OAuth 2.1 flow handles authentication — no API key to copy. On first connection, Xpoz opens a browser window for authorization.

### Claude Code / Cursor / Codex

```json
{
  "mcpServers": {
    "xpoz": {
      "url": "https://mcp.xpoz.ai/mcp"
    }
  }
}
```

### Python SDK (for programmatic use)

```bash
pip install xpoz
```

```python
from xpoz import XpozClient

client = XpozClient()
results = client.search(
    query="AI business tools",
    platform="twitter",
    timeframe="last_30_days"
)
```

## CorpusIQ Integration

Xpoz + CorpusIQ is a growth operator's command center: use Xpoz for top-of-funnel social intelligence (brand mentions, competitor activity, lead signals), then use CorpusIQ to qualify those signals against actual business data (are the companies mentioning your competitor also in your CRM? what's their revenue band?). For growth operators, this closes the loop between social listening and business qualification.

Pair with LinkedMash (LinkedIn content ops) for publishing, and SiteGuru (SEO) for organic search — a complete operator visibility stack.

## Limitations

- Remote-only (no local stdio transport) — requires internet connectivity
- Rate limits on free tier (paid plans for higher volume)
- Sentiment analysis quality varies by platform and language
- 3B+ posts indexed but real-time coverage depends on indexing frequency
- Relatively new (10 stars, 18 commits) — API may evolve

## Verdict: ★★★

**Best-in-class social MCP.** The "no platform API keys" design is the killer feature — operators don't need Twitter API approval, Instagram Business accounts, or Reddit API credentials. Multi-platform coverage in one endpoint. Trusted by NYU, UC Berkeley, Columbia, Georgia Tech, and the Linux Foundation. For any operator doing brand monitoring or social listening, this is the first MCP to install.

## See Also

- [LinkedMash MCP](/hermes/mcp/servers/external/linkedmash-mcp/) — LinkedIn saved posts + content publishing
- [SiteGuru MCP](/hermes/mcp/servers/external/siteguru-mcp/) — SEO audit + rankings
- [AfterLaunch MCP](/hermes/mcp/servers/external/afterlaunch-mcp/) — AI answer visibility + GEO
- [Pangolinfo MCP](/hermes/mcp/servers/external/pangolinfo-mcp/) — Amazon + e-commerce intelligence
