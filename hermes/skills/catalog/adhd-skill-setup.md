---
title: "ADHD Skill - Divergent Thinking for Agents"
description: "uditakhourii/adhd on skills.sh: 7.6K combined installs; parallel divergent ideation with scoring, trap pruning and deepening for coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/adhd-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "ideation", "tree of thought", "architecture decisions"]
---

# ADHD Skill - Setup Guide

**Source:** [uditakhourii/adhd](https://www.skills.sh/uditakhourii/adhd) via skills.sh - 7.6K combined installs across 1 indexed listing; first seen 2026-11-06 (Nov 6, 2026 evening sweep)
**GitHub:** 4,509 stars, MIT, last pushed 2026-10-25, a single SKILL.md at skills/adhd/ with a TypeScript CLI and bench suite beside it
**Category:** Creative reasoning for agents: tree-of-thought fan-out under fixed cognitive frames, scoring, pruning and deepening
**Quality Tier:** 🟢 Recommended - MIT licence, 4,509 stars, Pass on all three scanners, a single well-scoped skill and a documented cost model.

One skill, one loop, and a clear argument for why the loop exists. Linear chain-of-thought anchors on whatever it says first. Tree-of-thought widens the search but still walks a single shared context, so the anchoring survives across branches. This skill treats that as an architectural problem rather than a prompting one: it spawns isolated reasoning processes under deliberately distorted cognitive frames, with zero shared context during divergence, then runs a separate critic pass to score, cluster, prune traps and deepen the survivors.

`skills/adhd/SKILL.md` is 215 lines and holds the whole method: a pre-flight gate, a 15-frame table, two strict phases, an output shape, an anti-pattern list, calibration guidance and a cost section. The repository also ships the reference implementation as an npm package, `adhd-agent`, with a CLI and a library entry, plus a bench suite and a preprint.

The pre-flight gate is the part most skills skip. Before spending anything, the skill checks whether the request is open-ended, high-stakes and openly phrased. If a senior engineer would give one canonical answer, or the user said "quick", "standard", "canonical", "just" or "one-line", it aborts and answers directly, optionally appending one sentence offering the wider run. Explicit invocation with `/adhd` skips the gate entirely, because the user already opted in.

## Installation

The README's install is one command and auto-detects the agent, covering Claude Code, Cursor, Antigravity, Codex, Cline, Gemini CLI, Windsurf and around 50 more:

```bash
npx skills add UditAkhourii/adhd
```

Then invoke it explicitly, or let it trigger on ideation intents:

```text
/adhd "your problem"
```

The same loop exists as a standalone tool for use outside a skill-aware harness, or in batch. It needs Node 18 or newer:

```bash
npm install -g adhd-agent
adhd "design a rate limiter that survives a leader election"
```

As a library, the loop is importable and returns structured results rather than prose:

```ts
import { run, renderText } from "adhd-agent";

const result = await run({ problem: "How should we shard this queue under bursty load?", framesPerRun: 5, topK: 3 });
console.log(renderText(result));
```

The result carries `shortlist`, `nonObviousPick`, `traps`, `deepened` and `clusters` as separate fields, which is the difference between a brainstorm you can wire into a pipeline and a wall of text you have to re-parse.

## What It Provides

One listing carries the whole thing:

| Skill | Installs | Use For |
|---|---|---|
| adhd | 7,589 | Parallel divergent ideation: five isolated frames, six ideas each, scored on novelty, viability and fit, clustered, with traps flagged and the top three deepened |

The single indexed listing clears the 500-install threshold and appears in the table above.

What the listing describes is a two-phase loop with a hard wall between the phases. Phase 1 picks five frames from the 15-frame table, biased toward engineering tags for code-shaped problems with at least one wild frame for range, and spawns five parallel agent calls. Each branch receives only the problem, any user context and its frame's vantage prompt, under a system instruction that forbids evaluation and bans the first three obvious answers. The stated invariant is that the calls must be parallel and isolated: serialising them, or passing one branch's output as context to another, collapses the method into a wider single thought.

Phase 2 turns the critic on. Ideas are scored 0 to 10 on novelty, viability and fit, with attractive traps flagged and given a one-line reason. Surviving ideas are clustered into three to six groups by underlying angle rather than surface keywords, then ranked by a weighted score of 0.35 novelty, 0.40 viability and 0.25 fit. The top three, excluding traps, get a deepening pass each: a sketch of how the idea works, its load-bearing risk, the first concrete step a builder would take, and three to five child ideas.

The output shape is prescribed. A brief, the full pool grouped by cluster with score chips, a shortlist of two to four with reasons and the non-obvious pick marked, the three deepened branches, and one closing provocation. That structure is the point: the skill's own anti-pattern list names walls of equally weighted prose and "here are 20 ideas, you decide" as failure modes.

## Why This Matters for Hermes Agents

The failure this addresses is real and easy to observe in practice. Ask an agent for retry strategy options and the first three answers will be staged timeouts, exponential backoff and hedged parallel requests: correct, textbook and identical to what a senior engineer says in thirty seconds. The useful fourth answer, the one that questions whether the slow model is the right model at all, only shows up if something forces the search past the obvious.

Hermes runs multi-agent work already, which makes the isolation invariant cheap to satisfy. Each divergent branch needs a fresh context, and a subagent call gives exactly that. The skill is written for the agent that has a Task tool, and its anti-patterns call out the fake version explicitly: writing the branches sequentially in one context is not the method, it is a wider single thought with extra steps.

The critic separation is the other piece worth borrowing even if you never install the skill. A generator that is also scoring its own output hedges, and a critic that is present during generation strangles range. Splitting them into two phases, with a scoring rubric and named trap reasons, is a pattern that improves almost any multi-agent design review.

The cost model is stated instead of hidden: roughly 10 agent calls per run, 30 to 90 seconds of wall clock, and 5 to 10 times the tokens of a single answer. For an architecture decision or an API surface, that is cheap. For naming a helper function, it is waste, and the pre-flight gate is what stops you paying it.

## Usage

| You say | What happens |
|---|---|
| "/adhd how should we shard this queue under bursty load" | Skips the gate, runs five isolated frames, scores and clusters, then deepens the top three |
| "ADHD mode: we need to pick a public API surface for the SDK" | Classifies as a high-stakes open decision and runs the full loop |
| "Give me a few ways to handle offline sync" | The open phrasing triggers the method without the explicit command |
| "Quick, rename this variable" | Pre-flight aborts, because "quick" signals a direct answer, and you get the rename |
| "This design feels obvious, push past the textbook answer" | Frames are biased toward wild tags to escape the default cluster |
| "What are the traps in these options" | The critic pass names each trap with a one-line reason before any deepening |
| "Name a product in this space" | Frame selection leans on the 10-year-old, markets and inversion frames rather than engineering tags |

## Verification

Read the skill before installing it. This path returned 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/uditakhourii/adhd/main/skills/adhd/SKILL.md | head -40
```

It should open with frontmatter naming `adhd` and a MIT licence line, and a description that scopes the skill to parallel divergent ideation, names the frame examples, and tells you to skip it for syntax, lookups, bugs with a known root cause, and closed phrasing.

After install, confirm the skill landed and, if you took the CLI route, that Node is new enough:

```bash
ls ~/.claude/skills/adhd
node --version
adhd "name this function"
```

The directory should hold `SKILL.md`. `node --version` should print 18 or higher, which is the floor the repository declares. The last command is a cheap end-to-end check: it should return a shortlist rather than a single answer, and if it returns one answer, the frames or the parallelism are not working.

For a stricter check of the packaged implementation, the repository ships a test suite and a bench directory with recorded results, so `npm test` in a clone is a fair way to confirm the loop behaves as documented before you trust it in a pipeline.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| adhd | Pass | Pass | Pass |

The skill itself is markdown with no executable content in the reasoning path. The install surface is small, and the optional CLI is a normal npm package with a package lock in the repository.

The real consideration is spend, not code execution. A run fans out five agent calls plus scoring, clustering and three deepening calls, so an agent that triggers the loop casually will multiply your token bill by five to ten without asking. The pre-flight gate exists to prevent that, and the skill is explicit that the cost is per decision point rather than per keystroke.

The second consideration is where the ideas go. Divergent frames including a hostile competitor and an attacker are designed to surface abuse paths, which is useful for threat modelling and awkward if the output is pasted into customer-facing material without review.

## Limitations

- Snapshot data, verified 2026-11-06: 7,589 combined installs across 1 indexed listing; 4,509 GitHub stars; MIT; last pushed 2026-10-25. Counts drift over time.
- Expensive by design. Roughly 10 agent calls and 5 to 10 times the tokens of a single answer per run, with 30 to 90 seconds of wall clock, so it is for decision points and not for routine questions.
- The isolation invariant needs a real subagent primitive. In a harness that cannot spawn fresh contexts, the branches share one and the method degrades to a wider single thought, which the skill's own anti-patterns call a failure.
- Quality is frame-dependent. Five frames chosen from 15 determine what the run can find, and the table is opinionated toward engineering and wild angles rather than, say, regulatory or financial ones.
- The evidence is the maintainer's. The bench, the preprint and the side-by-side comparison in the README are the project's own work, and the adopters list is a list of people who shipped it, not an independent benchmark.
- Only one indexed listing exists, so the 7,589 installs are the entire adoption signal, and there is no second implementation to compare against.

## Related

- [Context Engineering Kit - Prompt and MCP Setup](/hermes/skills/catalog/context-engineering-kit-setup)
- [Superpowers - Agentic Skills Framework & Development](/hermes/skills/catalog/superpowers-setup)
- [Multi-Agent Review - Adversarial Code Review Setup](/hermes/skills/catalog/multi-agent-review-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Invoke it with the command, not with hope. `/adhd` skips the pre-flight gate, and the gate is conservative enough that a politely phrased request often gets answered directly instead.
- Ask for the traps explicitly on a design review. The trap list is where the method earns its cost, because naming why a tempting option fails is cheaper than discovering it in production.
- Re-run the same problem later. Frame selection is meant to vary across sessions, so a second run produces a different candidate set rather than the same shortlist.
- Read the anti-patterns before you judge the output. Ten variations of one idea, or thirty unsorted absurdities, are the two ways this goes wrong, and both are recognisable in seconds.
- Use it at the decision boundary. Pick the architecture, the API surface, the name, the schema; then drop back to a direct answer for everything downstream.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
