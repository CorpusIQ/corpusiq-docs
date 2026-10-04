---
title: "New Skills - October 4, 2026"
description: "Skills.sh sweep for October 4, 2026: 733 skills collected, 15 NEW, 1 new publisher guide (CrewAI Skills - official agent design suite, ~29.7K installs)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct4-2026-skills/"
robots: "index,follow"
last_updated: "2026-10-04"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace"]
---

# New Skills - October 4, 2026

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 733 (15 queries, 0 failed) |
| NEW (not in catalog) | 15 |
| NEW >= 100 installs | 2 |
| PARTIAL (source known, skill not cataloged) | 191 |
| New publisher guides | 1 |
| Roster reconciles | 0 |

## New Publisher Guides

### 1. CrewAI Skills - Official Agent Design Suite

**Source:** [crewAIInc/skills](https://github.com/crewAIInc/skills) (44⭐, no LICENSE file) · **~29,666 installs** across 4 indexed listings · 4 SKILL.md files in-repo

The official skills from the CrewAI team behind the 59.3K⭐ multi-agent framework: architecture decisions + project scaffolding (getting-started), agent configuration (design-agent), task design (design-task), and a live docs lookup (ask-docs). The repo also ships a Claude Code plugin marketplace.

→ [Setup guide](/hermes/skills/catalog/crewai-skills-setup)

## NEW Candidates Below the Guide Floor (<100 installs)

| Source | Skill | Installs |
|---|---|---|
| ken-guru/skills | setup-antigravity-devcontainer | 18 → cluster combined 733 |
| nevaberry/nevaberry-plugins | hono-knowledge-patch | 5 → cluster combined 693 |
| elct9620/claude-hono-plugin | Hono Documentation Search | 5 (single-listing repo) |
| vinihdsouza/skill-react | hono/Hono | 2 → cluster combined 46 |

Publisher follow-ups confirmed the remaining NEW set sits below the guide floor: two 1-install re-host bundles of the documented `sickn33/antigravity-awesome-skills` family (`costrict-plugins-repo/...odoo-erp` 7 listings; `satnamrsm/https-github.com-...` 3 listings). Separately, the one other NEW item at 163 installs - `arthurzakirov/agentdesk` `openclaw-browser-setup` - remains a standing rejection: a 0-star dormant personal setup-script publisher (21 listings / 3,052 combined, no community traction).

## Notes

- The guide candidate was verified via GitHub trees API + repo meta API on branch `main`; not previously documented (0 tree hits).
- No roster reconciles this run; the PARTIAL >=100 backlog (70 rows) remains deferred.
- skills.sh skill pages expose per-skill security verdicts (Gen Agent Trust Hub / Socket / Snyk); all four CrewAI skills show Pass, recorded in the setup guide.
