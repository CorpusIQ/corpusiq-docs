---
title: native-mcp — Full Setup Guide for Hermes Agents
description: Install and configure the native-mcp skill from nousresearch/hermes-agent. Connect Hermes Agent to MCP servers over stdio and HTTP, auto-discover tools, and manage server lifecycles.
---

# native-mcp — Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent) (79 installs)
**Category:** Infrastructure / MCP

The native MCP client skill enables Hermes Agent to connect to Model Context Protocol (MCP) servers over stdio and HTTP transports. It handles server discovery, tool registration, and lifecycle management — the foundation for building tool-rich AI agents.

---

## Installation

```bash
npx skills add nousresearch/hermes-agent --skill native-mcp
```

The skill is already bundled with Hermes Agent (it's in the `autonomous-ai-agents` and `creative` categories). Verify with:

```bash
hermes skills list | grep native-mcp
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | v0.16.0+ (uses built-in MCP transport layer) |
| **MCP Server** | Any MCP-compatible server (stdio or HTTP) |
| **Python 3.11+** | Required for the MCP client runtime |

For HTTP-based MCP servers, configure the server endpoint in `~/.hermes/config.yaml`:

```yaml
mcp_servers:
  - name: "example-server"
    transport: "http"
    url: "http://localhost:3000"
```

For stdio-based servers, define the command:

```yaml
mcp_servers:
  - name: "local-tools"
    transport: "stdio"
    command: "python"
    args: ["-m", "my_mcp_server"]
```

---

## Key Capabilities

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| **Connect to MCP server** | Configure in `config.yaml` → Hermes auto-connects on startup | stdio and HTTP transports supported |
| **Auto-discover tools** | Connected servers expose tools automatically | Tools appear in `hermes tools list` |
| **List connected servers** | `hermes mcp list` | Shows transport, status, tool count |
| **Reconnect on failure** | Automatic — handles disconnects gracefully | Exponential backoff for HTTP |
| **Tool registration** | Automatic on connect | No manual registration needed |

### Configuration Reference

```yaml
# ~/.hermes/config.yaml — MCP server configuration
mcp_servers:
  - name: "corpusiq-mcp"
    transport: "http"
    url: "https://mcp.corpusiq.io"
    headers:
      Authorization: "Bearer ${CORPUSIQ_MCP_TOKEN}"
    timeout: 30
    
  - name: "local-filesystem"
    transport: "stdio"
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/hermes"]
```

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **CorpusIQ MCP integration** | Connect Hermes agents to the CorpusIQ MCP server (54+ data connectors) for live business data access |
| **Multi-server orchestration** | Connect to 3+ MCP servers simultaneously — analytics, CRM, and email — for cross-source workflow automation |
| **Development toolchain** | Connect to local MCP servers (filesystem, git, database) for agent-powered development workflows |
| **Customer deployments** | Configure customer-specific MCP servers with scoped tool access for white-label agent deployments |
| **Tool discovery** | Use `hermes mcp list` to audit which tools are available across all connected servers before building automation |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| **Server connection refused** | Verify the MCP server is running: `curl http://localhost:3000/health` |
| **Tools not appearing** | Check server logs for tool registration errors. Run `hermes mcp test <server-name>` |
| **HTTP timeout** | Increase `timeout` in config.yaml. Default is 30s — large tool payloads may need 60+ |
| **stdio server exits** | Check command path and args. Run the command manually to verify it stays alive |
| **Auth header not sent** | Use env var syntax `${VAR}` in config — Hermes expands at connection time |

## Verification

```bash
# List connected MCP servers
hermes mcp list

# Test a specific server connection
hermes mcp test corpusiq-mcp

# List all tools from all connected servers
hermes tools list | grep mcp

# Check native-mcp skill is loaded
hermes skills list | grep native-mcp
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 17 Discovery](/hermes/skills/marketplace/new-june17-2026/) →*
*Powered by CorpusIQ*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
