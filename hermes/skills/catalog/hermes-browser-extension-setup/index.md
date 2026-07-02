---
title: "Hermes Browser Extension — Full Setup Guide"
description: "Install, configure, and use the Hermes Browser Extension side panel for Chrome/Edge/Chromium. Connect active browser context to your local or remote Hermes Agent runtime."
---

# Hermes Browser Extension — Setup Guide

**Repo:** [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension)
**Stars:** 439 | **Author:** Jon Komet (`@abundantbeing`)
**Status:** Public alpha — load unpacked, not on Chrome Web Store yet
**Skills.sh:** `npx skills add aradotso/hermes-skills --skill hermes-browser-extension`

---

## What It Is

The Hermes Browser Extension is a Chrome/Edge/Chromium side panel that connects to your Hermes Gateway/API server. It's not a standalone chatbot — it talks to the real Hermes Agent runtime (local by default, remote when configured) so it can use the models, tools, skills, sessions, memory, and MCP servers already configured in Hermes.

### Key Features

- **Browser-native side panel** — MV3 extension powered by Chrome's Side Panel API
- **Local or remote Hermes** — Default `http://127.0.0.1:8642`, configurable to any reachable URL
- **Dashboard WebSocket mode** — No API key needed when you have a signed-in remote Hermes dashboard tab
- **Auto-sync** — Connected providers/models, profiles, skills, sessions, and capabilities sync automatically
- **Hermes compatibility panel** — Older gateways degrade into explicit fallback/manual modes instead of breaking
- **Context injection** — Sends active tab/browser context into a persisted Hermes session, or switch to Chat-only
- **Composer-header context menu** — Quick controls for context scope (Chat only / Follow active tab / Page only)

---

## Prerequisites

- **Hermes Agent** running locally (port 8642) or remotely (reachable URL)
  - Install: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
- **Chrome, Edge, or any Chromium browser** (version 114+ for Side Panel API)
- **Developer mode** enabled in browser extensions page

---

## Installation

### Method 1: Load Unpacked Extension (Current)

The extension is NOT yet on the Chrome Web Store. Load it as an unpacked extension:

```bash
# Clone the repo
git clone https://github.com/abundantbeing/hermes-browser-extension.git
cd hermes-browser-extension

# Install dependencies and build
npm install
npm run build
```

Then in Chrome/Edge:
1. Navigate to `chrome://extensions` (or `edge://extensions`)
2. Enable **Developer mode** (toggle top-right)
3. Click **Load unpacked**
4. Select the `dist/` or `build/` folder from the cloned repo
5. The Hermes side panel icon appears in your toolbar

### Method 2: Via skills.sh (When Available)

```bash
npx skills add aradotso/hermes-skills --skill hermes-browser-extension
```

---

## Configuration

### 1. Open the Side Panel

Click the Hermes icon in your browser toolbar, or use the keyboard shortcut (configurable in `chrome://extensions/shortcuts`).

### 2. Connect to Hermes

**Local Hermes (default):**
- The extension defaults to `http://127.0.0.1:8642`
- If Hermes is running locally with default settings, it connects automatically

**Remote Hermes:**
- In the extension settings, enter your Hermes API server URL
- Example: `https://your-server.com:8642`
- Add your API key if required

**Dashboard WebSocket mode:**
- If you have a Hermes dashboard tab open and signed in, the extension can use WebSocket mode
- No API key needed in this mode

### 3. Configure Context Scope

The composer header has a context menu with three modes:
- **Chat only** — No browser context sent; pure chat with Hermes
- **Follow active tab** — Context follows whichever tab you're viewing
- **Page only** — Context stays locked to one page

### 4. Appearance Settings

The extension supports:
- **Color modes:** Light, dark, system
- **Theme picker:** Multiple built-in themes (Mono, etc.)
- **Font size:** Adjustable for readability

---

## Hermes-Side Configuration

### Verify Gateway is Reachable

The extension talks to the Hermes Gateway. Verify it's running and reachable:

```bash
# Check Hermes gateway status
hermes gateway status

# Test API endpoint
curl http://127.0.0.1:8642/api/health
```

### Ensure CORS is Configured (Remote Setups)

If connecting from a browser on a different machine, the Hermes Gateway needs CORS configured:

```bash
# In Hermes config.yaml, add under gateway section:
# cors:
#   allowed_origins:
#     - "chrome-extension://*"
#     - "https://your-domain.com"
```

### API Key (Remote Setups)

For remote Hermes connections, generate an API key:

```bash
hermes auth create-key --name "browser-extension" --expires 90d
```

---

## Usage Examples

### 1. Ask About the Current Page

With context scope set to **Follow active tab** or **Page only**, simply type:

> "Summarize this page"  
> "What framework does this site use?"  
> "Extract the pricing information from this page"

### 2. Debug Your Own Web App

Open your local dev server in Chrome, then ask Hermes:

> "Check this page for accessibility issues"  
> "Find all broken links on this page"  
> "Analyze the network requests on this page"

### 3. Research With Context

Browse documentation or competitor sites, then:

> "Compare the API design of this page with our internal docs at /api/v2"  
> "What SEO improvements would you suggest for this page?"

---

## Troubleshooting

### "Cannot connect to Hermes"

1. Verify Hermes Gateway is running: `hermes gateway status`
2. Check the port: default is 8642, verify with `hermes config get gateway.port`
3. For remote setups: ensure the URL is reachable from the browser machine
4. Check firewall rules if connecting across networks

### "API key required"

- Generate an API key: `hermes auth create-key --name "browser-extension"`
- Or use Dashboard WebSocket mode (open Hermes dashboard in a tab first)

### "Compatibility mode" warning

- Your Hermes version may be older than the extension expects
- Update Hermes: `hermes update`
- The extension will fall back to manual/compatibility mode

### Side panel not showing

- Requires Chrome/Edge 114+
- Check `chrome://extensions` — the extension must be enabled
- Try the keyboard shortcut: `chrome://extensions/shortcuts`

---

## Security Notes

- The extension runs with MV3 permissions model
- Browser context is **read-only** — the extension cannot modify pages
- All communication with Hermes uses the configured API endpoint (local by default)
- API keys are stored in browser extension storage, not synced to cloud
- No telemetry or external services — all processing happens through your Hermes instance

---

## CorpusIQ Use Cases

| Use Case | How |
|----------|-----|
| **Competitive research** | Browse competitor sites, ask Hermes to analyze architecture/SEO/copy patterns |
| **Content auditing** | Review CorpusIQ docs/landing pages with Hermes analysis in side panel |
| **API exploration** | Browse API docs, have Hermes generate integration code on the fly |
| **Social media monitoring** | Browse X/Reddit threads, ask Hermes to draft contextual replies |
| **Onboarding** | New team members browse internal docs with Hermes explaining concepts |

---

*Setup guide by CorpusIQ. Extension by [Jon Komet](https://github.com/abundantbeing). Hermes Agent by [Nous Research](https://github.com/nousresearch/hermes-agent).*
