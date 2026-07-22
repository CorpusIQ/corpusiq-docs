---
title: "SignWell MCP — Official E-Signature Server for AI Agents"
description: "Official SignWell MCP server — the first major e-signature platform with native MCP support. Create, send, and track legally binding documents from any MCP-compatible agent. Full API access with template management and status tracking."
category: mcp
tags: [mcp-server, e-signature, signwell, official, workplace, productivity, contracts, legal]
last_updated: 2026-07-19
---

# SignWell MCP Server ★ Official

The first major e-signature platform to ship an official MCP server. SignWell lets any MCP-compatible AI agent (Claude, Codex, Cursor, Hermes) create signature requests from templates, send documents for signing, check signing status, and manage the complete e-signature workflow — all without leaving the agent interface.

**Source:** mcpservers.org via awesome-mcp-servers PR #9513 (discovered July 19, 2026)
**Category:** Workplace & Productivity / E-Signature / Legal
**Author:** SignWell (Official) / Bidsketch
**Repo:** https://github.com/Bidsketch/signwell-mcp
**Docs:** https://www.signwell.com
**Status:** Active

## Why This Matters for Operators

E-signature is a daily workflow for business operators — vendor agreements, client contracts, NDAs, employment letters. Every one of these follows a repeatable pattern: pick a template, fill in variables, send, track. The SignWell MCP server automates this end-to-end from within your AI agent, eliminating the context-switch to a separate e-sign dashboard.

## Installation

```bash
# Via npm
npm install -g signwell-mcp

# Or run directly
npx signwell-mcp
```

## Claude Desktop / Hermes Configuration

```json
{
  "mcpServers": {
    "signwell": {
      "command": "npx",
      "args": ["signwell-mcp"],
      "env": {
        "SIGNWELL_API_KEY": "your-api-key"
      }
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `create_document_from_template` | Generate a signature request from a saved template with variable substitution |
| `send_document` | Send a document for e-signature to one or more recipients |
| `get_document_status` | Check signing status (pending, viewed, signed, declined) |
| `list_templates` | Browse available document templates |
| `download_signed_document` | Retrieve the completed, legally binding PDF |

## Authentication

Requires a SignWell API key. Sign up at [signwell.com](https://www.signwell.com). Free tier available for testing.

## CorpusIQ Relevance

E-signature is one of the most requested connectors from CorpusIQ operators. Integrating SignWell alongside existing connectors (QuickBooks, Shopify, HubSpot) would create a complete business operations workflow: CRM deal → contract generation → e-signature → accounting sync — all agent-driven.

## See Also

- [[sweeps/sweep-july19-2026]]
- Setell MCP
- 1Password MCP
