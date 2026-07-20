---
title: "skillselion-mcp — Skills & MCP Marketplace Search"
description: "Search Skillselion's curated directory of Claude Code skills, MCP servers & plugin marketplaces, ranked by installs and GitHub stars."
source: github.com/skillselion/skillselion-mcp
stars: 0
language: TypeScript
transport: stdio
category: Aggregators
last_updated: 2026-07-20
---

# skillselion-mcp — Skills & MCP Marketplace Search

**Search Skillselion's curated directory of Claude Code skills, MCP servers, and plugin marketplaces** — all ranked by installs and GitHub stars. For operators discovering the best AI agent tools.

## Installation

```bash
npx -y skillselion-mcp
```

## Config

```json
{
  "mcpServers": {
    "skillselion": { "command": "npx", "args": ["-y", "skillselion-mcp"] }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `search_skills` | Search Claude Code skills by keyword, ranked by installs |
| `search_mcp_servers` | Search MCP servers ranked by GitHub stars |
| `search_plugins` | Search plugin marketplaces |
| `get_trending` | Get trending skills/servers this week |

## Operator Use Cases

- Discover new MCP servers for your AI toolchain
- Find Claude Code skills for specific workflows (DevOps, finance, marketing)
- Track trending tools in the agent ecosystem
- Competitive research on MCP server adoption
