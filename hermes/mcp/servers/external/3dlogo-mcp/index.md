---
title: 3dlogo MCP Server - 3D Logos and Coins from Your AI Assistant
description: Design 3D logos and 3D coins from any MCP client. Public tier lists materials, coin looks, plans and build-studio deep links; OAuth tier creates projects, publishes share pages, and runs AI image-to-3D generation.
category: Content Creation & Creative
stars: n/a (new listing)
added: 2026-08-26
source: "mcp.so GitHub issue #3779"
relevance: ★★★
tags: [3d, logos, design, creative, image-generation, remote-mcp, oauth, brand-assets]
---

# 3dlogo MCP Server

**Remote MCP server (Streamable HTTP)** - 3dlogo.io turns a wordmark or prompt into a production 3D logo or 3D coin: chrome, gold, glass, holographic, neon, clay, wood and more. The anonymous tier gives agents five read-only tools: material and coin-look catalogues, plan comparison, and deep links that open the 3dlogo.io studio preconfigured with text, material, lighting and motion. The authenticated tier (OAuth 2.1 with PKCE and dynamic client registration) adds project creation and management, share-page publishing, invite links, and AI image-to-3D-model generation with status polling. Registered in the official MCP registry as `io.github.cottom/3dlogo`. Endpoint verified live - anonymous initialize answered by the public tier (serverInfo `3dlogo` v1.0.0); the main endpoint returns HTTP 401 for unauthenticated probes, confirming the OAuth gate is active.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 + PKCE (main); none (public tier)
Endpoint: https://3dlogo.io/api/mcp (public: /api/mcp/public)
Tools: 5 public (read-only); project + generation tools behind OAuth
Pricing: Free plan (exports carry a small 3dlogo.io mark); Pro removes it, adds 4K stills and HD MP4
Category: Content Creation & Creative
Built by: 3dlogo.io (registry io.github.cottom/3dlogo)
```

## Why This Matters for Operators

Brand assets are a constant bottleneck. Every launch, campaign or rebrand needs a logo treatment, a coin or badge for a loyalty program, a token graphic, or a 3D wordmark for social headers and video intros. Most operators either pay a designer per asset or settle for flat text.

**3dlogo gives the AI assistant a direct line to a production 3D renderer.** The agent can spec the wordmark, pick the material, set the lighting room and motion, and hand the operator a link that opens the studio already configured. No design tool expertise required. For teams that need repeatable assets, the OAuth tier turns the whole flow into a managed pipeline: create the project, iterate, publish the share page, generate 3D models from photos.

## Tools & Capabilities (public tier)

| Tool | Purpose |
|---|---|
| `list_materials` | Lists materials the 3D logo editor can render (chrome, gold, glass, holographic, neon, clay, wood, stone, 14 categories) with ids for the editor links |
| `list_coin_looks` | Lists preset coin looks (gold, chrome, silver, bronze) and blank edges (reeded, milled, smooth) for the 3D coin studio |
| `build_logo_editor_link` | Returns a link that opens the 3D logo editor with a wordmark already typed and styled (text, material, font, environment, background, motion, depth) - works without an account |
| `build_coin_studio_link` | Returns a link that opens the 3D coin studio with a mark struck into a coin - works without an account |
| `get_plans` | Compares Free and Pro plan details (exports, watermark, credits, saves) and where to upgrade |

Authenticated tier (OAuth) adds: create and manage logo/coin projects, publish share pages, create invite links, and run AI image-to-3D-model generation with status polling. All tools carry titles and read-only/destructive annotations.

## Installation

```bash
# Public tier - no account
claude mcp add 3dlogo --transport http https://3dlogo.io/api/mcp/public

# Full tier - OAuth 2.1 with dynamic client registration
claude mcp add 3dlogo --transport http https://3dlogo.io/api/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "3dlogo": {
      "type": "http",
      "url": "https://3dlogo.io/api/mcp/public"
    }
  }
}
```

For the authenticated tier, follow the client's OAuth flow (RFC 8414/9728 discovery, PKCE, dynamic client registration) against `https://3dlogo.io/api/mcp`.

## Business Relevance

- **Marketing teams** generate on-brand 3D wordmarks for campaigns, webinars and social headers without a design backlog.
- **Product teams** mint coin/badge assets for loyalty programs, token launches, and gamification features.
- **Founders** create pitch-deck logo treatments and product mockups in minutes instead of days.
- **Agencies** hand clients a studio link preconfigured with the client's brand text and material, letting the client iterate in the browser.

## Integration with CorpusIQ

3dlogo pairs cleanly with CorpusIQ's creative workflow: an operator can pull brand guidelines or past campaign performance from CorpusIQ's content and analytics connectors, ask the assistant to generate a 3D logo treatment matched to the winning campaign theme, and track which assets drive engagement through the reporting connectors. The public tier's deep-link model fits the CorpusIQ philosophy of handing the operator a configured workspace rather than a black box.

## Limitations

- Brand new - zero track record, just listed.
- Public tier is read-only by design: no rendering happens inside the MCP session, the tools hand off to the studio web app.
- Free-plan exports carry the 3dlogo.io watermark; Pro is required for clean 4K stills and HD MP4.
- Image-to-3D generation and project management require the OAuth tier.
- Wordmark length caps (40 chars for logos, 24 for coin marks) limit long-form text treatments.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
