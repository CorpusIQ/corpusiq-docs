---
title: "Graphite Skills - Stacked Pull Requests for Agents"
description: "withgraphite/agent-skills on skills.sh: 10.0K combined installs across 1 listing; the Graphite CLI skill for stacked PRs, restacks and submit."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/graphite-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "graphite", "pull requests", "git workflow"]
---

# Graphite Skills - Setup Guide

**Source:** [withgraphite/agent-skills](https://www.skills.sh/withgraphite/agent-skills) via skills.sh - 10.0K combined installs across 1 indexed listing; first seen 2026-11-07 (Nov 7 2026 morning sweep)
**GitHub:** 7 stars, no license file at the repository root, branch `main`, last pushed 2026-02-17, one skill directory at `skills/graphite/SKILL.md`
**Category:** Stacked pull requests for agents: branch creation, stack restacking, review submission and trunk sync through the Graphite CLI
**Quality Tier:** 🟡 Yellow - every scanner passes and this is the vendor's own skill, but the repository has no LICENSE file, 7 stars, and a one-line README that documents nothing.

Graphite is a commercial code review tool built around stacked pull requests, and this repository is the vendor's Agent Skill for its `gt` CLI. It ships as a single 344-line `SKILL.md` under `skills/graphite/`, with no scripts, no references and no manifest files. The README is one sentence long ("Agent skills to help agentic tools work with Graphite"), so the skill file is the entire document set.

The content is operational rather than conceptual. It opens with a command table that maps intent to `gt` invocation, then spends the rest of the file on the parts an agent gets wrong without being told: what makes an acceptable PR in a stack, how to name branches, what to do with untracked branches created by parallel worktrees, how to verify the stack is rooted on `main` before submitting, and how to write PR bodies without shell escaping destroying the markdown.

## Installation

The skills.sh listing documents one command for this repository:

```bash
npx skills add withgraphite/agent-skills
```

For a manual placement, the repository is a single directory:

```bash
git clone https://github.com/withgraphite/agent-skills.git
mkdir -p .agents/skills && cp -r agent-skills/skills/graphite .agents/skills/
```

The skill is a set of instructions for `gt`, not a substitute for it. The Graphite CLI has to be installed and authenticated on the host before the skill can do anything, and this repository does not document that step, so follow Graphite's own installation guide rather than guessing a package name.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| graphite | 9,989 | The Graphite CLI skill: stack creation, navigation, restacking, submit and PR body conventions |

No indexed listings fall below the threshold.

The quick reference table alone is worth the install, because it converts intent into the right subcommand: `gt create` for a new branch and PR, `gt modify` to amend, `gt up` / `gt down` / `gt top` / `gt bottom` to move through the stack, `gt ls` to view structure, `gt submit --no-interactive` to open the stack for review, `gt restack` to rebase onto trunk, `gt track --parent` to re-parent, and `gt move` to reorder.

Around that table the skill makes a set of house rulings. Atomic, narrowly scoped, small diffs rank in that order, and the file argues explicitly for more pull requests rather than fewer ("NO CHANGE IS TOO SMALL"). Branch names follow a `stack-name/terse-description` pattern with a four-branch example. Before submitting, the agent is told to confirm the first branch is parented on `main` with `gt ls`, and to fix it with `gt checkout`, `gt track -p main`, `gt restack` if it is not.

The PR body guidance is the most practical part. It forbids bash heredocs for descriptions because shell escaping breaks markdown, and instead prescribes writing `/tmp/pr-body.md` and calling `gh pr edit <PR_NUMBER> --title ... --body-file /tmp/pr-body.md`, with a required stack-context section and a why section.

## Why This Matters for Hermes Agents

Stacked PRs are a workflow where the agent's default behaviour is actively wrong. Left alone, an agent asked for a large feature produces one enormous branch, or a pile of unrelated commits on `main`. The skill encodes the opposite preference in plain language: split the work, keep each PR independently buildable, and prefer more PRs over fewer.

The second gain is mechanical correctness. `gt` is not `git`, and a model that has never used it will reach for `git rebase -i` or `git branch` where `gt create`, `gt restack` and `gt track` are the right tools. The command table means the agent chooses the correct verb on the first try instead of improvising a rebase that detaches the stack.

The third is the submit path. A stack that is not rooted on `main` submits as a chain that reviewers cannot merge in order, and the file puts a two-command check in front of `gt submit` for exactly that reason. The heredoc ban matters for the same class of failure: a PR description with a broken table is a review that stalls.

For Hermes agents working in parallel worktrees, the untracked-branch section is the specific fix. Worktrees commonly produce branches that Graphite does not know about, and `gt track` is the repair rather than deleting and recreating the branch.

## Usage

| You say | What happens |
|---|---|
| "Split this feature into a stack of PRs" | The agent creates one branch per change with `gt create <stack-name>/<description> -m ...`, then submits the whole stack with `gt submit --no-interactive` |
| "Restack my branches on the new main" | The agent runs `gt restack`, which rebases the stack onto trunk in order rather than rebasing branches one at a time |
| "Move this branch below the other one" | The agent uses `gt move`, then `gt restack`, instead of hand-editing branch parents |
| "My PRs are showing the wrong parent" | The agent checks `gt ls`, re-parents with `gt track -p main`, and restacks |
| "Update the description on PR 42" | The agent writes `/tmp/pr-body.md` and calls `gh pr edit 42 --body-file /tmp/pr-body.md`, avoiding heredoc escaping |
| "This branch is untracked, fix it" | The agent runs `gt track -p main` on the branch, which is the documented repair for branches created outside Graphite |

## Verification

Read the skill before installing. This path returned HTTP 200 on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/withgraphite/agent-skills/main/skills/graphite/SKILL.md | head -30
```

It should open with `name: graphite`, then an `allowed-tools` list restricted to `Bash(gt *)`, several `git` subcommands and `Bash(gh pr *)`, then a "Quick Reference" table whose first row is `gt create`.

After install, confirm the file is in place, adjusting the path to the directory your agent scans:

```bash
ls .agents/skills/graphite/SKILL.md
```

To check the runtime side, run `gt ls` inside a repository that has been initialised with Graphite. A tracked stack prints its branch tree; an uninitialised repository errors, which tells you the CLI is missing before the agent tries to use it.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| graphite | Pass | Pass | Pass |

The payload is markdown plus a narrowed tool grant. The frontmatter's `allowed-tools` list is the security-relevant part: it permits `Bash(gt *)`, `git add`, `git reset`, `git diff`, `git status`, `git stash`, `git checkout`, `git rebase`, `git branch` and `gh pr`, and nothing else. There is no arbitrary shell, no network call and no file write declared by the skill itself.

That narrow grant has a practical consequence. The skill also instructs the agent to run the project's lint, build and test commands after creating each PR, and those commands are not covered by the allowlist. On a host that enforces `allowed-tools` strictly, expect approval prompts at the validation step; on a host that ignores the field, expect no restriction at all.

No LICENSE file is present at the repository root, so there is no repository-level grant to redistribute the text even though the skill is published openly. Check Graphite's own terms before bundling it into a product.

## Limitations

- Snapshot data, verified 2026-11-07: 9,989 combined installs across 1 indexed listing; 7 GitHub stars; no license file; last pushed 2026-02-17. Counts drift over time.
- The Graphite CLI is a prerequisite that the repository never mentions. Without an authenticated `gt` on the host, the skill produces commands that fail at the first invocation.
- No LICENSE file at the root means no clear redistribution terms, which matters more than usual here because the content is vendor-authored guidance for a paid product.
- The README is a single sentence and carries no install command, so the command above comes from the skills.sh listing page rather than the repository.
- Last push was 2026-02-17. Graphite's CLI evolves, and there is no version pin, changelog or release to check the documented flags against.
- The workflow assumes one repository per stack. Multi-repository stacks and cross-repo dependencies are not covered.

## Related

- [gh-stack - GitHub Stacked PRs Skill Setup](/hermes/skills/catalog/gh-stack-setup)
- [Cli Anything Harnesses Setup](/hermes/skills/catalog/cli-anything-harnesses-setup)
- [Fandhe Agent CLI Skills - Commit and PR Workflows](/hermes/skills/catalog/fandhe-agent-cli-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Tell the agent the stack shape up front ("three PRs: schema, API, UI"). It produces better boundaries than asking for the split afterwards.
- Run `gt ls` before any submit. One parent check prevents a stack that reviewers cannot merge in sequence.
- Keep the heredoc ban. `gh pr edit --body-file /tmp/pr-body.md` is the reliable path for PR descriptions with tables or code blocks.
- Pair it with `gh` for the parts Graphite does not own, such as editing titles, labels and reviewers on the resulting PRs.
- If you work in parallel worktrees, budget for `gt track -p main` after each new branch. Untracked branches are the most common source of "cannot perform this operation" errors.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
