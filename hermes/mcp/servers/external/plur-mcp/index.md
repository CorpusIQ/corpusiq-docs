---
title: "PLUR MCP — Persistent Memory for AI Agents"
description: "Open, local-first memory for AI agents. Store corrections, preferences, and conventions as plain-text engrams on your own machine — memory you can read, correct, and carry across sessions."
category: mcp
tags: [mcp, memory, knowledge, agent-memory, local-first, plur, hermes-agent]
github: https://github.com/plur-ai/plur
stars: 226
verified: true
source: mcp.so
discovered: 2026-07-24
pricing: Free · Open Source (MIT)
---

# PLUR MCP — Persistent Memory for AI Agents

**PLUR** solves the amnesia problem: AI agents start every session with amnesia — you re-explain the project, repeat your preferences, and correct the same mistakes over and over. PLUR gives them a memory that persists.

It's open, local-first memory for AI agents. Your agent's corrections, preferences, and conventions are stored as plain-text engrams on your own machine — memory you can read, correct, and carry across sessions without vendor lock-in.

## What It Does

- **Persistent agent memory**: Corrections, preferences, and conventions survive across sessions
- **Local-first**: All engrams stored as plain-text files on your machine — no cloud dependency
- **Open source (MIT)**: Full transparency, no vendor lock-in
- **Multi-agent aware**: One memory store for all your MCP-compatible agents
- **Human-readable**: Engrams are plain text — you can read, edit, and prune them directly

## Key Tools

| Tool | Description |
|------|-------------|
| `plur_store` | Save a new memory engram |
| `plur_search` | Semantic search across stored engrams |
| `plur_list` | List all stored engrams |
| `plur_delete` | Remove an engram by ID |

## Quick Start

### 1. Install

```bash
git clone https://github.com/plur-ai/plur
cd plur
npm install
npm run build
```

### 2. Configure Your MCP Client

```json
{
  "mcpServers": {
    "plur": {
      "command": "node",
      "args": ["/path/to/plur/dist/index.js"],
      "env": {
        "PLUR_STORE_PATH": "~/.plur/engrams"
      }
    }
  }
}
```

### 3. First Use

Once connected, your agent can call `plur_store` to remember anything:
- "Remember I prefer TypeScript with strict mode"
- "Store that our API base URL is https://api.corpusiq.io"
- "Save the convention: always use async/await, never .then()"

On the next session, call `plur_search` and the agent retrieves what it needs.

## Hermes Agent Integration

```yaml
# ~/.hermes/config.yaml
mcp_servers:
  plur:
    command: "node"
    args: ["/home/hermes/tools/plur/dist/index.js"]
    env:
      PLUR_STORE_PATH: "~/.plur/engrams"
```

## Use Cases for Business Operators

1. **Self-improving agents**: Your growth agent remembers what content performed well, what outreach templates worked, and which communities respond best
2. **Cross-session consistency**: Agents carry preferences, style guides, and business rules across restarts
3. **Team memory**: Share engram stores across team members for consistent AI behavior
4. **Audit trail**: Plain-text engrams let you inspect exactly what your agents have "learned"

## How It Compares

| Tool | Approach | Storage | License |
|------|----------|---------|---------|
| **PLUR** | Local-first engrams | Your filesystem | MIT |
| **Groundwork** | Company-state feed | Cloud-hosted | Source-available |
| **Memory (official)** | Knowledge graph | Local file | MIT |
| **Context7** | Doc retrieval | Cloud | Proprietary |

PLUR differentiates by being: (1) fully local, (2) plain-text readable, (3) MIT licensed, and (4) purpose-built for agent corrections and preferences rather than general knowledge retrieval.

## Limitations

- **No cloud sync (yet)**: Engrams are local — share via git, rsync, or your own sync solution
- **New project**: Early-stage, API may evolve
- **Text-only**: No structured data or multimodal memory (yet)
- **Local setup required**: Must install Node.js and clone the repo — no hosted version

## Category

**Memory & Knowledge** — PLUR focuses specifically on agent corrections and preferences, making it complementary to general documentation tools like Context7 and company-state feeds like Groundwork.

---

*Discovered via [mcp.so](https://mcp.so/servers/plur) on July 24, 2026. Verified listing. GitHub: [plur-ai/plur](https://github.com/plur-ai/plur). 226 stars.*
