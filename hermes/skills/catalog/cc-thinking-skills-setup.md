---
title: "Claude Code Thinking Skills - Mental Models Setup"
description: "tjboudreaux/cc-thinking-skills: 28 eval-informed mental models and critical-thinking skills for structured agent reasoning - 21.1K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cc-thinking-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "critical thinking", "reasoning", "decision making"]
---

# Claude Code Thinking Skills - Setup Guide

**Source:** [tjboudreaux/cc-thinking-skills](https://www.skills.sh/tjboudreaux/cc-thinking-skills) via skills.sh - 21.1K combined installs across 39 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 morning sweep)
**GitHub:** [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) - 1,762 stars, MIT license, main branch, last pushed Aug 7, 2026; 28 skills each live at skills/thinking-<name>/SKILL.md with evals/, analysis/, scripts/ and .claude-plugin/ directories at the repository root.
**Category:** Structured Reasoning and Decision-Making Skills
**Quality Tier:** 🟢 Green - no Fail cells across the 20-skill sample; the single Warn cell is Socket on thinking-red-team.

cc-thinking-skills is a public catalog of 28 portable Agent Skills for structured reasoning in Claude Code, GitHub Copilot, Codex, Cursor and other compatible tools. Each skill gives an agent a named procedure for a reasoning frame, covering decisions, diagnosis, systems, risk, strategy and innovation.

The catalog is eval-informed rather than asserted. A harness under evals/ runs structural, routing and outcome evaluations, and analysis/AUDIT.md plus analysis/evidence.json record what the runs actually show; the README states the evidence supports structured procedures but is not an accuracy guarantee. thinking-model-router picks among the 28 leaf skills and can return NONE, one skill, or up to three complementary skills, so an agent does not have to memorize all 28 triggers.

## Installation

Install all 28 skills at once with the skills CLI:

```bash
npx skills add tjboudreaux/cc-thinking-skills --all
```

Install with per-skill prompts instead:

```bash
npx skills add tjboudreaux/cc-thinking-skills
```

Or through the Claude Code plugin marketplace:

```text
/plugin marketplace add tjboudreaux/cc-thinking-skills
/plugin install thinking-skills@thinking-skills-marketplace
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| thinking-first-principles | 856 | separate physics from convention and rebuild from the simplest supported primitives |
| thinking-pre-mortem | 821 | assume a launch already failed and turn failure paths into mitigations and stop checks |
| thinking-red-team | 818 | authorized security review with a reproducible exploit path and verified mitigation |
| thinking-theory-of-constraints | 783 | find the single binding constraint, exploit and subordinate it, then recheck |
| thinking-opportunity-cost | 753 | name the best forgone use of time, people or money before committing |
| thinking-socratic | 738 | ask the few load-bearing questions that expose hidden requirements |
| thinking-second-order | 727 | trace consequences, incentives and feedback past the immediate fix |
| thinking-model-router | 722 | map the problem and return one thinking skill, up to three, or NONE |
| thinking-steel-manning | 717 | build the strongest faithful opposing case before rejecting or agreeing |
| thinking-systems | 716 | map boundary, stocks and flows and feedback when fixes elsewhere break things |
| thinking-triz | 700 | name the design contradiction and invent a no-compromise resolution |

The remaining 28 indexed listings range from 120 to 698 installs.

## Why This Matters for Hermes Agents

An agent that answers directly reaches for the first plausible frame instead of the right one. These skills force a named procedure before the answer: first principles before a rebuild, base rates before a forecast, a pre-mortem before a launch. The highest-value skills for a builder are the router, which picks one frame or none, red-team, which reports only reproducible findings with mitigations, and scientific-method, which ranks causes and tests the cheapest discriminator first. theory-of-constraints and reversibility stop an agent from over-engineering and over-deliberating. The catalog is eval-informed with a real harness under evals/, so you can audit which skills change outcomes before trusting them, and the README is explicit that the evidence supports procedures rather than guaranteeing an accuracy gain. The 28 skills stay manual-only with no automatic-retain verdict, so you invoke them deliberately rather than loading all of them into context.

## Usage

| You say | What happens |
|---|---|
| Use thinking-model-router for this problem | Routes to one thinking skill, up to three complementary ones, or NONE |
| Find the binding bottleneck in this pipeline | theory-of-constraints identifies the single constraint and subordinates everything else |
| Stress-test this launch plan | pre-mortem assumes failure and converts failure paths into mitigations and stop checks |
| Localize this bug | scientific-method ranks falsifiable hypotheses and tests the cheapest discriminator |
| Is this decision reversible? | reversibility splits cheap two-way doors from staged one-way doors |
| Red-team my API | red-team models the attacker and reports only reproducible findings with mitigations |
| What is the best use of my time here? | opportunity-cost names the best forgone use before committing |

## Verification

Confirm the router skill resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/tjboudreaux/cc-thinking-skills/main/skills/thinking-model-router/SKILL.md | head -30
```

Spot-check a leaf skill to confirm the skills/thinking-<name>/SKILL.md layout:

```bash
curl -sL https://raw.githubusercontent.com/tjboudreaux/cc-thinking-skills/main/skills/thinking-scientific-method/SKILL.md | head -30
```

Review the README before relying on the evidence claims:

```bash
curl -sL https://raw.githubusercontent.com/tjboudreaux/cc-thinking-skills/main/README.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| thinking-first-principles | Pass | Pass | Pass |
| thinking-pre-mortem | Pass | Pass | Pass |
| thinking-red-team | Pass | Warn | Pass |
| thinking-theory-of-constraints | Pass | Pass | Pass |
| thinking-opportunity-cost | Pass | Pass | Pass |
| thinking-socratic | Pass | Pass | Pass |
| thinking-second-order | Pass | Pass | Pass |
| thinking-model-router | Pass | Pass | Pass |
| thinking-steel-manning | Pass | Pass | Pass |
| thinking-systems | Pass | Pass | Pass |
| thinking-triz | Pass | Pass | Pass |
| thinking-probabilistic | Pass | Pass | Pass |
| thinking-scientific-method | Pass | Pass | Pass |
| thinking-reversibility | Pass | Pass | Pass |
| thinking-five-whys-plus | Pass | Pass | Pass |
| thinking-ooda | Pass | Pass | Pass |
| thinking-via-negativa | Pass | Pass | Pass |
| thinking-circle-of-competence | Pass | Pass | Pass |
| thinking-jobs-to-be-done | Pass | Pass | Pass |
| thinking-cynefin | Pass | Pass | Pass |

The sample is nearly clean: one Warn cell (Socket on thinking-red-team) and no Fail cells across 20 skills; 19 of the 39 indexed listings carry no published verdict.

## Limitations

- Snapshot data, verified Nov 23, 2026: 21,137 combined installs across 39 indexed listings; 1,762 GitHub stars; MIT license; last pushed Aug 7, 2026. Counts drift over time.
- The index lists 39 entries but the tree holds 28 skills/ directories; 11 listings (bayesian, inversion, debiasing, occams-razor, feedback-loops, model-selection, archetypes, dual-process, regret-minimization, leverage-points and fermi-estimation) carry install counts and eval contracts but no skills/<name>/SKILL.md in the current tree.
- Below the top 11 skills, install counts fall into a flat band from 698 down to 120, so the tail distinguishes little between skills.
- The README states the eval evidence supports structured procedures but does not guarantee a model accuracy gain; treat the provisional scientific-method result as directional.

## Related

- [Obra Superpowers - Engineering Workflow Skills](/hermes/skills/catalog/obra-superpowers-setup)
- [Karpathy Guidelines - Coding Discipline Skill](/hermes/skills/catalog/karpathy-guidelines-setup)
- [Daniel Miessler LifeOS - Life Operating System Setup](/hermes/skills/catalog/danielmiessler-lifeos-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with thinking-model-router when the fit is unclear; the plugin ID is thinking-skills:thinking-model-router and it can return NONE.
- Install with --all to pull all 28 skills, then invoke leaf skills one at a time instead of loading the whole catalog into context.
- Read analysis/AUDIT.md as the honest ledger of what is proven; the README warns the evidence is directional, not an accuracy guarantee.
- Run red-team only for code, auth or APIs you control; it reports only reproducible exploit paths with verified mitigations.
- Use reversibility before deliberating: decide cheap two-way doors fast and stage one-way doors to preserve options.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
