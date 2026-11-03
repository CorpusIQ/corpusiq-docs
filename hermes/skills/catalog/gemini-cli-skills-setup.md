---
title: "Gemini CLI Skills - Repository Workspace Pack"
description: "google-gemini/gemini-cli: 21.7K combined installs. The repo's own in-tree skills for PR review, docs, changelogs, behavioural evals and CI triage."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gemini-cli-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "gemini cli", "code review", "ci"]
---

# Gemini CLI Skills - Setup Guide

**Source:** [google-gemini/gemini-cli](https://www.skills.sh/google-gemini/gemini-cli) via skills.sh - 21.7K combined installs across 19 indexed listings; first seen 2026-10-31 (evening sweep)

**GitHub:** [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) - 108,637 stars, Apache-2.0, branch main, last pushed 2026-11-01T01:14:56Z; 25 `SKILL.md` directories, 13 of them under `.gemini/skills/` and the rest scattered through `packages/` and `tools/`

**Category:** Gemini CLI's own in-repo skills: PR review, changelog writing, behavioural evals and CI helpers

**Quality Tier:** 🟡 Yellow - code-reviewer and pr-address-comments each carry a Snyk Warn, so the pack is Yellow even though every Gen Agent Trust Hub and Socket verdict in the sample is a Pass

This is not a skill pack that happens to live in a repository. It is the working set of skills the Gemini CLI team uses on its own codebase, which is why the sizes in the table are so uneven: `code-reviewer` at 9,691 installs and `docs-writer` at 3,134 are general-purpose enough to travel, while `skill-creator` sits at 10 and the four bot skills between 140 and 180 installs are only meaningful inside this project. Read it as a source of good, battle-tested skill text rather than as a suite to install wholesale.

The file layout reflects that history, and it is the thing to understand before installing anything. The primary set is 13 skills in `.gemini/skills/`, which is Gemini CLI's workspace skills directory. The other six listings live in unusual places: `skill-creator` ships as a built-in skill in `packages/core/src/skills/builtin/`, `pirate-skill` is test data in `packages/sdk/test-data/skills/`, and `critique`, `memory`, `metrics` and `prs` are the internal phases of the GitHub bot under `tools/gemini-cli-bot/.gemini/skills/`. A further six directories carry a `SKILL.md` but are not indexed at all, including an `antigravity-support` builtin and a `greeter` example used in the extension docs.

The contents split by workflow. Review is the strongest cluster: `code-reviewer` handles local diffs and remote pull requests by ID or URL, `review-duplication` hunts reinvented wheels during a review, `string-reviewer` polices user-facing copy and `pr-address-comments` works through review comments on the current branch. Authoring is `pr-creator`, `github-issue-creator` and `docs-writer`. Release work is `docs-changelog`. Verification is `behavioral-evals`, `ci`, `agent-tui` and `tui-tester`, which together cover the decision-logic, workflow and terminal-output layers of testing.

One caveat belongs up front rather than in Limitations. The repository README's install banner states that Gemini CLI itself is aimed at Gemini Code Assist Standard or Enterprise licenses on Google Cloud, that free individual access and Google AI Pro and Ultra moved to Antigravity CLI, and that the CLI is not tuned for the Gemini 4 series. These skills are markdown, so they load into any agent that reads `SKILL.md`, but the tool they were written for has a narrower audience than its star count suggests.

## Installation

There is no skills section in the repository README, because skills here are part of the product's own development setup rather than a distributable pack. The authoritative instructions are in the project docs, `docs/cli/skills.md`, which document the discovery tiers and the management commands. The `npx skills add` CLI is not mentioned anywhere in this repo, so it is not a documented route.

The docs describe `gemini skills install`, Gemini CLI's own installer, which takes a Git repository plus the sub-directory holding the skill:

```bash
gemini skills install https://github.com/google-gemini/gemini-cli.git \
  --path .gemini/skills/code-reviewer --consent
```

`--path` is documented as "the sub-directory within a Git repository containing the skill", `--scope` takes `user` or `workspace`, and `--consent` skips the interactive security confirmation. Confirm the path exists in the tree before running it, since the layout here is not the flat `skills/<name>/` shape that most packs use.

The durable route for a Hermes profile is a directory copy out of the clone, taking the 13 workspace skills:

```bash
git clone --depth 1 https://github.com/google-gemini/gemini-cli.git /tmp/gemini-cli
cp -r /tmp/gemini-cli/.gemini/skills/. ~/.hermes/profiles/corpusiq/skills/
```

Two of the listings sit far from that directory, so they need their own copy if they are wanted:

```bash
cp -r /tmp/gemini-cli/packages/core/src/skills/builtin/skill-creator ~/.hermes/profiles/corpusiq/skills/
cp -r /tmp/gemini-cli/tools/gemini-cli-bot/.gemini/skills/critique ~/.hermes/profiles/corpusiq/skills/
```

If the target is Gemini CLI rather than Hermes, the documented discovery tiers are built-in skills, extension skills, user skills in `~/.gemini/skills/` or the `~/.agents/skills/` alias, and workspace skills in `.gemini/skills/` or its `.agents/skills/` alias, with workspace overriding user and the `.agents/` alias winning inside a tier. `/skills list [all] [nodesc]`, `/skills link <path>`, `/skills disable`, `/skills enable` and `/skills reload` manage the set inside a session; `gemini skills list --all` and `gemini skills uninstall` do it from a shell.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| code-reviewer | 9,691 | Reviewing code: local staged or working-tree changes and remote pull requests by ID or URL, focused on correctness, maintainability and adherence to project standards. |
| docs-writer | 3,134 | Writing, reviewing and editing `/docs` and markdown files in the repository, with the skill declared as always-on for documentation tasks. |
| pr-creator | 2,367 | Creating pull requests that follow the repository's own templates and standards, including title and description conventions. |
| docs-changelog | 1,303 | Generating and formatting changelog entries for a release from a version number and raw changelog data, following the project's release procedure. |
| pr-address-comments | 985 | Working through GitHub review comments on the current branch, including comments from the automated review agent, and requires the `gh` CLI. |
| pirate-skill | 877 | Answering in pirate speak, with the "Arrr" convention, as a deliberately trivial demo that ships in the SDK test data rather than as a working skill. |
| github-issue-creator | 848 | Creating GitHub issues across issue types such as bug and feature, using the repository's issue templates and applying the right labels. |
| string-reviewer | 394 | Reviewing user-facing strings and text in the codebase for clarity, usefulness, brevity and house style. |
| async-pr-review | 351 | Kicking off an asynchronous pull request review: a background job runs the project's preflight checks, Gemini-powered test plans and a review with custom prompts, and the status is pollable. |
| review-duplication | 344 | Investigating during a review whether a change duplicates existing functionality, reinvents a wheel or fails to reuse shared utilities and existing best practice. |
| behavioral-evals | 289 | Creating, running, fixing and promoting behavioural evaluations, for verifying agent decision logic, debugging prompt steering and adding workspace regression tests. |
| ci | 253 | Monitoring GitHub Actions workflows fail-fast and reproducing CI failures locally, discovering the run automatically from a branch name. |
| memory | 180 | Maintaining the bot's persistent memory, synchronising with previous sessions through the task ledger and preserving decision logs. Ships in the bot's own skills folder. |
| critique | 152 | Auditing and fixing repository scripts and GitHub Actions workflows for technical robustness and security. Part of the bot's phase set under `tools/gemini-cli-bot/`. |
| metrics | 143 | Analysing time-series repository health metrics, investigating root causes and proposing proactive workflow improvements. Bot phase, not a general analytics skill. |
| prs | 140 | Managing the Git and GitHub pull request lifecycle for the bot: staging changes, generating descriptions and branch management. |
| agent-tui | 137 | Driving terminal UI applications programmatically for testing, automation and inspection; the skill itself warns main agents not to use it directly and to invoke the `tui_tester` subagent instead. |
| tui-tester | 131 | Testing Gemini CLI behaviour and visual output through terminal automation, as the operational manual for interactive verification. |
| skill-creator | 10 | Creating or updating a skill that extends Gemini CLI with specialised knowledge, workflows or tool integrations, shipped as a built-in skill in `packages/core/src/skills/builtin/`. |

All 19 indexed listings appear above; the threshold for this guide is 0 installs, so there is no tail to summarise.

## Why This Matters for Hermes Agents

Review is the workflow most agent teams get wrong first, and this pack is unusually specific about it. `code-reviewer` separates local diff review from remote pull request review, so the agent knows whether it is reading a working tree or fetching a PR. `review-duplication` adds the check that reviewers actually care about and models rarely perform: whether the change reinvents something the repository already has. `string-reviewer` covers the surface that is invisible to tests but visible to every user.

The authoring skills encode the same kind of local knowledge. `pr-creator` and `github-issue-creator` read the repository's own templates rather than inventing a format, which is the difference between a PR that fits a maintainer's triage process and one that has to be rewritten. `docs-changelog` follows a release procedure instead of summarising commits.

The verification cluster is the part worth stealing even if the rest is not installed. `behavioral-evals` is a written methodology for testing agent decision logic, running evals, debugging failures, promoting them and adding workspace regression tests, which is the maturity step most agent setups never reach. `ci` monitors workflow runs and reproduces failures locally. `agent-tui` and `tui-tester` cover interactive terminal behaviour, a layer with no other natural test surface.

The design also demonstrates a skill system done honestly. The docs describe discovery tiers with explicit precedence, a consent prompt that names the directory a skill will gain access to, and progressive disclosure where only names and descriptions load until activation. That is the same contract a Hermes profile wants: small always-on metadata, large on-demand instructions, and a human approval step before a skill gets file access.

## Usage

| You say | What happens |
|---|---|
| "Review this diff before I commit" | `code-reviewer` reads the staged or working-tree changes and reports on correctness, maintainability and project standards. |
| "Review PR 1234" | `code-reviewer` fetches the pull request by ID or URL and reviews it against the same criteria. |
| "Does this duplicate anything we already have" | `review-duplication` searches the codebase for existing functionality, shared utilities and reinventions before the review concludes. |
| "Open a PR for this branch" | `pr-creator` writes the pull request using the repository's template and title conventions. |
| "Work through the review comments on my branch" | `pr-address-comments` reads the comments with the `gh` CLI and works through them one at a time. |
| "Why did CI fail on this branch" | `ci` discovers the workflow run for the branch, reports the failure quickly and reproduces the failing steps locally. |
| "Write a changelog entry for this release" | `docs-changelog` formats the release notes from the version and raw changelog data. |

## Verification

The raw path for the top skill returned HTTP 200 on branch main when this guide was written on 2026-10-31. Note the leading dot in the path:

```bash
curl -sL -o /dev/null -w "%{http_code} code-reviewer\n" \
  https://raw.githubusercontent.com/google-gemini/gemini-cli/main/.gemini/skills/code-reviewer/SKILL.md
```

Expect `200`. After the copy lands, confirm how many directories arrived and that the frontmatter parsed, since these files use several YAML description styles including folded blocks:

```bash
ls /tmp/gemini-cli/.gemini/skills | wc -l
ls ~/.hermes/profiles/corpusiq/skills | grep -Ec 'code-reviewer|pr-creator|tui-tester|behavioral-evals'
head -5 ~/.hermes/profiles/corpusiq/skills/ci/SKILL.md
```

The count should print 13, the filter should match four, and the header should show `name: ci` with an indented multi-line description. Inside Gemini CLI, `gemini skills list --all` or `/skills list` should show the same names once the session reloads.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| code-reviewer | Pass | Pass | Warn |
| pr-address-comments | Pass | Pass | Warn |
| review-duplication | Pass | Pass | Pass |
| metrics | Pass | Pass | Pass |
| skill-creator | Pass | Pass | Pass |

The surface is small: each skill is a `SKILL.md`, and only `ci` ships more than that, with a `scripts/` folder beside it. Nothing installs packages, runs a build or fires a postinstall hook. The two Warns land on the two skills that reach outward, `code-reviewer` fetching pull requests and `pr-address-comments` driving `gh` against the GitHub API, which is the usual shape for a heuristic network-access flag rather than a specific finding.

The real consideration is credentials and scope. `pr-address-comments` requires `gh` and acts on the current branch, so the authenticated GitHub identity matters more than the skill text: use a token scoped to the repository being reviewed. `ci` reads workflow runs through the GitHub API for the same reason. `memory`, `metrics` and `prs` are fragments of an autonomous bot that keeps a task ledger across sessions, and they are the only skills here designed to persist state, so read them before enabling them in an agent that also writes to a repository.

The skill system's own consent step is worth keeping enabled. Gemini CLI shows the skill name, purpose and the directory it will gain access to before activation, and disabling that with `--consent` trades a meaningful check for convenience.

## Limitations

- Snapshot data, verified 2026-10-31: 21,729 combined installs across 19 indexed listings; 108,637 GitHub stars; Apache-2.0; last pushed 2026-11-01T01:14:56Z, a UTC timestamp that lands one day after this snapshot date. Counts drift over time.
- This is a product monorepo, not a skill pack. Of the 25 `SKILL.md` directories, only 19 are indexed listings; the other six are an `antigravity-support` builtin, a `greeter` extension example and the four caretaker-agent skills.
- The skills are written for this repository. `docs-writer` scopes itself to `/docs`, `pr-creator` and `github-issue-creator` use this project's templates, and `ci` assumes this project's workflows, so the guidance transfers as technique rather than as drop-in behaviour.
- Six of the 19 listings live outside `.gemini/skills/`, in `packages/core/src/skills/builtin/`, `packages/sdk/test-data/skills/` and `tools/gemini-cli-bot/.gemini/skills/`. A copy that only takes `.gemini/skills/` gets 13 of them.
- `pirate-skill` is test data, not a working skill, and the four bot skills (`critique`, `memory`, `metrics`, `prs`) are internal phases of an autonomous bot rather than general-purpose helpers.
- Several skills assume tooling outside the repository: `pr-address-comments` and `ci` need `gh` authenticated against GitHub, and `agent-tui` expects a terminal application to drive.

## Related

- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)
- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [Lev Nikolaevich Skills - DevOps and Delivery Setup](/hermes/skills/catalog/levnikolaevich-claude-code-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy only `.gemini/skills/` unless a specific builtin is wanted. That is 13 coherent skills; the remaining six drag in test data and bot internals.
- Read `behavioral-evals` even if nothing else from this repo is installed. It is a written methodology for testing agent decision logic, and it is the least portable and most reusable document in the set.
- Keep `review-duplication` in a review workflow. It is the check that finds reinvented utilities, which is the failure mode code review catches and tests do not.
- If the target is Gemini CLI itself, prefer the `.agents/skills/` alias when sharing with other agents, since the docs state it takes precedence over `.gemini/skills/` within the same tier.
- Do not disable the activation consent prompt with `--consent` on a repo you have not read. The prompt names the directory a skill gains file access to, and that is the only per-skill scope control the system offers.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
