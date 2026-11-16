---
title: "Basecamp Skills - 37signals Product Automation"
description: "basecamp/skills: 3.2K combined installs across 9 listings, agent skills that drive the Basecamp, HEY and Fizzy CLIs for projects, email and boards."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/basecamp-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "basecamp", "hey", "cli automation"]
---

# Basecamp Skills - Setup Guide

**Source:** [basecamp/skills](https://www.skills.sh/basecamp/skills) via skills.sh - 3.2K combined installs across 9 indexed listings; first seen Nov 14, 2026 (Nov 14 evening sweep)
**GitHub:** 87 stars, no LICENSE file in the tree, `main` branch, last pushed 2026-11-13, four `SKILL.md` files under `skills/`
**Category:** Project management and email automation through CLIs
**Quality Tier:** 🟠 Orange - one sampled verdict fails Snyk while the other passes all three auditors, and the repository ships no licence file.

37signals publishes these skills from its own CLIs. The idea is consistent across the family: rather than teach an agent an API, each skill teaches it to drive the product's command line, so the agent works through the same interface a person would and the CLI owns authentication and rate limits.

The collection covers Basecamp, HEY and Fizzy, but only two of the three are actually present. The README is candid about it: `hey` disappeared because two release pipelines shared one `.managed-skills` manifest and each product's release deleted the other's skills, and `fizzy` is not published here at all because its CLI has no skills sync yet. Both have documented workarounds.

## Installation

Install every skill in the repository:

```bash
npx skills add basecamp/skills
```

Each skill drives one product's CLI, so install and authenticate the CLI for the products you use. One is enough; the skills for the others sit idle. For HEY and Fizzy, install the skill from its own CLI (`hey skill install`, `fizzy skill install`) until the sync bug is resolved.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| basecamp | 2,438 | Full Basecamp coverage through the Basecamp CLI: projects, todos, cards, messages, files, schedule, check-ins, timeline, webhooks, templates and chat. |
| basecamp-doctor | 312 | Diagnosing Basecamp CLI, authentication and agent-plugin health. |
| hey | 251 | HEY email through the HEY CLI: reading and sending mail, contacts, boxes, labels, calendars and habits. |

The remaining 6 indexed listings range from 4 to 87 installs.

## Why This Matters for Hermes Agents

Project management is where an agent's work becomes visible to people who do not use agents. An agent that can read a Basecamp project, file a todo and reply in the right thread is useful to a team; one that produces a summary in a chat window nobody reads is not. Driving the CLI is also the safer path, since permissions and audit trails stay in the product rather than in a custom integration.

The coverage list is unusually complete for a single skill. Basecamp's CLI reaches projects, todos, cards, messages, files, schedule, check-ins, timeline, recordings, templates, webhooks, subscriptions, lineup, chat, pings, gauges, assignments, notifications, bookmarks and drafts, which means an agent can operate the product rather than summarize it.

The `basecamp-doctor` skill is the practical safeguard. When an agent suddenly cannot reach a product, the diagnosis is almost always authentication or plugin state, and having that as a skill turns a debugging session into one command.

## Usage

| You say | What happens |
|---|---|
| "What is open on the Q4 launch project?" | Reads the project through the Basecamp CLI and lists open todos and cards. |
| "Add a todo for the pricing page copy" | Creates the todo in the right project list with an assignee. |
| "Post a summary to the team message board" | Writes the message to the project's board. |
| "Why can the agent no longer see Basecamp?" | Runs the doctor skill against CLI and authentication state. |
| "Check my HEY inbox for anything from the bank" | Searches mail through the HEY CLI, once that skill is installed from its own CLI. |
| "What is on the schedule this week" | Reads the schedule entries and reports them by date. |

## Verification

Read the Basecamp skill and confirm the CLI is authenticated:

```bash
curl -fsSL https://raw.githubusercontent.com/basecamp/skills/main/skills/basecamp/SKILL.md | head -20
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/basecamp/skills/main/skills/basecamp-doctor/SKILL.md
basecamp --version
```

Skill paths are flat under `skills/<name>/SKILL.md`. The CLI itself is what carries the behaviour, so a version mismatch shows up there before it shows up in the skill.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| basecamp | Pass | Pass | Pass |
| basecamp-doctor | Pass | Pass | Fail |

`basecamp-doctor` fails Snyk in the sampled set, and the repository has no LICENSE file, so the reuse terms are unstated. These skills also drive accounts that hold real project data and email, so scope the CLI credentials to what an agent should reach.

## Limitations

- Snapshot data, verified 2026-11-14: 3,158 combined installs across 9 indexed listings; 87 GitHub stars; no LICENSE file; last pushed 2026-11-13. Counts drift over time.
- The install index lists 9 names but the tree carries 4 `SKILL.md` files: `skill-crafting`, `consult-outside-expert`, `install-md`, `unify-worktree-memory` and `ralph-lisa-loop` have no skill directory here.
- `hey` is documented as missing from `skills/` because of a sync bug between two CLI release pipelines. Install it from `hey-cli` or with `hey skill install` until that is fixed.
- `fizzy` is not published in this repository at all; its CLI has no skills sync yet.
- No licence file. Treat it as source-available until 37signals states terms.
- `basecamp-doctor` carries a Snyk Fail. Review it before an agent runs it unattended against a live account.

## Related

- [Linear CLI - Issue Tracking from the Terminal](/hermes/skills/catalog/linear-cli-setup)
- [gh-issue-sync - Local Markdown GitHub Issues Skill Setup](/hermes/skills/catalog/gh-issue-sync-setup)
- [Make Platform Skills - Make.com Automation Setup](/hermes/skills/catalog/make-platform-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only the product CLIs you actually use; each skill is idle weight otherwise.
- Run `basecamp-doctor` before debugging any "the agent cannot reach Basecamp" report.
- Prefer the product CLI over a hand-built API client: authentication and rate limits stay where 37signals maintains them.
- For HEY, install from the HEY CLI rather than this repository until the sync bug is closed.
- Ask the agent to read a project before writing to it, so new todos land in the right list.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
