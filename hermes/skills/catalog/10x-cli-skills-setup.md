---
title: "10x CLI Skills - Course Content for Agents"
description: "przeprogramowani/10x-cli on skills.sh: 6.7K combined installs across 3 listings; a CLI that copies 10xDevs course skills and configs into a project."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/10x-cli-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "10xdevs", "course content", "cli"]
---

# 10x CLI Skills - Setup Guide

**Source:** [przeprogramowani/10x-cli](https://www.skills.sh/przeprogramowani/10x-cli) via skills.sh - 6.7K combined installs across 3 indexed listings; first seen 2026-11-07 (Nov 7, 2026 morning sweep)
**GitHub:** 87 stars, no LICENSE file in the repository root, branch `master`, last pushed 2026-10-27, 3 SKILL.md directories (`skills/10x-cli-setup`, `skills/10x-cli-guide`, `.claude/skills/verify-10x-cli`)
**Category:** Skill distribution for agents: fetch, verify and apply course skills, prompts and configs into a workspace with one CLI
**Quality Tier:** 🟡 Yellow - all three sampled skills pass every scanner, but the repository ships no license file and the skills exist to feed a paid course account.

This is a different shape from most repositories in this catalog. The skills are not the product. `@przeprogramowani/10x-cli` is a CLI that pulls 10xDevs course content (skills, prompts, rules, configs) into a project directory, and the two big listings teach an agent to drive that CLI: one sets it up and hands off, the other covers downloading, syncing, changelog reading and troubleshooting. The third listing is a test harness that exercises the CLI against a fake delivery API.

That makes the suite useful in two ways. If you are a 10xDevs learner, the skills turn an agent into a setup assistant that knows the auth flow, the version matrix and the conflict rules. If you are building your own course-delivery tooling, the pair is a readable case study in how to teach an agent a CLI safely: explicit tool targets, project-only writes, dry runs, and an exit code contract the agent is told about.

## Installation

The CLI itself, from the README. Node 20 or newer is the only runtime dependency:

```bash
npx @przeprogramowani/10x-cli auth
npx @przeprogramowani/10x-cli get m1l1
npm install -g @przeprogramowani/10x-cli
```

The first two lines run the CLI without a global install, the third installs it globally for shorter commands, and the README also points at standalone binaries on the GitHub Releases page.

Installing the npm package does not put the helper skills into your agent. The README is explicit about that, and gives two routes. The first is a pinned public source, which needs a full public CLI `master` SHA that contains the helper version you want:

```bash
: "${CLI_SKILLS_REF:?Set the full public CLI master SHA containing the helpers}"
npx --yes skills@1.5.26 add "https://github.com/przeprogramowani/10x-cli/tree/$CLI_SKILLS_REF/skills" --skill 10x-cli-setup --agent claude-code --copy
npx --yes skills@1.5.26 add "https://github.com/przeprogramowani/10x-cli/tree/$CLI_SKILLS_REF/skills" --skill 10x-cli-guide --agent claude-code --copy
```

The second is `10x helpers install`, which is implemented on the branch but not released. The README states plainly that it is not available in 1.21.0 or the 1.22.0 baseline, and that a checkout build may still print 1.22.0 until the release process assigns a version. Check `10x helpers --help` against your actual executable before relying on it. Once a release has it:

```bash
10x helpers install --tool copilot --dry-run
10x helpers install --tool copilot
```

That writes both helper skills, each with its complete `SKILL.md` and `references/compatibility.md`, into `.github/skills/`. The target must be explicit: `claude-code`, `cursor`, `codex`, `devin-desktop`, `factory`, `gemini`, `kiro` or `generic`. Installation is project-only, with no `--global`, no agent auto-detection, no network access and no authentication.

## What It Provides

Two listings clear the 500-install threshold:

| Skill | Installs | Use For |
|---|---|---|
| 10x-cli-setup | 3,266 | Set up or troubleshoot `@przeprogramowani/10x-cli` for a learner: reuse or install a compatible CLI, check auth and course access, choose the project and AI tool, then hand off to the guide skill |
| 10x-cli-guide | 3,209 | Download, use and update course skills: choose an installation channel, inspect course content, switch tool profiles, read 10x-toolkit changelogs and resolve CLI, auth or content conflicts |

The remaining 1 indexed listings range from 193 to 193 installs: verify-10x-cli, a harness that drives the real CLI end to end (login, list, get, sync, changelog, doctor) against a local fake delivery API and captures stdout, stderr, exit codes, PTY screens and screenshots.

The split between the two helpers is worth reading before install, because it explains the handoff. `10x-cli-setup` establishes state: which CLI build is running, whether the account is authenticated, which project directory and AI tool are in play. It explicitly excludes CLI source development and the everyday download and sync work. `10x-cli-guide` owns that second half, including the changelog command and the conflict cases. The README says the setup helper passes project context to the guide rather than doing both jobs.

The third listing sits outside that pair. It lives at `.claude/skills/verify-10x-cli/SKILL.md` rather than under `skills/`, and its job is testing the CLI against a local fake API with isolated config and project directories, which is a pattern worth copying if you publish a CLI that agents drive.

## Why This Matters for Hermes Agents

Most agent skills assume the tool is already installed and authenticated. This pair starts one step earlier, which is where agents usually fail: they run a command from a stale blog post, get an auth error, and then invent an explanation. `10x-cli-setup` is written to check the actual runner first and to distrust a moving README.

The conflict contract is the part worth stealing. `10x helpers install` writes nothing if any existing helper file differs, and exits 1. Identical files are left alone, missing files are created, and no extra local files are ever deleted. An agent-owned install that silently overwrites human edits is a common source of lost work, and this one refuses to do it.

The version discipline is the other good habit. The README distinguishes released CLI behaviour from branch behaviour, tells the agent to check `10x helpers --help` on the executable it actually has, and warns that a checkout build can misreport its own version. That is unusual honesty in a skill that drives a moving CLI.

There is also a clean seam for Hermes: the skills are project copies, so a course workspace and an unrelated repo can carry different helpers without interfering, and the CLI-owned copies update through `sync` while the public copies update through a deliberate new SHA.

## Usage

| You say | What happens |
|---|---|
| "Set up the 10x CLI and log me in" | `10x-cli-setup` checks for an existing compatible CLI, installs one if needed, runs the auth flow and confirms course access |
| "Download module 1 lesson 1 skills into this project" | The guide walks the `10x get` route with an explicit tool, language and `--dry-run` first, then the real write |
| "What changed in the last 10x-toolkit release?" | `10x-cli-guide` runs `10x changelog`, which reads the project's baseline version and reports the release notes since the last sync |
| "My sync is about to overwrite edits I made" | The guide shows the dry-run preview and the skipped-file report, and the single-skill `get` route for taking one update |
| "Put the helper skills in this repo for Copilot" | `10x helpers install --tool copilot` writes both helpers into `.github/skills/`, after a `--dry-run` pass on paths and conflicts |
| "Doctor says my project is on the wrong edition" | `10x-cli-setup` reads the `10x doctor` output, then explains the edition binding and the `--course` flag |
| "Which agent paths does this write to?" | The guide names the per-tool directories and the `10x helpers install --tool` values, including `generic` |

## Verification

Read the setup skill before installing. This path returned HTTP 200 on the repository's `master` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/przeprogramowani/10x-cli/master/skills/10x-cli-setup/SKILL.md | head -30
```

It should open with a quoted description that says it excludes CLI source development, then name the compatibility reference the skill tells the agent to read first. The guide skill is at the same shape, `skills/10x-cli-guide/SKILL.md` (also 200), and both directories carry `references/compatibility.md`.

After install, confirm the helpers landed where your agent looks, for example:

```bash
ls .github/skills
```

You should see `10x-cli-setup` and `10x-cli-guide`, each with a `SKILL.md` and a `references` directory. Then check the capability claim before using the bundled route:

```bash
10x helpers --help
```

If that command is missing, your CLI predates the feature and the pinned public install above is the supported path. For Copilot CLI, the README's next step is `/skills reload`, then `/skills info 10x-cli-setup` and `/skills info 10x-cli-guide` in the same project.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| 10x-cli-setup | Pass | Pass | Pass |
| 10x-cli-guide | Pass | Pass | Pass |
| verify-10x-cli | Pass | Pass | Pass |

All three listings pass all three scanners, and the install surface is small: markdown skills, one compatibility reference each, and a CLI that the README describes down to its exit codes.

Two facts still deserve a look. The repository has no LICENSE file in its root, so the skills arrive without explicit reuse terms even though the npm package is public. And the CLI authenticates a course account, which means the skills handle a login flow and read entitled content; review what the auth flow stores before running it on a machine that also holds production credentials.

The file-writing behaviour is the reassuring part. The bundled installer is project-only, refuses to guess a target, writes nothing when an existing helper differs, and never deletes files it does not own.

## Limitations

- Snapshot data, verified 2026-11-07: 6,668 combined installs across 3 indexed listings; 87 GitHub stars; no license file; last pushed 2026-10-27. Counts drift over time.
- No LICENSE file at the repository root, so redistribution and reuse terms are unstated. Treat the skill text as all rights reserved until the maintainers add one.
- The default branch is `master`, not `main`. Raw content URLs and the pinned install snippet must keep `master`; rewriting them to `main` returns 404.
- `10x helpers install` is unreleased. The README says it is absent from the 1.21.0 and 1.22.0 baselines, so the documented command is not the documented experience yet.
- The install index covers 3 listings, while the course itself ships more skills. The README's own examples fetch `10x-idea-check` and `10x-init` from lesson content, and neither appears in the index with an install count.
- Every skill here assumes a 10xDevs account and entitled course content. Without that account the CLI can install but cannot fetch, and the skills describe a flow you cannot exercise.

## Related

- [Cli Anything Harnesses Setup](/hermes/skills/catalog/cli-anything-harnesses-setup)
- [Bailian CLI - Alibaba Model Studio Agent Skills Setup](/hermes/skills/catalog/modelstudio-cli-setup)
- [Fandhe Agent CLI Skills - Commit and PR Workflows](/hermes/skills/catalog/fandhe-agent-cli-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `10x doctor` before anything else. It reports the auth state, API reachability, local config and which course edition the directory is bound to, which is the context both helpers need.
- Keep course projects separate from work repos. The edition binding follows the directory, and a bound directory silently keeps its own course instead of taking the highest one your account can reach.
- Use `--dry-run` on every `get` and `sync`, then read the skipped-file report. It names edited files and gives the single-skill command that takes just that update.
- Pick one updater per copy. A CLI-owned helper updates through `sync`, a public copy updates through a new pinned SHA, and mixing the two is how you get two half-current copies.
- Pin `skills@1.5.26` in the public route. The README pins it deliberately, and an unpinned `npx skills` can change install semantics under you.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
