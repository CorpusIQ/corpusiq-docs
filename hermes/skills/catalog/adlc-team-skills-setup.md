---
title: "ADLC Team Skills - Agentic SDLC Skills Setup"
description: "tikalk/adlc-team-skills: agent skills for the Agentic SDLC - team context, software factory, evals and decision records - 13.9K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/adlc-team-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "sdlc", "agentic development", "team context"]
---

# ADLC Team Skills - Setup Guide

**Source:** [tikalk/adlc-team-skills](https://www.skills.sh/tikalk/adlc-team-skills) via skills.sh - 13.9K combined installs across 65 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 morning sweep)
**GitHub:** [tikalk/adlc-team-skills](https://github.com/tikalk/adlc-team-skills) - 146 stars, MIT license, main branch, last pushed Nov 23, 2026; skills live two levels deep under skills/<family>/<name>/SKILL.md across team, evals, product, architect, change, tech-radar, authoring and factory, each family sharing a templates/ directory.
**Category:** Agentic Software Development Lifecycle Skills
**Quality Tier:** 🟠 Orange - team-setup carries a Snyk Fail cell, with 8 further Warn cells (7 Snyk, 1 Gen Agent Trust Hub on architect-init) across the 20-skill sample.

adlc-team-skills gives a coding agent its team's context at session start so it stops working like a stranger. team-boot fires on the session_start event hook and injects a lean index (constitution titles, a CDR index ranked by confidence, the Class Boots catalog and the skills registry); the full text of a rule loads only when a task matches it. The index lives in a version-controlled team-ai-directives repo, reviewed by pull request and shared by the whole team.

Around that session loop sit the decision-record lifecycles (product PDR, architecture ADR, change ChDR and context CDR) plus the software factory, which runs intake, mission, review and learning with human gates at every decision point. The evals-* skills build executable graders with holdout splits and TPR/TNR, and tech-radar-boot injects the Tikal Tech Radar before a tech selection. The README counts 48 skills across 8 categories, installed with one adlc-cli command.

## Installation

One command installs the skills, generates slash commands and wires the event hooks, then runs team-setup to configure the team-ai-directives repo:

```bash
npx adlc-cli team setup tikalk/adlc-team-skills -a opencode
```

Install just the skills without team configuration:

```bash
npx adlc-cli skills add tikalk/adlc-team-skills -a opencode
```

Or install plain skills without commands or events:

```bash
npx skills add tikalk/adlc-team-skills -a claude -g
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| architect-implement | 317 | generate or update AD.md from accepted ADRs |
| team-boot | 316 | session-start bootstrap that injects the team index and dispatches class boots |
| architect-specify | 316 | guided trade-off analysis that writes the lightweight ADR draft |
| architect-clarify | 316 | review ADRs and approve them to Accepted before architecture generation |
| architect-analyze | 316 | detect ADR-to-AD drift, completeness gaps and quality issues |
| product-implement | 315 | generate or update PRD.md from accepted PDRs |
| product-clarify | 315 | refine, de-conflict and approve PDRs to Accepted |
| architect-init | 315 | reverse-engineer ADRs from an existing codebase |
| team-setup | 314 | clone, link or scaffold the team-ai-directives repo |
| team-discover | 313 | manual re-scan of team context into a structured match table |
| team-skills | 312 | list, add and onboard team skills, with --all installing everything |
| product-specify | 312 | guided trade-off analysis that writes the lightweight PDR draft |
| product-roadmap | 312 | weekly progress and milestone checks across four layers of truth |
| product-analyze | 312 | detect PDR-to-PRD drift and cross-PDR conflicts |
| team-repair | 311 | re-index, conflict scan, freshness and build-to-delete proposals |
| team-constitution | 311 | define or amend team-wide principles |
| product-init | 311 | document product decisions inferred from an already-built product |
| evals-init | 310 | scaffold evals/{system}/, pick PromptFoo or DeepEval, add a security baseline |
| evals-validate | 309 | run the evaluation pyramid and validate grader quality (TPR/TNR, SLA) |
| evals-specify | 309 | guided error analysis that writes the lightweight eval draft |
| evals-implement | 309 | generate graders and unit tests |
| evals-clarify | 309 | cluster criteria, isolate a holdout and publish the goldset |
| evals-analyze | 309 | route failures to deterministic checks, context rules or the backlog |
| workspace | 301 | multi-repo workspace with --init, --link and --status |

The remaining 41 indexed listings range from 1 to 292 installs.

## Why This Matters for Hermes Agents

Without this suite an agent treats every project as a blank slate: it does not know the team's rules, guesses at product and architecture decisions, and lets hard-won fixes evaporate when the session ends. team-boot fixes the blank-slate problem by injecting a lean index at session start and pulling rule bodies only when a task matches, which keeps context small. The decision-record lifecycles (PDR, ADR, ChDR and CDR) make product and architecture decisions visible and traceable from record to document to code instead of living in one developer's head. For operators the factory is the point: factory-mission forces a spec contract before code, factory-review grades PRs against policy-as-code, and factory-learn feeds what each run taught back into team memory, with human gates at every decision point. The evals-* skills turn "the maker grades its own work" into binary graders with holdout splits, and team-levelup publishes accepted CDRs back to the team repo so the next session starts smarter.

## Usage

| You say | What happens |
|---|---|
| Set up this repo for my team | team-setup clones, links or scaffolds the team-ai-directives repo and writes .adlc/init-options.json |
| Give the team context at session start | team-boot injects the index automatically via the session_start hook |
| Document this architecture decision | architect-specify writes a lightweight ADR draft, then architect-clarify approves it |
| Turn this product decision into a PRD | product-clarify accepts the PDR, then product-implement generates PRD.md |
| Verify my eval graders actually work | evals-validate runs the evaluation pyramid and checks TPR/TNR and SLA |
| Why does my code look like this? | change-init mines git history for issue-linked commits and recovers ChDRs |
| Reclaim stale rules | team-repair re-indexes, scans conflicts and proposes deletions with --build-to-delete |

## Verification

Confirm the team-boot entry point resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/tikalk/adlc-team-skills/main/skills/team/team-boot/SKILL.md | head -40
```

Spot-check the factory engine to confirm the two-level skills/<family>/<name>/SKILL.md layout:

```bash
curl -sL https://raw.githubusercontent.com/tikalk/adlc-team-skills/main/skills/factory/factory-mission/SKILL.md | head -40
```

Review the README before relying on install commands:

```bash
curl -sL https://raw.githubusercontent.com/tikalk/adlc-team-skills/main/README.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| architect-implement | Pass | Pass | Pass |
| team-boot | Pass | Pass | Warn |
| architect-specify | Pass | Pass | Warn |
| architect-clarify | Pass | Pass | Pass |
| architect-analyze | Pass | Pass | Warn |
| product-implement | Pass | Pass | Warn |
| product-clarify | Pass | Pass | Pass |
| architect-init | Warn | Pass | Pass |
| team-setup | Pass | Pass | Fail |
| team-discover | Pass | Pass | Pass |
| team-skills | Pass | Pass | Warn |
| product-specify | Pass | Pass | Pass |
| product-roadmap | Pass | Pass | Warn |
| product-analyze | Pass | Pass | Pass |
| team-repair | Pass | Pass | Pass |
| team-constitution | Pass | Pass | Pass |
| product-init | Pass | Pass | Pass |
| evals-init | Pass | Pass | Pass |
| evals-validate | Pass | Pass | Pass |
| evals-specify | Pass | Pass | Warn |

The sample has one Fail cell (Snyk on team-setup) and 8 Warn cells (Snyk on team-boot, architect-specify, architect-analyze, product-implement, team-skills, product-roadmap and evals-specify, plus a Gen Agent Trust Hub Warn on architect-init); 45 of the 65 indexed listings carry no published verdict.

## Limitations

- Snapshot data, verified Nov 23, 2026: 13,914 combined installs across 65 indexed listings; 146 GitHub stars; MIT license; last pushed Nov 23, 2026. Counts drift over time.
- The index lists 65 entries but the tree holds 49 skill directories; 16 indexed names (levelup-*, mission-plan, mission-specify, mission-verify, mission-implement, factory-architect, factory-product, factory-deploy, tech-radar-context, team-learn and diagnosing-team-skills) have no directory in the current tree. The README's deck-code glossary records that team-learn was hard-renamed to team-levelup in v0.30.0.
- Installed artifacts are CLI-generated (.agents/skills/, .opencode/commands/, skills-lock.json); regenerate with npx adlc-cli skills add when they look stale.
- The README discloses a July 27, 2026 supply-chain incident in which a stolen maintainer token briefly injected a payload into the repo's .claude/ and .vscode/ directories; history was rewritten and branch protection now blocks the vector, and the npx skills install path never shipped those files.
- Most of the 41 listings below the table cluster from 47 to 292 installs, so the tail carries little differentiation.

## Related

- [Obra Superpowers - Engineering Workflow Skills](/hermes/skills/catalog/obra-superpowers-setup)
- [Addy Osmani - Production-Grade Agent Skills for Hermes](/hermes/skills/catalog/addyosmani-agent-skills-setup)
- [19 Matt Pocock TypeScript Skills for Hermes Agent](/hermes/skills/catalog/mattpocock-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with team-boot: on an unconfigured project it points to /team-setup, and /team-constitution fills in the principles once.
- Keep jq installed; the setup scripts build JSON with jq -n and fail loudly if jq is missing.
- Run npx adlc-cli team update and team repair for routine maintenance (git pull, skills update, confidence update, reindex).
- Use --build-to-delete to shrink stale rules over time instead of letting them accumulate as context noise.
- Treat .vscode/tasks.json and .claude/settings.json in a clone as executable code; the repo's own security incident makes that lesson concrete.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
