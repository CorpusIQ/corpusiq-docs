---
title: "CraftStory MCP - Talking-Avatar and UGC Video Generation for Agents"
description: "Local MCP server that exposes the CraftStory API as tools: turn one photo into a lip-synced talking video with gestures (CraftStory 2.0, any length up to 30 minutes) or a 5-15 second clip with generated sound (MiniMax H3). 180+ voices in 30+ languages, custom avatars, cost preview and bounded job polling. npm package, MIT."
category: "Content"
stars: 0 (new repo)
added: 2026-09-12
source: "mcp.so feed (craftstory) + npm @craftstory/mcp + github.com/itseez3d/craftstory-mcp"
relevance: ★★
tags: [video, talking-avatar, ugc, ads, content-generation, npm]
---

# CraftStory MCP

**Local MCP server (npm, stdio)** - exposes the CraftStory API as tools so Claude, Cursor and other MCP clients generate videos: one photo becomes a talking-avatar video with lip-sync, natural gestures and expressions (CraftStory 2.0), or a short clip with generated sound or lip-synced to your audio (MiniMax H3). Aimed at UGC and product ads at scale, personalized video outreach and localized explainers.

```
Server type: Local (stdio via npx)
Auth: CraftStory API key (sk-cs-..., from Account - API Access; a plan with API access is required)
Package: @craftstory/mcp (npm, v0.1.3)
Source: github.com/itseez3d/craftstory-mcp (MIT)
Talks to: api.craftstory.com over HTTPS
Category: Content
Built by: itseez3d / CraftStory (craftstory.com/mcp)
```

## Tools

| Tool | Purpose |
|---|---|
| create_craftstory2_video | Photo (or a custom avatar scene) plus audio clips become a lip-synced talking video with gestures; portrait or landscape, any length |
| create_minimax_h3_video | 5-15 second clip from one photo with generated sound, or lip-synced to your own audio |
| list_voices | 180+ library voices in 30+ languages, plus voices cloned in the app |
| create_audio_clip | Synthesize speech from text or upload a recording |
| list_avatars | Custom avatars trained in the app, usable from the tools |
| wait_for_job | Polls in bounded slices (55 s max per call) so assistants never hang |
| get_job_status | Progress and failure reasons |
| get_job_result | Returns the finished video URL; failed jobs are refunded |
| preview_cost | Credit price before committing |
| upscale_video | 1080p render (CraftStory 2.0) or 2x (MiniMax H3) as a new job |

## Connection

1. Get an API key in the CraftStory app (Account, API Access; keys look like `sk-cs-...`; requires a plan with API access).
2. Claude Code: `claude mcp add --scope user craftstory -e CRAFTSTORY_API_KEY=sk-cs-... -- npx -y @craftstory/mcp`
3. Claude Desktop / Cursor: command `npx`, args `["-y", "@craftstory/mcp"]`, env `CRAFTSTORY_API_KEY`. A one-click Claude Desktop bundle (.mcpb) is attached to GitHub releases.
4. Ask for a video in plain language; the server creates the audio clip, starts the generation, waits for the job and returns the video URL.

## Pricing notes

The server is free and open source; videos use CraftStory credits exactly like the app (CraftStory 2.0 from 2.2 credits per second of audio, MiniMax H3 3.3 credits per second). Failed jobs are refunded. Generation takes 8-15 minutes per CraftStory 2.0 video and 1-3 minutes for MiniMax H3.

## Verification (Sep 12, 2026 midday sweep)

npm `@craftstory/mcp` live at v0.1.3, source repo github.com/itseez3d/craftstory-mcp public under MIT (pushed Sep 12, 2026), vendor documentation enumerates all ten tools above. The server is stdio local (no remote endpoint to probe); it talks only to api.craftstory.com over HTTPS.

## See Also

- [Shhots AI MCP - AI UGC Ads and Avatar Videos](/hermes/mcp/servers/external/shhots-ai-mcp/)
- [ReelsFarm MCP - Short-Form Social Content Production](/hermes/mcp/servers/external/reelsfarm-mcp/)
- [ViewMax MCP - AI Video, Image and Speech Generation](/hermes/mcp/servers/external/viewmax-mcp/)
