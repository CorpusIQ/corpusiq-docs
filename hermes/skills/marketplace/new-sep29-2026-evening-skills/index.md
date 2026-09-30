---
title: "Sep 29, 2026 Evening - 3 New Skill Publisher Clusters"
description: "Skills.sh sweep: 3 new publisher guides (Riekelt Principal Engineer 120K, OpenSpec 70.7K⭐ un-parked, Dboeckli AI Agent Skills 11K)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-sep29-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "skill marketplace", "skills.sh"]
---

# Sep 29, 2026 (Evening) - 3 New Skill Publisher Clusters

**Discovered:** 3 new publisher guides (31 skills, ~173K combined installs) · **Un-parks:** 1 (OpenSpec) · **Roster reconciles:** 0 (backlog noted)

Evening sweep of the skills.sh REST API across 15 queries (one-pass ripgrep cross-reference on the Mac Mini, ~2 min). 717 unique skills collected, 0 failed queries. Tiered crossref: 24 NEW / 211 PARTIAL. NEW ≥100 installs: 2 clusters; PARTIAL ≥100: 93 rows across 45 already-documented families. One Aug 18 "watch for growth" park (fission-ai/openspec) cleared its threshold and was guided.

## New Publishers at a Glance

| # | Publisher | Top Skill | Installs | Category | Setup Guide |
|---|-----------|-----------|----------|----------|-------------|
| 1 | riekelt/principal-engineer | principal-engineering | 10,973 | Engineering Discipline | ✅ |
| 2 | fission-ai/openspec | openspec-propose | 3,321 | Spec-Driven Development | ✅ |
| 3 | dboeckli/ai-agent-skills | project-references | 2,584 | Skill Authoring / Workflow | ✅ |

## Setup Guides Created

1. **[Riekelt Principal Engineer Setup](/docs/hermes/skills/catalog/riekelt-principal-engineer-setup)** - 11-skill engineering-discipline plugin (~120K combined): verification-as-done, no silent failures, one source of truth, scope-to-trigger. Multi-platform manifests, change-verifier subagent, evals, semantic-release. 🟡 (no repo LICENSE file disclosed).
2. **[OpenSpec Skills Setup](/docs/hermes/skills/catalog/fission-openspec-skills-setup)** - 15 SDD skills (~42K combined) from the 70,706⭐ MIT OpenSpec project. **Un-parked** from the Aug 18 watch-list (8.5K → 42K, ~5x growth). 🟡 authority-justified.
3. **[Dboeckli AI Agent Skills Setup](/docs/hermes/skills/catalog/dboeckli-ai-agent-skills-setup)** - 5 AI-agnostic skills (~11K combined, MIT): SKILL.md authoring, Claude Code patterns, project references, cron de-peaking planner, Camel version matrices. 🔵 Community.

## Skipped / Parks

| Item | Reason parked |
|---|---|
| 22 NEW below floor (<100 installs, max 23) | Below the 100-install guide threshold (standing rule) |
| OpenClaw-named PARTIAL repos (irangareddy/openclaw-essentials 486, leoyeai/openclaw-master-skills 309, phenomenoner/openclaw-agent-optimize 165, sundial-org 169, prompt-security/clawsec 116) | OpenClaw exclusion class (standing, Sep 12) |
| moonlight-lupin/agent-skills (news-monitoring, 101) | Sub-500 park |
| wihy/hermes-agent-skill (hermes-agent, 570) | Already documented in [Hermes Agent Setup](/docs/hermes/skills/catalog/hermes-agent-setup) index |
| googleworkspace/cli persona-hr-coordinator (28.4K) | Family documented across guides (Sep 29 daytime reconcile) |

**Reconcile backlog:** 93 PARTIAL rows ≥100 installs remain across 45 documented publisher families (e.g. github/awesome-copilot 27 rows, nousresearch/hermes-agent 7 rows - all verified covered in the official-skills-batch guide). Deferred to a dedicated roster-reconcile pass; no new guides required.

## Quick Install

```bash
npx skills add riekelt/principal-engineer
npx skills add fission-ai/openspec
npx skills add dboeckli/ai-agent-skills
```

## Why This Matters for Hermes

**Principal Engineer** is the sweep's most directly relevant find for Hermes operators: its discipline stack (verification-as-done, no silent failures, one source of truth, scope-to-trigger) is the same doctrine CorpusIQ runs its own agent fleet on - now available as installable skills with evals. **OpenSpec** graduated its watch-list park with 5x growth; at 70.7K⭐ it is a canonical SDD workflow that turns agent feature work into spec-reviewable, archiveable changes - directly useful for CorpusIQ's agent-built product pipeline. **Dboeckli** contributes niche but practical workflow skills, notably `cron-schedule-planner`'s cron de-peaking analysis for multi-repo GitHub Actions fleets.

*← [Skills Marketplace](/docs/hermes/skills/marketplace) | [Skills Catalog](/docs/hermes/skills/catalog) →*
*Powered by CorpusIQ*
