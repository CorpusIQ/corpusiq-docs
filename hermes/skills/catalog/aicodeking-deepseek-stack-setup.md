---
title: "DeepSeek Stack - Agent Skills Collection Setup"
description: "aicodeking/deepseek-stack - 17.3K combined installs: agent skills that make DeepSeek models plan, verify, and ship like frontier models."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/aicodeking-deepseek-stack-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "deepseek", "coding agent", "verification"]
---

# DeepSeek Stack - Setup Guide

**Source:** [aicodeking/deepseek-stack](https://www.skills.sh/aicodeking/deepseek-stack) via skills.sh - 17.3K combined installs across 29 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 evening sweep)
**GitHub:** [aicodeking/deepseek-stack](https://github.com/aicodeking/deepseek-stack) - 344 stars, MIT license, last pushed Oct 28, 2026, main branch; 29 skill folders under skills/<name>/SKILL.md.
**Category:** Developer Workflows (DeepSeek / Coding Agents)
**Quality Tier:** 🟡 Yellow - 15 sampled skills: thirteen pass all three checks and two carry a single Snyk Warning; no Fails.

aicodeking/deepseek-stack is a collection of 29 agent skills that make DeepSeek models (V4.1 Flash, V4 Pro) plan, verify, and ship like a much more expensive frontier model. Cheap models usually fail in the same few ways: they skip the plan, claim a fix works without running it, retry a broken idea, and drift on long runs. Each skill here closes one of those gaps with a short loop, a hard stop condition, and a demand for real evidence.

The skills work in any harness that reads SKILL.md files: Claude Code, Codex, Cline, OpenCode, PandaCode, and others. Installation is a one-liner through npx skills, and any single skill can be installed on its own.

## Installation

```bash
npx skills add aicodeking/deepseek-stack
```

Add `-g` to install for every project. To install one skill only:

```bash
npx skills add aicodeking/deepseek-stack --skill ds-verify-loop
```

Manual install: copy `skills/*` into `~/.claude/skills/`, `~/.codex/skills/`, or your harness's skills folder. Not sure where to start? Run `/ds-help`.

## What It Provides

skills.sh publishes per-skill install counts for all 29 indexed listings. The 9 most-installed skills are listed below; the remaining 20 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| ds-verify-loop | 641 | Run edit, real check, read the actual error, fix the root cause, rerun until the check passes or the cap is hit |
| ds-plan-loop | 620 | Write a numbered plan with a check per step, critique it once, then build one step at a time |
| ds-mode | 620 | Always-on working style for DeepSeek agents: restate, read before editing, small verified steps, evidence before done |
| ds-unstick | 618 | Break out of a repeating failure: name the shared assumption, test it, pick a different approach |
| ds-context-reset | 613 | Keep a PROGRESS.md for long tasks and continue in a fresh session when context gets long or stale |
| ds-principles | 606 | Compact engineering rules for design, debugging, verification, and delegation, each with a trigger |
| ds-blast-radius | 600 | Find what a change could break outside its own diff, then prove the key safety fact by running real code |
| ds-unslop | 598 | Remove AI writing tells from prose and code comments, then rewrite in plain, specific English |
| ds-review-loop | 598 | Run an author and a fresh-context reviewer until both agree the change is correct, max four rounds |

The remaining 20 indexed listings range from 580 to 597 installs.

## Why This Matters for Hermes Agents

These skills encode the discipline cheap models lack. A Hermes agent running on DeepSeek (V4.1 Flash or V4 Pro) gets concrete loops instead of prompts: ds-plan-loop forces a numbered plan with a check per step, ds-verify-loop demands a real test or build pass before claiming done, and ds-unstick breaks the retry-the-same-fix cycle by naming the shared assumption. ds-mode is the always-on working style that pairs with any harness, and ds-context-reset gives long-running agents a PROGRESS.md handoff for fresh sessions. The collection is MIT-licensed, every listing has a matching SKILL.md in the tree, and the Ship skills (ds-pr, ds-ship, ds-ready) plus ds-jury, ds-best-of-n, and ds-swarm lean on subagents or a second model, which a Hermes multi-agent setup already provides.

## Usage

| You say | What happens |
|---|---|
| Plan this change before I start coding | Uses ds-plan-loop to write a numbered plan with a check per step, critique it once, then build step by step |
| Keep running this until it actually passes | Uses ds-verify-loop to edit, run the real check, read the error, and fix until it passes or the cap is hit |
| I keep hitting the same error | Uses ds-unstick to name the assumption behind the failed fixes and pick a different approach |
| What could this change break? | Uses ds-blast-radius to find breakage outside the diff and prove safety by running code |
| Review this PR | Uses ds-review-loop with an author and a fresh-context reviewer until both agree |
| Clean up the AI-sounding prose | Uses ds-unslop to rewrite in plain, specific English |
| Start a fresh context for this long task | Uses ds-context-reset to hand off a PROGRESS.md and continue in a new session |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/aicodeking/deepseek-stack/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/aicodeking/deepseek-stack/main/skills/ds-verify-loop/SKILL.md | head -40
```

Both URLs return 200. After installing, run `/ds-help` to confirm the skills are wired in, and review each skills/<name>/SKILL.md before relying on it.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ds-verify-loop | Pass | Pass | Pass |
| ds-plan-loop | Pass | Pass | Pass |
| ds-mode | Pass | Pass | Pass |
| ds-unstick | Pass | Pass | Pass |
| ds-context-reset | Pass | Pass | Pass |
| ds-principles | Pass | Pass | Pass |
| ds-blast-radius | Pass | Pass | Pass |
| ds-unslop | Pass | Pass | Pass |
| ds-review-loop | Pass | Pass | Pass |
| ds-help | Pass | Pass | Pass |
| ds-design | Pass | Pass | Pass |
| ds-design-audit | Pass | Pass | Warn |
| ds-ledger | Pass | Pass | Pass |
| ds-blueprint | Pass | Pass | Pass |
| ds-lessons | Pass | Pass | Warn |

Thirteen of the 15 sampled skills pass all three checks; ds-design-audit and ds-lessons each carry a single Snyk Warning. No Fails.

## Limitations

- Snapshot data, verified Nov 25, 2026: 17,290 combined installs across 29 indexed listings; 344 GitHub stars; MIT license; last pushed Oct 28, 2026. Counts drift over time.
- Fifteen of the 29 listings were security-sampled; the other 14 have no published verdict on skills.sh.
- ds-jury, ds-best-of-n, and ds-swarm need subagents or a second model; without them, the attempts run one after another in fresh contexts.
- The Ship skills need the gh CLI, signed in, and ds-watch-pr needs python3 for its watch script.

## Related

[Self-Improving Agent - Universal Agent Self-Evolution](/hermes/skills/catalog/self-improving-agent-setup) | [Caveman Skills - Agent Coding Workflow Suite Setup](/hermes/skills/catalog/caveman-skills-setup) | [Vigiles - Agent Harness Quality Suite Setup](/hermes/skills/catalog/vigiles-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `/ds-help` first to see which skill fits a task; it explains how the suite fits together.
- Use ds-mode for every coding task; it is the always-on working style and stops drift before it starts.
- Spend DeepSeek's cheap tokens on quality: ds-best-of-n, ds-review-loop, and ds-jury cost little and catch a lot.
- Use thinking mode at max effort for planning and review; it matters more than any skill.
- Pair a stronger planner with DeepSeek as the implementer if your harness supports separate plan and act models.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
