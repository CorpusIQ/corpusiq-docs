---
title: "Lavox MCP: Local-First Meeting Memory for AI Agents"
description: "Local-first macOS meeting recorder and dictation app whose on-device Whisper transcriptions and typed assertion index become a queryable memory any AI can read over MCP. Decisions carry the chosen option, rejected alternatives and stated reasoning, each anchored to a verbatim transcript quote; corrections supersede rather than delete. MIT licensed, new Aug 2026."
category: Productivity
stars: n/a (new listing)
added: 2026-08-24
source: "chatmcp/mcpso issue #3724"
relevance: ★★
tags: [meetings, transcription, memory, local-first, macos, decisions, stdio]
---

# Lavox MCP

**A local-first macOS meeting recorder and dictation app that turns everything you say into a structured memory any AI can read over MCP.** Lavox records on-device, transcribes with local Whisper, identifies speakers, and writes a single SQLite memory file the user owns. The memory is two-layer and bitemporal: verbatim transcript chunks are canonical, a typed assertion index (decisions, facts, commitments) sits on top, and each decision stores the chosen option, the rejected alternatives, and the stated reasoning, anchored to the exact transcript quote. Corrections supersede rather than delete, so "what did we believe in July?" stays answerable.

```
Server type: stdio wrapper over a local HTTP server (macOS 13+, Apple Silicon)
Auth: None (everything runs on-device; nothing leaves the machine by default)
Repo: github.com/lavox-app/lavox (MIT, 1 star, Aug 2026)
Install: Local server on 127.0.0.1:8040 plus the lavox-mcp.sh wrapper
Tools: Memory search and recall over transcript chunks, decisions, facts, and commitments
```

## Why This Matters for Operators

Everything you say evaporates. Meetings, decisions, and promises are spoken, then gone; three months later nobody remembers why option A beat option B, and every AI session starts from zero. Cloud notetakers solve neither problem: they upload your conversations and stop at summaries. Lavox closes the loop: record locally, transcribe locally, build the structured memory, and serve it to every AI tool you use through MCP, with the verbatim quote to prove each answer.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| Memory search | Full-text and typed search across recorded meetings and voice notes |
| Decision recall | Retrieves decisions with chosen option, rejected alternatives, and stated reasoning, each anchored to a transcript quote |
| Fact and commitment lookup | Queries the typed assertion index for facts and commitments stated in meetings |
| Verbatim citation | Every recalled answer carries the exact transcript quote and its occurrence time |
| Bitemporal history | Corrections supersede rather than delete, so past beliefs remain queryable by date |

Capability-level table: tool names are defined by the local server and wrapper; the issue and README document the query surface above without enumerating exact tool identifiers.

## Installation

Requirements: macOS 13+ on Apple Silicon, Rust and pnpm for the app, Python 3.12 for the server.

```bash
git clone https://github.com/lavox-app/lavox.git && cd lavox

# 1. The server: transcription, memory, MCP
cd server
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/uvicorn app:app --host 127.0.0.1 --port 8040   # keep running

# 2. The app: recorder and dictation bar
cd ../app
pnpm install
./build-and-install.command

# 3. Wire the memory into Claude Code
claude mcp add lavox-memory -- "$PWD/../bin/lavox-mcp.sh"
```

Record a meeting or dictate a note, then ask Claude to search `lavox-memory` for it.

## Configuration

No accounts and no API keys. Recording, Whisper transcription, speaker identification, and embeddings all run on-device; the memory is a single SQLite file the user owns. The MCP wrapper points the agent at the local server, so nothing leaves the machine by default.

## Example Prompts

- "What did we decide about pricing last month, and why not the other option?"
- "List every commitment I made in last week's meetings, with the exact quote."
- "What did we believe about the launch date in July, and when did it change?"
- "Summarize my voice notes from yesterday and file any open action items."

## Business Relevance

- **Founders and operators** keep decisions and their reasoning searchable across months
- **Teams with AI workflows** give every agent the same meeting memory instead of re-explaining context
- **Privacy-sensitive orgs** get meeting intelligence with zero cloud upload
- **Anyone who dictates** turns voice notes into structured, queryable memory

## Integration with CorpusIQ

Lavox answers what was said and decided in meetings; CorpusIQ answers what the business data shows. An agent can recall the pricing decision from Lavox with its reasoning and quote, then pull actual revenue, churn, and deal data from CorpusIQ to see whether the decision held up, joining spoken memory with measured business truth in one answer.

## Limitations

- macOS-only (Apple Silicon, macOS 13+), so Windows and Linux teams cannot run the recorder.
- Very new project (1 star, Aug 2026); the app requires building from source with Xcode.
- Local-first means the memory lives on one machine unless you sync the SQLite file yourself.
- Exact MCP tool names are not enumerated in public docs; the capability table above is prose-derived.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [BusyMail MCP](/docs/hermes/mcp/servers/external/busymail-mcp) - email operations for agents
- [GTD Brain MCP](/docs/hermes/mcp/servers/external/gtd-brain-mcp) - task and context management
- [Agentic Memory MCP](/docs/hermes/mcp/servers/external/agentic-memory-mcp) - persistent agent memory layer
- [Greminders MCP](/docs/hermes/mcp/servers/external/greminders-mcp) - reminder and follow-up scheduling
