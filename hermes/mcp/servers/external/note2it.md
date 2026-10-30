---
title: note2it MCP Server Integration Guide
description: AI agent knowledge management with notebooks, nested pages, meeting transcripts and precise undoable edits via the note2it MCP server for Hermes Agent
category: mcp
tags: [mcp, note2it, knowledge-management, meetings, notebooks, hermes-agent]
last_updated: 2026-10-30
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/note2it/"
robots: "index,follow"

---

# note2it MCP - AI Agent Knowledge Management for Hermes Agent

Give your AI agents a persistent notebook system with meeting transcripts, a link graph, and precise, undoable edits.

## What It Does

note2it is a notes workspace designed for human and AI agent collaboration:

- **Notebooks, sections, and nested pages** - hierarchical organization
- **Meeting pages** - transcripts and structured summaries live on the meeting's page, so an agent reads them like any other page
- **AI agent access** - search, read, and make targeted, undoable edits
- **Wiki-link graph** - backlinks and outgoing links between pages
- **Fast slash-command editor** - keyboard-first for humans
- **MCP-native** - Claude, ChatGPT, Perplexity and other MCP clients connect directly or through a local bridge

For teams managing knowledge work, this replaces scattered note pages, meeting notes, and task lists with a single, AI-accessible knowledge base.

## Quick Setup

### Prerequisites

- **note2it account:** sign up at [note2it.com](https://note2it.com). The AI-assistant connector is included on the **Premium and Pro** plans (not Standard).
- **Node.js 18 or newer** for the local bridge (`npx` ships with it).
- **Personal API token:** in note2it open **Settings → AI assistants** and create a token. It starts with `n2i_` and is shown once. Pick read-only (`notes:read`) or read and write (`notes:write`).

### Option A - Local bridge (used by Hermes Agent)

The bridge is a small stdio process: your MCP client launches it, and it forwards every MCP message to note2it's hosted server at `https://app.note2it.com/api/mcp/mcp`. The client sees the same tools the hosted server exposes.

```bash
hermes mcp add note2it -- npx -y @note2it/mcp
```

Package: [`@note2it/mcp`](https://www.npmjs.com/package/@note2it/mcp). Set `NOTE2IT_API_KEY` to your token.

Or manual config:

```json
{
  "mcpServers": {
    "note2it": {
      "command": "npx",
      "args": ["-y", "@note2it/mcp"],
      "env": {
        "NOTE2IT_API_KEY": "n2i_..."
      }
    }
  }
}
```

Environment variables:

| Variable | Required | Description |
|----------|----------|-------------|
| `NOTE2IT_API_KEY` | yes | Personal API token (`n2i_...`). `NOTE2IT_TOKEN` also works. |
| `NOTE2IT_URL` | no | MCP endpoint. Defaults to `https://app.note2it.com/api/mcp/mcp`. Must be `https://` (`http://` is accepted only for localhost). |

### Option B - Direct remote connection

Clients that support remote MCP servers can skip the package and the token entirely and connect to:

```
https://app.note2it.com/api/mcp/mcp
```

note2it documents this one-click path for Claude (web, desktop, mobile) and ChatGPT developer mode, which sign in with OAuth instead of pasting a key. Perplexity connects with the same endpoint using the token as an `Authorization: Bearer` header. For Hermes Agent, the stdio bridge in Option A is the supported path.

## Tools

Read tools (`notes:read` scope):

| Tool | Description |
|------|-------------|
| `note2it-search` | Full-text search across every page you can read, with notebook, section, tag and date filters |
| `note2it-fetch` | Read one page by id or exact title, as Markdown or as a block outline with ids |
| `note2it-browse` | Walk the notebook → section → page hierarchy |
| `note2it-links` | Backlinks, outgoing links and graph neighbours around a page |
| `note2it-tags` | Tag index with page counts and recent pages |
| `note2it-list-templates` | List template pages and the fill-in fields each one has |

Write tools (`notes:write` scope):

| Tool | Description |
|------|-------------|
| `note2it-create-page` | Create a page from Markdown in a notebook and section |
| `note2it-update-page` | Replace a page's title or content, or toggle its template flag |
| `note2it-patch-page` | Edit part of a page without touching the rest |
| `note2it-move-page` | Move a page between notebooks or sections, or reorder it |
| `note2it-create-from-template` | Create a filled-in page from one of your templates |
| `note2it-page-history` | List a page's saved revisions from assistant edits, and restore one |
| `note2it-trash-page` | Move to trash or restore. Never deletes permanently |
| `note2it-upload-image` | Import an image from a public https URL into the media library |

The tool list comes from the server, so new note2it tools appear without updating the bridge package. There is no separate transcript or action-item tool: meeting transcripts and action items live on the meeting's page and are read with `note2it-search` and `note2it-fetch`.

## Use Cases for Business Operators

### 1. Meeting Follow-Through

A meeting page carries the transcript plus the structured summary. An agent can read it, pull the action items, and draft the follow-up in the same pass.

```
Agent prompt: "Fetch yesterday's product review meeting page in note2it.
List every action item and draft the follow-up messages."
```

### 2. Persistent AI Memory

Unlike chat history that disappears, note2it gives your AI agents a permanent memory layer. Research, decisions, and context persist across sessions.

```
Agent prompt: "Search note2it for our Q2 marketing strategy discussion
from March and summarize the decisions we made."
```

### 3. Team Knowledge Base

A shared repository that both humans and AI agents read, write and maintain. Every assistant edit is a saved revision, so a bad write is restored with `note2it-page-history` rather than retyped.

### 4. Project Documentation

Project specs, meeting notes and decisions in one searchable, AI-accessible space, with `note2it-move-page` and `note2it-browse` keeping the structure usable as it grows.

## Integration with CorpusIQ

note2it + CorpusIQ is a decision-support pipeline:

1. **CorpusIQ** - pull the business numbers (revenue, traffic, pipeline) from connected systems, cited
2. **note2it** - retrieve past decisions, context and meeting history
3. **AI agent** - make recommendations with both the live numbers and the reasoning behind them

The agent sees current operational data and the historical decision context in one answer.

## Pricing

The AI-assistant connector is included on the **Premium** and **Pro** plans. See [note2it.com/en/pricing](https://www.note2it.com/en/pricing) for current prices.

## Limitations

- The connector is not on the Standard plan; an unentitled plan returns HTTP 401 with a valid token.
- A token can only do what its scope allows: a read-only token makes every write tool fail with a scope error.
- The local bridge is new (npm v0.1.0, published Oct 30, 2026) - the tool surface is server-driven and may change without a package release.
- Product name is spelled **note2it**, all lowercase.

## See Also

- [note2it connect reference](https://www.note2it.com/en/connect)
- [`@note2it/mcp` on npm](https://www.npmjs.com/package/@note2it/mcp)
- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [MCP Overview](/hermes/mcp)
