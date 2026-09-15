---
title: YoTrends MCP - Live YouTube and TikTok Trends as Content Packs
description: Remote MCP server that pulls live YouTube and TikTok trend data across nine markets into your own AI assistant, with 8 tools for trend search, topic tracking, rising-creator discovery, digests and publish-ready text packs (titles, hooks, script, tags) generated from trends already proven to be rising.
category: Content
stars: n/a (new listing)
added: 2026-09-10
source: mcpservers.org /all via r.jina.ai
relevance: ★★★
tags: [content, trends, youtube, tiktok, creator-research, social-media, remote-mcp, marketing]
---

# YoTrends MCP

**Remote MCP server (Streamable HTTP, Bearer token)** - a YouTube and TikTok trend analytics tool covering nine markets (US, Russia, Japan, Mexico, Indonesia, Saudi Arabia, Thailand, Vietnam, South Korea) that turns live trends into content ideas from inside your own AI assistant. The loop: pull live trends, filter to your tracked topics, check what top and rising creators are doing, then generate a publish-ready text pack.

```
Server type: Remote (hosted, Streamable HTTP)
Auth: Bearer token (generated in YoTrends profile under Connect to AI, shown once)
Endpoint: https://app.yotrends.ai/mcp/
Repo / tool reference: github.com/29user/yotrends-mcp
```

## Tools

| Tool | What it does |
|---|---|
| `search_trends` | Find rising trends on YouTube and TikTok |
| `list_trend_clusters` | See trends grouped into themes |
| `list_top_creators` | Surface top and rising creators |
| `list_my_topics` | List the topics you track |
| `get_topic_feed` | Pull the latest in a topic |
| `create_topic` | Start tracking something new |
| `get_topic_digest` | Get an AI narrative summary of a topic |
| `generate_text_pack` | Write titles, hooks, a script and tags |

`generate_text_pack` returns everything needed to publish: video titles, hooks, a script outline and tags. Because the input is a trend already proven to be rising, the demand question is answered before the writing starts. `list_top_creators` surfaces two views: rising creators ranked by growth velocity, and the precomputed leaders in a niche - rising tells you where momentum is, top tells you who set the standard.

## Connection

```
{
  "mcpServers": {
    "yotrends": {
      "url": "https://app.yotrends.ai/mcp/",
      "headers": { "Authorization": "Bearer <your token>" }
    }
  }
}
```

## Weekly Content-Calendar Loop

1. Monday - ask for a digest of each tracked topic to see what moved.
2. Tuesday - pick the strongest rising trends and generate text packs for the week.
3. Wednesday onward - film and publish against the packs.

For social and marketing teams, one person runs the digest pass and hands finished text packs to the people filming, keeping the calendar a few weeks ahead.

## Verification (Sep 10, 2026 night sweep)

Endpoint `https://app.yotrends.ai/mcp/` live-probed over JSON-RPC: anonymous initialize rejected with HTTP 401 "Invalid or missing MCP token. Generate one in YoTrends → Settings → Connect to AI" - live, key-gated endpoint with a clear remediation message. Full tool table and per-market coverage published on the directory listing.

## See Also

- [ViralHunt MCP - Trending Discovery and Social Publishing for Agents](/docs/hermes/mcp/servers/external/viralhunt-mcp)
- [Capslane MCP - Timestamped YouTube Transcripts for Agents](/docs/hermes/mcp/servers/external/capslane-mcp)
- [LinkDigest MCP - Social Post URLs to LLM-Readable Text](/docs/hermes/mcp/servers/external/linkdigest-mcp)
