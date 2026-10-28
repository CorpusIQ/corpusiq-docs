---
title: "PStack Skills - Engineering Discipline Suite Setup"
description: "poteto's pstack: 300.3K combined installs. Engineering discipline for coding agents - rigor playbooks, verification, review and parallel subagents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pstack-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "engineering discipline", "code review", "verification"]
---

# PStack - Setup Guide

**Source:** [backnotprop/pstack](https://www.skills.sh/backnotprop/pstack) via skills.sh - 300.3K combined installs across 61 indexed listings; snapshot 2026-10-28 (Oct 28 morning sweep)

**GitHub:** [backnotprop/pstack](https://github.com/backnotprop/pstack) - 3,030 stars, MIT, branch main, `plugin.json` v0.15.34, 61 skill directories (58 under `skills/`, 3 under `automations/benny/skills/`), plus `agents/poteto-agent.md` and `agents/comment-sicko.md`

**Category:** Engineering discipline, review and verification workflow for coding agents

**Quality Tier:** 🟡 Beta - author-maintained mirror of `cursor/plugins/pstack` kept in sync through a two-branch flow, 3,030 GitHub stars, 61 indexed listings against 61 skill directories, three auditor verdicts sampled this sweep with one Snyk warning

pstack is Lauren Tan's (poteto) working skill set, published as a standalone mirror of `cursor/plugins/pstack` so it installs without Cursor. The MIRROR.md file explains the sync model: an `upstream` branch holds Cursor's files exactly, `main` is upstream plus this mirror's edits, and harness-neutral rewrites replace Cursor-specific behaviour so the skills run in any agent that reads `SKILL.md` files. The premise in the README is narrow and worth quoting because it explains the whole design: AI writes too much slop code, so the goal is not to maximize lines written, it is to write less but higher quality code, and throughput without quality is not a goal.

The suite is structured around one router. `poteto-mode` is the default entry point: it matches a request to one of 23 playbooks (investigation, bug fix, perf, hillclimb, runtime forensics, feature, refactoring, prototype, visual parity, eval, babysit, shipping, autonomous run, orchestrate, autopilot, session pickup, multi-phase plan and more), opens a todo list whose first items are that playbook's steps copied verbatim, and then routes to the other skills as the steps fire. Around it sit 24 short principle skills (one rule each, indexed inline so the router reads the index instead of every file), 33 task skills from `unslop` and `interrogate` to the verification family, and two subagent definitions: `poteto-agent`, the wrapper every delegate runs through, and `comment-sicko`, a read-only comment reviewer invoked through `no-comments`.

## Installation

The mirror's own README opens with the skills.sh CLI, which installs from this repository into an agent's skills directory:

```bash
npx skills add backnotprop/pstack
```

The CLI lists every skill for search, then asks which skills and which agents. The upstream README documents the Cursor and Claude Code plugin routes instead:

```bash
/plugin marketplace add cursor/plugins
/plugin install pstack@cursor-plugins
```

Claude Code prefixes plugin commands and agents, so `/poteto-mode` becomes `/pstack:poteto-mode`, and the adapter in `docs/harness/claude-code.md` maps the remaining Cursor names. Claude Code leaves auto-update off for third-party marketplaces, so the install stays on the version you picked until you enable auto-update in the marketplaces tab or run `claude plugin update pstack@cursor-plugins`.

Hermes has no plugin marketplace, so the directory copy is the route that applies. Every skill is a plain `skills/<name>/SKILL.md` folder, which is the format the skills CLI installs anyway:

```bash
git clone --depth 1 https://github.com/backnotprop/pstack.git
cp -R pstack/skills/poteto-mode pstack/skills/unslop pstack/skills/interrogate \
  ~/.hermes/profiles/corpusiq/skills/
```

Several skills carry dependencies the README pins explicitly. `teach` needs `how` and `why`, `architect` needs `arena` and `how`, `blast-radius` needs `arena`, `how`, `why` and `unslop`, and the verification pair needs its maintainer (`create-verification-skill` with `maintain-verification-skill`). `poteto-mode` needs the principle skills and most of the rest, since it routes into all of them. The README calls out 17 skills that call nothing else and work alone, `unslop`, `bro`, `how`, `tdd`, `typescript-best-practices`, `arena`, `swarm`, `interrogate`, `reflect`, `show-me-your-work`, `figure-it-out`, `automate-me`, `correct`, `benchmark-checklist`, `in-your-own-words`, `sharpen` and `statechart`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| unslop | 7,021 | Cleaning up writing before it ships: removes the tells that mark text as machine written, across replies, docs and PR descriptions. |
| how | 6,255 | Walking through how a subsystem works, from the entry point to the data it touches, so a new contributor or an agent can act on it instead of guessing. |
| principle-fix-root-causes | 6,139 | Tracing each symptom back to the first place the system went wrong and fixing it there, so a guard is only accepted when the state it handles is legitimate. |
| why | 6,059 | Recovering why something was built this way: discovers the available MCP servers at run time, then queries source control, the issue tracker, long-form docs, chat, infra observability, error tracking and analytics in parallel. |
| interrogate | 6,020 | Putting a diff in front of several models and asking each to break it from an independent angle, including a strict code-quality lens. |
| technical-writing | 5,943 | Writing or revising docs, RFCs, READMEs, PR descriptions and commit messages against a layered standard built from Diataxis, Google developer style, Simplified Technical English and Global English. |
| arena | 5,917 | Getting N parallel attempts at the same task and taking the best parts of each, instead of committing to the first plausible answer. |
| poteto-mode | 5,910 | The rigour entry point: matches the request to one of 23 playbooks, writes the playbook's steps into a todo list, then routes each step to the skill that owns it. |
| architect | 5,898 | Settling the caller's usage, types and module shape before writing code that crosses a function boundary. |
| blast-radius | 5,773 | Answering what else a small looking change could break, and proving the safe fact by running code rather than asserting it. |
| reflect | 5,770 | Capturing a long task as a skill edit, so the next run of the same work starts from the recipe instead of rediscovering it. |
| figure-it-out | 5,762 | Designing a rigorous, auditable playbook for work that no bundled playbook fits, including long migrations the operator steps away from. |
| no-comments | 5,736 | Stripping comments before review, spawning the read-only Comment Sicko reviewer, fixing the findings it accepts and offering an encoding for each constraint it cannot verify. |
| show-me-your-work | 5,733 | Keeping a reviewable decision trail in a TSV an operator can read, commit or diff after an unattended run. |
| principle-type-system-discipline | 5,732 | Making illegal states unrepresentable: branded primitives, external data parsed at the boundary, exhaustive variants, types derived from the authoritative schema. |
| setup-pstack | 5,723 | Detecting the models you actually have access to and writing the rule that maps each role (code, judgment, the review panels) to one of them. |
| typescript-best-practices | 5,720 | Editing TypeScript with the type-system principle in view, expressed as syntax rather than abstraction. |
| create-verification-skill | 5,705 | Generating a project-local verify skill with a feature map when the project has no scripted way to prove app behavior, for any language or platform. |

The remaining 43 indexed listings range from 9 to 5,689 installs, led by `principle-prove-it-works` (5,689) and `maintain-verification-skill` (5,664), then 21 more principle skills between 4,560 and 5,650, the review and process skills `swarm` (5,650), `tdd` (5,459), `teach` (5,443), `correct` (4,589) and `benchmark-checklist` (4,486), the utility set `recall` (5,581), `make-bot-ui` (5,283), `poteto-help` (4,145), `ketchup` (3,372), `in-your-own-words` (3,018) and `sharpen` (2,671), the two formal verification skills (`maintain-formal-verification-skill` at 1,605 and `create-formal-verification-skill` at 1,530), `ketchup-video` (827) and `statechart` (820), and the three benny automation skills at 9 installs each.

## Why This Matters for Hermes Agents

The common failure in agent work is not a wrong answer, it is an unverified claim. An agent edits a file, reports it works, and nobody has run anything. `principle-prove-it-works` states the countermeasure directly: verify against the real artifact, run the feature, read the actual value, inspect the diff, and treat "it compiles" as a proxy rather than proof. That single rule changes what a Hermes session is allowed to call done.

The parallel story is the other half. `poteto-mode` exists so one agent can be trusted on deep work and several can then run at once, and the skills that make the fleet safe are the delegation principles: `principle-guard-the-context-window` routes bulk to subagents and keeps summaries in the main thread, while `principle-never-block-on-the-human` says proceed, present the result and reserve confirmation for irreversible actions. For cron and unattended runs that is the useful default, and it is stated as a principle rather than left to the operator's judgment.

The subagent wrapper is portable enough to matter here. `poteto-agent` must read `poteto-mode` in full, including its inline principles index, before doing any work, because substituting a general purpose subagent skips that read and drifts. In a harness with no subagent tool the skill says to do each delegated step yourself in order, which is exactly the shape of a small Hermes session.

Verification can also be generated rather than described. `create-verification-skill` builds a project-local verify skill with a feature map for any language or platform, `maintain-verification-skill` repairs that map when the app drifts from it, and the formal pair covers the cases tests cannot reach: races, retries, state machines, parsers and unsafe code. `benchmark-checklist` closes the loop by vetting a measured number (limiter, tuning, errors, repeat runs, end-to-end relevance) before anyone reports it.

## Usage

| You say | What happens |
|---|---|
| "this pr has a subtle bug where the scroll drifts every 750ms even when idle" | poteto-mode matches the bug fix playbook, writes the repro first, traces the drift to its cause and fixes it there, then verifies against the running app before reporting. |
| "why is this feature flag not on yet?" | why discovers the reachable MCP servers, queries source control, the issue tracker and chat in parallel, and returns the decision trail behind the flag rather than a guess. |
| "will this refactor break anything else?" | blast-radius maps the callers and dependents, then proves the safe fact by running code, and reports what it actually checked. |
| "review this diff like different models would, including quality" | interrogate sends the diff to several reviewers, one of them the strict code-quality lens, and returns the findings that survived the challenge. |
| "i'm going to bed, land the stack even if ci flakes" | poteto-mode takes the overnight playbook: independently verify the green stack, then land the contiguous verified run bottom-up through GitHub, without a question back unless an action is irreversible. |
| "this project has no way to prove the app works" | create-verification-skill generates a project-local verify skill with a feature map, then maintain-verification-skill keeps it honest when the app changes. |
| "set pstack up for the models I actually have" | setup-pstack detects the models on the machine, writes the role mapping to a rule every skill reads, and a rerun keeps only the roles you overrode. |

## Verification

Probe the paths you plan to install from. All six URLs below returned 200 when this guide was written, on branch `main`:

```bash
for p in skills/unslop/SKILL.md \
         skills/poteto-mode/SKILL.md \
         skills/interrogate/SKILL.md \
         skills/setup-pstack/SKILL.md \
         skills/create-verification-skill/SKILL.md \
         agents/poteto-agent.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/backnotprop/pstack/main/$p"
done
```

Read three of them before installing:

- https://raw.githubusercontent.com/backnotprop/pstack/main/skills/poteto-mode/SKILL.md
- https://raw.githubusercontent.com/backnotprop/pstack/main/skills/no-comments/SKILL.md
- https://raw.githubusercontent.com/backnotprop/pstack/main/skills/principle-never-block-on-the-human/SKILL.md

`poteto-mode` owns the playbooks and the principles index, `no-comments` carries one of the two community fixes this mirror adds on top of upstream, and the delegation principle governs what a skill will do without asking.

After install, check what landed. The principle set is the cheapest count to confirm if you installed `poteto-mode` with the skills it routes into, and the router's frontmatter should match the name the install index uses:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -c '^principle-'
head -5 ~/.hermes/profiles/corpusiq/skills/poteto-mode/SKILL.md
```

The `head` output should show `name: poteto-mode` and `disable-model-invocation: true`, which means the skill is not auto-invoked from a description match. If the count is not 24, the principle set is incomplete and the router is reading an index it cannot follow.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| unslop | Pass | Pass | Pass |
| how | Pass | Pass | Pass |
| principle-fix-root-causes | Pass | Pass | Pass |
| why | Pass | Pass | Warn |
| interrogate | Pass | Pass | Pass |
| technical-writing | Pass | Pass | Pass |

Five of the six sampled skills pass all three auditors. `why` carries a Snyk warning with code W011, which is published on that skill's security page, so read it before you install that one.

The install surface is markdown only. There is no `package.json` at the repository root, so adding these skills runs no lifecycle hooks. Two `package.json` files do exist inside skill directories, `skills/poteto-mode/scripts/` (alongside `bootstrap.ts`, `check-plan.mjs` and the `orch` and `watch-pr` TypeScript entry points, with a `bun.lock`) and `skills/statechart/scripts/`. Nothing runs them at install time, but the router can call them during a run, so decide deliberately whether those two skills belong in a session that has network and repository write access.

The run-time surface is broader than the file surface. These skills drive git, `gh`, worktrees, subagent spawns and model routing, and the shipping and autonomous run playbooks take a verified stack through to merge rather than stopping at a proposal. `setup-pstack` writes a configuration rule that every other skill reads, so the model mapping it produces governs which model receives judgment calls. In Claude Code that file is `~/.claude/rules/pstack-models.md`, written by `/pstack:setup-pstack`. Treat that rule as configuration with authority rather than as a preference, and review it once after the first setup run.

## Limitations

- Snapshot data, verified 2026-10-28: 300,310 combined installs across 61 indexed listings; 3,030 GitHub stars; MIT; last pushed 2026-10-27. Counts drift over time.
- The repository is a mirror, not the origin. Upstream is `cursor/plugins/pstack`, `main` is upstream plus local edits, and MIRROR.md warns that copying Cursor's files onto `main` erases those edits. Two community fixes are mirror-only, `no-comments` keeping a comment about an outside rule it cannot check and `--base <branch>` for orchestrate scripts on PR stacks that do not start at `main`, so a skill of the same name can behave differently here than in the Cursor plugin.
- Three of the 61 indexed listings are benny automation skills under `automations/benny/skills/`, at 9 installs each. They are not registered as slash skills, they are Cursor automations only, and setup copies the pack into a target repository rather than installing it into an agent.
- 57 of the 58 directories under `skills/` carry `disable-model-invocation: true`, so most of the suite will not fire from a description match; you name the skill you want, or you name `poteto-mode` and let it route. `setup-pstack` is the exception.
- Some referenced material is not bundled. `/deslop`, `control-cli` and `control-ui` ship in the `cursor-team-kit` plugin and `/create-skill` is a Cursor built-in, so the full set needs that plugin alongside pstack.
- The documented routes are skills.sh, Cursor and Claude Code. Hermes has no plugin marketplace, so a directory copy is the only path, and it brings no slash commands, subagent types or model routing with it.

## Related

- [Cursor Plugins Skills - Engineering Discipline Suite Setup](/hermes/skills/catalog/cursor-plugins-skills-setup)
- [Waza - Engineering Habit Skills for Coding Agents](/hermes/skills/catalog/waza-skills-setup)
- [Masseater Skills - Engineering Judgment Suite](/hermes/skills/catalog/masseater-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `poteto-mode` and let it route. The 23 playbooks are the actual product, and asking for one directly ("use the perf playbook") gets you the same steps without the router having to guess.
- Run `setup-pstack` first thing. The default panel is opus 5.5 for judgment and grok for code delegation, and on any other model set the routing rule that gets written is the difference between a run that uses your models well and one that fights them.
- Ask for the todo list before the work. `poteto-mode` copies the playbook's steps in verbatim as the first todo items, so the list is your review surface, and correcting it there is cheaper than correcting the patch.
- Keep `show-me-your-work` on for unattended runs. The TSV decision trail is the only artifact that tells you why an agent chose a path once the session is gone.
- When a number matters, pair `benchmark-checklist` with `principle-explain-the-number`. One vets the measurement, the other finds what limits it, and together they catch the speedup that measured something other than the change.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
