---
title: "VoIPstudio MCP - Call Analytics and QA for Agents"
description: "Official VoIPstudio MCP server that lets AI agents query call recordings, CDRs, live calls and voicemails, with per-user API tokens and optional CX scoring."
category: Communication
stars: n/a (new listing)
added: 2026-09-11
source: mcpservers.org scan (docs maintenance backfill)
relevance: ★★
tags: [voice, telephony, call-analytics, qa, call-center, remote-mcp, sse]
---

# VoIPstudio MCP

**Remote MCP server (SSE)** - the official VoIPstudio MCP server gives AI assistants secure access to a VoIPstudio account: call recordings, call detail records (CDRs), live calls and voicemails. Connected through an API token, an agent can query calls, analyze patterns, surface agent performance issues and generate QA reports in plain English, with no custom development.

```
Server type: Remote (SSE)
Auth: VoIPstudio API token (user_token, scoped per user, sent as Bearer)
Endpoint: https://mcp.voipstudio.workers.dev/sse
Built by: VoIPstudio (official)
Category: Communication
```

## What it does

| Tool | What it returns |
|---|---|
| `get_recordings` | Call recordings with call metadata (caller, agent, duration, direction, context). With the CX Addon active, each record also carries the transcript, speaker-diarized segments, summary, sentiment, CX score and a timeline |
| `get_cdrs` | Call detail records, the raw log of every call leg: timestamps, disposition (CONNECTED, NO ANSWER, BUSY, FAILED), billable seconds, charge and labels. Use for volume stats, cost analysis and agent activity summaries |
| `get_live_calls` | Real-time snapshot of all active calls on the account |
| `get_voicemails` | Voicemail messages, filterable by source, destination, call date, duration and listened status |
| `get_recording_audio` | Time-limited MP3 download URL for a specific recording ID |

All list tools accept a `filters` array (`property`, `operator`, `value`, with operators `eq`, `ne`, `lt`, `lte`, `gt`, `gte`, `in`, `like`, `notlike`), plus `limit` (default 10, max 1000) and `page`. A prompt like "show me recordings from this week where the CX score was below 6, grouped by agent" becomes a filtered `get_recordings` call.

## Getting an API key

1. In the VoIPstudio admin dashboard, open the user the token should belong to.
2. Open **API Keys**, name the key (for example, `Agent MCP`) and click **Add**.
3. Reveal and copy the key (`user_token`). The key inherits that user's access, so scope follows who you pick.
4. Keys expire after 7 days without use by default; choose a longer timeout or unlimited before creating the key if the integration is intermittent.

## Connecting

The server is not in the Claude connector directory; add it as a custom MCP server.

```json
{
  "mcpServers": {
    "voipstudio": {
      "url": "https://mcp.voipstudio.workers.dev/sse",
      "transport": "sse",
      "headers": {
        "Authorization": "Bearer YOUR_VOIPSTUDIO_API_KEY"
      }
    }
  }
}
```

The Anthropic API accepts the same server per request via `mcp_servers` with `type: "url"`, the endpoint above and `authorization_token` set to the VoIPstudio key. Other platforms that support external MCPs use the same URL and key; look for an option labelled external MCP, custom MCP or remote MCP in their integrations.

## CX Addon

Without the CX Addon, recordings arrive as raw metadata and the model must transcribe and analyze each call itself. With it, VoIPstudio handles transcription, summarisation, sentiment, action extraction and CX scoring on its own infrastructure. The vendor prices it as a fixed monthly cost with no per-call fees, and documents roughly 10,000-15,000 tokens per call for model-side processing of raw audio against 300-500 tokens per call with the addon's finished intelligence.

Fields unlocked by the addon: `transcript`, `transcript_speakers`, `summary`, `sentiment`, `cx_score` (1-10) and `metadata.timeline` (key moments and action items).

## Verification (Sep 11, 2026 docs maintenance)

Endpoint `https://mcp.voipstudio.workers.dev/sse` live-probed: anonymous GET returned HTTP 401 with `WWW-Authenticate: Bearer realm="OAuth"` and body `{"error":"invalid_token","error_description":"Missing or invalid access token"}` - live and auth-gated exactly as documented.

## See Also

- [DialNexa MCP - Voice AI Agents and Confirmed Outbound Calls](/hermes/mcp/servers/external/dialnexa-mcp)
- [VoIP.ms MCP - Business Telephony for AI Agents](/hermes/mcp/servers/external/voipms-mcp)
- [Canarics MCP - AI Call Analysis and Voice Agents for Sales Teams](/hermes/mcp/servers/external/canarics-mcp)
