---
title: "Tactiq MCP - Meeting Transcript Intelligence for Agents"
description: "Hosted meeting intelligence from Tactiq: agents search, read and summarise meeting transcripts and AI summaries from Google Meet, Zoom and Microsoft Teams across your whole meeting history. Endpoint mcp.tactiq.io with Tactiq account sign-in; verified Claude connector; free plan with paid tiers for full transcript access."
category: Productivity
stars: "n/a (hosted, no public repo)"
added: 2026-08-30
source: "mcp.so feed (listed Aug 15, 2026; first evaluated Aug 30)"
relevance: ★★★
tags: [mcp-server, meetings, transcripts, meeting-notes, google-meet, zoom, teams, oauth]
---

# Tactiq MCP

**Your meeting history, answerable from any MCP client.** Tactiq automatically captures transcripts from Google Meet, Zoom and Microsoft Teams, and its MCP server gives Claude, Cursor and other agents direct access to search, read and summarise those transcripts and AI Companion summaries. Ask what was decided, who you spoke with, or what has come up across any call - without leaving the chat.

```
Server type: Hosted (Streamable HTTP)
Endpoint: https://mcp.tactiq.io
Auth: Tactiq account sign-in (OAuth connector flow; anonymous initialize returns 401 missing_token)
Capture: Google Meet, Zoom, Microsoft Teams (automatic transcripts + AI Companion summaries)
Distribution: verified connector in Claude's directory (two-click connect); works with Cursor, ChatGPT, Gemini and any MCP client
Pricing: Free plan; paid plans lift the plan gate on reading summary content (tactiq.io/pricing)
Built by: Tactiq (tactiq.io)
```

## Why This Matters for Operators

Meeting notes die in tools nobody reopens. Tactiq's MCP turns the meeting record into live agent context in three ways.

First, **cross-meeting recall.** The MCP surface answers questions across the entire meeting history - "what did the customer decide about pricing last month" or "who was in the Q3 planning call" - which is exactly the institutional memory operators lose when notes live in silos.

Second, **zero-friction distribution.** Tactiq is a verified connector in Claude's directory, so the connect flow is two clicks with no server URL to paste; other clients use the endpoint directly with Tactiq sign-in.

Third, **capture is automatic.** Transcripts and AI summaries are produced during the call, so the agent works from the same record every participant can see, not a personal notes file.

## Tools and Capabilities

Capability-level table from the vendor's MCP documentation; exact tool names require sign-in - anonymous enumeration is refused (the endpoint returns 401 missing_token for unauthenticated initialize calls, which confirms liveness).

| Capability | Description |
|-----------|-------------|
| Meeting search | Find meetings by participant, date, title or keyword across the full history |
| Transcript read | Read full transcripts and AI Companion summaries from Google Meet, Zoom and Teams |
| Cross-meeting Q&A | Ask what was decided, who you spoke with, or what came up across any call |
| Recording and summary access | Surface recordings and summaries inside the client |

**Plan gating note:** on the free and Pro Tactiq plans, Claude can find your meetings but cannot read the summary content - the meeting-content read access is unlocked on higher plans (per Tactiq's help center).

## Verification (Aug 30, 2026)

- Endpoint live-verified: anonymous initialize at mcp.tactiq.io returns HTTP 401 with "missing_token" - proof of liveness with sign-in auth (same class as the Taskfolk and Jitsu verifications)
- Vendor documentation: tactiq.io/mcp (product page), tactiq.io/learn/how-to-connect-meeting-notes-to-claude-mcp (setup guide), help.tactiq.io (plan-gating article)
- mcp.so listing websiteUrl points at mcp.tactiq.io

## Notes and Caveats

- Sign-in required: no API-key paste path - the connector flow authenticates your Tactiq account
- Plan gating: transcript summary reads are tiered; check which plan unlocks agent read access before evaluating
- Hosted service: meeting data lives in your Tactiq account; review Tactiq's privacy terms if meetings are sensitive
- No public repo or star history: the surface is the hosted product

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [BulkTranscripts MCP - Hosted YouTube Transcripts and Channel Research](/hermes/mcp/servers/external/bulktranscripts-mcp)
- [TikTok Transcript MCP - AI Transcriptions of Public TikTok Videos](/hermes/mcp/servers/external/tiktok-transcript-mcp)
