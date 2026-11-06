---
title: "Hyperskills - Review, Research and Orchestration Skills"
description: "hyperb1iss/hyperskills on skills.sh: 5.3K combined installs across 28 listings; review, research, planning and terminal UI skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hyperskills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "orchestration", "terminal ui"]
---

# Hyperskills - Setup Guide

**Source:** [hyperb1iss/hyperskills](https://www.skills.sh/hyperb1iss/hyperskills) via skills.sh - 5.3K combined installs across 28 indexed listings; first seen 2026-11-05 (Nov 5, 2026 evening sweep)
**GitHub:** 36 stars, MIT licence, last pushed 2026-11-05, 14 skill directories under `skills/<name>/SKILL.md`, with a `.claude-plugin` marketplace manifest plus `AGENTS.md` and `CLAUDE.md` at the root
**Category:** Agent craft: cross-model review, PR review, research, orchestration and terminal UI design skills
**Quality Tier:** 🟡 Yellow - Gen Agent Trust Hub Warns on the ty listing and leaves demo-reel unrated; MIT, 36 stars.

Hyperskills is a small, opinionated library from Hyperbliss Technologies. Its README states the test for admission directly: a model does not need a tutorial for every tool it touches, so the collection carries only the parts that are easy to miss, such as preserving another worker's edits during Git surgery, telling a review finding apart from a plausible story, or verifying a generated artifact at its destination.

That leaves 14 skills in two groups. The process skills (brainstorm, research, plan, implement, orchestrate, hyper-pr-review, cross-model-review, super-good-pr, deslop, dream, codex-imagegen, demo-reel) cover decisions and evidence and deliberately avoid prescribing agent counts, approval rituals or a fixed pipeline. The domain skills stay narrow: `git` for rebase, stacked branch and worktree work, and `tui-design` for terminal interfaces. Skills load independently, and the README notes that Sibyl adds durable project memory when it is present.

## Installation

Claude Code installs the whole set as a plugin:

```text
/plugin marketplace add hyperb1iss/hyperskills
/plugin install hyperskills@hyperb1iss
```

The skills CLI installs everything, or one skill by name:

```bash
npx skills add hyperb1iss/hyperskills --all
npx skills add hyperb1iss/hyperskills --skill implement
```

For local development, clone and use the Makefile:

```bash
git clone https://github.com/hyperb1iss/hyperskills.git
cd hyperskills
make install
```

The installer links each skill into `~/.agents/skills` and `~/.claude/skills`, and backs up existing directories before replacing them. Installing the plugin or updating the checkout does not remove older standalone copies of skills the project has since retired, so inspect those copies by hand.

## What It Provides

Seven listings clear the 100-install bar; the repository ships 14 skill directories in total.

| Skill | Installs | Use For |
|---|---|---|
| tui-design | 1,316 | Terminal interface design: layout, visual hierarchy, Unicode width, fallback rendering, keyboard access, resize behaviour and terminal restoration |
| orchestrate | 668 | Partitioning independent work, defining ownership beyond file paths, worker and reviewer briefs, integrating results against the original request |
| research | 645 | Evidence gathering with source lineage, contradiction tracking and benchmark comparability, stopping when the remaining uncertainty would not change the action |
| codex-review | 614 | An early Codex-driven review listing with no counterpart directory in the current `skills/` tree; the current review skills are hyper-pr-review and cross-model-review |
| brainstorm | 612 | Exploring an open product or architecture question before choosing an approach, treating the user's hunch as a hypothesis |
| plan | 605 | Turning requirements into dependency-aware tasks with observable completion criteria, tests kept with the behaviour they verify |
| implement | 577 | Making a focused change and verifying it where another component consumes it, with error diagnosis, test receipts and compatibility checks |

The remaining 21 indexed listings range from 1 to 39 installs.

## Why This Matters for Hermes Agents

Most agent guidance fails in the same place: it describes a workflow instead of the decision that workflow exists to protect. These skills are written the other way round. `implement` asks for verification where another component consumes the change, not at the point the change was written. `research` stops when the remaining uncertainty would not change the action. `hyper-pr-review` requires each finding to be explained as a concrete cause and consequence, which is a test an agent can fail.

The review pair is the strongest argument for the set. `cross-model-review` covers the mechanics of getting an independent opinion out of another model, including CLI discovery, process handles, output capture, permissions and billing intent, and then insists that agreement still needs proof. `hyper-pr-review` covers doing the review yourself, tracing changed behaviour and actual callers and trying to disprove each candidate finding. A Hermes agent that delegates review but never performs it, or performs it but never validates the findings, will get caught by one of the two.

`orchestrate` is the piece that matters once a Hermes run fans out. It defines ownership beyond file paths, includes lifecycle tracking and artifact verification, and makes incomplete work visible rather than quietly rounding it up. The README is explicit that agent count follows useful parallelism and available capacity, which keeps the skill from turning into a licence to spawn workers.

`tui-design` is the only visual skill and it is unusually concrete: Unicode width, fallback rendering, resize behaviour and terminal restoration are the failure modes that make a terminal UI unreadable or leave a shell broken after exit. `demo-reel` closes the loop by treating a product video as an acceptance test, where every shot is a test and a failed take opens a fix lane.

## Usage

| You say | What happens |
|---|---|
| "/hyperskills:brainstorm should this be a queue or a cron?" | The agent separates stated requirements from inferred preferences and names the experiment that would settle the choice |
| "/hyperskills:research what changed in the ChromaDB metadata filters?" | Runs a targeted lookup with source lineage and contradictions recorded, then makes a call if the evidence supports one |
| "/hyperskills:plan the migration to the new vector backend" | Produces dependency-aware tasks with observable completion criteria and enough context for another worker to resume |
| "/hyperskills:implement add retry to the ingest job" | Makes the change and verifies it at the consumer, with a test receipt rather than a claim |
| "/hyperskills:hyper-pr-review this branch" | Traces changed behaviour and callers, tries to disprove each candidate finding, and groups repeated symptoms under one remedy |
| "/hyperskills:cross-model-review this diagnosis" | Launches an independent review through another model's CLI, captures the output, and dispositions findings on evidence |
| "/hyperskills:tui-design the status dashboard" | Design guidance for layout, focus, keybindings, resize handling and terminal restoration |

## Verification

Fetch one skill entrypoint from the branch the installer uses:

```bash
curl -fsSL https://raw.githubusercontent.com/hyperb1iss/hyperskills/main/skills/tui-design/SKILL.md | head -5
```

It should open with `name: tui-design` and a description naming TUI design, layout and terminal accessibility. Then confirm what landed locally:

```bash
ls ~/.claude/skills
ls ~/.claude/skills/tui-design
```

The first listing should include the 14 skill directories the README badge advertises; the second should show `SKILL.md` and any `references/`, `scripts/` or `assets/` the skill declares. Run `make check` in a clone if you want the repository's own validator, which parses manifests and frontmatter and checks that declared reference files exist.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| tui-design | Pass | Pass | Pass |
| tilt | Pass | Pass | Pass |
| ty | Warn | Pass | Pass |
| platform | Pass | Pass | Pass |
| demo-reel | ? | Pass | Pass |

Two sampled results are not clean. Gen Agent Trust Hub Warns on `ty`, which is one of the retired Python tooling skills that version 3.11 removed from the tree, so the warning attaches to an indexed listing rather than to a directory you would install today. `demo-reel` has no Gen Agent Trust Hub rating in the sample; it is also the one skill that ships executable scripts, for deterministic 4K browser capture, sandboxed agent takes and MP4 verification, and it needs ffmpeg plus Node and Playwright for the browser path.

## Limitations

- Snapshot data, verified 2026-11-05: 5,348 combined installs across 28 indexed listings; 36 GitHub stars; MIT; last pushed 2026-11-05. Counts drift over time.
- The install index outruns the tree. `uv`, `ruff`, `ty`, `uv-build` were removed in version 3.11 and Tilt was retired in 3.12, yet their listings still carry installs. `codex-review` (614) has no directory in the current `skills/` tree at all.
- Yellow tier follows the sampled audits: Gen Agent Trust Hub Warns on `ty` and has no rating for `demo-reel`, while every Socket and Snyk result in the sample is a Pass.
- It is a young, small repository: 36 stars, one maintainer organisation, and a changelog that shows the skill set still being actively reshaped.
- `demo-reel` needs ffmpeg, and its browser capture adds Node and Playwright. The sandboxing in that skill is described by its own README as brakes rather than isolation.
- The skills assume an agent that reads them selectively. Loading all 14 entrypoints at once spends context on procedures the current task will not use.

## Related

- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)
- [Git PR Review (skills.sh) - Automated PR description](/hermes/skills/catalog/git-pr-review-skills-sh-setup)
- [Claude Code Skills - Agentic Coding & Skill](/hermes/skills/catalog/claude-code-skills-setup)

## Pro Tips

- Start from the uncertainty, not from the pipeline. The README's own composition table sends a clear bug straight to `implement` and an open product question through `brainstorm` first.
- Use `cross-model-review` for the second opinion and `hyper-pr-review` for the first pass. Running both on the same diff without disposing of findings produces two reports and no decision.
- Ask for the evidence, not the verdict. Every process skill here is built to keep unfinished checks visible next to a conclusion, so a summary that omits them is a signal the skill was not followed.
- Keep retired copies out of the skills directory. The installer backs up and replaces, but it does not delete standalone copies of skills the project has since removed, and stale duplicates confuse routing.
- Pair `tui-design` with a real terminal at a narrow width. Resize and fallback behaviour is where the guidance earns its keep and where a generated interface breaks first.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
