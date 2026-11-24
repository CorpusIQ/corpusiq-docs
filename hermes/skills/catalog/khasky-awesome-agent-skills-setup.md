---
title: "Khasky Agent Skills - Code Review and Debug Suite Setup"
description: "khasky/awesome-agent-skills - 3.8K combined installs: code review, debugging and security skills for AI coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/khasky-awesome-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "security", "debugging"]
---

# Khasky Agent Skills - Code Review and Debug Suite Setup

**Source:** [khasky/awesome-agent-skills](https://www.skills.sh/khasky/awesome-agent-skills) via skills.sh - 3.8K combined installs across 73 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 morning sweep)
**GitHub:** [khasky/awesome-agent-skills](https://github.com/khasky/awesome-agent-skills) - 40 stars, MIT license, main branch, last pushed Oct 20, 2026; each skill is a folder with a SKILL.md, most with evals/ and references/ support files.
**Category:** Code Review and Security Auditing
**Quality Tier:** 🟠 Orange - awesome-architecture-audit carries one Fail (Gen Agent Trust Hub); awesome-code-review, awesome-code-cleanup, awesome-bug-fix and awesome-dependency-audit carry Warn cells.

khasky/awesome-agent-skills is a 73-skill library for AI coding agents covering code review, debugging, security audits, refactoring and cleaning up AI-written code and text. Each skill is a folder with a SKILL.md in the Agent Skills format, distilled from public collections and documented practice, and it ships marketplace manifests for Claude Code, Codex, Copilot CLI, Gemini CLI, Qwen Code and several other agents.

The collection is audit-heavy and read-only by design: architecture, security, database, dependency, performance and accessibility audits each end in a SHIP / FIX / BLOCK verdict, while the code review, bug fix and test writing skills carry the day-to-day engineering. A long tail of 56 listings sits below 80 installs, most of them at a single install, so the library is effectively two collections: a popular audit and review core plus an exploratory tail.

## Installation

Install every skill globally into Claude Code, Codex and Gemini CLI:

```bash
git clone https://github.com/khasky/awesome-agent-skills.git
cd awesome-agent-skills
npx skills add ./skills -g -s "*" -a claude-code codex gemini-cli -y
```

To skip the clone, npx skills add khasky/awesome-agent-skills installs straight from GitHub. Change -a to pick agents; -a "*" installs to every detected agent.

Install as a Claude Code plugin:

```bash
/plugin marketplace add khasky/awesome-agent-skills
/plugin install awesome-agent-skills@awesome-agent-skills
```

The README also documents plugin installs for Codex, Copilot CLI, Gemini CLI, Qwen Code, Cursor, Antigravity and Kilo Code.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| awesome-code-review | 146 | reviewing a diff, patch or pull request for correctness, security and team standards |
| awesome-architecture-audit | 133 | read-only audit of a whole codebase's design with a verdict |
| awesome-test-writing | 126 | designing and writing tests that catch real regressions |
| awesome-code-cleanup | 126 | behavior-preserving cleanup of AI-like code noise |
| awesome-bug-fix | 125 | fixing a bug through a runnable reproduction and its root cause |
| awesome-security-audit | 119 | read-only security audit of source code with CWE-mapped fixes |
| awesome-code-standards | 101 | coding conventions that fill the gaps a project's own rules leave |
| awesome-performance-audit | 99 | read-only performance and reliability audit |
| awesome-regression-sweep | 98 | read-only sweep for regressions against a recorded baseline |
| awesome-api-design | 96 | designing or reviewing an HTTP API's shape before code |
| awesome-design-doc | 90 | writing a design doc or ADR with real alternatives and a recommendation |
| awesome-dependency-audit | 89 | read-only supply-chain audit of packages and agent extensions |
| awesome-logging-standards | 85 | applying structured logging with levels and PII redaction |
| awesome-error-standards | 85 | applying consistent error handling and API error envelopes |
| awesome-database-audit | 83 | read-only audit of a database layer's schema, queries and indexes |
| awesome-accessibility-audit | 83 | WCAG checks, each finding carrying its fix |
| awesome-root-cause | 81 | root-cause analysis for incidents and process problems |

The remaining 56 indexed listings range from 1 to 77 installs.

## Why This Matters for Hermes Agents

Code review and pre-release auditing are the highest-leverage places to attach an agent, and this library covers that whole surface with a consistent, verdict-driven shape. Every audit skill is read-only and ends in a SHIP / FIX / BLOCK judgement, which maps cleanly onto a CI or release gate a Hermes agent can enforce. The review, bug-fix and test-writing skills chain together, so an agent can implement, clean up and review a change in one pass without switching tools.

For a builder, the value is the shared vocabulary and dependency graph: findings are rated Critical through Informational, audits share checklists and references across skills, and the repository ships a lint script that keeps every cross-skill reference and the dependency table in sync. A second cluster of content, git-history and publishing skills serves agents that write and ship prose as well as code. Because four skills can rewrite published git history or post to live accounts, the README gates them behind explicit naming, a safety pattern worth copying.

## Usage

| You say | What happens |
|---|---|
| Review a PR before merge | Uses awesome-code-review for severity-ranked findings |
| Find why a test is flaky | Uses awesome-bug-fix to reproduce and isolate the root cause |
| Audit this repo before open-sourcing it | Uses awesome-security-audit for injection, secrets and CI/CD exposure |
| Check the database schema for anti-patterns | Uses awesome-database-audit for a read-only schema review |
| Write tests that actually catch regressions | Uses awesome-test-writing for behavior-first tests |
| Clean the AI-slop out of this code | Uses awesome-code-cleanup to remove noise while preserving behavior |
| Design an API before writing endpoints | Uses awesome-api-design for resources, pagination and idempotency |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/khasky/awesome-agent-skills/main/README.md | head -40
```

Confirm the code review skill body before installing:

```bash
curl -sL https://raw.githubusercontent.com/khasky/awesome-agent-skills/main/skills/awesome-code-review/SKILL.md | head -30
```

After install, confirm the skills landed in the global skills directory (~/.agents/skills/ for the quick-start install, or the plugin's skills directory).

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| awesome-code-review | Pass | Pass | Warn |
| awesome-architecture-audit | Fail | Pass | Pass |
| awesome-test-writing | Pass | Pass | Pass |
| awesome-code-cleanup | Pass | Pass | Warn |
| awesome-bug-fix | Pass | Pass | Warn |
| awesome-security-audit | Pass | Pass | Pass |
| awesome-code-standards | Pass | Pass | Pass |
| awesome-performance-audit | Pass | Pass | Pass |
| awesome-regression-sweep | Pass | Pass | Pass |
| awesome-api-design | Pass | Pass | Pass |
| awesome-design-doc | Pass | Pass | Pass |
| awesome-dependency-audit | Pass | Pass | Warn |
| awesome-logging-standards | Pass | Pass | Pass |
| awesome-error-standards | Pass | Pass | Pass |
| awesome-database-audit | Pass | Pass | Pass |

awesome-architecture-audit carries the single Fail (Gen Agent Trust Hub); four skills carry a Warn on Snyk.

## Limitations

- Snapshot data, verified Nov 24, 2026: 3,827 combined installs across 73 indexed listings; 40 GitHub stars; MIT license; last pushed Oct 20, 2026. Counts drift over time.
- The install distribution is a steep long tail: 56 of 73 listings sit below 80 installs, and 22 of them show a single install.
- 23 indexed listings have no counterpart in the current tree (21 bare-name skills at 1 install each, plus awesome-content-graphics and awesome-db-audit), so their behaviour is not verifiable from the repository.
- skills.sh sampled 15 of the 73 listings; the other 58 carry no verdict in this snapshot.
- The README documents that several skills adapt material from other projects (humanizer-ru, sepia, claude-seo and others), so review attribution before redistributing.

## Related

- [Code Review Skill - 20+ Language Review Guides](/hermes/skills/catalog/code-review-skill-setup)
- [Multi-Agent Review - Adversarial Code Review Setup](/hermes/skills/catalog/multi-agent-review-setup)
- [Review Loop Skill - Continuous Code Review Discipline](/hermes/skills/catalog/review-loop-skill-setup)
- [Cybersecurity Skills - 42 Audit and Pentest Skills](/hermes/skills/catalog/briiirussell-cybersecurity-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the whole set rather than single skills, because many skills read reference files that ship with other skills.
- Name the four history-rewriting and live-posting skills explicitly to run them; they never fire on a matching request alone.
- Run scripts/lint.py in a clone to keep cross-skill references and the dependency table in sync.
- Chain the skills: implement, then awesome-code-cleanup, then awesome-code-review before merging.
- Treat the audit verdicts (SHIP / FIX / BLOCK) as your release gate rather than reading raw findings.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
