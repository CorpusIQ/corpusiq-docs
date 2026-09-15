---
title: "Shotstack MCP: Video Editing API for AI Agents"
description: "Official hosted MCP endpoint from Shotstack that gives AI assistants direct access to the video editing API, producing video from conversation instead of hand-written Edit JSON. Tools cover rendering video and images, rendering from saved templates with merge values, template management, render status and Studio editor links at mcp.shotstack.io. API key auth."
category: Content
stars: n/a (new listing)
added: 2026-08-24
source: mcp.so feed listing
relevance: ★★
tags: [video, editing, rendering, templates, remote-mcp, content-production]
---

# Shotstack MCP

**Shotstack's official remote MCP server: produce video from a conversation instead of writing Edit JSON by hand.** The hosted endpoint at `https://mcp.shotstack.io/` gives AI assistants direct access to the Shotstack video editing API, covering rendering video and images, rendering from a saved template with merge values, creating, listing, and deleting templates, checking render status, and opening a Studio editor link for visual edits. Nothing to install or run locally; connect the endpoint and authenticate with a Shotstack API key.

```
Server type: Remote (Streamable HTTP, hosted)
Auth: Shotstack API key (anonymous probe returned HTTP 401, endpoint confirmed live)
Endpoint: https://mcp.shotstack.io/
Repo: Official vendor listing on mcp.so (hosted endpoint, no install)
Tools: Render video and images, template rendering with merge values, template CRUD, render status, Studio editor link
```

## Why This Matters for Operators

Video production for ads, product pages, and social feeds normally means a designer or a templating script, plus a render queue to babysit. Shotstack MCP moves that into the agent conversation: the agent renders the video, polls the status, and hands back the asset URL. For operators running recurring creative (weekly ad variations, listing videos, personalized clips), template rendering with merge values turns one approved template into hundreds of on-brand videos without a designer in the loop.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Render video | Submits video renders from Edit JSON or programmatic edits |
| Render images | Produces image renders for thumbnails and static creative |
| Template rendering | Renders from a saved template with merge values for personalization at scale |
| Template management | Creates, lists, and deletes saved templates |
| Render status | Polls render progress and returns the final asset URL |
| Studio link | Opens a Studio editor link for visual edits of a render |

Capability-level table from the official mcp.so listing; the live tool list is exposed by the endpoint after API-key authentication, which anonymous probes are refused by design.

## Installation

```json
{
  "mcpServers": {
    "shotstack": {
      "type": "http",
      "url": "https://mcp.shotstack.io/"
    }
  }
}
```

For the Claude Code CLI:

```bash
claude mcp add shotstack --transport http https://mcp.shotstack.io/
```

## Configuration

Create a Shotstack account and API key, then pass it to the client when connecting the endpoint. Renders consume Shotstack credits or plan limits, so operators should confirm the plan before letting an agent batch-render variations. Template rendering with merge values is the highest-leverage configuration: save one approved template, then merge per-product or per-audience values at render time.

## Example Prompts

- "Render this week's ad variation set from the approved template for these ten products."
- "Check the status of the render queue and give me the asset URLs that finished."
- "Create a template from this Edit JSON and save it for the product launch series."
- "Open a Studio link so I can tweak the intro before the final render."

## Business Relevance

- **DTC and e-commerce teams** generate per-product video variations from one template
- **Agencies** run recurring creative renders without blocking designers
- **Content teams** produce social clips and thumbnails inside the agent workflow
- **Anyone with a render queue** offloads status polling and asset retrieval to the agent

## Integration with CorpusIQ

Shotstack MCP produces the creative asset; CorpusIQ knows where it should go and whether it worked. An agent can render product video variations with Shotstack, then use CorpusIQ connectors to match each variation to its product's catalog data, sales performance, and campaign attribution, so creative decisions are joined to revenue data instead of guesswork.

## Limitations

- Requires a Shotstack API key and plan; render costs accrue with volume.
- Exact tool names require an authenticated connection; the table above is capability-level from the official listing.
- Video editing is constrained to Shotstack's rendering model, not arbitrary editor operations.
- Hosted-only endpoint; self-hosting is not an option.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [ReelsFarm MCP](/docs/hermes/mcp/servers/external/reelsfarm-mcp) - shortform video generation pipeline
- [UnrealUGC MCP](/docs/hermes/mcp/servers/external/unrealugc-mcp) - UGC-style video content generation
- [ViewMade MCP](/docs/hermes/mcp/servers/external/viewmade-mcp) - video content workflow tools
