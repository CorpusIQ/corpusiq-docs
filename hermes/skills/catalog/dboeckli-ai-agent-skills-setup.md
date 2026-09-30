---
title: "Dboeckli AI Agent Skills - CLI & Best Practices Setup"
description: "Setup guide for dboeckli/ai-agent-skills - 5 AI-agnostic agent skills for Claude Code best practices, SKILL.md authoring, project references, and cron planning. ~11K installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dboeckli-ai-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "skill authoring", "claude code", "cron"]
---

# Dboeckli AI Agent Skills - Setup Guide

**Source:** [dboeckli/ai-agent-skills](https://github.com/dboeckli/ai-agent-skills) (0⭐, MIT, master branch)
**Skill:** `dboeckli/ai-agent-skills` (5 installable skills, 11,058 combined installs)
**Publisher:** Dominique Boeckli ([dboeckli](https://github.com/dboeckli))
**Category:** Skill Authoring / Claude Code Workflow / GitHub Automation
**Quality Tier:** 🔵 Community (published in good faith, minimal external verification - verified Sep 29, 2026)

Five reusable skills in the open SKILL.md format, deliberately Claude-free in their dependencies - everything runs on standard `git`, `gh`, and shell tools, so any agent host that reads SKILL.md directories (including Hermes Agent) can use them. Covers Claude Code usage patterns, SKILL.md authoring discipline, local project-reference lookup, GitHub Actions cron planning, and an Apache Camel version compatibility matrix generator. Repo README is German; skill content is English.

---

## Installation

```bash
# Full suite
npx skills add dboeckli/ai-agent-skills

# Or copy skills directly (repo layout: .claude/skills/<name>/)
git clone https://github.com/dboeckli/ai-agent-skills
```

## Roster - All 5 Skills

| Skill | Installs | Does |
|---|---|---|
| project-references | 2,584 | Look up conventions/patterns from local checkouts under `~/projects/referenzen/`; generate a GitHub Actions trigger overview (push, PR, schedule/cron) as a Markdown report |
| skill-best-practices | 2,510 | Create, structure, and improve SKILL.md files: frontmatter, trigger descriptions, testing, troubleshooting |
| cc-best-practices | 2,456 | Effective Claude Code use: context management, explore-plan-implement workflow, prompting, common failure patterns |
| camel-matrix | 2,452 | Generate Apache Camel / Spring Boot / CXF version compatibility matrices via a bundled shell script |
| cron-schedule-planner | 1,056 | Map GitHub Actions cron schedules across repos (via `gh` or checkouts), classify job intensity, propose de-peaking into low-load windows (Markdown report with hourly histogram) |

Each skill ships a `references/` directory with supporting patterns (search-patterns, commands, classification-and-timezones).

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Skill library maintenance** | `skill-best-practices` aligns with CorpusIQ's skill-creation standards (frontmatter, triggers, testing) |
| **Cron fleet planning** | `cron-schedule-planner`'s de-peaking histogram maps directly to the multi-cron Hermes fleet scheduling |
| **Cross-repo conventions** | `project-references` for consistent patterns across CorpusIQ's repos |

## Limitations / Verification

- 0-star personal repository; skills verified structurally (frontmatter + references) but not community-audited
- README documentation is German; SKILL.md content is English
- `project-references` assumes the author's `~/projects/referenzen/` checkout layout - adapt the path for your own setup
- Verify: `npx skills add dboeckli/ai-agent-skills --list` shows 5 skills

## Security

MIT license (Copyright 2026 Dominique Boeckli). No skills.sh security audits published (verified Sep 29, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Riekelt Principal Engineer Setup](/docs/hermes/skills/catalog/riekelt-principal-engineer-setup)
- [Skill Vetting](/docs/hermes/skills/catalog/skill-vetter-setup)
- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Skills Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
