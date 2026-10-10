---
title: "PM Skills - Product Management Lifecycle Suite Setup"
description: "Setup guide for product-on-purpose/pm-skills - 44.7K combined installs. 68 product management skills across the lifecycle, with templates and samples."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pm-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "product management", "product lifecycle", "workflows"]
---

# PM Skills - Setup Guide

**Source:** [product-on-purpose/pm-skills](https://www.skills.sh/product-on-purpose/pm-skills) via skills.sh - 44.7K combined installs across 71 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [product-on-purpose/pm-skills](https://github.com/product-on-purpose/pm-skills) (716 stars, Apache-2.0; pushed 2026-10-08; layout `skills/<name>/SKILL.md`)
**Category:** Product Management
**Quality Tier:** 🟡 Beta - 716-star Apache-2.0 library; active Oct 2026; all sampled verdicts Pass

PM Skills is a curated library of 68 plug-and-play product management skills for AI agents, published by product-on-purpose. It covers the complete product lifecycle: 30 Triple Diamond phase skills, 11 foundation skills, 12 utility skills, and 15 tool skills across the Foundation Sprint and Design Sprint workshop families plus note-and-vote. The repo also ships 6 sub-agents, workflow orchestrators, 200+ real-world sample outputs, and CI-enforced contracts.

The library is designed to route between skills: a build-risk review hands off to a hypothesis skill, survey analysis points at experiment design, and so on. The publisher recommends installing the whole set - subsets via `--skill` work, but handoffs are only seamless with the full library. Skills invoke by name after install, for example `/pm-skills:deliver-prd`.

---

## Installation

### Claude Code plugin (recommended)

```bash
/plugin marketplace add product-on-purpose/agent-plugins
/plugin install pm-skills@product-on-purpose
```

All 68 skills and their slash commands become available immediately; no clone required.

### Cross-agent (skills CLI)

```bash
npx skills add product-on-purpose/pm-skills
```

The skills CLI scans the `skills/` directory and installs the library into your agent's default skills directory. Works with Claude Code, Cursor, GitHub Copilot, Cline, and other agents in the skills ecosystem.

### Clone (manual, everything included)

```bash
git clone https://github.com/product-on-purpose/pm-skills.git
cd pm-skills
```

Use this path when you want local access to the sample outputs, plan to customize skills, or prefer not to depend on a CLI. Optional: run `./scripts/sync-claude.sh` (macOS/Linux) or `./scripts/sync-claude.ps1` (Windows) to populate `.claude/skills/` for agents that use that discovery path.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| deliver-acceptance-criteria | 1,002 | Given/When/Then testable acceptance scenarios |
| deliver-prd | 950 | Comprehensive product requirements document with problem, metrics, stories, scope, and dependencies |
| deliver-user-stories | 847 | INVEST-compliant user stories with acceptance criteria |
| deliver-edge-cases | 818 | Error states, boundaries, and recovery paths for a feature |
| discover-competitive-analysis | 793 | Mapping the competitive landscape for gaps and differentiation opportunities |
| define-problem-statement | 767 | Crystal-clear problem framing with scope, impact, and success criteria |
| define-hypothesis | 763 | Testable assumptions with measurable success conditions |
| develop-adr | 754 | Architecture Decision Records in Michael Nygard format |
| deliver-launch-checklist | 744 | End-to-end launch checklist so nothing gets missed |
| define-jtbd-canvas | 732 | Jobs to be Done framework for customer motivation |
| develop-solution-brief | 730 | One-page solution pitch with tradeoffs and open questions |
| define-opportunity-tree | 730 | Teresa Torres-style outcome-driven opportunity mapping |
| discover-interview-synthesis | 729 | Turning raw user research into insights, patterns, and design implications |
| measure-dashboard-requirements | 720 | Analytics dashboard specifications |
| deliver-release-notes | 715 | User-facing release communication |
| measure-experiment-design | 714 | Rigorous A/B test planning with hypothesis, sample size, and success criteria |
| measure-instrumentation-spec | 709 | Event tracking requirements for engineers |
| develop-design-rationale | 709 | Documenting why a design choice was made, for future reference |
| foundation-persona | 708 | Product or marketing personas with evidence and confidence ratings |
| iterate-retrospective | 706 | Team retros that produce real action items, not just feelings |
| measure-experiment-results | 705 | Documenting and synthesizing learnings from completed experiments |

The remaining 50 indexed listings range from 60 to 699 installs.

## Why This Matters for Hermes Agents

Product management is one of the highest-leverage places to point an agent, and one of the easiest places for low-quality output to show: stakeholders who have read hundreds of PRDs notice boilerplate immediately. This library encodes the quality bar. Every skill pairs an instruction set with templates and sample outputs - 200+ real-world examples ship in the repo as the acceptance bar - and the repo's contracts are CI-enforced so skill files stay structurally consistent. The lifecycle structure matters for agent workflows: 30 phase skills map onto Discover, Define, Develop, Deliver, Measure, and Iterate, with foundation, utility, and workshop tool families on top. Skills hand off deliberately (a build-risk review routes into a hypothesis skill; survey analysis points at experiment design), and 10 workflow commands plus a `/chain` runner orchestrate multi-skill sequences without re-prompting. For teams maintaining their own agent catalogs, the utility family - pm-skill-builder, pm-skill-validate, and pm-skill-auditor - doubles as meta-tooling for authoring and auditing skills.

## Usage

| You say | What happens |
|---|---|
| Write a PRD for the new onboarding flow | deliver-prd drafts problem, metrics, stories, scope, and dependencies |
| Break this epic into shippable work | deliver-user-stories writes INVEST-compliant stories with testable acceptance criteria |
| Stress-test this feature before we build | deliver-edge-cases maps error states, boundaries, and recovery paths |
| Design the A/B test for our pricing page | measure-experiment-design produces hypothesis, sample size, and success criteria; measure-experiment-results reads the outcome later |
| Synthesize these user interviews | discover-interview-synthesis returns actionable insights, patterns, and design implications |
| Run our sprint retrospective | iterate-retrospective ends with real action items, not just discussion |
| Kick off the new feature end to end | the Feature Kickoff workflow chains problem-statement, hypothesis, prd, user-stories, and launch-checklist |

## Verification

Confirm the skills CLI install with:

```bash
npx skills list | grep pm-skills
```

In Claude Code, invoke a skill directly - `/pm-skills:deliver-prd` should resolve after a plugin install - and confirm the workflow commands (`/workflow-*`) are present. Before installing, review the exact instructions the agent will read: the repo holds one folder per skill at `skills/<name>/SKILL.md`. For example, fetch the acceptance-criteria skill file at `https://raw.githubusercontent.com/product-on-purpose/pm-skills/main/skills/deliver-acceptance-criteria/SKILL.md` (verified reachable Oct 10, 2026).

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| deliver-acceptance-criteria | Pass | Pass | Pass |
| deliver-prd | Pass | Pass | Pass |
| deliver-user-stories | Pass | Pass | Pass |

## Limitations

- Install counts are flat outside the top of the chart - the bottom 50 listings sit between 60 and 699 installs - so treat popularity as a weak signal for most of the library.
- Subset installs via `--skill` can strand handoffs; the publisher recommends the full library or following the routing table to its destinations.
- Sampled verdicts cover the three deliver-* skills above only; re-check the rest on skills.sh before production use.
- The index (71 listings) and the documented library (68 skills) do not match one-to-one, so a few indexed entries sit outside the documented set.
- Nothing runs at install except opt-in hooks, per the project's provenance documentation - review those hooks before enabling them.

- Snapshot data, verified Oct 10, 2026: 44,697 combined installs across 71 indexed listings; 716 GitHub stars; Apache-2.0; last pushed 2026-10-08. Counts drift over time.

## Related

- [ClawFu Skills - 175 Marketing Methodologies for AI Agents Setup](/hermes/skills/catalog/clawfu-skills-setup) - the method-library approach applied to marketing work
- [Content Strategy - Full Planning Framework Setup](/hermes/skills/catalog/content-strategy-setup) - planning frameworks that complement discovery and positioning skills
- [Hermes Marketing Dashboard - AI Agent Marketing Ops Setup](/hermes/skills/catalog/hermes-marketing-dashboard-setup) - dashboard-side ops for measure-phase work
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use the plugin path in Claude Code: `/plugin marketplace add product-on-purpose/agent-plugins` then `/plugin install pm-skills@product-on-purpose` gets all 68 skills plus the workflow commands with no clone.
- Keep project context across sessions with `.claude/pm-skills.local.md` (gitignored); eight skills read it so you stop re-supplying phase and initiative details.
- Trust the samples: the repo's 200+ real-world outputs are the acceptance bar for what a good deliverable looks like.
- Chain instead of re-prompting - workflows such as Feature Kickoff, Lean Startup, and Customer Discovery, or the `/chain` runner, sequence skills for you.
- The skills CLI install path notes anonymous telemetry; opt out with `DISABLE_TELEMETRY=1` or `DO_NOT_TRACK=1`.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
