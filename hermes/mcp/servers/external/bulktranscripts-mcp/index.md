---
title: BulkTranscripts MCP - Hosted YouTube Transcripts and Channel
description: "Hosted remote MCP server for YouTube research: fetch clean transcripts (single or batch), search videos, channels and playlists, list channel or playlist archives, and track new uploads. No signup, 50 free transcript extractions per IP, live-probed 7 tools."
category: Content & Research
stars: n/a (new listing)
added: 2026-08-23
source: "mcpservers.org homepage + live endpoint probe"
relevance: ★★★
tags: [youtube, transcripts, research, content, remote-mcp, hosted]
---

# BulkTranscripts MCP

**One URL gives an MCP client real YouTube access: transcripts, search, channel and playlist archives, and new-upload tracking, with no install and no signup.** BulkTranscripts is a hosted streamable-HTTP MCP server at `bulktranscripts.co/mcp` that rides the same production extraction chain as the BulkTranscripts web app (residential proxy routing, proof-of-origin tokens, retries, and a shared cache serving popular videos instantly). Anonymous connections get 50 free transcript extractions per IP; cached transcripts and re-exports never cost a credit, and the new-uploads tool is free forever.

```
Server type: Remote (Streamable HTTP, hosted)
Auth: Keyless to start; optional license key as Bearer header (or ?key= parameter)
Endpoint: https://bulktranscripts.co/mcp
Tools: 7 (live-probed; server v1.0.0, protocol 2025-03-26)
Pricing: 50 free transcript extractions per IP, then one-time credit packs (no subscription)
Built by: BulkTranscripts (bulktranscripts.co)
```

## Why This Matters for Operators

Most YouTube MCP servers on GitHub run yt-dlp locally and die on YouTube bot checks within a week of setup. **BulkTranscripts is maintained infrastructure: a hosted server with proxy rotation, retries and a shared cache, so transcripts keep flowing while you do other work.** For operators, that converts video content from a black box into queryable business data: competitor channel monitoring, creator research, market intelligence from talks and interviews, and batch notes from courses and playlists.

The workflow the toolset enables is deliberately agentic: list a channel archive (up to 1,000 videos), pick candidates, then read only the transcripts that matter. A one-line MCP add in Claude Code, Cursor, VS Code or ChatGPT developer mode is the entire install.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| get_transcript | Full transcript of one YouTube (or TikTok) video as clean text with metadata: title, channel, duration, upload date |
| get_transcripts | Batch fetch up to 20 videos per call from YouTube URLs or ids (1 credit per uncached video) |
| search_youtube | Keyword search across videos, channels or playlists (type parameter) |
| search_channel | Topic search inside one channel's uploads, for researching what a creator has said |
| get_channel_videos | List a channel's videos (id, title, duration, URL) without fetching transcripts; accepts @handle, channel URL or id |
| get_playlist_videos | List every video in a playlist, in playlist order (courses and series keep their sequence) |
| get_latest_videos | Newest uploads (up to 15) with publish dates from YouTube RSS; always free, no credit charged |

Seven tools confirmed by live probe (the marketing page lists six; the probe is the ground truth). The batch tool costs 1 credit per uncached video; already-cached videos return instantly and free.

## Installation

```json
{
  "mcpServers": {
    "bulktranscripts": {
      "type": "http",
      "url": "https://bulktranscripts.co/mcp"
    }
  }
}
```

For the Claude Code CLI: `claude mcp add --transport http bulktranscripts https://bulktranscripts.co/mcp`

## Configuration

Start keyless: anonymous connections get 50 free transcript extractions per public IP with no account and no credit card. When the free allowance runs out, buy a one-time credit pack and pass its license key as a Bearer header (`Authorization: Bearer YOUR_KEY`), or as a `?key=` parameter for clients that cannot send headers. There is no subscription tier.

## Example Prompts

- "Summarize this talk with key quotes."
- "Turn this course playlist into study notes."
- "Watch these three competitor channels and brief me on new uploads each morning."
- "List everything this creator has said about our category across their channel archive."

## Business Relevance

Video is where competitor positioning, creator partnerships and market shifts show up first, and transcript data is the cheapest way to index it. BulkTranscripts turns that into a zero-infrastructure subscription to YouTube's text layer: competitor channel monitoring, conference talk distillation, playbook extraction from courses, and creator research before outreach. The free-latest-uploads tool doubles as a lightweight "what did this channel post this week" monitor that never costs a credit.

## Integration with CorpusIQ

CorpusIQ answers questions about business data: what campaigns earned, which channels convert, where revenue comes from. BulkTranscripts supplies the external market and content layer those answers live next to: an agent can pull a competitor's newest videos (BulkTranscripts), extract positioning and tool mentions from the transcripts, and cross-check claims against live business metrics in CorpusIQ. BulkTranscripts covers YouTube content; CorpusIQ's 40+ connectors remain the read-side authority for the business systems themselves.

## Limitations

- Credit metering is IP-based for the free tier, so multiple agents behind one NAT share the 50-extraction allowance.
- TikTok transcript support exists on get_transcript but the archive and search tools are YouTube-only.
- No write path: the server reads YouTube data only, no comments API, no posting surface.
- Requires the license key for sustained volume; there is no subscription, so heavy use means repeated credit packs.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [tube-bridge MCP](/docs/hermes/mcp/servers/external/tube-bridge-mcp) - self-hosted YouTube research with local semantic search
- [viral-outliers MCP](/docs/hermes/mcp/servers/external/viral-outliers-mcp) - viral social outlier database with transcripts
- [MCP Integration Guide](/docs/hermes/mcp) - connecting MCP servers to Hermes Agent
