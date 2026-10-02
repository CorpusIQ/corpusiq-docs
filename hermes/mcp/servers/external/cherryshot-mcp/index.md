---
title: CherryShot MCP - Product Photography and Video Ads
description: "Remote MCP server for Cherry Shot: generate campaign-grade product imagery from one photo - on-model shots, lifestyle scenes, marketplace images - and turn them into short video ads, from any MCP client. Six tools over a Bearer API key: credits, models, create and poll a shoot, create and poll a video. Same account, credits and rate limits as the Cherry Shot REST API."
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-09-14
source: "mcpservers.org /all page 1 (Sep 14 evening crawl) + vendor docs at cherryshot.mintlify.app/guides/mcp"
relevance: ★★
tags: [ecommerce, product-photography, video-ads, creative, image-generation, ad-creative, marketplace, remote-mcp, api-key]
---

# CherryShot MCP

**Product shoots and video ads, generated from chat.** Cherry Shot ships a remote MCP server so any compatible client (Claude Desktop, claude.ai, Claude Code, Cursor) can generate product photography and video ads directly: one photo in, on-model shots, lifestyle scenes and marketplace-ready images out, then a short video ad built from the images that worked.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer API key (Cherry Shot account)
Endpoint: https://kyliwpyuseadbwawnsyd.supabase.co/functions/v1/mcp (401-verified live, Sep 14 2026)
Tools: 6
Pricing: Credit-based; same balance and rate limits as the Cherry Shot REST API
Category: Commerce & E-Commerce / Creative
```

## Why This Matters for Operators

Product photography is one of the last manual bottlenecks in an ecommerce launch. A new SKU needs a hero image, a lifestyle scene, marketplace crops and something motion-shaped for paid social, and the shoot calendar decides the launch date. This server turns the sequence into a conversation:

> **You:** Generate an editorial 4-shot set for this product: `https://example.com/bottle.jpg`
>
> **Assistant:** _(calls create_shoot, polls get_shoot until the images are ready, returns the four image URLs inline)_
>
> **You:** Great - make a 10-second 720p video ad from the first two images.
>
> **Assistant:** _(calls create_video, polls get_video until rendering completes, returns the MP4 link)_

Styles can be iterated in the same thread, and custom models are available alongside presets for with-model shoots.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `get_credits` | Current credit balance |
| `list_models` | Preset and custom models for with-model shoots |
| `create_shoot` | Start a product-photography shoot; returns a shoot ID |
| `get_shoot` | Poll shoot status; returns image URLs when complete |
| `create_video` | Start a video ad from one or more shoot images |
| `get_video` | Poll video status; returns the MP4 URL when rendered |

The MCP server is a thin, fully-supported layer over the Cherry Shot REST API: same API key, same credit balance, same rate limits. Credits spent through MCP appear in the dashboard exactly as REST usage would.

## Installation

**Claude Desktop / claude.ai** - Settings, Connectors, Add custom connector, paste the MCP URL, and add the Cherry Shot API key as a bearer token.

**Claude Code:**

```bash
claude mcp add --transport http cherry-shot \
  https://kyliwpyuseadbwawnsyd.supabase.co/functions/v1/mcp \
  --header "Authorization: Bearer cs_your_key"
```

## Configuration

```json
{
  "mcpServers": {
    "cherry-shot": {
      "type": "http",
      "url": "https://kyliwpyuseadbwawnsyd.supabase.co/functions/v1/mcp",
      "headers": { "Authorization": "Bearer cs_your_key" }
    }
  }
}
```

## Business Relevance

- **Ecommerce operators** produce listing and marketplace imagery without booking a studio for every SKU.
- **Performance marketers** turn winning product photos into short video ads for paid social in the same session.
- **Agencies** run client product shoots as a repeatable prompt workflow, with all spend in one credit balance.
- **Founders** get launch-grade creative before the product page goes live, on the timeline the launch needs.

## Integration with CorpusIQ

Cherry Shot produces the creative; CorpusIQ tells you what to shoot and whether it worked. With a CorpusIQ connection the same assistant reads Shopify orders, Stripe revenue, GA4 sessions and ad-platform data with source-cited answers, so a creative request starts from the numbers ("the top seller needs a new hero shot") and ends with a check ("did sessions and conversion move after the new images"). Both flows are account-scoped and read-oriented until you explicitly spend: CorpusIQ reads business data, Cherry Shot spends credits only when a shoot or video is created.

## Limitations

- **Bring your own key**: credits are charged through your Cherry Shot account; there is no free tier documented on the listing.
- **Asynchronous by design**: shoots and videos are started and polled (create/get pairs), not returned inline.
- **API-key auth only** on this endpoint (no OAuth flow documented).
- **The endpoint is hosted on a Supabase edge function URL**, which is less brand-legible than a dedicated domain; verify it against the vendor's own documentation before connecting.
- **New listing** with no third-party track record at catalog time.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CraftStory MCP - Talking-Avatar and UGC Video Generation for Agents](/hermes/mcp/servers/external/craftstory-mcp)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
