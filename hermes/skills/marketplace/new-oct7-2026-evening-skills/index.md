---
title: "New Skills - October 7, 2026 (Evening)"
description: "Skills.sh sweep (Oct 7 evening): 441 skills checked; 1 new publisher guide - Callstack Agent Skills (official React Native suite, ~80.7K installs)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct7-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-07"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 7, 2026 (Evening Sweep)

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. Follows the Oct 7 morning run (720 unique, 0 above the guide floor, silent) and repairs a crossref tooling defect found during this pass (see Notes).

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 441 (stability re-run; first pass 440; 15 queries, 0 failed) |
| NEW (not in catalog) | 31 |
| NEW >= 100 installs | 0 (all below floor, max 7 installs) |
| PARTIAL (source known, skill not cataloged) | 140 raw / 122 after tooling fix |
| PARTIAL >= 100 installs | 12 raw rows / 0 after tooling fix |
| New publisher guides | 1 |
| Roster reconciles | 0 |

## New Publisher Guides

### 1. Callstack Agent Skills - React Native Skills (official)

**Source:** [callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills) (1,663⭐, MIT LICENSE; very active - pushed Oct 6, 2026) · **~80,715 installs** across 15 indexed listings · 13 SKILL.md files in-repo (9 first-party + validate-skills tooling + 3 vendored)

The official Callstack skill suite for React Native: three plugin bundles (Building, Testing, Migrating) covering performance optimization, framework upgrades, React Navigation 7, TV apps, library authoring, GitHub Actions CI artifact builds, device automation, exploratory QA, migration assessment, and brownfield adoption. Top skills: react-native-best-practices (28,198), upgrading-react-native (11,583), github-actions (9,834). First seen in July and deferred then as below-floor; re-qualified Oct 7 at roughly 4x its July size.

→ [Setup guide](/hermes/skills/catalog/callstackincubator-agent-skills-setup)

## NEW Candidates Below the Guide Floor

| Source | Listings | Installs | Note |
|---|---|---|---|
| l3ad3r1/hermes-skills | 3 | 13 combined (7 top: agent-reach) | Hermes-named personal set - below floor |
| noahnan-max/reading-pipeline | 1 | 6 | Personal reading pipeline - below floor |
| erencoding/cloakbrowser-hermes-skill | 1 | 5 | Browser skill - below floor |
| scavio-ai/hermes-agent | 1 | 5 | competitive-intel-brief - below floor |
| (remaining 24 listings) | 24 | all <= 4 installs | personal / dormant single-skill repos - below floor |

## Notes

- **Crossref tooling fix (this cycle):** the fast one-pass crossref mis-reported covered names as PARTIAL when a shorter collected name (for example `github`, `setup`, `migrate`) masked a longer literal in the single bulk `rg` pass. The repair pass now re-probes both containment directions; 18 previously-PARTIAL rows reclassify as covered, and PARTIAL >= 100 drops from 12 rows to 0. Reclassified examples verified against the tree: nousresearch/hermes-agent `github-pr-workflow`, `github-code-review`, `github-issues`, `github-auth`, `github-repo-management`, `hermes-agent-skill-authoring`; garrytan/gstack `setup-gbrain`; garrytan/gbrain `cron-scheduler`; plastic-labs/honcho `migrate-honcho-ts`; reactnativecn/react-native-update-skill `react-native-update`; podo/design-agent-skills `p5js-hermes`.
- **Zero-catalog audit:** before the fix, one PARTIAL >= 100 source lacked a catalog-guide hit (callstackincubator/agent-skills) - resolved this cycle with the new setup guide. The standing OpenClaw/Azure source set audited in prior sweeps (irangareddy/openclaw-essentials, leoyeai/openclaw-master-skills, phenomenoner/openclaw-agent-optimize, microsoftdocs/agent-skills, arthurzakirov/agentdesk) was not returned in tonight's served windows; no re-qualifications this pass.
- **Collection window:** this evening's served set is 440/441 unique versus 706-733 on every run from Sep 29 through Oct 7 morning. Two consecutive runs agree, so the change is on the skills.sh serving side - several large documented publishers are absent from tonight's windows while new listings surfaced (all additions stayed below the guide floor). Classification remains valid for the items served; monitoring the next runs.
- skills.sh exposes per-skill security verdicts (Gen Agent Trust Hub / Socket / Snyk); the Callstack samples are recorded in the setup guide (4 of 5 sampled all-Pass; one Socket Warn on github-actions).
- Evening sweep mechanics: one-pass rg crossref on the Mac Mini; 0 failed queries; duplicate defense checked first (no Oct 7 skills-sweep commit at the remote tip c5e16c794).

---

*Sweep run: Oct 7, 2026, skills-monitor cron (evening). Includes the Callstack Agent Skills setup guide.*
