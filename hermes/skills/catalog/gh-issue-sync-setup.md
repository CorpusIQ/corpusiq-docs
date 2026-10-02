---
title: gh-issue-sync - Local Markdown GitHub Issues Sync
description: "mitsuhiko/gh-issue-sync - 1 skill, 2.5K installs, by Armin Ronacher (Flask creator): manage GitHub issues as local Markdown files - triage, search, edit, and create issues without leaving the editor or terminal."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gh-issue-sync-setup/"
robots: "index,follow"
last_updated: "2026-08-24"
tags: ["hermes skill", "agent skill", "skill setup", "github", "issue management", "markdown"]
---

# gh-issue-sync - Setup Guide

**Source:** [mitsuhiko/gh-issue-sync](https://skills.sh/mitsuhiko/gh-issue-sync)
**GitHub:** [mitsuhiko/gh-issue-sync](https://github.com/mitsuhiko/gh-issue-sync) (160⭐, Apache-2.0, by Armin Ronacher)
**Skills:** 1 skill (gh-issue-sync), 2.5K installs
**Category:** Developer Tools / GitHub
**First Seen:** August 24, 2026 sweep (skills.sh first-listed Jan 22, 2026)
**Quality Tier:** 🟢 Production - authored by mitsuhiko (Flask, Jinja2), live since January 2026, 2.5K installs; Gen Agent Trust Hub Pass, Socket Pass, Snyk Warn

gh-issue-sync syncs GitHub issues to local Markdown files under `.issues/open/` and `.issues/closed/`, so an agent (or a human) can triage, search, edit, and create issues without leaving the editor or terminal. Changes are diffable, greppable, and reviewable like code - then pushed back to GitHub with a single command. For a repo like corpusiq-docs with open community epics (issues #18, #12, #7), this turns issue backlog management into a plain file workflow the agent can script.

---

## Installation

The maintained-checkout pattern (recommended - keeps the skill updateable with `git pull`):

```bash
git clone https://github.com/mitsuhiko/gh-issue-sync.git
```

```yaml
# ~/.hermes/config.yaml
skills:
  external_dirs:
    - /absolute/path/to/gh-issue-sync
```

Or via the skills.sh marketplace:

```bash
npx skills add mitsuhiko/gh-issue-sync
```

## Commands

```bash
gh-issue-sync init            # Initialize in a git repo
gh-issue-sync pull            # Fetch open issues (--all for closed too)
gh-issue-sync push            # Push local changes (--dry-run to preview)
gh-issue-sync list            # List issues (supports gh issue list flags + --search)
gh-issue-sync new "Title"     # Create issue (--label, --edit)
gh-issue-sync close 42        # Close (--reason completed|not_planned)
gh-issue-sync reopen 42
gh-issue-sync status          # Show local changes
gh-issue-sync diff 42         # Show diff (--remote to re-fetch)
```

## Prerequisites

| Requirement | Details |
|---|---|
| **gh CLI** | The tool builds on the GitHub CLI; authenticated `gh` is expected |
| **A git repo** | Run `gh-issue-sync init` inside the repo you want issue sync for |

## Core Skill

| Skill | Installs | Use For |
|---|---|---|
| gh-issue-sync | 2.5K | Manage GitHub issues locally as Markdown files - triaging, searching, editing, and creating issues without leaving your editor or terminal |

## Security Audit Status (skills.sh, verified Aug 24, 2026)

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gh-issue-sync | Pass | Pass | Warn |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Issue backlog as files** | Sync corpusiq-docs issues (community epics #18, #12, #7 and the open PR queue) to `.issues/` - triage and label in bulk with grep/scripting instead of the web UI |
| **Reviewable issue edits** | `push --dry-run` + `diff` give a code-review-style path for bulk issue updates - matches the agent's verify-before-assertion discipline |
| **Agent-scripted triage** | The plain Markdown format makes automated triage cron jobs (stale-issue sweeps, label normalization) simple shell scripts |

## Limitations / Verification

- Snyk audit is Warn-level on skills.sh - review dependencies before production use, though the tool's surface is a thin CLI over `gh`.
- Requires the `gh` CLI and its auth; not a replacement for the GitHub API in agent workflows, a complement for human/file-based workflows.
- Single-purpose tool - issue sync only, no PR or project-board surface.

## Related

- [GitHub Code Review Setup](/hermes/skills/catalog/github-code-review-setup) - review workflow skills
- [Skills Marketplace](/hermes/skills/marketplace) - more discovery batches
