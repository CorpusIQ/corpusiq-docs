---
title: MCP Use Setup — Fullstack MCP Framework for Hermes Agents
description: Install and configure mcp-use — the fullstack MCP framework for building MCP Apps and Servers. Python + TypeScript SDK, 10K+ GitHub stars.
author: manufact.com
repo: https://github.com/mcp-use/mcp-use
stars: 10,317
license: Apache 2.0
---

# MCP Use Setup Guide

**Source:** [mcp-use/mcp-use](https://skills.sh/mcp-use/mcp-use) (10,317 ⭐)
**Category:** Agent Infrastructure / MCP Development

mcp-use is the fullstack MCP framework for developing MCP Apps for ChatGPT, Claude, and MCP Servers for AI agents. It provides Python and TypeScript SDKs with a unified API for building, testing, and deploying MCP-powered applications. Compatible with Hermes, OpenClaw, Claude Code, and any MCP client.

---

## Quick Install

```bash
# Install the skill
npx skills add mcp-use/mcp-use@mcp-apps-builder

# Python SDK
pip install mcp-use

# TypeScript SDK
npm install mcp-use
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Python** | 3.10+ for Python SDK |
| **Node.js** | 18+ for TypeScript SDK |
| **Hermes Agent** | v0.16.0+ with MCP support |
| **MCP Inspector** | Optional — for debugging MCP servers |

---

## What You Can Build

mcp-use unlocks three categories of MCP development:

### 1. MCP Apps (Agent-facing UI)
Build interactive apps that agents can use — dashboards, forms, visualizations. Think of these as "websites for AI agents."

```python
from mcp_use import MCPApp, ui

app = MCPApp("my-dashboard")

@app.page("/")
def dashboard():
    return ui.Card(
        ui.Text("System Status"),
        ui.Chart(data=metrics, type="line")
    )
```

### 2. MCP Servers (Tool Providers)
Build servers that expose tools, resources, and prompts to MCP clients.

```python
from mcp_use import MCPServer, tool

server = MCPServer("my-tools")

@server.tool()
def search_knowledge_base(query: str) -> list:
    """Search the company knowledge base."""
    return kb.search(query)
```

### 3. MCP Clients (Tool Consumers)
Build clients that connect to multiple MCP servers and orchestrate tool usage.

---

## Key Features

| Feature | Description |
|---|---|
| **Unified SDK** | Same API across Python and TypeScript |
| **Auto-discovery** | Servers auto-register with MCP clients |
| **Hot reload** | Edit servers without restarting |
| **Built-in auth** | OAuth2.1, API keys, JWT support |
| **Streaming** | Real-time tool output streaming |
| **Validation** | JSON Schema validation for all tool inputs |
| **Testing** | Built-in MCP test harness |

---

## Hermes Integration

mcp-use servers work natively with Hermes' MCP client. After building a server:

```bash
# Start the MCP server
python -m mcp_use serve my_server.py --port 3001

# Register with Hermes (in config.yaml)
mcp_servers:
  my-tools:
    transport: http
    url: http://localhost:3001/mcp
```

Hermes will auto-discover all tools, resources, and prompts exposed by the server.

---

## Why This Matters

Before mcp-use, building MCP servers required manual implementation of the MCP protocol — JSON-RPC message handling, transport layer management, capability negotiation. mcp-use abstracts all of this behind a clean SDK:

- **Python:** `pip install mcp-use` → `@server.tool()` decorator → done
- **TypeScript:** `npm install mcp-use` → `server.tool()` → done

This reduces MCP server development from days to minutes.

---

## Production Notes

- 10K+ GitHub stars, active daily development
- Built by manufact.com — production MCP infrastructure provider
- Python package: 100K+ downloads/month (PyPI)
- TypeScript package: growing rapidly (npm)
- Full documentation at https://mcp-use.com/docs
- Active Discord community (https://discord.gg/XkNkSkMz3V)

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Server not discovered | Wrong transport config | Verify `transport: http` and URL |
| Tool returns 404 | Server not running | Check `mcp_use serve` process |
| Auth failure | Missing credentials | Configure OAuth or API key in server config |

---

*← [AgentMemory Setup](/hermes/skills/catalog/agentmemory-setup/) | [Memory Merger Setup →](/hermes/skills/catalog/memory-merger-setup/)*
*Powered by CorpusIQ*
