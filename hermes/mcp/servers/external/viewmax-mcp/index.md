---
title: "ViewMax MCP - CorpusIQ Docs"
description: AI video, image, music and speech generation over MCP — Sora-class video models with OAuth or API-key auth and credit-based billing.
category: Content
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★
tags: [video-generation, image-generation, music-generation, sora, creative-production, marketing-content, credits, remote-mcp]
---

# ViewMax MCP

**Remote MCP server (Streamable HTTP, OAuth or API key)** — ViewMax brings AI video, image, music, and speech generation into any MCP client: `generate_video` with Sora-class models, text-to-image and image-to-image, music tracks, and speech — with model discovery via `list_video_models` and friends. Billing is credit-based; generation consumes credits.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (Claude Web/Desktop) or API key (Authorization: Bearer, for CLI and Codex)
Endpoint: https://viewmax.studio/api/mcp
Tools: generate_video, generate_image, generate_music, generate_speech + list/get model tools
Pricing: credit-based (credits consumed per generation)
Category: Content
Built by: ViewMax Studio (viewmax.studio)
```

## Why This Matters for Operators

Video production is the most expensive content type to outsource and the most effective to publish. ViewMax moves generation into the agent loop: the same conversation that writes the brief can call `generate_video` and get back a task with status and video URLs.

**The model-discovery pattern is the practical win**: instead of hard-coding a model name, the agent lists available video models, checks one with `get_video_model`, then generates — so model availability and deprecations are handled by the server, not by your workflow. Marketing teams get an 8-second vertical clip the way they currently get a draft headline: on demand, in chat.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| generate_video | Video generation task; model options via list_video_models / get_video_model |
| generate_image | Text-to-image or image-to-image; model list via list_image_models |
| generate_music | Original music tracks from a prompt; model list via list_music_models |
| generate_speech | Speech synthesis |
| get_task | Task status and output URLs (video_urls on success) |

## Installation

```bash
claude mcp add --transport http viewmax https://viewmax.studio/api/mcp --header "Authorization: Bearer YOUR_API_KEY"
```

In claude.ai or Claude Desktop, add the connector URL and sign in with a ViewMax account — OAuth, no API key needed. API keys are created in Settings → API Keys.

## Configuration

```json
{
  "mcpServers": {
    "viewmax": {
      "type": "http",
      "url": "https://viewmax.studio/api/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

## Business Relevance

- **Marketing teams** get video and image creative from the same chat that writes the campaign copy.
- **Content operators** get short vertical clips without a production queue or an editor.
- **Product teams** get image-to-image iteration for mockups and launch assets.
- **Music-poor video workflows** get a generated soundtrack instead of stock-library hunting.

## Integration with CorpusIQ

ViewMax slots into the CorpusIQ content pipeline as the generation layer. Creative produced through ViewMax feeds the social cadence engine, publishing via Postiz and measured by the YouTube and TikTok connectors, closing the loop from generation to performance. It complements ReelsFarm's short-form production: ViewMax for raw model generation, ReelsFarm for avatars, staging, and approval-gated scheduling. The credit-based billing keeps content spend visible per asset, matching the cost-attribution discipline CorpusIQ operators already apply to ad budgets.

## Limitations

- Brand new — no track record yet; listing appeared August 17, 2026.
- Credit-based billing — generation costs per asset, and credits are the account currency.
- Model availability is served at runtime; a named model in a workflow today may rotate tomorrow.
- Consumer-grade creative focus — no brand-kit, template, or approval-gate tooling beyond generation.
- OAuth for Claude, API key for everything else — key management is manual.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
