---
title: "Skill From Masters - Domain Expert Methodology Suite Setup"
description: "Setup guide for gbsoss/skill-from-masters - convert proven methodologies from expert GitHub repos and notebooks into reusable agent skills. 2K+ installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/skill-from-masters-setup/"
robots: "index,follow"
last_updated: "2026-09-30"
tags: ["hermes skill", "agent skill", "skill setup", "skill authoring", "knowledge extraction", "github"]
---

# Skill From Masters - Domain Expert Methodology Suite Setup - Setup Guide

**Source:** [gbsoss/skill-from-masters](https://github.com/gbsoss/skill-from-masters) (1,586⭐, MIT, main branch, updated 2026-09-29)
**Skill:** `gbsoss/skill-from-masters` (4 installable skills, 2.1K combined installs)
**Publisher:** gbsoss
**Category:** Skill Authoring / Knowledge Extraction
**Quality Tier:** 🔵 Community (good-faith publisher, minimal external verification - verified Sep 30, 2026)

Skill From Masters builds agent skills from proven expert methodologies rather than generic instructions. It extracts working patterns from domain-expert GitHub repositories and notebooks, then converts them into reusable skills in the open SKILL.md format, so agents inherit battle-tested approaches instead of re-deriving them. The suite ships four skills: the core skill-from-masters builder, a search-skill for locating existing skills, a skill-from-github extractor, and a skill-from-notebook converter for Jupyter-based expert workflows.

---

## Installation

```bash
# Full suite
npx skills add gbsoss/skill-from-masters

# Or clone the repo and copy skills directly
git clone https://github.com/gbsoss/skill-from-masters
```

Verify the indexed skills with `npx skills add gbsoss/skill-from-masters --list`.

## Roster - All 4 Skills

| Skill | Installs | Does |
|---|---|---|
| skill-from-masters | 754 | Core builder: extracts a proven methodology from an expert source and scaffolds it into a reusable SKILL.md skill |
| search-skill | 483 | Finds existing skills by topic before authoring a new one, avoiding duplicates in the skill library |
| skill-from-github | 480 | Converts patterns and workflows from a GitHub repository into an installable agent skill |
| skill-from-notebook | 372 | Turns expert Jupyter notebook workflows into documented, reusable agent skills |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Skill library growth** | `skill-from-github` converts proven patterns from high-signal repos into candidate skills for the Hermes catalog |
| **Notebook workflow capture** | `skill-from-notebook` turns recurring data-analysis notebook workflows into reusable skills |
| **Duplicate prevention** | `search-skill` checks existing skills before authoring, keeping the catalog free of near-duplicates |

## Limitations / Verification

- All four skills target skill authoring and knowledge extraction, with nothing for general agent tasks
- Per-skill install counts are modest (372 to 754), so community validation is limited
- Extraction quality depends on the source repo or notebook being well structured
- Verify: `npx skills add gbsoss/skill-from-masters --list` shows 4 skills

## Security

MIT license. No skills.sh security audits published (verified Sep 30, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Claude MPM Skills Setup](/docs/hermes/skills/catalog/claude-mpm-skills-setup)
- [Dboeckli AI Agent Skills Setup](/docs/hermes/skills/catalog/dboeckli-ai-agent-skills-setup)
- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Skills Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
