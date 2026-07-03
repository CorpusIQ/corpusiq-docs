---
title: "🆕 July 3, 2026 — Hermex iPhone App + Crypto Radar + Agent Memory Stack"
description: "7 new Hermes-relevant repos discovered July 3, 2026: Hermex native iPhone app (286⭐), Hermes Crypto Radar, Da7-Tech/mind memory engine, Obsidian plugin, n8n workflow engineer, Hermes skins, and Nick's Stack template."
---

# 🆕 July 3, 2026 — 7 New Repos Discovered

**Date:** July 3, 2026
**New Repos:** 7 | **New Skills/Tools:** 7 | **Combined Stars:** 297

Daily sweep of GitHub (`hermes-agent` topic, `hermes-skill` topic, new repos created July 2-3) surfaced 7 new Hermes-relevant projects. The standout is **Hermex** — a polished native iPhone app that turns your phone into a mobile cockpit for your self-hosted Hermes agent. 286 stars in its first 24 hours.

---

## New at a Glance

| # | Project | Stars | Type | Category | Source |
|---|---------|:-----:|------|----------|--------|
| 1 | **Hermex** | 286 | iOS App | Mobile/UX | uzairansaruzi/hermex |
| 2 | **Hermes Crypto Radar** | 1 | Plugin | Crypto/Finance | ssdeanx/Hermes-Crypto-Radar |
| 3 | **Da7-Tech/mind** | 4 | Library | Memory/AI | Da7-Tech/mind |
| 4 | **n8n Workflow Engineer** | 1 | Skill | Automation | 503496348-ops/n8n-workflow-engineer |
| 5 | **Hermes Chatbot for Obsidian** | 0 | Plugin | PKM/Notes | jeongu0569-ui/hermes-connection-obsidian- |
| 6 | **Hermes Skins** | 0 | Theme | UI/CLI | mdgld/hermes-skins |
| 7 | **Nick's Stack** | 4 | Template | Deployment | nickvasilescu/nicks-stack |

---

## Category Breakdown

### Mobile & UX (1 project)

#### Hermex (286⭐) ⭐ Setup Guide Available

