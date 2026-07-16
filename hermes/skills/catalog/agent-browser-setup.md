---
title: Agent Browser — Full Setup Guide for Hermes Agents
description: Install, configure, and use the agent-browser CLI from Vercel Labs. Fast native Rust browser automation for AI agents — 38K+ GitHub stars.
---

# Agent Browser — Setup Guide

**Source:** [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) (38,590⭐)
**Category:** Browser Automation
**Languages:** Rust + Node.js

Fast native Rust CLI for browser automation, purpose-built for AI agents. Uses Chrome for Testing with accessibility-tree-based interaction (snap + refs) plus traditional CSS selectors. No Playwright or Node.js runtime dependency for the daemon.

---

## Installation

```bash
# Global install (recommended)
npm install -g agent-browser
agent-browser install  # Downloads Chrome for Testing (first time only)

# Or via Homebrew (macOS)
brew install agent-browser
agent-browser install

# Or via Cargo (Rust)
cargo install agent-browser
agent-browser install

# Linux: install system dependencies automatically
agent-browser install --with-deps

# Update
agent-browser upgrade
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Chrome** | `agent-browser install` downloads from Chrome for Testing. Existing Chrome/Brave/Playwright/Puppeteer installations detected automatically. |
| **Node.js 24+** | Only needed when building from source |
| **Rust** | Only needed when building from source |
| **Hermes Agent** | Any version — CLI tool, no integration required |

---

## Key Capabilities

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| **Open page** | `agent-browser open <url>` | Launches headless Chrome |
| **Accessibility snapshot** | `agent-browser snapshot` | Returns accessibility tree with refs (@e1, @e2...) |
| **Click by ref** | `agent-browser click @e2` | Ref-based clicking from snapshot |
| **Fill by ref** | `agent-browser fill @e3 "text"` | Fill input fields by ref |
| **Get text** | `agent-browser get text @e1` | Extract text content by ref |
| **Screenshot** | `agent-browser screenshot page.png` | Full-page or viewport screenshots |
| **CSS selectors** | `agent-browser click "#submit"` | Traditional selector support |
| **JavaScript eval** | `agent-browser eval "document.title"` | Execute JS in page context |
| **Daemon mode** | `agent-browser daemon` | Persistent browser session |

### CLI Command Reference

```bash
# Quick start flow
agent-browser open example.com
agent-browser snapshot
agent-browser click @e2
agent-browser fill @e3 "test@example.com"
agent-browser get text @e1
agent-browser screenshot page.png
agent-browser close

# Traditional selectors
agent-browser click "#submit"
agent-browser fill "input[name='email']" "user@test.com"

# JavaScript evaluation
agent-browser eval "document.title"
agent-browser eval "JSON.stringify(window.__NEXT_DATA__)"

# Daemon mode for persistent sessions
agent-browser daemon --port 3000
```

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Web scraping** | Use `snapshot` + `get text` to extract structured data from any site without building selectors |
| **Competitive research** | Open competitor sites, screenshot features, extract pricing data |
| **Social media monitoring** | Automate profile checks, extract follower counts, monitor mentions |
| **Form automation** | Fill and submit lead gen forms, waitlist signups, directory submissions |
| **SEO auditing** | Extract meta tags, check page structure, audit accessibility trees |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| **Chrome not found** | Run `agent-browser install` to download Chrome for Testing |
| **Covering element blocks click** | Dismiss the covering element (consent banner, modal), take fresh snapshot, retry |
| **Linux dependencies missing** | Run `agent-browser install --with-deps` |
| **Snapshot too large** | Use CSS selectors for targeted interaction instead of full accessibility tree |
| **Daemon port in use** | Specify alternate port: `agent-browser daemon --port 3001` |

## Verification

```bash
# Verify installation
agent-browser --version

# Quick functional test
agent-browser open example.com && agent-browser get text @e1 && agent-browser close
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Discovery Page](/hermes/skills/marketplace/new-july16-2026/) →*
*Powered by CorpusIQ*
