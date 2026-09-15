---
title: Treza MCP - AI Video Pipelines to Social Channels
description: "Hosted video pipeline platform for agents. Build a pipeline from a brief, run renders on Treza's workers, follow per-node results, and publish finished videos to connected YouTube, TikTok and Instagram channels. Sixteen tools map to producer steps, with schedule triggers, credit estimation before spending, and OAuth sign-in or scoped API keys."
category: Content
stars: n/a (hosted platform)
added: 2026-09-07
source: mcpservers.org
relevance: ★★
tags: [video-production, youtube, tiktok, instagram, content-automation, scheduling, publishing, remote-mcp]
---

# Treza MCP - AI Video Pipelines to Social Channels

**Remote MCP server (Streamable HTTP, OAuth)** - a hosted video pipeline platform from Treza Labs (trezalabs.com) that gives an assistant a full production workflow: build a pipeline from a brief on a node canvas, run it, follow the render, and publish the result to a connected social channel. Every tool maps to a step a producer takes, scoped to the account that signed in.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth browser sign-in on first use, or a scoped API key as a bearer token (pipelines:read, pipelines:run, pipelines:write, keys:provision scopes)
Endpoint: https://www.trezalabs.com/api/mcp
Tools: 16 (authoring, running, budgeting, publishing)
Pricing: Prepaid credits; estimate_run_cost prices a run against the balance before anything renders
Category: Content
Built by: Treza Labs (trezalabs.com)
```

## Why This Matters for Operators

Recurring video content - podcast clips, product announcements, weekly shorts - dies on the calendar because a human has to cut, caption, render and upload every time. Treza turns that into a pipeline an agent can own: the assistant drafts the graph from a template or node vocabulary, fixes validation issues before anything runs, and the published snapshot fires on a schedule without a human touching the canvas.

**Cost and channels are first-class**: `estimate_run_cost` prices one run against the current balance before spending credits, and `list_connected_channels` returns the YouTube, TikTok and Instagram accounts the operator connected once in settings, so a pipeline can end with the video uploaded without the agent ever holding channel credentials. The endpoint is live and OAuth-gated - an unauthenticated probe returns 401 as expected.

## Tools & Capabilities

| Group | Tools |
|---|---|
| Authoring (pipelines:write) | `list_pipeline_templates` (ready-made pipelines, e.g. Podcast Clip Factory), `list_node_types`, `get_node_type` (ports, config schema, live model catalog), `create_pipeline`, `update_pipeline` (error-level issues block the write), `publish_pipeline` (snapshot as immutable deployed version) |
| Running (pipelines:run) | `list_pipelines`, `get_pipeline`, `run_pipeline` (background run, returns a run id at once), `get_run` (per-node results and output URLs; poll until status leaves running), `list_runs`, `set_schedule_paused` (pause or resume without touching the published graph) |
| Budgeting (read-only) | `estimate_run_cost` (what one run will charge and whether the balance covers it), `get_credit_balance` (prepaid balance, plan usage, top-up link) |
| Publishing and access (keys:provision) | `list_connected_channels` (channel ids for upload nodes), `create_api_key` (mint a durable scoped treza_live_ key, shown once) |

## Installation

```bash
claude mcp add --transport http treza https://www.trezalabs.com/api/mcp
```

On first use the client opens a browser window to sign in to Treza and approve the scopes it asked for - no key touches the chat or a config file. A Cursor walkthrough is published at trezalabs.com/blog/how-to-connect-cursor-to-a-video-pipeline-mcp.

## Configuration

```json
{
  "mcpServers": {
    "treza": {
      "url": "https://www.trezalabs.com/api/mcp"
    }
  }
}
```

For headless use, a scoped API key with `pipelines:read` and `pipelines:run` permissions can be sent in the Authorization header; minting one requires the `keys:provision` scope, which only an OAuth consent or first-party session carries.

## Business Relevance

- **Content teams** turn a podcast feed into a weekly captioned vertical short with a schedule trigger and zero manual editing.
- **Social media managers** run the same pipeline across YouTube, TikTok and Instagram channels from one connected account.
- **Marketing operations** get credit estimation before every render, so agent-driven video never silently drains a balance.
- **Agencies** mint scoped keys per client pipeline and let headless systems drive production without sharing channel logins.

## Integration with CorpusIQ

Treza extends CorpusIQ's content automation stack: the CorpusIQ agent writes the weekly video brief, calls `create_pipeline` from a template, points the upload node at the connected YouTube channel, and lets `run_pipeline` plus `get_run` handle render and delivery while the agent reports the finished URL back into the campaign record. The schedule trigger replaces a cron for recurring content, and `estimate_run_cost` feeds CorpusIQ's budget tracking so video spend is visible alongside ad spend in the operator's monthly report. Channel connections stay with the operator's Treza account - CorpusIQ never sees social credentials.

## Limitations

- Hosted platform with prepaid credits; no self-host build.
- OAuth sign-in requires a browser flow on first connection.
- Video output quality depends on the models wired into the node canvas.
- The raw key shown by `create_api_key` appears once; store it immediately.
- Brand new listing in this catalog (listed Sep 2026 on mcpservers.org).

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
