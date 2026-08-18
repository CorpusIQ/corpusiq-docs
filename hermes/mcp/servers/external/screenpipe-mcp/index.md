---
title: "Screenpipe MCP - CorpusIQ Docs - CorpusIQ Docs"
description: "Local-first workflow memory for AI agents - screenpipe records screen, audio, app and meeting context locally and exposes it to Claude, Codex and Cursor through a searchable MCP server"
category: Productivity
stars: 21061
added: 2026-08-18
source: "mcp.so GitHub issue #3626"
relevance: ★★★
tags: [screen-recording, workflow-memory, local-first, audio-transcription, productivity, agent-context, meeting-notes, ocr]
---

# Screenpipe MCP

**Local-first workflow memory for AI agents: screenpipe captures selected screen, audio, app and meeting context on-device 24/7, then exposes that searchable history to Claude, Codex, Cursor and other MCP clients through an MCP server and local API.** YC S26 company, 21,000+ GitHub stars, and the capture stays on your machine — the MCP server talks to the local screenpipe API at `localhost:3030`, not a cloud service.

```
Server type: stdio via npm (local API at localhost:3030), optional HTTP wrapper
Auth: None for local use; optional SCREENPIPE_LOCAL_API_KEY
Install: npx -y screenpipe-mcp
Tools: search-content, export-video over the local capture index
Requirements: screenpipe app running, Node.js 18+
License: source-available (LICENSE.md, updated June 10, 2026)
Category: Productivity / local-first workflow memory
Built by: screenpipe (screenpipe.com, YC S26) — 21,061★ on GitHub
```

## Why This Matters for Operators

Operators live in context nobody captures: the dashboard you checked before the call, the meeting where a decision was actually made, the error you fixed last Tuesday. Agents work from what you tell them. Screenpipe closes that gap by recording everything locally, OCR-ing screens, transcribing audio and meetings, and letting the agent search it the way it searches any tool. "What did I say about the pricing page last Thursday" becomes a real query instead of a memory test.

**The local-first angle matters for business data.** Capture never leaves the machine; screenpipe is source-available so teams can audit exactly what gets stored. For operators handling financials, customer data or internal strategy, that beats sending screen context through a cloud recorder.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `search-content` | Search the local index across screen text, audio transcripts, user input events, apps, windows and time ranges |
| `export-video` | Export recorded video for a selected local time range |

The MCP server is a thin layer over the richer local API (`localhost:3030`), which adds OCR, full-text search, audio transcription, and pipe-based processing. If the MCP server returns empty results, the health check is `curl http://localhost:3030/health` — the capture app must be running first.

## Installation

```bash
claude mcp add screenpipe --transport stdio -- npx -y screenpipe-mcp
```

Or via one-click install from the screenpipe desktop app: Settings → Connections → Install extension, which writes the config for Claude, Codex or Cursor automatically.

Manual JSON config for Claude Desktop (`~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "screenpipe": {
      "command": "npx",
      "args": ["-y", "screenpipe-mcp"],
      "transport": "stdio"
    }
  }
}
```

For Codex, the app writes `~/.codex/config.toml` directly; manual form:

```toml
[mcp_servers.screenpipe]
command = "npx"
args = ["-y", "screenpipe-mcp"]
enabled = true
```

## Configuration

| Variable | Required | Default | Description |
|---|---|---|---|
| `SCREENPIPE_LOCAL_API_KEY` | no | — | Optional key for the local API, set in the same config block |
| app process | yes | — | screenpipe desktop app must be running on localhost:3030 |

Verify the connection by asking the agent "what did I do in the last 5 minutes" — a working install answers from the local index.

## Business Relevance

- **Executives and operators** get searchable meeting memory without a SaaS transcription bill; screenpipe transcribes locally and keeps it on-device
- **Support and ops teams** can reconstruct "what was on screen when the error happened" from the captured window history
- **Solo operators** replace fragmented note-taking with a queryable record of their actual workday
- **Security-conscious teams** keep capture data in-house; no cloud dependency in the default path

## Integration with CorpusIQ

Screenpipe is context infrastructure, not a business-data connector — it does not overlap with CorpusIQ's 40+ connectors for commerce, ads, finance and analytics. The two compose: screenpipe supplies the agent's memory of what happened in your workspace, and CorpusIQ supplies the live business data to act on it. An agent with both can go from "what did the CFO say about churn in Tuesday's call" (screenpipe) to "what is churn this quarter by plan" (CorpusIQ) in one session.

## Limitations

- Capture app must be running locally; the MCP server is a search surface, not a recorder
- Source-available license (updated June 10, 2026), not OSI open source — review LICENSE.md for commercial use
- Local index grows with recording time; plan disk usage for always-on capture
- Windows, macOS and Linux supported, but setup paths differ per client and platform
