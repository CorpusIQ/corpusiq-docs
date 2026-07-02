---
title: "bb-browser-openclaw — Setup Guide"
description: "Full setup guide for bb-browser-openclaw: integrate Blackbox Browser (5,931⭐) with OpenClaw/Hermes agents for Chrome automation with real login state."
---

# bb-browser-openclaw — Setup Guide

**Skill:** `bb-browser-openclaw` | **Installs:** 584 | **Source:** [epiral/bb-browser](https://github.com/epiral/bb-browser) — 5,931⭐

OpenClaw wrapper for **Blackbox Browser** — one of the most popular AI-browser tools. Lets Hermes/OpenClaw agents control Chrome with your existing cookies, sessions, and login state. No headless-mode restrictions.

---

## 1. Prerequisites

- **OpenClaw or Hermes Agent** running with skills.sh support
- **Node.js 18+** (for `npx skills` installation)
- **Chrome/Chromium** installed locally
- **Blackbox Browser** MCP server (included in skill install)

---

## 2. Quick Install

```bash
# Install via skills.sh (recommended)
npx skills add epiral/bb-browser --skill bb-browser-openclaw

# Verify installation
npx skills list | grep bb-browser
```

The skill installs both the OpenClaw skill wrapper AND the Blackbox Browser MCP server dependency.

---

## 3. Configuration

### 3.1. Start Blackbox Browser MCP Server

```bash
# Start the MCP server (runs on localhost:7331 by default)
npx bb-browser serve

# Or with custom port
npx bb-browser serve --port 7332
```

### 3.2. Connect OpenClaw/Hermes

Add to your agent configuration:

```yaml
# ~/.openclaw/config.yaml or equivalent
mcp_servers:
  bb-browser:
    command: "npx"
    args: ["bb-browser", "serve"]
    env:
      CHROME_PATH: "/usr/bin/google-chrome"  # Optional: explicit Chrome path
```

### 3.3. MCP Tools Provided

Once connected, your agent gains these browser-control tools:

| Tool | Description |
|---|---|
| `browser_navigate` | Navigate to URL |
| `browser_click` | Click element by selector/text |
| `browser_type` | Type into input fields |
| `browser_snapshot` | Capture page state as text |
| `browser_screenshot` | Take visual screenshot |
| `browser_evaluate` | Run JavaScript in page context |
| `browser_tabs` | List/manage open tabs |

---

## 4. Key Capabilities

### 4.1. Real Login State

Unlike Playwright/Puppeteer, Blackbox Browser uses your **actual Chrome profile** — all cookies, sessions, and login states are preserved. Agents can:

- Access authenticated dashboards without re-authentication
- Interact with sites that block headless browsers
- Use saved passwords from your Chrome profile

### 4.2. MCP-Native Architecture

The skill wraps the MCP server, so Hermes/OpenClaw agents discover browser tools automatically — no custom tool registration needed.

### 4.3. Text-First Snapshots

`browser_snapshot` returns structured accessibility-tree text (not raw HTML), optimized for LLM context windows. This is how the 5,931-star project achieved efficiency — agents get what they need without raw DOM bloat.

---

## 5. CorpusIQ Use Cases

| Scenario | Tools Used |
|---|---|
| **Social media monitoring** — Agent checks X/Reddit dashboards with login state | `browser_navigate` + `browser_snapshot` |
| **E-commerce competitor analysis** — Agent browses Shopify/Amazon seller dashboards | `browser_navigate` + `browser_evaluate` |
| **SaaS dashboard health checks** — Agent verifies Stripe/HubSpot dashboards load correctly | `browser_navigate` + `browser_screenshot` |
| **Form autofill automation** — Agent fills GA4/Google Ads setup forms | `browser_type` + `browser_click` |

---

## 6. Troubleshooting

| Symptom | Fix |
|---|---|
| **"Chrome not found"** | Set `CHROME_PATH` environment variable or install Chrome |
| **MCP connection refused** | Verify `npx bb-browser serve` is running on expected port |
| **Site blocks automation** | Blackbox uses real Chrome — most anti-bot measures don't trigger. If blocked, try: `npx bb-browser serve --stealth` |
| **Skills install fails** | Ensure Node.js 18+ and npm are installed; try `npx skills update` first |

---

## 7. Alternatives

| Tool | When to Use |
|---|---|
| **Playwright (native)** | When you need headless, parallel, CI-friendly browser control |
| **browser-use (Python)** | When your agent uses Python and needs autonomous browsing |
| **Hermes Browser Extension** | When you want a side panel, not programmatic control |
| **bb-browser-openclaw (this)** | When you need real Chrome with login state + MCP integration |

---

## CLI Reference

```bash
# Start the server
npx bb-browser serve

# Check version
npx bb-browser --version

# Run with stealth mode (reduces bot detection)
npx bb-browser serve --stealth

# Specify Chrome executable
npx bb-browser serve --chrome /usr/bin/google-chrome-stable
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

---

*Part of the [Hermes Skills Library](/hermes/skills/) — curated by CorpusIQ. Setup guide for `bb-browser-openclaw` from [epiral/bb-browser](https://github.com/epiral/bb-browser). Content remains attributed to original authors.*
