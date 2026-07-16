---
title: "Periscope MCP — Playwright-Powered Website Testing"
description: "63 Playwright-powered testing tools with agent-first ergonomics. Browser automation, screenshots, visual regression, accessibility checks, and assertions — all from AI agents. Built for CI/CD integration."
category: mcp
tags: [mcp-server, testing, playwright, browser-automation, qa, web-testing, ci-cd, developer-tools]
last_updated: 2026-07-08
---

# Periscope MCP Server ★ New (July 2 PM)

## Overview

Periscope MCP (`segentic-lab/periscope-mcp`) delivers 63 Playwright-powered website testing tools designed specifically for AI agents. Unlike general browser automation MCPs, Periscope is built with agent-first ergonomics — each tool is a discrete testing action (navigate, assert, screenshot, check accessibility, measure performance) that composes cleanly into AI-driven test workflows. Development and QA teams can write, run, and debug end-to-end tests through natural language, with results structured for AI consumption.

**Key advantage**: 63 purpose-built testing tools, agent-first design, Playwright-backed reliability — testing that works the way AI agents think.

## Key Features

- **Browser navigation**: Navigate to URLs, click elements, fill forms, scroll, wait for conditions
- **Screenshots & visual regression**: Capture full-page and element screenshots; compare against baselines for visual regression detection
- **Assertions**: Assert element visibility, text content, attributes, CSS properties, and page state
- **Accessibility checks**: Run axe-core accessibility audits, flag WCAG violations
- **Performance metrics**: Capture Core Web Vitals (LCP, CLS, INP), page load timings, and resource waterfall
- **Network monitoring**: Intercept and inspect network requests, mock API responses, validate API calls
- **CI/CD ready**: Structured JSON output for test runners, GitHub Actions, and CI pipelines
- **Agent-first ergonomics**: Each tool returns structured, parseable results — no parsing raw HTML or console output

## Installation

```bash
# Requires Playwright browsers
npx playwright install

# Clone and install
git clone https://github.com/segentic-lab/periscope-mcp.git
cd periscope-mcp
npm install
npm run build

# Add to Hermes
hermes mcp add periscope --command "node" --args "dist/index.js" --workdir "$(pwd)"
```

## Configuration

```json
{
  "mcpServers": {
    "periscope": {
      "command": "node",
      "args": ["dist/index.js"],
      "workdir": "/path/to/periscope-mcp",
      "env": {
        "BASE_URL": "https://staging.example.com",
        "HEADLESS": "true",
        "SCREENSHOT_DIR": "./screenshots"
      }
    }
  }
}
```

## Business Relevance

- **QA Automation**: QA teams can write and execute test suites through natural language — "test the checkout flow on mobile viewport and flag any layout issues" — without writing Playwright scripts
- **Visual Regression**: Automatically detect visual regressions after deployments — screenshot comparison with pixel-diff reporting
- **Accessibility Compliance**: Run WCAG audits as part of CI/CD — catch accessibility regressions before they reach production
- **Pre-release Validation**: AI agents can run a full test battery before every release — login flow, critical paths, form validation, mobile responsiveness
- **Competitive Monitoring**: Schedule automated checks on competitor websites — feature changes, pricing updates, UX modifications

## Integration with CorpusIQ

Periscope MCP strengthens CorpusIQ's development and QA toolchain, complementing existing testing infrastructure:

- **CI/CD Pipeline**: Combine Periscope's browser testing with Drumbeats MCP for monitoring — "if deployment succeeds, run Periscope smoke tests, then update Drumbeats status page"
- **Pre-flight Testing**: Integrate with CorpusIQ's pre-flight gate — before publishing content or deploying changes, run Periscope checks on the affected pages
- **Competitive Intelligence**: Pair with SEO tools (SE Ranking, OpenSEO) — Periscope captures visual/functional competitor changes while SEO tools track ranking shifts
- **Agent Workflows**: AI agents can orchestrate end-to-end validation — database query (dbridge) → API check (Bruno) → browser test (Periscope) → deploy (Cloudflare)

## Limitations

- Requires Playwright browser binaries (Chromium, Firefox, WebKit) — ~500MB disk space
- Self-hosted — runs locally, not a cloud service
- Chromium-based rendering may differ from real device browsers
- Visual regression sensitive to anti-aliasing and font rendering differences across OS

## See Also

- [Playwright MCP — Official Microsoft](/hermes/mcp/servers/external/)
- [Drumbeats MCP — Uptime Monitoring](/hermes/mcp/servers/external/drumbeats-mcp/)
- [QA Skills — Test Automation Toolkit](/hermes/mcp/servers/external/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
