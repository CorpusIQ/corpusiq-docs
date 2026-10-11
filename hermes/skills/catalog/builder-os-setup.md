---
title: "BuilderOS - Product Builder Workflow Suite Setup"
description: "Setup guide for buildgreatproducts/builder-os - 15.7K combined installs. Ideation to launch: validators, planners, design system, build loops."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/builder-os-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "product development", "build workflow", "planning"]
---

# BuilderOS - Setup Guide

**Source:** [buildgreatproducts/builder-os](https://www.skills.sh/buildgreatproducts/builder-os) via skills.sh - 15.7K combined installs across 10 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [buildgreatproducts/builder-os](https://github.com/buildgreatproducts/builder-os) (229 stars, MIT license; last pushed Jul 7, 2026; formerly PLAID - the PLAID skills were refactored into standalone BuilderOS skills; layout `skills/<name>/SKILL.md`)
**Category:** Product Development / Builder Workflow
**Quality Tier:** 🟡 Beta - 229-star MIT suite; formerly PLAID; last pushed Jul 2026; all sampled verdicts Pass

BuilderOS, from publisher BuildGreatProducts, is the successor to PLAID (Product Led AI Development): a suite of ten agent skills that give product builders a repeatable system for ideating, designing, and building software with AI. The premise is discipline - AI coding agents are fast, and speed without process produces features that compile rather than features that work. BuilderOS encodes product-team habits (plan-driven work, mandatory review, end-to-end testing, honest reporting) as skills an agent follows automatically, turning a coding agent from autocomplete into a disciplined collaborator.

The skills chain through documents. Each one is fully standalone, but each writes its output to a shared `docs/` folder at the project root, and downstream skills pick those documents up automatically: idea-generator and idea-validator feed product-planner, product-planner feeds the build skills, and design-system feeds the craft and build layers. No single skill dominates the install mix; all ten listings sit above 1,000 installs, which suggests the suite is adopted across the whole lifecycle.

---

## Installation

BuilderOS installs through the skills CLI from your project root:

```sh
# Everything in one go
npx skills add BuildGreatProducts/builder-os
```

Individual skills are self-contained; install just the one you need:

```sh
npx skills add BuildGreatProducts/builder-os/skills/idea-generator
npx skills add BuildGreatProducts/builder-os/skills/product-planner
npx skills add BuildGreatProducts/builder-os/skills/build-loop-claude-code
npx skills add BuildGreatProducts/builder-os/skills/design-system
```

Or select by skill name:

```sh
npx skills add BuildGreatProducts/builder-os --skill product-planner
```

Manual alternative: clone the repo and copy the skill folders you want into your project's skills directory (for example `.claude/skills/` for Claude Code). You only need the build loop for the coding agent you actually use - Claude Code, Codex, or Cursor.

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| design-system | 1,820 | Turn screenshots, mockups, or Figma URLs into a design system: tokens plus rationale in design.md, mirrored by a live design.html style guide |
| product-planner | 1,684 | Structured vision intake (8 sections) that generates strategy, a coding-agent-ready spec, and a phased roadmap with task checkboxes |
| idea-validator | 1,674 | Pressure-test an idea: core assumption, ranked fatal flaws, real competition, first 10 customers, a 2-week MVP test, and a blunt verdict |
| launch-checklist | 1,672 | Audit the codebase (stack, services, env vars, payments, deploy config) and write a step-by-step path from "works on my machine" to "customers can use it" |
| idea-generator | 1,671 | Guided discovery of a product idea: mine what you already know, synthesize 3-5 candidate directions, score them, and sharpen the winner |
| build-loop-claude-code | 1,642 | Review-gated build loop for Claude Code: every increment is built, reviewed, tested end to end, then fixed before anything ships |
| build-mvp | 1,610 | Execute the entire roadmap end to end, testing and verifying each task, then finish with an initial git commit |
| build-loop-codex | 1,482 | The same build-review-test loop adapted to OpenAI Codex CLI's review tooling |
| build-loop-cursor | 1,439 | The same loop adapted to Cursor's review tooling |
| design-better | 1,022 | Craft layer for UI: 50 numbered UX/UI heuristics plus a pre-flight checklist, from hierarchy and typography to motion and WCAG 2.2 AA |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

Coding agents are fast, but speed without discipline produces features that compile rather than features that work - BuilderOS's own framing of the problem. The suite targets that gap with encoded process rather than more prompting: plan-driven work, mandatory review, end-to-end testing, and honest reporting become skills the agent follows automatically. The document chain is what makes multi-step projects tractable: each skill reads upstream documents from the project's `docs/` folder, so context carries across sessions and across agents instead of living in one chat window. Three build-loop flavors cover Claude Code, Codex, and Cursor, and build-mvp is agent-agnostic, so the same lifecycle works whichever coding agent runs underneath. The craft layer matters for agent output quality: design-better's heuristics and design-system's tokens give review passes something concrete to check against. Everything is MIT licensed and installs as plain markdown skills through the standard CLI.

## Usage

| You say | What happens |
|---|---|
| "Help me find a product idea" | idea-generator mines your context, synthesizes 3-5 directions, scores them on a five-axis scorecard, and writes docs/product-idea.md |
| "Validate my idea before I build" | idea-validator ranks fatal flaws, maps competition (including doing nothing), plans the first 10 customers, and delivers a strong / weak / pivot verdict |
| "Plan my product" | product-planner runs the 8-section vision intake and generates VISION.md, product-vision.md, prd.md, and product-roadmap.md |
| "Create a design system from this screenshot" | design-system produces design.md tokens plus a live design.html style guide the whole suite can implement from |
| "Build my MVP" or "run the build loop" | build-mvp executes the whole roadmap task by task; the build loop instead ships tighter review-gated increments - built, reviewed, tested, then fixed |
| "Make this UI feel more designed" | design-better applies 50 UX/UI heuristics and a pre-flight checklist, flagging missing tokens instead of inventing values |
| "Create my launch checklist" | launch-checklist audits the actual codebase and writes a step-by-step launch path with time estimates, costs, and success checks |

## Verification

```bash
# Confirm the skills landed (Claude Code example; adjust to your agent's directory)
ls ~/.claude/skills/ | grep -i -E "idea-validator|product-planner|build-loop"

# Review a skill straight from GitHub before installing (layout: skills/<name>/SKILL.md)
curl -s https://raw.githubusercontent.com/buildgreatproducts/builder-os/main/skills/design-system/SKILL.md | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| design-system | Pass | Pass | Pass |
| product-planner | Pass | Pass | Pass |
| design-review | - | - | - |

## Limitations

- Last pushed July 2026: recent enough to work as designed, but the suite is not under active daily development.
- Agent-specific build loops: install the one matching your coding agent (Claude Code, Codex, or Cursor); build-mvp is the agent-agnostic route.
- Security sampling is partial: design-review returned no verdicts from any engine in the sampled set.
- The lifecycle assumes a docs/ folder workflow - run the skills from the project root so the document chain works.
- Skills are standalone, but the payoff compounds only when upstream documents exist; running the build skills without a roadmap skips the pre-fill behavior.
- Snapshot data, verified Oct 10, 2026: 15,716 combined installs across 10 indexed listings; 229 GitHub stars; MIT; last pushed Jul 7, 2026. Counts drift over time.

## Related

- [PM Skills - Product Management Lifecycle Suite Setup](/hermes/skills/catalog/pm-skills-setup) - product-management counterpart across the same lifecycle stages
- [Compound Engineering Plugin - Every Inc Workflow Suite Setup](/hermes/skills/catalog/compound-engineering-plugin-setup) - workflow-suite sibling for engineering teams
- [ClawFu Skills - 175 Marketing Methodologies for AI Agents Setup](/hermes/skills/catalog/clawfu-skills-setup) - marketing layer for the launch phase this suite ends on
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start anywhere in the lifecycle: the README maps entry points - "help me find an idea", "validate my idea", "plan my product", "create a design system from this image", "build my MVP", "run the build loop", "design better", "create my launch checklist".
- Let the docs/ chain work: run upstream skills first, or drop existing documents into docs/, so each skill pre-fills its questions.
- Install only the build loop for the coding agent you actually use; add build-mvp when you want the whole roadmap executed in one pass.
- Design System accepts images, mockups, and Figma URLs, and its design.md becomes the token source for Product Planner, Build MVP, Build Loop, and Design Better.
- Trigger the craft layer for UI work with "design better" or "make this feel more designed" - it flags missing tokens as New Patterns instead of inventing values.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