**Repo:** [uzairansaruzi/hermex](https://github.com/uzairansaruzi/hermex)
**Author:** Uzair Ansari (`@uzairansar`)
**App Store:** [Hermex on the App Store](https://apps.apple.com/app/hermex/id6767006319)
**Website:** [hermexapp.com](https://hermexapp.com)

Native SwiftUI iPhone app for driving a self-hosted Hermes agent. The phone is the control plane, not the compute plane — your agent, tools, and data stay on your own hardware. No subscriptions, no analytics, no third-party relay.

**Key features:**
- Real-time streaming chat with thinking + tool-call visibility
- Stop/steer agent runs mid-flight
- Browse, search, and resume sessions (offline-cached)
- Switch models, providers, profiles, and projects on the fly
- View/edit cron tasks and installed skills from your phone
- Workspace file browser for your server's filesystem
- Read-only memory and usage insights panels
- iOS 18+ native SwiftUI (not a web wrapper)

**Setup Guide:** [Hermex iPhone App — Full Setup Guide](/hermes/skills/catalog/hermex-iphone-app-setup/)

```bash
# Install from App Store
# https://apps.apple.com/app/hermex/id6767006319

# Or build from source:
git clone https://github.com/uzairansaruzi/hermex.git
cd hermex
open HermesMobile.xcodeproj
```

**Why this matters:** Hermex closes the mobile UX gap for Hermes. Previously, interacting with a self-hosted Hermes agent from your phone meant using a web browser pointed at Hermes Web UI. Hermex gives you a native experience — streaming, sessions, skills, tasks, workspace browsing — all in a polished SwiftUI app. At 286 stars in 24 hours, the community is voting loudly.

---

### Crypto & Finance (1 project)

#### Hermes Crypto Radar (1⭐)

**Repo:** [ssdeanx/Hermes-Crypto-Radar](https://github.com/ssdeanx/Hermes-Crypto-Radar)
**Author:** ssdeanx

Hermes Agent plugin for multi-chain crypto market intelligence. Tracks 39+ tokens across Solana, Polygon, Cosmos, and more with RSI, MACD, Bollinger Bands, ATR, and EMA technical indicators. RSS news aggregation with a 3-strategy signal engine (momentum, mean-reversion, trend-following). Integrates Binance data and DeFiLlama on-chain metrics.

**Key features:**
- Multi-chain: Solana, Polygon, Cosmos, Aptos, Sui
- 6 technical indicators (RSI, MACD, Bollinger, ATR, EMA)
- 3-strategy signal engine
- Binance + DeFiLlama data sources
- RSS news aggregation
- Hermes Agent plugin architecture

```bash
git clone https://github.com/ssdeanx/Hermes-Crypto-Radar.git
# Install as Hermes plugin — see repo README
```

---

### Memory & Agent Infrastructure (1 project)

#### Da7-Tech/mind (4⭐)

**Repo:** [Da7-Tech/mind](https://github.com/Da7-Tech/mind)
**Author:** Da7-Tech

Brain-like memory for any coding agent: spreading-activation recall, Ebbinghaus forgetting curve, deterministic dream consolidation. One Python file, zero dependencies, works offline. Compatible with Hermes Agent, Claude Code, and Codex.

**Key features:**
- Spreading-activation recall for associative memory retrieval
- Ebbinghaus forgetting curve — naturally decays unused memories
- Deterministic dream consolidation — dedup, supersede, compress
- Single Python file, zero dependencies
- Offline-first, English + Arabic support
- Hermes-agent compatible

```bash
git clone https://github.com/Da7-Tech/mind.git
# Drop mind.py into your agent's memory layer
```

---

### Automation & Workflow (1 project)

#### n8n Workflow Engineer (1⭐)

**Repo:** [503496348-ops/n8n-workflow-engineer](https://github.com/503496348-ops/n8n-workflow-engineer)

Hermes Skill for production-grade n8n workflow generation, inspection, scaffolding, and structural atlas mining. Designed for operators who build n8n automations through their Hermes agent.

```bash
npx skills add 503496348-ops/n8n-workflow-engineer
```

---

### PKM & Notes (1 project)

#### Hermes Chatbot for Obsidian (0⭐)

**Repo:** [jeongu0569-ui/hermes-connection-obsidian-](https://github.com/jeongu0569-ui/hermes-connection-obsidian-)

Obsidian plugin that integrates the Hermes chatbot directly into your workspace. Leverage Hermes AI to streamline note-taking, brainstorming, and writing without leaving Obsidian.

```bash
# Install via Obsidian Community Plugins (once published)
# Or manual: clone into .obsidian/plugins/
git clone https://github.com/jeongu0569-ui/hermes-connection-obsidian-.git
```

---

### UI & Theming (1 project)

#### Hermes Skins (0⭐)

**Repo:** [mdgld/hermes-skins](https://github.com/mdgld/hermes-skins)

A collection of light and dark skins for Hermes Agent TUI/CLI based on Widmer Hazenberg's Monokai color scheme. Drop-in theme files to customize your terminal agent experience.

```bash
git clone https://github.com/mdgld/hermes-skins.git
# Copy theme files to ~/.hermes/themes/
```

---

### Deployment Templates (1 project)

#### Nick's Stack (4⭐)

**Repo:** [nickvasilescu/nicks-stack](https://github.com/nickvasilescu/nicks-stack)

Ready-to-run Hermes AI agent template with Orgo (Telegram QR onboarding), Composio integrations, AgentPhone SMS, Obsidian sync, and GPT-5.5 support. Bring your own keys — zero secrets baked in.

```bash
git clone https://github.com/nickvasilescu/nicks-stack.git
cd nicks-stack
# Follow README for setup — all config via .env
```

---

## Why These Matter for Hermes Users

### Hermex: The Mobile Control Plane
Until today, there was no native mobile experience for Hermes. Hermex changes that — and it does it with a polished, App Store-distributed SwiftUI app. For operators who want to check on their agents, review sessions, or kick off tasks from their phone, this is the missing piece.

### Ecosystem Maturation Signals
This sweep shows three healthy trends:
1. **Mobile expansion** — Hermex proves the Hermes ecosystem can support native mobile clients.
2. **Domain specialization** — Crypto Radar, n8n Workflow Engineer, and Obsidian plugin show the community building domain-specific Hermes extensions.
3. **Infrastructure innovation** — Da7-Tech/mind introduces cognitive memory models (spreading activation, Ebbinghaus forgetting) that push beyond simple key-value stores.

---

## Setup Guides Added

This sweep produced one detailed setup guide:
- **[Hermex iPhone App Setup](/hermes/skills/catalog/hermex-iphone-app-setup/)** — App Store install, server pairing, feature walkthrough, troubleshooting

---

## Comparison

| Metric | Count |
|--------|:-----:|
| Previously documented in catalog | ~180 |
| New this sweep | 7 |
| New setup guides created | 1 |
| Combined new stars | 297 |

---

*← [July 2 Sweep](/hermes/skills/marketplace/new-july2-2026/) | [Marketplace Home](/hermes/skills/marketplace/) | [July 3 Update (6 more) →](/hermes/skills/marketplace/new-july3-2026-update/)*
*Powered by CorpusIQ*
