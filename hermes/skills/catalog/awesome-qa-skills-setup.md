---
title: "Awesome QA Skills - Bilingual QA Testing Suite Setup"
description: "naodeng/awesome-qa-skills - 7.7K combined installs: bilingual QA and software testing skills from requirements through release."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/awesome-qa-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "qa", "testing", "software testing"]
---

# Awesome QA Skills - Bilingual QA Testing Suite Setup

**Source:** [naodeng/awesome-qa-skills](https://www.skills.sh/naodeng/awesome-qa-skills) via skills.sh - 7.7K combined installs across 96 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 morning sweep)
**GitHub:** [naodeng/awesome-qa-skills](https://github.com/naodeng/awesome-qa-skills) - 322 stars, GitHub reports the license as NOASSERTION while the README cites PolyForm Noncommercial 1.0.0, main branch, last pushed Nov 24, 2026; each skill is an independent directory under skills/en/ and skills/zh/ across testing-types, testing-workflows, and skill-engineering, with a SKILL.md plus prompts/, agents/openai.yaml, and evals/.
**Category:** QA and Software Testing
**Quality Tier:** 🟡 Yellow - requirements-analysis carries one Warn cell (Gen Agent Trust Hub); the other 14 sampled skills pass all three checks.

Awesome QA Skills is a bilingual (Chinese and English) QA skill library for coding agents, published by naodeng. It spans the full testing lifecycle: requirements analysis, test strategy, test case design and review, functional, API, UI, regression, performance, and security testing, plus release verification and AI, LLM, and agent testing. Each skill is independently installable and follows the Agent Skills convention, with a SKILL.md entry point, prompt files, OpenAI/Codex metadata, and skill-up evaluation cases.

The repository ships 176 skills per language (352 directories across zh and en), while skills.sh indexes 96 of the 176 canonical skills; the other 80 have no index entry yet. The indexed set concentrates on core QA skills such as test-case-writing, requirements-analysis, and functional-testing, alongside tool-specific entries for Playwright, Cypress, Selenium, k6, JMeter, and Postman. The primary README and governance documentation are written in Chinese, with an English counterpart in README_EN.md.

## Installation

Install a single English skill with the Agent Skills installer:

```bash
npx skills add naodeng/awesome-qa-skills --skill functional-testing
```

Install a single Chinese skill from the zh subdirectory:

```bash
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh --skill functional-testing
```

The README also ships one-click installer scripts for Codex, Cursor, Claude Code, Kiro, OpenCode, and Trae, each targeting that tool's skills directory. The canonical entry point is npx skills or a manual copy of the desired language directory.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| test-case-writing | 482 | writing high-quality test cases with normal, exception, and boundary scenarios |
| requirements-analysis | 279 | identifying test points, boundaries, dependencies, and risks before test design |
| test-case-reviewer | 233 | reviewing test cases for completeness, clarity, maintainability, and missing scenarios |
| functional-testing | 194 | designing functional test plans for business flows, UI, data, and integrations |
| test-reporting | 158 | generating test reports with summary, metrics, defect analysis, and risk assessment |
| testcase-writer-plus | 156 | producing high-quality test cases from requirements and analysis artifacts |
| api-testing | 151 | designing API test plans for REST, GraphQL, or gRPC interfaces |
| automation-testing | 147 | designing automation approaches with POM, data-driven, or BDD patterns |
| bug-reporting | 143 | writing clear, reproducible bug reports with steps, environment, and evidence |
| test-case-reviewer-plus | 133 | structured test-case review findings from requirements, strategy, and case docs |
| requirements-analysis-plus | 125 | parsing Word, HTML, JSON, Markdown, and Excel requirements into structured analysis |
| test-strategy | 122 | defining test scope, methods, resources, risks, and quality gates |
| manual-testing | 122 | planning manual or exploratory testing with charters and session records |

The remaining 83 indexed listings range from 48 to 111 installs.

## Why This Matters for Hermes Agents

Awesome QA Skills is one of the larger QA-specific skill libraries on skills.sh, which makes it a useful reference for agents that need to produce test artifacts rather than just explain testing. The skills are granular and task-shaped: an agent asked to write test cases can invoke test-case-writing, while a requirements document can be routed to requirements-analysis or requirements-analysis-plus depending on the input format. This mirrors how a human QA lead would split work across a team.

The bilingual layout matters too. Skills exist as mirrored zh and en directories with aligned canonical names, so the same QA workflow can run for English and Chinese teams without re-authoring. Tool-specific skills such as api-test-pytest, ui-test-playwright, and performance-test-k6 lower the barrier to turning a testing strategy into concrete, runnable automation.

The tradeoff is scale and freshness. The library is large, the primary documentation is Chinese-first, and the license is PolyForm Noncommercial, which restricts reuse to non-commercial purposes. Treat it as a planning and design aid rather than a drop-in commercial test harness.

## Usage

| You say | What happens |
|---|---|
| Write test cases for the login feature | Uses test-case-writing for normal, exception, and boundary scenarios |
| Review my test cases for gaps | Uses test-case-reviewer for completeness and missing scenarios |
| Design an API test plan for our REST service | Uses api-testing for the REST interface test plan |
| Plan an automation strategy | Uses automation-testing for POM, data-driven, or BDD patterns |
| Write up this defect | Uses bug-reporting for a reproducible report with evidence |
| Check what regression tests to run before release | Uses regression-test-selection for a minimal risk coverage set |
| Assess our LLM feature's behavior and safety | Uses llm-testing and prompt-injection-testing |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/naodeng/awesome-qa-skills/main/README.md | head -40
```

Confirm a core skill body is present before installing it:

```bash
curl -sL https://raw.githubusercontent.com/naodeng/awesome-qa-skills/main/skills/en/testing-types/functional-testing/SKILL.md | head -30
```

Skills install under the tool's own directory (for example ~/.codex/skills/ for Codex, ~/.claude/skills/ for Claude Code), so confirm the directory after install.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| test-case-writing | Pass | Pass | Pass |
| requirements-analysis | Warn | Pass | Pass |
| test-case-reviewer | Pass | Pass | Pass |
| functional-testing | Pass | Pass | Pass |
| test-reporting | Pass | Pass | Pass |
| testcase-writer-plus | Pass | Pass | Pass |
| api-testing | Pass | Pass | Pass |
| automation-testing | Pass | Pass | Pass |
| bug-reporting | Pass | Pass | Pass |
| test-case-reviewer-plus | Pass | Pass | Pass |
| requirements-analysis-plus | Pass | Pass | Pass |
| test-strategy | Pass | Pass | Pass |
| manual-testing | Pass | Pass | Pass |
| performance-testing | Pass | Pass | Pass |
| security-testing | Pass | Pass | Pass |

The single Warn cell sits on requirements-analysis (Gen Agent Trust Hub). The other 14 sampled skills pass Gen Agent Trust Hub, Socket, and Snyk. Only 15 of the 96 indexed listings were sampled.

## Limitations

- Snapshot data, verified Nov 24, 2026: 7,738 combined installs across 96 indexed listings; 322 GitHub stars; GitHub reports the license as NOASSERTION while the README cites PolyForm Noncommercial 1.0.0; last pushed Nov 24, 2026. Counts drift over time.
- The PolyForm Noncommercial 1.0.0 license permits use, modification, and distribution only for non-commercial purposes (personal study, research, education, and public-interest organizations), which limits commercial use.
- The repository ships 176 skills per language (352 directories) but skills.sh indexes only 96 of the 176 canonical skills, so the index undercounts the full library.
- The primary README and governance documentation are written in Chinese; the English counterpart is a separate README_EN.md.
- Only 15 of the 96 indexed listings carry a skills.sh security verdict; the rest are unverified.

## Related

- [Petr Kindlmann QA Skills - 50-Skill Test Suite](/hermes/skills/catalog/petrkindlmann-qa-skills-setup)
- [TestDino Playwright Skills - 79-Guide Testing Suite Setup](/hermes/skills/catalog/testdino-playwright-skill-setup)
- [Supabase Pentest Skills - 24-Skill Audit Suite](/hermes/skills/catalog/supabase-pentest-skills-setup)
- [Code Review Skill - 20+ Language Review Guides](/hermes/skills/catalog/code-review-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install one skill at a time with --skill; the full library is too large to add wholesale.
- Use the en directory for English prompts and the zh directory for Chinese prompts, since the two languages are mirrored.
- Prefer the 15 skills that carry a skills.sh security verdict when you need a known-good starting set.
- Check the license before any commercial or product use; PolyForm Noncommercial forbids it.
- Route "which skill first" questions through discover-testing, the library's own skill router.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
