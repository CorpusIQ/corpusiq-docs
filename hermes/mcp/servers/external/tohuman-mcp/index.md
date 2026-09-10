---
title: ToHuman MCP - AI Text Humanization for Content Teams
description: Official hosted MCP server for the ToHuman humanizer - one humanize tool with four intensity levels (minimal, subtle, medium, heavy), called over a free API key. No storage, no copy-paste.
category: Content
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★
tags: [content, humanizer, writing, ai-content, marketing, remote-mcp]
---

# ToHuman MCP

**Humanize AI text inside your agent, not in a browser tab** - the first-party ToHuman humanizer exposed as a single MCP tool. The hosted endpoint takes text, runs it through the ToHuman synchronous humanize API with your key, and returns the rewritten text as the tool response. No storage, no extra prompt layers - that is the whole surface area.

```
Server type: Remote (hosted, Streamable HTTP)
Auth: Free ToHuman API key in the Authorization header
Endpoint: https://tohuman.io/mcp
Tools: 1 (humanize, with intensity levels: minimal / subtle / medium / heavy)
Pricing: Free API key from your tohuman.io account
Built by: ToHuman (tohuman.io)
```

## Why This Matters for Operators

Teams that produce AI-drafted content end up with a manual "humanize" step - someone opens a browser, pastes the text, pastes it back, and breaks formatting on the way. **ToHuman MCP removes that step from the pipeline**: the drafting agent calls `humanize` directly with the intensity level that matches the brand (minimal for light polish, heavy for full rewrite), and the result lands in the same workflow as the draft. Because the server stores nothing and only forwards text to the humanize API, draft content never sits in an intermediary system.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `humanize` | Rewrite text to read more human, with selectable intensity: minimal, subtle, medium or heavy |

The server passes the text to the ToHuman synchronous humanize API using the API key from your client's Authorization header, waits for the output, and returns it as the tool response. No storage, no prompt injection, no extra processing.

## Installation

```bash
claude mcp add --transport http tohuman https://tohuman.io/mcp --header "Authorization: Bearer YOUR_TOHUMAN_KEY"
```

## Configuration

```json
{
  "mcpServers": {
    "tohuman": {
      "type": "http",
      "url": "https://tohuman.io/mcp",
      "headers": { "Authorization": "Bearer YOUR_TOHUMAN_KEY" }
    }
  }
}
```

Get the free API key from your tohuman.io account. Clients that only launch local (stdio) servers can use the build-your-own tutorial at tohuman.io/tutorials/mcp-server-humanize-ai-text, which wraps the same synchronous API.
