---
name: "Moxie Docs MCP Server Setup Guide"
title: "Moxie Docs MCP Server Setup Guide"
description: "GitHub personal access token with repo scope is required for PR workflows. Setup guide for the Moxie Docs MCP server."
category: "Developer Tools"
source: "mcp.so"
discovered: "2026-07-23"
stars: 1
verified: true
repository: "Jackalope-Dev/moxie-docs (repo no longer public)"
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/moxie-docs-mcp/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

> **Upstream status (2026-10-31):** `Jackalope-Dev/moxie-docs` is no longer available. GitHub returns 404 and the repository cannot be cloned; the commands below are kept as published and will fail until the project reappears.

# Moxie Docs MCP - Automated Codebase Documentation

Moxie Docs generates and maintains searchable documentation for GitHub repositories, provides MCP context to AI coding agents, detects documentation drift, and creates automated Friday Cleanup PRs.

## What It Does

- **Auto-generate docs** - Scans your codebase and produces structured documentation
- **MCP context** - Feeds up-to-date codebase knowledge into AI agents via MCP tools
- **Drift detection** - Alerts when code changes make documentation stale
- **Cleanup PRs** - Automated Friday PRs to fix broken links, outdated examples, and formatting

## Quick Start

```bash
# Install
git clone https://github.com/Jackalope-Dev/moxie-docs
cd moxie-docs
npm install

# Add to Claude Code
claude mcp add moxie-docs -- npx tsx src/index.ts

# Or Hermes Agent
hermes mcp add moxie-docs -- npx tsx /path/to/moxie-docs/src/index.ts
```

**Prerequisites:** Node.js 20+, GitHub repo access

## Key Tools

| Tool | Description |
|------|-------------|
| `generate_docs` | Scan repo and generate structured docs |
| `search_docs` | Full-text search across documentation |
| `check_drift` | Identify stale docs vs current code |
| `get_context` | Pull relevant docs for AI agent context |
| `create_cleanup_pr` | Generate Friday Cleanup PR |
| `get_doc_coverage` | Report on documentation coverage by file/module |

## Use Cases

- **Onboarding acceleration** - New developers ask the agent "how does the auth system work?" and get accurate, current docs
- **CI/CD integration** - Run `check_drift` in CI to block PRs that break documentation
- **Agent context** - AI coding agents pull Moxie Docs context instead of guessing at codebase architecture
- **Documentation maintenance** - Friday Cleanup PRs keep docs fresh without manual effort

## Hermes Agent Integration

```python
# Agent checks if docs are current before making changes
context = mcp_moxiedocs_get_context(query="authentication middleware")
drift = mcp_moxiedocs_check_drift()
if drift.stale_files:
    print(f"Warning: {len(drift.stale_files)} files have outdated docs")
```

---

*Discovered via [mcp.so](https://mcp.so) sweep. Listed in the [CorpusIQ MCP Catalog](https://corpusiq-docs/hermes/mcp/).*
