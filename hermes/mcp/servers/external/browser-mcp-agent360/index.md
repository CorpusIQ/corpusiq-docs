---
title: "Agent360 Browser MCP — Real Chrome Automation for AI Agents"
description: "Integration guide for agent360dk/browser-mcp. Drive real logged-in Chrome from AI agents — CAPTCHA solving, Gmail OTP reading, 34 tools. MIT license."
category: mcp
tags: [mcp-server, browser-automation, captcha, chrome, web-scraping, hermes-agent]
last_updated: 2026-07-16
mcp_server: agent360dk/browser-mcp
stars: 22
source: mcpservers.org
---

# Agent360 Browser MCP — Real Chrome Where Headless Dies

**Repository:** [Agent360dk/browser-mcp](https://github.com/Agent360dk/browser-mcp)
**Stars:** 22 ★
**Category:** Browser Automation / Web Tools
**Language:** JavaScript
**License:** MIT
**Last Updated:** July 2026

## What It Does

Browser MCP connects AI agents to a **real, logged-in Chrome browser** — not headless. This means it works on sites that block headless browsers, handles CAPTCHAs, reads 2FA/login codes from Gmail, and maintains authenticated sessions. 34 MCP tools covering navigation, clicking, typing, screenshot, and more. Runs locally (your Chrome, your sessions, your data).

### Key Capabilities

| Capability | Description |
|-----------|-------------|
| **Real Chrome Browser** | Connects to your actual logged-in Chrome — bypasses headless detection |
| **CAPTCHA Solving** | Built-in CAPTCHA handling for sites that challenge automated access |
| **Gmail OTP Reading** | Reads emailed login/2FA codes from your Gmail inbox automatically |
| **34 MCP Tools** | Navigate, click, type, screenshot, scroll, extract text, execute JS |
| **Session Persistence** | Maintains logged-in state across interactions — no re-authentication |
| **Local-First** | Everything runs on your machine — no cloud browser, no proxy service |
| **Element Interaction** | Click by selector, text, or coordinates — flexible targeting |

### Tools Provided (selected)

| Tool | Description |
|------|-------------|
| `navigate` | Open a URL in the browser |
| `click` | Click an element by selector, text, or coordinates |
| `type` | Type text into a focused element |
| `screenshot` | Capture visible viewport or full page |
| `extract` | Extract text, HTML, or structured data from the page |
| `scroll` | Scroll the page up/down |
| `execute_js` | Run arbitrary JavaScript in the page context |
| `wait` | Wait for element to appear or timeout |
| `get_gmail_code` | Read verification/login codes from Gmail |
| `solve_captcha` | Attempt to solve CAPTCHA challenges |
| `get_cookies` | Extract cookies for session transfer |

## Why Business Operators Care

- **Access gated platforms:** Monitor competitors, check listings, verify pricing on sites that block headless browsers
- **Automate authenticated workflows:** Any web app you're logged into becomes an MCP tool — CRM, analytics dashboards, supplier portals
- **No API dependency:** Platforms without APIs (or with expensive APIs) become accessible through browser automation
- **2FA/OTP automation:** Gmail OTP reading eliminates the manual step of checking email for login codes

## Setup for Hermes Agent

### Prerequisites

- Google Chrome installed (not Chromium — real Chrome with Widevine)
- Node.js 18+
- Chrome running with remote debugging enabled

### Step 1: Start Chrome with Debugging

```bash
# Linux
google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-mcp-profile

# macOS
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-mcp-profile

# Login to the sites you want automated (Gmail, CRMs, dashboards)
# Chrome will remember these sessions in the user-data-dir
```

### Step 2: Install Browser MCP

```bash
git clone https://github.com/Agent360dk/browser-mcp.git
cd browser-mcp
npm install
```

### Step 3: MCP Configuration

Add to `~/.hermes/config.yaml`:

```yaml
mcp_servers:
  browser:
    type: stdio
    command: node
    args:
      - /path/to/browser-mcp/server.js
    env:
      CHROME_DEBUG_PORT: "9222"
      GMAIL_REFRESH_TOKEN: "${GMAIL_REFRESH_TOKEN}"  # For OTP reading
```

### Step 4: Gmail OTP Setup (Optional)

For automatic 2FA code reading:

```bash
# Create a Gmail app password (not your main password)
# Google Account → Security → App Passwords

# Store securely
echo "your-gmail-app-password" > ~/.hermes/profiles/corpusiq/secrets/gmail-browser-mcp.token
chmod 600 ~/.hermes/profiles/corpusiq/secrets/gmail-browser-mcp.token
```

## Common Queries via Hermes

Once configured, ask Hermes:

- "Log into our supplier portal and check if order #12345 has shipped"
- "Go to competitor-pricing.com and extract the pricing table for our comparison spreadsheet"
- "Take a screenshot of our Google Analytics dashboard"
- "Check if our product listing is live on the marketplace"
- "Log into our CRM and pull the last 10 deals"

## Comparison: Agent360 Browser MCP vs browser-use vs Playwright

| Feature | Agent360 Browser MCP | browser-use (Python) | Playwright |
|---------|---------------------|----------------------|------------|
| **Browser type** | Real Chrome (non-headless) | Headless with stealth | Headless/headed |
| **CAPTCHA handling** | Built-in | Via plugins | No built-in |
| **Gmail OTP reading** | Built-in | Manual | Not available |
| **Anti-bot bypass** | High (real browser) | Moderate (stealth patches) | Low (detectable) |
| **MCP native** | Yes | No (Python library) | No |
| **Session persistence** | Chrome user profile | Browser context | Browser context |
| **Best for** | Authenticated sites, gated platforms | General web scraping | Testing & automation |

**Verdict:** Agent360 Browser MCP is the go-to for authenticated, anti-bot-protected sites where headless browsers fail. browser-use remains better for general scraping at scale. Playwright is the foundation layer — both tools build on it.

## Security Considerations

⚠️ **This tool runs YOUR Chrome with YOUR logged-in sessions.** The AI agent has full access to any site you're logged into — email, banking, admin panels. Mitigations:

1. **Use a dedicated Chrome profile** (separate `--user-data-dir`) — don't use your daily browsing profile
2. **Log in only to the specific sites needed** for the task, not everything
3. **Set session timeouts** — log out after completion
4. **Review screenshots** after sensitive operations before sharing
5. **Never expose the debugging port** to the network — 9222 should be bound to localhost only

## Pitfalls

1. **Chrome must already be running** — the MCP server connects to an existing Chrome instance, it doesn't launch one
2. **CAPTCHA solving is not 100%** — complex CAPTCHAs (reCAPTCHA v3, hCaptcha Enterprise) may still fail
3. **Gmail OTP requires app password** — Google requires 2FA to be enabled before creating app passwords
4. **Browser state affects results** — A/B tests, personalized content, and geo-targeting mean different users may see different pages
5. **Early stage** — 22 stars, MIT license. Expect API changes and potential instability.

---

*Discovered July 16, 2026 during mcpservers.org sitemap scan. 22 stars at time of discovery. Complementary to browser-use (general scraping) and unique in CAPTCHA + Gmail OTP integration.*
