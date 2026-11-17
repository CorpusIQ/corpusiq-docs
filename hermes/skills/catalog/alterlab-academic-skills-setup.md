---
title: "AlterLab Academic Skills - Research to Submission"
description: "alterlab-ieu/alterlab-academic-skills - 6.8K combined installs across 96 indexed listings: keyless academic skills spanning 18 research domains."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/alterlab-academic-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "academic research", "scientific writing"]
---

# AlterLab Academic Skills - Setup Guide

**Source:** [alterlab-ieu/alterlab-academic-skills](https://www.skills.sh/alterlab-ieu/alterlab-academic-skills) via skills.sh - 6.8K combined installs across 96 indexed listings; first seen Nov 16, 2026 (Nov 16 evening sweep)
**GitHub:** 87 stars, MIT license, `main` branch, last pushed 2026-11-11, 241 skills under `skills/<domain>/<skill>/SKILL.md` with an eval per skill
**Category:** Academic research - literature review, writing, citation integrity, and 38 scientific databases
**Quality Tier:** 🟡 Yellow - 6 of the 24 sampled skills carry a Snyk Warn; the rest pass all three scanners.

AlterLab Academic Skills is a 241-skill library for academic work, built by AlterLab Creative Technologies Laboratory at Izmir University of Economics. It spans 18 domains: literature review, manuscript writing, citation checking, research design and statistics, scientific databases and toolkits, and the Turkish academic system (YOK, UAK, DergiPark, TUBITAK). Every skill ships an executable eval.

The library is keyless by default: no API key, account, or login is required, and each optional credential is declared in the skill's metadata. The whole catalog was graded behaviorally against a live model, with 90% of answers passing with a skill against 52% without. Four core pipeline skills carry non-commercial licenses from their upstream, so check a skill's license before redistributing it.

## Installation

The README recommends Claude Code plugins:

```sh
/plugin marketplace add AlterLab-IEU/AlterLab-Academic-Skills
/plugin install alterlab-essentials@alterlab-academic-skills
/plugin install alterlab-turkish-academia@alterlab-academic-skills
/reload-plugins
```

Or a plain install into a skills directory (needs python3):

```bash
git clone https://github.com/AlterLab-IEU/AlterLab-Academic-Skills.git && cd AlterLab-Academic-Skills
scripts/install.sh --list
scripts/install.sh core/alterlab-citation-verifier
```

With the skills CLI: `npx skills add alterlab-ieu/alterlab-academic-skills`. Skills a selected skill depends on are installed with it (`--no-deps` to skip).

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| alterlab-teaching-design | 125 | Design courses, syllabi, rubrics, and assessments with backward design and constructive alignment. |
| alterlab-thesis-supervisor | 95 | Supervise theses end to end, from proposal through defense, chapter by chapter. |
| alterlab-survey-design | 94 | Build questionnaires, Likert scales, sampling plans, and instrument validation. |
| alterlab-literature-review | 87 | Run systematic literature reviews with PRISMA flow tracking and risk-of-bias assessment. |
| alterlab-qualitative-methods | 82 | Design and analyze qualitative research: thematic analysis, grounded theory, IPA, and more. |
| alterlab-mixed-methods | 81 | Plan convergent, explanatory, and other mixed-method designs and integrate qual and quant. |

The remaining 90 indexed listings range from 67 to 78 installs.

## Why This Matters for Hermes Agents

This is one of the largest academic skill sets an agent can pull from, and its value is the eval discipline behind it. All 241 skills ship a structurally valid eval file checked in CI on every PR, and the whole set was graded behaviorally against a live model. The citation verifier reports existence and metadata separately, never conflating a resolving DOI with a verified author, and an entry it cannot check is unverified rather than a pass. The seven multi-agent workflows return a status plus a coverage account, so a builder sees requested, completed, failed, and unresolved work at a glance. The keyless-by-default install model is enforced by a CI script, which cuts credential sprawl for agents that fan out across many domains. For Hermes agents, the reusable pattern is the one the repo applies to itself: encode the check as a gate, run it on every change, and refuse to claim a pass when the check did not run.

## Usage

| You say | What happens |
|---|---|
| "Use AlterLab skills to turn this topic into a researchable question" | alterlab-skill-finder picks a skill and says which and why, then alterlab-deep-research runs in Socratic mode. |
| "Check that every reference exists and is not retracted" | alterlab-citation-verifier resolves each reference against Crossref and other indexes and flags retractions. |
| "Set up a PRISMA search and screening plan" | alterlab-literature-review builds the search strategy, screening steps, and evidence tables. |
| "Which test fits this design, and what does it assume?" | alterlab-test-selection-guard routes to the right test and states its assumptions. |
| "Draft a point-by-point response to these comments" | The /alterlab-workflows:rebuttal workflow writes a point-by-point reply with a consistency pass. |
| "Draft the 1001 proposal" | alterlab-tubitak-proposal scaffolds a TUBITAK proposal against the funder's review criteria. |

## Verification

Check the skill files before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/alterlab-ieu/alterlab-academic-skills/main/skills/core/alterlab-citation-verifier/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/alterlab-ieu/alterlab-academic-skills/main/skills/core/alterlab-deep-research/SKILL.md | head -20
```

Each skill is one `SKILL.md` under `skills/<domain>/<skill>/` with an `evals/evals.json` alongside it; confirm the path exists in the current tree before copying a specific skill.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| alterlab-teaching-design | Pass | Pass | Pass |
| alterlab-thesis-supervisor | Pass | Pass | Pass |
| alterlab-survey-design | Pass | Pass | Warn |
| alterlab-literature-review | Pass | Pass | Warn |
| alterlab-qualitative-methods | Pass | Pass | Warn |
| alterlab-mixed-methods | Pass | Pass | Pass |
| alterlab-social-science-methods | Pass | Pass | Pass |
| alterlab-peer-review | Pass | Pass | Pass |
| alterlab-scientific-schematics | Pass | Pass | Pass |
| alterlab-scientific-viz | Pass | Pass | Pass |
| alterlab-research-grants | Pass | Pass | Pass |
| alterlab-research-ethics | Pass | Pass | Warn |
| alterlab-open-science | Pass | Pass | Warn |
| alterlab-matplotlib | Pass | Pass | Pass |
| alterlab-infographics | Pass | Pass | Warn |
| alterlab-academic-career | Pass | Pass | Pass |
| alterlab-venue-templates | Pass | Pass | Pass |
| alterlab-sympy | Pass | Pass | Pass |
| alterlab-scientific-writing | Pass | Pass | Pass |
| alterlab-digital-humanities | Pass | Pass | Pass |
| alterlab-zarr | Pass | Pass | Pass |
| alterlab-statsmodels | Pass | Pass | Pass |
| alterlab-scholar-eval | Pass | Pass | Pass |
| alterlab-pptx-posters | Pass | Pass | Pass |

All 24 sampled skills pass the Gen Agent Trust Hub and Socket; 6 carry a Snyk Warn and none fail.

## Limitations

- Snapshot data, verified Nov 16, 2026: 6,796 combined installs across 96 indexed listings; 87 GitHub stars; MIT; last pushed 2026-11-11. Counts drift over time.
- Only 96 of the 241 skills are indexed on skills.sh at snapshot, so install counts cover a subset of the catalog.
- Per-skill licenses differ from the repo's MIT (201 MIT, 19 Apache-2.0, 4 CC-BY-NC-4.0, and smaller counts of others); four core pipeline skills are non-commercial from their upstream.
- 6 of the 24 sampled skills carry a Snyk Warn; the other 72 indexed listings were not sampled in the verdict set.
- Behavioral eval figures (90% with a skill against 52% without) are 4.0.0 numbers on synthetic fixtures and do not validate the whole catalog.

## Related

- [Academic Research Skills](/hermes/skills/catalog/academic-research-skills-setup)
- [Academic Writing Skills](/hermes/skills/catalog/academic-writing-skills-setup)
- [llm-wiki](/hermes/skills/catalog/llm-wiki-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with alterlab-skill-finder; describe the task and it picks the right skill and explains why.
- Prefer the plugin install for domain bundles; the plain install pulls a skill's dependencies with it.
- Run the citation verifier before submission; unverified entries are flagged, never silently passed.
- Check the license frontmatter per skill; the repo is MIT but four core skills are CC-BY-NC-4.0.
- Install only the domains you need; 38 database skills add up fast.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
