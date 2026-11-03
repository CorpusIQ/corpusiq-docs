---
title: "JS Mastery Skills - Agentic Development Workflow"
description: "jsmastery-pro/skills: 52.9K combined installs. Nine MIT skills that carry a change from scope to shipped, verified, documented code."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/jsmastery-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "agentic development", "code review", "testing", "workflow"]
---

# JS Mastery Skills - Setup Guide

**Source:** [jsmastery-pro/skills](https://www.skills.sh/jsmastery-pro/skills) via skills.sh - 52.9K combined installs across 13 indexed listings; first documented 2026-11-03 (nightly sweep)

**GitHub:** [jsmastery-pro/skills](https://github.com/jsmastery-pro/skills) - 1,595 stars, MIT, branch main, last pushed 2026-08-09; nine skill directories under `skills/` (architect, audit, check, debug, develop, document, scope, sync, test), each with a `SKILL.md` plus its own support files, 1,189 lines of `SKILL.md` in total

**Category:** Phase based engineering workflow for coding agents: scope, audit, architect, develop, check, test, document, sync, debug

**Quality Tier:** 🟡 Yellow - Snyk warns on the sampled `architect` listing while Gen Agent Trust Hub and Socket pass all three sampled skills, and the repository does ship a LICENSE file (MIT)

JS Mastery Skills is published by JavaScript Mastery, the education brand behind the JS Mastery YouTube channel and course catalogue. The package manifest describes it as "a phase based engineering workflow as Agent Skills" that takes a change from a vague idea to shipped, verified, documented code for any AI coding agent, and the repository is MIT licensed at version 2.0.0.

The design bet is that state belongs in files, not in a chat session. A scope document, a build spec per load bearing decision, `AGENTS.md` context files, and a test suite carry the work, so a new session can pick up where the last one stopped and a team can share one workflow. Nine skills map to the phases, and the README is explicit that you run only the ones a change needs, in any order: `/scope` seeds what to build, `/audit` writes the context files, `/architect` decides and records, `/develop` builds, `/check` verifies and reviews, `/test` writes tests, `/document` writes the prose, `/sync` reconciles knowledge, and `/debug` handles anything that breaks.

## Installation

The README documents the vercel-labs `npx skills` installer in two forms, one per client family:

```bash
# Claude Code (installs into .claude/skills, then restart Claude Code)
npx skills@latest add jsmastery-pro/skills -a claude-code

# Generic .agents/skills, read by Codex and other agents
npx skills@latest add jsmastery-pro/skills
```

The skills.sh listing page carries the same installer without the pinned version, which is the form to copy if you want the current CLI rather than the one the README was written against:

```bash
npx skills add jsmastery-pro/skills
```

For a Hermes profile, install from a clone and copy the whole skill directory rather than only `SKILL.md`. Several skills ship support files that their instructions read at run time: `develop` carries `flow/`, `agents/`, `ui/`, `checklist.md`, `logical-guide.md` and `ui-guide.md`, while `check` carries `modes/`, `agents/`, `review-agent-prompt.md` and `review-guide.md`:

```bash
git clone --depth 1 https://github.com/jsmastery-pro/skills.git /tmp/jsmastery-skills
cp -r /tmp/jsmastery-skills/skills/develop ~/.hermes/profiles/corpusiq/skills/
cp -r /tmp/jsmastery-skills/skills/check ~/.hermes/profiles/corpusiq/skills/
```

Restart the agent afterwards, because most clients read the skill directory once at session start. The installer writes to `.agents/skills` for generic clients and `.claude/skills` for Claude Code, so a copy aimed at a Hermes profile has to name that profile's skills directory instead.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| architect | 7,125 | A load bearing technical decision that is still unmade: choosing between approaches, designing a feature or page, picking a stack. Asks, recommends, writes a build spec to docs/specs/ and owns every spec file. |
| develop | 4,701 | Building a feature, UI or backend from an approved design, page, component, API or data slice, reading the spec plus AGENTS.md, and stopping to route to /architect when a decision is owed. |
| debug | 4,654 | Root cause work on a bug: a test failing for an unclear reason, a /check verify failure, or wrong behavior. Runs reproduce, localize, hypothesize, test, fix, verify, then hands a regression test to /test. |
| check | 4,625 | Confirming a change before merge. /check verify drives the real app against every acceptance criterion; /check review runs a senior review on a fresh model that did not write the code. Writes to docs/reviews/ and never edits code. |
| scope | 4,624 | Turning a product idea into a living, coarse scope in docs/scope/: plan a new product, plan the next slice, enroll one named feature, or reconcile after shipping with no argument. |
| audit | 4,613 | Bootstrapping AI context on a greenfield project, an undocumented codebase, or one area such as src/auth: writes tool agnostic AGENTS.md files plus thin CLAUDE.md pointers and never overwrites curated content. |
| document | 4,607 | Human facing prose about a change: a PR body, changelog, release note or postmortem, drafted from the real commits and diff. Writes no code, tests or specs. |
| sync | 4,597 | The last step around merge: update root and nested AGENTS.md, reconcile the scope from repo evidence, and flag specs the change made stale, with surgical line level edits only. |
| test | 4,551 | A test suite for code just built or changed: targets uncommitted changes, reads test preferences.json for the framework, and picks happy path, edge case, error state or accessibility per file. |
| review | 2,267 | Indexed listing that carries the architect description; there is no review directory in the repository tree, so treat it as an alias rather than a separate phase. |
| remember | 2,256 | Indexed listing that carries the architect description; no remember directory exists in the tree, so the durable knowledge work lives in /sync instead. |
| recover | 2,245 | Indexed listing that carries the architect description; no recover directory exists in the tree. Use /debug plus a fresh /scope reconciliation for recovery work. |
| imprint | 2,028 | Indexed listing that carries the architect description; no imprint directory exists in the tree. |

No indexed listings fall below the threshold; all 13 appear above.

The substance is in the nine real directories. `develop` is the largest workflow surface at 144 lines of `SKILL.md` plus a `flow/` tree, and it is the skill that enforces the gate back to `/architect` when a spec does not record a decision. `test` is the longest single file at 216 lines, and `architect` at 206 lines carries the spec template (`spec-template.md`) that every later phase reads. The README also names a workflow depth chosen at the end of `/scope`: Prototype runs only `/develop` with a self check, Alpha adds `/check verify`, Beta adds `/test`, and GA adds a fresh-model `/check review` and `/document`. Depth is described as a suggested checking tail, not a lock.

## Why This Matters for Hermes Agents

Most agent workflows lose their state at the end of a session, which makes long changes expensive to resume and impossible to hand to a second agent. This suite moves the state into the repository: `docs/scope/`, `docs/specs/`, `AGENTS.md`, and tests. An agent that starts cold can read the scope and the spec and continue, and a reviewer agent can be handed the same files.

The division of labour is unusually strict for a skill pack, and that is the useful part. `/check review` is specified to run on a fresh model that did not write the code, which is the cheapest available substitute for an independent reviewer. `/document` is forbidden from writing code, tests or specs. `/sync` is limited to adding lines and rewriting single lines it owns, never a whole section and never curated prose. `/audit` adds only what is missing to `AGENTS.md`. Those constraints are what stop a workflow pack from turning into an agent that rewrites everything it touches.

The tool agnostic choice matters for Hermes. Context lives in `AGENTS.md` with thin `CLAUDE.md` pointers, so the same repository works for a Hermes session, a Codex run or a Claude Code run without duplicating instructions, and the README states that monorepo work scopes to the target workspace with its own context, scope, stack and commands.

## Usage

| You say | What happens |
|---|---|
| "Scope this product idea into something we can build" | `/scope` writes a coarse living scope into `docs/scope/`, asks for a workflow depth, and queues the first slice. |
| "Seed AGENTS.md from this codebase" | `/audit` reads the real project, writes tool agnostic `AGENTS.md` files plus thin `CLAUDE.md` pointers, and adds only what is missing. |
| "Should we use Postgres or SQLite for this?" | `/architect` asks the load bearing questions, recommends an answer, and records it as a build spec in `docs/specs/` so `/develop` can read it later. |
| "Build the settings page from the spec" | `/develop` reads the spec and `AGENTS.md`, builds, advances the scope, and stops to route back to `/architect` if something undecided blocks it. |
| "Prove this change actually works before I merge" | `/check verify` drives the real app against every acceptance criterion; `/check review` then reads the code on a second model and writes findings to `docs/reviews/`. |
| "This test fails and I do not know why" | `/debug` runs the reproduce, localize, hypothesize, test, fix, verify loop, makes the minimal fix, and hands a regression test to `/test`. |
| "Write the PR description and changelog for this branch" | `/document` drafts from the real commits and diff into the right files, without touching code, tests or specs. |

## Verification

The raw path below returned 200 on branch main on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/jsmastery-pro/skills/main/skills/architect/SKILL.md
```

After a clone, confirm the tree really holds nine skills and that the support files came with them:

```bash
git clone --depth 1 https://github.com/jsmastery-pro/skills.git /tmp/jsmastery-skills
ls -d /tmp/jsmastery-skills/skills/*/ | wc -l
wc -l /tmp/jsmastery-skills/skills/*/SKILL.md | tail -1
head -3 /tmp/jsmastery-skills/skills/develop/SKILL.md
ls /tmp/jsmastery-skills/skills/develop
```

The directory count should print 9, the line count should print 1189 in total, and `head` should show `name: develop` followed by the description the runtime routes on. The `develop` listing should include `flow`, `agents`, `ui`, `checklist.md`, `logical-guide.md` and `ui-guide.md`; if only `SKILL.md` is present, the copy was too narrow. On the installed copy:

```bash
ls ~/.hermes/profiles/corpusiq/skills/develop
grep -n 'docs/specs' ~/.hermes/profiles/corpusiq/skills/architect/SKILL.md | head -3
```

The grep should show the spec path the skill writes to, which is the file `/develop` reads in the next phase.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| architect | Pass | Pass | Warn |
| develop | Pass | Pass | Pass |
| debug | Pass | Pass | Pass |

The single warn is on `architect`, which is also the skill with the broadest write surface in the set: it owns every file in `docs/specs/`. Every skill in the pack declares `allowed-tools` in its frontmatter, and `architect` lists Bash, Read, Grep, Glob, Write, Edit, Agent and AskUserQuestion, so an agent running it can write files and spawn a subagent by design. Read that list before installing into a profile where the working directory holds anything you would not want edited.

The repository is Markdown plus two development scripts. `package.json` declares `check` as `node scripts/check-portability.mjs` and `tokens` as `node scripts/analyze-token-usage.mjs`, and both run only when a human invokes npm, not when a skill loads. There is no hook, no postinstall step and no runtime dependency beyond Node 18 or newer for those scripts. The skills do instruct the agent to write into the project (`docs/scope/`, `docs/specs/`, `docs/reviews/`, `AGENTS.md`), so the practical control is the repository boundary, not the skill text.

## Limitations

- Snapshot data, verified 2026-11-03: 52,893 combined installs across 13 indexed listings; 1,595 GitHub stars; MIT; last pushed 2026-08-09. Counts drift over time.
- The index and the tree disagree on scope. skills.sh lists 13 names, the repository has nine directories, and the four extras (`review`, `remember`, `recover`, `imprint`) reuse the `architect` description verbatim, so their installs are real but their instructions are not separately authored in this repo.
- The README states that hardening, the systems level failure mode analysis phase, is temporarily removed and will return as a system design specialization. Do not plan a workflow around it.
- Every skill writes into the project (`docs/specs/`, `docs/scope/`, `docs/reviews/`, `AGENTS.md`) and `/test` reads a `test-preferences.json` at the project root to pick a framework. A repository with its own conventions will need those paths agreed before the first run.
- `architect` carries the only sampled Snyk warn and the widest tool allowlist in the pack, including Bash, Write, Edit and Agent. The warn reason is not visible in the pack, so check the security page on skills.sh before production use.

## Related

- [codebase-design - Deep Module Design Vocabulary Setup](/hermes/skills/catalog/codebase-design-setup)
- [shadcn Improve - Codebase Audit to Plan Setup](/hermes/skills/catalog/shadcn-improve-setup)
- [Qodo Skills - Code Review and Standards Suite](/hermes/skills/catalog/qodo-skills-setup)
- [Fallow Skills - Codebase Intelligence for TS and JS Setup](/hermes/skills/catalog/fallow-rs-fallow-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `/scope` and `/audit` on any existing repository. Every later skill reads the context files `/audit` writes, so skipping it makes `/develop` guess at conventions.
- Install `architect`, `develop` and `check` first. That trio is the feature loop, and it is small enough to keep resident while you decide whether the rest earns its context.
- Pick the workflow depth per feature rather than per project. The README treats Prototype through GA as a suggested checking tail, so throwaway work does not need a fresh-model review.
- Read `docs/specs/` before a `/develop` run. The gate back to `/architect` fires when a decision is unrecorded, and a missing spec is the most common reason a build stops early.
- Copy skill directories whole. `develop` and `check` read files beside their `SKILL.md`, and a lone `SKILL.md` copy fails at the first phase that needs a guide.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
