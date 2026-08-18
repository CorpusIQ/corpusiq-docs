---
title: "Shhots AI MCP - CorpusIQ Docs - CorpusIQ Docs"
description: Generate AI UGC ads, cinematic product films, and studio-quality product photos from chat. The full Shhots engine over MCP, live on Pro and Scale plans.
category: Content
stars: n/a (new listing)
added: 2026-08-14
source: mcpservers.org
relevance: ★★
tags: [ugc-ads, ai-video, product-photography, ad-creative, video-generation, ecommerce, content, remote-mcp]
---

# Shhots AI MCP

**Remote MCP server (Streamable HTTP, account sign-in)** — the full Shhots ad engine, one prompt away. Generate AI UGC ads with avatars speaking your script, cinematic product films with camera moves and pacing, and studio-quality product photos from a reference image, without leaving the conversation.

```
Server type: Remote (Streamable HTTP)
Auth: Shhots account sign-in
Endpoint: https://mcp.shhots.ai/mcp/
Tools: AI UGC ads, cinematic ads, AI images/photoshoots
Pricing: Pro & Scale plans (commercial)
Category: Content
Built by: Shhots (shhots.ai)
```

## Why This Matters for Operators

UGC-style creative is the best-performing ad format for most ecommerce brands and also the most expensive to produce per variant. Shhots removes the shoot: creator-style video ads with AI avatars speaking your script, in 12 languages and every aspect ratio, ten variants at a time.

**Campaign planning and creative production happen in one chat.** Describe the shot, get the finished cut back in your workspace. Product photography gets the same treatment — new scenes, backdrops, and styles from a single reference image, no camera.

## Tools & Capabilities

| Capability | What it produces |
|---|---|
| AI UGC Ads | Creator-style video ads with AI avatars, 12 languages, all aspect ratios, multi-variant batches |
| Cinematic Ads & AI Videos | Commercial-grade product films with camera moves, lighting, and pacing |
| AI Images & Photoshoots | Studio-quality product photos and lifestyle shoots from one reference image |

Everything available in the Shhots app is available over MCP.

## Installation

```bash
claude mcp add shhots --transport http https://mcp.shhots.ai/mcp/
```

Paste the server URL, sign in with your Shhots account, and ask for your first ad. Live for Claude (web, desktop, Claude Code) and ChatGPT today; more MCP clients coming.

## Configuration

```json
{
  "mcpServers": {
    "shhots": {
      "type": "http",
      "url": "https://mcp.shhots.ai/mcp/"
    }
  }
}
```

Sign-in flow completes in the client; renders land in your Shhots workspace.

## Business Relevance

- **Ecommerce operators** spin up UGC variants for every product without a shoot
- **Performance marketers** test ten ad variants from one prompt
- **DTC brands** refresh product photos per season from existing reference images
- **Agencies** produce client creative from chat instead of coordinating vendors

## Integration with CorpusIQ

Shhots sits upstream of the paid channels CorpusIQ already reads: generate the creative in Shhots, push it to Meta Ads, then read spend, CTR, and ROAS back through the CorpusIQ Meta Ads connector. A composed workflow generates seasonal variants in Shhots, launches them through the ad platform, and closes the loop with first-party performance data from CorpusIQ.

## Limitations

- Requires Shhots Pro or Scale plan
- Live for Claude and ChatGPT only; other clients coming
- Commercial rendering costs
- Brand new — no track record yet

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
