---
title: Moxie Docs MCP Server
subtitle: Automated codebase documentation with MCP context for AI agents
source: mcp.so
github: https://github.com/Jackalope-Dev/moxie-docs
created: 2026-07-21
category: Documentation
stars: 1
tags: [documentation, github, codebase, drift-detection, developer-tools]
---

# Moxie Docs MCP Server

MCP server for **automated codebase documentation on GitHub**. Generates searchable docs, provides MCP context for AI agents working on your codebase, detects documentation drift, and files Friday Cleanup PRs.

## What It Does

- **Auto-Documentation** — Generate docs from your codebase structure, APIs, and types
- **MCP Context** — Feeds generated docs as context to AI coding agents
- **Drift Detection** — Catch when code changes but docs don't
- **Cleanup PRs** — Automated Friday PRs fixing documentation gaps

## Business Operator Use Cases

| Use Case | Value |
|----------|-------|
| **Onboarding Acceleration** | New developers get instant AI-assisted context from auto-generated docs |
| **Documentation Hygiene** | "Show me all endpoints with outdated docs" → automated cleanup PR |
| **Agent-Assisted Development** | Coding agents understand your codebase from generated docs, not just raw code |
| **Technical SEO** | Searchable API docs improve developer discovery and integration |

## Installation

```bash
git clone https://github.com/Jackalope-Dev/moxie-docs
cd moxie-docs
npm install
```

## Configuration

Add to your MCP client config:

```json
{
  "mcpServers": {
    "moxie-docs": {
      "command": "node",
      "args": ["path/to/moxie-docs/index.js"],
      "env": {
        "GITHUB_TOKEN": "your-github-token",
        "GITHUB_REPO": "owner/repo",
        "MOXIE_OUTPUT_DIR": "./docs"
      }
    }
  }
}
```

## Auth

GitHub personal access token with repo scope required for PR creation and repository access.

## Tools Provided

- `generate_docs` — Analyze codebase and generate documentation
- `check_drift` — Detect code changes without corresponding doc updates
- `create_cleanup_pr` — File automated PR with documentation fixes
- `get_context` — Return MCP context for AI coding agents
- `search_docs` — Full-text search across generated documentation

## Limitations

- **1 star, brand new** — Created July 21, 2026. Early stage.
- **GitHub only** — No GitLab/Bitbucket support yet.
- **Language support unclear** — Unknown which languages are supported for doc generation.
- **PR quality may vary** — Automated cleanup PRs may need human review.

## Operator Verdict

★★ **Useful for teams growing their documentation culture.** The drift detection + automated cleanup PR pattern is smart — it lowers the activation energy for keeping docs current. For teams with >2 developers and a monorepo, this could meaningfully reduce the "undocumented feature" problem. Watch for multi-platform support.
