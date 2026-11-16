---
title: "gh-axi - Token-Efficient GitHub CLI for Agents"
description: "kunchenguid/gh-axi: 9.9K combined installs from one listing, a token-efficient GitHub CLI wrapper with structured output and next-step hints for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gh-axi-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "github", "cli", "devops"]
---

# gh-axi - Setup Guide

**Source:** [kunchenguid/gh-axi](https://www.skills.sh/kunchenguid/gh-axi) via skills.sh - 9.9K combined installs across 1 indexed listing; first seen Nov 14, 2026 (Nov 14 evening sweep)
**GitHub:** 367 stars, MIT license, `main` branch, last pushed 2026-11-14, one `SKILL.md` at `skills/gh-axi/SKILL.md` over a TypeScript CLI in `src/` with tests in `test/`
**Category:** GitHub and CI operations for autonomous agents
**Quality Tier:** 🟡 Yellow - the single sampled skill carries Socket and Snyk Warn verdicts, with no Fail in the sample.

gh-axi is a wrapper around the official GitHub CLI built for agents rather than for people. It keeps `gh` as the transport and changes what the agent sees: compact structured output instead of prose, suggested next commands after each call, and errors that come back as typed fields instead of a wall of text.

The skill that ships with it is deliberately thin. It does not restate the command list, because installed copies go stale; it tells the agent to read the current truth from `npx -y gh-axi --help` at call time. The repository's own benchmark is the interesting part: it claims the lowest input tokens, cost and duration of five GitHub interface setups tested on the same 17 tasks.

## Installation

Install the skill with the skills CLI, which is the documented path:

```bash
npx skills add kunchenguid/gh-axi --skill gh-axi -g
```

That is the whole setup, with no `npm install` step: the CLI itself runs through `npx -y gh-axi` on demand. The documented prerequisite is the official `gh` CLI, installed and authenticated with `gh auth login`, on Node 20 or later.

For a single project instead of every project, drop the `-g` flag. If `gh` lives somewhere non-standard, set `GH_BIN` to point at the binary, and for GitHub Enterprise authenticate that host and pass `--hostname` or set `GH_HOST`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| gh-axi | 9,858 | GitHub operations from an agent: issues, pull requests, stacked PRs, workflow runs, releases, labels, gists, Projects v2, Actions secrets and raw API access. |

The single indexed listing appears in the table above.

## Why This Matters for Hermes Agents

A Hermes agent that touches GitHub usually does it through shell calls, and the cost of that is paid twice: once in tokens for raw `gh` output, and again in turns spent guessing the next command. gh-axi targets both. Structured output replaces the human-formatted tables, and each response carries the next step, which shortens the loop between "the CI run failed" and "here is the failing job".

The repository publishes its own measurement of that difference. In its benchmark, 17 real GitHub tasks (issue triage, PR review prep, CI failure investigation) ran five times each through five interface setups, with an LLM judge scoring task success:

| Setup | Success | Avg input tokens | Avg cost per task | Avg duration |
|---|---|---|---|---|
| gh-axi | 100% | 46,462 | $0.050 | 15.7s |
| gh CLI, raw | 86% | 47,076 | $0.054 | 17.4s |
| GitHub MCP, code execution | 84% | 137,409 | $0.101 | 43.4s |

Against the GitHub MCP server the claimed saving is roughly two thirds of the cost with 74 percent fewer input tokens, and half the turns. Treat the numbers as the author's own measurement on his own harness rather than as an independent audit.

The frontmatter is written for this stack in particular. It declares `metadata.hermes` tags for github, git, ci, pull-requests, releases and projects, and a `devops` category, so a Hermes agent can categorize the skill and load it when a task touches a repository. The skill is also marked `user-invocable: false`, which keeps it out of the slash-command list and leaves loading to the agent's own recognition.

## Usage

| You say | What happens |
|---|---|
| "File a bug for this stack trace" | Creates the issue with gh-axi, which returns the issue number and the suggested next action. |
| "What failed in CI on the last push?" | Lists the failing workflow run, then narrows to the failing job and its log lines. |
| "Review PR 412" | Fetches the diff and review state in a compact form and suggests the review commands. |
| "Cut a release for v2.3.0" | Runs the release command and reports the created release with its URL. |
| "Open the secret in Actions" | Manages Actions secrets and variables, returning names only, never values. |
| "Stack these three PRs" | Uses the stacked PR commands, which require the official `gh extension install github/gh-stack`. |
| "List my open issues assigned this week" | Searches issues with the structured search output and the counts per label. |

## Verification

Read the stub before installing, then confirm the CLI answers on your machine:

```bash
curl -fsSL https://raw.githubusercontent.com/kunchenguid/gh-axi/main/skills/gh-axi/SKILL.md | head -30
npx -y gh-axi --help
gh auth status
```

The skill file itself points at the CLI for current guidance, so `--help` is the authoritative command list rather than any page about it.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gh-axi | Pass | Warn | Warn |

Two of the three auditors carry a Warn and none fails. The wrapper executes the official `gh` binary and shells out to `npx`, so review the version you install and pin it if your agent runs unattended.

## Limitations

- Snapshot data, verified 2026-11-14: 9,858 combined installs across 1 indexed listing; 367 GitHub stars; MIT; last pushed 2026-11-14. Counts drift over time.
- It is a wrapper, not a replacement: `gh` must be installed and authenticated first, and older `gh` versions return a structured error instead of running the command.
- Some features have version floors. Attaching a file on issue and PR create, edit or comment needs `gh` 2.99.0 or later, and closing an issue as a duplicate needs 2.88.0 or later.
- Stacked pull request commands need the separate `gh extension install github/gh-stack`; without it those commands fail.
- The benchmark is the author's own harness with one model and an LLM judge, so the cost and success figures are not an independent benchmark.
- Two of three sampled verdicts are Warn. If your policy requires a clean Socket and Snyk pass, this skill does not meet it today.

## Related

- [gh-stack - GitHub Stacked PRs Skill Setup](/hermes/skills/catalog/gh-stack-setup)
- [gh-issue-sync - Local Markdown GitHub Issues Skill Setup](/hermes/skills/catalog/gh-issue-sync-setup)
- [Linear CLI - Issue Tracking from the Terminal](/hermes/skills/catalog/linear-cli-setup)
- [Awesome Copilot - MCP Server Generators & GitHub Automation Setup](/hermes/skills/catalog/awesome-copilot-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `npx -y gh-axi` with no arguments first: it prints a dashboard for the current repository, which is the fastest way to see whether the wrapper sees your checkout correctly.
- Keep the skill installed and skip the extra plumbing. The stub is the point: the CLI carries the command surface, so there is nothing to update in the skill when flags change.
- Install `github/gh-stack` at the same time if your workflow uses stacked pull requests, rather than discovering the gap mid-review.
- Set `GH_BIN` when several `gh` versions coexist, so the wrapper and your shell use the same binary.
- If your agent retries a failed comment, read the error first: the documented behaviour warns against retrying a mutation whose readback failed.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
