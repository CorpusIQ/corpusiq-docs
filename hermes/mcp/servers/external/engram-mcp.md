---
title: "Engram MCP — Git-Backed Shared Memory Dashboard for AI Agents"
description: "Engram MCP server — self-hosted memory with dashboard UI backed by a git repository of markdown files. Authoritative search ensures agents always get the latest version. Docker-deployable."
category: mcp
tags: [mcp-server, memory, knowledge-management, git-backed, self-hosted, dashboard]
last_updated: 2026-07-19
---

# Engram MCP Server — Git-Backed Memory Dashboard

Engram is a self-hosted MCP server + dashboard that gives AI agents shared memory over a git-backed folder of markdown files. What differentiates it from other memory servers: search is authoritative — it always returns the latest committed version, not a stale embedding. The dashboard provides human visibility into what agents are remembering.

**Source:** awesome-mcp-servers PR #9807 (discovered July 19, 2026)
**Category:** Knowledge & Memory
**Author:** rwnalds
**Repo:** https://github.com/rwnalds/engram
**Status:** Active

## Why This Matters

Most vector-based memory solutions have a fundamental problem: the embedding and the source document drift apart. Engram solves this by making the source of truth a git repository of markdown files — every write is a commit, every read is from HEAD. The dashboard lets humans audit what agents are writing, edit memories directly, and roll back bad writes via git.

## Installation

```bash
# Clone and run via Docker
git clone https://github.com/rwnalds/engram
cd engram
docker-compose up -d

# Or run directly
npm install -g engram-mcp
npx engram-mcp
```

## Claude Desktop / Hermes Configuration

```json
{
  "mcpServers": {
    "engram": {
      "command": "npx",
      "args": ["engram-mcp"],
      "env": {
        "ENGRAM_REPO_PATH": "~/.engram/memory",
        "ENGRAM_PORT": "3001"
      }
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `write_memory` | Commit a new memory as a markdown file |
| `search_memory` | Authoritative search — always returns HEAD version |
| `edit_memory` | Modify an existing memory (creates a new commit) |
| `list_memories` | Browse all stored memories with metadata |
| `get_history` | View git log for a specific memory file |

## Dashboard

Engram includes a web dashboard at `http://localhost:3001` where humans can:
- Browse all agent-written memories
- Edit or delete entries manually
- View git history and diffs
- Roll back to any previous version

## CorpusIQ Relevance

Engram's git-backed approach is philosophically aligned with how CorpusIQ already operates (GBrain's markdown vault, git-tracked docs). Could serve as a lighter alternative to GBrain for teams that want agent memory without the full knowledge graph infrastructure.

## See Also

- [[sweeps/sweep-july19-2026]]
- Linksee Memory
