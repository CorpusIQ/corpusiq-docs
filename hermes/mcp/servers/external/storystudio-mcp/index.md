---
title: "StoryStudio MCP - AI Film and Media Studio in Your Agent"
description: "StoryStudio is a remote MCP studio for AI image, video, voice and music generation: write the story, lock a cast, generate shots with Nano Banana 2, GPT-Image 2, FLUX, Veo 3.1 Fast, Seedance 2.5, Kling, MiniMax or Wan, assemble on a timeline and export MP4. OAuth with a free 5-credit plan."
category: Content
stars: n/a (new listing)
added: 2026-09-15
source: "mcp.so feed (Sep 15 midday) + mcp.so detail page + vendor site storystudio.cc"
relevance: ★★
tags: [video-generation, image-generation, voice, music, character-consistency, mp4-export, oauth, remote-mcp]
---

# StoryStudio MCP

**Idea to finished film in one conversation.** StoryStudio is a media generation studio that lives inside the agent: it writes the story, keeps characters consistent across shots with its Cast & World model, routes each shot to the right model (Nano Banana 2, GPT-Image 2 or FLUX 1.1 Pro for images; Veo 3.1 Fast, Seedance 2.5, Kling, MiniMax or Wan for video), then assembles clips on a browser timeline with MP4 export. It connects to Claude, Cursor, Codex and other MCP clients.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in; free plan with 5 credits)
Endpoint: https://storystudio.cc/mcp
Tools: Live tool list served from the endpoint (the listing shows none extracted)
Pricing: free plan with 5 credits; paid plans on storystudio.cc
Category: Content / Media generation
Built by: StoryStudio (storystudio.cc)
```

## Why This Matters for Operators

Video asks sit in every growth plan and stall at the same place: someone has to become a video editor. StoryStudio keeps the whole pipeline in the conversation you are already having. The Cast & World model is the practical unlock: lock a character once and the same face, wardrobe and world persist across shots, so a string of clips becomes an actual scene instead of disconnected generations.

## Capabilities

| Capability | What it covers |
|---|---|
| Image generation | Nano Banana 2, GPT-Image 2, FLUX 1.1 Pro |
| Video generation | Veo 3.1 Fast, Seedance 2.5, Kling, MiniMax, Wan |
| Voice and music | Generated voice and music for the piece |
| Character consistency | Cast & World keeps faces, wardrobe and world across shots |
| Timeline assembly | Browser timeline to edit and arrange shots |
| MP4 export | Finished film exported from the conversation |

The vendor's flow: prompt, image, video, voice and music, montage, MP4. A free plan with 5 credits covers evaluation.

## Installation

```bash
claude mcp add storystudio --transport http https://storystudio.cc/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "storystudio": {
      "type": "http",
      "url": "https://storystudio.cc/mcp"
    }
  }
}
```

Auth is OAuth: the first connection opens a browser to sign in, and the client reuses the credential for future sessions.

## Business Relevance

- **Marketing teams** turn campaign concepts into short films without opening a separate video tool.
- **E-commerce operators** produce product and lifestyle clips from the same session that holds product data.
- **Founders** create launch and explainer clips from a description, iterating in conversation.
- **Agencies** keep character and world consistent across a multi-shot story for a client piece.

## Integration with CorpusIQ

CorpusIQ holds the business context (product catalogs, performance data, customer segments); StoryStudio turns narratives built from that context into media. A composed pattern: use CorpusIQ to pull the product or offer details and angle the story, draft the script in the same session, then generate and assemble the clip through StoryStudio. Both run as MCP servers in one client, so the handoff between data and media is a message, not an export.

## Limitations

- Credits-based: the free plan includes 5 credits; generation volume scales with a paid plan.
- Output quality varies by the underlying model and provider chosen per shot.
- The listing shows no extracted tool list; the endpoint serves it (verified live and auth-gated at sweep time).
- Single-vendor studio: timeline and export live in StoryStudio's browser surface.
- Brand new to this catalog.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
