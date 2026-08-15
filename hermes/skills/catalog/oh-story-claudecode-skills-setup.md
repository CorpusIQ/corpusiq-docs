---
title: Oh Story ClaudeCode Skills — Long-Form Writing & Browser CDP Setup
description: "worldwonderer/oh-story-claudecode — 13 skills, 146.6K installs: story long/short write, analyze, scan, and deslop pipelines plus browser-cdp automation, covers, setup, review, and import for agent-driven long-form writing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/oh-story-claudecode-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "writing", "long-form content", "browser automation", "cdp"]
---

# Oh Story ClaudeCode Skills — Setup Guide

**Source:** [worldwonderer/oh-story-claudecode](https://skills.sh/worldwonderer/oh-story-claudecode)
**GitHub:** [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode)
**Skills:** 13 skills · 146.6K total installs
**Category:** Content Writing & Browser Automation
**First Seen:** catalogued August 15, 2026 midday sweep
**Quality Tier:** 🟡 Trusted (community publisher; 146.6K verified on publisher page vs 11.4K API-sum estimate at queue time)

The Oh Story suite turns an agent into a long-form writing pipeline: long and short write modes, analysis, scanning, and a dedicated deslop pass for cleaning AI-flavored prose, plus a browser-cdp skill for live page automation and cover generation for finished pieces. The morning sweep parked this cluster at an 11.4K estimate; the publisher page shows 146.6K across 13 skills.

---

## Installation

```bash
npx skills add worldwonderer/oh-story-claudecode
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Claude Code environment** | Suite is built for ClaudeCode workflows |
| **Browser for CDP** | For the browser-cdp skill (Chrome DevTools Protocol) |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| story-long-write | 11.8K | Long-form piece writing |
| story-deslop | 11.7K | Remove AI-slop patterns from prose |
| story-long-analyze | 11.6K | Analyze long drafts |
| story-short-write | 11.6K | Short-form writing |
| story-long-scan | 11.5K | Scan long content for issues |
| story-short-analyze | 11.5K | Analyze short pieces |
| browser-cdp | 11.4K | Chrome DevTools Protocol browser automation |
| story-short-scan | 11.4K | Scan short content |
| story-cover | 11.1K | Generate story covers |
| story / story-setup / story-review | 10.8K each | Core orchestration, environment setup, editorial review |
| story-import | 10.5K | Import existing material |

## Quick Start

1. Install: `npx skills add worldwonderer/oh-story-claudecode`
2. Run story-setup to configure the environment
3. Ask: "write a long-form piece on X and run it through deslop before we publish"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Content pipeline** | Long-write plus deslop matches our de-AI-fication doctrine for public content |
| **Browser automation** | browser-cdp as an alternative to our Playwright stack for page-level tasks |
| **Content scanning** | long-scan and short-scan as pre-publish QA passes |
| **Cover generation** | story-cover for post thumbnails and article heroes |

## Limitations / Verification

- Community-maintained; no security-audit pages fetched for this multi-skill suite
- Browser-cdp requires a Chrome/Chromium instance with remote debugging enabled
- Install counts verified on the publisher page; API sums undercount (11.4K vs 146.6K)

```bash
npx skills add worldwonderer/oh-story-claudecode   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
