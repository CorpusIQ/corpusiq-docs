---
title: "Web Access Skill — Unified Browsing & Scraping Setup"
description: "eze-is/web-access — 1 skill, 15.7K installs: unified web access for search, scraping, login-required operations, and CDP browser automation through your existing Chrome or Edge. 8.7K GitHub stars; audit findings named in Limitations."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/web-access-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-17"
tags: ["hermes skill", "agent skill", "skill setup", "web scraping", "browser automation", "web-access"]
---

# Web Access Skill — Setup Guide

**Source:** [eze-is/web-access](https://skills.sh/eze-is/web-access)
**GitHub:** [eze-is/web-access](https://github.com/eze-is/web-access)
**Skills:** 1 skill · 15.7K installs
**Category:** Web Access & Scraping
**First Seen:** catalogued August 17, 2026 sweep (web-access on skills.sh since March 19, 2026)
**Quality Tier:** 🟡 Trusted — Socket Warn and Snyk Fail named (see Limitations)

web-access is a unified web access skill covering three methods in one workflow: WebSearch for discovery, WebFetch/curl for static content, and CDP browser automation for login-protected or dynamically-rendered platforms (Xiaohongshu, WeChat, Twitter, and similar). It drives your existing Chrome or Edge through a CDP proxy — preserving login state, running in background tabs, with no separate browser instance.

---

## Installation

```bash
npx skills add eze-is/web-access
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/eze-is/web-access --skill web-access
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js 22+** | Required — uses native WebSocket |
| **Chrome or Edge** | Your existing browser, driven via CDP proxy |
| **Dependency check** | Skill runs `check-deps.mjs` before any network operation |

## What It Provides

- Three access methods in one skill: search discovery, static fetch, and CDP browser automation for login-gated content
- 10+ core commands: `/eval` (DOM queries and JS execution), `/click` (UI interaction), `/screenshot` (visual capture), `/scroll` (lazy-load triggering), `/navigate` (page transitions), plus file upload support
- Human-like browsing doctrine: clarify success criteria first, choose the most direct path, validate results against goals, adjust on evidence rather than repeating failed approaches
- Parallel sub-agent execution for independent research targets, with a shared browser instance and automatic tab cleanup

## Quick Start

1. Install: `npx skills add eze-is/web-access`
2. The dependency check confirms CDP availability before any operation
3. Ask: "search for X and open the results in the existing browser session"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Login-gated research** | Preserves real browser sessions — the same property our Mac Mini Playwright context provides, available to any agent |
| **Resilient fetch path** | A third fallback path when our primary search backends degrade |
| **Social-platform checks** | CDP interaction with platforms that block headless automation |

## Limitations / Verification

- Security audits on web-access: Gen Agent Trust Hub Pass, Socket **Warn**, Snyk **Fail** — named per catalog policy; review before use in security-sensitive contexts
- Publisher-page install counts verified (15.7K single skill); GitHub 8.7K stars on the repo
- SKILL.md front matter is bilingual (Chinese primary) — the dependency check and config prompts appear in Chinese first
- Requires a real Chrome/Edge session on the host — not a headless replacement

```bash
npx skills add eze-is/web-access   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
