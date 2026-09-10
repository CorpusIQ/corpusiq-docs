---
title: Modelglass MCP - Live AI Model Pricing and Routing for Agents
description: Hosted MCP server over live AI model pricing and capability data - ask about model costs, compare providers and get routing recommendations for image, language, video and audio models from inside Claude Code or VS Code.
category: AI Operations
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★
tags: [llm-costs, model-routing, ai-ops, pricing, ai-infrastructure, remote-mcp]
---

# Modelglass MCP

**Live AI model pricing, compared and routed** - connects Claude Code (and VS Code via extension) directly to live pricing and capability data for image generation, language models, video generation and audio. Ask natural questions about model costs, compare providers, and get routing recommendations from inside the session where the decision gets made.

```
Server type: Remote (hosted, Bearer-token HTTP)
Auth: Free Modelglass API key (no credit card, keys do not expire)
Endpoint: https://modelglass-api.vercel.app/mcp
REST: /v1/health, /v1/models (and per-model detail)
Clients: Claude Code (CLI + IDE), VS Code extension. Claude Desktop pending OAuth support
Built by: Modelglass (modelglass.com.au)
```

## Why This Matters for Operators

AI model pricing moves weekly, and routing decisions - flux vs. midjourney-class for product shots, which TTS for the ad voiceover - are made on stale spreadsheets or gut feel. **Modelglass puts the live market inside the agent session**: the assistant that is about to call an image model can first check what it costs, whether a cheaper model covers the same capability, and what the routing recommendation is - then act. Keys are free, instant and persistent, so this is a zero-friction way to stop overpaying on model calls.

## Tools & Capabilities

The MCP surface answers natural-language queries over the pricing and capability data (cost comparisons, provider comparisons, routing recommendations). The underlying REST API is also directly callable:

| Endpoint | Purpose |
|---|---|
| `GET /v1/models` | Live model catalogue with pricing and capabilities |
| `GET /v1/models/{id}` | Per-model detail (e.g. flux-schnell-replicate) |
| `GET /v1/health` | Key and service health check |

## Installation

```bash
claude mcp add --transport http modelglass https://modelglass-api.vercel.app/mcp --header "Authorization: Bearer YOUR_KEY"
```

## Configuration

```json
{
  "mcpServers": {
    "modelglass": {
      "type": "http",
      "url": "https://modelglass-api.vercel.app/mcp",
      "headers": { "Authorization": "Bearer YOUR_KEY" }
    }
  }
}
```

Get the free key at modelglass.com.au/signup. Restart Claude Code after adding, then run `/mcp` to confirm the server is connected. If a key stops working (e.g. after regeneration), update the header and restart.
