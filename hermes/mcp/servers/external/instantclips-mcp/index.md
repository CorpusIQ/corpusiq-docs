---
title: InstantClips MCP - E-Commerce Short-Form Video Ads
description: Turn e-commerce products into short-form vertical video ads for TikTok, Instagram Reels and Stories. Import a product from its page URL or photos, draft on-brand creative direction per brand, and render videos through a hosted OAuth MCP endpoint.
category: Marketing
stars: n/a (new listing)
added: 2026-09-08
source: mcp.so
relevance: ★★★
tags: [ecommerce, video-ads, tiktok, instagram-reels, creative-production, social-marketing, remote-mcp]
---

# InstantClips MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1)** - InstantClips turns an e-commerce product into short-form vertical video for TikTok, Instagram Reels and Stories. Import a product from its page URL or photos, generate on-brand video ads, and manage brands and products through 10 tools. No prompt box, no timeline, no style library - built for this one job.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (browser sign-in)
Endpoint: https://app.instantclips.ai/mcp
Tools: 10 (brands, product imports, creative direction, video rendering)
Pricing: Credit-based rendering (only generate_video spends credits)
Category: Marketing
Built by: InstantStudioAI (github.com/InstantStudioAI/instantclips-mcp)
```

## Why This Matters for Operators

Product video ads are the highest-leverage creative format in e-commerce right now, and producing them still means an editor, a brief, and days of turnaround per product. **InstantClips collapses that to a single agent conversation**: paste a storefront URL, the product is scraped, a brand-aware creative direction is drafted, and a render comes back with a share link - in minutes, not days.

The brand-identity system is the mechanism worth noting. Every video is drafted against a brand's voice, target market and keywords, and the server refuses to guess when a product's storefront does not match a known brand - it halts on a brand decision instead of rendering a video in the wrong company's voice. That guardrail is what makes this safe to hand to an agent without a creative director watching every render.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_brands` | List brands on the account with plan limits and identity |
| `import_product_from_url` | Import a product from a storefront URL (Shopify page etc.) |
| `create_product_from_images` | Import a product from hosted product photos |
| `get_product` | Poll import status, video direction, credit cost and renders |
| `create_brand` | Create a brand and attach a product waiting on a brand decision |
| `set_product_brand` | Attach a product to an existing brand (or re-point brand identity) |
| `update_video_direction` | Edit creative direction and render settings for the next video |
| `redraft_video_direction` | Draft a fresh creative direction from product facts and brand identity |
| `generate_video` | Render the video (the only credit-spending tool) |
| `get_video` | Poll render status and get output_url and share_url |

## Installation

```bash
claude mcp add instantclips --transport http https://app.instantclips.ai/mcp
```

Setup snippets for Claude Code, Cursor and VS Code are published on the mcp.so listing.

## Configuration

```json
{
  "mcpServers": {
    "instantclips": {
      "type": "http",
      "url": "https://app.instantclips.ai/mcp"
    }
  }
}
```

Authentication is OAuth: the first time a client connects it opens a browser window to sign in and authorize, then reuses the credentials for future sessions. No API key management on the operator side.

## Business Relevance

- **DTC and Shopify brands** turn their catalog into TikTok and Reels ads without a video editor per SKU
- **Performance marketers** iterate creative direction in conversation and approve renders before credits are spent
- **Agencies** run client product videos through brand slots, with the brand-voice guardrail preventing cross-client mixups
- **Founders** get a first video ad for a new product in minutes instead of waiting on a freelance edit

## Integration with CorpusIQ

InstantClips slots into the e-commerce creative loop that CorpusIQ already reads: the Shopify connector surfaces the product catalog and top sellers, the agent imports those winners into InstantClips by URL, and the render comes back for publishing through the social channel of choice. GA4 closes the loop - campaign lift on the advertised product feeds back into the decision of which SKU to render next. CorpusIQ reads the business, InstantClips produces the creative, and the operator stays in one conversation the whole time.

## Limitations

- Credit-based rendering - every video costs credits, and the agent must confirm cost with the user before each render
- Brand slots are plan-limited; re-pointing a brand identity affects every product sharing it
- Watermark on free accounts until credits are purchased
- Store-domain ownership restriction refuses imports for stores the account does not own
- Remote-only hosted service - no self-host option

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Abyssale MCP - Ad Creative Production for Agents](/hermes/mcp/servers/external/abyssale-mcp/)
- [Treza MCP - AI Video Pipelines to Social Channels](/hermes/mcp/servers/external/treza-mcp/)
