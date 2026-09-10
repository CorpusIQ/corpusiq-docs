---
title: Capslane MCP - Timestamped YouTube Transcripts for Agents
description: "Hosted MCP server and npm package for the Capslane YouTube transcript API: native captions with millisecond timestamps, automatic generation when captions are missing, job-based status polling, and workspace-based usage limits."
category: Content & Research
stars: 1
added: 2026-09-10
source: mcpservers.org
relevance: ★★
tags: [youtube, transcripts, captions, video-research, content, remote-mcp]
---

# Capslane MCP

**Timestamped YouTube transcripts through an MCP endpoint, npm package or Claude Code plugin** - native caption retrieval with per-segment millisecond offsets, an auto mode that starts audio transcription only when captions are unavailable, and a job model that fits interactive assistants (submit, poll status, stop on content). Endpoint live-verified Sep 10, 2026 (key challenge on anonymous initialize).

```
Server type: Remote (hosted, Streamable HTTP) + stdio npm package
Auth: Capslane workspace API key
Endpoint: https://capslane.com/mcp
npm: @webba_tech/capslane-mcp (MIT)
Tools: 3
Pricing: Workspace allowance - transcript and language calls consume units, status checks do not
Built by: Webba Creative Technologies (capslane.com)
```

## Why This Matters for Operators

Video research (competitor analysis, creator partnerships, customer calls on YouTube) still usually means pasting links into a transcript website and losing the timestamps. **Capslane gives the agent citation-grade transcripts**: segments carry offsets and durations in milliseconds, the source URL and selected language come back with the content, and the tools distinguish cache hits from native captions from generated audio transcripts - so an agent can say where a quote came from instead of paraphrasing a paraphrase. The job model is designed for the agent loop: submit with waitForCompletion false, poll get_transcript_status, stop on content or failed. Cached transcripts return in every mode without a new unit charge, and status checks reserve nothing.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `get_youtube_transcript` | Retrieve a transcript or accept a generation job (mode: native, auto or generate) |
| `get_transcript_status` | Poll a job: pending, content-ready, failed or cancelled; costs no extra unit |
| `list_available_languages` | Languages observed during native transcript requests |

## Installation

```bash
# Remote
claude mcp add capslane https://capslane.com/mcp --env CAPSLANE_API_KEY

# Or stdio via npm (Node 20+)
npx --yes --package @webba_tech/capslane-mcp@0.1.8 capslane-mcp
```

A Claude Code plugin path also exists: add the Webba-Creative-Technologies/capslane-mcp marketplace and install the capslane plugin, which bundles an agent skill with the connection.

## Configuration

```json
{
  "mcpServers": {
    "capslane": {
      "type": "http",
      "url": "https://capslane.com/mcp",
      "headers": { "Authorization": "Bearer ${CAPSLANE_API_KEY}" }
    }
  }
}
```

Create the workspace key at capslane.com/api-keys. Modes: native never starts generation, auto starts it only when captions are unavailable, generate requests audio transcription.
