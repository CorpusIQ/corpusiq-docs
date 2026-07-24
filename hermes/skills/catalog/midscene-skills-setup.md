---
title: Midscene — AI-Powered Visual Browser Automation for Hermes Agents
description: Configure Midscene (14K+ GitHub stars) for vision-driven UI automation — browser-use, computer-use, and phone-use with natural language commands. Works with Hermes for web testing, scraping, and autonomous interaction.
---

# Midscene Skills — Setup Guide

**Source:** [web-infra-dev/midscene-skills](https://skills.sh/web-infra-dev/midscene-skills) (6K+ combined installs)
**GitHub:** [web-infra-dev/midscene](https://github.com/web-infra-dev/midscene) — 14,183 ★ | JavaScript
**Category:** Automation / Browser-Use
**Quality Tier:** 🟢 Production (14K+ GitHub stars, active development)

Midscene is an AI-powered, vision-driven UI automation framework that works across web browsers, desktop applications, and mobile devices. Instead of brittle CSS selectors or XPath, Midscene uses visual AI to locate and interact with UI elements — making it resilient to DOM changes and ideal for autonomous Hermes agents that need reliable browser automation.

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add web-infra-dev/midscene-skills --skill browser-automation --yes
npx skills add web-infra-dev/midscene-skills --skill computer-automation --yes
npx skills add web-infra-dev/midscene-skills --skill vitest-midscene-e2e --yes
```

### Via npm

```bash
npm install -g @midscene/web
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **harmonyos-device-automation** | 1.8K | HarmonyOS device automation |
| **vitest-midscene-e2e** | 1.6K | E2E testing with Vitest + Midscene |
| **computer-automation** | 1.4K | Desktop computer UI automation |
| **browser-automation** | 456 | Browser interaction via natural language |
| **desktop-computer-automation** | 443 | Full desktop automation workflows |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | 18+ |
| **Chrome/Chromium** | For browser automation (Puppeteer downloads its own by default) |
| **API Key** | `MIDSCENE_MODEL_API_KEY` in `.env` for vision model |
| **Display** | Required for computer-use mode (desktop automation) |

---

## Key Capabilities

### 1. Natural Language Browser Control

```bash
# Fill forms and click buttons with plain English
npx -y @midscene/web@1 act --prompt "fill in the email field with 'user@example.com' and click Log In"

# Navigate complex multi-step workflows
npx -y @midscene/web@1 act --prompt "complete the multi-step checkout form"
```

### 2. Visual Element Location

Instead of brittle selectors, Midscene "sees" the page:

```bash
# Click a specific visual element
npx -y @midscene/web@1 tap --locate "the gear icon in the top-right toolbar"

# Take screenshots for verification
npx -y @midscene/web@1 take_screenshot
```

### 3. Precision Modes

Two flags for complex scenarios:

- `--deep-locate` — extra visual reasoning to pinpoint elements (fixes location drift)
- `--deep-think` — deeper planning for complex multi-step instructions

```bash
# Combine both for challenging pages
npx -y @midscene/web@1 act --deep-locate --deep-think \
  --prompt "open settings, go to Preferences, enable dark mode"
```

### 4. Cross-Platform

- **Browser**: Chrome/Chromium via CDP (Chrome DevTools Protocol) or Bridge mode
- **Desktop**: Native desktop UI automation via computer-use
- **Mobile**: HarmonyOS and mobile device automation

---

## Quick Start

```bash
# 1. Install
npm install -g @midscene/web

# 2. Set API key
export MIDSCENE_MODEL_API_KEY="your-key-here"

# 3. Navigate and interact
npx -y @midscene/web@1 act --prompt "go to google.com and search for 'Hermes agent framework'"

# 4. Take a screenshot to verify
npx -y @midscene/web@1 take_screenshot

# 5. Run browser in CDP mode (more stable)
npx -y @midscene/web@1 act --cdp --prompt "log into the dashboard"
```

---

## Verification

```bash
# Check installation
npx @midscene/web --version

# Verify skills.sh install
npx skills list | grep midscene

# Quick smoke test
npx -y @midscene/web@1 act --prompt "navigate to example.com"
```

---

## Troubleshooting

| Issue | Fix |
|---|---|
| Connection failure | Ensure Chrome/Chromium installed; check firewall isn't blocking debugging ports |
| API key errors | Verify `MIDSCENE_MODEL_API_KEY` in `.env` is valid |
| Timeouts | Take screenshot first to verify page loaded; add waits between steps |
| Screenshots not displaying | Path is absolute local file — use Read tool to view |
| Version mismatch | `npm ls @midscene/web @midscene/core @midscene/shared` → `npm i @midscene/web@latest` |

---

## Hermes Integration Notes

- Midscene's vision-based approach complements Hermes' existing Playwright/browser-use tools
- Use `--deep-locate` for pages where Hermes' CSS selectors fail due to dynamic DOM
- Bridge mode allows connecting to already-running browser instances
- E2E testing with Vitest enables Hermes to validate its own web automation workflows

---

## Notes

- **Production-grade**: 14K GitHub stars, actively maintained by web-infra-dev team
- **Vision-first**: No CSS selectors needed — Midscene sees the UI like a human
- **Best for**: Dynamic SPAs, complex forms, sites with frequent DOM changes
- **Complementary**: Use alongside Hermes' native browser tools — Midscene for visual tasks, Playwright for API-level control
- **Related**: See [Browser-Use Automation](/hermes/skills/catalog/browser-use-automation-setup/) and [Playwright Social Media](/hermes/skills/catalog/playwright-social-media-automation-setup/)
