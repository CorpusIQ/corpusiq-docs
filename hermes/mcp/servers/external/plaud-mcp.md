---
title: "Plaud MCP - AI Recording Integration for Hermes Agent"
description: "Connect Plaud.ai recordings to Hermes Agent. Search recordings, read transcripts, generate documents - all from your AI assistant."
category: mcp
tags: [mcp-server, plaud, meeting-notes, transcription, recordings, communication, knowledge-retrieval]
last_updated: 2026-10-30
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/plaud-mcp/"
robots: "index,follow"

---

# Plaud MCP Server ★ New (July 4)

## Overview

Plaud MCP connects AI agents to your Plaud.ai recording library. Plaud is an AI-powered voice recorder that captures meetings, calls, and conversations - then transcribes and summarizes them. With the MCP server, agents can search your recording history, pull full transcripts, generate summaries, and extract action items from any conversation you've captured.

**Key advantage**: Your AI assistant gains access to every conversation you've recorded. Ask "what was the client's feedback on the Q3 roadmap?" and get answers grounded in actual meeting transcripts, not memory.

## Key Features

- **Recording search**: Full-text search across all recordings, transcripts, and summaries
- **Transcript retrieval**: Pull complete transcripts with speaker labels and timestamps
- **Document generation**: Create meeting notes, summaries, and action-item lists from recordings
- **Cross-recording analysis**: Find patterns, recurring topics, and commitments across multiple recordings
- **AI-powered summaries**: Generate concise summaries of any recording via the Plaud AI engine
- **Remote endpoint**: Hosted MCP server - connect directly, no local installation needed

## Installation

```bash
# Add to Hermes (remote SSE endpoint)
hermes mcp add plaud --url https://api.plaud.ai/mcp
```

## Configuration

1. Obtain your Plaud API credentials from [docs.plaud.ai](https://docs.plaud.ai/plaud-mcp-cli/mcp)
2. Add the remote endpoint to your MCP client configuration
3. Authenticate via OAuth - your client will open a browser for one-time authorization

## Tools

14 tools, all prefixed `plaud_`.

| Tool | Description |
|------|-------------|
| `plaud_list_files` | List recordings, optionally filtered by transcription status |
| `plaud_get_file` | Get detailed metadata for a specific file |
| `plaud_search_files` | Search recordings by keyword or date range |
| `plaud_get_transcript` | Fetch raw or polished transcript text |
| `plaud_get_summary` | Fetch AI-generated summary |
| `plaud_export_transcript` | Export transcript as TXT or SRT with optional timestamps |
| `plaud_generate` | Generate transcript and summary for a file |
| `plaud_name_speakers` | Rename speakers in a transcript |
| `plaud_rename_file` | Rename a single file |
| `plaud_batch_rename` | Rename multiple files at once (rate-limited) |
| `plaud_move_to_folder` | Move a file to a folder |
| `plaud_list_folders` | List all folders and tags |
| `plaud_trash_file` | Move a file to trash |
| `plaud_get_user` | Get current user profile |

## Use Cases for Operators

- **Client call intelligence**: Before a follow-up call, ask your agent "what did we promise Acme Corp in our last three calls?" - it searches your Plaud recordings and surfaces commitments
- **Meeting prep**: "Summarize all conversations about the pricing change from the last two weeks"
- **Knowledge preservation**: Every customer call, team standup, and partner meeting becomes a searchable knowledge asset
- **Cross-functional alignment**: "Find every mention of the API migration across all recordings this month"

## Why Operators Need This

Operators spend 40%+ of their time in meetings. Most of those insights evaporate within 48 hours. Plaud MCP turns every recorded conversation into a persistent, queryable memory that your AI assistant can draw on - so you stop forgetting decisions and start building on them.

---

*Discovered via mcpservers.org - July 4, 2026*
*← [External MCP Catalog](/hermes/mcp/servers/external) | [Plaud MCP Docs](https://docs.plaud.ai/plaud-mcp-cli/mcp) →*
