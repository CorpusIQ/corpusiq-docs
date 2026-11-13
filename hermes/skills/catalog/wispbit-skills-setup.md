---
title: "Wispbit Skills - Code Review Standards Setup"
description: "wispbit-ai/skills: 3.6K combined installs across 5 listings, opinionated code review standards for Python, Postgres, Rust, GraphQL and SQLAlchemy"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wispbit-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "python", "postgresql", "graphql"]
---

# Wispbit Skills - Setup Guide

**Source:** [wispbit-ai/skills](https://www.skills.sh/wispbit-ai/skills) via skills.sh - 3.6K combined installs across 5 indexed listings; first seen Nov 11, 2026
**GitHub:** 9 stars, no licence file, `main` branch, last pushed 2026-02-11, 5 `SKILL.md` files under `skills/`, 69 files in total
**Category:** Language and database code review standards
**Quality Tier:** 🟡 Yellow - five focused review standards with a clean tree, a real point of view and a documented rule format, held back by a missing licence file, a stale push and no install step in the README.

Five skills, all of them review standards rather than generators. Wispbit's README is short and honest about what this is: a public mirror of the Agent Skills they use internally, refreshed weekly from their code quality engine, published for tech leads who care about long-term maintainability.

The claim worth testing is the format. Each rule is supposed to carry a "why", a "when", a "when not", and correct and incorrect code patterns, with the rules ordered by impact so a review hits the expensive problems first. That is a materially different design from the usual "here are 40 best practices" file, because it gives the agent a reason to reject a pattern and an escape hatch for the case where the pattern is right.

The five domains are narrow on purpose: SQLAlchemy with Alembic, Python, PostgreSQL, Rust and GraphQL. There is no TypeScript, no Go and no frontend coverage, so this is a pack for backend teams working in that exact stack rather than a general review layer.

## Installation

The repository README documents no install step. It describes the skills, the rule format and the weekly refresh, and stops there.

The skills CLI command published on the pack's own skills.sh source page is:

```bash
npx skills add wispbit-ai/skills
```

Treat that as the install path rather than a repo instruction: it is what the skills.sh listing carries, and it installs all five skills from the repository root. If the command fails on a fresh checkout, clone the repository and copy the `skills/` subdirectories into your agent's skills directory instead, which is the same layout the repository ships.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| sqlalchemy-alembic-expert-best-practices-code-review | 2,113 | SQLAlchemy ORM and Alembic migration rules for safe, reversible, performant schema changes. |
| python-expert-best-practices-code-review | 685 | Python review rules for production-grade code: typing, error handling, structure and testability. |
| postgresql-expert-best-practices-code-review | 391 | PostgreSQL design, migration and query performance rules, including index and lock behaviour. |
| rust-expert-best-practices-code-review | 257 | Idiomatic Rust: ownership, error handling, safety and performance patterns. |
| graphql-expert-best-practices | 144 | GraphQL schema and resolver rules aimed at scalable, query-cost-aware APIs. |

All 5 indexed listings clear the 100-install threshold and appear in the table above.

The distribution is steep. Two of the five are database-specific, a third covers the GraphQL layer above them, and the SQLAlchemy skill alone accounts for 2,113 of the 3,590 installs, which suggests the pack is being pulled in by teams with a migration problem rather than by reviewers shopping for a general standard.

## Why This Matters for Hermes Agents

Code review is the task where an agent most often produces confident noise. It can list generic advice about naming and complexity without reading the diff, and the output looks like a review until someone tries to act on it. A rule file with a "why", a "when not" and a correct and incorrect pair is the cheapest fix for that, because it forces the finding to name a rule and a pattern.

The priority ordering matters as much as the rules. A review that leads with the migration that will lock a table for ten minutes is useful even if it says nothing else; a review that leads with line length is not. Ordering by impact is the part most agent review prompts skip.

The SQLAlchemy and Alembic coverage is the specific gap this fills for Python backends. Migration safety is a class of bug that is invisible in review unless the reviewer knows what an unsafe `ALTER TABLE` looks like on a large table, and it is exactly the kind of thing an agent with a rule file can catch consistently.

All five skills are text with no scripts, so installation is a copy and inspection is cheap. The trade is that they judge code; they do not run it, and they cannot see the query plan.

## Usage

| You say | What happens |
|---|---|
| "Review this Alembic migration before I merge it" | Runs the SQLAlchemy and Alembic skill and flags unsafe DDL, missing downgrades and lock risk. |
| "Is this index going to help or just slow writes?" | Runs `postgresql-expert-best-practices-code-review` and reasons about the query it serves. |
| "Review this Python module the way a senior would" | Runs `python-expert-best-practices-code-review` and returns prioritised findings with the rule named. |
| "Check this Rust error handling for idiomatic patterns" | Runs `rust-expert-best-practices-code-review` and points at the ownership or error-type issue. |
| "Will this resolver scale to a thousand concurrent queries?" | Runs `graphql-expert-best-practices` and reviews the schema and resolver for cost and N+1 risk. |
| "Write the downgrade path for this table rename" | Runs the SQLAlchemy and Alembic skill and returns a reversible migration with the downgrade spelled out. |

## Verification

Two skill files on `main`, both returning 200:

```bash
curl -fsSL https://raw.githubusercontent.com/wispbit-ai/skills/main/skills/python-expert-best-practices-code-review/SKILL.md | head -8
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/wispbit-ai/skills/main/skills/sqlalchemy-alembic-expert-best-practices-code-review/SKILL.md
```

After installation, confirm 5 folders with one `SKILL.md` each. Because the repository documents no install command, verify the count rather than trusting the command: a partial install that silently picked up three of five skills will look fine until a review misses the migration entirely.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sqlalchemy-alembic-expert-best-practices-code-review | Pass | Pass | Pass |
| python-expert-best-practices-code-review | Pass | Pass | Pass |
| postgresql-expert-best-practices-code-review | Pass | Pass | Pass |
| rust-expert-best-practices-code-review | Pass | Pass | Pass |
| graphql-expert-best-practices | - | - | - |

The GraphQL listing has no verdict row yet, so four of five are sampled. All five are instruction files with no executables and no dependencies, and nothing in the pack touches a network or a credential. The absence of a licence file is the bigger unknown here, covered under Limitations.

## Limitations

- Snapshot data, verified 2026-11-13: 3,590 combined installs across 5 indexed listings; 9 GitHub stars; no licence file; last pushed 2026-02-11. Counts drift over time.
- No licence file in the repository, and nothing in the README grants terms. Read the skills, but treat redistribution and commercial reuse as unresolved until you have permission.
- The README documents no install path at all. The `npx skills add` command above comes from the skills.sh listing, not from the repository, so it is the one step here you cannot verify from the source.
- The README says the skills are refreshed weekly from Wispbit's code quality engine, but the last push to the public mirror is February 2026, which is well behind a weekly cadence.
- These are review standards, not code generators. They will tell you what is wrong with a migration; they will not write the replacement or run it against a database.
- Five skills is the whole scope: SQLAlchemy with Alembic, Python, PostgreSQL, Rust and GraphQL. A team that works in none of those stacks gets nothing from this pack.

## Related

- [Vinta Django AI Plugins - Django and Celery Setup](/hermes/skills/catalog/vintasoftware-django-ai-plugins-setup)
- [Astral Plugins - Python uv, ruff and ty Setup](/hermes/skills/catalog/astral-sh-claude-code-plugins-setup)
- [Ghost Security Skills - AppSec Agent Plugin Setup](/hermes/skills/catalog/ghostsecurity-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the review on the diff, not the file. The rules are about choices, and a choice only shows up against what changed.
- Paste the wrong pattern into the prompt alongside the right one. The correct and incorrect pairs are the part of the format that survives contact with a real review.
- Ask for findings in impact order explicitly. The rules are ordered that way, and an agent asked for "all issues" will flatten them back into a list.
- Use the Alembic skill on every migration, including small ones. Reversibility is cheap to check and expensive to discover in production.
- If you only keep one skill, keep the SQLAlchemy and Alembic one. It carries most of the pack's installs, and schema changes are where a review omission is hardest to undo.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
