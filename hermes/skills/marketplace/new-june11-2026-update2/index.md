---
title: "June 11, 2026 — Update #2 (28 New Skills)"
description: "Evening sweep: 23 OpenClaw ecosystem skills from aradotso/hermes-skills plus 5 new standalone Hermes skills. Agent control centers, Chinese platform integrations, deployment tooling, PPT generation, QQ bot, and marketing dashboard."
---

# June 11, 2026 — Update #2: 28 New Skills

Third sweep of the day found **28 additional skills** not in the morning or afternoon discoveries. The `aradotso/hermes-skills` repo grew its OpenClaw ecosystem dramatically — 23 new skills covering control centers, deployment tooling, Chinese platform integrations (WeChat, DingTalk, Lark/Feishu), security guides, and training frameworks. Plus 5 standalone skills from independent publishers.

*Previously cataloged today: aradotso/hermes-skills (31), membranedev/application-skills (10), nousresearch/hermes-agent (15), community standalone (5), aradotso/ai-agent-skills (2), aradotso/trending-skills (1).*

---

## aradotso/hermes-skills — 23 new OpenClaw ecosystem skills

The community repo now has **54 skills** (up from 31). New additions focus on OpenClaw deployment, control interfaces, China integrations, and community resources.

### OpenClaw Control & Operations (7)

| Skill | Installs | Use Case |
|-------|----------|----------|
| `aradotso/hermes-skills@openclaw-control-center` | 137 | Central OpenClaw control center dashboard |
| `aradotso/hermes-skills@openclaw-mission-control` | 127 | Mission control for OpenClaw agent coordination |
| `aradotso/hermes-skills@openclaw-studio-dashboard` | 104 | Studio dashboard for agent development |
| `aradotso/hermes-skills@openclaw-admin-vue` | 95 | Admin panel built with Vue.js |
| `aradotso/hermes-skills@openclaw-bot-review-dashboard` | 107 | Bot review and quality assurance dashboard |
| `aradotso/hermes-skills@openclaw-zero-token` | 135 | Zero-token optimization mode for cost reduction |
| `aradotso/hermes-skills@openclaw-rl-training` | 137 | Reinforcement learning training pipeline |

### China Platform Integrations (6)

| Skill | Installs | Use Case |
|-------|----------|----------|
| `aradotso/hermes-skills@openclaw-chinese-ai-assistant` | 126 | Chinese-language AI assistant integration |
| `aradotso/hermes-skills@openclaw-china-integration` | 122 | General China platform integration framework |
| `aradotso/hermes-skills@openclaw-wechat-integration` | 122 | WeChat messaging platform integration |
| `aradotso/hermes-skills@dingtalk-openclaw-connector` | 106 | DingTalk enterprise messaging connector |
| `aradotso/hermes-skills@openclaw-lark-integration` | 117 | Lark (Feishu) platform integration |
| `aradotso/hermes-skills@openclaw-china-docker` | 119 | Docker deployment optimized for China networks |

### Deployment & Tooling (3)

| Skill | Installs | Use Case |
|-------|----------|----------|
| `aradotso/hermes-skills@openclaw-installer-deployment` | 116 | One-click installer and deployment scripts |
| `aradotso/hermes-skills@openclaw-deployment-installer` | 114 | Alternative deployment installer (variant) |
| `aradotso/hermes-skills@openclaw-security-practice-guide` | 122 | Security best practices guide for OpenClaw |

### Community & Resources (7)

| Skill | Installs | Use Case |
|-------|----------|----------|
| `aradotso/hermes-skills@awesome-openclaw-agents-templates` | 118 | Curated agent template collection |
| `aradotso/hermes-skills@awesome-openclaw-tutorial` | 131 | Step-by-step OpenClaw tutorials |
| `aradotso/hermes-skills@awesome-openclaw-skills-zh` | 124 | Chinese-language curated skill collection |
| `aradotso/hermes-skills@awesome-openclaw-usecases-zh` | 138 | Chinese-language use case patterns |
| `aradotso/hermes-skills@openclaw101-resource-platform` | 111 | Beginner resource platform for OpenClaw |
| `aradotso/hermes-skills@openclaw-awd-arena` | 111 | AWD (Attack/Defense) training arena |
| `aradotso/hermes-skills@openclaw-master-skills` | 109 | Master skills meta-collection |

**Setup:**

