---
title: gh-stack - GitHub Stacked PRs Skill Setup Guide
description: "github/gh-stack - 9.6K installs, 1.4K stars: the official GitHub CLI extension for stacked branches and pull requests, packaged as an agent skill - create, rebase, navigate, submit, and merge layered PR chains from a Hermes agent."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gh-stack-setup/"
robots: "index,follow"
last_updated: "2026-08-30"
tags: ["hermes skill", "agent skill", "skill setup", "github", "git", "pull requests", "cli", "stacked prs", "code review"]
---

# gh-stack - Setup Guide

**Source:** [github/gh-stack](https://skills.sh/github/gh-stack/gh-stack) (9.6K installs)
**GitHub:** [github/gh-stack](https://github.com/github/gh-stack) (MIT license, 1.4K stars, official GitHub org)
**Skill:** `gh-stack`, 9.6K installs
**Category:** Developer Tools / Git & GitHub Workflow
**First Seen:** skills.sh Apr 10, 2026; catalogued in the Aug 30, 2026 sweep
**Quality Tier:** 🟢 Production - first-party publisher (official `github` org) and all three skills.sh security audits Pass (see Security Audit Status)

`gh stack` is GitHub's own CLI extension for **stacked branches and pull requests**. A stack is an ordered chain of branches rooted on a trunk, where each branch carries exactly one PR based on the branch below it - so a reviewer sees only that layer's diff. Large changes that would be one un-reviewable mega-PR become a sequence of small, logically separated PRs, and the extension automates the tedious parts: creating layers, keeping them rebased, setting correct PR base branches, and navigating between them.

The repo ships the skill under `skills/gh-stack/SKILL.md` with `metadata.author: github`, and the README carries a first-party agent-integration path (`gh skill install github/gh-stack`). The skill is the reference for how any agent - Hermes included - should drive the `gh stack` CLI.

---

## Installation

### 1. Install the CLI extension (required - the skill drives this binary)

```bash
gh extension install github/gh-stack
```

Requires the [GitHub CLI](https://cli.github.com/) (`gh`) v2.0+.

### 2. Skill-level setup from the repo's SKILL.md

```bash
git config rerere.enabled true         # remember conflict resolutions across rebases
git config remote.pushDefault origin   # required if the repo has more than one remote
```

`gh stack init` also enables `git rerere` automatically.

### 3. Install the skill

GitHub's native agent-integration path:

```bash
gh skill install github/gh-stack
```

Via skills.sh (the installer clones the repo and discovers the skill tree):

```bash
npx skills add https://github.com/github/gh-stack --skill gh-stack
```

## Prerequisites

| Requirement | Details |
|---|---|
| **GitHub CLI** | `gh` v2.0+ (`gh auth login` with an authenticated account) |
| **git** | Any recent git; `rerere.enabled` recommended for rebase automation |
| **`remote.pushDefault`** | Set `git config remote.pushDefault origin` when the repo has multiple remotes |
| **Repo access** | Push access to the target repo for `gh stack push` / `submit` |

## Core Skill

| Skill | Installs | Use For |
|---|---|---|
| gh-stack | 9.6K | Stacked PR management - creating stacks, splitting work into reviewable layers, keeping layers rebased, submitting and merging linked PR chains. Triggers: "split this into stacked PRs", "stack of branches", "dependent PRs", "gh stack" |

## Command Reference

A stack is an ordered list of branches rooted on a **trunk** (typically `main`). The **bottom** is closest to the trunk and merges first; `up` moves away from the trunk, `down` toward it. Stack metadata lives in `.git/gh-stack` (a JSON file, never committed); interrupted-rebase state lives in `.git/gh-stack-rebase-state`.

| Command | Purpose |
|---|---|
| `gh stack init` | Start a new stack. Non-interactive: `gh stack init feature-auth feature-api feature-ui`. `-b, --base <branch>` overrides the trunk |
| `gh stack add [branch]` | Add a new layer on top of the current stack (must be on the topmost branch). Flags: `-m <msg>` commit before branching, `-A` stage all, `-u` stage tracked |
| `gh stack checkout` | Switch to a specific layer of the stack |
| `gh stack rebase` | Rebase a layer on the one below it (rerere remembers conflict resolutions) |
| `gh stack modify` | Edit the stack - rename/reorder layers, change the base |
| `gh stack sync` | Pull trunk updates and propagate them through the layers |
| `gh stack push` | Push all stack branches to the remote |
| `gh stack submit` | Open one PR per layer, base of each set to the branch below, linked as a GitHub Stack |
| `gh stack link` | Link existing PRs into a Stack on GitHub |
| `gh stack merge [<stack-number>\|<pr-number>]` | Merge the stack up to and including a layer - all-or-nothing, in a single operation. `--yes` for non-interactive runs |
| `gh stack view` | Print the stack trunk-first, left to right: `(main) <- auth <- api <- frontend` |
| `gh stack unstack` | Convert stacked branches back to independent branches |
| `gh stack feedback` | Open feedback about the extension |
| `gh stack alias` | Manage shell aliases for stack commands |

Exit codes are documented and stable: `0` success, `1` generic error, `2` not in a stack, `3` rebase conflict, `4` GitHub API failure, `5` invalid arguments, `6` disambiguation required, `7` rebase already in progress, `8` stack locked by another process.

Non-interactive behavior: commands branch on whether stdout is a TTY. Piped runs need explicit arguments (or `--yes`) because interactive prompts are skipped.

## Security Audit Status (skills.sh, verified Aug 30, 2026)

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gh-stack | Pass | Pass | Pass |

All three audits Pass - the basis for the 🟢 Production tier.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Multi-cron shared repo changes** | corpusiq-docs is written to by several crons at once - a sweep's guide + `catalog/index.md` entry + PROGRESS.md bumps stack cleanly as dependent layers instead of one conflicted mega-commit |
| **Reviewable sweep shipping** | Split a docs sweep into layers (new guide -> index updates -> stat bumps) so each change set is reviewable on its own |
| **Dependent feature work** | Agent build chains where layer N+1's code depends on layer N (e.g., CLI extension + skill docs + install automation) stay ordered and merge in the correct sequence |
| **Safe batch merges** | `gh stack merge --yes` gives an all-or-nothing merge gate - if any layer can't merge, none merge |
| **Conflict-tolerant rebases** | Automatic `git rerere` means a recurring conflict in a rebase chain is resolved once, then replayed - valuable for crons that repeatedly rebase long-running branches |

## Limitations / Verification

- Below the 20K-install drafting bar; drafted on **publisher authority**: first-party `github` org (1.4K stars, MIT), GitHub's own `gh skill install` agent-integration channel, and a clean audit slate - the same brand-authority precedent as trailofbits and vercel-labs clusters.
- The skill assumes `gh` is authenticated and the agent has push access; it does not bypass repo permission models.
- TTY-branching means cron/pipe contexts must pass explicit arguments (`gh stack merge --yes`, non-interactive `init` branch lists) or commands error cleanly with exit code 5.

Verification after install:

```bash
gh extension list | grep gh-stack          # extension registered
gh skill list 2>/dev/null | grep gh-stack  # skill installed (gh >= 2.8x agent-integration channel)
gh stack view                              # exit 2 outside a stack = CLI works, just no stack yet
```

## Related

- [gh-issue-sync - Local Markdown GitHub Issues Skill Setup](/hermes/skills/catalog/gh-issue-sync-setup)
- [Native Development Skills](/hermes/skills/development) - github-repo-management and other built-in GitHub workflow skills
- [Skills Marketplace](/hermes/skills/marketplace) - more discovery batches

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
