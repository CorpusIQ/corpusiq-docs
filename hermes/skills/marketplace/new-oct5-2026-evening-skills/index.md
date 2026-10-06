---
title: "New Skills - October 5, 2026 (Evening)"
description: "Skills.sh sweep (Oct 5 evening): 724 skills, 2 NEW; 1 new publisher guide - Goldsky Agent Skills (19 official blockchain pipeline skills, ~19.8K installs)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct5-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-05"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 5, 2026 (Evening Sweep)

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The evening pass follows the Oct 5 morning run (730 unique / 0 NEW, silent) and the Oct 4 evening un-park cycle.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 724 (15 queries, 0 failed) |
| NEW (not in catalog) | 2 |
| NEW >= 100 installs | 2 |
| PARTIAL (source known, skill not cataloged) | 198 |
| PARTIAL >= 100 installs | 64 rows / 46 sources (backlog deferred) |
| New publisher guides | 1 |
| Roster reconciles | 0 |

## New Publisher Guides

### 1. Goldsky Agent Skills - Blockchain Data Pipelines (official)

**Source:** [goldsky-io/goldsky-agent](https://github.com/goldsky-io/goldsky-agent) (12⭐, 1 fork, MIT LICENSE; very active - pushed Oct 5, 2026) · **~19,805 installs** across 29 indexed listings · 19 SKILL.md files in-repo

The official Goldsky plugin for AI agents: build, deploy, and debug blockchain data pipelines across the full product surface - Turbo pipelines, Mirror, Subgraphs, Compose (offchain-to-onchain TypeScript apps), Edge RPC and Boost, Feeds, datasets, and secrets. Pairs builder and doctor skills per product (turbo-builder / turbo-doctor, subgraph-builder / subgraph-doctor, and so on) plus a cross-product onchain-automation router. Top skills: turbo-builder and turbo-pipelines at 1,113 installs each.

→ [Setup guide](/hermes/skills/catalog/goldsky-agent-skills-setup)

## NEW Candidates Below the Guide Floor

| Source | Listings | Installs | Note |
|---|---|---|---|
| bussgrowwithlucky-crypto/openclaw-skill-file-manager | 4 | 158 combined (155 top) | OpenClaw-named single-maintainer set (0⭐, no license, dormant since Feb 2026, all-Pass verdicts) - OpenClaw exclusion class holds; below floor |

## Notes

- Zero-catalog audit: 4 PARTIAL >=100 sources without catalog-guide hits, all standing dispositions (irangareddy/openclaw-essentials 485, leoyeai/openclaw-master-skills 307, phenomenoner/openclaw-agent-optimize 165 - OpenClaw exclusion class; arthurzakirov/agentdesk 163 - below-floor dormant personal publisher). No re-qualifications this pass.
- PARTIAL >=100 backlog: 64 rows across documented families - deferred to a dedicated roster-reconcile pass (policy unchanged from prior sweeps).
- skills.sh exposes per-skill security verdicts (Gen Agent Trust Hub / Socket / Snyk); the goldsky samples are recorded in the setup guide (Trust Hub Pass on all four sampled; Socket/Snyk mixed).
- Evening sweep mechanics: one-pass rg crossref on the Mac Mini; 0 failed queries; duplicate defense checked first (no Oct 5 sweep commit at remote tip ce5708496).

---

*Sweep run: Oct 5, 2026, skills-monitor cron (evening). Includes the Goldsky Agent Skills setup guide.*
