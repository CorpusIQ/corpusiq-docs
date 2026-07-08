---
title: Note2IT MCP Server Integration Guide
description: AI agent knowledge management with notebooks, meeting transcripts, and structured action items via Note2IT MCP for Hermes Agent
category: mcp
tags: [mcp, note2it, knowledge-management, meetings, notebooks, hermes-agent]
last_updated: 2026-07-08
---

# Note2IT MCP — AI Agent Knowledge Management for Hermes Agent

Give your AI agents a persistent notebook system with meeting transcripts, structured summaries, and undoable edits.

## What It Does

Note2IT is a knowledge workspace designed for human + AI agent collaboration:

- **Notebooks, sections, and nested pages** — hierarchical organization
- **Meeting recording** → automatic transcript + structured summary with action items
- **AI agent access** — search, read, and make precise, undoable edits
- **Fast slash-command editor** — keyboard-first for humans
- **MCP-native** — Claude and other AI agents connect directly

For operators managing knowledge work, this replaces scattered Notion pages, meeting notes, and task lists with a single, AI-accessible knowledge base.

## Quick Setup

### Prerequisites
- **Note2IT account:** Sign up at [note2it.com](https://note2it.com)
- **API access:** Available with paid plans

### Add to Hermes Agent

```bash
hermes mcp add note2it -- npx -y @note2it/mcp
```

Or manual config:

```json
{
  "mcpServers": {
    "note2it": {
      "command": "npx",
      "args": ["-y", "@note2it/mcp"],
      "env": {
        "NOTE2IT_API_KEY": "your-api-key"
      }
    }
  }
}
```

## Key Capabilities

| Tool | Description |
|------|-------------|
| `search_notes` | Full-text search across all notebooks |
| `read_page` | Read a specific page's content |
| `edit_page` | Make precise, undoable edits to a page |
| `create_page` | Create a new page in a notebook |
| `get_transcript` | Retrieve meeting transcript |
| `get_action_items` | Extract structured action items from meetings |
| `summarize_notebook` | Generate summary of a notebook's contents |

## Use Cases for Business Operators

### 1. Meeting Intelligence Pipeline
Record a meeting → AI generates transcript + structured summary → action items auto-populated → AI agent can reference later.

```
Agent prompt: "Read yesterday's product review meeting in Note2IT. 
List all action items assigned to me and draft follow-up messages."
```

### 2. Persistent AI Memory
Unlike chat history that disappears, Note2IT gives your AI agents a permanent memory layer. Research, decisions, and context persist across sessions.

```
Agent prompt: "Search Note2IT for our Q2 marketing strategy discussion 
from March and summarize the key decisions we made."
```

### 3. Team Knowledge Base
Build a shared knowledge repository that both humans and AI agents can read, write, and maintain.

### 4. Project Documentation
Keep project specs, meeting notes, and decisions in one searchable, AI-accessible space.

## Integration with CorpusIQ

Note2IT + CorpusIQ = decision-support pipeline:

1. **CorpusIQ** → pull business metrics (revenue, traffic, pipeline)
2. **Note2IT** → retrieve past decisions, context, meeting history
3. **AI agent** → make informed recommendations with full context

The AI sees both real-time business data AND the historical decision context.

## Pricing

Check [note2it.com/pricing](https://note2it.com) for current plans. MCP access typically requires a paid tier.

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Overview](/hermes/mcp/)*

*↑ [MCP Documentation](/hermes/mcp/)*
