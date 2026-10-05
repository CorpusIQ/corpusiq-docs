---
title: "New Skills - October 4, 2026 (Evening)"
description: "Skills.sh sweep (Oct 4 evening): 708 skills, 9 NEW below floor; 1 un-parked guide - Moonlight Lupin Agent Skills (35-skill Hermes suite, ~3.4K installs)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct4-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-04"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 4, 2026 (Evening Sweep)

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. This evening pass closed out Oct 4 after the morning catch-up cycle (the 04:00 run was lost to the fleet SSL incident and recovered at 16:33).

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 708 (15 queries, 0 failed) |
| NEW (not in catalog) | 9 |
| NEW >= 100 installs | 0 |
| PARTIAL (source known, skill not cataloged) | 214 |
| PARTIAL >= 100 installs | 93 (backlog deferred) |
| New publisher guides | 1 (watch-list re-qualification) |
| Roster reconciles | 0 |

## New Publisher Guides

### 1. Moonlight Lupin Agent Skills - Hermes-Native Skill Suite (un-parked)

**Source:** [moonlight-lupin/agent-skills](https://github.com/moonlight-lupin/agent-skills) (88⭐, 15 forks, MIT LICENSE; active) · **~3,354 installs** across 37 indexed listings · 36 SKILL.md files in-repo (35 installable skills)

A 35-skill collection built specifically for Hermes Agent - research, agent-ops, productivity, creative, mlops, devops, web-scraping - plus two plugins (skill-retrieval BM25 retrieval, lumen wiki). Parked on the Sep 29 evening sweep in the sub-500 class with a "watch for growth" note; re-verified tonight (hermes-onboarding was 1-8 installs at the Aug 26 park and is now 101; family combined 3,354) and un-parked per the watch-list re-qualification rule (same mechanics as fission-ai/openspec, Sep 29).

→ [Setup guide](/hermes/skills/catalog/moonlight-lupin-agent-skills-setup)

## NEW Candidates Below the Guide Floor

| Source | Listings | Installs | Note |
|---|---|---|---|
| costrict-plugins-repo/sickn33-antigravity-awesome-skills-antigravity-bundle-odoo-erp | 7 | 1 each | Re-host bundle of the documented sickn33 family (standing rejection class) |
| satnamrsm/https-github.com-sickn33-antigravity-awesome-skills | 3 | 1 each | Same re-host class |

All 9 NEW skills this run belong to these two sources (100% overlap with the morning run) and sit at 1 install each - far below the guide floor. Publisher follow-ups confirm 10 listings / 10 combined installs.

## Notes

- Watch-list audit: the three PARTIAL sources without catalog-guide hits were re-sized - fanthus/agent-skills (241 combined) stays below the meaningful floor, leoyeai/openclaw-master-skills (432) stays in the standing OpenClaw exclusion class, and only moonlight-lupin/agent-skills (3,354) re-qualified.
- PARTIAL >=100 backlog: 93 rows across ~45 documented families - deferred to a dedicated roster-reconcile pass (policy unchanged from prior sweeps).
- skills.sh exposes per-skill security verdicts (Gen Agent Trust Hub / Socket / Snyk); sampled moonlight-lupin verdicts are mixed Pass/Warn and are recorded in the setup guide.
- Evening sweep mechanics: one-pass rg crossref on the Mac Mini, ~17s, 0 failed queries; repo pulled to 913177e22 before the run.

---

*Sweep run: Oct 4, 2026, skills-monitor cron (evening). Includes the un-parked moonlight-lupin guide.*
