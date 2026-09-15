---
title: "Transcodely MCP - Video Transcoding and Hosting for AI Agents"
description: "Hosted Transcodely MCP server for agent-native video infrastructure: transcode gs://, s3:// or https:// sources into renditions, host videos with an adaptive ladder, CDN and player link, generate AI captions, and read job status, playable links and EUR usage. OAuth 2.1 PKCE or app-scoped API key."
category: Content
stars: 0
added: 2026-08-25
source: "mcp.so GitHub issue #3753"
relevance: ★★
tags: [mcp-server, video, transcoding, hosting, captions, media]
---

# Transcodely MCP

**Agent-native video infrastructure.** Transcodely runs a hosted MCP server that turns a natural-language request into a transcode-and-host job and hands back a durable, playable video URL. An agent ingests a public video, Transcodely transcodes it to an adaptive ladder, hosts it on CDN with a player, and returns the link - plus AI-generated WebVTT captions on request. Four of the seven tools are read-only; the three that create work bill at standard Transcodely rates.

```
Server type: Remote Streamable HTTP (hosted)
Endpoint: https://mcp.transcodely.com/mcp
Auth: OAuth 2.1 with PKCE (browser authorization) or app-scoped API key (ak_...) as bearer for headless use
Tools: 7 (create_video_from_url, create_job, generate_captions, get_video, get_job_status, list_jobs, get_usage)
Repo: github.com/transcodely/mcp (MIT, 0 stars)
Pricing: free to connect; 3 creating tools bill at standard rates; 4 read tools are free
```

## Why This Matters for Operators

Video hosting is a three-step chore: transcode, host, distribute. Transcodely compresses it into one agent call with a playable link back - the same workflow operators run through dashboards today (adaptive ladders, CDN delivery, captions), now drivable from any MCP client. The surface is deliberately safe: there is no delete, cancel, or update tool, so an agent cannot destroy existing media. `create_video_from_url` rejects private and internal addresses, and every tool call is written to an audit log with scrubbed arguments.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `create_video_from_url` | Ingest a public https:// video, transcode to an adaptive ladder, host it with CDN and player (billable) |
| `create_job` | Transcode a source from gs://, s3://, or https:// into renditions written to a storage origin you own (billable) |
| `generate_captions` | Transcribe a hosted video into a WebVTT subtitle track, idempotent per video and language (billable) |
| `get_video` | Read a hosted video: status, visibility, duration, poster, every rendition, and the playback block (read-only) |
| `get_job_status` | Compact progress snapshot for one job: status, per-output status, and errors (read-only) |
| `list_jobs` | Recent jobs newest first, optional status filter, cursor paging (read-only) |
| `get_usage` | Encoding minutes, storage, egress, and cost in EUR for a billing month (read-only) |

There is no file-upload tool over MCP; push bytes through the dashboard or upload API instead.

## Installation

Add the endpoint to any MCP client that supports remote HTTP with OAuth:

```shell
claude mcp add --transport http transcodely https://mcp.transcodely.com/mcp
```

On first use the client opens a browser authorization flow; an account is provisioned during authorization if you do not have one.

## Configuration

- **Browser flow (default):** authorize once, no key to create or paste. An authorized connection acts as you within the app it resolved to, and cannot reach admin, billing, team, or key-management surfaces.
- **Headless and CI:** use an app-scoped API key (ak_...) as a bearer token. The MCP server accepts the same keys as the REST API; every call is scoped to that key's app, and a key presented at another app's URL is rejected. Treat a key file like any other secret.
- **Ending access:** remove the connector in the client, remove the member from the organization (re-checked on every call), or revoke the API key for the headless path.

## Business Relevance

- **Content operations:** marketing, product demo, and onboarding videos transcoded and hosted from chat without a media pipeline.
- **E-learning and webinars:** captions generated per video and language, idempotent re-runs.
- **Partner deliverables:** durable player URLs handed to clients, agencies, and sales teams.
- **Cost visibility:** `get_usage` returns monthly encoding, storage, egress, and EUR cost from inside the agent.

## Integration with CorpusIQ

Transcodely's job and usage data pairs with CorpusIQ connectors for the operational side of content work: log hosted video links in Notion or Airtable next to campaign records, reconcile media spend against QuickBooks or Stripe invoices, and track video page performance in GA4 once the player link is embedded.

## Limitations

- Brand-new repo and listing (repo created Aug 25, 2026, 0 stars); vendor history is on the Transcodely product side.
- The three creating tools bill at standard Transcodely rates - read-only tools are free, but work started by an agent costs money.
- No delete, cancel, or update tools; no file upload over MCP.
- Endpoint enumeration is refused without auth (401 on anonymous initialize); the tool list above comes from the vendor's MCP guide and the submission issue.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Shotstack MCP - Video Editing API for AI Agents](/docs/hermes/mcp/servers/external/shotstack-mcp)
- [LiveSend MCP - Share Client-Facing Content with Read Tracking](/docs/hermes/mcp/servers/external/livesend-mcp)
