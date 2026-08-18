---
title: "UnrealUGC MCP - CorpusIQ Docs - CorpusIQ Docs"
description: "Create and manage AI UGC video ads through eleven typed MCP tools - browse video models, creators and voices, estimate credit cost before spending, and generate asynchronously"
category: Marketing
stars: "n/a (new listing)"
added: 2026-08-18
source: "mcp.so GitHub issue #3623"
relevance: ★★
tags: [ugc, video-ads, ai-video, creators, voices, marketing, async-generation, remote-mcp, video-generation]
---

# UnrealUGC MCP

**Create and manage AI UGC video ads through eleven typed MCP tools: browse available video models, creators and voices, estimate credit cost before spending, start asynchronous generations and poll for completed output.** Ships as local stdio (`npx -y @unrealugc/mcp`) and hosted Streamable HTTP (`unrealugc.com/api/mcp`), MIT-licensed, with the same API key for both transports.

```
Server type: stdio via npm or hosted Streamable HTTP
Auth: UNREALUGC_API_KEY (usk_live_...)
Install: npx -y @unrealugc/mcp
Remote endpoint: https://unrealugc.com/api/mcp
Tools: 11 (models, creators, voices, projects, videos, credits, generation)
License: MIT
Category: Marketing / AI video ads
Built by: UnrealUGC (unrealugc.com) — registry com.unrealugc/mcp
```

## Why This Matters for Operators

UGC-style ads convert, but shooting them is the bottleneck: finding creators, briefing, filming, editing, iterating. UnrealUGC moves the whole loop into an agent: pick a creator persona, pick a voice, estimate what the generation costs in credits before spending anything, then generate asynchronously and poll for the finished video. Eleven tools cover the entire workflow, so the agent can run "make three ad variations across three creators and tell me which performs best" as one job instead of a production calendar.

**Cost-before-spend is the operator-friendly detail.** `estimate_video_cost` prices a generation before it starts, and `get_credits` answers "how many 15-second videos can I make this month" — credit discipline built into the tool surface rather than discovered on the invoice.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `get_me` / `get_credits` | Account info and credit balance |
| `list_models` | Available video models (includes Seedance 2.0 and Kling-class models) |
| `list_creators` | Stock and custom creator personas |
| `list_voices` | Stock and custom voices |
| `list_projects` / `create_project` | Project organization |
| `list_videos` / `get_video` | Prior generations and status |
| `estimate_video_cost` | Credit estimate before generating |
| `generate_video` | Start an asynchronous generation |

Tools self-describe via `tools/list` with full JSON Schema inputs.

## Installation

Stdio (Claude Code):

```bash
claude mcp add unrealugc \
  --env UNREALUGC_API_KEY=usk_live_... \
  -- npx -y @unrealugc/mcp
```

Generic JSON config:

```json
{
  "mcpServers": {
    "unrealugc": {
      "command": "npx",
      "args": ["-y", "@unrealugc/mcp"],
      "env": {
        "UNREALUGC_API_KEY": "usk_live_..."
      }
    }
  }
}
```

Hosted HTTP for remote MCP clients: register `https://unrealugc.com/api/mcp` and pass the same API key as a Bearer token.

## Configuration

| Variable | Required | Default | Description |
|---|---|---|---|
| `UNREALUGC_API_KEY` | yes | — | API key from unrealugc.com/dashboard/settings/api-keys |
| `UNREALUGC_BASE_URL` | no | `https://unrealugc.com` | Override for self-hosting |

## Business Relevance

- **DTC brands** produce UGC-style ad variants without a creator shoot per variation
- **Growth operators** A/B test creator personas and scripts at credit cost instead of agency day rates
- **Agencies** run client ad production as agent jobs with per-job cost estimates up front
- **Lean teams** cover "we need video ads" with one API key instead of a production pipeline

## Integration with CorpusIQ

CorpusIQ's 40+ connectors measure what ads earn — spend, revenue, conversions across Google, Meta and storefronts. UnrealUGC produces the creative that enters those funnels. The composed loop: UnrealUGC generates and polls ad variants from an agent, the agent publishes them through the existing social stack, and CorpusIQ's ad and analytics connectors attribute results — creative production and performance measurement in one session, no spreadsheet handoff between tools.

## Limitations

- New listing (repo and service launched Aug 18, 2026); no public pricing beyond credit-based billing
- Asynchronous generation means polling — long videos need the agent to check back rather than blocking
- Creator and voice libraries are stock-first; custom creators may be a higher plan tier
- Eleven tools cover the core loop, but no editing or caption tooling — post-production stays outside the MCP surface
