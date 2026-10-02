---
title: Riekelt Principal Engineer - Engineering Discipline Suite
description: "Setup guide for riekelt/principal-engineer - 11-skill engineering discipline plugin for AI coding agents: verification, grounding, scope control, safe ops. ~120K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/riekelt-principal-engineer-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "engineering discipline", "verification", "code quality"]
---

# Riekelt Principal Engineer - Setup Guide

**Source:** [riekelt/principal-engineer](https://github.com/riekelt/principal-engineer) (3⭐, v1.2.4, pushed Sep 2026)
**Skill:** `riekelt/principal-engineer` (11 installable skills, 120,279 combined installs)
**Publisher:** [riekelt](https://github.com/riekelt) (also ships the `riekelt/technical-writer` plugin)
**Category:** Engineering Discipline / Code Quality / Agent Safety
**Quality Tier:** 🟡 Beta (functional, author-tested, ships evals; no third-party audits - verified Sep 29, 2026)

"Engineering discipline as skills" - the judgment layer for coding agents. One core skill (`principal-engineering`) holds the hard rules, risk tiers, and routing; ten discipline skills build on it. Distilled conventions: evidence over theory, no silent error swallows, one home per fact, verification as the definition of done, and fixes that never outgrow their trigger. Ships as a multi-platform plugin (Claude Code, Codex, Cursor manifests) with a change-verifier subagent, `/verify` and `/preflight` commands, an evals suite, and semantic-release versioning.

---

## Installation

```bash
# Claude Code plugin
/plugin marketplace add riekelt/principal-engineer
/plugin install principal-engineer@principal-engineer

# Any Agent Skills host (including Hermes Agent)
npx skills add riekelt/principal-engineer

# Manual: point the platform plugin loader at plugins/principal-engineer/,
# or symlink plugins/principal-engineer/skills/* into the agent's skills directory
```

## Roster - All 11 Skills

| Skill | Installs | Does |
|---|---|---|
| principal-engineering | 10,973 | Core: pre-change checkpoint, hard rules, risk tiers, rule lifecycle |
| writing-unit-tests | 10,972 | Unit tests: behavior not implementation, names as claims, determinism, mock policy |
| verifying-before-done | 10,948 | Drive the change at its surface, run the proof, distrust green suites, own failing gates |
| grounding-before-coding | 10,942 | Map real code and data first - never guess conventions in unfamiliar code |
| guarding-architecture | 10,937 | Named, enforced invariants (statement, rationale, guard); violations mean redesign |
| keeping-one-source-of-truth | 10,933 | Derive rather than store; absorb duplicates of data, config, and state |
| testing-changes | 10,932 | Decide what tests a change owes; bug-regression pattern, discriminating assertions |
| scoping-changes | 10,931 | Size fixes to their trigger; decompose instead of descoping |
| operating-safely | 10,928 | Destructive-op guards, secrets hygiene, operator-owned process lifecycles |
| handling-failures | 10,925 | No-silent-swallows contract for error paths, catch blocks, fallbacks |
| adding-dependencies | 10,858 | Exhaust-what-you-have ladder, posture declarations, pin-and-prove updates |

Bundled: `change-verifier` subagent + `/verify` and `/preflight` commands.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Hermes agent quality gates** | `verifying-before-done` and `operating-safely` mirror CorpusIQ's verification-discipline and pre-flight gate patterns for cron/automation work |
| **Skill authoring** | `keeping-one-source-of-truth` and `guarding-architecture` align with CorpusIQ's skill-audit and consolidation doctrine |
| **Client dev work** | `testing-changes` + `writing-unit-tests` for shipping client integrations with proof, not vibes |
| **Docs repo health** | `scoping-changes` and `handling-failures` for the daily sweep/cron scripts that must fail loudly |

## Limitations / Verification

- Designed for coding agents first; the discipline rules transfer to any agent workflow via the Agent Skills-format SKILL.md files
- **No standalone LICENSE file in the repository** - the plugin manifest (`plugin.json`) declares MIT, but the repo root lacks a LICENSE.md (verified Sep 29, 2026). Confirm licensing before commercial reuse
- Single-author project (3⭐); install counts are high (~10.9K per skill) but community audits are not published
- Verify: `npx skills add riekelt/principal-engineer --list` shows 11 skills

## Security

No skills.sh security audits published (verified Sep 29, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [OpenSpec Skills Setup](/hermes/skills/catalog/fission-openspec-skills-setup)
- [Skill Best Practices](/hermes/skills/catalog/dboeckli-ai-agent-skills-setup)
- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
