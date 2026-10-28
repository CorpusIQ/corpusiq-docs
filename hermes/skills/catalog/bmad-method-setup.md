---
title: "BMad Method Skills - Agile AI Development Suite Setup"
description: "BMad Method's agile delivery suite: 383.8K combined installs. Briefs, PRDs, architecture, tickets, build, review and retro skills for coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/bmad-method-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "agile delivery", "product planning", "code review"]
---

# BMad Method - Setup Guide

**Source:** [bmad-code-org/bmad-method](https://www.skills.sh/bmad-code-org/bmad-method) via skills.sh - 383.8K combined installs across 81 indexed listings; first seen 2026-10-28 (Oct 28 morning sweep)

**GitHub:** [bmad-code-org/bmad-method](https://github.com/bmad-code-org/bmad-method) - 54,667 stars, MIT, branch main, 31 directories under `skills/` (28 runnable skills plus the `bmod-method`, `bmod-core-tools` and `bmod-toolsmith` module records) and one nested sample skill, for 32 `SKILL.md` files in the clone; no `package.json`, so an install runs no npm lifecycle hooks

**Category:** Agile AI-driven development: planning, delivery, review and retrospective workflows

**Quality Tier:** 🟡 Beta - maintained by the BMad Code organisation, 54,667 GitHub stars, MIT, 81 indexed listings against 31 directories on main, security verdicts sampled for six skills with three Warn cells

BMad Method is an agile process for AI-driven development, which the README calls Agile Ai Driven Development: turn an idea or a change request into working software while keeping the decisions explicit. The process sizes itself to the work, so a small change goes straight to build and a larger one earns planning first, and the artifacts it produces (brief, PRD, architecture spine, ticket tree) stay in the repository as context for the next session rather than living in a chat. It is not a code generator. A large part of the suite is planning and review: briefs, PRDs, UX spines, architecture documents, epics and stories, walkthroughs, retrospectives, plus six persona agents (Mary the analyst, John the PM, Winston the architect, Sally the UX designer, Amelia the developer, Sofia the product owner) that can be addressed by name or convened together in party mode.

The suite ships on two lines. The stable v6.12 release is installed by the npm installer and frozen aside from bug fixes, while the skills on this branch are the V7 preview alpha, which the README says changes often and expects breaking changes from. Both routes want `uv` for setup and for the Python scripts the skills call. The v6.11.0 changelog entry explains how the current catalog got its shape: core dropped from fourteen skills to eight, six older review and editorial skills became `bmad-review` lenses (`adversarial`, `edge-case-hunter`, `verification-gap`, `structure`, `prose`), the research trio consolidated into `bmad-deep-recon`, and the preview branch has since handed `bmad-spec`, `bmad-ticket` and `bmad-correct-course` to Sofia the product owner.

## Installation

The README leads with the skills.sh CLI for the V7 preview. Run it in the project you want BMad to work on:

```bash
npx skills add bmad-code-org/BMAD-METHOD --skill '*'
```

`--skill '*'` installs the full method and asks which coding tools to install to. To pick skills instead, run the command without `--skill '*'` and include `bmad` for setup and help, plus the module record for each module you take skills from: `bmod-method` and `bmod-core-tools`.

The stable line is a different installer, with Node.js 20.12+ and Python 3.10+:

```bash
npx bmad-method install
```

Claude Code users add the plugin marketplace from inside the tool, and Codex users add it from a terminal:

```text
/plugin marketplace add bmad-code-org/bmad-plugins
```

```bash
codex plugin marketplace add bmad-code-org/bmad-plugins
```

For either marketplace, install `bmad-method` for the delivery workflows and `bmad-core-tools` for the standalone skills, including the `bmad` hub.

Whatever the install route, the next step happens inside the project. Open your coding tool there, ask the `bmad` skill to run `bmad setup`, then invoke `bmad-build` with what you want to change. Setup is also the updater: it runs `npx skills update`, refreshes the project, and cleans up renamed and removed skills. Ask for `bmad status` to see versions and what to run next.

Hermes is not one of the install targets the CLI offers, so on this host the tree is the install source. Clone the repository and copy the skill directories you want:

```bash
git clone --depth 1 https://github.com/bmad-code-org/bmad-method.git
cp -R bmad-method/skills/bmad ~/.hermes/profiles/corpusiq/skills/
cp -R bmad-method/skills/bmod-method ~/.hermes/profiles/corpusiq/skills/
```

Copying the skills does not scaffold the project. The first thing to run afterwards is the `bmad` skill's setup, which writes `_bmad/` and its scripts into the repository you are working in; without that, every workflow skill halts with a message telling the agent to run setup.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| bmad | 13,809 | The hub: answering BMad questions, recommending the next skill from what is installed, and running setup, status, doctor, repair, migration and initiative switching. |
| bmad-build | 13,010 | Taking delegated implementation work (a feature, a story, a bug fix, or a bare issue link) through build, review and verification, following the workflow the project renders. |
| bmad-code-review | 12,666 | Running several independent reviewers in parallel over a change, then triaging and presenting what they found. |
| bmad-brainstorming | 12,430 | A facilitated ideation session using named creative techniques when the ask is "help me brainstorm" or "help me ideate". |
| bmad-agent-architect | 12,418 | Talking to Winston, the system architect persona, for technical design leadership. |
| bmad-architecture | 12,393 | Writing one short architecture document that keeps separately built parts consistent, from a ticket file or against an existing codebase. |
| bmad-agent-pm | 12,383 | Talking to John, the product manager persona, for requirements discovery and PRD work. |
| bmad-agent-dev | 12,317 | Talking to Amelia, the developer persona, to implement stories and code changes. |
| bmad-agent-analyst | 12,283 | Talking to Mary, the business analyst persona, for market research, competitive analysis and requirements. |
| bmad-prd | 12,222 | Creating, updating or validating a PRD, in the same create, update and validate shape the other planning skills use. |
| bmad-agent-ux-designer | 12,157 | Talking to Sally, the UX designer persona, for UI and interaction decisions. |
| bmad-product-brief | 12,135 | Creating, updating or validating a product brief before planning starts. |
| bmad-ux | 11,983 | Capturing a UX vision as two files: DESIGN.md for how the product looks and EXPERIENCE.md for how it behaves. |
| bmad-advanced-elicitation | 11,975 | Making the model reconsider its last output with socratic questioning, first principles, a pre-mortem or a red-team pass. |
| bmad-review | 11,958 | Running one or more review lenses over a diff, a pull request or a document and reporting triaged findings, including adversarial, edge-case, verification-gap, structure and prose lenses. |
| bmad-qa-generate-e2e-tests | 11,940 | Adding end-to-end and API tests to a feature that already works, following the project's own test harness. |
| bmad-party-mode | 11,866 | A round table between installed agents or custom personas, plus authoring parties and AI focus-group panels. |
| bmad-project-context | 11,864 | Setting up, refreshing or auditing a repository's AGENTS.md block, and recording observed agent mistakes as pitfalls. |
| bmad-build-auto | 11,828 | One iteration of an unattended development loop, used when it is invoked by name. |
| bmad-deep-recon | 11,727 | Decision-grade research on a topic or on the repository itself: market, domain, technical, competitor, user sentiment, literature review or how a piece of code came to be. |
| bmad-prfaq | 11,705 | Testing a product concept with Amazon's Working Backwards method: the press release first, then the hard customer and stakeholder questions. |
| bmad-forge-idea | 11,679 | Pressure-testing a half-formed idea in a one-question-at-a-time interrogation, with persona rooms and an optional brief for the planning skills. |
| bmad-customize | 11,614 | Authoring and updating customization overrides for installed BMad skills, agent behaviour and workflows. |
| bmad-walkthrough | 11,607 | Guiding a human review of a commit, PR, file or directory, invoked by name. |
| bmod-core-tools | 10,915 | The Core Tools module record, not a runnable skill: the `bmad` hub reads it when setting up or reporting core tools. |
| bmod-method | 10,759 | The method module record that lists the shipped skills and the module version; setup reads it and no agent invokes it. |
| bmad-spec | 10,185 | Distilling messy intent (a brain dump, PRD, transcript or brief) into a five-field SPEC.md kernel with an optional stories.yaml breakdown. Retired on this branch, where bmad-agent-po replaces it. |
| bmad-retrospective | 9,829 | Retros on a finished epic folder: sourced findings, action items and an acceptance decision, with a headless mode for unattended runs. |
| bmad-correct-course | 9,783 | A retired planning skill from the earlier loop, now covered by bmad-agent-po; the name survives in the module's retired list, not in the tree. |
| bmad-ticket | 6,398 | A retired ticket skill that retired.toml records as renamed to bmad-agent-po; the install index still carries its old count. |

The remaining 51 indexed listings range from 11 to 4,975 installs: bmad-eval (4,975), bmad-toolsmith (4,968) and bmod-toolsmith (4,951) sit closest to the cut, followed by bmad-create-epics-and-stories (3,239), bmad-sprint-planning (3,156), bmad-agent-po (2,224) and bmad-preview-ticketing (1,630), then 44 smaller listings between 11 and 498 installs led by bmad-help (498) and ending at with-trigger, missing-trigger and deprecated-shim (11 each).

## Why This Matters for Hermes Agents

Most of the damage an agent does on a software task happens before it writes code: unstated assumptions become requirements, a decision made in one session is forgotten in the next, and a review that the agent runs on its own work finds nothing. BMad's whole design is aimed at those three failures. Every planning skill writes a named file into an output folder, so the next session reads the brief or the spec instead of reconstructing intent from a chat log.

The routing layer is the part worth copying into a Hermes setup even if you never adopt the method. `bmad` is an explicit dispatcher: it reads the installed modules' help through `uv run {skill-root}/scripts/knowledge.py --content` before answering what to do next, rather than guessing from skill names. `bmad-project-context` maintains an AGENTS.md block per repository and records mistakes the agent actually made as pitfalls. `bmad-customize` puts local overrides in a TOML file so a broken workflow can be changed without forking the skill.

The review skills carry the discipline. `bmad-code-review` fans out to independent reviewers and triages their output instead of letting one pass stand in for a review, `bmad-review` runs lenses whose stances differ (the adversarial lens must return at least ten concrete findings and treats an empty list as a signal to re-check), and `bmad-review` is explicitly forbidden from being invoked uninvited, including on its own edits. That last rule is the one most agent frameworks leave out, and it is why the suite is usable in a supervised loop.

For unattended work, `bmad-build-auto` is a single loop iteration rather than a daemon, and it only runs when something invokes it by name. Combined with `bmad-retrospective`'s headless mode, that keeps the unattended surface small and auditable.

## Usage

| You say | What happens |
|---|---|
| "What should I do next on this project" | bmad reads the installed modules' own help, checks the project state, and recommends the next skill with a reason instead of listing everything. |
| "Run bmad setup, it is a new checkout" | bmad runs setup.py, writes `_bmad/` and its scripts, asks the module's config questions in order and reports what changed. |
| "Turn this rough idea into something buildable" | bmad-forge-idea or bmad-product-brief pressure-tests the idea, then bmad-prd and bmad-architecture write the documents the build skills read. |
| "Build this story and review it properly" | bmad-build runs the implementation workflow for the story, then bmad-code-review sends the diff to several independent reviewers and triages their findings. |
| "Review this diff for edge cases only" | bmad-review runs the edge-case lens alone and reports findings in the canonical shape, naming the files it inspected. |
| "Get the team's read on this decision" | bmad-party-mode runs a round table between the installed personas, resolves the roster with its own script and keeps a per-party memory log. |
| "Retro this epic before we close it" | bmad-retrospective reads the epic file, each ticket and plan, the diffs and the commits, then produces sourced findings, action items and an acceptance decision. |

## Verification

Probe the paths before you copy them. All six URLs below returned 200 when this guide was written:

```bash
for p in skills/bmad/SKILL.md \
         skills/bmad-build/SKILL.md \
         skills/bmad-code-review/SKILL.md \
         skills/bmad-party-mode/SKILL.md \
         skills/bmad-review/SKILL.md \
         skills/bmod-method/bmod.toml; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/bmad-code-org/bmad-method/main/$p"
done
```

Read the hub before installing the rest, since it is the one that writes `_bmad/`:

- https://raw.githubusercontent.com/bmad-code-org/bmad-method/main/skills/bmad/SKILL.md
- https://raw.githubusercontent.com/bmad-code-org/bmad-method/main/skills/bmad/references/setup.md

After install, confirm what landed. The install index names match the frontmatter `name` field, so a mismatch means you are reading a stale copy:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -cE '^(bmad|bmod)-'
head -5 ~/.hermes/profiles/corpusiq/skills/bmad/SKILL.md
```

Then run the hub once in a scratch project and ask for `bmad status`. It writes nothing, and it is the cheapest way to see whether `_bmad/` and the module records line up.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| bmad | Pass | Pass | Pass |
| bmad-build | Pass | Pass | Pass |
| bmad-code-review | Pass | Pass | Warn |
| bmad-brainstorming | Warn | Pass | Pass |
| bmad-agent-architect | Warn | Pass | Pass |
| bmad-architecture | Pass | Pass | Pass |

The install surface is quiet. There is no `package.json` in the repository, so adding the skills runs no npm lifecycle hooks, and the skills themselves are Markdown plus TOML metadata and their own `references/` and `scripts/` folders. What runs later is `uv`: nearly every workflow skill's first instruction is `uv run --no-cache "{project-root}/_bmad/scripts/render_skill.py"` with the skill's own directory, and if that script is missing the skill is told to stop and offer setup rather than work around it. Audit `_bmad/scripts/` after the first setup, because that directory, not the skill tree, is the code that executes.

The setup reference widens the agent's authority in two ways worth knowing about. It instructs the agent to run `npx skills` install and update commands itself, with `-y`, so an unattended run can add skills without a prompt. It also collects the module's config answers into a project TOML file and marks which answers are `user` scope, meaning personal and not shared with the repository. Both are reasonable, both deserve a supervised first run.

Warnings are concentrated where the work is. `bmad-code-review` is the only sampled skill with a non-pass cell, a Snyk Warn carrying code W011, and `bmad-brainstorming` plus `bmad-agent-architect` carry a Gen Agent Trust Hub Warn. Read those three on skills.sh before you hand the agent a worktree. Modules can also carry author-supplied install messages (the fields sit in each `bmod.toml`), and the setup flow tells the agent to show them quoted and never follow them as instructions; keep that rule in place if you retarget the skills at another harness.

## Limitations

- Snapshot data, verified 2026-10-28: 383,849 combined installs across 81 indexed listings; 54,667 GitHub stars; MIT; branch main. Counts drift over time.
- The install index outruns the tree. 47 of the 81 indexed listings have no directory in the current `skills/` tree, and three of them are large enough to sit in the table above: bmad-spec (10,185), bmad-correct-course (9,783) and bmad-ticket (6,398). The module's `retired.toml` records bmad-ticket as renamed to bmad-agent-po, and lists bmad-spec and bmad-correct-course as removed, so those counts describe an older state of the suite.
- 81 indexed listings resolve to 31 directories on main, 28 of them runnable and three of them module records, plus one nested sample skill inside `bmad-toolsmith/shapes/`. The older, smaller skill names in the tail (bmad-create-prd, bmad-dev-story, bmad-market-research and similar) are v6-era skills that the current tree does not carry.
- This branch is the V7 preview alpha. The README says to expect breaking changes between updates, and the changelog already removes translated documentation, `planning_artifacts` and web bundles. The stable v6.12 line lives on a separate branch and is installed by `npx bmad-method install` instead.
- Setup needs `uv` and writes `_bmad/` into the target project. A copied skill without a project setup is inert: it halts and asks the agent to run the hub's setup, which means the skills are per-project, not global.
- The documented install paths are the skills CLI, the Claude Code and Codex plugin marketplaces, and the npm installer. None of them names Hermes, so the copy route is the only one here, and it brings no slash commands or hooks with it.

## Related

- [Compound Engineering Plugin - Every Inc Workflow Suite Setup](/hermes/skills/catalog/compound-engineering-plugin-setup) - the closest comparison: a plan, build, review and compound loop shipped as agent skills.
- [PM Skills - Product Management Lifecycle Suite Setup](/hermes/skills/catalog/pm-skills-setup) - the product side of the same work, without BMad's delivery and review layers.
- [Sentimony Skills - Dev Workflow & Review Gates Setup](/hermes/skills/catalog/sentimony-skills-setup) - review gates as a standalone workflow if you want the checkpoints without the planning suite.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `bmad` first and let it scaffold. `npx skills add bmad-code-org/BMAD-METHOD --skill bmad` is the README's own fallback, only setup creates `_bmad/`, and every workflow skill halts until that directory exists.
- Ask for `bmad status` before and after an update. Setup runs `npx skills update`, retires renamed skills and can add config questions, so the diff between two status calls is the real changelog for your project.
- Pick skills by module instead of taking the whole tree. `bmad` plus `bmod-method` and `bmod-core-tools` is the smallest working install, and the review and planning skills can be added per project.
- Name the lens when you ask for a review. `bmad-review` defaults to every applicable lens, and a single edge-case or verification-gap pass costs a fraction of the context.
- Treat the persona agents as debrief partners, not authors. Asking Winston or Sofia to argue a decision is cheap; letting them write code without `bmad-build`'s review step skips the part of the suite that checks the work.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
