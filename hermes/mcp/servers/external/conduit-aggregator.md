---
title: "Conduit (Toolport) MCP — Local-First Desktop Gateway for All MCP Tools"
description: "Conduit (Toolport) is a local-first desktop app that aggregates all your MCP servers behind one gateway, shared across every AI coding tool — Claude, Cursor, VS Code, Codex. One config, everywhere."
category: mcp
tags: [mcp-server, aggregator, gateway, desktop, local-first, multi-client]
last_updated: 2026-07-19
---

# Conduit (Toolport) — Local MCP Gateway

Conduit is a local-first desktop application that puts all your MCP servers behind one unified gateway. Configure your MCP servers once in Conduit, and they're automatically available to Claude Desktop, Cursor, VS Code, Codex, and any other MCP-compatible tool you use. No more copy-pasting JSON configs between tools.

**Source:** awesome-mcp-servers PR #8386 (discovered July 19, 2026)
**Category:** Aggregators / Developer Tools
**Author:** tsouth89
**Repo:** https://github.com/tsouth89/conduit-aggregator
**Status:** Active

## Why This Matters

Anyone running more than one MCP client knows the pain: configure servers in Claude Desktop's JSON, then again in Cursor, then again in Codex, and keep them all in sync. Conduit solves this by being the single source of truth — configure once, broadcast everywhere. For teams standardizing on MCP tooling, this is infrastructure.

## Installation

```bash
# Desktop app (macOS/Windows/Linux)
# Download from releases: https://github.com/tsouth89/conduit-aggregator/releases

# Or run the gateway directly
npm install -g conduit-aggregator
npx conduit-aggregator
```

## Configuration

Instead of configuring each MCP client individually, point them all to Conduit's local endpoint:

```json
{
  "mcpServers": {
    "conduit": {
      "command": "npx",
      "args": ["conduit-aggregator"],
      "env": {
        "CONDUIT_PORT": "3456"
      }
    }
  }
}
```

Then in Conduit's desktop UI, add all your actual MCP servers. They're instantly available to every connected client.

## Key Features

- **Single config** — manage all MCP servers from one desktop interface
- **Multi-client broadcast** — Claude, Cursor, VS Code, Codex all see the same tools
- **Local-first** — all traffic stays on your machine, no cloud dependency
- **Hot reload** — add/remove servers without restarting clients

## CorpusIQ Relevance

For teams running CorpusIQ's MCP server alongside other tools (GitHub, Filesystem, Brave Search), Conduit simplifies the configuration matrix. Could be recommended in CorpusIQ's onboarding docs as the preferred multi-server management approach.

## See Also

- [[sweeps/sweep-july19-2026]]
