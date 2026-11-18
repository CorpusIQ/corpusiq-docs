---
title: "Loopy - Agent Loop Library Setup"
description: "forward-future/loopy: 5.6K combined installs across 2 listings; a skill for finding, adapting, running, and publishing repeatable AI-agent loops."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/loopy-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "agent loops", "workflow automation"]
---

# Loopy - Setup Guide

**Source:** [forward-future/loopy](https://www.skills.sh/forward-future/loopy) via skills.sh - 5.6K combined installs across 2 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 3,249 stars, MIT license, `main` branch, last pushed 2026-09-11, two skills under `skills/` plus the Loop Library website source under `loop-library/`
**Category:** Agent workflows / loop libraries
**Quality Tier:** 🟡 Yellow - 4 Pass and 2 Warn across both listed skills; no Fail.

forward-future/loopy is the Loop Library repository, and it ships two things that are easy to conflate. The Loop Library website is a public catalog of published agent loops; browsing it needs no install. The Loopy skill is an optional installable guide that helps an agent discover, find, audit, repair, adapt, craft, run, debrief, save, and publish loops, checking the live catalog when it recommends or publishes one.

The second indexed listing, loop-library, is a compatibility alias for Loopy, kept for existing installations that invoke the old name. The repository's `loop-library/` directory holds the website source, a site shell plus a Cloudflare Worker; the published loop records live in a database and are not committed to the tree.

## Installation

Install Loopy with npx (Node.js required). Pick one agent:

```bash
npx skills add Forward-Future/loopy --skill loopy --agent codex -g -y
npx skills add Forward-Future/loopy --skill loopy --agent cursor -g -y
npx skills add Forward-Future/loopy --skill loopy --agent claude-code -g -y
```

Or install for all three at once:

```bash
npx skills add Forward-Future/loopy \
  --skill loopy \
  --agent codex \
  --agent cursor \
  --agent claude-code \
  -g -y
```

`Forward-Future/loopy` is the repository, `--skill loopy` selects the skill, `--agent` selects the target runtime, `-g` installs for all projects (drop it for project-only), and `-y` accepts the prompts. If an agent was already open and Loopy does not appear, restart it. The previous `loop-library` name remains as a compatibility alias for existing installs; use `loopy` for all new work.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| loopy | 3,168 | Discover, find, audit, adapt, craft, run, debrief, save, and publish repeatable agent loops. |
| loop-library | 2,444 | Compatibility alias for Loopy; use only for existing installations that invoke loop-library. |

No indexed listings fall below the threshold; all 2 appear above.

The `loop-library/` directory is the Loop Library website source, not a third installable skill. Installing Loopy does not install or host the website; it adds the guided workflow only.

## Why This Matters for Hermes Agents

Most agent prompts ask for a single action. Loopy is built around the loop: an instruction with a check, a next step, and a stopping point, so the agent learns from each result instead of guessing. For a Hermes agent that turns open-ended work into repeatable, verifiable work: run one bounded action, apply the acceptance check, keep the change only if it helps, and stop at success or a blocker.

The skill also closes the loop on the loop itself. Debrief analyzes a run receipt and recommends the smallest evidence-backed change; Audit flags weak checks or unsafe authority before a loop runs. And because loops are deliberately bounded, Loopy hands control back to you at approval boundaries instead of running forever.

## Usage

| You say | What happens |
|---|---|
| "Find a loop for keeping our docs current" | Loopy searches the live catalog and recommends up to three published loops. |
| "Analyze this repo for repeated work" | Discovery inspects the codebase and turns the strongest qualified candidate into a bounded loop. |
| "Run the Overnight Docs Sweep here" | Loopy runs the loop in bounded passes and returns an evidence-backed receipt. |
| "Audit this loop" | Loop Doctor flags weak checks or unsafe actions and repairs only material problems. |
| "Interview me to craft a loop" | Loopy asks one question at a time and produces a bounded loop when no catalog fit exists. |
| "Save this loop to the project" | Loopy appends it to LOOPS.md for reuse in later sessions. |

## Verification

Confirm both skill files exist on the `main` branch before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/forward-future/loopy/main/skills/loopy/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/forward-future/loopy/main/skills/loop-library/SKILL.md
```

Both skills live at `skills/<name>/SKILL.md`. After install, restart any already-open agent if Loopy does not appear.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| loopy | Pass | Pass | Warn |
| loop-library | Pass | Pass | Warn |

The sample covers both indexed listings, so this is a full census; both skills carry a Snyk Warn and pass Gen Agent Trust Hub and Socket.

## Limitations

- Snapshot data, verified 2026-11-17: 5,612 combined installs across 2 indexed listings; 3,249 GitHub stars; MIT; last pushed 2026-09-11. Counts drift over time.
- loop-library is a compatibility alias, not a second capability; its installs reflect the old name. Install loopy for new work.
- Installing Loopy does not install or host the Loop Library website; the site runs separately at signals.forwardfuture.com.
- Published loop records are not in the Git tree; they live in a Cloudflare Durable Object database, so the repository alone does not contain the loop catalog.
- Both skills carry a Snyk Warn verdict on skills.sh.

## Related

- [Loop Maker Setup](/hermes/skills/catalog/loop-maker-setup)
- [Perfectloop Setup](/hermes/skills/catalog/perfectloop-setup)
- [Coleam00 Skills - PIV Loop & AI Layer Setup](/hermes/skills/catalog/coleam00-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install only loopy; loop-library exists for existing installations that still invoke the old name.
- Browse the Loop Library website, or point an agent at its agent guide, without installing anything.
- Invoke Loopy explicitly (/loopy, $loopy, or /skills) for the most predictable start.
- Saved loops go to LOOPS.md and are treated as untrusted reference data, not permission to run anything.
- Loopy never starts schedules, publishes, or sends messages on its own; approvals stay with you.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
