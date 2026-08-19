---
title: "WaveSpeed MCP - Media Generation for AI Agents"
description: "Official WaveSpeed AI MCP server runs any image, video, audio or 3D model from the live platform catalog with schema introspection, local file upload, honest price quotes before spending, and account balance checks from any MCP client"
category: Media Generation
stars: 30
added: 2026-08-19
source: "mcp.so GitHub issue #3647"
relevance: ★★
tags: [media-generation, image, video, audio, 3d, ai-models, stdio, npm, content-creation]
---

# WaveSpeed MCP

**Run any image, video, audio, or 3D model on the live WaveSpeed catalog from any MCP client.** The official vendor server ships no hardcoded model list — the catalog comes from the live API, so new platform models work the day they ship. Every generation goes through the same `run_model` verb, with `get_model_schema` for real input schemas, `get_price` for quotes before spending, and `get_prediction` for async results.

```
Server type: Local (npm, stdio) with Dockerfile
Auth: WAVESPEED_API_KEY (or wavespeed login)
Package: npx -y @wavespeed/mcp (MIT)
Tools: 7
Registry: ai.wavespeed/mcp
Pricing: Pay-as-you-go credits (wavespeed.ai/accesskey)
Category: Media Generation
Built by: WaveSpeed AI (official)
```

## Why This Matters for Operators

Marketing operators constantly need hero images, product renders, video clips, and audio assets, and every generation model has different inputs, costs, and quality tradeoffs. WaveSpeed MCP gives an agent one interface to the whole catalog: the agent can list models, read a model's real input schema before calling it, quote the price before spending, and check account balance — the same pre-spend discipline operators apply to ad budgets, applied to media spend.

The honesty mechanics matter for automation: `get_price` explicitly names the inputs the quote was blind to (`unpriced_inputs`) instead of presenting a formula floor as the real price, and local-file upload uses an explicit `@path` marker so inputs are never silently mutated.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `list_models` | Search the live catalog by text or modality |
| `get_model_schema` | A model's real input schema — required fields, properties, defaults |
| `run_model` | Submit and wait; `@path` inputs upload automatically; returns output URLs |
| `get_price` | Cost estimate with `unpriced_inputs` / `at_base_price` disclosure |
| `get_balance` | Account credit balance |
| `upload_file` | Local file to hosted URL (24h content-hash dedupe) |
| `get_prediction` | Recover status and outputs of any run by id |

Long-running jobs keep running server-side past the wait limit — the error names the prediction id, and `get_prediction` picks it up.

## Installation

```bash
claude mcp add wavespeed -- npx -y @wavespeed/mcp
```

Claude Desktop / other clients:

```json
{
  "mcpServers": {
    "wavespeed": {
      "command": "npx",
      "args": ["-y", "@wavespeed/mcp"],
      "env": { "WAVESPEED_API_KEY": "wsk_..." }
    }
  }
}
```

## Configuration

Auth resolves from `WAVESPEED_API_KEY`, or from the CLI's stored login (`wavespeed login`) — one login covers both tools. Keys are created at wavespeed.ai/accesskey. Repository: `github.com/WaveSpeedAI/mcp-server` (MIT). Listed on Glama with Quality A.

## Business Relevance

- **Marketing operators** generate campaign assets — hero images, product shots, short video clips — directly in the agent session
- **Content teams** produce image/video/audio variants across models without leaving the assistant
- **E-commerce operators** create product visuals and social creatives at scale from one catalog
- **Automation builders** fold media generation into workflows with pre-spend price quotes and balance checks

## Integration with CorpusIQ

WaveSpeed is the creative output layer; CorpusIQ is the business-data layer. A marketing operator can pull campaign performance from CorpusIQ (GA4, ad platforms, CRM), decide which creative to produce next, and generate it through WaveSpeed — then attribute the resulting content's performance back through the same CorpusIQ connectors. The price-quote-before-spend pattern in WaveSpeed's tools mirrors the spend visibility CorpusIQ gives across ad and email platforms.

## Limitations

- Media generation costs accrue per run; agents need a credit balance to execute
- `get_price` quotes are estimates — `unpriced_inputs` names what the quote could not see
- Output URLs are hosted by WaveSpeed; long-term storage is not guaranteed
- Requires an account and API key; no anonymous free tier documented

## See Also

- [UnrealUGC MCP — AI UGC Video Ad Generation](/hermes/mcp/servers/external/unrealugc-mcp/)
- [MCPGRAM MCP — OAuth Connectivity Gateway](/hermes/mcp/servers/external/mcpgram-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
