---
title: "Tubask MCP — Hosted YouTube Intelligence for AI Agents"
description: "Search YouTube videos, extract transcripts, analyze content, and retrieve metadata — all from a hosted MCP endpoint. Designed for Claude & Cursor with zero infrastructure management."
category: mcp
tags: [mcp-server, youtube, transcripts, content-analysis, video-search, research, content-marketing]
last_updated: 2026-07-02
---

# Tubask MCP Server ★ New (July 2 PM)

## Overview

Tubask MCP (`tubask.app/mcp` · `Amorizz/tubask-mcp`) is a hosted YouTube MCP server designed for Claude, Cursor, and any MCP-compatible client. Search YouTube videos, extract full transcripts, retrieve metadata (titles, descriptions, view counts, publish dates), and analyze video content — all from a remote endpoint with zero infrastructure to manage. Content researchers, marketing teams, and operators who work with YouTube data can now query and analyze video content directly from their AI agents.

**Key advantage**: Hosted endpoint — no API keys to manage, no infrastructure, designed for Claude & Cursor but works with any MCP client.

## Key Features

- **YouTube search**: Search videos by keyword, channel, or topic — returns structured results with metadata
- **Transcript extraction**: Extract full video transcripts with timestamps — support for auto-generated and manual captions
- **Video metadata**: Title, description, view count, like count, publish date, duration, channel info
- **Channel analysis**: Retrieve channel statistics, recent uploads, and content themes
- **Content summaries**: AI-powered video content summarization for quick insights
- **Multi-language**: Transcript extraction across major languages with auto-detection

## Installation

```bash
# Remote endpoint — no local install needed
hermes mcp add tubask --url https://tubask.app/mcp

# Or self-hosted
git clone https://github.com/Amorizz/tubask-mcp.git
cd tubask-mcp
npm install
npm run build
hermes mcp add tubask --command "node" --args "dist/index.js" --workdir "$(pwd)"
```

## Configuration

```json
{
  "mcpServers": {
    "tubask": {
      "url": "https://tubask.app/mcp",
      "transport": "sse"
    }
  }
}
```

For self-hosted, add YouTube API key:

```json
{
  "mcpServers": {
    "tubask": {
      "command": "node",
      "args": ["dist/index.js"],
      "workdir": "/path/to/tubask-mcp",
      "env": {
        "YOUTUBE_API_KEY": "your-youtube-data-api-key"
      }
    }
  }
}
```

## Business Relevance

- **Content Research**: Marketing teams can analyze competitor YouTube content — "extract transcripts from top 10 videos about 'AI customer service' and identify common themes"
- **Competitive Intelligence**: Track competitor video publishing cadence, content themes, and audience engagement metrics over time
- **Video SEO**: Analyze top-performing videos in your niche — extract titles, descriptions, and tags to inform your own video SEO strategy
- **Content Repurposing**: Extract transcripts → summarize → convert to blog posts, social threads, newsletters
- **Market Research**: "What are customers saying about [product] in YouTube reviews?" — sentiment analysis from video transcripts at scale

## Integration with CorpusIQ

Tubask MCP enhances CorpusIQ's content and research capabilities, complementing existing YouTube and content tools:

- **Content Pipeline**: Tubask (transcripts) → HumanTone (humanize) → Blog2Video (repurpose) — AI-driven content recycling
- **Competitive Monitoring**: Combine with SEO tools (SE Ranking, OpenSEO) — track both video and web presence of competitors
- **Lead Intelligence**: Tubask (competitor video analysis) → Google Maps Email Extractor (maps leads) → SyncGTM (enrichment) — multi-source lead intelligence
- **Market Research**: Pair with Paper Search MCP for academic context — video content analysis + academic research = comprehensive market intelligence
- **Social Publishing**: Extract insights → draft posts → publish via FeedSquad or Solnk — content insight to publication pipeline

## Limitations

- Hosted endpoint may have rate limits and usage quotas
- Self-hosted requires YouTube Data API key (free quota: 10,000 units/day)
- Transcript quality depends on YouTube's auto-captioning for non-manually-captioned videos
- YouTube API quota costs apply at scale — self-hosted with own API key recommended for heavy usage

## See Also

- [Scribefy — YouTube Transcripts](/hermes/mcp/servers/external/)
- [Valossa Assistant — Multimodal Video AI](/hermes/mcp/servers/external/)
- [Blog2Video — Blog to Video Conversion](/hermes/mcp/servers/external/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
