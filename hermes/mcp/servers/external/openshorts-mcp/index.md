---
title: OpenShorts MCP - Video Clipping and Publishing for AI Agents
description: OpenShorts turns long videos into 9:16 shorts through MCP. AI moment detection, face-tracked reframing, word-level subtitles and direct publishing to TikTok, Instagram Reels and YouTube Shorts. Eight tools cover the pipeline, with a free MIT self-hosted edition.
category: Content
stars: n/a (new listing)
added: 2026-09-04
source: mcpservers.org
relevance: ★★★
tags: [video-clipping, shorts, tiktok, youtube-shorts, content-repurposing, oauth, streamable-http, remote-mcp]
---

# OpenShorts MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 or API key)** - the native agent surface of OpenShorts, the long-video to shorts pipeline. Eight tools cover the whole flow: process a video, track the job, list clips, restyle subtitles and publish to TikTok, Instagram Reels and YouTube Shorts. The same endpoint runs self-hosted, unmetered, under MIT.

```
Server type: Remote (Streamable HTTP) or self-hosted (MIT)
Auth: OAuth 2.1 with dynamic client registration, or osk_ API key as bearer
Endpoint: https://mcp.openshorts.app/mcp
Tools: 8
Pricing: Free 20 min/mo cloud · from $12/mo for 100 min · self-hosted free
Category: Content
Built by: OpenShorts (source at github.com/mutonby/openshorts)
```

## Why This Matters for Operators

Repurposing a podcast or webinar into shorts is an afternoon in an editor times three platforms. OpenShorts compresses it to one instruction: clip this, schedule the best three to TikTok. **Every MCP call draws from the same flat minute balance as the dashboard, and the self-hosted edition serves the same endpoint with no meter at all, which is rare in this market.**

Agent calls are not billed separately from normal usage, a sharp contrast with competitors that meter per source minute or per operation. Completion webhooks are HMAC-signed, so pipeline builders get one POST per finished job instead of polling loops.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `process_video` | Start clipping a video from a URL or upload_id; returns a job id immediately |
| `create_upload` | Reserve an upload slot and receive a presigned URL for local files |
| `get_job_status` | Progress, recent log lines and the clips once a job completes |
| `list_clips` | Titles, durations, platform-ready descriptions and download URLs |
| `get_quota` | Plan and remaining minutes before starting a large job |
| `add_subtitles` | Restyle burned-in captions, classic or karaoke word highlighting |
| `recut_clip` | Recut an existing clip against new bounds |
| `publish_clip` | Post or schedule a clip to TikTok, Instagram or YouTube |

## Installation

```bash
claude mcp add --transport http openshorts https://mcp.openshorts.app/mcp
```

For CLI and workflow clients, create an osk_ API key in the account page and attach it as a bearer Authorization header. Self-hosters point the client at http://localhost:8000/mcp after starting the Docker edition.

## Configuration

```json
{
  "mcpServers": {
    "openshorts": {
      "url": "https://mcp.openshorts.app/mcp"
    }
  }
}
```

Auth notes: claude.ai and ChatGPT connect with the URL alone through OAuth 2.1 with dynamic client registration, no key to copy. API-key clients pass the osk_ key as the bearer Authorization header. The account page has copy-ready snippets for Claude Desktop, Cursor, n8n and curl.

## Business Relevance

- **Podcasters** turn one episode into three to fifteen vertical clips with word-level captions.
- **Content teams** schedule clips to TikTok, Reels and Shorts directly from the assistant.
- **Agency operators** run pipelines on webhooks instead of polling, with HMAC-signed delivery.
- **Cost-conscious teams** self-host the MIT edition and remove the meter entirely.

## Integration with CorpusIQ

OpenShorts produces the content; CorpusIQ measures whether it worked. After clips publish to TikTok and YouTube, CorpusIQ's GA4 and Shopify connectors show which formats drove sessions and sales, and the operator feeds that back into the next clip request. CorpusIQ closes the attribution loop that a pure publishing tool cannot see.

## Limitations

- Cloud processing spends from the same minute balance as the dashboard; check quota before large jobs.
- The self-hosted edition needs a GPU for the ~50 second processing times the cloud offers; CPU-only runs are slower.
- Publishing requires connected TikTok, Instagram or YouTube accounts with the platform's own approval flows.
- Free cloud tier is 20 minutes per month with a watermark.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [Shotstack MCP: Video Editing API for AI Agents](/hermes/mcp/servers/external/shotstack-mcp)
- [ReelDrop MCP - Instagram Reel Scheduling and Analytics](/hermes/mcp/servers/external/reeldrop-mcp)
