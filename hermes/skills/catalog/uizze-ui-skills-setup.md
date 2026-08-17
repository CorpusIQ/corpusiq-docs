---
title: "Uizze UI Skills — Anti-UI-Slop Design Quality Setup"
description: Install the uizze.com UI quality skills (394.7K combined installs) — anti-ui-slop (260.5K), ui-radar (132K), ui-design, and ui-slop-score for detecting and fixing AI-generated interface slop.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/uizze-ui-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Uizze UI Skills — Setup Guide

**Source:** [uizze.com](https://www.skills.sh/site/uizze.com) (5 skills · 394.7K combined installs)
**Site:** [uizze.com](https://uizze.com/)
**Category:** Design Quality / UI Engineering
**First Seen:** August 12, 2026
**Quality Tier:** 🟢 Production (`anti-ui-slop` at 260.5K installs)

Uizze's skills attack a specific problem: "UI slop" — the generic, samey, gradient-and-glassmorphism interfaces that AI coding agents default to. `anti-ui-slop` is the flagship at 260.5K installs, joined by `ui-radar` (132K) which scans and scores existing interfaces. Together they form a design-quality gate for anything an agent builds.

---

## Installation

```bash
# Site registry listing — install by skill
npx skills add https://skills.sh/site/uizze.com --skill anti-ui-slop
npx skills add https://skills.sh/site/uizze.com --skill ui-radar
```

If the CLI rejects site-registry sources, clone the skill definitions directly from [uizze.com](https://uizze.com/) and drop them into the agent's skills directory.

---

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| `anti-ui-slop` | 260.5K | Building interfaces that avoid generic AI slop patterns |
| `ui-radar` | 132.0K | Scanning and scoring existing UIs for slop |
| `ui-design` | 1.1K | General UI design guidance |
| `ui-slop-score` | 1.1K | Scoring a UI's slop factor |
| `anti-ai-ui-slop` | 3 | Newest/experimental variant |

---

## Prerequisites

| Requirement | Details |
|---|---|
| Node.js + npx | For the skills.sh CLI install path |
| A UI to build or audit | Works on code or live URLs |
| Any agent runtime | Pure procedural knowledge — no API keys |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Docs site polish** | `ui-radar` audit on docs.corpusiq.io before design passes |
| **Agent-built dashboards** | `anti-ui-slop` as a pre-ship gate on agent-generated UI |
| **Competitive UI reviews** | `ui-radar` to benchmark competitor interfaces |
| **Design QA for HyperFrames/landing pages** | Score and fix before publish |

---

## Limitations / Verification

- Site-registry publisher (no GitHub repo) — install path depends on skills.sh CLI support for site sources
- `anti-ai-ui-slop` at 3 installs is experimental
- Verify install: `npx skills list | grep -i slop`

---

## Related

- [Popular Web Designs Setup](/hermes/skills/catalog/popular-web-designs-setup/)
- [Web Design Guidelines Setup](/hermes/skills/catalog/popular-web-designs-setup/)
- [Skills Catalog](/hermes/skills/catalog/)

*Powered by CorpusIQ*
