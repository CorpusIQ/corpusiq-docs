---
title: "BMad Test Architecture - Enterprise QA Skills Setup"
description: "bmad-code-org/bmad-method-test-architecture-enterprise - 15.1K combined installs: TEA, a BMad enhancement for test planning, automation and releases."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/bmad-test-architecture-enterprise-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "test architecture", "qa", "test automation"]
---

# BMad Test Architecture - Setup Guide

**Source:** [bmad-code-org/bmad-method-test-architecture-enterprise](https://www.skills.sh/bmad-code-org/bmad-method-test-architecture-enterprise) via skills.sh - 15.1K combined installs across 22 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 morning sweep)
**GitHub:** [bmad-code-org/bmad-method-test-architecture-enterprise](https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise) - 121 stars, NOASSERTION license field, last pushed Nov 25, 2026, main branch; ten skill directories under skills/<name>/SKILL.md, plus a Node CLI, docs, and test and evaluation layers.
**Category:** Test Architecture / QA (BMad Method)
**Quality Tier:** 🟠 Orange - bmad-tea-test-design carries a Snyk Fail and most sampled listings carry at least one Warn; license field NOASSERTION.

TEA (Test Engineering Architect) is the BMad Method's enterprise test-architecture module. Its agent, Murat, drives eight skills and a shared testing knowledge base to turn requirements and risks into tests and evidence, then makes release decisions. The suite covers test planning, framework and CI setup, acceptance tests, automation expansion, test quality review, scored behavioral evaluation, NFR evidence audit, and traceability to a PASS, CONCERNS or FAIL gate.

skills.sh indexes 22 listings at 15.1K combined installs, but the current tree ships 10 skill directories. Twelve indexed listings have no directory in the current tree: ten carry the pre-3.0 slash-command names (bmad-testarch-test-design, bmad-testarch-trace, bmad-testarch-test-review, bmad-testarch-automate, bmad-testarch-nfr, bmad-testarch-framework, bmad-teach-me-testing, bmad-testarch-ci, bmad-testarch-atdd and bmad-testarch-evaluate) plus the refund-check and stub-skill listings. The README documents the 3.0 rename from bmad-testarch-* to bmad-tea-*, so the two old names that still clear the install mark map to their renamed successors.

## Installation

Install the skills from GitHub:

```bash
npx skills add bmad-code-org/bmad-method-test-architecture-enterprise
```

TEA 4.x requires BMad v7 core. Setup needs uv plus the bmad and bmod-core-tools skills from BMad Method's main branch:

```bash
npx skills add bmad-code-org/BMAD-METHOD --skill bmad bmod-core-tools
```

Then type bmad setup tea in your assistant chat; setup asks about your test stack, integrations, and output folder, and writes the answers to _bmad/config.toml. Run it again to change those answers. To pin a tagged release instead of main, replace <version> with the release number:

```bash
npx skills add https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise/tree/v<version>/skills
```

TEA also publishes an npm package for CI and terminal use, requiring Node.js 22.20.0 or later:

```bash
npm install --save-dev bmad-method-test-architecture-enterprise
```

## What It Provides

The 12 most-installed listings appear below with their skills.sh install counts. bmad-testarch-test-design and bmad-testarch-trace are pre-3.0 names the README maps to bmad-tea-test-design and bmad-tea-trace; neither has a directory in the current tree.

| Skill | Installs | Use For |
|---|---|---|
| bmad-tea | 1,484 | Master Test Architect and Quality Advisor (Murat); invoke for test architect work |
| bmod-tea | 1,452 | required bmod metadata; never invoke this skill |
| bmad-tea-test-design | 1,304 | system-level or epic-level test plans and test strategy |
| bmad-tea-automate | 1,290 | generate tests in red or expand mode and run-and-heal new tests |
| bmad-tea-trace | 1,280 | traceability matrix and quality gate decision |
| bmad-tea-test-review | 1,271 | review test quality against a fixed criteria registry |
| bmad-tea-evaluate | 1,267 | scored behavioral evaluations and repair gaps |
| bmad-tea-teach-me-testing | 1,264 | teach testing progressively through structured sessions |
| bmad-tea-framework | 1,263 | initialize test framework and CI/CD setup for browser, backend or mobile |
| bmad-tea-nfr | 1,261 | audit NFR evidence: performance, security, reliability, maintainability |
| bmad-testarch-test-design | 203 | test plans and strategy (renamed to bmad-tea-test-design in 3.0) |
| bmad-testarch-trace | 201 | traceability matrix and gate (renamed to bmad-tea-trace in 3.0) |

The remaining 10 indexed listings range from 9 to 199 installs.

## Why This Matters for Hermes Agents

For a builder shipping agent-driven QA, TEA packages the whole test lifecycle as workflow skills an agent can step through one step file at a time. bmad-tea-test-design plans coverage by risk and priority from P0 to P3; bmad-tea-framework scaffolds the framework and CI; bmad-tea-automate generates acceptance tests in red mode before implementation and expand mode after; bmad-tea-test-review scores test quality against a fixed criteria registry; and bmad-tea-trace maps requirements to evidence and returns a PASS, CONCERNS or FAIL release gate. bmad-tea-evaluate adds scored behavioral checks with regression baselines, the layer most agent teams skip. Because each skill loads its knowledge fragments from a shared knowledge base (skills/bmod-tea/knowledge/tea-index.csv), the guidance stays consistent across the eight workflows. The CLI mirrors the skills for CI, so the same review and trace gates run on every pull request. The main cost is weight: this is a full BMad module, not a drop-in snippet, and it expects BMad v7 core plus uv.

## Usage

| You say | What happens |
|---|---|
| Design a test plan for this feature | Runs /bmad-tea-test-design to plan risks and coverage |
| Set up a test framework and CI | Runs /bmad-tea-framework to scaffold both |
| Expand test coverage on this code | Runs /bmad-tea-automate in expand mode |
| Review the quality of these tests | Runs /bmad-tea-test-review against the criteria registry |
| Map requirements to tests | Runs /bmad-tea-trace for the coverage gate |
| Teach me testing | Runs /bmad-tea-teach-me-testing sessions |
| Prove this agent behaves correctly | Runs /bmad-tea-evaluate with scored checks |

In Codex, replace the leading / in each command with $.

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/bmad-code-org/bmad-method-test-architecture-enterprise/main/README.md | head -60
curl -sL https://raw.githubusercontent.com/bmad-code-org/bmad-method-test-architecture-enterprise/main/skills/bmad-tea/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it; the README's Start with one skill table lists the eight workflow commands and their menu codes.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| bmad-tea | Pass | Pass | Warn |
| bmod-tea | Pass | Warn | Warn |
| bmad-tea-test-design | Pass | Pass | Fail |
| bmad-tea-automate | Pass | Pass | Warn |
| bmad-tea-trace | Pass | Pass | Warn |
| bmad-tea-test-review | Pass | Pass | Warn |
| bmad-tea-evaluate | Pass | Pass | Warn |
| bmad-tea-teach-me-testing | Pass | Pass | Warn |
| bmad-tea-framework | Pass | Pass | Warn |
| bmad-tea-nfr | Pass | Pass | Warn |
| bmad-testarch-test-design | Warn | Warn | Pass |
| bmad-testarch-trace | Pass | Warn | Pass |
| bmad-testarch-test-review | Pass | Warn | Pass |
| bmad-testarch-automate | Warn | Pass | Warn |
| bmad-testarch-nfr | Pass | Warn | Pass |

15 of 22 indexed listings were sampled. bmad-tea-test-design carries a Snyk Fail; bmod-tea carries Socket and Snyk Warns; and most other listings carry at least one Warn. Treat the suite as community code pending your own review.

## Limitations

- Snapshot data, verified Nov 25, 2026: 15,065 combined installs across 22 indexed listings; 121 GitHub stars; NOASSERTION license; last pushed Nov 25, 2026. Counts drift over time.
- GitHub reports the license field as NOASSERTION while the README's License section links an MIT license file; treat the license as ambiguous and check the LICENSE file before redistributing.
- The install index outruns the tree: 12 indexed listings have no directory in the current tree, including the ten pre-3.0 slash-command names and the refund-check and stub-skill listings.
- TEA 4.x requires BMad v7 core and uv; the workflows do not run against a 6.12.x core.
- The repository is large, thousands of files across skills, CLI, docs and test fixtures, so a full review is a real cost.

## Related

[BMad Method Skills - Agile AI Development Suite Setup](/hermes/skills/catalog/bmad-method-setup) | [BMAD Labs Skills - Architecture and Delivery Toolkit](/hermes/skills/catalog/bmad-labs-skills-setup) | [BMAD Planning and Orchestrator - Claude Code Plugin](/hermes/skills/catalog/aj-geddes-claude-code-bmad-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with /bmad-tea-test-design on a new feature, then follow with /bmad-tea-automate and /bmad-tea-trace before any release.
- Run the review, NFR and trace gates in CI with the npm CLI so every PR gets the same verdict the agent gets locally.
- Use the agent's GATE menu code to route through test review, NFR evidence audit and trace in one pass.
- Keep red mode for before implementation and expand mode for existing code; the direct automate command defaults to expand.
- Ask for framework only, CI only, or both; TEA infers scope from your prompt and asks once when it is unclear.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
