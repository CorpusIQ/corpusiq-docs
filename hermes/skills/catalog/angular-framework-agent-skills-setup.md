---
title: "Angular Framework Skills - Official Repo Agent Guides"
description: "angular/angular on skills.sh: 9.7K combined installs; the framework repo's own agent skills for Angular code, signals, forms, compiler and PR review."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/angular-framework-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "angular", "frontend", "code review"]
---

# Angular Framework Skills - Setup Guide

**Source:** [angular/angular](https://www.skills.sh/angular/angular) via skills.sh - 9,733 combined installs across 7 indexed listings; first seen 2026-11-08 (Nov 8 2026 morning sweep)
**GitHub:** 101,466 stars, MIT, last pushed 2026-11-07, 7 SKILL.md directories in two trees: five under .agent/skills and two under skills/dev-skills
**Category:** Angular for agents: framework conventions, signals and forms references, compiler and CLI guidance plus PR review standards
**Quality Tier:** 🟢 Recommended - MIT licence, 101,466 stars, the Angular team's own skill files, and a Pass on every scanner row that was sampled.

Most skills arrive as a small standalone repository. This one is the Angular framework itself, and the skills inside it were written for two different jobs that are easy to confuse. The five skills under `.agent/skills/` are for changing the framework: the core runtime, the compiler, the docs site, and pull requests against angular/angular. The two under `skills/dev-skills/` are for building applications with Angular.

That split is the whole story of this pack. If you install it expecting app-building guidance you get `angular-developer`, a 147-line SKILL.md with 43 reference files behind it covering components, signals, `linkedSignal`, `resource`, `httpResource`, signal forms, dependency injection, routing, SSR and hydration, ARIA, animations, testing and CLI tooling. If you install it because you work on the framework, the other five are the ones that matter, and four of them are written against paths that only exist inside the Angular source tree.

The strongest piece is the instruction set rather than the reference dump. `angular-developer` opens with three rules: analyse the project's Angular version before advising, because available features differ sharply between versions; scaffold through the Angular CLI rather than hand-writing files; and run `ng build` after generating code, then fix the errors before proceeding. `ng new` gets an explicit three-step decision tree: a named version goes straight to `npx @angular/cli@<version> new`, otherwise `ng version` decides between the local install and `npx @angular/cli@latest new`.

## Installation

There is no `npx skills` path for the framework repository itself, and the repository never claims one. The top-level `README.md` covers documentation, contributing and the npm packages, with no skills section at all. The only install command the repo documents is in `skills/dev-skills/README.md`, and it points at a separate mirror repository, `angular/skills`, which carries just the two application skills:

```bash
npx skills add https://github.com/angular/skills
```

For the seven indexed skills in the framework repo, the documented route is to open the files where they live and point your harness at them, or copy the directories into the skills folder your harness reads:

```bash
git clone --depth 1 https://github.com/angular/angular ~/src/angular

# application-facing skills
ls ~/src/angular/skills/dev-skills/angular-developer/SKILL.md
ls ~/src/angular/skills/dev-skills/angular-new-app/SKILL.md

# framework-facing skills
ls ~/src/angular/.agent/skills/reference-core/SKILL.md
ls ~/src/angular/.agent/skills/reference-signal-forms/SKILL.md
ls ~/src/angular/.agent/skills/reference-compiler-cli/SKILL.md
ls ~/src/angular/.agent/skills/adev-writing-guide/SKILL.md
ls ~/src/angular/.agent/skills/pr_review/SKILL.md
```

A shallow clone is enough for the markdown, but `angular-developer` links 43 files under its own `references/` directory, so copy the whole skill directory rather than the SKILL.md alone.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| angular-developer | 4,836 | Writing Angular application code: components, signals, forms, DI, routing, SSR, ARIA, testing and CLI scaffolding, backed by 43 reference files |
| reference-core | 991 | Mental model of `packages/core`: Ivy and Render3 instructions, DI, change detection, signals and Zone.js integration |
| reference-signal-forms | 976 | The `packages/forms/signals` model: a writable signal as the source of truth, a proxy `FieldTree`, lazily resolved `FieldNode`s |
| adev-writing-guide | 914 | Writing Angular docs: Google technical writing standards plus the markdown extensions and components used in `adev/src/content` |
| reference-compiler-cli | 911 | `ngtsc` architecture: the wrapper around `tsc`, the trait state machine, template type checking and AOT |
| angular-new-app | 578 | Scaffolding a new app: checks for the CLI on PATH first, then drives `ng new` and the modern project layout |
| PR Review | 527 | Reviewing pull requests against angular/angular, with package-specific rules and five `gh` helper scripts |

The threshold for this pack is zero, so every indexed row is in the table above. There is no tail: 0 rows fall below the threshold.

The two reference skills that name a package directory in their description (`reference-core`, `reference-compiler-cli`) say "you MUST use this skill any time you plan to work with code in" that package. That is a path-scoped trigger, and it is the most portable idea in the pack: the description carries the activation condition so the harness does not have to guess from the user's phrasing.

`PR Review` is worth reading even if you never review Angular code. It insists on a full review of the entire pull request rather than only the area the user pointed at, tells the agent not to run tests locally because CI already does, and routes package-specific rules through a `reference/` directory (for example `reference/router.md`, which flags any change to navigation timing as near-certainly breaking). The five shell scripts next to it wrap `gh`: `determine_review_type.sh`, `get_pr_comments.sh`, `post_inline_comment.sh`, `submit_pr_review.sh` and `reply_pr_comment.sh`.

## Why This Matters for Hermes Agents

Three things here transfer to any agent setup, Angular or not.

First, version guardrails. `angular-developer` refuses to give advice before it knows which Angular version the project runs, because the same question has different answers across v17, v20 and v22. An agent that skips that step answers from its training data and produces code for a version the user does not have. The rule costs one command and removes a whole class of wrong answers.

Second, verification built into the skill. "Once you finish generating code, run `ng build`" with an instruction to fix failures is a skill telling the agent how to check its own work, not just what to write. Skills that stop at style guidance leave the check to the human.

Third, scoping by path. The four framework skills declare their scope as a directory (`packages/core`, `packages/compiler-cli`, `packages/forms/signals`, `adev/src/content`). Hermes loads skills per task, so a repo-scoped skill that says exactly where it applies is easy to gate and easy to trust. The same pattern works for any codebase with a stable layout.

The limits show up as soon as you leave the repository. These are contributor skills: they assume the Angular monorepo, its build system and its conventions. Copied into an unrelated project, `reference-core` has nothing to describe.

## Usage

| You say | What happens |
|---|---|
| "Add a signal-based input to this component" | `angular-developer` reads `references/inputs.md` and follows the v20+ intent-over-role naming rules |
| "Create a new Angular app called billing" | The `ng new` decision tree runs: explicit version to `npx`, else `ng version`, else `npx @angular/cli@latest new` |
| "Why is this form value not updating?" | Signal forms guidance: the writable signal is the source of truth, the field tree is a projection over it |
| "Review PR 61234" | `PR Review` fetches comments with `gh`, then applies the whole-PR rule plus any package-specific reference |
| "Explain how change detection works here" | `reference-core` walks the Ivy instruction pipeline and the signals-to-zone bridge |
| "Write the docs page for this feature" | `adev-writing-guide` applies the Google writing standards and the adev markdown components |
| "How does the compiler handle this decorator?" | `reference-compiler-cli` describes the trait states: pending, analysed, resolved |

## Verification

Read the two ends of the pack before installing. Both paths returned 200 on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/angular/angular/main/skills/dev-skills/angular-developer/SKILL.md | head -40
curl -fsSL https://raw.githubusercontent.com/angular/angular/main/.agent/skills/reference-core/SKILL.md | head -40
```

The first should open with frontmatter naming `angular-developer`, a `license: MIT` line, `metadata.author: Copyright 2026 Google LLC`, `version: '1.0'`, and a description that lists the trigger surface: reactivity, queries, forms, DI, routing, SSR, ARIA, styling, testing, naming and CLI. The second should open with `name: reference-core` and a description that scopes it to `packages/core` and says you must use it before working there.

To confirm what the documented mirror actually ships, ask GitHub for the tree rather than trusting the README:

```bash
curl -s "https://api.github.com/repos/angular/skills/git/trees/main?recursive=1" \
  | grep -c "SKILL.md"
```

That returned 2 on 2026-11-08: `angular-developer/SKILL.md` and `angular-new-app/SKILL.md`. It is the mirror, not the framework repo, so five of the seven indexed skills are not in it.

After copying into a harness, check that the reference files travelled with the skill (adjust the path to wherever your harness reads skills):

```bash
ls ~/.claude/skills/angular-developer/references | wc -l
```

The count should be 43. A SKILL.md without its references is a skill that will cite files it cannot read.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-08) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| angular-developer | Pass | Pass | Pass |
| reference-core | Pass | Pass | Pass |
| adev-writing-guide | Pass | Pass | Pass |
| angular-new-app | Pass | Pass | Pass |
| PR Review | ? | ? | ? |

Four of the five sampled skills pass all three scanners, which is what you would expect from text files authored by the framework team and reviewed in public. `PR Review` is unrated on all three, and it is the only skill in the pack that ships executables: five bash scripts that call the GitHub CLI. Read them before running them. They act on the pull request you name and use your `gh` credentials, so the blast radius is your GitHub token's permissions, not your filesystem.

Two skills in the table have no verdict row at all: `reference-signal-forms` and `reference-compiler-cli` were not sampled. That is a coverage gap in the scanner run, not a failure, but it means 2 of the 7 indexed skills carry no security signal.

Licence is unambiguous: the repository root has a LICENSE file, the MIT License, Copyright 2010-2026 Google LLC. The skill frontmatter repeats it for the two application skills (`license: MIT`). Nothing here executes as part of the reasoning path; the risk surface is the `gh` scripts and whatever your harness does with a skill that instructs it to edit a large TypeScript monorepo.

## Limitations

- Snapshot data, verified 2026-11-08: 9,733 combined installs across 7 indexed listings; 101,466 GitHub stars; MIT; last pushed 2026-11-07. Counts drift.
- No documented `npx skills` path for angular/angular. The only install command in the repo targets the `angular/skills` mirror and delivers 2 skills, not 7. Anything else is your own clone-and-copy step.
- Indexed listings and SKILL.md directories match at 7, so there is no drift in count, but they sit in two trees with different audiences: five contributor skills under `.agent/skills/`, two application skills under `skills/dev-skills/`.
- The `.agent/skills` set assumes the Angular source tree. `reference-core`, `reference-compiler-cli` and `reference-signal-forms` describe `packages/` paths, `adev-writing-guide` describes `adev/src/content`, and `PR Review` assumes a `gh`-authenticated clone of angular/angular.
- `angular-developer` is only useful with its `references/` directory. A copy of the SKILL.md alone leaves 43 dangling links.
- `PR Review` requires the GitHub CLI installed and authenticated. Its five scripts are bash and were read, not executed, during this review.
- Version claims inside the skills are the maintainers' and were not re-checked against angular.dev: the text treats Signal Forms as stable in v22 and names v20+ for naming conventions.
- Not verified: that skills.sh can install angular/angular directly. The listing page indexes it, but no command in the repository targets that repo, so this guide does not ship one.
- Two indexed skills (`reference-signal-forms`, `reference-compiler-cli`) have no scanner verdicts, and `PR Review` is unrated on all three scanners.

## Related

- [Angular Skills - Framework Development Setup](/hermes/skills/catalog/angular-skills-setup)
- [Syncfusion Angular UI Skills - Vendor Component Pack](/hermes/skills/catalog/syncfusion-angular-ui-skills-setup)
- [Feature-Sliced Design Skill - Frontend Architecture Setup](/hermes/skills/catalog/feature-sliced-design-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Point your harness at `.agent/skills/` with a path filter rather than a keyword. The descriptions already name the package directory, so activation can be deterministic instead of inferred.
- If you only build Angular apps, take `angular-developer` and `angular-new-app` and skip the rest. The five contributor skills describe internals that do not exist in your project.
- Steal the build-check rule for your own skills: generate, then `ng build`, then fix. It converts a skill from advice into a loop with a stopping condition.
- Read `reference/router.md` before touching router code. Timing changes to navigations, resolvers and guards are treated as breaking, and that rule is exactly the kind of thing an agent gets wrong from first principles.
- Keep the skills pinned to the framework commit you build against. They describe `packages/core` internals that change often, and a stale mental model is worse than none.
- The mirror repository is the cheap update channel for the two application skills: `git pull` there and re-run the install, instead of re-cloning the framework.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
