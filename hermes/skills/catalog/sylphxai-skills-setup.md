---
title: "Sylphx AI Skills - Agent Methodology Standards Setup"
description: "sylphxai/skills: 4.8K combined installs across 95 listings; scenario-driven agent skills and reference standards for Claude Code, Codex, and OpenCode."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sylphxai-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "engineering methodology", "product review", "skill authoring"]
---

# Sylphx AI Skills - Setup Guide

**Source:** [sylphxai/skills](https://www.skills.sh/sylphxai/skills) via skills.sh - 4.8K combined installs across 95 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 morning sweep)
**GitHub:** 1 star, MIT licence, `main` branch, last pushed 2026-11-16. Sixteen skills live at `skills/<name>/SKILL.md`, each with a `references/` folder and a `trigger-cases.json`, plus `.claude-plugin` and `.codex-plugin` manifests and a `scripts/verify-skills.py` verifier.
**Category:** Engineering methodology, product review, and skill authoring
**Quality Tier:** 🟡 Yellow - 2 Warns among 20 sampled skills (saas-subscription-pricing and market-research-synthesis, both Snyk); MIT licence.

Sylphx AI Skills is an opinionated, scenario-driven collection of Agent Skills with colocated reference methodologies for software engineering, system architecture, product design, commercial and partner negotiations, operations, marketing and growth, customer support, and clear communication. Skills trigger on the observable task moment rather than a persona, and each deep domain standard lives beside the skill that uses it in `skills/<name>/references/`.

The install index and the repo tree are far apart. skills.sh indexes 95 listings, but the current tree holds 16 skill directories (author-item, challenge, frontend-design, corporate-governance, game-economy, deliver-and-verify, prove-it, patrol, fan-out, swarm-fuse, unblock, refactor, clear-writing, author-skill, customer-support, ambassador). The 95 indexed names - saas-subscription-pricing, interface-craft, and other product and commerce review skills - have no matching directory in the current tree.

## Installation

Install all skills globally across detected coding agents:

```bash
npx skills add SylphxAI/skills -g -y
```

Or install into the current project workspace:

```bash
npx skills add SylphxAI/skills -y
```

Update installed skills to the latest commit on main:

```bash
npx skills update
```

The README also documents a Claude Code plugin marketplace route (`claude plugin marketplace add SylphxAI/skills`, then `claude plugin install sylphx-skills@sylphx`) and a direct git clone with symlinks into `~/.agents/skills`, `~/.claude/skills`, and Antigravity.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| saas-subscription-pricing | 69 | Audit SaaS subscription pricing and packaging: value metric, tiers, trials, seats, and enterprise path. |
| interface-craft | 68 | Improve product interfaces with UI craft, micro-interactions, and accessibility-preserving polish. |
| skill-marketplace-creator | 66 | Create, curate, and operate repositories or marketplaces for reusable agent skills. |
| refund-and-support-flow-review | 66 | Design and audit refund, cancellation, chargeback, and customer support flows. |
| payment-platform-readiness | 66 | Prepare payment integration for Apple Pay, Google Pay, app stores, and web checkout. |
| market-research-synthesis | 66 | Synthesize competitors, app-store listings, reviews, and pricing pages into market research. |
| customer-support-operations | 66 | Design support operations: help centers, ticket triage, refund handling, and escalation. |
| skill-eval-designer | 63 | Design behavior evals, positive and negative prompts, rubrics, and quality gates for skills. |
| marketplace-payouts-review | 63 | Design and audit marketplace payout, fee, revenue-share, and ledger flows. |
| decision-memo-writer | 62 | Write and review decision memos for product, pricing, launch, and growth choices. |

The remaining 85 indexed listings range from 42 to 55 installs.

## Why This Matters for Hermes Agents

For an agent doing product or commerce work, these skills encode review checklists and decision templates rather than ad hoc judgment: pricing and packaging, payment readiness, refund and chargeback flows, marketplace payouts, and support operations each come with a specific audit surface. An agent that loads them produces a structured review instead of a generic opinion.

The skill-authoring angle matters too. skill-marketplace-creator and skill-eval-designer cover the two sides of shipping reusable agent skills - building and operating the marketplace, and designing behaviour evals with positive and negative prompts, rubrics, and quality gates. Those are the same contracts a Hermes skill pack must satisfy.

The index-to-tree gap is the one thing to verify before you rely on the numbers. The 95 indexed listings describe a product and commerce review suite that is not present in the current tree, so treat the install counts as skills.sh index data rather than a list of the 16 skills the repo actually ships.

## Usage

| You say | What happens |
|---|---|
| "Review our SaaS pricing and packaging" | saas-subscription-pricing audits the value metric, tiers, trials, and enterprise path. |
| "Is our refund flow going to cause chargebacks?" | refund-and-support-flow-review walks refund, cancellation, and dispute handling. |
| "Set up a marketplace for our skills" | skill-marketplace-creator scaffolds a publishable, curated skill marketplace. |
| "Write a decision memo on this launch" | decision-memo-writer produces a structured memo with the open choices and recommendation. |
| "Design evals for my new skill" | skill-eval-designer lays out positive and negative prompts, rubrics, and quality gates. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/SylphxAI/skills/main/skills/challenge/SKILL.md
```

Then install and run the repository's own verifier, which checks YAML frontmatter, plugin manifests, links, reference coverage, and each skill's trigger contracts:

```bash
npx skills add SylphxAI/skills -g -y
python3 scripts/verify-skills.py
python3 scripts/verify-terminology.py
```

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| saas-subscription-pricing | Pass | Pass | Warn |
| interface-craft | Pass | Pass | Pass |
| skill-marketplace-creator | Pass | Pass | Pass |
| refund-and-support-flow-review | Pass | Pass | Pass |
| payment-platform-readiness | Pass | Pass | Pass |
| market-research-synthesis | Pass | Pass | Warn |
| customer-support-operations | Pass | Pass | Pass |
| skill-eval-designer | Pass | Pass | Pass |
| marketplace-payouts-review | Pass | Pass | Pass |
| decision-memo-writer | Pass | Pass | Pass |
| game-economy-review | Pass | Pass | Pass |
| promotion-campaign-review | Pass | Pass | Pass |
| launch-readiness-review | Pass | Pass | Pass |
| incident-communication-playbook | Pass | Pass | Pass |
| help-center-architecture | Pass | Pass | Pass |
| desktop-os-integration | Pass | Pass | Pass |
| app-store-distribution-readiness | Pass | Pass | Pass |
| subscription-entitlement-review | Pass | Pass | Pass |
| store-listing-optimization | Pass | Pass | Pass |
| startup-growth-review | Pass | Pass | Pass |

The sample covers 20 of 95 indexed listings; two carry a Snyk Warn (saas-subscription-pricing and market-research-synthesis).

## Limitations

- Snapshot data, verified Nov 19, 2026: 4,841 combined installs across 95 indexed listings; 1 GitHub star; MIT licence; last pushed 2026-11-16. Counts drift over time.
- The install index outruns the tree: 95 indexed listings against 16 skill directories, and none of the 95 indexed names has a counterpart in the current tree. The indexed names describe a product and commerce review suite that the tree does not contain.
- The repo is young: one GitHub star and a single maintainer-visible activity trace, so treat the methodology content on its own merits rather than community adoption.
- The 16 in-tree skills are methodology-heavy; they encode a specific opinionated workflow rather than neutral option lists, so they fit teams that want a prescribed process.

## Related

- [Product Skills - UX Design & Product Management Setup](/hermes/skills/catalog/product-skills-setup)
- [skill-creator - Anthropic's Skill Creation Framework Setup](/hermes/skills/catalog/skill-creator-setup)
- [ClawHub Skill Vetting - Security Scanner Setup](/hermes/skills/catalog/clawhub-skill-vetting-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load the 16 in-tree skills rather than chasing the indexed names; the index names do not map to directories in the current repo.
- Start with author-item and deliver-and-verify if you want the ATDD and verification workflow; they are the core of the three-stage methodology.
- Run `python3 scripts/verify-skills.py` in CI alongside your own checks; it enforces trigger contracts and reference coverage, not just YAML shape.
- Keep organization-specific state in your workspace or Organization Knowledge; the repo is explicit that company state does not belong inside a skill.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
