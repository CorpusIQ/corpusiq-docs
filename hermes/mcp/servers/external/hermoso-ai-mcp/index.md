---
title: Hermoso AI MCP
description: AI ad studio over MCP. Research the ads winning in your market, generate finished on-brand image and video ads with 50+ models, publish them, and run campaigns across ten ad platforms.
category: Content
stars: n/a (new listing)
added: 2026-08-14
source: mcpservers.org
relevance: ★★★
tags: [ad-creative, video-generation, image-generation, ad-research, campaign-management, marketing-automation, content, remote-mcp]
---

# Hermoso AI MCP

**Remote MCP server (Streamable HTTP, OAuth)** — Hermoso ships an open-source MCP server, a CLI, and installable Claude skills so the assistant you already use can run your whole ad function: research the ads winning in your market, create finished image and video ads, publish them, and read the paid campaigns behind them. 415 tools over one OAuth'd endpoint.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth
Endpoint: Single Hermoso endpoint (documented at hermoso.ai)
Tools: 415 (research, creative, post-production, publishing, campaigns)
Pricing: Credit-metered; exact per-render costs published before spend
Category: Content
Built by: Hermoso (hermoso.ai)
```

## Why This Matters for Operators

Most marketing MCP servers stop at scheduling — they move creative between tools but never make it. Hermoso generates the creative itself: one connector is a one-stop shop for 50+ image and video models — Seedance, Veo, Kling, Sora and Gemini Omni for video; Nano Banana, Imagen, Flux, Seedream and GPT Image for stills; plus premium voices and writing models — on a single credit meter with no per-vendor API keys to hold.

**The full ad workflow in one connector: competitor research across the Meta, Google and LinkedIn ad libraries, creative planning, finished branded renders, post-production, scoring, publishing, and campaign management.** Exact per-render credit costs are published before anything spends.

## Tools & Capabilities

The 415-tool surface clusters into the ad workflow:

| Area | What the assistant can do |
|---|---|
| Ad research | Winning ads from Meta, Google, LinkedIn ad libraries |
| Creative planning | Briefs and concept generation |
| Image generation | On-brand stills with real product composited in |
| Video generation | Finished video ads across 50+ models |
| Post-production | Editing, scoring, variant generation |
| Publishing | Push creative to ad platforms |
| Campaign management | Build and read paid campaigns |

## Installation

```bash
claude mcp add hermoso --transport http <hermoso-endpoint>
```

Hermoso publishes MCP installs, a CLI, and Claude skills. Works with Claude, ChatGPT, Claude Code, Cursor, Codex, OpenClaw, and Hermes clients.

## Configuration

```json
{
  "mcpServers": {
    "hermoso": {
      "type": "http",
      "url": "<hermoso-endpoint>"
    }
  }
}
```

Single OAuth flow on first connect; one credit meter across all underlying models.

## Business Relevance

- **Performance marketers** research, generate, and iterate ad creative in one chat
- **Ecommerce operators** produce on-brand product video without an agency
- **Agencies** run multiple client ad functions from one connector
- **Solopreneurs** get 50+ creative models without holding vendor accounts

## Integration with CorpusIQ

Hermoso's campaign-management tools complement CorpusIQ's Meta Ads and Google Ads connectors: CorpusIQ reads first-party performance and spend, while Hermoso generates the creative and pushes variants live. A composed workflow pulls losing creative from Meta Ads, asks Hermoso to generate replacements from the winning library patterns, and re-reads performance through CorpusIQ. CorpusIQ's read-only analytics close the loop the creative pipeline opens.

## Limitations

- Commercial credit system — renders are metered (though priced before spend)
- 415-tool surface is large; expect a learning curve
- OAuth endpoint means account-scoped usage
- Brand new — no track record yet

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
