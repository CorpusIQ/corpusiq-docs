---
title: "Open SDD Skills - Spec-Driven Development Setup"
description: "forztf/open-skilled-sdd: 9.6K combined installs across 16 listings, OpenSpec and Spec Kit workflows packaged as inspectable, composable agent skills"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/open-skilled-sdd-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "spec-driven development", "openspec", "spec kit"]
---

# Open SDD Skills - Setup Guide

**Source:** [forztf/open-skilled-sdd](https://www.skills.sh/forztf/open-skilled-sdd) via skills.sh - 9.6K combined installs across 16 indexed listings; first seen Nov 13, 2026
**GitHub:** 10 stars, no licence file, `main` branch, last pushed 2025-11-28, 16 `SKILL.md` files under `skills/`, 159 files in total
**Category:** Spec-driven development workflow for AI coding assistants
**Quality Tier:** 🟡 Yellow - all 16 indexed listings map to 16 skills in the tree and the workflow is documented end to end, held back by the absence of a licence file, a single author and a very small star count.

Most spec-driven development tooling ships as a black box. You install a CLI, the assistant changes how it behaves, and when the output is disappointing you cannot tell whether the model was weak, the assistant fed it the wrong context, or your own prompt was the problem. This repository exists to make the middle suspect inspectable, and it does that by putting the method in files you can read.

The README describes the path to it. The author read through the open options (6A workflow, PRPs, Spec Kit, OpenSpec, spec-workflow-mcp, BMad-Method), used each of them, and concluded that a single merged "comprehensive" method was a dead end because the vendors are all trying to build that same thing. The bet here is the opposite one: instead of one method, a set of small composable skills you can read, edit and combine. The README credits `skilled-spec` as the original English version of the approach.

What you get is one method family per skill. The eight `openspec-*` skills cover proposal creation, implementation, context loading and archiving, each with a Chinese-language counterpart. The eight `speckit-*-zh` skills do the same for the Spec Kit workflow in Chinese. Both families write real artifacts into the repo, so the proposal, the task list and the archive are files you and the agent both reason over.

## Installation

The documented Claude Code path is the plugin marketplace:

```text
/plugin marketplace add forztf/open-skilled-sdd
/plugin install open-skilled-sdd@open-skilled-sdd-marketplace
```

The same README documents a manual route for Claude Code, which is to copy every subdirectory under `skills/` into `.claude/skills/` for a project or `~/.claude/skills/` for a global install, and commit the result so the team picks it up on clone. For hosts that read `AGENTS.md` (Codex, Gemini, Cursor) it ships its own CLI:

```bash
npx open-skilled-sdd
npx open-skilled-sdd sync
```

There is no `npx skills add` line anywhere in this README. The CLI above is the repository's own npm package, not the skills CLI from this catalog, so treat the plugin marketplace and the copy step as the install paths and the CLI as the `AGENTS.md` sync step.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| openspec-implementation | 1,419 | Executes an approved proposal by working through tasks in order, with testing and progress tracking. |
| openspec-proposal-creation | 1,194 | Structured change proposals with specification deltas for new features, breaking changes or new capabilities. |
| openspec-proposal-creation-cn | 1,168 | Chinese-language variant of proposal creation, same structured proposals and spec deltas. |
| openspec-context-loading | 1,102 | Loads project context, lists existing specs and open changes, searches capabilities and requirements. |
| openspec-archiving | 1,032 | Archives completed changes and merges the specification deltas into living documentation. |
| openspec-context-loading-cn | 392 | Chinese-language variant of context loading: which specs exist, what is in flight, which capabilities are available. |
| openspec-implementation-cn | 384 | Chinese-language variant of implementation, verification first and tasks in order. |
| openspec-archiving-cn | 363 | Chinese-language archiving: merge the deltas, update the living spec, close the proposal. |
| speckit-specify-zh | 333 | Spec Kit step in Chinese: turns a feature description into a structured spec, with branch naming and quality checks. |
| speckit-tasks-zh | 320 | Spec Kit step in Chinese: generates a dependency-ordered `tasks.md` from the design documents. |
| speckit-plan-zh | 313 | Spec Kit step in Chinese: runs the planning workflow and produces the design artifacts. |
| speckit-clarify-zh | 312 | Spec Kit step in Chinese: asks up to five targeted questions and writes the answers back into the spec. |
| speckit-checklist-zh | 312 | Spec Kit step in Chinese: generates a requirements checklist that tests clarity, completeness and consistency. |
| speckit-implement-zh | 309 | Spec Kit step in Chinese: executes the approved tasks, testing first. |
| speckit-analyze-zh | 308 | Spec Kit step in Chinese: cross-checks spec, plan and tasks for gaps, duplication and ambiguity. |
| speckit-constitution-zh | 305 | Spec Kit step in Chinese: writes or updates the project constitution and keeps the dependent templates in sync. |

All 16 indexed listings clear the 300-install threshold and appear in the table above.

The install band is informative. The four English OpenSpec skills sit between 1,032 and 1,419 installs, and the Chinese proposal variant lands inside the same band at 1,168, which is what a pack installed as a unit looks like. Everything else trails between 305 and 392, the shape of variants found later rather than installed as a set.

## Why This Matters for Hermes Agents

The useful idea here is not spec-driven development as a methodology, it is the refusal to hide the method. A skill file is a prompt you can open, diff and rewrite. When the same repository also writes its decisions into files in the repo, the debugging loop closes: a bad result points at a spec you can read rather than at a system prompt you cannot.

For an agent setup, that turns three vague failure modes into one concrete one. If the proposal skill produced a weak proposal, the proposal is a file. If the implementation skill drifted from it, the task list is a file. Neither can hide behind "the model was having a bad day".

The archiving skill is the part most teams skip and most agent workflows need. Merging deltas back into a living spec is what stops the next session from re-deriving context that was already settled, and it is the cheapest form of long-term memory a repo can have.

The composition model is the other transferable lesson. Sixteen small skills that each do one step beat one large skill that does the workflow, because you can replace the step that misfires and leave the rest alone.

## Usage

| You say | What happens |
|---|---|
| "openspec context, what specs exist and what is in flight?" | Runs `openspec-context-loading` and returns the spec list, open changes and matching capabilities. |
| "openspec proposal, add rate limiting to the public API" | Runs `openspec-proposal-creation` and writes a proposal with EARS-style requirement deltas. |
| "openspec implement the rate limiting proposal" | Runs `openspec-implementation` and works the task list in order, testing as it goes. |
| "The proposal is done, archive it and update the spec" | Runs `openspec-archiving` and merges the deltas into the living documentation. |
| "Turn this feature description into a spec with a branch name" | Runs `speckit-specify-zh` for the Spec Kit specify step. |
| "Generate the task list from the plan and data model" | Runs `speckit-tasks-zh` and returns a dependency-ordered `tasks.md`. |
| "Check the spec, plan and tasks against each other before I start" | Runs `speckit-analyze-zh` and reports gaps, duplication and ambiguity. |

## Verification

Two skill files on the `main` branch, both returning 200:

```bash
curl -fsSL https://raw.githubusercontent.com/forztf/open-skilled-sdd/main/skills/openspec-proposal-creation/SKILL.md | head -8
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/forztf/open-skilled-sdd/main/skills/openspec-archiving/SKILL.md
```

After installation, confirm 16 folders with one `SKILL.md` each. A missing folder is a copy problem rather than an install problem. Read a proposal SKILL.md before you use it: these files are the method, and you are meant to edit them.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| openspec-implementation | Pass | Pass | Pass |
| openspec-proposal-creation | Pass | Pass | Pass |
| openspec-proposal-creation-cn | Pass | Pass | Pass |
| openspec-context-loading | Pass | Pass | Pass |
| openspec-archiving | - | - | - |

The other 11 indexed listings carry no verdict row on skills.sh yet, so the sampled passes cover less than a third of the pack. One thing the verdicts do not capture: this is not a text-only pack. The 159 files include 20 shell scripts, 30 PowerShell scripts and 7 JavaScript files, mostly helper scripts under the Spec Kit skills' own `scripts/` and `assets/` folders plus the npm CLI in `bin/`. Read a script before you let a skill run it.

## Limitations

- Snapshot data, verified 2026-11-13: 9,566 combined installs across 16 indexed listings; 10 GitHub stars; no licence file; last pushed 2025-11-28. Counts drift over time.
- No licence file is present in the repository, even though the README carries an MIT badge and a License section that points at a `LICENSE` file. Treat the terms as unspecified until that is resolved.
- Last pushed November 2025, so the skills have not moved in a year. The OpenSpec CLI and Spec Kit have both changed since, and the skills are instructions rather than pinned code.
- One author and 10 stars means no second set of eyes on the prompts. Read them; do not assume review happened elsewhere.
- The Spec Kit skills ship bash and PowerShell helper scripts inside their own `scripts/` and `assets/` folders, so a full install is not a read-only operation. Those files sit outside the OpenSpec listings that carry security verdicts, and they are what to review first.
- The listing count is inflated by language pairs: 16 listings describe 8 distinct capabilities, four OpenSpec skills doubled into English and Chinese, plus eight Chinese Spec Kit steps. The README table itself lists only the 8 OpenSpec skills.
- The README documents the plugin marketplace, a manual copy into `.claude/skills/` and its own npm CLI. There is no skills-CLI install line, so `npx skills add` is undocumented here even if the package resolves.

## Related

- [OpenSpec Skills - Spec-Driven Development Suite Setup](/hermes/skills/catalog/fission-openspec-skills-setup)
- [Warp Common Skills - Spec-Driven Development Workflow Setup](/hermes/skills/catalog/warpdotdev-common-skills-setup)
- [Fernando Skills - Spec-Driven Development for Agents](/hermes/skills/catalog/fernando-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `openspec-context-loading` at the start of a session on an existing repo. It is the cheapest way to stop the agent inventing a spec that already exists.
- Paste the proposal file into the implementation prompt. The implementation skill expects to read tasks it did not write, and handing it the file keeps the two in step.
- Archive when you merge, not when you remember. `openspec-archiving` is what keeps the living spec from drifting into a folder of dead proposals.
- Edit the SKILL.md files in your fork. The whole premise of the repository is that you can inspect and change the method, and an unedited copy gives up that advantage.
- If you work in English, do not install the Chinese variants. They are full duplicates and they double the description surface the agent has to disambiguate on.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
