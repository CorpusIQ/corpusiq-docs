---
title: "Codex MCP Server Integration — OpenAI Codex CLI via MCP Setup"
description: "129+ installs. Bridge Codex CLI into MCP-compatible editors for AI-powered code analysis, generation, review, and web search. Setup guide for Hermes agents."
---

# Codex MCP Server Integration — Setup Guide

**Source:** [aradotso/mcp-skills](https://skills.sh/aradotso/mcp-skills/codex-mcp-server-integration) (129+ installs)
**Category:** Agent Infrastructure / MCP Integration
**Quality Tier:** 🟡 Beta

Bridges OpenAI's Codex CLI into MCP-compatible editors (Claude Code, Cursor, Hermes Agent) through the Model Context Protocol. Provides AI-powered code analysis, generation, review, and web search capabilities without leaving your editor. Architecture: `Editor → Codex MCP Server → Codex CLI → OpenAI API`.

---

## Installation

```bash
npx skills add aradotso/mcp-skills --skill codex-mcp-server-integration
```

### Step 1: Install Codex CLI

```bash
npm install -g @openai/codex
# Verify: codex --version (0.75.0+ required)
```

### Step 2: Authenticate

```bash
codex login --api-key "$OPENAI_API_KEY"
codex ping  # Verify
```

### Step 3: Install MCP Server

```bash
# Claude Code
claude mcp add codex-cli -- npx -y codex-mcp-server

# Or manual MCP config
# Add to MCP settings file (see below)
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | 18+ |
| **Codex CLI** | v0.75.0+ (`npm install -g @openai/codex`) |
| **OpenAI API Key** | For Codex authentication |
| **MCP-Compatible Editor** | Claude Code, Cursor, or Hermes Agent |

---

## Key Capabilities

### Code Analysis & Generation
Main `codex` tool: ask questions about code, request refactoring, generate new implementations. Supports file context arrays and session resumption for multi-turn conversations.

### Code Review (`review` tool)
Review uncommitted changes, branch diffs, or specific commit ranges. Supports `uncommitted`, `base/head` branch comparison, and commit range modes.

### Web Search (`web_search` tool)
OpenAI-powered web search integrated into the code review flow. Search documentation, find examples, and verify implementation patterns.

### Model Selection
Override model per-request: `o3`, `gpt-4`, `gpt-4-turbo`. Reasoning effort control for o-series models: `low`, `medium`, `high`.

### Sandbox Modes
Control execution boundaries: `read-only` (safe for review), `workspace-write` (needed for generation), or full autonomous (`fullAuto`).

---

## Quick Start

```bash
# Install and configure
npm install -g @openai/codex
codex login --api-key "$OPENAI_API_KEY"
claude mcp add codex-cli -- npx -y codex-mcp-server

# Usage examples (from MCP-compatible editor):
# "Use codex to review my uncommitted changes"
# "Analyze src/auth/login.ts and suggest improvements"
# "Use codex web_search to find React 19 migration docs"
```

### MCP Configuration (Manual)

```json
{
  "mcpServers": {
    "codex-cli": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "codex-mcp-server"],
      "env": {
        "CODEX_MCP_CALLBACK_URI": "http://localhost:8080/mcp-callback"
      }
    }
  }
}
```

---

## Verification

```bash
# Verify Codex CLI
codex --version
codex ping

# Verify MCP server registration
claude mcp list | grep codex

# Test with a simple prompt
codex "explain this: const x = [1,2,3].map(n => n * 2)"
```

---

## Notes

- Codex 0.87+ returns `threadId` for session resumption — enables multi-turn conversations
- Sandbox mode `read-only` is recommended for code review; use `workspace-write` only for generation tasks
- The `review` tool is separate from `codex` — it wraps git diff analysis with AI review
- Requires active Codex CLI authentication — tokens expire and need refresh
- Web search capability depends on Codex CLI provider configuration (requires OpenAI API)

---
