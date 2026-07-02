---
title: "🆕 July 2, 2026 (Update) — 8 OpenClaw Ecosystem Skills"
description: "8 new OpenClaw-relevant skills discovered July 2, 2026: Blackbox Browser integration (5,931⭐), Alibaba Cloud AI suite (5 skills), independent browser-use, and video generation."
---

# 🆕 July 2, 2026 (Update) — 8 New Skills Discovered

**Date:** July 2, 2026
**New Repos:** 4 | **New Skills:** 8 | **Context:** OpenClaw ecosystem sweep

Evening sweep across 20 skills.sh API queries (hermes + openclaw + ecosystem terms) surfaced 8 uncatalogued OpenClaw-relevant skills. Highlights: **Blackbox Browser** (5,931⭐ project) gets an OpenClaw wrapper, **Alibaba Cloud's AI suite** adds 5 OpenClaw-specific integration skills, and independent contributions for browser-use and video generation.

*This is an update to the [morning discovery](/hermes/skills/marketplace/new-july2-2026/) (Hermes Browser Extension + OpenClaw on Android).*

---

## New Skills at a Glance

| # | Skill | Installs | Category | Source |
|---|-------|:--------:|----------|--------|
| 1 | **bb-browser-openclaw** | 584 | Browser/Automation | epiral/bb-browser |
| 2 | **alicloud-platform-openclaw-setup** | 196 | Cloud/Infrastructure | cinience/alicloud-skills |
| 3 | **browser use** | 180 | Browser/Automation | quentintou/openclaw-skill-browser-use |
| 4 | **alicloud-observability-openclaw-sls-integration** | 85 | Cloud/Observability | cinience/alicloud-skills |
| 5 | **aliyun-sls-openclaw-integration** | 49 | Cloud/Logging | cinience/alicloud-skills |
| 6 | **aliyun-openclaw-setup** | 48 | Cloud/Infrastructure | cinience/alicloud-skills |
| 7 | **evolink-video** | 42 | Video/Media | evolinkai/video-generation-skill-for-openclaw |
| 8 | **bb-browser-openclaw** | 35 | Browser/Automation | yan5xu/bb-browser |

---

## Category Breakdown

### Browser Automation (3 skills)

#### bb-browser-openclaw (584 installs) ⭐ Setup Guide Available

**Repo:** [epiral/bb-browser](https://github.com/epiral/bb-browser) — 5,931⭐
**Source:** skills.sh

OpenClaw wrapper for the **Blackbox Browser** project — a CLI + MCP server that lets AI agents control Chrome with your existing login state. The bb-browser project itself is one of the most popular AI-browser tools (5,931 stars). This skill wraps it for native OpenClaw/Hermes agent use.

**Key capabilities:**
- Control Chrome with your cookies, sessions, and login state intact
- MCP server for agent-to-browser communication
- No headless-mode limitations — uses your real browser
- OpenClaw integration via skills.sh

**Setup Guide:** [bb-browser-openclaw — Full Setup Guide](/hermes/skills/catalog/bb-browser-openclaw-setup/)

```bash
npx skills add epiral/bb-browser --skill bb-browser-openclaw
```

---

#### browser use (180 installs)

**Repo:** [quentintou/openclaw-skill-browser-use](https://github.com/quentintou/openclaw-skill-browser-use) — 5⭐
**Source:** skills.sh

OpenClaw skill for AI-driven browser automation. Dual-tool approach: `agent-browser` (CLI-based Playwright) and `browser-use` (Python autonomous agent). Compatible with ClawdHub.

```bash
npx skills add quentintou/openclaw-skill-browser-use --skill "browser use"
```

---

#### bb-browser-openclaw (35 installs) — alternate fork

**Repo:** [yan5xu/bb-browser](https://github.com/yan5xu/bb-browser)
**Source:** skills.sh

Alternate OpenClaw wrapper for Blackbox Browser. Lower install base; prefer the epiral/bb-browser version for production use.

---

### Cloud Infrastructure — Alibaba Cloud (5 skills)

All five skills from **cinience/alicloud-skills**, providing OpenClaw agent integration with Alibaba Cloud services:

| Skill | Installs | Purpose |
|---|---|---|
| **alicloud-platform-openclaw-setup** | 196 | One-command Alibaba Cloud platform bootstrap for OpenClaw agents |
| **alicloud-observability-openclaw-sls-integration** | 85 | SLS (Simple Log Service) observability — log query, dashboards, alerts |
| **aliyun-sls-openclaw-integration** | 49 | Alibaba Cloud SLS log management from OpenClaw |
| **aliyun-openclaw-setup** | 48 | Streamlined Alibaba Cloud account + service setup for agents |

Plus 6 additional AI-service skills (Qwen vision, TTS, video generation) already catalogued in prior sweeps.

```bash
# Install all Alibaba Cloud skills
npx skills add cinience/alicloud-skills --skill alicloud-platform-openclaw-setup
npx skills add cinience/alicloud-skills --skill alicloud-observability-openclaw-sls-integration
npx skills add cinience/alicloud-skills --skill aliyun-sls-openclaw-integration
npx skills add cinience/alicloud-skills --skill aliyun-openclaw-setup
```

---

### Video Generation (1 skill)

#### evolink-video (42 installs)

**Repo:** [evolinkai/video-generation-skill-for-openclaw](https://github.com/evolinkai/video-generation-skill-for-openclaw)
**Source:** skills.sh

OpenClaw skill for AI video generation. Integrates video creation pipelines into Hermes/OpenClaw agent workflows.

```bash
npx skills add evolinkai/video-generation-skill-for-openclaw --skill evolink-video
```

---

## Installation Summary

```bash
# Browser automation (recommended)
npx skills add epiral/bb-browser --skill bb-browser-openclaw

# Alibaba Cloud suite
npx skills add cinience/alicloud-skills --skill alicloud-platform-openclaw-setup
npx skills add cinience/alicloud-skills --skill alicloud-observability-openclaw-sls-integration
npx skills add cinience/alicloud-skills --skill aliyun-sls-openclaw-integration
npx skills add cinience/alicloud-skills --skill aliyun-openclaw-setup

# Independent tools
npx skills add quentintou/openclaw-skill-browser-use --skill "browser use"
npx skills add evolinkai/video-generation-skill-for-openclaw --skill evolink-video
```

---

## Trend Notes

- **Blackbox Browser** (5,931⭐) is the most significant project in this sweep — the OpenClaw wrapper brings its MCP-server browser control to Hermes agents
- **Alibaba Cloud's AI suite** continues expanding OpenClaw integrations (now 10+ skills from cinience/alicloud-skills)
- All 8 skills are OpenClaw-compatible and work with Hermes Agent via the OpenClaw runtime

---

*← [Previous Discovery](/hermes/skills/marketplace/new-july2-2026/) | [Marketplace Home](/hermes/skills/marketplace/) →*

---

*Part of the [Hermes Skills Library](/hermes/skills/) — curated by CorpusIQ. This page catalogs skills discovered via automated API sweeps of [skills.sh](https://skills.sh). Content remains attributed to original authors and repositories.*
