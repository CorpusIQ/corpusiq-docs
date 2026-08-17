---
title: "last30days Skill — Recent-Activity Research Setup"
description: "mvanhorn/last30days-skill — 1 core skill, 32.7K installs: find projects, repos, and ecosystem activity from the last 30 days. 58.4K GitHub stars; audit findings named in Limitations."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/last30days-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-17"
tags: ["hermes skill", "agent skill", "skill setup", "research", "discovery", "last30days"]
---

# last30days Skill — Setup Guide

**Source:** [mvanhorn/last30days-skill](https://skills.sh/mvanhorn/last30days-skill)
**GitHub:** [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)
**Skills:** 3 skills · 32.7K total installs (core skill carries 32.7K)
**Category:** Research & Discovery
**First Seen:** catalogued August 17, 2026 sweep (last30days on skills.sh since February 7, 2026)
**Quality Tier:** 🟡 Trusted — Gen Agent Trust Hub Fail and Snyk Fail named (see Limitations)

last30days is a research skill for finding what actually happened recently: projects, repos, and ecosystem activity with movement in the last 30 days. Its opening move is a stale-clone self-check, then it runs structured searches and synthesizes a fresh-activity report — the pattern behind "what's new in X right now" questions.

---

## Installation

```bash
npx skills add mvanhorn/last30days-skill
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/mvanhorn/last30days-skill --skill last30days
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Search access** | Web/GitHub search for activity lookups |
| **Skill hygiene** | The skill's own stale-clone self-check verifies it was not loaded from an outdated marketplace cache |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| last30days | 32.7K | Core research workflow: 30-day-window activity discovery |
| last30days-3 | 2 | Companion variant |
| last30days-v3-spec | 1 | v3 specification notes |

## Quick Start

1. Install: `npx skills add mvanhorn/last30days-skill`
2. Ask: "what's new in <domain> in the last 30 days"
3. The skill runs recency-windowed searches and reports fresh projects and activity

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Ecosystem discovery** | A recency window pairs with our nightly ecosystem scans — fresh-activity bias for skills.sh and MCP directory sweeps |
| **Competitive research** | "What shipped in <competitor space> in the last 30 days" as a first-pass brief |
| **Catch-up briefings** | Fast context rebuild after downtime or focus elsewhere |

## Limitations / Verification

- Security audits on last30days: Gen Agent Trust Hub **Fail**, Socket Warn, Snyk **Fail** — the two Fails are named here per catalog policy; review the findings before production use
- Publisher-page install counts verified (32.7K core); GitHub 58.4K stars on the repo — the star count and install base are large, but the audit fails mean the skill's dependencies deserve a closer look in security-sensitive contexts
- Companion skills (last30days-3, last30days-v3-spec) are sub-10 installs — effectively single-skill content

```bash
npx skills add mvanhorn/last30days-skill   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
