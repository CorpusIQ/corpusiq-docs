---
title: MCP Integration — Connect MCP servers to agent plugins for Hermes Agents
description: Comprehensive guide for integrating Model Context Protocol servers into Claude Code plugins. 78+ installs from anthropics/claude-plugins-public.
---

# MCP Integration — Setup Guide

**Source:** [anthropics/claude-plugins-public](https://skills.sh/anthropics/claude-plugins-public/mcp-integration) (78+ installs)
**Category:** Engineering / MCP
**Quality Tier:** 🔵 Community

Comprehensive reference for integrating Model Context Protocol (MCP) servers into agent plugins. Covers all four server types (stdio, SSE, HTTP, WebSocket), authentication patterns (OAuth, token-based, environment variables), and plugin integration patterns.

---

## Installation

```bash
npx skills add anthropics/claude-plugins-public --skill mcp-integration
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Claude Code** | Plugin-capable agent host |
| **MCP server** | Running MCP server (local or remote) |
| **.mcp.json** | Plugin root MCP configuration file |

---

## Key Capabilities

### Four MCP Server Types
- **stdio**: Local process MCP servers (npx, python, custom binaries)
- **SSE**: Hosted servers with OAuth (Asana, GitHub MCP endpoints)
- **HTTP**: REST API-based MCP with token authentication
- **WebSocket**: Real-time bidirectional MCP connections

### Authentication Patterns
OAuth flow automation, token-based headers, environment variable injection, and `${CLAUDE_PLUGIN_ROOT}` path expansion for portability.

### Integration Patterns
Simple tool wrappers, autonomous multi-step agents, and multi-server plugin configurations spanning multiple services.

---

## Quick Start

**Dedicated `.mcp.json` (Recommended):**

```json
{
  "database-tools": {
    "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
    "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
    "env": {
      "DB_URL": "${DB_URL}"
    }
  }
}
```

**SSE with OAuth:**

```json
{
  "asana": {
    "type": "sse",
    "url": "https://mcp.asana.com/sse"
  }
}
```

---

## Verification

```bash
# Check skill installed
npx skills list | grep mcp-integration

# Verify MCP server appears (in Claude Code)
/mcp
```

---

## Notes

- Tool naming convention: `mcp__plugin_<name>_<server>__<tool>`
- Always use `${CLAUDE_PLUGIN_ROOT}` for portable paths — never hardcode absolute paths
- Pre-allow specific MCP tools rather than wildcards for security
- Use HTTPS/WSS only — never HTTP/WS for production
- Documentation covers lifecycle management, error handling, debugging, and performance best practices
- Complements `aradotso/mcp-skills@codex-mcp-server-integration` (129 installs) for Codex-specific MCP workflows
