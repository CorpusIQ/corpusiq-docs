---
title: Agent Browser MCP Server
description: "Setup and usage guide for Agent Browser MCP Server. Part of the Hermes resource directory. URL: https://github.com/codeChap/mcp-server-agent-browser."
last_updated: 2026-08-12
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/agent-browser-mcp/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]

---

# Agent Browser MCP Server

**URL:** https://github.com/codeChap/mcp-server-agent-browser
**Base:** https://github.com/vercel-labs/agent-browser
**Category:** Browser Automation
**Priority:** LOW

## What It Does for Operators

MCP server wrapping Vercel's agent-browser CLI. Provides browser automation tools for AI agents — navigate pages, click elements, extract content, take screenshots. Useful for web scraping and automation tasks that require JavaScript rendering.

## Installation

```bash
# Requires agent-browser CLI first
npm install -g @vercel/agent-browser
npx mcp-server-agent-browser
```

## Key Tools

| Tool | Description |
|------|-------------|
| `navigate` | Navigate to URL |
| `click` | Click page elements |
| `extract` | Extract page content |
| `screenshot` | Capture page screenshots |
| `execute_js` | Execute JavaScript on page |

## Operator Use Cases

1. **Web scraping** — extract data from JavaScript-heavy sites
2. **Competitive monitoring** — screenshot and analyze competitor pages
3. **Form automation** — fill and submit web forms
4. **Visual testing** — automated screenshot comparison

## CorpusIQ Angle

Overlaps with Playwright-based browser automation. The Vercel agent-browser is lighter weight and cloud-native. For operators already in the Vercel ecosystem, this is a natural fit.

## Limitations

- Requires agent-browser CLI dependency
- Beta quality (July 2026)
- Limited vs. full Playwright/Browserless

---
**Discovered:** July 24, 2026 via mcpservers.org /all page
**Repo:** codechap/mcp-server-agent-browser (wraps vercel-labs/agent-browser)
