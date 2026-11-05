---
title: "Julius Brussee Skills - Agent Coding Drills"
description: "juliusbrussee/skills on skills.sh: 18.8K combined installs across 9 listings; terse output, calibrated critique, UI craft and review-gated loops."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/juliusbrussee-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "agent workflow", "code review", "writing"]
---

# Julius Brussee Skills - Setup Guide

**Source:** [juliusbrussee/skills](https://www.skills.sh/juliusbrussee/skills) via skills.sh - 18.8K combined installs across 9 indexed listings; first seen 2026-11-04 (Nov 4, 2026 evening sweep)
**GitHub:** 175 stars, MIT licence, last pushed 2026-08-07, 8 directories at skills/<name>/SKILL.md
**Category:** Agent working discipline: output compression, calibrated critique, UI craft, spec-driven build loops and context monitoring
**Quality Tier:** 🟡 Beta - Snyk Fail on caveman; MIT; 175 stars.

This repository holds eight personal agent skills that change how an agent works rather than what it knows. Caveman compresses replies, Interface Kit sets UI quality, Grill Me calibrates critique, Loop Factory enforces a spec-driven loop, Junior to Senior upgrades plans, Deslopify strips AI writing tells, Context Canary surfaces context drift and The Last 20% finishes the experiential layer.

The README states the intent plainly: agents should be terse when talking, precise when building interfaces, calibrated when challenging plans and disciplined when running build loops. skills.sh indexes nine listings for the repo, one more than the number of SKILL.md directories, so one listing has no matching folder.

## Installation

The README's quickstart installs the pack through the skills.sh CLI:

```bash
npx skills@latest add JuliusBrussee/skills
```

The listing on skills.sh shows the same install in its short form:

```bash
npx skills add juliusbrussee/skills
```

The installer asks which skills you want, and the README names Claude Code, Codex, Gemini, Cursor, Windsurf, Cline and Copilot as targets, plus any agent the installer supports.

Caveman has its own canonical installer, which the README lists separately:

```bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash
```

Read that script before running it. It is fetched from a different repository than the one being installed here, and piping a remote file into bash executes it without review.

## What It Provides

All 9 indexed listings are above the 500-install threshold.

| Skill | Installs | Use For |
|---|---|---|
| caveman | 3,725 | Ultra-compressed replies that cut output tokens while keeping commands, code, errors and technical meaning exact, with intensity levels |
| grill-me | 2,764 | Calibrated interrogation of a plan, one question at a time with recommended answers, matched to stated knowledge and pressure level |
| junior-to-senior | 2,679 | Adversarial senior review of agent plans, grounded in codebase research and live web research of current practice |
| interface-kit | 2,275 | Accessible, performant UI implementation: typography, colour roles, spatial rhythm, motion and interaction states |
| context-canary | 1,974 | A per-turn canary signal that makes silent context degradation visible, plus a recovery protocol when it trips |
| loop-factory | 1,881 | Spec-driven loop where markdown specs move through inbox, active and archive behind a review gate |
| fuck-slop | 1,881 | No SKILL.md description in the pack; inspect the skill file before relying on it |
| last-20-percent | 1,045 | Finishes the experiential layer: what output reads like, first-run and empty states, opinionated defaults, the golden path |
| deslopify | 587 | Regex scan, diagnosis and rewrite loop that removes AI writing tells from text and re-scans its own output |

No indexed listings fall below the threshold; all 9 appear above.

## Why This Matters for Hermes Agents

Most agent output fails in three boring ways: too many words, an interface that looks like every other generated demo, and critique that starts at maximum before understanding the problem. This pack addresses each one with a behaviour rather than a reference document.

Token discipline is operational in a long session. Caveman drops filler and hedging while preserving commands, code, errors and API names, which is the difference between a cheaper reply and a lossy one.

Context drift is the harder failure to notice. Context Canary installs a visible per-turn signal so degradation shows up in the transcript instead of surfacing later as a confident wrong answer, and it ships a recovery protocol for when the signal breaks.

Loop Factory carries the most transferable structure: task state is which folder a spec sits in, and nothing counts as done until it passes a review gate. That is the same shape as any staged agent workflow, with implementation and verification automated and product decisions left to a human.

Junior to Senior and Grill Me handle review from opposite ends. One rewrites a plan at staff-engineer altitude with evidence; the other asks what the user already knows before deciding how hard to push. Interface Kit and Deslopify cover the output surface, one for screens and one for prose.

## Usage

| You say | What happens |
|---|---|
| "caveman mode" | replies compress to the default level, preserving commands, code and errors, until "normal mode" ends it |
| "grill me on this launch plan" | grill-me asks about knowledge and pressure level first, then one question at a time with recommended answers |
| "tear this plan apart like a staff engineer" | junior-to-senior rewrites it with evidence from the codebase and current web sources, and lists the delta |
| "build this settings page properly" | interface-kit applies accessibility, typography, colour roles, motion and interaction states to the implementation |
| "turn these specs into a build loop" | loop-factory scaffolds the inbox, active and archive structure and generates implementation and review prompts |
| "this session is drifting" | context-canary checks the per-turn signal and runs the recovery protocol if it tripped |
| "strip the AI tells from this post" | deslopify reports which tells it found, rewrites by meaning and re-scans until clean |

## Verification

Fetch one skill file and confirm the frontmatter matches the listing. The path below is `skills/caveman/SKILL.md` on branch main, and it returned 200 on November 4, 2026:

```bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/skills/main/skills/caveman/SKILL.md | head -5
```

A response opening with `name: caveman` and a quoted description confirms the tree still matches what skills.sh indexed. Then run this from the directory your agent loads skills from to confirm the copies landed:

```bash
ls -d */ | grep -E "^(caveman|grill-me|interface-kit|loop-factory)$"
```

Four matching directory names is the expected result. The repository itself carries eight SKILL.md directories, so a full install writes eight skill folders while skills.sh lists nine names.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-04) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| caveman | Pass | Pass | Fail |
| grill-me | Pass | Pass | Pass |
| junior-to-senior | Pass | Pass | Pass |
| context-canary | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified 2026-11-04: 18,811 combined installs across 9 indexed listings; 175 GitHub stars; MIT licence; last pushed 2026-08-07. Counts drift over time.
- Caveman carries a Snyk Fail in the sampled verdicts, which is what holds this pack at the Beta tier. The other three sampled skills pass all three scanners.
- The repository has eight SKILL.md directories but nine indexed listings. fuck-slop is the extra listing, and the pack carries no description for it, so check how it resolves before depending on it.
- Caveman's canonical installer pipes a remote shell script into bash. Read it first, or install through the skills.sh CLI instead.
- Loop Factory in the pack is the skill only. The README points to a separate Loop-Factory repository for the CLI and the native Claude and Codex adapters, so the full loop needs both.
- These are behavioural skills. Caveman and Deslopify change register and cadence, not correctness, and compressed output can hide reasoning that a reviewer would want to see.

## Related

- [Caveman Skills - Agent Coding Workflow Suite Setup](/hermes/skills/catalog/caveman-skills-setup)
- [Dogfood - Systematic QA Testing Setup](/hermes/skills/catalog/dogfood-setup)
- [Meticulous Agent Skills - Visual Regression Testing Setup](/hermes/skills/catalog/meticulous-agent-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Set intensity deliberately. Caveman defaults to full, and the lite level is the one to use in sessions where a human is reading every reply.
- Run Grill Me before Junior to Senior. One finds out how much pressure the user wants, the other supplies the senior evidence, and the pair costs less than a rewrite after commitment.
- Give Context Canary a visible marker you will actually notice, such as a turn counter. A signal that blends into the prose catches nothing.
- Keep Loop Factory specs in version control. State is the folder a spec sits in, so the repository history doubles as the audit trail.
- Use Deslopify on anything published, not on internal notes. The rewrite loop costs tokens, and the tells it targets matter most where a reader judges the writing.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
