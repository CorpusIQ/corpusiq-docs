---
title: "tube-bridge MCP - Self-Hosted YouTube Research and Transcript Corpora"
description: "Self-hosted YouTube research MCP server for AI agents: 17 tools for video and channel discovery, transcripts with timestamps, comments, playlists, ephemeral timestamped frames, and private local semantic-search corpora — 14 tools work without a YouTube API key"
category: Content & Research
stars: n/a (new listing)
added: 2026-08-20
source: "mcp.so GitHub issue #3655"
relevance: ★★
tags: [youtube, transcripts, research, semantic-search, local-first, video-analysis, corpus, self-hosted, stdio-mcp]
---

# tube-bridge MCP

**Self-hosted YouTube research for AI agents — transcripts, frames, and private semantic corpora on your own machine.** tube-bridge is a 17-tool MCP server that turns YouTube into a queryable research surface: search videos and channels, read transcripts (optionally with `[MM:SS]` timestamps), pull comments and playlists, extract one ephemeral JPEG frame at an exact millisecond, and build private semantic-search corpora over collected transcripts. Fourteen tools need no YouTube API key; only comments and channel-search tools require an optional user-supplied key.

```
Server type: Self-hosted stdio (uvx) — optional self-hosted Streamable HTTP or Docker
Install: uvx tube-bridge
Tools: 17 (14 keyless, 3 optional YouTube API key)
License: MIT
Registry: io.github.TheWhiteWater/tube-bridge (PyPI v1.1.6, active)
Built by: TheWhiteWater
```

## Why This Matters for Operators

Competitor videos, founder interviews, and channel research are a material research source that most agents handle badly — transcripts pulled ad hoc, no way to search across them, no way to cite the exact moment. tube-bridge fixes the workflow end to end: `youtube_search` finds candidates, `youtube_get_transcript` pulls text with timestamps, `corpus_add` chunks and locally embeds it (80-second windows, 20-second overlap, BGE-small-en-v1.5 via fastembed), and `corpus_search` returns similarity scores with canonical video URLs and timestamped deep links. `youtube_get_frame` returns a bounded JPEG near any transcript finding so an agent can verify visually that the quote matches the frame.

The privacy posture is the differentiator: transcripts, SQLite databases, vectors, and indexes stay on the operator's machine — there is no hosted intermediary, no account, and no managed storage. Everything is local-first and MIT-licensed.

## Tools & Capabilities

| Capability | Tools | YouTube API key |
|---|---|---|
| Discovery | `youtube_search`, `youtube_get_video_info`, `youtube_get_trending` | Optional (yt-dlp fallback without) |
| Content | `youtube_get_channel_videos`, `youtube_get_playlist`, `youtube_get_transcript`, `youtube_get_available_languages` | No |
| Visual evidence | `youtube_get_frame` (ephemeral JPEG at exact millisecond, needs ffmpeg) | No |
| Engagement | `youtube_get_comments`, `youtube_search_channels`, `youtube_get_channel_info` | Required |
| Local corpus | `corpus_create`, `corpus_add`, `corpus_search`, `corpus_list`, `corpus_delete` | No |
| Runtime docs | `tube_bridge_help` | No |

Corpus results return similarity score, time span, video title, canonical URL, and timestamp URL — built for citation, not just answers.

## Installation

```bash
uvx tube-bridge
```

```json
{
  "mcpServers": {
    "tube-bridge": {
      "command": "uvx",
      "args": ["tube-bridge"]
    }
  }
}
```

```bash
claude mcp add --scope user tube-bridge -- uvx tube-bridge
```

Requires Python 3.12+. `ffmpeg` is only needed for `youtube_get_frame`; the first embedding operation downloads the local model. Alternatives: `pip install tube-bridge` for a persistent install (stdio, or `tube-bridge --http` for Streamable HTTP on port 8080), or `docker run -p 8080:8080 ghcr.io/thewhitewater/tube-bridge:latest` with `/health` and `/mcp` endpoints.

## Configuration

```bash
export YOUTUBE_API_KEY="your-key"        # optional — unlocks comments + channel tools
export TUBE_BRIDGE_PROXY="http://..."    # optional — routes yt-dlp/transcript calls via proxy
export TUBE_BRIDGE_CACHE="/path/to/data" # optional — moves corpus and cache databases
export TUBE_BRIDGE_AUTH_KEY="long-random" # optional — Bearer-protects self-hosted HTTP routes
```

A YouTube Data API v3 key (Google Cloud Console) unlocks the three API-only tools and upgrades search reliability. Corpus storage is SQLite plus sqlite-vec under `~/.tube_bridge/corpus.db`; embedding inference runs locally after a one-time model download.

## Business Relevance

- **Market and competitor research** — search competitor channels, corpus their uploads, ask questions across months of content with timestamp citations
- **Interview and earnings-call mining** — transcripts with `[MM:SS]` links make every finding quotable with a deep link
- **Content teams** — frame-level visual verification without building a media library
- **Privacy-conscious operators** — all research artifacts stay on-premise; nothing is shipped to a vendor

## Integration with CorpusIQ

tube-bridge is the research front-end; CorpusIQ is the business record layer. An agent can research a competitor's YouTube presence with tube-bridge — corpus their uploads, extract pricing mentions and product claims with timestamp URLs — then verify the claims against CorpusIQ's connectors: their web analytics via GA4/Semrush, their company record via HubSpot or QuickBooks-side vendor data, and the outreach follow-up via email. The timestamped transcript citations give the "where did we see this" audit trail that pairs with CorpusIQ's source-declared reporting.

## Limitations

- Self-hosted only — no hosted endpoint or managed storage is provided
- New listing (Aug 2026), zero-star repository, single maintainer
- `youtube_get_frame` requires ffmpeg and re-downloads a temporary section per call
- ToS posture: pulls public YouTube content via yt-dlp and youtube-transcript-api; operators should respect YouTube's terms for commercial use

## See Also

- [Arc Research MCP — Commodities Research & Knowledge Graph](/hermes/mcp/servers/external/arc-research-mcp/)
- [APITube News MCP — News Search with Sentiment & Entity Filters](/hermes/mcp/servers/external/apitube-news-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
