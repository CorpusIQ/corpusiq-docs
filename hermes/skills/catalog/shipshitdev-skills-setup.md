---
title: "Ship Shit Dev Skills - 14 Command Routers Setup"
description: "shipshitdev/skills: 14 user-invoked command routers, 27.5K combined installs. Issue, execute, test, QA, review, git and release workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/shipshitdev-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-27"
tags: ["hermes skill", "agent skill", "skill setup", "dev workflow", "code review", "git automation"]
---

# Ship Shit Dev Skills - Setup Guide

**Source:** [shipshitdev/skills](https://www.skills.sh/shipshitdev/skills) via skills.sh - 27.5K combined installs across 150 indexed listings; verified 2026-10-27 (Oct 27 sweep)

**GitHub:** [shipshitdev/skills](https://github.com/shipshitdev/skills) - 38 stars, no license declared (the README and `package.json` both say MIT, but there is no LICENSE file at the repo root), branch `master`, 14 skill directories under `skills/`, each a one-word router with its action playbooks in `references/`

**Category:** Development workflow automation (issues, review, git, QA, release)

**Quality Tier:** 🟡 Beta - 38 GitHub stars, no LICENSE file at the root despite MIT in the README and `package.json`, and 14 in-tree skill directories against 150 indexed listings

This repository is not a pile of topic skills. It is 14 user-invoked commands for the loop a developer runs every day: file an issue, execute it, test, review, open and land a PR, cut a release, deploy, and report on what happened. Every command is one word. Related workflows share a command and take an action as the first argument (`/git pr`, `/issue prd`, `/check grok`), and the playbook for that action lives in the router's `references/` folder, so `/git` stays one line of dispatch on top of nine separate procedures.

Two properties make the design unusual. Every skill sets `disable-model-invocation: true`, so the model never picks one up on its own and you run it by name; routers that compose another skill read that skill's playbook directly from the installed skills directory instead of exposing it to the model. And no skill names a concrete model or effort level: the harness supplies both, which is what makes the same files usable in Claude Code, Codex and Cursor.

The install index and the tree do not line up, and the gap is large. The 150 indexed listings read as a broad topic library (`financial-operations-expert` at 1,710 installs, `youtube-video-analyst` at 1,043), and none of those names has a directory in the current tree or in the repository's commit history. The tree is the 14 routers below. Install by the router names you can read in `skills/`, not by the index entry that brought you here.

## Installation

The README documents the skills.sh CLI. All skills, globally, for the three hosts it targets:

```bash
bunx skills add shipshitdev/skills -g --agent claude-code codex cursor --skill '*' -y
```

One skill:

```bash
bunx skills add shipshitdev/skills -g --skill git -y
```

Always pass `--agent`; `--all` installs into every agent the CLI knows (30+).

No Hermes target is documented, so the direct route is a clone plus a copy. Copy the whole directory, not just `SKILL.md`, because dispatch reads `references/<action>.md` from beside the router:

```bash
git clone --depth 1 https://github.com/shipshitdev/skills.git shipshitdev-skills
mkdir -p ~/.hermes/skills
cp -R shipshitdev-skills/skills/git ~/.hermes/skills/git
cp -R shipshitdev-skills/skills/issue ~/.hermes/skills/issue
```

The README's companion libraries are not vendored here and are optional: pstack comes from the `cursor/plugins` marketplace (`/plugin marketplace add cursor/plugins`, then `/plugin install pstack@cursor-plugins`), and mattpocock/skills installs with `bunx skills add mattpocock/skills -g --agent claude-code -y`. Upstream skills are referenced only as "when installed": `/check adversarial` wants pstack's `interrogate`, `/issue prd` uses mattpocock's `grilling` when present, and both commands work without them.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| financial-operations-expert | 1,710 | Finance operations work: bookkeeping, invoicing and reporting tasks for an operator-facing agent. |
| youtube-video-analyst | 1,043 | Analysis of YouTube videos and channels: what a video says and how it performs. |
| nestjs-testing-expert | 747 | Testing work in a NestJS codebase: suites for services, controllers and modules. |
| agent-browser | 446 | Browser control for an agent: navigating pages, reading state and capturing results. |
| copywriter | 419 | Marketing copy: landing pages, emails, ads and product descriptions. |
| context-optimization | 384 | Reducing what an agent carries in context: prompt structure, retrieval scope and token budget. |
| playwright-e2e-init | 369 | Standing up Playwright end-to-end tests in a repository. |
| design-consistency-auditor | 360 | Auditing a UI for design-system drift: spacing, color, type and component reuse. |
| competitive-intelligence-analyst | 327 | Competitor research: positioning, pricing and feature comparison. |
| brand-name-generator | 316 | Brand naming: candidate generation and shortlist screening. |
| nestjs-queue-architect | 311 | Queue and background-job architecture in a NestJS application. |
| expo-architect | 305 | Expo and React Native application architecture. |
| landing-page-vercel | 269 | Marketing landing pages deployed to Vercel. |
| brand-architect | 264 | Brand foundations: voice, palette, typography and usage rules. |
| funnel-architect | 257 | Conversion funnel design: offer, email steps and checkpoints. |
| idea-validator | 247 | Pressure-testing a product idea before build. |
| html-style | 232 | HTML and CSS styling conventions for pages built without a framework. |
| security-expert | 228 | Security review of an application: auth boundaries, secrets and input handling. |
| memory-systems | 226 | Persistent memory design for an agent: what to store, when to recall, when to expire. |
| aws-infrastructure | 222 | AWS infrastructure work: provisioning and deployment layout. |
| qa-reviewer | 221 | Reviewing finished work against the request it was meant to satisfy. |
| mvp-architect | 209 | Scoping a minimum viable build and the smallest shippable slice. |

Every row above comes from the install index, and none of the 22 names has a directory in the current `skills/` tree or a commit that created one. The Use For column therefore reads the listing name; it is not a summary of a skill file, because no such file exists in this repository. The remaining 128 indexed listings carry fewer than 200 installs each, and the dump runs from `micro-landing-builder` (199) down to `error-handling-expert` (174) before it truncates, so the floor of the tail is not visible.

### The 14 in-tree commands

These are the skills you can actually read and install, taken from the README's command table:

| Command | Actions | What it does |
|---|---|---|
| `/issue` | `feature` (default), `prd`, `plan`, `check`, `publish`, `bug` | Prepares work as GitHub issues: requirements, plan, readiness gate, publishing, bug reports. |
| `/execute` | | Executes a prepared issue and tracks review, CI, merge, and deploy evidence. |
| `/test` | | Runs tests at the right scope and reports failures with evidence. |
| `/qa` | `run` (default), `review` | Interactive localhost QA loop, or a verification pass over finished agent work. |
| `/check` | `code` (default), `grok`, `council`, `week` | Code review, a verified Grok second opinion, a scored multi-provider panel, or the weekly engineering review. |
| `/standup` | `all`, `audit` | Personal git recap, or everyone's merged changes with an optional audit. |
| `/git` | `worktree`, `safety`, `conflicts`, `pr`, `ci`, `babysit`, `modernize`, `merge`, `cleanup` | Local git and GitHub: worktrees, secret guards, conflicts, PRs, CI fixes, PR babysitting, stale-PR updates, merging, cleanup. |
| `/release` | | Cuts a release from a green trunk. |
| `/deploy` | | Runs staging or production deployment workflows. |
| `/board` | `configure`, `sync` | Audits and configures GitHub or Jira boards, or reconciles them with delivery evidence. |
| `/orchestrate` | `status`, `plan`, `run`, `help` | Coordinates existing project sessions and routes their questions. |
| `/browse` | | Drives the project's own Brave session over the DevTools protocol. |
| `/image` | | Generates raster images through the Codex CLI. |
| `/stack` | | Flags outdated Biome, Bun, Next.js, and Tailwind config. |

## Why This Matters for Hermes Agents

Most skill libraries fail on context cost before they fail on quality: 150 flat skills means 150 descriptions competing for the same selection budget on every turn. This repo inverts that. You get 14 entry points, each a dispatch table over `references/` playbooks, so the agent loads one procedure per task and the rest of the suite costs nothing until you ask for it. `disable-model-invocation: true` on every skill makes the inversion explicit: nothing here fires on its own, and a Hermes agent invokes it by name.

The procedures are written as evidence-producing loops rather than instructions. `/execute` implements the prepared plan, escalates gaps instead of inventing decisions, and tracks review, CI, merge and deploy evidence separately. `/standup` traces every bullet to a diff and keeps merged work distinct from deployed work. `/git cleanup` is a read-only plan that proves what is merged before anything is deleted. Those three habits cover most of what goes wrong when an agent reports on work it did not verify.

The gates are placed where the irreversible steps are. `/qa` makes one local commit per fix, never pushes, never opens a PR and never deploys; you publish the branch afterwards with `/git pr`. `/git merge` reviews and confirms before landing. `/release` proves checks on the trunk SHA before it cuts a version. An unattended run therefore stops short of the actions you would want to approve yourself.

Because no skill names a model or an effort level, routing stays with the harness. That matters in Hermes, where model selection is a policy decision rather than something baked into a skill file: the same `/check` works with a local model or an escalated one, and `/check council` can compare them by convening the provider CLIs you already have installed.

Composition is the last piece. A router that needs another skill reads that skill's `SKILL.md` or `references/<action>.md` from the installed skills directory instead of waiting for the Skill tool, which cannot load user-only skills. Copy the directory with its references intact and the composition works; copy the `SKILL.md` alone and dispatch has nothing to read.

## Usage

| You say | What happens |
|---|---|
| "/issue add CSV export to the invoices page" | `/issue` runs feature intake: requirements, plan, readiness gate, then one execution-ready GitHub issue. |
| "/execute #123" | Implements exactly the prepared plan, escalates gaps rather than deciding, and collects review, CI, merge and deploy evidence. |
| "/qa the onboarding flow" | Branches `qa/YYYY-MM-DD` from freshly fetched `origin/<default>` in the current checkout, reproduces each issue you report, fixes it with one local commit each, and re-verifies. It stops and lists uncommitted changes instead of guessing. |
| "/check council #42" | Convenes a panel of every installed provider CLI and writes scored rounds into the PR body. |
| "/git cleanup" | Dry run: proves which branches are merged and deletes nothing. `/git cleanup prune` then removes only that proven set, branches and worktrees. |
| "/check week since <SHA> --fix" | Reports the last 7 days, then repairs confirmed findings in scope through PRs. |
| "/release cut minor" | Proves the gates on the trunk SHA, derives the semver bump and notes, and cuts the release. |

## Verification

Confirm the paths before you copy anything. The branch is `master`, so every raw URL carries it:

```bash
for p in skills/issue/SKILL.md skills/git/SKILL.md skills/qa/SKILL.md skills/check/SKILL.md README.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/shipshitdev/skills/master/$p"
done
```

All five returned 200 when checked on 2026-10-27. The same probes against `main` return 404, which is how the branch was confirmed.

Read the two that touch remotes and the working tree before installing:

- https://raw.githubusercontent.com/shipshitdev/skills/master/skills/git/SKILL.md
- https://raw.githubusercontent.com/shipshitdev/skills/master/skills/qa/SKILL.md

After the copy, each router appears as one folder under your agent's skills directory, and each should carry its `references/` folder beside the `SKILL.md`: `git` has 15 files there, `issue` 8, `board` 7, `check` 5. A clone also lets you run the repo's own validator, `python3 scripts/validate.py`, which checks frontmatter, user-only invocation, links and stray model IDs; `bun run validate` wraps it, and `bun run lint` / `bun run test` cover markdown, Biome, shellcheck and the skill test suites.

## Security

skills.sh verdicts for the Gen Agent Trust Hub, Socket and Snyk auditors were not sampled for this fire, so every cell below reads Not checked. Open each skill's security page on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| financial-operations-expert | Not checked | Not checked | Not checked |
| youtube-video-analyst | Not checked | Not checked | Not checked |
| nestjs-testing-expert | Not checked | Not checked | Not checked |
| agent-browser | Not checked | Not checked | Not checked |
| copywriter | Not checked | Not checked | Not checked |
| context-optimization | Not checked | Not checked | Not checked |
| playwright-e2e-init | Not checked | Not checked | Not checked |
| design-consistency-auditor | Not checked | Not checked | Not checked |
| competitive-intelligence-analyst | Not checked | Not checked | Not checked |
| brand-name-generator | Not checked | Not checked | Not checked |
| nestjs-queue-architect | Not checked | Not checked | Not checked |
| expo-architect | Not checked | Not checked | Not checked |
| landing-page-vercel | Not checked | Not checked | Not checked |
| brand-architect | Not checked | Not checked | Not checked |
| funnel-architect | Not checked | Not checked | Not checked |
| idea-validator | Not checked | Not checked | Not checked |
| html-style | Not checked | Not checked | Not checked |
| security-expert | Not checked | Not checked | Not checked |
| memory-systems | Not checked | Not checked | Not checked |
| aws-infrastructure | Not checked | Not checked | Not checked |
| qa-reviewer | Not checked | Not checked | Not checked |
| mvp-architect | Not checked | Not checked | Not checked |

The first real finding is licensing, not execution. There is no LICENSE file at the repo root and the GitHub API reports no license, while the README and `package.json` both claim MIT. Without the licence text in the tree you have nothing to rely on if your policy depends on it; get the author to add a LICENSE file, or treat the repo as source-available rather than permissive, which is also why the quality tier carries no licence confidence.

The second is scope of authority. `skills/git/SKILL.md` declares `allowed-tools: Bash(git *) Bash(gh *) Bash(jq *) Bash(bun *) Bash(bunx *)`, which is broad: it can rewrite history, delete branches and worktrees, and push to any remote the checkout can reach. The playbook gates the destructive steps (`/git cleanup` plans before it prunes, `/git merge` confirms before landing), but the permission surface is real and should be reviewed against whatever allowlist your Hermes profile runs.

Third, the destructive edges are concentrated in a few actions: `/git merge force` drains a queue, `/git cleanup prune` removes branches and worktrees, `/deploy` targets staging or production, and `/release` tags and publishes. Grant those deliberately. `/qa` is the safe default for autonomous runs by design: local commits only, no push, no PR, no deploy.

Fourth, the optional upstream libraries run code you did not install from this repo. pstack comes from the `cursor/plugins` marketplace and mattpocock/skills from its own repo, so audit them separately if you use `/check adversarial`, `/issue prd` or the retro flows. The router model has one more consequence worth knowing: a composing skill reads whatever playbook sits in your installed skills directory under that name, so a same-named third-party skill in `~/.hermes/skills/` is what actually executes.

## Limitations

- Snapshot data, verified 2026-10-27: 27,455 combined installs across 150 indexed listings; 38 GitHub stars; no license declared; branch master. Counts drift over time.
- The listing count and the directory count measure different things: 150 indexed listings against 14 `SKILL.md` directories in the tree. The two name sets do not overlap, and the repository's history contains no commit that created any of the 22 indexed names in the table above, so the install counts cannot be traced to files you can read and review today.
- No LICENSE file at the repo root. The README and `package.json` both say MIT and the GitHub API reports no license, so cite both when you justify use rather than picking the friendlier one.
- The documented install path covers Claude Code, Codex and Cursor only. There is no documented `hermes-agent` target, so the clone and copy route is the supported one for Hermes, and it is on you to keep `references/` with the router.
- The router design is load-bearing: `SKILL.md` files dispatch into `references/<action>.md` and composing skills read sibling playbooks from disk. Copy a `SKILL.md` alone and the command exists but cannot do its job.
- Several actions depend on tools outside the repo: `gh` and `jq`, Python 3.9+ for `/git babysit` and `/git cleanup`, a locally runnable application for `/qa run`, and provider CLIs for `/check council`. The repo runs Bun only, so its own lint and test scripts assume `bun` and `python3`.

## Related

- [Agent Browser - Vercel Labs CLI for AI Agents Setup](/hermes/skills/catalog/agent-browser-setup)
- [Superpowers - Agentic Skills Framework Setup](/hermes/skills/catalog/superpowers-setup)
- [OpenSpec Skills - Spec-Driven Development Suite Setup](/hermes/skills/catalog/fission-openspec-skills-setup)
- [Ultracite - Zero-Config Lint Preset Setup](/hermes/skills/catalog/ultracite-skills-setup)

## Pro Tips

- Start with `/issue`, `/execute` and `/git pr`. Those three are the spine of the repo, and the remaining eleven routers make more sense once you have watched one feature go from rough request to merged PR.
- Bare commands print their action table rather than guessing. `/git`, `/board` and `/orchestrate help` are the cheap way to see what is available without spending a turn on a wrong action.
- Copy the whole skill directory. `git` carries 15 files under `references/`, and dispatch breaks silently if only the `SKILL.md` lands in `~/.hermes/skills/`.
- Run `python3 scripts/validate.py` in the clone before you trust a copy. It enforces the one-word name, the `disable-model-invocation: true` flag and the absence of model IDs, which is exactly the property set that keeps the suite portable across hosts.
- Keep `/qa` and `/git merge` in separate turns. `/qa` leaves one local commit per fix on a dated branch and never pushes; `/git merge` is where you confirm and land. Mixing them in one instruction is how an agent ends up pushing from inside a QA loop.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
