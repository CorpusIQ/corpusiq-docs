---
title: "June 27, 2026 — Skills Gallery (1,672"
description: "9 newly discovered Hermes Agent repos — Skills Gallery mega-collection (1,672+ skills across 49 categories), Agent-to-Agent Protocol bridge, autonomy flight recorder, WeChat plugin, Coolify ARM64 deploy, Walkie-Talkie, ztk context compressor, Robert Greene skill, and Gruvbox skin"
---

# New Skills Discovered — June 27, 2026

**Sources:** GitHub Search + [skills.sh](https://skills.sh)
**Total new:** 9 repos | **Highlight:** Skills Gallery (1,672+ skills across 49 categories)
**Date:** June 27, 2026

A massive single-day discovery: the Skills Gallery mega-collection unifies 1,672+ AI agent skills under one install command, plus 8 additional Hermes-native repos spanning agent-to-agent protocol bridges, autonomy evaluation, WeChat integration, deployment templates, and context optimization.

---

## ⭐ Standout Find: Skills Gallery — 1,672+ Skills

**Repo:** [uthumany/Skills-Gallery](https://github.com/uthumany/Skills-Gallery)
**Stars:** ⭐1 | **License:** MIT | **Created:** June 27, 2026
**npm:** `skills-gallery` | **pip:** `skills-gallery` | **By:** uthuman Inc.

The largest single collection of AI agent skills ever published. One command installs access to **1,672+ skills** organized across **49 categories** — frontend development, security auditing, creative coding, multi-agent orchestration, and everything in between. Compatible with 60+ AI agent tools including Hermes Agent.

### Category Breakdown

| Category | Skills | Highlights |
|----------|:------:|------------|
| 🤖 AI & ML | 187 | ML engineering, self-evaluation, reasoning |
| 🎨 Design & UX | 137 | UI/UX design, creative coding, branding |
| 💻 Development | 203 | Frontend, backend, software architecture |
| ☁️ Cloud & DevOps | 165 | Cloud platforms, CI/CD, monitoring |
| 🔒 Security | 58 | Security & permissions |
| 📝 Content & Docs | 221 | Content creation, communication, knowledge mgmt |
| 🔗 APIs & Automation | 148 | API integration, tool use, workflow automation |
| 🌐 Web & Search | 82 | Web browsing, information retrieval, browser automation |
| 🧠 Agent Systems | 178 | Memory & context, multi-agent coordination, planning |
| 📊 Data & Analytics | 85 | Data analysis, visualization, databases |
| 📱 Social & Media | 69 | Social media, email marketing, voice & audio |
| 💼 Business | 119 | Project management, CRM, e-commerce |
| 🖥️ Desktop & Gaming | 10 | Game development |

**Why this matters for Hermes:** Skills Gallery is the "npm of AI agent skills." With 1,672+ skills installable via any package manager (npm, yarn, pnpm, bun, pip, uv, curl), it's the most comprehensive skill catalog available. Hermes Agent is explicitly listed as a compatible platform. For CorpusIQ operators, this single install unlocks hundreds of skills across marketing, sales, data analysis, and automation.

```bash
# One command, every skill
npx skills-gallery

# Or install globally
npm install -g skills-gallery
```

---

## 🔗 New Hermes Agent Repos (8)

### 1. Hermes A2A Bridge — Agent-to-Agent Protocol

**Repo:** [asimons81/hermes-a2a-bridge](https://github.com/asimons81/hermes-a2a-bridge)
**Stars:** ⭐0 | **Created:** June 27, 2026
**Python:** v3.11+ | **Protocol:** A2A v0.4.6

A local-first bridge for the Agent-to-Agent Protocol (HTTP+JSON subset). Lets Hermes discover named remote agents and exposes Hermes itself through an A2A-shaped surface. MCP lets agents use tools; A2A lets agents call other agents. This bridge gives Hermes the second half.

```bash
python -m pip install -e .
hermes plugins enable a2a-bridge
hermes a2a init
hermes a2a serve
```

**Why it matters:** First A2A implementation for Hermes Agent. Enables true multi-agent collaboration where Hermes can delegate to other agent instances across a network. Complements existing subagent/delegation patterns with a standardized protocol.

---

### 2. Hermes Flight Recorder — Autonomy Eval Harness

**Repo:** [zwright8/hermes-flight-recorder](https://github.com/zwright8/hermes-flight-recorder)
**Stars:** ⭐0 | **Created:** June 26, 2026
**License:** Not specified

A standalone adversarial eval harness for Hermes Agent runs. Converts run artifacts into normalized traces, scores against explicit autonomy boundaries, and renders static HTML reports. Includes training export with SFT/DPO/reward model views, scenario quality metrics, and evidence coverage reports.

```bash
git clone https://github.com/zwright8/hermes-flight-recorder.git
cd hermes-flight-recorder
./demo.sh
open runs/index.html
```

**Why it matters:** Accountability infrastructure for autonomous agents. For CorpusIQ operators running autonomous growth workflows, this provides regression testing, boundary enforcement verification, and training data export for continuous improvement.

---

### 3. Robert Greene Skill — The 48 Laws of Power

**Repo:** [ooovenenoso/robert-greene-skill](https://github.com/ooovenenoso/robert-greene-skill)
**Stars:** ⭐4 | **Created:** June 26, 2026

Hermes Agent skill for The 48 Laws of Power. Cite any law by number, get law recommendations for a situation, and see complementary and contradictory laws. A unique domain-specific knowledge skill for strategic thinking.

```bash
git clone https://github.com/ooovenenoso/robert-greene-skill.git
```

**Why it matters:** Highest-starred new skill of this sweep (⭐4). Demonstrates the pattern of loading book-level domain knowledge as installable agent skills — applicable to business strategy, negotiation, and leadership use cases.

---

### 4. Hermes ztk Integration — Context Token Compressor

**Repo:** [csx0574/hermes-ztk-integration](https://github.com/csx0574/hermes-ztk-integration)
**Stars:** ⭐0 | **Created:** June 26, 2026

Transparent ztk (shell output compressor) integration for Hermes Agent. Auto-wraps non-interactive commands, saving **60-99% context tokens**. Directly addresses one of the most expensive aspects of agent operation — shell output consuming context window.

```bash
git clone https://github.com/csx0574/hermes-ztk-integration.git
```

**Why it matters:** Direct cost optimization for CorpusIQ agents. Every shell command output that gets compressed saves real API costs. At 60-99% compression rates, this could significantly reduce per-session token consumption.

---

### 5. Hermes Walkie-Talkie — Voice Gateway

**Repo:** [TheSethRose/Hermes-Walkie-Talkie](https://github.com/TheSethRose/Hermes-Walkie-Talkie)
**Stars:** ⭐1 | **Created:** June 26, 2026

Pairs an Android push-to-talk client with a local Hermes Voice Gateway. Enables real-time voice interaction with Hermes from an Android device — walkie-talkie style.

---

### 6. Coolify Hermes Agent ARM64 — Production Docker

**Repo:** [darvax/coolify-hermes-agent-arm64](https://github.com/darvax/coolify-hermes-agent-arm64)
**Stars:** ⭐0 | **Created:** June 26, 2026

Production-ready ARM64 Docker Compose template for deploying Hermes Agent on Coolify without the WebUI. Targets the growing ARM64 self-hosting ecosystem (Raspberry Pi, Apple Silicon Mac Minis, AWS Graviton).

---

### 7. Hermes WeChat Multi-Account Plugin

**Repo:** [hyonex/hermes-weixin-multi](https://github.com/hyonex/hermes-weixin-multi)
**Stars:** ⭐1 | **Created:** June 26, 2026

Hermes WeChat Multi-Account Plugin using the iLink Bot API. Chinese market expansion — enables Hermes agents to operate across multiple WeChat accounts simultaneously.

---

### 8. Hermes Gruvbox Skin

**Repo:** [unleashed-nick/hermes-gruvbox-skin](https://github.com/unleashed-nick/hermes-gruvbox-skin)
**Stars:** ⭐1 | **Created:** June 26, 2026

Gruvbox Dark skins for Hermes Agent. Community-contributed theming — the first third-party visual customization for the Hermes terminal interface.

---

## Installation Summary

```bash
# === Skills Gallery (1,672+ skills) ===
npx skills-gallery
# or
npm install -g skills-gallery

# === Hermes A2A Bridge ===
git clone https://github.com/asimons81/hermes-a2a-bridge.git
cd hermes-a2a-bridge && python -m pip install -e .
hermes plugins enable a2a-bridge
hermes a2a init

# === Hermes Flight Recorder ===
git clone https://github.com/zwright8/hermes-flight-recorder.git
cd hermes-flight-recorder && ./demo.sh

# === Hermes ztk Integration ===
git clone https://github.com/csx0574/hermes-ztk-integration.git

# === Robert Greene Skill ===
git clone https://github.com/ooovenenoso/robert-greene-skill.git
```

---

## Impact Assessment

**Skills Gallery** is the single largest skill discovery since the marketplace launched. At 1,672+ skills across 49 categories, it dwarfs all previous sweeps combined. For CorpusIQ operators, this provides instant access to hundreds of production-ready skills for marketing, sales, data analysis, and automation — all installable with one command.

**Hermes A2A Bridge** fills a critical architectural gap: standardized agent-to-agent communication. Combined with existing subagent/delegation capabilities, this enables Hermes to participate in multi-agent networks using an emerging industry protocol.

**Hermes Flight Recorder** adds the evaluation layer that production agent deployments need. For CorpusIQ's autonomous growth agents, this provides regression testing, boundary verification, and continuous improvement data.

---

*← [June 26 Afternoon Update](/hermes/skills/marketplace/new-june26-2026-afternoon/) | [Marketplace Home](/hermes/skills/marketplace/) →*

*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
