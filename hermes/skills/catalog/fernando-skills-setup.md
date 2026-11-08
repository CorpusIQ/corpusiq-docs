---
title: "Fernando Skills - Spec-Driven Development for Agents"
description: "klerith/fernando-skills on skills.sh: 9.1K combined installs; a spec and spec-impl pair that writes an approved spec before any code exists."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/fernando-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "spec driven development", "planning", "code review"]
---

# Fernando Skills - Setup Guide

**Source:** [klerith/fernando-skills](https://www.skills.sh/klerith/fernando-skills) via skills.sh - 9,073 combined installs across 3 indexed listings; first seen 2026-11-08 (Nov 8 2026 morning sweep)
**GitHub:** 372 stars, MIT, last pushed 2026-10-08, 2 SKILL.md directories under skills/engineering
**Category:** Spec-driven development for agents: write the spec first, implement against it, and keep code and intent in sync
**Quality Tier:** 🟢 Recommended - MIT licence, Pass on all three scanners for every skill, small enough to read end to end before you install it.

Two skills that only work as a pair, and a deliberate gap between them. `/spec` turns a one-line idea into a numbered spec file through questions, and never writes application code. `/spec-impl` reads that file, refuses to start unless its state says approved, creates a branch, and implements the plan one step at a time with a pause after each step.

That gap is the design. The status field is edited by a human between the two commands, and the README says it outright: without that hand edit the method degrades into an agent that writes plausible documentation and then writes whatever code occurs to it anyway. The skill file enforces the same thing from the other side: `/spec` is instructed not to mark a new spec as approved and not to propose implementing it after saving.

The spec template is the part that carries the weight. Header in a blockquote with status, dependencies, date and a one-sentence objective; then scope with an explicit "not in" list; data model with real names; a numbered implementation plan where each step leaves the system working; boolean acceptance criteria; decisions taken and discarded; and risks. Valid states are `Draft`, `In review`, `Approved`, `Implemented` and `Obsolete`, and both skills accept the equivalents in any language, so a Spanish repo with `Aprobado` works the same as an English one.

## Installation

The README documents three routes. The first is the one most harnesses want:

```bash
npx skills@latest add Klerith/fernando-skills
```

For Cursor, Codex and Antigravity, the repo ships an installer that rewrites the skill for each target:

```bash
git clone https://github.com/Klerith/fernando-skills ~/.fernando-skills
cd ~/your-project
~/.fernando-skills/scripts/install-to-agent.sh <agent>
```

`<agent>` is one of `claude`, `cursor`, `codex` or `antigravity`. Per the README's table, `claude` symlinks each skill into a project-scoped `.claude/skills/`, `cursor` generates `.cursor/rules/<name>.mdc` files invoked with `@spec` and `@spec-impl`, `codex` adds a `## Skills` block to `AGENTS.md` and copies bodies into `.codex/skills/`, and `antigravity` copies bodies into `.antigravity/skills/`. Cursor and Codex do not support the `argument-hint` and `disable-model-invocation` frontmatter fields, so the installer drops them and keeps the body.

The third route is a manual copy, which is the one to use if you want the skills in one project rather than all of them:

```bash
mkdir -p .claude/skills
cp -r skills/engineering/spec .claude/skills/
cp -r skills/engineering/spec-impl .claude/skills/
mkdir specs
```

Whichever route you take, `specs/` has to exist at the project root. The `/spec` skill reads its directory listing at load time to work out the next number, and `/spec-impl` reads it to find the file you name.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| spec | 4,591 | Turning a feature request into `specs/NN-slug.md` through four phases: context, clarifying questions, write, save |
| spec-impl | 4,481 | Implementing an approved spec on a `spec-NN-slug` branch, one plan step at a time, with diff review pauses |
| setup-fernando-skills | 1 | The setup row for this collection on skills.sh; it has no SKILL.md directory in the repository |

The threshold for this pack is zero, so every indexed row is in the table above. There is no tail: 0 rows fall below the threshold.

Two of the three rows are the actual skills and they split the work cleanly. `spec` runs a session context block that injects today's date and the current `specs/` listing, reads the project memory file (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md` or `README.md`, first hit wins), reads the two most recent specs to match their conventions, then asks questions in blocks of three to five with concrete options and a marked recommendation. It stops asking when it can answer three things without assuming: which files change, what the first and last executable step are, and how completion is verified. Saving writes the file, seeds `specs/.spec-config.yml` with `AutoCreateBranch: true` if that file is missing, and stops.

`spec-impl` is the stricter half. It validates the state means approved, then checks the working tree and refuses to carry uncommitted changes onto a new branch without an explicit answer. It derives the branch name from the file (`01-mvp-arkanoid.md` becomes `spec-01-mvp-arkanoid`), shows the objective, scope, plan and acceptance criteria before writing anything, and then never commits: not per step, not at the end. On an ambiguity it stops and presents two or three options rather than improvising.

## Why This Matters for Hermes Agents

The common failure in agent-assisted feature work is not bad code, it is code that answers a question nobody asked. A prompt like "add multiplayer" contains a dozen unstated decisions, and an agent that starts typing resolves all of them silently. This pair makes the resolution explicit and cheap: questions now, a file that records the answers, and an implementation pass that is allowed to follow the file and nothing else.

The state machine is the second idea worth copying. `disable-model-invocation: true` on both skills means the agent cannot decide to run them; the human types `/spec` or `/spec-impl`. The approved state is also human-set. That combination turns a workflow into a gate, and gates are what stop an autonomous loop from drifting.

The third idea is tool restriction in frontmatter. `spec` declares `allowed-tools` limited to `Read, Glob, Grep, Write, AskUserQuestion` plus `ls`, `cat` and `date`. `spec-impl` adds `Edit` and read-only git: `git status`, `git branch`, `git checkout`, `git log`, `git diff`, `git stash`. Commit is deliberately absent. If your harness honours `allowed-tools`, the "never commits automatically" rule is enforced by the tool layer and not only by prose.

Hermes runs the same shape already: a planning phase, a written artifact, then execution against it. What this pack adds is the part most planning prompts skip, which is a written refusal path. `/spec-impl` has a fixed error message for a spec that is not approved and an instruction not to offer alternatives, and that consistency is why the gate holds.

## Usage

| You say | What happens |
|---|---|
| "/spec add leaderboards to the game" | Reads project memory and recent specs, asks clarifying blocks, writes `specs/03-leaderboards.md` in `Draft` |
| "/spec levels-and-highscores" | A single kebab-case token is treated as both slug and seed description, without asking for confirmation |
| "/spec-impl 01-mvp-arkanoid" | Validates the state is approved, creates or switches to `spec-01-mvp-arkanoid`, shows the plan, waits to start |
| "/spec-impl 02" | Number-only arguments resolve to the one matching file in `specs/` |
| "Implement the spec" after a Draft was saved | Stops with the standard refusal, because Draft is not approved, and offers to resume with `/spec` |
| "Also add a chat system while you are in there" | Outside the spec's scope: the agent says so and suggests a new spec instead of implementing it |
| "Change the state to Approved" | The agent should not do this. The README and both skills put that edit in human hands |

## Verification

Read both skill files before installing. These paths returned 200 on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/klerith/fernando-skills/main/skills/engineering/spec/SKILL.md | head -40
curl -fsSL https://raw.githubusercontent.com/klerith/fernando-skills/main/skills/engineering/spec-impl/SKILL.md | head -40
```

The first should open with frontmatter naming `spec`, `disable-model-invocation: true`, `argument-hint: 'short feature description or requirement'` and an `allowed-tools` line, then a heading that calls it the guided spec designer. The second should open with `name: spec-impl`, an `argument-hint: <NN-spec-name>`, and a description that says it validates the state means approved in any language, creates the branch and pauses for diff review.

After installing, the cheapest end-to-end check is a throwaway spec in a scratch repository:

```bash
mkdir -p /tmp/specprobe/specs && cd /tmp/specprobe && git init -q
# invoke /spec with a one-sentence feature, answer the questions, accept the saved file
ls specs/
head -6 specs/01-*.md
```

The listing should show `01-<slug>.md` and, on the second run, a `specs/.spec-config.yml` with `AutoCreateBranch: true`. The header should carry a status of Draft, a date and a one-sentence objective. Then run `/spec-impl 01` against it without touching the status: it should refuse. Change the status to `Approved` by hand and run it again: it should create `spec-01-<slug>` and ask before step one.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-08) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| spec | Pass | Pass | Pass |
| spec-impl | Pass | Pass | Pass |
| setup-fernando-skills | Pass | Pass | Pass |

Every row passes every scanner, and the artifacts justify it: both skills are markdown plus one template file. Nothing executes during a run except the shell snippets the harness expands at load time, which are `date +%F`, `ls specs/`, `git status --short`, `git branch --show-current` and a `cat` of the config file. All read-only, all inside the project.

The one executable in the repository is `scripts/install-to-agent.sh`, which the README documents as the installer for Cursor, Codex and Antigravity. It writes into the project and symlinks or copies skill directories, so it is worth a read before you run it in a repository you care about. It was read as a path reference here, not executed.

The design decision that matters more than any scanner result is the write boundary. `spec` may write exactly one file under `specs/`. `spec-impl` may edit code but is not granted commit access, and it is told to stop when the working tree is dirty rather than stash on your behalf. If your harness ignores `allowed-tools`, none of that is enforced and the guarantee drops back to prompt compliance.

Licence: the repository root ships a LICENSE file, the MIT License, Copyright (c) 2026 Fernando Herrera. That covers the skill text, the template and the install script.

## Limitations

- Snapshot data, verified 2026-11-08: 9,073 combined installs across 3 indexed listings; 372 GitHub stars; MIT; last pushed 2026-10-08. The star count is small and the repo has not moved in a month, so treat it as one author's workflow rather than a maintained product.
- Drift between the index and the tree: 3 indexed listings against 2 SKILL.md directories. The third listing, `setup-fernando-skills`, has 1 install and no directory in the repository, so its contents could not be inspected.
- The workflow needs a harness that supports slash commands with arguments. On Cursor and Codex the installer drops `argument-hint` and `disable-model-invocation`, so the command names become `@spec` rules and model-invocation blocking is lost.
- `disable-model-invocation: true` is a Claude Code frontmatter field. Harnesses that do not read it will let the model trigger these skills on its own, which removes the human gate the method depends on.
- Both skills assume git and a `specs/` directory at the project root. There is no test suite and no CI, so the only verification is running the pair against a real repository.
- Repository documentation has drifted from the code: `CLAUDE.md` says skill descriptions are written in Spanish, while both shipped SKILL.md files are in English. The skills themselves reply in the language of the user's prompt.
- The method is opinionated about scale. A feature that does not fit in one sentence, or that touches more than three areas, is supposed to be split into several specs, which is right for large work and heavy for a two-file change.
- Not verified: behaviour on a repository with a dirty working tree, an existing branch named after the spec, or a spec whose dependency points at a missing file. The skill documents all three paths, but they were read rather than exercised.

## Related

- [Spec Kit Skills - Specify, Plan, Implement](/hermes/skills/catalog/speckit-agent-skills-setup)
- [Claude Code Skills - Agentic Coding & Skill](/hermes/skills/catalog/claude-code-skills-setup)
- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `AutoCreateBranch: false` in `specs/.spec-config.yml` on a repository with branch protection. It turns branch creation into a `[y/N]` prompt and keeps the one irreversible step of `/spec-impl` under your hand.
- Keep `specs/` in version control. The specs are the audit trail, and `/spec` reads the two most recent to match wording, headings and language, so a committed history makes each new spec cheaper and more consistent.
- Invoke `/spec-impl` with just the number (`/spec-impl 03`). It resolves number, slug or full filename, and the short form avoids typos in long slugs.
- Edit the status field yourself, on purpose. That single human action is the whole gate; if you let the agent flip it to Approved, you have an expensive writing prompt and no review step.
- Put rejected options in the decisions section. It is the section with the longest shelf life, because it is what stops a future agent from proposing the approach you already ruled out.
- Read `template.md` before your first run. It defines the section shapes the skill is instructed to follow, including the mandatory explicit "not in scope" block.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
