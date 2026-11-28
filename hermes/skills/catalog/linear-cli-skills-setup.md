---
title: "Linear CLI Skills - Linear.app Agent Skills Suite"
description: "nesszer/linear-cli: 5.1K combined installs. A Rust CLI for Linear.app whose 38 skills drive issue, project and search workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/linear-cli-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-28"
tags: ["hermes skill", "agent skill", "skill setup", "linear", "cli", "issue tracking"]
---

# Linear CLI Skills - Setup Guide

**Source:** [nesszer/linear-cli](https://www.skills.sh/nesszer/linear-cli) via skills.sh - 5.1K combined installs across 38 indexed listings; first seen Nov 28 2026 morning

**GitHub:** [nesszer/linear-cli](https://github.com/nesszer/linear-cli) - 138 stars, MIT license, branch master, last pushed 2026-09-13; skills live under `skills/<name>/SKILL.md`, one directory per command group.

**Category:** Linear.app CLI and agent skills - issue tracking, project management, sprint planning, search and git workflows

**Quality Tier:** 🟡 Yellow - the Gen Agent Trust Hub and Socket pass all 20 sampled skills; Snyk warns on linear-search, linear-uploads and linear-triage, with no Fail cells.

nesszer/linear-cli is a fast, comprehensive Rust CLI for Linear.app that manages issues, projects, cycles, sprints and documents from the terminal. The same repository ships 38 Agent Skills for AI coding assistants (Claude Code, Cursor, Codex and others), indexed on skills.sh at 5.1K combined installs across 38 listings.

The skills map one-to-one onto the CLI's command groups, so a single repository drives both interactive terminal use and agent workflows. Install counts are small and tightly packed, from 101 to 188 per skill, and every indexed listing has a matching `skills/<name>/SKILL.md` directory in the tree.

## Installation

The CLI installs through Cargo; the skills install separately through the skills CLI.

```bash
# Pre-built binary (no compilation)
cargo binstall linear-cli

# From crates.io (compiles from source)
cargo install linear-cli

# With OS keyring support (Keychain, Credential Manager, Secret Service)
cargo install linear-cli --features secure-storage

# From source
git clone https://github.com/nesszer/linear-cli.git
cd linear-cli && cargo build --release
```

Authenticate, then add the skills:

```bash
# API key (get one at https://linear.app/settings/api)
printf '%s\n' "$LINEAR_API_KEY" | linear-cli config set-key

# Or OAuth 2.0 (browser based, auto-refreshing)
linear-cli auth oauth

# Install all 38 skills
npx skills add nesszer/linear-cli

# Install one skill
npx skills add nesszer/linear-cli --skill linear-workflow
```

The CLI updates itself with `linear-cli update` (or `linear-cli update --check` to preview). Pre-built binaries for Linux, macOS and Windows are on GitHub Releases, and the README documents shell completions, configuration, multiple workspaces and diagnostics (`linear-cli doctor`).

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| linear-create | 188 | Create bugs, tasks and feature requests. |
| linear-list | 183 | List and get issues, check status, fetch details. |
| linear-search | 176 | Find issues, look up bugs, search the backlog. |
| linear-update | 170 | Change status, priority, assignee or labels. |
| linear-workflow | 148 | Start and stop work, create branches, get current issue context. |
| linear-projects | 147 | Full project CRUD with labels, members and archive. |
| linear-labels | 144 | Create, list and delete labels. |
| linear-relations | 143 | Blocking, parent/child and duplicate relations. |
| linear-git | 143 | Branches, checkout and PRs with Git or Jujutsu. |
| linear-uploads | 142 | Fetch screenshots, images and file attachments. |
| linear-documents | 141 | Create and view documentation. |
| linear-history | 139 | Activity logs and audit trails. |
| linear-bulk | 137 | Update multiple issues at once. |
| linear-triage | 135 | Unassigned issues needing attention. |
| linear-pr | 135 | Create GitHub PRs linked to Linear issues. |
| linear-roadmaps | 134 | View roadmap planning. |
| linear-cycles | 134 | List, create, update and complete sprint cycles. |
| linear-notifications | 131 | View, read and archive notifications. |
| linear-initiatives | 131 | High-level tracking across projects. |
| linear-watch | 130 | Monitor issues, projects or teams for changes. |
| linear-teams | 130 | List, create and manage teams and members. |
| linear-templates | 129 | Local and Linear workspace issue templates. |
| linear-export | 127 | Export issues to CSV, JSON or Markdown. |
| linear-config | 127 | View and set config, switch workspace profiles. |
| linear-comments | 127 | List, add and edit issue comments. |
| linear-project-updates | 123 | Project health updates (onTrack, atRisk, offTrack). |
| linear-favorites | 123 | Track favorite issues. |
| linear-milestones | 122 | Project milestones. |
| linear-api | 122 | Raw GraphQL query and mutate for anything not covered by built-in commands. |
| linear-done | 121 | Mark the current branch issue as Done. |
| linear-attachments | 121 | List, link and manage issue attachments. |
| linear-metrics | 120 | Team velocity and stats. |
| linear-statuses | 119 | List and rename workflow states. |
| linear-time | 116 | List and edit time entries. |
| linear-views | 112 | Create and apply saved custom views. |
| linear-sprint | 109 | Sprint status, burndown, velocity and carry-over. |
| linear-import | 107 | Import issues from CSV or JSON. |
| linear-webhooks | 101 | Webhook CRUD and a local HMAC-signed listener. |

All 38 indexed listings appear above. Install counts are tightly packed from linear-webhooks at 101 up to linear-create at 188, with no single skill dominating the index.

## Why This Matters for Hermes Agents

Each skill maps one Linear command group to a focused capability, so an agent can pull only what it needs (linear-create for new issues, linear-git for branches, linear-search for lookups) instead of loading a monolithic connector. The README states the skills are 10-50x more token-efficient than MCP tools, which matters when context budgets are tight.

Machine-readable output is built into the underlying CLI (`--output json`, `--compact`, `--fields`, `--id-only`, `--fail-on-empty`), so the skills compose cleanly with scripts and agent pipelines rather than relying on parsed human-readable text.

The git and workflow skills encode a repeatable loop (start issue, create branch, done, open PR) that mirrors how a coding agent actually works day to day, so the skill descriptions double as a workflow template. Finally, the security posture is a useful calibration: a local CLI that handles credentials still surfaces three Snyk Warns across the sampled skills, a reminder to scan before production adoption.

## Usage

| You say | What happens |
|---|---|
| "Create a bug for the login crash" | Uses linear-create to open a new issue. |
| "Find issues matching auth bug" | Uses linear-search to search issues and projects. |
| "Start work on LIN-123 and create a branch" | Uses linear-workflow to start the issue and check out a branch. |
| "Update LIN-123 to Done and add the urgent label" | Uses linear-update to set the status and labels. |
| "Open a PR for LIN-123" | Uses linear-pr to create a GitHub pull request linked to the issue. |
| "Summarize my team's sprint progress" | Uses linear-sprint for status, burndown and velocity. |
| "Snooze the unassigned triage items" | Uses linear-triage to claim or snooze unassigned issues. |

## Verification

The skills live under `skills/<name>/SKILL.md` on branch master. Fetch one before installing to review its frontmatter and instructions:

```bash
curl -sL https://raw.githubusercontent.com/nesszer/linear-cli/master/skills/linear-workflow/SKILL.md
```

After a clone, confirm the skill directories and the CLI itself:

```bash
git clone --depth 1 https://github.com/nesszer/linear-cli.git /tmp/linear-cli
ls /tmp/linear-cli/skills/
head -3 /tmp/linear-cli/skills/linear-workflow/SKILL.md
linear-cli doctor
```

The skills listing should show 38 skill directories (linear-api through linear-workflow). `linear-cli doctor` checks config and connectivity, and `linear-cli doctor --fix` auto-remediates common issues.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| linear-create | Pass | Pass | Pass |
| linear-list | Pass | Pass | Pass |
| linear-search | Pass | Pass | Warn |
| linear-update | Pass | Pass | Pass |
| linear-workflow | Pass | Pass | Pass |
| linear-projects | Pass | Pass | Pass |
| linear-labels | Pass | Pass | Pass |
| linear-relations | Pass | Pass | Pass |
| linear-git | Pass | Pass | Pass |
| linear-uploads | Pass | Pass | Warn |
| linear-documents | Pass | Pass | Pass |
| linear-history | Pass | Pass | Pass |
| linear-bulk | Pass | Pass | Pass |
| linear-triage | Pass | Pass | Warn |
| linear-pr | Pass | Pass | Pass |
| linear-roadmaps | Pass | Pass | Pass |
| linear-cycles | Pass | Pass | Pass |
| linear-notifications | Pass | Pass | Pass |
| linear-initiatives | Pass | Pass | Pass |
| linear-watch | Pass | Pass | Pass |

This guide is Yellow because Snyk warns on three sampled skills: linear-search, linear-uploads and linear-triage. The Gen Agent Trust Hub and Socket pass all 20 sampled listings, and no skill carries a Fail. Only 20 of the 38 indexed listings were sampled; the other 18 are not covered by these verdicts.

## Limitations

- Snapshot data, verified 2026-11-28: 5,087 combined installs across 38 indexed listings; 138 GitHub stars; MIT licence; last pushed 2026-09-13. Counts drift over time.
- Security verdicts cover only 20 of the 38 indexed listings; the remaining 18 skills were not sampled by skills.sh.
- Install counts are small and tightly packed (101 to 188 per skill), reflecting an early-stage suite that is less battle-tested than high-volume alternatives.
- The CLI and the skills are installed separately: the binary via Cargo and the skills via `npx skills add`. A working `linear-cli` binary with valid auth is a prerequisite for the skills to be useful.
- Branch is `master` rather than `main`, so every raw.githubusercontent URL must use `master`.
- The CLI is a local tool that still handles Linear credentials, OAuth tokens and webhook secrets; read SECURITY.md and the repository threat model before production use.

## Related

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only the skills you need with `npx skills add nesszer/linear-cli --skill <name>` instead of pulling all 38.
- Authenticate first: `linear-cli auth oauth` or `LINEAR_API_KEY`; the skills drive the CLI, not a separate API.
- Read a skill's SKILL.md before relying on it; the raw path is `skills/<name>/SKILL.md` on branch master.
- Prefer `--output json --compact` when scripting, and `--id-only` for chaining one command into the next.
- Re-check the three Snyk Warn skills (linear-search, linear-uploads, linear-triage) on skills.sh before production adoption.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
