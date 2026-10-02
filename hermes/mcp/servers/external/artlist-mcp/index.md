---
title: Artlist MCP - AI Creative Suite for Agents
description: Official Artlist MCP server that gives AI agents image, video, music and voice-over generation from the Artlist AI creative suite, over OAuth at mcp.artlist.io - no local install, works with Claude, ChatGPT and VS Code.
category: Content
stars: n/a (new listing)
added: 2026-09-09
source: mcp.so
relevance: ★★★
tags: [image-generation, video-generation, music-generation, voice-over, creative, media-production, content-creation, remote-mcp]
---

# Artlist MCP

**Remote MCP server (Streamable HTTP, OAuth)** - the official Artlist connector that hands an AI agent the full Artlist AI creative suite: generate images, videos, original music and voice-overs straight from the conversation. Listed by Artlist itself, verified and featured on mcp.so.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (Artlist account)
Endpoint: https://mcp.artlist.io/mcp
Tools: 4 (image generation, video generation, music generation, voice-over)
Pricing: Artlist account required (subscription details on artlist.io)
Category: Content
Built by: Artlist (artlist.io)
```

## Why This Matters for Operators

Content production is the operator's biggest creative bottleneck - every campaign, launch video and ad needs assets, and each asset currently means another human in the loop or another tool tab. **Artlist MCP puts the entire Artlist AI creative suite inside the agent's toolbelt**, so a brief turns into generated images, video, music and voice-over without leaving the conversation.

Because this is the official Artlist build, the same account and licensing umbrella that covers Artlist's stock libraries backs the generated output - an operator can brief creative in chat and know the results sit on commercial-grade rails rather than a consumer generator's gray area.

## Tools & Capabilities

The mcp.so listing shows no extracted tool list; the four capabilities below are the published tool set from the vendor's overview and the live tool list is served from the endpoint.

| Tool | Purpose |
|---|---|
| `Image generation` | Generate images from a prompt or reference image |
| `Video generation` | Generate videos from a prompt or reference |
| `Music generation` | Generate original music tracks |
| `Voice-over` | Generate voice-overs from a script |

## Installation

```bash
claude mcp add artlist --transport http https://mcp.artlist.io/mcp
```

Supported clients today: Claude (claude.ai), ChatGPT/OpenAI and VS Code. Cursor, Codex and other clients are not yet supported - more platforms coming soon.

## Configuration

```json
{
  "mcpServers": {
    "artlist": {
      "type": "http",
      "url": "https://mcp.artlist.io/mcp"
    }
  }
}
```

Auth is OAuth: on first connect the MCP client opens a browser window to sign in to your Artlist account and authorize the server, then reuses the credentials for later sessions.

## Business Relevance

- **Marketing teams** get campaign-ready images, ad video, music and voice-over briefed in plain English from the agent
- **Content operators** run one connected tool for the whole creative stack instead of four separate generators
- **Agencies** brief multiple asset variants per campaign without opening a design tool
- **Founders** ship launch creative from chat on day one, with licensed output under the Artlist account

## Integration with CorpusIQ

Artlist MCP is a pure creative-production complement to CorpusIQ's business-data core: an agent answering "what did we sell last month" from CorpusIQ's Stripe and Shopify connectors can flow straight into "now generate the video ad for the best seller" through Artlist. It pairs naturally with the catalogued social-publishing servers (PostNitro, Chirpie, Treza) - Artlist generates the assets, the publisher pushes them to channels - while CorpusIQ reads back the business result and closes the loop from spend to asset to revenue.

## Limitations

- Brand new MCP listing - no track record yet
- Requires an Artlist account; subscription costs live on the Artlist side
- Four generation tools only - editing and campaign features remain in the Artlist apps
- Client support is currently Claude, ChatGPT and VS Code; Cursor and Codex not yet
- No extracted live tool list on the directory listing; tools documented from vendor overview

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