```bash
# Core control & operations
npx skills add aradotso/hermes-skills@openclaw-control-center
npx skills add aradotso/hermes-skills@openclaw-mission-control
npx skills add aradotso/hermes-skills@openclaw-studio-dashboard
npx skills add aradotso/hermes-skills@openclaw-admin-vue
# Requires: OpenClaw installed + Vue.js dev environment for admin panel

# China platform integrations (requires respective platform accounts)
npx skills add aradotso/hermes-skills@openclaw-wechat-integration
npx skills add aradotso/hermes-skills@dingtalk-openclaw-connector
npx skills add aradotso/hermes-skills@openclaw-lark-integration
# WeChat: Official Account or Mini Program credentials
# DingTalk: Enterprise app credentials from DingTalk Open Platform
# Lark: App ID + App Secret from Lark Developer Console

# Deployment & security
npx skills add aradotso/hermes-skills@openclaw-installer-deployment
npx skills add aradotso/hermes-skills@openclaw-security-practice-guide
# Installer: Requires Docker + access to target deployment environment
# Security: Read-only; no API keys required

# Community resources (read-only — no API keys)
npx skills add aradotso/hermes-skills@awesome-openclaw-agents-templates
npx skills add aradotso/hermes-skills@awesome-openclaw-tutorial
npx skills add aradotso/hermes-skills@openclaw101-resource-platform
npx skills add aradotso/hermes-skills@openclaw-master-skills

# Cost optimization & training
npx skills add aradotso/hermes-skills@openclaw-zero-token
npx skills add aradotso/hermes-skills@openclaw-rl-training
# zero-token: Applies to any OpenClaw deployment — instant savings
# rl-training: Requires RL environment + training compute
```

---

## Standalone Community Skills — 5 new

Independent Hermes-relevant skills from four new publishers.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `wihy/hermes-agent-skill@hermes-agent` | 489 | Hermes agent skill from wihy — alternative community wrapper |
| `aradotso/marketing-skills@hermes-marketing-dashboard` | 383 | Marketing analytics dashboard for Hermes agents |
| `hermess/ppt-director@ppt-director` | 82 | PowerPoint presentation director — generate slide decks from Hermes |
| `chujianyun/skills@hermes-qq` | 51 | QQ (Tencent) instant messaging bot integration |
| `skills.volces.com@hermes-install` | 17 | Hermes installer from ByteDance/Volces |

**Setup:**

```bash
# Alternative Hermes agent wrapper
npx skills add wihy/hermes-agent-skill@hermes-agent
# Drop-in alternative to the official nousresearch/hermes-agent skill.
# Good for environments where the official version has conflicts.

# Marketing dashboard
npx skills add aradotso/marketing-skills@hermes-marketing-dashboard
# Connects to Google Analytics, Meta Ads, Google Ads for unified view.

# PowerPoint generation
npx skills add hermess/ppt-director@ppt-director
# Requires: python-pptx (`pip install python-pptx`)
# Generates .pptx files from markdown outlines.

# QQ bot (Chinese market)
npx skills add chujianyun/skills@hermes-qq
# Requires: QQ Bot AppID + Token from QQ Open Platform
# Enables Hermes agent as an interactive QQ group bot.

# ByteDance installer
npx skills add skills.volces.com@hermes-install
# One-line Hermes installer optimized for Volces/ByteDance cloud.
# Alternative to `hermes setup` for Chinese cloud environments.
```

---

## Summary

| Repository | New Skills | Total Cataloged | Category |
|-----------|:---------:|:---------------:|----------|
| aradotso/hermes-skills | 23 | **54** | OpenClaw Ecosystem |
| wihy/hermes-agent-skill | 1 | **1** | Community Standalone |
| aradotso/marketing-skills | 1 | **1** | Marketing Dashboard |
| hermess/ppt-director | 1 | **1** | Productivity |
| chujianyun/skills | 1 | **2** | Community Standalone |
| skills.volces.com | 1 | **2** | ByteDance |
| **Total New** | **28** | — | — |

**Combined June 11 total:** 38 (morning) + 19 (afternoon) + 28 (evening) = **85 new skills discovered today.**

All skills installable via `npx skills add <owner/repo>@<skill>`. OpenClaw skills require OpenClaw installed (`pip install openclaw`). China platform skills require respective platform developer accounts.

---

*← [June 11 Update #1](/hermes/skills/marketplace/new-june11-2026-update/) | [Skills Catalog](/hermes/skills/catalog/) →*
*↑ [Marketplace Home](/hermes/skills/marketplace/)*


---
*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*


---
*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*
