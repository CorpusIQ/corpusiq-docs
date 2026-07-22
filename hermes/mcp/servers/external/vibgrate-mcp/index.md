---
title: "Vibgrate MCP — Integration Guide"
description: "Connect AI agents to Vibgrate Cloud for dependency drift, vulnerability (CVE), and migration intelligence. 51 tools for DriftScores, EOL runtimes, upgrade paths, and org catalog management."
category: mcp
tags: [mcp-server, devops, security, drift-detection, cve, dependency-management]
last_updated: 2026-07-18
---

# Vibgrate MCP — Integration Guide

**Source:** mcp.so listing  
**Author:** Vibgrate  
**License:** Apache-2.0  
**Endpoint:** `https://mcp.vibgrate.com`  
**Docs:** [vibgrate.com/mcp](https://vibgrate.com/mcp)  
**Trust & Security:** [vibgrate.com/mcp-trust](https://vibgrate.com/mcp-trust)

## What It Does

Vibgrate MCP connects your AI agents (Cursor, Claude, ChatGPT, Windsurf, VS Code) directly to Vibgrate Cloud — giving them 51 tools across 14 groups to query your team's software supply chain health:

- **DriftScores** — quantify how far your dependencies have drifted from their ideal versions
- **CVE scanning** — check for known vulnerabilities in your dependency tree
- **EOL runtime detection** — flag end-of-life runtimes and libraries before they become security risks
- **Upgrade path analysis** — calculate the blast radius of proposed dependency upgrades
- **Organization catalog management** — manage your team's software inventory across repos
- **Reports** — generate compliance and health reports on demand

Source code never leaves your environment. The MCP server exposes only metadata collected by the Vibgrate CLI (`vg`).

**Scopes:** `vibgrate:read` / `vibgrate:write`, selected per workspace at OAuth consent.

## Setup

### Prerequisites

- A Vibgrate account at [vibgrate.com](https://vibgrate.com)
- The Vibgrate CLI installed in your repos (`npx @vibgrate/cli serve`)

### MCP Client Configuration

Add this to your MCP client's server configuration:

```json
{
  "mcpServers": {
    "vibgrate": {
      "url": "https://mcp.vibgrate.com"
    }
  }
}
```

For Claude Code:
```bash
claude mcp add vibgrate https://mcp.vibgrate.com
```

### OAuth Flow

On first connection, your MCP client will open a browser for OAuth 2.1 authorization. You select:
- Which workspace(s) to grant access to
- `vibgrate:read` for query-only access (recommended for AI agents)
- `vibgrate:write` for report generation and catalog management

Tokens are scoped and revocable from the Vibgrate dashboard.

## Local Companion: Vibgrate AI Context

The same package includes `vg serve` — a local-first companion that runs on your machine:

```bash
npx @vibgrate/cli serve
```

This provides:
- Version-correct library documentation
- A deterministic code map of your repository
- Offline drift reporting (no cloud connection needed)

Use this when you want AI agents to have context about your codebase without sending anything to the cloud.

## Use Cases for Business Operators

- **Security audits:** Ask your AI agent "Are there any CVEs in our production dependencies?" and get an instant answer backed by live data
- **Migration planning:** Before upgrading a major framework, ask "What's the blast radius of upgrading React to v20?" and see every affected file
- **Compliance reporting:** Generate dependency health reports for SOC2, ISO 27001, or internal audits
- **Team onboarding:** New developers can ask "What version of TypeScript are we on and why?" and get context-aware answers

## Operator Relevance

Vibgrate MCP is relevant for any business operator managing production software — startups, agencies, and enterprise teams alike. It turns the tedious work of tracking dependency drift and CVEs into a conversational workflow. Instead of running scanners and reading reports, operators can ask their AI assistant directly.

## See Also

- External MCP Server Catalog(/hermes/mcp/servers/external/)
- Shieldly AWS MCP(/hermes/mcp/servers/external/shieldly-aws-mcp/) — AWS security analysis via MCP
