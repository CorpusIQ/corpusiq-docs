---
title: Build MCP Server — Anthropic Official Setup Guide
description: Install and configure build-mcp-server, Anthropic's official guide to building MCP (Model Context Protocol) servers. 3,148 installs, TypeScript + Python examples. From anthropics/claude-plugins-official.
---

# Build MCP Server — Setup Guide

**Source:** [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 3,148 installs
**Category:** MCP Development / Agent Infrastructure
**License:** MIT · **Language:** TypeScript, Python · **Published:** 2026

Anthropic's official skill for building MCP (Model Context Protocol) servers. Step-by-step guidance from transport layer setup through tool registration, resource exposure, and prompt templates. The most-installed MCP server creation guide on skills.sh.

---

## What It Does

| Phase | What You Build |
|-------|---------------|
| **Transport** | stdio or HTTP/SSE transport layer for MCP communication |
| **Tools** | Register tools with typed inputs and outputs |
| **Resources** | Expose data sources as MCP resources with URI templates |
| **Prompts** | Define reusable prompt templates for agent consumption |
| **Testing** | Validate server behavior with MCP Inspector |

Covers both TypeScript (via `@modelcontextprotocol/sdk`) and Python (via `mcp` package) implementations with complete, runnable examples.

---

## Prerequisites

- Node.js 18+ (for TypeScript servers) or Python 3.10+ (for Python servers)
- Familiarity with JSON-RPC concepts
- Hermes Agent (or any MCP-compatible client) for testing

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add anthropics/claude-plugins-official@build-mcp-server
```

### Direct from GitHub

```bash
git clone https://github.com/anthropics/claude-plugins-official.git
cd claude-plugins-official/build-mcp-server
```

### Quick Start — TypeScript

```bash
mkdir my-mcp-server && cd my-mcp-server
npm init -y
npm install @modelcontextprotocol/sdk zod
npm install -D typescript @types/node
```

### Quick Start — Python

```bash
mkdir my-mcp-server && cd my-mcp-server
python3 -m venv venv
source venv/bin/activate
pip install mcp
```

---

## Usage with Hermes Agent

Once your MCP server is built, register it in Hermes:

```yaml
# ~/.hermes/config.yaml
mcp_servers:
  my-custom-server:
    command: node
    args: ["dist/index.js"]
    # or for Python:
    # command: python3
    # args: ["server.py"]
```

Hermes will auto-discover the server's tools and make them available to all agents.

```bash
# Verify the server is connected
hermes mcp test
hermes mcp list  # should show your server's tools
```

---

## Core Patterns

### Tool Registration (TypeScript)

```typescript
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [{
    name: "get_weather",
    description: "Get current weather for a city",
    inputSchema: {
      type: "object",
      properties: {
        city: { type: "string", description: "City name" }
      },
      required: ["city"]
    }
  }]
}));
```

### Tool Registration (Python)

```python
@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="get_weather",
            description="Get current weather for a city",
            inputSchema={
                "type": "object",
                "properties": {
                    "city": {"type": "string"}
                },
                "required": ["city"]
            }
        )
    ]
```

---

## CorpusIQ Use Cases

| Use Case | How |
|----------|-----|
| Custom data connectors | Build MCP servers for proprietary data sources |
| Internal tool exposure | Wrap internal APIs as MCP tools for Hermes agents |
| Multi-agent tool sharing | One MCP server, consumed by all CorpusIQ agents |
| Client deployments | Build customer-specific MCP servers for white-label |

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Server not discovered | Verify command/args in config.yaml; check `hermes mcp test` |
| Tool calling fails | Validate inputSchema matches what you're sending |
| Python import errors | Ensure `mcp` package is in the venv |
| stdio transport hangs | Use HTTP/SSE transport for long-running servers |

---

## Companion Skills

- [build-mcp-app](/hermes/skills/marketplace/new-june30-2026/) — Full MCP application development
- [build-mcpb](/hermes/skills/marketplace/new-june30-2026/) — Same guide, Bun runtime
- [mcp-developer](/hermes/skills/marketplace/new-june30-2026/) — Debugging and testing toolkit
- [mcp-security-audit](/hermes/skills/marketplace/new-june30-2026/) — Security scanning for MCP servers

---

*← [MCP Development](/hermes/skills/catalog/#mcp--api-integration) | [Catalog Home](/hermes/skills/catalog/) →*

---

*Part of the Hermes Skills Library. Curated by CorpusIQ — one MCP endpoint, all your business tools. Content remains attributed to original authors and repositories.*
