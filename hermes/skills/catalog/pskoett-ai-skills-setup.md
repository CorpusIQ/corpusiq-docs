---
title: "PSKoett AI Skills - Self-Improving Agent Loops"
description: "pskoett/pskoett-ai-skills on skills.sh: 6.5K combined installs across 25 listings; self-improving agent loops, evals and context handoffs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pskoett-ai-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "self-improvement", "evals", "context engineering"]
---

# PSKoett AI Skills - Setup Guide

**Source:** [pskoett/pskoett-ai-skills](https://www.skills.sh/pskoett/pskoett-ai-skills) via skills.sh - 6.5K combined installs across 25 indexed listings; first seen 2026-11-05 (Nov 5, 2026 evening sweep)
**GitHub:** 328 stars, no LICENSE file in the repository root, last pushed 2026-10-27, 72 SKILL.md directories spread across skills/, agent-plugin/skills/, plugin/skills/ and .agents/skills/
**Category:** Self-improving agents: plan interviews, context surfing, evals and self-healing loops for long working sessions
**Quality Tier:** 🟡 Review - no LICENSE file in the repo root, and 4 of the 5 sampled skills.sh audits carry a Socket or Snyk Warn (mcp-builder, simplify-and-harden-ci, learning-aggregator-ci, context-decay).

PSKoett AI Skills is one maintainer's working set for making a coding agent improve between sessions rather than restart from zero each time. The repository follows the Agent Skills specification and also ships an Agent Plugins 1.0 package, so the same content installs as loose skills, as a Claude Code plugin, as a Codex repo-local plugin or through the GitHub Copilot CLI. Everything is markdown plus a handful of shell helpers.

The design is two feedback loops. The inner loop catches failures inside a session: plan, frame intent, verify, heal, review. The outer loop uses what went wrong to change later sessions: aggregate learnings, promote approved rules into project instructions, turn them into regression evals, then surface them at the start of the next run. Each skill also works alone, so the loops are a recommended combination rather than a dependency chain.

## Installation

Claude Code takes the plugin from the repo's own marketplace. Run each command inside Claude Code:

```text
/plugin marketplace add pskoett/pskoett-skills
/plugin install pskoett-ai-skills@pskoett-skills
/reload-plugins
```

The GitHub Copilot CLI installs the same bundle from its own manifest:

```bash
copilot plugin marketplace add pskoett/pskoett-skills
copilot plugin install pskoett-ai-skills
```

For Codex, open the repository in Codex, restart it after pulling so the repo marketplaces reload, then pick the `pskoett skills` marketplace and install `pskoett-ai-skills`. Codex reads the marketplace from `.agents/plugins/marketplace.json` and the manifest from `plugin/.codex-plugin/plugin.json`.

Single skills install with the GitHub CLI, which needs version 2.90.0 or later:

```bash
gh skill install pskoett/pskoett-skills self-improvement
gh skill install pskoett/pskoett-skills verify-gate --agent codex --scope user
```

Or with the Agent Skills CLI, pointing at the skill directory inside the repo:

```bash
npx skills add pskoett/pskoett-skills/skills/simplify-and-harden
```

The manual route is a clone and a copy:

```bash
git clone https://github.com/pskoett/pskoett-skills.git
cp -r pskoett-skills/skills/verify-gate ~/.claude/skills/
```

An Agent Plugins 1.0 client or packager can instead be pointed straight at `agent-plugin/`, whose entrypoint is `agent-plugin/plugin.json`.

## What It Provides

Ten of the 25 indexed listings clear 100 installs. The top of the table is the review and learning layer, not the planning layer, which is a fair signal of what people keep installed.

| Skill | Installs | Use For |
|---|---|---|
| self-improvement | 2,076 | Capturing corrections, errors, outdated knowledge and feature requests in .learnings/, then promoting approved patterns into CLAUDE.md, AGENTS.md or a new skill |
| self-improvement-ci | 535 | The same capture loop headless in GitHub Agentic Workflows, turning recurring PR check failures into learning candidates and prevention rules |
| simplify-and-harden | 521 | A bounded post-completion pass over finished work: simplify, harden, micro-document and re-verify before the agent signals done |
| agent-teams-simplify-and-harden | 509 | Team variant of the simplify-and-harden review; the index carries it but the current tree has no directory and the README no row for it |
| plan-interview | 481 | A structured pre-planning interview over technical constraints, scope, risk tolerance and success criteria, writing a plan file under docs/plans/ |
| intent-framed-agent | 432 | Recording the intended outcome at execution start and watching for scope drift until the task resolves |
| simplify-and-harden-ci | 387 | The review pass as a gh-aw pull request scan that posts structured findings and can block merges on critical or advisory classes |
| dx-data-navigator | 355 | Indexed listing with no directory and no README row in the current tree; the name is all the repository discloses |
| context-surfing | 261 | Watching context health on long sessions, running one cold-context review when self-recovery is uncertain, and writing a handoff file on real drift |
| skill-pipeline | 106 | Classifying each task and dispatching the right skills at the right depth across standard, orchestrated-batch, CI and outer-loop variants |

The remaining 15 indexed listings range from 5 to 93 installs: skill-creator (93) and mcp-builder (89) at the top, session-context (5) and context-decay (5) at the bottom.

## Why This Matters for Hermes Agents

Most agent failures are not reasoning failures, they are bookkeeping failures. The command that failed twice in the same way, the correction the user already gave in a previous session, the file that was edited without re-running the test. A Hermes agent with no persistent layer repeats all three, and the second and third repetitions are what erode trust.

This suite puts a named owner on each of those gaps. `self-improvement` writes the entry, `learning-aggregator` finds the pattern, `self-improvement` promotion turns an approved pattern into a rule in the project instructions, and `eval-creator` turns the rule into a regression case. A rule that is not eval-backed is a suggestion; a rule with an eval is a constraint.

The verification half is the part that pays back fastest. `verify-gate` runs the project's compile, test and lint commands between implementation and review, with up to three attempts per phase, and hands failures to `self-healing`, which has to prove the fix before it records a HEAL entry. That converts "I fixed it" into a claim with evidence attached.

The pipeline gives a Hermes agent a depth dial rather than a single mode. A typo fix loads nothing, an isolated bug fix loads verification and review, a multi-file feature adds intent framing and session context, and a long-running job adds context surfing for handoffs. Loading fewer skills for smaller tasks is the difference between a suite that helps and a suite that taxes every turn.

It is also honest about its own limits, which is rarer than it should be. `session-context` is labelled beta with a stated budget of about 600 tokens and no guarantee of a useful match; `context-surfing` explicitly says not to auto-activate on a medium task that merely has a plan. Those hedges are the reason the suite is usable in a real session.

## Usage

| You say | What happens |
|---|---|
| "Interview me before we build this" | plan-interview runs the structured interview and writes a plan file to docs/plans/ before any codebase exploration |
| "Stay on scope while you refactor the auth layer" | intent-framed-agent records the frame, then flags work that drifts outside it |
| "Why did the build fail twice this week?" | self-healing reads the HEAL entries it filed, learning-aggregator groups them by pattern |
| "Run the checks before you tell me it is done" | verify-gate runs compile, test and lint, loops through self-healing on failure, and only then allows review |
| "Review what you just wrote and tighten it" | simplify-and-harden runs simplify, harden, document and re-verify as four bounded phases |
| "What did we decide about the migration last month?" | session-context searches prior sessions and returns a short cited brief, or says nothing useful matched |
| "We are running out of context, hand this off" | context-surfing writes a handoff file under .context-surfing/ and the next session picks it up |

## Verification

Confirm the skill index the installer resolves before trusting the bundle:

```bash
curl -fsSL https://raw.githubusercontent.com/pskoett/pskoett-ai-skills/main/skills/self-improvement/SKILL.md | head -5
```

It should open with `name: self-improvement` and a description naming corrections, errors and feature requests. Then confirm what landed on disk:

```bash
ls ~/.claude/skills
```

Each installed skill is a directory holding SKILL.md, with `scripts/` only where the skill ships helpers, as `self-improvement` and `context-surfing` do. If you installed the Claude Code plugin instead, the skills arrive together with the hooks, and the README's settings block adds `activator.sh`, `error-detector.sh`, `handoff-checker.sh` and `pre-flight.sh` to `.claude/settings.json`.

Hook output is described as roughly 50 to 200 tokens, and silent when there is nothing to report. If you see no reminder text after a prompt, that is the expected state, not a broken install.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| self-improvement | Pass | Pass | Pass |
| simplify-and-harden-ci | Pass | Warn | Warn |
| mcp-builder | Pass | Pass | Warn |
| learning-aggregator-ci | Pass | Warn | Warn |
| context-decay | Pass | Warn | Pass |

Two things carry more risk than the verdict table shows. First, the repository has no LICENSE file, so there is no explicit grant to use, modify or redistribute it; treat it as all rights reserved until the author adds one. Second, this is not a markdown-only suite. The Claude Code integration registers shell hooks that execute `activator.sh`, `error-detector.sh` and `handoff-checker.sh` on prompt submit, session start and tool failure, and `extract-skill.sh` writes new skill content. Read those four scripts before enabling the hooks, and prefer the skill-only install if you do not want command execution on every turn.

The CI variants are described as no code mutation in CI, review of changed files only, with gating through GitHub Agentic Workflows. That keeps them out of your local repository, but it also means the gate decisions come from a workflow definition you should read in the repo rather than from the skill text.

## Limitations

- Snapshot data, verified 2026-11-05: 6,493 combined installs across 25 indexed listings; 328 GitHub stars; no LICENSE file; last pushed 2026-10-27. Counts drift over time.
- No LICENSE file means no licence grant. Nothing in the repository states terms for reuse, so redistribution inside a product needs the author's permission.
- The index outruns the tree in two places: `dx-data-navigator` and `agent-teams-simplify-and-harden` carry install counts but have no matching directory anywhere in the repository and no README row.
- The README's install commands name `pskoett/pskoett-skills` while skills.sh indexes `pskoett/pskoett-ai-skills`. The GitHub CLI and npx commands above are the README's spellings; if one fails, check whether the rename has been completed.
- Hook dispatch is the fragile layer. The README states that installation was checked on Claude Code 2.1.280, Copilot CLI 1.0.99-2 and Codex 0.160.1, and that actual hook dispatch, Copilot and Codex runtime agent registration, and remote marketplace copying remain unverified.
- `session-context` is beta. It needs authorised history tools, starts at two search rounds and three sessions, and has not been measured against a no-history baseline. `skill-tester` and `skill-tester-ci` exist in `skills/` but appear in no README table.

## Related

- [skill-creator - Anthropic's Skill Creation Framework](/hermes/skills/catalog/skill-creator-setup)
- [Advanced Skill Creator - Custom Skill Generation Setup](/hermes/skills/catalog/advanced-skill-creator-setup)
- [Context Engineering Kit - Prompt and MCP Setup](/hermes/skills/catalog/context-engineering-kit-setup)

## Pro Tips

- Start with the outer loop alone: `self-improvement` plus a weekly `learning-aggregator` run. It is the cheapest half to adopt and it produces the evidence the rest of the suite depends on.
- Keep promotions human-approved. The README's encode stage shows diffs and waits; letting an agent write its own rules into AGENTS.md unsupervised is how a project instruction file fills with noise.
- Install skills individually rather than the plugin if you do not want hooks. Every skill works standalone, and `gh skill install` targets the right directory per host.
- Read `skill-pipeline` before installing the rest. It is the map of when each skill should fire, and it is cheaper to read one routing document than to discover the triggers by trial.
- Treat `verify-gate` as the boundary, not the afterthought. The suite's own rule is that review only starts when checks pass, and that only holds if the gate runs on every task the pipeline classifies as non-trivial.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
