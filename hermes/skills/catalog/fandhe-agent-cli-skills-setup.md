---
title: "Fandhe Agent CLI Skills - Commit and PR Workflows"
description: "fandhe-ai/agent-cli-skills on skills.sh: 38.0K combined installs; Conventional Commits, PR and issue-tree workflow skills for coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/fandhe-agent-cli-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "conventional commits", "pull requests", "issue triage"]
---

# Fandhe Agent CLI Skills - Setup Guide

**Source:** [fandhe-ai/agent-cli-skills](https://www.skills.sh/fandhe-ai/agent-cli-skills) via skills.sh - 38.0K combined installs across 32 indexed listings; first seen 2026-11-06 (Nov 6, 2026 evening sweep)
**GitHub:** 2 stars, no licence file in the repo root, last pushed 2026-11-05, 30 SKILL.md directories split across skills/, .claude/skills/ and .agents/skills/
**Category:** CLI workflows for agents: Conventional Commits, PR creation, issue triage, review passes and skill authoring
**Quality Tier:** 🟡 Review - broad adoption and clean scanner verdicts on most samples, held back by the absence of any licence file and a two-star repository.

This is a working developer's command set, written in Japanese, for the parts of a coding session that an agent usually improvises: the commit message, the pull request body, the issue tree, the review pass. The README puts it as a collection of CLI workflow skills for Claude Code that automate everyday development under Conventional Commits, installed with the vercel-labs skills CLI.

The repository is organised in three layers, and the README is explicit about why. Most skills live as real directories under `skills/` and are symlinked from `.claude/skills/`. Three repository-management skills (`create-skill`, `create-agent`, `sweep-sync-prs`) exist only in `.claude/skills/` with no counterpart under `skills/`, because they manage this repository rather than ship to users. Three reference skills (`github-docs`, `anthropic-claude-code`, `anthropic-claude-code-extend`) live under `.agents/skills/`.

What makes the set worth reading is the discipline inside individual skills. `create-commit` scans the staged diff for secrets twice, once by pattern and once by eye, and states that pre-commit hooks must run with `--no-verify` forbidden. `create-pr` runs an OWASP Top 10 check first and aborts the PR if anything fails. `contribute-skill` refuses to push anywhere outside the `Fandhe-AI/` organisation. Those are refusal rules, not suggestions, and refusal rules are what keep an autonomous commit loop from doing damage.

## Installation

The README uses the skills CLI throughout. Show what is available first:

```bash
npx skills add Fandhe-AI/agent-cli-skills --list
```

Then install one skill, a named set, or everything:

```bash
npx skills add Fandhe-AI/agent-cli-skills --skill create-commit
npx skills add Fandhe-AI/agent-cli-skills --skill create-commit --skill create-pr --skill implement-review
npx skills add Fandhe-AI/agent-cli-skills --all
```

By default the installer creates symlinks under `.claude/skills/` in the current project. Two flags change that, in the README's wording: `--copy` writes real files instead of links, and `-g` installs into `~/.claude/skills/` for the whole user.

The repository is also listed on skills.sh, which publishes the same command under its lowercase slug:

```bash
npx skills add fandhe-ai/agent-cli-skills
```

Whichever route you take, install a slice rather than all thirty. The skills are independent, and the ones that matter to a given repository are the four or five that match its actual workflow.

## What It Provides

Twenty of the thirty-two indexed listings clear the 906-install threshold:

| Skill | Installs | Use For |
|---|---|---|
| create-plan | 2,132 | Research the codebase, then write a verifiable implementation plan into `_/local-plans/` |
| create-commit | 2,059 | Analyse the diff, scan for secrets, generate and run a Conventional Commits message |
| create-pr | 2,056 | OWASP Top 10 check, then a PR with Summary, Test plan and Design sections |
| implement-issue | 2,053 | Fetch an issue, plan, get approval, implement, test |
| create-issue | 2,052 | Create a GitHub issue with sub-issues under a parent |
| implement-review | 2,047 | Read-only review of quality, architecture and OWASP Top 10 against a diff |
| implement-review-pr | 2,044 | Review a PR: CI status, title convention, code quality, security |
| implement-issue-tree | 2,016 | Work an issue tree in post-order, in parallel worktrees, through to mergeable PRs |
| update-docs | 1,979 | Refresh the CLAUDE.md skill list and structure tree from the last docs commit |
| contribute-skill | 1,816 | Post a locally edited skill upstream as a PR, with an org allowlist guard |
| create-issue-tree | 1,778 | Break requirements into phases and create a tracked issue hierarchy |
| comment-code | 1,719 | Add or strengthen comments with the package and caller contracts in mind |
| init-claude | 1,695 | Bootstrap the `.claude/` tree: CLAUDE.md, agents, rules, skills, hooks |
| update-issue-tree | 1,682 | Reconcile an existing tree: reparent orphans, sync phase labels |
| update-claude | 1,651 | Diagnose an existing `.claude/` tree and propose the missing pieces |
| sync-skills-lock | 1,394 | Recompute `skills-lock.json` hashes against upstream sources |
| project-archive-done | 912 | Archive Done items on a GitHub Project board in bulk |
| project-add-items | 911 | Create project items from a Markdown checklist or requirements doc |
| project-init | 907 | Create a GitHub Project v2 with Status, Priority and Size fields |
| project-create-issues | 906 | Convert draft items into real issues, carrying fields and parent links |

The remaining 12 indexed listings range from 1 to 897 installs.

Two mechanics are worth knowing before you read the table as a feature list. Each skill declares a model in its frontmatter, and the choice is deliberate: `create-commit` and `project-archive-done` run on haiku, while `create-pr`, `implement-review` and the issue-tree skills run on sonnet. Mechanical work goes cheap, judgement work goes expensive. The other mechanic is the lock file. `skills-lock.json` pins each skill to a source repository and a hash, `sync-skills-lock` recomputes those hashes, and `contribute-skill` reads the source field to decide whether a push is allowed at all.

## Why This Matters for Hermes Agents

Most agent workflow advice is about prompts. This repository is about the seams, and the seams are where agents lose credibility with a team. A commit message that ignores the project's convention, a PR with no test plan, an issue that arrives as a paragraph instead of a hierarchy, a review that edits the code it is reviewing: each of those is small, and each one is the reason a team stops letting an agent touch the repository.

The concrete rules here are the transferable part. Secret scanning runs twice, by pattern and by eye, because pattern matching misses context. Hooks always run, because `--no-verify` is how a broken commit escapes. A PR body is not free-form. A review is read-only, and the fix skills are separate. An issue tree gets worked in dependency order, not in the order the agent happens to read it.

The organisational guardrails deserve a mention on their own. `contribute-skill` reads `skills-lock.json` and aborts any push whose source is not `Fandhe-AI/`, and `sync-skills-lock` skips entries that fail the same test rather than cloning them. That is an allowlist expressed as code, and it is a better pattern than an instruction in a system prompt telling the agent to be careful about where it pushes.

The costs are real. Everything is written in Japanese, including the trigger phrases, so the agent will pick up the workflow but you will be reading descriptions through translation. The skills assume `gh` is installed and authenticated, which is stated as a precondition in `create-pr`.

## Usage

| You say | What happens |
|---|---|
| "Commit this" | create-commit reads the staged diff, scans for secrets, writes a Conventional Commits message and runs the commit through the hooks |
| "Open a PR for this branch" | create-pr runs the OWASP Top 10 check, aborts on findings, otherwise drafts a PR with Summary, Test plan and Design |
| "Break this task into issues" | create-issue-tree splits the requirements at a two-hour granularity by default and creates the root, phase and child issues with sub-issue links |
| "Implement this issue" | implement-issue plans first, waits for approval, then implements and tests |
| "Review these changes before I commit" | implement-review produces a read-only pass over quality, architecture and security, with no edits |
| "Set up Claude Code in this repo" | init-claude creates CLAUDE.md, agents, rules, skills and hooks |
| "Archive the Done items on the board" | project-archive-done bulk-archives via `gh project item-archive` and reports on the built-in auto-archive setting |

## Verification

The repository is public and the paths are stable. This one returned 200 on `main` when checked on 2026-11-06:

```bash
curl -fsSL https://raw.githubusercontent.com/fandhe-ai/agent-cli-skills/main/skills/create-commit/SKILL.md | head -25
```

The response should open with frontmatter naming `create-commit`, a description in Japanese that mentions Conventional Commits and secret scanning, `model: haiku`, and `user-invocable: true`, followed by a body whose second step is the secret check.

After an install, the skills land where the flags said they would. Default project install:

```bash
ls -l .claude/skills | head
```

A user-wide install with `-g` puts them in the home directory instead:

```bash
ls ~/.claude/skills | head -30
```

Symlinks are the default, so `ls -l` should show links pointing back into a skills source directory rather than real folders. If you see real directories after a default install, either `--copy` was used or the installer changed behaviour.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| create-plan | Pass | Pass | Pass |
| update-docs | Pass | Pass | Pass |
| project-archive-done | Pass | Pass | Warn |
| create-agent | Pass | Pass | Pass |
| setup-firebase-hosting | Pass | Warn | Warn |

Three of the five samples are clean across all three scanners. The two exceptions are both project-board infrastructure rather than the commit path, which is the part of this repository that touches your code. The commit, PR and review skills all sampled Pass.

The licence is the gap that decides the tier. There is no LICENSE file in the repository root, only AGENTS.md and CLAUDE.md, so the terms of reuse rest on a README that says nothing about rights. Absent an explicit grant, treat redistribution as unresolved and ask the maintainer before shipping these skill files inside a product.

The operational risk sits in what these skills can do rather than what they contain. `create-commit` runs git and the pre-commit hooks, `create-pr` and `implement-review-pr` call the GitHub API through `gh`, `project-archive-done` mutates a project board, and `implement-issue-tree` creates worktrees and pushes branches. Install the ones that match your workflow, and read the body of any skill that pushes.

One more consideration: the `model:` keys in frontmatter are Claude Code conventions. A harness that does not understand them will ignore them silently, which means the cost design described above disappears on other runtimes.

## Limitations

- Snapshot data, verified 2026-11-06: 37,965 combined installs across 32 indexed listings; 2 GitHub stars; no licence file; last pushed 2026-11-05. Counts drift over time.
- No LICENSE file in the repository root. There is no stated grant of reuse rights, which is a bigger practical problem than the star count.
- Documentation and trigger phrases are in Japanese. The skills work, but the descriptions, argument hints and approval prompts are all written for a Japanese-speaking maintainer.
- Two indexed skills have moved. The README notes that `create-html-report` and `setup-firebase-hosting` were relocated to `Fandhe-AI/agent-util-skills`, yet both still appear in the skills.sh listing and one of them is the sample carrying two Warn verdicts.
- Built for Claude Code. Skills declare `model:` and `user-invocable:` keys and assume a `.claude/` tree, `gh` on the PATH and an authenticated session.
- Some skills encode one organisation's rules. The `Fandhe-AI/` allowlist in `contribute-skill` and `sync-skills-lock` is a safety valve for that org, and it will simply block you if you fork the set for your own.

## Related

- [CLI-Anything GUI Harnesses - Setup Guide](/hermes/skills/catalog/cli-anything-harnesses-setup)
- [Cline Skills - Official Cline 43-Skill Collection Setup](/hermes/skills/catalog/cline-skills-setup)
- [Multi-Agent Review - Adversarial Code Review Setup](/hermes/skills/catalog/multi-agent-review-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `create-commit` alone for a week. It is the skill with the tightest feedback loop, and the secret scan plus the no-`--no-verify` rule are the two habits worth adopting before anything else.
- Read the frontmatter before installing. `model: haiku` on a mechanical skill and `model: sonnet` on a review skill is a cost decision you can copy into your own skills regardless of language.
- Keep `implement-review` and the fix skills in separate runs. The review is read-only by design, and letting the same turn also edit removes the point of the pass.
- Use `--list` before `--all`. Thirty skills is more surface than most repositories need, and the issue-tree family in particular assumes a project board you may not have.
- If you fork it, replace the org allowlist. The `Fandhe-AI/` check in `contribute-skill` is the one constant that will silently stop working in your own fork.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
