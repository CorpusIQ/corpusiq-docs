---
title: "New Skills — August 17, 2026"
description: "skills.sh sweep: Brian Lovin Agent Config (33.6K, 19), last30days (32.7K, 3), Herdr (28.1K, 5), Web Access (15.7K), Stop Slop (10.6K), Avoid AI Writing (1.6K, locally installed) — 6 publisher clusters, 30 skills, 6 setup guides."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug17-2026/"
robots: "index,follow"
last_updated: "2026-08-17"
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills"]
sweep_id: "2026-08-17"
new_publishers: 6
new_skills: 30
guides_drafted: 6
---

# New Skills — August 17, 2026

First skills.sh sweep of August 17. 40 API queries collected 3,944 unique skills; all top-120 clusters (≥2K installs) are in-tree including the same-day-triage recovery pass, so this sweep's entire batch came from the **carry-over queue re-verification** — five clusters parked in prior sweeps whose publisher pages told a different story than their queue entries, plus one locally installed skill flagged as a docs gap by the August 17 ecosystem scan.

## New Publisher Clusters — Guided This Sweep

| Cluster | Skills | Installs | Tier | Guide |
|---|---|---|---|---|
| brianlovin/agent-config | 19 | 33.6K | 🟢 | [Brian Lovin Agent Config Setup](/hermes/skills/catalog/brianlovin-agent-config-setup/) |
| mvanhorn/last30days-skill | 3 | 32.7K | 🟡 | [last30days Skill Setup](/hermes/skills/catalog/last30days-skill-setup/) |
| herdrdev/herdr | 5 | 28.1K | 🟢 | [Herdr Skills Setup](/hermes/skills/catalog/herdr-skills-setup/) |
| eze-is/web-access | 1 | 15.7K | 🟡 | [Web Access Skill Setup](/hermes/skills/catalog/web-access-skill-setup/) |
| hardikpandya/stop-slop | 1 | 10.6K | 🟢 | [Stop Slop Setup](/hermes/skills/catalog/stop-slop-setup/) |
| conorbronsdon/avoid-ai-writing | 1 | 1.6K | 🟡 | [Avoid AI Writing Setup](/hermes/skills/catalog/avoid-ai-writing-setup/) |

## Method Notes

- API sweep: 40 queries → 3,944 unique skills → top-120 clusters all in-tree, including the recovery diff excluding `new-aug16-2026*` dirs (0 clusters only mentioned in the newest batch pages).
- Hot leaderboard (1H delta) surfaced open.feishu.cn/lark-approval, vercel-labs/skills, prisma/skills, google/agents-cli, wind-skills, larksuite/cli, mattpocock/skills — **all already guided** (lark-feishu-skills-setup, find-skills-setup, prisma catalog, google-agents-cli-setup, wind-skills-setup, mattpocock-skills-setup).
- The queue-underestimation / stale-assessment pattern fired again: five carry-over clusters re-verified on publisher pages were at or above the drafting bar with real numbers — brianlovin/agent-config parked at 13.3K (publisher: 33.6K across 19 skills), last30days parked un-quantified (publisher: 32.7K, 58.4K GitHub stars), herdr parked un-quantified (publisher: 28.1K, 29.7K stars), web-access parked at 15.6K (publisher: 15.7K), stop-slop parked at 10.4K (publisher: 10.6K).
- avoid-ai-writing drafted below the usual install bar (1.6K) on explicit justification: installed in the CorpusIQ production Hermes profile, 3.0K GitHub stars, and flagged as a docs gap by the August 17 ecosystem scan. Guide is verified against the locally installed SKILL.md (modes: rewrite/detect/edit).
- Security audits per top skill: herdr 🟢 (3/3 Pass), stop-slop 🟢 (3/3 Pass), brianlovin/agent-config 🟢 (simplify 3/3 Pass), avoid-ai-writing 🟡 (Snyk Warn), web-access 🟡 (Socket Warn, Snyk Fail named), last30days 🟡 (Gen Agent Trust Hub Fail + Snyk Fail named).

## Evaluated and Queued (next sweep)

| Cluster | Installs | Reason parked |
|---|---|---|
| uni-stack/uniwind | 5.4K | Flat (5.4K Aug 16); RN tooling, at bar |
| asksurf-ai/surf-skills | 3.8K | Flat; crypto-adjacent |
| ningzimu/codex-ppt-skill | 3.6K | Flat; below bar |
| streakyc/googleworkspacecli | 1.8K | Flat; 95 skills but tiny install total |
| steel-dev/skills | 1.3K | Flat; browser-automation vendor, brand watch |
| zhaono1/agent-playbook | — | Top skill already guided via charon-fan; rest ≤1.2K |

Carry-over parked: amazonappdev/devices-agent-skills, dmmulroy/anti-slop. Mac Mini remained unreachable (ping loss, SSH timeout) — sweep ran entirely from the Spark canonical clone.

## Notable Signals for CorpusIQ

- **brianlovin/agent-config** is the strongest design-engineering quality suite catalogued: simplify (function-preserving code refinement), deslop (UI slop removal), and knip (dependency hygiene) map one-to-one onto our code-quality and design-polish goals.
- **last30days** gives our ecosystem scans a recency-window research pattern — "what moved in the last 30 days" as a first-class question.
- **herdr** turns terminal panes into an agent-queryable session — directly useful for our multi-agent Spark workflows.
- **web-access** drives an existing Chrome/Edge session via CDP with preserved login state — the same property our Mac Mini Playwright context provides, available to any agent as a third fallback path.
- **stop-slop** and **avoid-ai-writing** pair as the content-quality gate layer: compressed ruleset plus audited multi-mode workflow, both aligned with our existing content-voice rules and slop scoring.

## Index State After Sweep

- catalog/index.md: +6 entries
- marketplace/index.md: header 882 → 888, footer 933 → 939
- last_updated on both indexes: 2026-08-17
