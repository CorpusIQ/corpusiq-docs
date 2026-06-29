---
title: Safari Web Agent — Native macOS Browser Automation Setup Guide
description: Install and configure safari-web-agent for real Safari browser automation using native macOS CGEvent. Anti-bot bypass, login session persistence, works where Playwright fails. Hermes + Claude Code.
---

# Safari Web Agent — Setup Guide

**Source:** [treyxu23/safari-web-agent](https://github.com/treyxu23/safari-web-agent) · 1★
**Category:** Agent Infrastructure / Browser Automation
**Platform:** macOS only
**License:** MIT · **Published:** June 28, 2026

Safari Web Agent solves the browser automation anti-bot problem by using your **real Safari browser** — not a headless Chromium instance. Native macOS CGEvent (Core Graphics) sends actual clicks and keystrokes, so websites see a real user with your login sessions, cookies, and fingerprint. Works on sites where Playwright, Puppeteer, and Selenium get detected and blocked.

---

## Why Safari Instead of Playwright?

| Problem with Playwright | Safari Web Agent Solution |
|------------------------|--------------------------|
| Detected as bot | Real Safari — indistinguishable from human |
| No existing login sessions | Uses your logged-in Safari with all cookies |
| CAPTCHA triggers | Native CGEvent bypasses automated input detection |
| Cloudflare/WAF blocks | Real browser fingerprint passes all checks |
| macOS-specific workflows | Native AppleScript + CGEvent integration |

---

## Installation

```bash
npx skills add treyxu23/safari-web-agent
```

### Prerequisites

| Requirement | Details |
|-------------|---------|
| **macOS** | macOS 14+ (Sonoma or later) |
| **Safari** | Safari 17+ with "Allow Remote Automation" enabled |
| **Accessibility permissions** | Terminal/Hermes needs Accessibility access (System Settings → Privacy) |
| **Hermes Agent** | v0.16.0+ running on macOS |

### macOS Permissions Setup

```bash
# Enable Safari remote automation
# Safari → Settings → Advanced → "Show features for web developers"
# Safari → Develop → "Allow Remote Automation"

# Grant Accessibility permission to Terminal
# System Settings → Privacy & Security → Accessibility → enable Terminal
```

---

## Usage with Hermes Agent

### Basic Navigation

```
"Open Safari and go to app.corpusiq.io/dashboard"
"Log into Stripe dashboard in Safari and download the monthly report"
"Check my Shopify orders page in Safari"
```

### Advanced Automation

```
"Open Safari, navigate to Twitter/X, scroll through my timeline, and screenshot trending topics"
"Log into my bank in Safari and check the last 3 transactions"
"Open Gmail in Safari, search for 'invoice', and extract all attachment filenames"
```

---

## Commands

```bash
# Navigate to URL
osascript -e 'tell application "Safari" to open location "https://example.com"'

# Get current page source
SKILL_DIR/scripts/get-source.sh

# Take screenshot
SKILL_DIR/scripts/screenshot.sh --output ~/Desktop/page.png

# Execute JavaScript in page
SKILL_DIR/scripts/execute-js.sh --code "document.title"
```

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Competitor research | Browse competitor sites without bot detection |
| SaaS dashboard monitoring | Check real dashboards with your login sessions |
| Social media management | Post, check analytics, engage — as real user |
| E-commerce operations | Monitor store dashboards, extract order data |
| Ad account checks | Verify live ad campaigns without API access |

---

## Limitations

- **macOS only** — No Linux/Windows support
- **Single session** — One Safari window at a time
- **Visible browser** — Safari must be open (not headless)
- **Permission prompts** — First run requires user to grant Accessibility access
- **Speed** — Slower than headless browsers (real UI events have natural delays)

---

*This guide is part of the [Hermes Skills Catalog](/hermes/skills/catalog/). Discovered June 29, 2026. Powered by CorpusIQ.*
