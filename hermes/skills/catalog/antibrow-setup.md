---
title: Anti-Detect Browser — Undetectable Playwright Browsers for Hermes Agents
description: Launch Chromium instances with real-device fingerprints via standard Playwright APIs. 29.9K+ installs. Anti-detect browser profiles with MCP server mode for AI agent automation, web scraping, and multi-account management.
---

# Anti-Detect Browser — Setup Guide

**Source:** [antibrow/anti-detect-browser-skills](https://skills.sh/antibrow/anti-detect-browser-skills) (29.9K+ installs)
**Category:** Browser Automation / Anti-Detection
**Quality Tier:** 🟢 Production

Anti-Detect Browser SDK lets Hermes agents launch Chromium instances with unique real-device fingerprints — undetectable by anti-bot systems. Each browser gets a persistent digital identity with 500+ fingerprint parameters across 30+ categories (Canvas, WebGL, Audio, Fonts, WebRTC, WebGPU). Standard Playwright APIs mean zero learning curve. MCP server mode enables direct AI agent control.

Critical for operations blocked by anti-bot walls: Instagram, TikTok, Reddit, LinkedIn scraping, and any site using Cloudflare/Datadome/PerimeterX.

---

## Installation

```bash
npm install anti-detect-browser
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **API Key** | Sign up at [antibrow.com](https://antibrow.com) (free tier: 2 profiles) |
| **Node.js** | 18+ |
| **Playwright** | Already installed in most Hermes setups |

---

## Key Capabilities

### Real-Device Fingerprints
Each launch fetches a real fingerprint collected from actual devices. Filter by OS, browser, device type:

```typescript
import { AntiDetectBrowser } from 'anti-detect-browser'
const ab = new AntiDetectBrowser({ key: 'your-api-key' })

// Windows Chrome
const { page } = await ab.launch({
  fingerprint: { tags: ['Windows 10', 'Chrome'], minBrowserVersion: 130 },
})

// Mac Safari
await ab.launch({ fingerprint: { tags: ['Apple Mac', 'Safari'] } })

// Mobile Android
await ab.launch({ fingerprint: { tags: ['Android', 'Mobile', 'Chrome'] } })
```

Available tags: `Microsoft Windows`, `Apple Mac`, `Android`, `Linux`, `iPad`, `iPhone`, `Edge`, `Chrome`, `Safari`, `Firefox`, `Desktop`, `Mobile`.

### Persistent Profiles
Profiles save cookies, localStorage, and session data across launches — stay logged in between sessions:

```typescript
// First launch — log in
const { page } = await ab.launch({ profile: 'shop-01' })
await page.goto('https://shop.example.com/login')
await browser.close()

// Later — session restored
const { page: p2 } = await ab.launch({ profile: 'shop-01' })
await p2.goto('https://shop.example.com/dashboard') // already logged in
```

### Proxy Integration
Route each browser through a different proxy for geo-targeting or IP rotation:

```typescript
await ab.launch({
  proxy: 'socks5://user:pass@us-proxy.example.com:1080',
  fingerprint: { tags: ['Windows 10', 'Chrome'] },
  profile: 'us-account',
})
```

### MCP Server Mode — AI Agent Control
Expose anti-detect browsers as MCP tools so Hermes can launch, navigate, and interact through tool calls:

```bash
npx anti-detect-browser serve
```

### Inject Into Existing Playwright
Add fingerprints without changing your workflow:

```typescript
import { applyFingerprint } from 'anti-detect-browser'
const context = await browser.newContext()
await applyFingerprint(context, {
  key: 'your-api-key',
  fingerprint: { tags: ['Windows 10', 'Chrome'] },
  profile: 'my-profile',
})
```

### Live View
Monitor headless sessions from the dashboard — useful for debugging AI agent actions:

```typescript
const { liveView } = await ab.launch({
  headless: true,
  liveView: true,
})
console.log('Watch live:', liveView.viewUrl)
```

---

## Quick Start — Hermes Agent

```bash
# Install
npm install anti-detect-browser

# Create a profile for Instagram (example)
node -e "
const { AntiDetectBrowser } = require('anti-detect-browser');
const ab = new AntiDetectBrowser({ key: process.env.ANTIBROW_KEY });
(async () => {
  const { page } = await ab.launch({
    fingerprint: { tags: ['Windows 10', 'Chrome'] },
    profile: 'instagram-corpusiq',
  });
  await page.goto('https://instagram.com');
  console.log('Ready — fingerprint:', await page.evaluate(() => navigator.userAgent));
  await page.screenshot({ path: '/tmp/ig-screenshot.png' });
  await page.context().browser().close();
})();
"
```

---

## Verification

```bash
# Check package installed
npm ls anti-detect-browser

# Test API key
curl -s "https://antibrow.com/api/v1/profiles" -H "Authorization: Bearer $ANTIBROW_KEY"
```

---

## Notes

- **Free tier**: 2 browser profiles — sufficient for testing before committing
- **Undetectable**: 500+ fingerprint parameters, real device data from the cloud — no synthetic fingerprints
- **Use case for CorpusIQ**: Bypass Instagram/TikTok anti-bot walls, Reddit scraping, LinkedIn prospect research
- **MCP integration**: Pairs with Hermes's native MCP client for autonomous browser operations
- **Related skills**: [browser-use-automation](browser-use-automation), [browser-act-setup](browser-act-setup.md), [browser-harness-setup](browser-harness-setup)
