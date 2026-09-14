---
title: "Statiko MCP - Telegram Channel Intelligence for Agents"
description: "Remote MCP server over live public Telegram data: trending stories with momentum, channel profiles and growth metrics, similar-channel cohorts, post history with edits and deletions, and per-post stat evolution. 10 read-only tools, every result citing its statiko.io page. initialize and tools/list are open; tool calls need a Pro or Business account over OAuth 2.1."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-09-14
source: "mcp.so feed (statiko) + vendor docs at statiko.io/product/mcp"
relevance: ★★
tags: [telegram, osint, trends, social-media, monitoring, analytics, oauth, remote-mcp]
---

# Statiko MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1)** - live intelligence from public Telegram channels for any MCP client. Telegram is where a large share of niche communities coordinate, and Statiko turns that layer into agent-readable data: what is trending right now with momentum and sparklines, how channels grow and engage, what similar channels look like, and what changed in a channel's history - including post edits and deletions. Ten read-only tools; every result carries its statiko.io permalink so a human can open the same page the model read.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (tool calls require a Statiko Pro or Business account)
Endpoint: https://mcp.statiko.io/mcp
Tools: 10 (all read-only; initialize and tools/list answer anonymously)
Pricing: Pro from $20/month; Business tier above
Category: Data & Analytics
Built by: Statiko (statiko.io)
```

## Why This Matters for Operators

Community signals move before they show up in dashboards, and Telegram is often the first place a topic, a competitor complaint or a coordinated campaign appears. Statiko makes that channel readable to agents with three capabilities that matter for operators. Trend data arrives scored and contextualized instead of as a raw feed. Channel metrics come as dated sparklines, so growth can be read as a curve rather than a number. And the timeline tool captures structural events - renames, description and photo changes, verification flips, subscriber milestones, post edits and deletions - which is how you tell what actually happened on a given date, a question screenshots cannot answer.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `get_trending_topics` | ranked board of trending stories across tracked channels for a rolling 24h window, with momentum and hourly sparklines |
| `get_trend_samples` | real posts behind each trending story, for reading the actual conversation |
| `search_channels` | find tracked channels by name, filtered by verification, category, language and activity |
| `get_channels` | one channel's full profile, or compact comparison rows for up to 10 channels over 30 days |
| `get_channel_posts` | recent posts with views, forwards, replies and reaction maps; text search and time ranges |
| `get_post_stats` | how a post's views, forwards and reactions evolved, bucketed per hour or day |
| `get_channel_timeline` | structural events: edits, deletions, renames, verification flips, milestones |
| `get_similar_channels` | peer cohort for a channel, for comparing metrics against real comparables |
| `search` | Statiko search over tracked channels and trending stories, returning document ids |
| `fetch` | full document behind a search id: a channel profile or a trending story |

## Installation

```bash
claude mcp add statiko --transport http https://mcp.statiko.io/mcp
```

Claude.ai: Settings, Connectors, Add custom connector, paste the endpoint. ChatGPT: Settings, Apps and Connectors, Developer mode, create with the URL and complete OAuth. The tools/list response is open to inspect before subscribing.

## Configuration

```json
{
  "mcpServers": {
    "statiko": {
      "type": "http",
      "url": "https://mcp.statiko.io/mcp"
    }
  }
}
```

## Business Relevance

- **Marketing and community teams** watch what a niche is talking about now, with the posts behind each trend.
- **Competitive intelligence** reads peer-channel cohorts and growth curves instead of anecdotal screenshots.
- **PR and comms** catch the edit and deletion trail on claims that keep circulating.
- **Research and analyst roles** get dated, citable series for channel and topic momentum.

## Integration with CorpusIQ

Statiko covers the Telegram layer of the community picture; the catalogued RedReplier guide covers Reddit, Facebook, Hacker News, X and Bluesky. Together they give an agent monitoring coverage across the platforms where business conversations actually start. Inside CorpusIQ workflows, trend and channel signals can be composed with the business data side - for example, cross-referencing a spike in regional chatter with orders or support volume from the same period.

## Limitations

- Public channels only; nothing private, and the tracking set is Statiko's catalog.
- Read-only: 10 tools, no writes anywhere.
- Tool calls require a Pro (from $20/month) or Business subscription; anonymous use is limited to initialize and tools/list.
- Sparkline and stat series depend on Statiko's own recording windows.
- Brand new listing: no long third-party track record yet.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [RedReplier MCP - Social Lead Monitoring and Reply Drafts for Agents](/hermes/mcp/servers/external/redreplier-mcp/)
- [TrendPulse MCP - Google News and Trends Research](/hermes/mcp/servers/external/trendpulse-mcp/)
