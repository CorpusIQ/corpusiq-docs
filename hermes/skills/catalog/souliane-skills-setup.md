---
title: "Souliane Skills - Python, Django and Codebase Review Setup"
description: "souliane/skills - 3.4K combined installs: Python, Django and codebase review skills from a skill-driven development workflow."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/souliane-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "python", "django", "code review"]
---

# Souliane Skills - Setup Guide

**Source:** [souliane/skills](https://www.skills.sh/souliane/skills) via skills.sh - 3.4K combined installs across 9 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [souliane/skills](https://github.com/souliane/skills) - 1 star, MIT license, last pushed Oct 27, 2026, main branch; skills live as ac-<name>/SKILL.md directories with references/, rules/, and scripts/ subdirectories.
**Category:** Developer Workflows (Python / Django)
**Quality Tier:** 🟡 Yellow - 2 of 9 listings sampled: ac-python passes all three checks, ac-reviewing-codebase carries a Snyk Warn.

souliane/skills is a skill-driven development collection: a set of ac-* skills for Python coding, Django work, and unified codebase review. The repository has no published description and a single GitHub star, so treat it as a personal toolkit rather than a maintained product. The install mass concentrates on three skills: ac-python, ac-reviewing-codebase, and ac-django, each around 1,134 to 1,139 installs, with six further listings at 1 to 2 installs.

The three head skills are substantial packages: ac-python is generic Python guidance (style, typing, OOP, testing, tooling), ac-django is a Django 6.1 reference with a Django 5.2 LTS section, and ac-reviewing-codebase runs deterministic metrics plus LLM-driven architectural judgment across a portfolio of repos.

## Installation

The README documents installation through the skills CLI:

```bash
npx skills add https://github.com/souliane/skills --skill '*' -g -y
```

To install into multiple agent runtimes at once:

```bash
npx skills add https://github.com/souliane/skills --skill '*' -g -y --agent claude-code codex cursor github-copilot
```

Skills are versioned; the README's roster lists each skill's version (ac-reviewing-codebase 0.6.0, ac-django 0.2.0, and others).

## What It Provides

skills.sh publishes per-skill install counts for all 9 indexed listings. The 3 most-installed skills are listed below; the remaining 6 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| ac-python | 1,139 | generic Python coding guidelines: style, typing, OOP design, testing, and tooling outside Django |
| ac-reviewing-codebase | 1,135 | unified codebase review: deterministic metrics plus LLM-driven architectural judgment across a repo portfolio |
| ac-django | 1,134 | Django 6.1 reference with a Django 5.2 LTS section and optional DRF: Fat Models, migrations, transactions, security, testing |

The remaining 6 indexed listings range from 1 to 2 installs.

## Why This Matters for Hermes Agents

The three head skills encode judgment that a coding agent otherwise invents per session. ac-python is a stable style, typing, and testing baseline for any Python outside Django, with explicit instructions not to use it for Django-specific patterns. ac-django is the complementary Django reference: the Fat Models doctrine, migrations, transactions, security, and testing, which is where Django agents most often go wrong. ac-reviewing-codebase is the most unusual of the three: it audits a whole portfolio of repos with deterministic metrics (ruff, coverage, complexity, dependency staleness) and then applies LLM-driven architectural judgment, so it doubles as a quality gate for skills and code alike. The honest caveats are the low star count, the missing repository description, and the fact that only two of nine listings carry a skills.sh verdict, one of them a Warn.

## Usage

| You say | What happens |
|---|---|
| Review my Python code | Uses ac-python for style, typing, OOP, and testing guidelines |
| Audit this codebase | Uses ac-reviewing-codebase for metrics plus architectural judgment |
| Build this Django feature | Uses ac-django for models, migrations, transactions, and security |
| Check my skills for quality | Uses ac-reviewing-codebase to audit skill quality and repo health |
| What needs pushing? | Uses ac-reviewing-codebase for delivery status and repo status |
| Migrate my schema safely | Uses ac-django for migration and transaction guidance |

## Verification

Confirm the three head skills resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/souliane/skills/main/ac-python/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/souliane/skills/main/ac-reviewing-codebase/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/souliane/skills/main/ac-django/SKILL.md | head -40
```

All three URLs return 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ac-python | Pass | Pass | Pass |
| ac-reviewing-codebase | Pass | Pass | Warn |

Across the 2 sampled skills there are 5 Pass, 1 Warn, and 0 Fail cells. skills.sh sampled only 2 of the 9 listings, so the other 7 carry no published verdict.

## Limitations

- Snapshot data, verified Nov 26, 2026: 3,415 combined installs across 9 indexed listings; 1 GitHub star; MIT license; last pushed Oct 27, 2026. Counts drift over time.
- The repository has no published description and a single GitHub star; treat it as a personal toolkit rather than a maintained product.
- ac-reviewing-codebase carries a Snyk Warn verdict; read its security page before relying on the review gate.
- skills.sh sampled only 2 of the 9 listings; the other 7 carry no published security verdict.
- Six of the nine listings sit at 1 to 2 installs each; the install mass is concentrated in the three head skills.

## Related

[OpenAI Agents Python Skills - Multi-Agent Setup](/hermes/skills/catalog/openai-agents-python-skills-setup) | [Obra Superpowers - Engineering Workflow Skills](/hermes/skills/catalog/obra-superpowers-setup) | [Data Analytics Skills - 31-Skill Analyst Suite Setup](/hermes/skills/catalog/data-analytics-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use ac-python for general Python and ac-django for Django work; the former explicitly says not to use it for Django-specific patterns.
- Run ac-reviewing-codebase as a periodic quality gate, not just on demand; it covers skill quality, code health, and repo status.
- ac-adopting-ruff and ac-scaffolding-skill-repos are small but useful companion skills for a skills repo.
- Install with `--skill '*'` to pull the full roster, or pin the three head skills for a lean install.
- Only two skills carry verdicts; re-check skills.sh before trusting the unsampled seven.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
