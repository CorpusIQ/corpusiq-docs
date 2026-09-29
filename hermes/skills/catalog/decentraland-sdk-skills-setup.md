---
title: "Decentraland SDK Skills - Scene Building Setup"
description: "Six Decentraland SDK7 skills for scene development, UI, multiplayer sync, and game design; ~5,900 indexed installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/decentraland-sdk-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "game dev", "decentraland"]
---

# Decentraland SDK Skills - Setup Guide

**Source:** [decentraland/sdk-skills](https://github.com/decentraland/sdk-skills) (3⭐)
**Skill family:** `decentraland/sdk-skills` (6 installable skills)
**Combined Installs:** ~5,900 across indexed listings (Sep 29, 2026 snapshot)
**Category:** Game Dev
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published - verified Sep 29, 2026)

Published by the official Decentraland organization, this repository collects "skills useful for creating Decentraland scenes with the help of an LLM." The six skills cover SDK7 scene development, building UI with React-ECS, authoritative multiplayer servers, multiplayer synchronization, game design and scene optimization, and adding interactivity. All six have indexed SKILL.md entries on skills.sh (6/6 as of the Sep 29, 2026 snapshot).

---

## Installation

```bash
npx skills add decentraland/sdk-skills
```

## Roster - Top Skills

| Skill | Installs | What It Does |
|---|---|---|
| authoritative-server | 209 | Multiplayer Server |
| sdk-scenes | 207 | Decentraland SDK7 Scene Development |
| build-ui | 207 | Building UI with React-ECS |
| multiplayer-sync | 205 | Multiplayer Synchronization in Decentraland |
| game-design | 205 | Decentraland Game Design & Scene Optimization |

The sixth skill, `add-interactivity`, covers adding interactivity to Decentraland scenes; its install count was not published in the snapshot.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Bootstrapping a new scene | Use sdk-scenes for SDK7 project structure and scene development |
| Social multiplayer worlds | Combine authoritative-server with multiplayer-sync for networked scenes |
| In-scene HUDs and menus | Apply build-ui for React-ECS user interfaces |

## Limitations / Verification

- All 6 SKILL.md entries were verified on skills.sh (Sep 29, 2026 snapshot); per-skill install counts are low (200-209), consistent with a young family.
- No live install test has been run from Hermes yet.
- No README facts beyond the repo description were used in this guide.

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
