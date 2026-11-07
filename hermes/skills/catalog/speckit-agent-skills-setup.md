---
title: "Spec Kit Skills - Specify, Plan, Implement"
description: "dceoy/speckit-agent-skills on skills.sh: 23.6K combined installs; Spec Kit's specify, plan, tasks and implement passes as portable agent skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/speckit-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "spec driven development", "spec kit", "planning"]
---

# Spec Kit Skills - Setup Guide

**Source:** [dceoy/speckit-agent-skills](https://www.skills.sh/dceoy/speckit-agent-skills) via skills.sh - 23.6K combined installs across 12 indexed listings; first seen 2026-11-06 (Nov 6, 2026 evening sweep)
**GitHub:** 170 stars, AGPL-3.0 licence, last pushed 2026-11-02, 22 SKILL.md directories: 12 under skills/ and 10 runtime copies under .cursor/skills/
**Category:** Spec-driven development for agents: constitution, specify, clarify, plan, tasks, implement, analyze and converge passes
**Quality Tier:** 🟡 Review - clean scanner verdicts on the core passes and a fully scripted regeneration workflow, held back by an AGPL licence and warnings on the analyze skill.

Spec Kit is GitHub's spec-driven development toolkit: a set of commands that turn a feature request into a written specification, an implementation plan, an ordered task list, and then code that follows both. This repository repackages that workflow as agent skills, so the passes are invocable from Claude Code, Codex CLI, Cursor, GitHub Copilot, OpenCode and Gemini rather than living as a set of commands in one tool's format.

It is generated output rather than a hand-written prompt library, and the README is explicit about that. A CI workflow resolves the latest Spec Kit release, records `specify --version` in `VERSION.md` (currently `specify 1.2.3`), re-runs `specify init --force --here --ignore-agent-tools --script sh --integration` for each configured integration, formats the result, and opens a pull request when the tracked version changes. The tracked version and the skills therefore move together.

The two repository-specific additions are `claude-command-converter`, which migrates older `.claude/commands/*.md` files into portable `skills/*/SKILL.md` directories, and `speckit-baseline`, which derives a specification from code that already exists. Everything else is the upstream flow, kept deliberately close to it.

## Installation

The README's quickstart clones the repository first, because the skills and the Spec Kit helper scripts are read from the checkout:

```bash
git clone https://github.com/dceoy/speckit-agent-skills.git
cd speckit-agent-skills
```

Spec Kit itself is a separate prerequisite. Install it from `github/spec-kit`, then initialize the target project with the integration that matches your agent, from the project root:

```bash
specify init --here --integration <integration>
```

The integrations the repository currently generates for are `codex`, `agy`, `cursor-agent`, `copilot`, `opencode` and `claude`. Initialization writes the runtime-specific entry points: `.claude/skills` and `.agents/skills` as symlinks to the shared `skills/` directory, `.cursor/skills/` as real copies, `.github/agents/` and `.github/prompts/` for Copilot, and `.opencode/commands/` for OpenCode.

If your runtime consumes Agent Skills directly, copy the skills into the project rather than pointing at the clone:

```bash
cp -a skills/* /path/to/project/skills/
```

Then invoke the pass you want, either by asking for it in natural language or through the runtime's skill invocation. The README warns that skills do not always auto-run, so requesting `speckit-specify` explicitly is the reliable path.

Nothing installs through a package manager, and nothing installs globally. This is a per-project workflow, which is appropriate given that its whole purpose is to write into the project's specification directory.

## What It Provides

Twelve indexed listings, all above the threshold, so the whole set appears here:

| Skill | Installs | Use For |
|---|---|---|
| speckit-specify | 2,621 | Capture requirements for new work as a specification before any code is written |
| speckit-plan | 2,520 | Produce the implementation strategy from the specification |
| speckit-tasks | 2,476 | Generate the ordered work items that implement the plan |
| speckit-implement | 2,444 | Execute the plan by processing the tasks in tasks.md |
| speckit-constitution | 2,425 | Create or update the project constitution from interactive or supplied principles |
| speckit-clarify | 2,251 | Ask up to five targeted questions about underspecified areas and encode the answers back into the spec |
| speckit-analyze | 1,568 | Non-destructive consistency and quality analysis across spec.md, plan.md and tasks.md after task generation |
| speckit-checklist | 1,549 | Generate a custom requirements-quality checklist for the current feature |
| speckit-taskstoissues | 1,516 | Convert generated tasks into GitHub issues so the work has an owner and a number |
| speckit-baseline | 1,514 | Derive a specification from an existing codebase, for code that has no written requirements |
| claude-command-converter | 1,431 | Convert `.claude/commands/*.md` files into portable Agent Skills format |
| speckit-converge | 1,294 | Compare the codebase against spec, plan and tasks, then append the unbuilt work to tasks.md so implement can finish it |

All 12 indexed listings clear the 500-install threshold and appear in the table above.

The install order is informative. Specify, plan, tasks and implement are the four passes everything else supports, and they carry the top four counts. Clarify, analyze and converge are the optional quality passes, and they sit lower, which matches how teams actually work: the happy path gets adopted and the checks get adopted later, usually after the first expensive misunderstanding.

## Why This Matters for Hermes Agents

An agent with no written spec optimizes for the nearest plausible interpretation of the prompt. The constitution pass is the correction that costs least: it writes project principles into a file the later passes read, so conventions stop being re-derived per session and stop drifting between sessions.

Clarify is the pass that most agents skip and most projects need. Asking up to five targeted questions about underspecified areas, and writing the answers back into the specification, converts assumptions into text. That text is the difference between a plan the agent can check itself against and a plan it can quietly reinterpret halfway through.

Analyze is where the repository earns its place for review work. It runs a non-destructive cross-artifact pass over spec.md, plan.md and tasks.md after task generation, which catches the failure mode that costs the most: three documents that each look reasonable and contradict each other. Because it does not rewrite anything, it is safe to run repeatedly in a loop.

Converge handles the reality of a partially built feature. It assesses the codebase against the spec, plan and tasks, then appends the remaining unbuilt work as new task entries, so a later implement pass can finish the job instead of the agent starting over and duplicating what exists.

Two smaller pieces matter for orchestration. `speckit-taskstoissues` moves tasks into GitHub issues, which gives work an external identifier a second agent or a human can be pointed at. `claude-command-converter` is the migration path for teams whose instructions still live as slash commands, and it is the piece that makes this repository usable outside Claude Code without rewriting the commands by hand.

The generated-output discipline is the honest caveat and also a feature: because the skills are regenerated from a tracked Spec Kit version, they will not silently diverge from upstream. They will also not carry local fixes, so repository-specific behaviour belongs in your own skills directory, not in edits to the generated copies.

## Usage

| You say | What happens |
|---|---|
| "Set up the project constitution for this repo" | The constitution pass interviews you for principles and writes or updates the constitution file the later passes read |
| "Specify the export feature before we write anything" | A specification is drafted from your description, with requirements and acceptance criteria, into the project's spec location |
| "Ask me what is still ambiguous in this spec" | Clarify asks up to five targeted questions and encodes the answers back into the specification |
| "Plan the implementation from the spec" | The plan pass produces the technical strategy, file touch list and sequencing from the written spec |
| "Break the plan into ordered tasks" | Tasks generates ordered work items, then analyze checks spec, plan and tasks against each other |
| "Implement the tasks" | Implement works through tasks.md in order and updates task state as it goes |
| "What is left to build before this feature matches its spec?" | Converge compares code to spec, plan and tasks, then appends the unbuilt work to tasks.md |

## Verification

Read the pass before installing it. This path returned 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/dceoy/speckit-agent-skills/main/skills/speckit-specify/SKILL.md | head -20
```

The frontmatter should name `speckit-specify` and the body should describe reading and writing the project's specification artifacts, with the `.specify/` templates as inputs.

After install, count what landed. A full checkout carries 12 skill directories under `skills/`:

```bash
ls skills | wc -l
ls .specify/templates
```

The count should be 12, and the templates directory should hold the spec, plan and task templates the passes read. If your runtime consumes the Cursor copies, `.cursor/skills/` should hold 10 directories, a subset that excludes `speckit-baseline` and `claude-command-converter`.

Then confirm the version tie, which is the thing that goes stale:

```bash
specify --version
cat VERSION.md
```

The installed Spec Kit version and the version recorded in `VERSION.md` should agree. A mismatch means either the checkout is behind upstream or your local Spec Kit is, and generated skills that assume a different command surface will fail in ways that look like model errors.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| speckit-specify | Pass | Pass | Pass |
| speckit-implement | Pass | Pass | Pass |
| speckit-analyze | Warn | Warn | Pass |
| speckit-baseline | Pass | Pass | Pass |
| speckit-converge | Pass | Pass | Pass |

Most of the surface is markdown, and the sampled core passes are clean on all three scanners. The two warnings sit on `speckit-analyze`, which is the pass that reads three artifacts plus the repository at once, so a scanner reacting to broad file reads is the plausible reading. It is worth opening the Socket report rather than assuming either way.

There is real executable surface underneath. `.specify/scripts/bash/` holds the helper scripts the passes run, `specify init` writes into the current project, and the implementation pass edits source files and can run tests. None of that is unusual for a spec-driven workflow, and all of it means the skill inherits whatever authority the agent already had.

The licence is the constraint to read carefully. The repository ships the GNU Affero General Public License version 3, not MIT, so copying these skills into a distributed product, or running a modified version as a network service, carries copyleft obligations. Using them inside your own project to plan and build that project is the ordinary case and is not the same thing as redistributing them.

The supply chain is the other consideration. The generated files come from a CI job that resolves the latest upstream Spec Kit release and opens a pull request, so trust in this repository is partly trust in `github/spec-kit` and partly trust in that workflow. Pinning to a commit rather than tracking `main` is the cheap mitigation.

## Limitations

- Snapshot data, verified 2026-11-06: 23,609 combined installs across 12 indexed listings; 170 GitHub stars; AGPL-3.0 licence; last pushed 2026-11-02. Counts drift over time.
- It depends on Spec Kit being installed and the project initialized. Without `specify init`, the passes have no templates and no artifact locations to write to.
- Skills do not always auto-run. The README says to use the runtime's invocation flow or the explicit skill name, which means a vague prompt can be handled without the workflow engaging at all.
- Generated files are managed output. The README asks you to change the integration configuration or your own skills instead of hand-maintaining generated copies, so local edits are expected to be overwritten on regeneration.
- Runtime layouts differ by design. Cursor gets copies, Claude Code and Codex get symlinks to the shared directory, Copilot and OpenCode get their own generated formats, so behaviour can differ between agents on the same commit.
- Gemini CLI is checked in but outside the regeneration set, so its commands will age against the tracked Spec Kit version unless someone maintains them by hand.

## Related

- [OpenSpec Skills - Spec-Driven Development Suite Setup](/hermes/skills/catalog/fission-openspec-skills-setup)
- [writing-plans + subagent-driven-development Setup Guide](/hermes/skills/catalog/writing-plans-subagent-development-setup)
- [Superpowers - Agentic Skills Framework & Development](/hermes/skills/catalog/superpowers-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run constitution once, early, and commit it. Every later pass reads it, and retrofitting principles after three features have shipped produces a document that describes what you did rather than what you meant.
- Use baseline instead of specify on inherited code. Asking for a spec of a codebase with no written requirements produces fiction; deriving it from the source at least starts from what exists.
- Run analyze after tasks, not before. Its contract is a cross-artifact pass over spec, plan and tasks, so it has nothing to compare until all three exist.
- Read tasks.md yourself before implementing. The implement pass follows the list in order, so a badly ordered list becomes a badly ordered change set.
- If you track `main`, re-run `specify --version` after every pull. Version skew between the generated skills and your local Spec Kit is the most common failure and the least obvious one.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
