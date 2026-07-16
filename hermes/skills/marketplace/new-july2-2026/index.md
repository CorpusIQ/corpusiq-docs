---
title: "July 2, 2026 — Hermes Browser Extension"
description: "2 new Hermes-relevant skills discovered July 2, 2026: Hermes Browser Extension (439⭐) brings side-panel access to Chrome/Edge, OpenClaw Android (1,649⭐) runs agents on old phones."
---

# 🆕 July 2, 2026 — 2 New Skills Discovered

**Date:** July 2, 2026
**New Repos:** 2 | **New Skills:** 2 | **Combined Stars:** 2,088

Daily sweep of `aradotso/hermes-skills` surfaced two new additions added July 1-2: the **Hermes Browser Extension** — a Chrome/Edge side panel connecting browser context to your Hermes runtime — and **OpenClaw on Android** — run autonomous agents on old phones without Linux overhead. Both are immediately relevant to Hermes agent deployments.

---

## New Skills at a Glance

| # | Skill | Stars | Installs | Category | Source |
|---|-------|:-----:|:--------:|----------|--------|
| 1 | **hermes-browser-extension** | 439 | ~180 | Browser/UI | abundantbeing/hermes-browser-extension |
| 2 | **openclaw-android-setup** | 1,649 | ~1,500 | Mobile/Deployment | AidanPark/openclaw-android |

---

## Category Breakdown

### Browser Integration (1 skill)

#### hermes-browser-extension (439⭐) ⭐ Setup Guide Available

**Repo:** [abundantbeing/hermes-browser-extension](https://github.com/abundantbeing/hermes-browser-extension)
**Author:** Jon Komet (`@abundantbeing`)

Browser-native side panel for Hermes Agent. Load as an unpacked Chrome/Edge/Chromium extension and get a persistent Hermes chat panel that sees your active browser context. Connects to local or remote Hermes Gateway — uses your existing models, tools, skills, and sessions.

**Key features:**
- Chrome MV3 side panel with Side Panel API
- Auto-syncs providers, models, profiles, skills, sessions
- Three context modes: Chat only, Follow active tab, Page only
- Dashboard WebSocket mode (no API key needed)
- Hermes compatibility panel for older gateways
- Theme picker with light/dark/system modes

**Setup Guide:** [Hermes Browser Extension — Full Setup Guide](/hermes/skills/catalog/hermes-browser-extension-setup/)

```bash
# Clone and load unpacked (Chrome Web Store pending)
git clone https://github.com/abundantbeing/hermes-browser-extension.git
# Then: chrome://extensions → Load unpacked → select dist/

# Via skills.sh
npx skills add aradotso/hermes-skills --skill hermes-browser-extension
```

---

### Mobile Deployment (1 skill)

#### openclaw-android-setup (1,649⭐) ⭐ Setup Guide Available

**Repo:** [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android)
**Author:** Aidan Park

Run OpenClaw agents on Android with a single command. Eliminates the 700MB–1GB overhead of proot-distro + Debian by installing just the glibc dynamic linker. Works on Android 7.0+ with Termux. Ideal for repurposing old phones as 24/7 agent nodes drawing only 3-5W.

**Key features:**
- No proot-distro — ~500MB total footprint (vs 1.5GB+)
- One-command install: `curl | bash`
- Works on phones as old as Samsung Galaxy S8+ (2017)
- Hermes-compatible skill installation via skills.sh
- Daemon mode for always-on agents
- Wake lock support to prevent Android sleep kills

**Setup Guide:** [OpenClaw on Android — Full Setup Guide](/hermes/skills/catalog/openclaw-android-setup/)

```bash
# In Termux (install from F-Droid, NOT Google Play):
curl -fsSL https://raw.githubusercontent.com/AidanPark/openclaw-android/main/setup.sh | bash

# Via skills.sh
npx skills add aradotso/hermes-skills --skill openclaw-android-setup
```

---

## Why These Matter for Hermes Users

### Browser Extension
The Hermes Browser Extension closes a critical UX gap: interacting with Hermes while browsing. Instead of copying text between terminal and browser, the side panel brings Hermes alongside your web activity. Research, debugging, content auditing — all with Hermes seeing exactly what you see.

### Android Deployment
Old Android phones are the cheapest self-hosted agent hardware available. A used Galaxy S8+ costs ~$50 and draws 3-5W — perfect for running a 24/7 monitoring agent, social media bot, or personal assistant. This project makes it trivial.

---

## Setup Guides Added

This sweep produced two new setup guides:
- **[Hermes Browser Extension Setup](/hermes/skills/catalog/hermes-browser-extension-setup/)** — Load unpacked, connect to Hermes, context modes, troubleshooting
- **[OpenClaw on Android Setup](/hermes/skills/catalog/openclaw-android-setup/)** — Termux install, one-command setup, daemon mode, battery optimization

---

## Comparison

| Metric | Count |
|--------|:-----:|
| Official Hermes skills on skills.sh | 192 |
| Previously documented in catalog | ~178 |
| New this sweep | 2 |
| New setup guides created | 2 |

---

*← [July 1 Sweep](/hermes/skills/marketplace/new-july1-2026/) | [Marketplace Home](/hermes/skills/marketplace/) →*
*Powered by CorpusIQ*
