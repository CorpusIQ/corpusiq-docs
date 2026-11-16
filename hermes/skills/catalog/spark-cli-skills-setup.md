---
title: "Spark CLI Skills - Email, Calendar and Meetings for Agents"
description: "readdle/spark-cli-skills - 11.9K combined installs across 34 indexed listings: email, calendar, contacts and meeting workflows for AI agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/spark-cli-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "email", "calendar", "spark"]
---

# Spark CLI Skills - Setup Guide

**Source:** [readdle/spark-cli-skills](https://www.skills.sh/readdle/spark-cli-skills) via skills.sh - 11.9K combined installs across 34 indexed listings; first seen Nov 16, 2026 (Nov 16 morning sweep)
**GitHub:** 157 stars, MIT license, `main` branch, last pushed 2026-11-16, `SKILL.md` files under `skills/<name>/`
**Category:** Productivity - Spark email, calendar, contacts and meeting workflows
**Quality Tier:** 🟡 Yellow - no Fails in the sample, but 11 of 12 sampled skills carry Snyk Warns and use-spark also carries a Gen Agent Trust Hub Warn.

Spark CLI Skills is Readdle's agent skill set for the Spark desktop email and calendar app. It wraps the Spark CLI behind one base command-reference skill (`use-spark`), a set of single-task recipes (inbox triage, meeting prep, unsubscribe audits) and long-running personas (executive assistant, founder, team lead) that shape tone and defaults across a session.

The skills are deliberately layered: every recipe and persona depends on `use-spark` for the command and filter syntax, so the individual workflows stay thin. Access is gated per account through Spark's three access levels (read-only, triage, send), which bound what an agent can actually do.

## Installation

Install everything, or just the base skill plus the recipes and persona you need:

```bash
# install the whole repo
npx skills add https://github.com/readdle/spark-cli-skills

# or pick individual skills
npx skills add https://github.com/readdle/spark-cli-skills/tree/main/skills/use-spark
npx skills add https://github.com/readdle/spark-cli-skills/tree/main/skills/recipe-inbox-zero
npx skills add https://github.com/readdle/spark-cli-skills/tree/main/skills/persona-exec-assistant
```

Requirements: macOS or Windows with a recent Spark Desktop build, the Spark CLI enabled (Settings - AI Agents - Spark CLI Setup), and per-account access levels configured under Spark CLI Access.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| use-spark | 532 | Command reference for the Spark CLI: mail, calendar, contacts, teams and meetings. |
| spark-recipe-morning-standup | 378 | Morning briefing: today's events, unread people and priority mail, team assignments. |
| spark-recipe-inbox-by-category | 375 | Process the inbox in priority order by Spark's smart categories. |
| spark-recipe-end-of-day | 373 | End-of-day review: loose ends, pinned items, and a preview of tomorrow. |
| spark-recipe-weekly-digest | 371 | Weekly summary of meetings, unread email by category and team status. |
| spark-recipe-meeting-prep | 369 | Gather agenda, email context and attendee details before a meeting. |
| spark-recipe-multi-account-review | 366 | Review inbox status across multiple accounts with per-account breakdown. |
| spark-recipe-inbox-zero | 359 | Process the inbox to zero using category-first triage. |
| spark-recipe-calendar-audit | 359 | Analyze meeting load, busy days, back-to-back chains and free blocks. |
| spark-persona-exec-assistant | 359 | Executive assistant persona: briefings, draft replies, scheduling, contact lookup. |
| spark-recipe-topic-timeline | 358 | Build a chronological narrative from meeting excerpts and email threads. |
| spark-recipe-stakeholder-brief | 358 | Compile a relationship dossier from all meetings and email with a person. |
| spark-recipe-newsletter-cleanup | 357 | Audit newsletter subscriptions: block, unsubscribe or enable summaries. |
| spark-recipe-shared-inbox-status | 351 | Review shared inbox health: open vs done, unassigned work, per-member breakdown. |

The remaining 20 indexed listings range from 315 to 348 installs.

## Why This Matters for Hermes Agents

The base skill is the real asset: `use-spark` concentrates the entire Spark CLI command and filter reference in one place, so recipes and personas can stay declarative instead of re-explaining syntax. Recipes map one-to-one onto single user requests, which is exactly the decomposition an agent should be doing anyway. The persona layer is a clean pattern for steering tone and defaults across a session rather than per message.

The per-account access-level model is the security story worth copying: read-only, triage, and send bound what an agent can touch, and a recipe that needs more access than the account allows fails with an explanation instead of silently escalating. That is a boundary agents should surface, not bury.

## Usage

| You say | What happens |
|---|---|
| "Walk me through this morning's inbox" | spark-recipe-morning-standup summarizes today's events, unread priority mail and team assignments. |
| "Get my inbox to zero" | spark-recipe-inbox-zero runs category-first triage, archiving or marking items done. |
| "What does my week look like?" | spark-recipe-weekly-digest summarizes meetings, email and team status. |
| "Prep me for my 2pm meeting" | spark-recipe-meeting-prep gathers agenda, email context and attendee details. |
| "Audit my meeting load" | spark-recipe-calendar-audit analyzes meeting hours, busy days and free blocks. |
| "Clean up newsletter noise" | spark-recipe-newsletter-cleanup blocks, unsubscribes or summarizes subscriptions. |
| "Act as my executive assistant" | spark-persona-exec-assistant biases the session toward briefings, drafts and scheduling. |

## Verification

Inspect the skill files before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/readdle/spark-cli-skills/main/skills/use-spark/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/readdle/spark-cli-skills/main/skills/recipe-inbox-zero/SKILL.md | head -20
```

Directories in the tree are `use-spark/`, `recipe-*/` and `persona-*/`; the skills.sh listing names add a `spark-` prefix to recipes and personas (the `name:` field in each SKILL.md). Confirm the directory path exists in the current tree before installing a specific skill.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| use-spark | Warn | Pass | Warn |
| spark-recipe-morning-standup | Pass | Pass | Warn |
| spark-recipe-inbox-by-category | Pass | Pass | Warn |
| spark-recipe-end-of-day | Pass | Pass | Warn |
| spark-recipe-weekly-digest | Pass | Pass | Warn |
| spark-recipe-meeting-prep | Pass | Pass | Warn |
| spark-recipe-multi-account-review | Pass | Pass | Warn |
| spark-recipe-inbox-zero | Pass | Pass | Warn |
| spark-recipe-calendar-audit | Pass | Pass | Pass |
| spark-persona-exec-assistant | Pass | Pass | Warn |
| spark-recipe-topic-timeline | Pass | Pass | Warn |
| spark-recipe-stakeholder-brief | Pass | Pass | Warn |

No skill carries a Fail, but Snyk Warns appear on 11 of 12 sampled skills and use-spark also carries a Gen Agent Trust Hub Warn. Treat the Spark CLI as an account-scoped data surface and keep access levels at read-only until a workflow needs more.

## Limitations

- Snapshot data, verified Nov 16, 2026: 11,880 combined installs across 34 indexed listings; 157 GitHub stars; MIT; last pushed 2026-11-16. Counts drift over time.
- Index-vs-tree naming drift: skills.sh lists recipes and personas as spark-recipe-* and spark-persona-* (from each SKILL.md `name:` field), but the repository directories are `skills/recipe-*` and `skills/persona-*`; only use-spark matches on both. Use the directory names in install URLs.
- macOS or Windows only; there is no Linux Spark CLI. Running these skills requires a signed-in Spark Desktop with the Spark CLI enabled.
- use-spark is a hard dependency of every recipe and persona; install it first or the workflows cannot run.
- Access-level enforcement is per account: a recipe that needs send or triage access fails with an upgrade prompt on accounts configured read-only.

## Related

- [Agent Email CLI Skill](/hermes/skills/catalog/agent-email-cli-setup)
- [Email Best Practices Skill](/hermes/skills/catalog/email-best-practices-skill-setup)
- [IMAP/SMTP Email - OpenClaw Email Integration](/hermes/skills/catalog/imap-smtp-email-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install use-spark first; every recipe and persona requires its command reference.
- Start with use-spark plus the one or two recipes you actually run, and at most one persona.
- Match the Spark CLI access level per account to the recipe's declared needs; read-only is the safe default.
- Keep one persona active per session to bias tone and defaults; recipes stay one-per-job.
- Remember the naming split: install URLs use recipe-* and persona-* directories, not the spark-prefixed listing names.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
