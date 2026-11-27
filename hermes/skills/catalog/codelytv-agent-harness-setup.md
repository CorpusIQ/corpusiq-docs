---
title: "Codely Agent Harness - Spec and Commit Workflow Skills"
description: "codelytv/agent-harness: 2.0K combined installs. Skills, plugins and hooks that turn conventions into rules and plan work in reviewable phases."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/codelytv-agent-harness-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "conventional commits", "plan and implement", "openspec"]
---

# Codely Agent Harness - Setup Guide

**Source:** [codelytv/agent-harness](https://www.skills.sh/codelytv/agent-harness) via skills.sh - 2.0K combined installs across 35 indexed listings; first documented 2026-11-27 (morning sweep)

**GitHub:** [codelytv/agent-harness](https://github.com/codelytv/agent-harness) - 349 stars, no license file (the Claude Code plugin manifest declares MIT), branch main, last pushed 2026-11-23; 13 skill directories under .agents/skills/<name>/SKILL.md with references/ folders, plus Claude Code plugins under .claude/plugins/ and export-blocking hooks for Claude Code, Cursor, Copilot and OpenCode

**Category:** Agent coding harness: Conventional Commits, plan-and-implement workflows, OpenSpec specs and deterministic rule enforcement

**Quality Tier:** 🟠 Orange - eight sampled listings fail the Socket audit (create-plan, create-plan-github, implement-plan-phase, create-plan-subagents, create-doc, implement-plan-phase-github, create-plan-gitlab, implement-plan-phase-gitlab) and several others carry Snyk Warns

Codely is a Spanish programming-education publisher (CodelyTV), and agent-harness is its in-house coding-agent harness: a set of skills, Claude Code plugins and pre-execution hooks with one stated goal, that an agent "writes the code you expect, the way you expect". The central idea is to stop reviewing code and start reviewing outputs by turning conventions into rules that fail in seconds, so the agent corrects itself.

The repository's 13 skill directories under `.agents/skills/` implement the workflow: `deterministify` and `create-rule` turn docs and corrections into linter rules and tests, `git-commit` writes Conventional Commits, `create-pull-request` produces evidence-backed PR descriptions, and `create-plan` with `implement-plan-phase` splits larger work into reviewable phases with GitHub, GitLab and subagent variants. The install index is wider than the tree: skills.sh lists 35 listings because the same skills are indexed under their plugin-registered `codely-` names, their clean `.agents` names, and a handful of colon-prefixed names.

## Installation

The README's primary route is skills.sh, and a Claude Code plugin route sits behind it:

```bash
npx skills@latest add codelytv/agent-harness
```

Pick the skills you want and the agents to install them on, then run one, for example `/create-rule`. Claude Code users can install the plugin, which registers the skills under the `codely-` namespace:

```bash
/plugin marketplace add CodelyTV/agent-harness
/plugin install codely-skills@codely
```

The README also documents an OpenSpec custom schema and two extra Claude Code plugins:

```bash
npx degit CodelyTV/agent-harness/openspec/schemas/codely-spec-plan openspec/schemas/codely-spec-plan
```

```bash
/plugin install ste100@codely
/plugin install ts7-lsp@codely
```

Rules live in `AGENTS.md` and skills in `.agents/skills/`, and each agent expects them in a different path. The `make` targets create the symlinks (not committed), so run the ones you need after cloning:

```bash
make claude-symlinks
make codex-symlinks
make cursor-symlinks
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| codely-git-conventional-commit | 277 | Create a git commit that follows the team's Conventional Commit conventions; the plugin-registered name for git-commit. |
| codely-plan-phase-implement | 258 | Implement one phase of a plan, then stop for user review; the plugin-registered name for implement-plan-phase. |
| codely-doc-create | 252 | Deprecated; create documentation from conversation context, superseded by create-rule. |
| codely-plan-create-subagents | 248 | Create a plan for a task, delegating codebase exploration to cheaper subagents running in parallel. |
| codely-plan-create-github | 208 | Turn a GitHub issue into a parent plan issue with one child issue per phase, linked as native sub-issues. |
| codely-plan-phase-implement-github | 158 | Implement one phase of a GitHub-issue plan; opens a pull request per phase that references the issue, never merges. |
| codely-openspec-spec-create-from-code | 53 | Create OpenSpec specs of behaviour already in the code, so the next change can modify or remove it. |
| codely-plan-create | 43 | Create a plan for a task, split into reviewable phases. |
| git-commit | 42 | Commit changes with a Conventional Commit message and the agent co-author trailer. |
| deterministify | 42 | Turn repository conventions into deterministic rules (linters, lint rules, tests) that fail in seconds. |
| create-rule | 42 | Turn one new convention into a deterministic rule, or a minimal doc with the reason when no rule can check it. |
| openspec-create-spec-from-code | 38 | Create OpenSpec specs of existing behaviour so the next change can modify or remove it. |
| create-pull-request | 34 | Write a pull request title and description from the team template with before/after evidence of the change. |
| create-plan | 31 | Start a larger task with a plan split into reviewable phases. |
| create-plan-github | 31 | Store a plan as GitHub issues, one child issue per phase. |

All 15 rows in the table clear the cut-off. The remaining 14 indexed listings range from 3 to 29 installs. Six further listings appear in the index under colon-prefixed names (codely:git-commit, codely:doc-create, codely:plan-create, codely:plan-create-github, codely:plan_phase-implement, codely:plan_phase-implement-github) at 1 install each; the install table cannot represent those names, so they are noted here instead.

## Why This Matters for Hermes Agents

The harness's core claim is a workflow change, not a library: review outputs, not code. `deterministify` and `create-rule` close the loop between "I corrected you" and "you will not do it again" by turning conventions into linter rules and tests that fail in seconds. `git-commit` and `create-pull-request` standardize the two artifacts a reviewer actually sees, the commit and the PR, so the agent writes Conventional Commits and evidence-backed descriptions. `create-plan` with `implement-plan-phase` makes large tasks reviewable one phase at a time, with GitHub, GitLab and parallel-subagent variants, and it never commits or merges on its own. OpenSpec users get `openspec-create-spec-from-code` so a spec exists before the next change. The export-blocking hooks are a security pattern worth copying on their own: they stop an agent from leaking environment variables through `export`. For builders, the one-source-many-symlinks layout (AGENTS.md plus `.agents/skills/`, linked per agent) is a clean way to serve the same rules to every agent runtime.

## Usage

| You say | What happens |
|---|---|
| "/deterministify docs" | Turns every checkable convention in the docs into a linter rule or test. |
| "/create-rule" | After a correction, turns the convention into a rule, or a minimal doc with the reason when no rule fits. |
| "/git-commit" | Creates a Conventional Commit with the agent co-author trailer. |
| "/create-pull-request" | Writes the PR title and description from the template with screenshots, videos and diagrams. |
| "/create-plan" | Splits a larger task into reviewable phases. |
| "/implement-plan-phase" | Implements one phase, then stops for review; never commits automatically. |
| "/openspec-create-spec-from-code" | Writes OpenSpec specs of existing behaviour before the next change. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/codelytv/agent-harness/main/.agents/skills/git-commit/SKILL.md
```

Review the plugin manifest, which lists the 13 skills, before installing:

```bash
curl -sL https://raw.githubusercontent.com/codelytv/agent-harness/main/.claude-plugin/plugin.json
```

The manifest should name git-commit, create-pull-request, create-rule, create-doc, deterministify, create-plan and its subagents/github/gitlab variants, implement-plan-phase and its variants, and openspec-create-spec-from-code.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| codely-git-conventional-commit | Pass | Pass | Pass |
| codely-plan-phase-implement | Pass | Pass | Pass |
| codely-doc-create | Pass | Pass | Pass |
| codely-plan-create-subagents | Pass | Pass | Pass |
| codely-plan-create-github | Pass | Pass | Warn |
| codely-plan-phase-implement-github | Pass | Pass | Warn |
| codely-openspec-spec-create-from-code | Pass | Pass | Pass |
| codely-plan-create | Pass | Pass | Pass |
| git-commit | Pass | Pass | Warn |
| deterministify | Pass | Pass | Warn |
| create-rule | Pass | Pass | Warn |
| openspec-create-spec-from-code | Pass | Pass | Pass |
| create-pull-request | Pass | Pass | Warn |
| create-plan | Pass | Pass | Fail |
| create-plan-github | Pass | Pass | Fail |
| implement-plan-phase | Pass | Pass | Fail |
| create-plan-subagents | Pass | Pass | Fail |
| create-doc | Pass | Pass | Fail |
| implement-plan-phase-github | Pass | Pass | Fail |
| create-plan-gitlab | Pass | Pass | Fail |
| implement-plan-phase-gitlab | Pass | Pass | Fail |
| codely-plan-create-gitlab | Pass | Pass | Warn |
| codely-plan-phase-implement-gitlab | Pass | Pass | Warn |
| docs-to-rules | Pass | Pass | Pass |

Every sampled listing passes the Gen Agent Trust Hub, which is the consistency to note: the failures are concentrated in Socket, with eight listings failing and several more warning on Snyk. The skills themselves are Markdown, but the repository ships executable shell hooks (`.cursor/hooks/block-export.sh`, `.github/hooks/block-export.sh`), a TypeScript plugin (`.opencode/plugins/block-export.ts`) and symlink-generation scripts, so it is not Markdown-only. Review those before adopting the hook pattern.

## Limitations

- Snapshot data, verified 2026-11-27: 2,000 combined installs across 35 indexed listings; 349 GitHub stars; no license file; last pushed 2026-11-23. Counts drift over time.
- The repository has no LICENSE file even though the Claude Code plugin manifest declares MIT. Treat the repository tree as unlicensed unless the publisher clarifies.
- The install index counts the same skills several ways: plugin-registered `codely-` names, clean `.agents/skills/` names, and six colon-prefixed listings at 1 install each. The table lists the 15 clean-name listings at or above 30 installs; 14 more clean listings sit at 3 to 29 installs, and 6 colon-named listings sit at 1 install each.
- The `codely-` prefixed skills, which hold the highest install counts, are the same skill directories served through the Claude Code plugin rather than separate implementations; installing both the plugin and the raw skills duplicates them.
- Eight sampled listings fail the Socket audit (the create-plan and create-doc families). The failure reasons are not published beside the verdicts, so check skills.sh before production use.
- The courses that explain each skill are in Spanish; the skill text itself is English.

## Related

- [Fandhe Agent CLI Skills - Commit and PR Workflows](/hermes/skills/catalog/fandhe-agent-cli-skills-setup)
- [Awesome Copilot - MCP Server Generators & GitHub Automation Setup](/hermes/skills/catalog/awesome-copilot-setup)
- [Hermes Agent Skill Authoring - Official SKILL.md Writing Guide](/hermes/skills/catalog/hermes-agent-skill-authoring-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install via the Claude Code plugin (`codely-skills@codely`) to get the `codely-` prefixed names plus the ste100 and ts7-lsp plugins from one marketplace.
- Run `make claude-symlinks` or `make codex-symlinks` after a clone; the symlinks are not committed and each agent looks in a different path.
- After every correction, run `/create-rule` so the fix becomes a rule rather than a session memory.
- Use the codely-spec-plan OpenSpec schema if you already run OpenSpec; it reduces each change to a lean spec plus a plan.md.
- Copy the export-blocking hooks even if you skip the skills; they stop an agent from leaking environment variables through `export`.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
