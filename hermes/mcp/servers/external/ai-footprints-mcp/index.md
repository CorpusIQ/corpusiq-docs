---
title: "ai-footprints-mcp — Agent-First Bookmark & Knowledge Manager"
description: "Let AI agents manage your digital footprints — bookmarks, reading history, and knowledge trails. Chinese (AI 足迹) + English."
source: github.com/Piccolo123/ai-footprints-mcp
stars: 0
language: TypeScript
transport: stdio
category: Knowledge & Memory
last_updated: 2026-07-20
---

# ai-footprints-mcp — Agent-First Bookmark Manager

**AI 足迹 (AI Footprints) MCP Server** — let your AI agents manage your digital footprints: bookmarks, reading history, knowledge trails, and web discoveries. Bilingual (Chinese + English).

## Installation

```bash
npx -y ai-footprints-mcp
```

## Config

```json
{
  "mcpServers": {
    "ai-footprints": { "command": "npx", "args": ["-y", "ai-footprints-mcp"] }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `save_bookmark` | Save a URL with tags and notes |
| `search_footprints` | Search your bookmark/knowledge library |
| `get_reading_list` | Retrieve unread items by priority |
| `export_trail` | Export your knowledge trail for review |

## Operator Use Cases

- Research-heavy operators: let your AI agent save and organize discoveries
- Knowledge workers: build a searchable trail of everything you've read/learned
- Teams: share digital footprints across the team's AI agents
