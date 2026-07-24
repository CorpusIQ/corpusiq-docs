---
name: "Argus Testing MCP"
description: "Autonomous QA that tests web and macOS apps like a real engineer — and verifies every bug"
category: "Development"
source: "mcp.so"
discovered: "2026-07-23"
stars: 2
verified: true
repository: "https://github.com/chriswu727/argus"
---

# Argus Testing MCP — Autonomous QA for Web & macOS

Argus is an MCP server that performs autonomous quality assurance testing on web and macOS applications. Unlike scripted test runners, Argus explores apps like a human QA engineer, reports bugs, and verifies each finding.

## What It Does

- **Exploratory testing** — Navigates web and macOS apps organically, discovering edge cases
- **Bug detection** — Identifies visual regressions, broken flows, and unexpected behavior
- **Self-verification** — Every reported bug is independently verified before surfacing
- **Playwright-powered** — Browser testing via Playwright for reliable cross-browser coverage
- **macOS native** — Tests native macOS apps alongside web apps

## Quick Start

```bash
# Install
git clone https://github.com/chriswu727/argus
cd argus
npm install

# Add to Claude Code
claude mcp add argus -- npx tsx src/index.ts

# Or Hermes Agent
hermes mcp add argus -- npx tsx /path/to/argus/src/index.ts
```

**Prerequisites:** Node.js 20+, Playwright browsers installed (`npx playwright install`)

## Key Tools

| Tool | Description |
|------|-------------|
| `start_test_session` | Begin a new QA session targeting a URL or app |
| `explore_page` | Autonomous page exploration with bug detection |
| `report_bug` | File a structured bug report with reproduction steps |
| `verify_fix` | Re-test a previously reported bug to confirm resolution |
| `get_coverage` | View which flows/pages have been tested |
| `run_regression` | Run regression suite against known flows |

## Use Cases

- **Pre-release QA** — Run Argus against staging before every deployment
- **Continuous testing** — Agent triggers Argus on new PRs to catch regressions early
- **Cross-browser testing** — Test across Chromium, Firefox, and WebKit in one session
- **Accessibility auditing** — Detect a11y issues during exploratory testing

## Hermes Agent Integration

```python
# Agent triggers QA on a new feature
result = mcp_argus_start_test_session(
    target_url="https://staging.corpusiq.io/dashboard",
    test_depth="deep",
    browser="chromium"
)
# Review bugs found
bugs = mcp_argus_report_bug(session_id=result.session_id)
```

---

*Discovered via [mcp.so](https://mcp.so) sweep. Listed in the [CorpusIQ MCP Catalog](https://corpusiq-docs/hermes/mcp/).*
