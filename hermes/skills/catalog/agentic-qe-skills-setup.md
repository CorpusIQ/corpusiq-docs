---
title: "Agentic QE Skills - Test Automation and Quality Engineering"
description: "proffesor-for-testing/agentic-qe on skills.sh: 5.9K combined installs; QA skills for code review, API testing, regression and release checks"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agentic-qe-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "quality engineering", "test automation", "code review", "api testing"]
---

# Agentic QE Skills - Setup Guide

**Source:** [proffesor-for-testing/agentic-qe](https://www.skills.sh/proffesor-for-testing/agentic-qe) via skills.sh - 5.9K combined installs across 20 indexed listings; sampled 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 524 stars, MIT licensed, `main` branch, last pushed 2026-11-09, 307 `SKILL.md` files across mirrored client directories (86 under `assets/skills/`, 119 under `.claude/skills/`, 86 under `.kiro/skills/`, 7 under `.agents/skills/` and 9 in the Claude Code plugin) in a repository of 5,946 blobs
**Category:** Quality engineering: test strategy, API and load testing, coverage analysis, defect triage and release gates
**Quality Tier:** 🟡 Solid with caveats - MIT licensed, 20 listings sampled with one Fail verdict and several Warnings.

Agentic QE is a quality engineering platform for coding agents from proffesor-for-testing. The repository ships three surfaces that share one skill set: an npm CLI (`agentic-qe`, which also exposes an MCP server as `aqe-mcp`), a Claude Code plugin called `agentic-qe-fleet`, and the `SKILL.md` packages that skills.sh indexes. The README describes the product as a loop rather than a single command: generate tests, investigate coverage gaps, analyse flaky behaviour, coordinate release checks, then store the patterns that worked. Framework output is written for Jest, Vitest, Playwright, Cypress, pytest and JUnit, with the explicit caveat that generated tests are an input to a human decision.

The skill count needs a careful reading. The publisher page claims 200 agent skills and the tree holds 307 `SKILL.md` files, but those files are mirrored per client: 86 directories under `assets/skills/`, 119 under `.claude/skills/` (which carries extra families such as `agentdb-*` and `a11y-ally`), 86 under `.kiro/skills/`, 7 under `.agents/skills/` and 9 inside the plugin. The 20 listings rendered on the skills.sh source page are a further subset, and they are what this guide covers. The practical read is a focused QE suite of a few dozen procedures, published many times over for different hosts.

## Installation

The skills CLI route installs one skill at a time, and the command names the skill explicitly:

```bash
npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill code-review-quality
```

Swap `code-review-quality` for any name in the table below. This route takes only the skill directory, not the CLI, the MCP wiring or the learning store.

The full platform install is the npm package, which expects Node.js 22.13.0 or newer and npm 10 or newer:

```bash
npm install -g agentic-qe
cd your-project
aqe init --auto
aqe health
```

`aqe init --auto` inspects the project and writes the default Claude Code configuration, including the MCP server. Other clients take their own flag, for example `aqe init --auto --with-codex`, `--with-copilot`, `--with-cursor` or `--with-all-platforms`. On npm 12 and later, dependency install scripts are blocked by default and the SQLite store needs its script to fetch a native binary, so the README recommends naming the packages:

```bash
npm install -g agentic-qe --allow-scripts=agentic-qe,better-sqlite3,hnswlib-node
```

The Claude Code plugin is the scoped alternative. It registers its own MCP server pinned to the matching package version and adds slash commands such as `/aqe-generate` and `/aqe-analyze`, without the broader project configuration that `aqe init` performs:

```text
/plugin install agentic-qe-fleet --marketplace proffesor-for-testing/agentic-qe
```

## What It Provides

The threshold for this guide is zero installs, so all 20 indexed listings appear in the table:

| Skill | Installs | Use For |
|---|---|---|
| code-review-quality | 1,552 | Context-driven code review focused on quality, testability and maintainability, for reviewing a change or setting review practice |
| compatibility-testing | 654 | Cross-browser, cross-platform and cross-device checks for responsive design, browser support and consistent behaviour |
| api-testing-patterns | 609 | Contract, REST, GraphQL and integration testing patterns for API suites and API test strategy |
| regression-testing | 334 | Test selection, impact analysis and regression suite planning so a fix does not break existing behaviour |
| test-automation-strategy | 256 | Automation pyramid, framework patterns and CI/CD integration for building or repairing an automation suite |
| github-code-review | 217 | GitHub code review with swarm-style agent coordination; the one sampled skill carrying a Fail verdict |
| technical-writing | 205 | Blog posts, documentation, tutorials and technical articles written from real experience |
| test-design-techniques | 202 | Boundary value analysis, equivalence partitioning, decision tables, state transition and combinatorial test design |
| brutal-honesty-review | 181 | Blunt technical criticism of code, tests and certification claims, with no sugar-coating |
| exploratory-testing-advanced | 174 | Session-based test management, RST heuristics and test tours for planned exploration |
| mobile-testing | 172 | iOS and Android testing across gestures, sensors, permissions, device fragmentation and performance |
| n8n-security-testing | 172 | Credential exposure, OAuth flow validation, API key handling and data sanitisation checks for n8n workflows |
| n8n-workflow-testing-fundamentals | 172 | n8n execution lifecycle, node connections, data flow and error handling tests |
| bug-reporting-excellence | 160 | Bug reports that get fixed: reproduction steps, evidence and reporting standards |
| visual-testing-advanced | 157 | Pixel comparison, diff analysis and cross-browser visual regression checks |
| pr-review | 152 | Pull request review for quality, scope and trust tier compliance, with user-facing feedback |
| agentic-quality-engineering | 149 | Orchestrating QE agents, PACTS principles and AQE v3 fleet configuration |
| security-testing | 147 | OWASP Top 10 scanning for XSS, SQL injection, CSRF and auth flaws, including SAST/DAST and authorisation checks |
| pentest-validation | 144 | Validating SAST/DAST findings, proving exploitability and cutting false positives through a four-phase pipeline |
| database-testing | 140 | Schema validation, data integrity, migrations, transaction isolation and query performance |

No indexed listings fall below the threshold; all 20 appear above.

The shape of the set is worth noting before installing. Testing procedures dominate: design techniques, regressions, compatibility, mobile, visual and database testing, plus two n8n-specific workflow skills. Around them sit review skills (code review, PR review, a deliberately harsh criticism skill) and two security skills that assume scan output already exists. Only three listings clear 500 installs, and the drop from 654 to 334 is steep, so the centre of gravity is a long tail of narrow procedures rather than a small set of flagship skills.

## Why This Matters for Hermes Agents

Quality work is where an agent is most tempted to overclaim. A model asked to "add tests" will produce plausible assertions, declare coverage improved and stop, and none of that survives a real CI run. The skills here are useful because they encode procedure instead: test design techniques that force boundary and equivalence cases, regression selection that starts from impact analysis, exploratory sessions that are time-boxed and chartered. Those are checklists an agent can follow and a reviewer can audit.

The security pair is the second reason. `security-testing` gives the agent an OWASP-shaped scan plan, and `pentest-validation` then asks whether a reported finding is actually exploitable. That second step is the one agents usually skip, and it is the difference between a vulnerability report and a false positive that wastes an afternoon.

The review skills matter for the same reason at a different layer. `code-review-quality` and `pr-review` give the agent review criteria that are about scope and testability rather than style opinions, which is the kind of review that catches a behaviour change before merge rather than after.

The caveat is that the suite is distributed across mirrored directories and three install surfaces, so an agent can end up with two copies of the same skill or with the CLI and no skills at all. Pick one route, check what landed, and treat generated tests as drafts that must be run in your environment.

## Usage

| You say | What happens |
|---|---|
| "Review this pull request for quality and scope" | `pr-review` walks the diff against quality, scope correctness and trust tier criteria, and returns feedback written for the author rather than for a reviewer |
| "Generate tests for src/services/UserService.ts" | The AQE workflow produces unit, integration or property-based tests with framework-appropriate output, and states which edge cases each test covers |
| "Our coverage is high but behaviour is still missing" | `agentic-quality-engineering` and the coverage workflow prioritise uncovered branches by risk instead of chasing a percentage |
| "Design test cases for this discount rule" | `test-design-techniques` applies boundary values, equivalence partitions, decision tables and state transitions to produce a systematic case list |
| "This suite is flaky, find the pattern" | The AQE flake workflow looks at failure patterns and reproduction, then proposes stabilisation, keeping the before and after results as evidence |
| "Is this scanner finding real?" | `pentest-validation` runs the recon, analysis, validation and report phases to prove or disprove exploitability |
| "Write the release quality summary" | The release workflow coordinates coverage, security, contract and resilience checks, then reports unresolved risks alongside tool output |

## Verification

The raw skill file sits under `assets/skills/` in the repository, and this URL returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/proffesor-for-testing/agentic-qe/main/assets/skills/code-review-quality/SKILL.md | head -6
```

The frontmatter should declare `name: code-review-quality` and a description beginning "Conduct context-driven code reviews", followed by the body heading and its review sections. Note that `github-code-review` lives under `.claude/skills/` instead, so its raw path is `https://raw.githubusercontent.com/proffesor-for-testing/agentic-qe/main/.claude/skills/github-code-review/SKILL.md`.

After an install, confirm the skill landed as a directory containing `SKILL.md` rather than as loose files. The skills CLI prints its target path; the common default is the agent's skills directory:

```bash
test -f ~/.claude/skills/code-review-quality/SKILL.md && echo ok
```

If your agent reads a Hermes profile directory instead, check the same relative path under it, for example `~/.hermes/profiles/corpusiq/skills/code-review-quality/SKILL.md`.

For the npm route, the CLI has its own health check, which also reports whether the native HNSW backend loaded:

```bash
aqe health
```

Look for `HNSW backend: native` on a machine where `hnswlib-node` compiled, and `HNSW backend: js` where it fell back. The JavaScript fallback is correct but degrades to a linear scan, which the README says is unsuitable for large indexes.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| code-review-quality | Pass | Pass | Pass |
| compatibility-testing | Pass | Pass | Warn |
| api-testing-patterns | Pass | Pass | Pass |
| regression-testing | Pass | Pass | Pass |
| test-automation-strategy | Pass | Pass | Pass |
| github-code-review | Fail | Warn | Warn |
| technical-writing | Pass | Pass | Pass |
| test-design-techniques | Pass | Pass | Pass |
| brutal-honesty-review | Pass | Pass | Pass |
| exploratory-testing-advanced | Pass | Pass | Pass |
| mobile-testing | Pass | Pass | Pass |
| n8n-security-testing | Pass | Pass | Warn |
| n8n-workflow-testing-fundamentals | Pass | Pass | Pass |
| bug-reporting-excellence | Pass | Pass | Pass |
| visual-testing-advanced | Pass | Pass | Pass |
| pr-review | Pass | Pass | Warn |
| agentic-quality-engineering | Pass | Pass | Pass |
| security-testing | Pass | Pass | Pass |
| pentest-validation | Pass | Warn | Pass |
| database-testing | Pass | Pass | Pass |

Every listing except `github-code-review` clears Gen Agent Trust Hub, and the only non-Pass cells elsewhere are four Warnings: Snyk on `compatibility-testing`, `n8n-security-testing` and `pr-review`, and Socket on `pentest-validation`. The single Fail is `github-code-review`, a skill whose whole description is one line about swarm coordination, so it is cheap to inspect by hand before installing.

Two exposures sit outside the scanners' reach. The npm route installs a global package with native dependencies and runs `aqe init`, which writes configuration and MCP entries into your project; review that diff as you would any installer. The skills themselves are markdown procedures, but they instruct an agent to generate and sometimes execute tests, so the blast radius is your test suite and the credentials it touches. Run test generation on a branch, and keep any project secrets out of the environment the agent inherits.

## Limitations

- Snapshot data, verified 2026-11-09: 5,949 combined installs across 20 indexed listings; 524 GitHub stars; MIT license; last pushed 2026-11-09. Counts drift over time.
- The skills.sh source page renders at most 20 listings, while the repository indexes far more skills. The tree holds 307 `SKILL.md` files, 86 directories under `assets/skills/` and 119 under `.claude/skills/`, against a publisher claim of 200 agent skills. The install counts above cover only the rendered 20, so the combined figure is a floor rather than a total.
- The category line mentions load testing, and no sampled listing is a load or performance testing skill. The closest entries are API testing patterns and database query performance inside `database-testing`.
- The install surfaces are not equivalent. `npx skills add --skill` takes one skill and nothing else, the npm CLI adds MCP and a persistent learning store, and the plugin adds slash commands with a pinned MCP server. Mixing them can leave duplicate skill directories.
- One sampled skill, `github-code-review`, has a Fail verdict from Gen Agent Trust Hub and Warnings from Socket and Snyk. Read it before use and prefer `code-review-quality` or `pr-review` for review work.
- The default branch is `main` and the last push is the same day as this snapshot, so skill bodies can change between the data above and your install. Re-read the raw file after updating.

## Related

- [Cypress AI Toolkit - E2E Testing Skills](/hermes/skills/catalog/cypress-ai-toolkit-setup)
- [Dogfood - Systematic QA Testing Setup](/hermes/skills/catalog/dogfood-setup)
- [Alan Skills - Plan, Test and Review PRs](/hermes/skills/catalog/alan-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `code-review-quality` and `test-design-techniques`, the two skills that change how an agent reasons rather than what it types. The review skill sets the criteria, and the design skill forces cases a model would otherwise skip.
- Give the agent a real coverage report before asking it to prioritise gaps. The workflow is built to rank uncovered branches by risk, and without a report it will estimate, which is the failure mode these skills exist to avoid.
- Use `pentest-validation` on every scanner finding you intend to act on. Proving exploitability is the only step that separates a real vulnerability from a noisy rule.
- Prefer the plugin if you only want slash commands in Claude Code, and the npm CLI if you want the learning store. Installing both is how duplicate skill directories happen.
- Check `aqe health` after the first install. A `js` HNSW backend on a large repository is a performance cliff, and the fix is a compiler toolchain rather than a configuration change.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
