---
title: "OpenSpec Skills - Spec-Driven Development Suite Setup"
description: "Setup guide for fission-ai/openspec - 15 spec-driven development skills for AI coding agents from the 70.7K-star MIT OpenSpec project. ~42K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/fission-openspec-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "spec-driven development", "sdd", "openspec"]
---

# OpenSpec Skills - Setup Guide

**Source:** [fission-ai/openspec](https://github.com/Fission-AI/OpenSpec) (70,706⭐, MIT, active CI)
**Skill:** `fission-ai/openspec` (15 skills.sh-indexed skills, 42,400 combined installs; 16 SKILL.md files in-repo)
**Publisher:** [Fission AI](https://github.com/Fission-AI) - OpenSpec maintainers
**Category:** Spec-Driven Development / Workflow / Code Quality
**Quality Tier:** 🟡 Authority-justified (70.7K⭐ flagship open-source project, MIT, CI + SECURITY.md; no skills.sh security verdicts published - verified Sep 29, 2026)

OpenSpec is "the most loved spec framework" for AI coding assistants: spec-driven development (SDD) where changes are proposed as machine-readable spec deltas, reviewed against them, then archived. The skills automate the full change lifecycle - propose, apply, verify, archive - plus docs drafting, releases, and onboarding. Ships as Agent Skills-format SKILL.md files in the main repo (`skills/` and `.agents/skills/`); the CLI is `@fission-ai/openspec` (npm).

> **Un-parked:** flagged "watch for growth" in the Aug 18, 2026 sweep (13 skills, ~8.5K combined). Grown ~5x to 42K combined installs - now guided.

---

## Installation

```bash
# Skills only (any Agent Skills host, including Hermes Agent)
npx skills add fission-ai/openspec

# Full CLI (required for the native openspec workflow)
npm install -g @fission-ai/openspec
```

## Roster - All 15 Indexed Skills

| Skill | Installs | Does |
|---|---|---|
| openspec-propose | 3,321 | Propose a new spec-driven change from requirements |
| openspec-explore | 3,321 | Explore existing specs and change history |
| openspec-archive-change | 3,308 | Archive a completed change into the spec baseline |
| openspec-apply-change | 3,296 | Apply/implement an approved change against specs |
| openspec-update-change | 3,244 | Update an in-flight change's spec deltas |
| openspec-sync-specs | 3,197 | Sync code-level specs with the spec repository |
| openspec-verify-change | 2,890 | Verify implementation matches the change's specs |
| openspec-continue-change | 2,860 | Resume a paused change |
| openspec-ff-change | 2,846 | Fast-forward a change through review |
| openspec-onboard | 2,838 | Onboard a new agent/contributor to the SDD workflow |
| openspec-bulk-archive-change | 2,818 | Batch-archive completed changes |
| release-openspec | 2,641 | Draft release notes from archived changes |
| draft-openspec-docs | 1,966 | Draft project docs from specs |
| write-openspec-docs | 1,927 | Write spec-derived documentation |
| verify-openspec-docs | 1,927 | Verify docs match current specs |

(In-repo but not skills.sh-indexed: `openspec-new-change`.)

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Agent-built features** | `openspec-propose` → `apply-change` → `verify-change` gives CorpusIQ spec-reviewable agent output instead of freeform diffs |
| **Docs freshness** | `draft/write/verify-openspec-docs` pairs with the docs-site pipeline for spec-derived content |
| **Client delivery** | SDD change logs (`release-openspec`) produce client-facing changelogs from archived changes |
| **Multi-agent handoffs** | `openspec-onboard` + `sync-specs` standardize context transfer between agent sessions |

## Limitations / Verification

- Full workflow needs the CLI (`npm i -g @fission-ai/openspec`); skills alone give the instructions, not the tooling
- Skills assume the OpenSpec project structure (specs/ directory conventions)
- Verify: `npx skills add fission-ai/openspec --list` shows 15 skills

## Security

70.7K⭐, MIT license, active CI, SECURITY.md and MAINTAINERS.md in-repo. No skills.sh security audits published (verified Sep 29, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Riekelt Principal Engineer Setup](/docs/hermes/skills/catalog/riekelt-principal-engineer-setup)
- [Task Observer Setup](/docs/hermes/skills/catalog/task-observer-setup)
- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Skills Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
