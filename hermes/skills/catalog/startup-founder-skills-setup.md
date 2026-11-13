---
title: "Startup Founder Skills - 50 Founder Tasks Setup"
description: "shawnpang/startup-founder-skills: 10.9K combined installs across 50 listings, an open-source skill for each founder task from pitch deck to SOC 2 prep"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/startup-founder-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "startup", "fundraising", "founder ops"]
---

# Startup Founder Skills - Setup Guide

**Source:** [shawnpang/startup-founder-skills](https://www.skills.sh/shawnpang/startup-founder-skills) via skills.sh - 10.9K combined installs across 50 indexed listings; first seen Nov 13, 2026
**GitHub:** 384 stars, MIT license, `main` branch, last pushed 2026-03-16, 50 `SKILL.md` files under `skills/`, 53 files in total
**Category:** Founder operations: fundraising, sales, product, recruiting, engineering, legal and growth
**Quality Tier:** 🟢 Green - a 50-for-50 tree, an MIT licence and a README that maps every founder task to its skill; held back only by a March 2026 push and a flat install band.

The README opens as a personal note rather than a product page. The author spent ten years bootstrapping, noticed how much of the week goes to repeatable writing (cold emails, pitch decks, call prep, contract review, job posts), and set out to pick the 50 founder tasks AI handles best, pairing each one with an open-source skill that does it. It is explicitly inspired by Corey Haines' marketingskills and extends that logic from marketing to the rest of the founder stack.

The structural idea is `startup-context`. Every other skill reads it first: company stage, product, market, team, metrics and goals. That is why 50 separate skills do not read as 50 separate prompts. Set the context once and the pitch deck, the investor email and the job description all come back describing the same company.

Coverage runs the length of the role: fundraising (`pitch-deck`, `investor-research`, `data-room`, `fundraising-email`, `accelerator-application`), sales and BD, product and strategy, recruiting, engineering, legal and compliance, operations, customer success and growth. Several skills are adaptations of published open-source work with the original author credited in the README table.

The install band is the tell. All 50 listings sit between 182 and 400 installs, a spread of 218 across a suite of 50, which is the signature of a pack installed as a unit rather than 50 skills found one at a time. The numbers describe the pack, not the merit of any single skill.

## Installation

```bash
# Install all 50 skills
npx skills add shawnpang/startup-founder-skills

# Install specific skills
npx skills add shawnpang/startup-founder-skills --skill pitch-deck cold-outreach

# Install a category
npx skills add shawnpang/startup-founder-skills --skill fundraising

# List available skills
npx skills add shawnpang/startup-founder-skills --list
```

The README states the pack works with Claude Code, OpenAI Codex, Cursor, Windsurf and any tool that follows the Agent Skills spec. Start with `startup-context` whichever route you take, because it is the file the rest read.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| terms-of-service | 400 | Drafting, reviewing or updating terms of service, acceptable use policies and SaaS agreements. |
| pitch-deck | 347 | Slide-by-slide deck content and narrative for a seed or Series A raise. |
| landing-page | 284 | Landing page copy, layout, CTAs and conversion critique. |
| review-mining | 270 | Pain points, switching triggers and voice-of-customer language mined from Trustpilot, G2, Capterra and app store reviews. |
| privacy-policy | 261 | Privacy policy, cookie policy and data processing documentation drafts. |
| market-research | 252 | TAM and SAM sizing, market dynamics and market hypothesis validation. |
| sales-script | 239 | Demo scripts, discovery call frameworks, objection handling and RFP responses. |
| startup-context | 236 | The company context document the other skills read first: stage, product, market, team, metrics, goals. |
| competitive-analysis | 235 | Competitor feature comparison, positioning, pricing benchmarks and market mapping. |
| mvp-scoping | 232 | Deciding what to build, cut and defer for a first release. |
| cold-outreach | 229 | Cold emails and LinkedIn messages to prospects, partners and investors. |
| data-room | 227 | Due diligence checklists, document organisation and drafts for missing diligence items. |
| founder-thought-leadership | 226 | Founder IP and personal brand on X and LinkedIn: frameworks, contrarian takes, building in public. |
| investor-research | 226 | Identifying, qualifying and prioritising investors by stage, sector, check size and portfolio fit. |
| accelerator-application | 217 | Applications to YC, Techstars and more than 40 other accelerators, with interview prep. |
| proposal-generation | 212 | Sales proposals, statements of work, NDAs and pricing quotes. |
| prd-writing | 212 | Product requirements documents, feature specs and user story sets. |
| event-hosting | 212 | Event page copy, run of show and promotion for meetups and workshops on Luma. |
| process-docs | 211 | SOPs, playbooks and runbooks for internal operations. |
| board-update | 211 | Monthly or quarterly investor updates and board decks. |
| architecture-design | 211 | Service boundaries, data models, API design and infrastructure planning. |

The remaining 29 indexed listings range from 182 to 210 installs.

## Why This Matters for Hermes Agents

A solo founder's day is a sequence of tasks that each need a different specialist: a deck for an investor, a script for a demo, a spec for the contract engineer, a policy for the first enterprise buyer. Hiring is not available and general-purpose prompting produces generic output, because the agent does not know the company.

This suite solves the second problem first. `startup-context` is a durable file the agent reads before anything else, so a job description comes back with the real stage, the real stack and the real comp band instead of the average of the internet.

The cross-references are the more interesting part. The README documents the chains: `pitch-deck` to `investor-research` to `data-room`, `cold-outreach` to `lead-scoring` to `sales-script`, `prd-writing` to `mvp-scoping` to `roadmap-planning`, `job-description` to `interview-kit` to `sourcing-outreach`. Each skill points at the next, which turns a one-off request into a workflow.

For an agent operator, the value is leverage on the tasks that are high stakes and low volume. Nobody writes enough privacy policies to get good at a privacy policy, and the first one usually arrives the week a customer asks for it.

## Usage

| You say | What happens |
|---|---|
| "Help me write a pitch deck for our Series A" | Runs `pitch-deck` with `investor-research`, returning slide-by-slide narrative for the round. |
| "Write a cold email to reach enterprise prospects" | Runs `cold-outreach` and `lead-scoring` against the ICP in `startup-context`. |
| "Create a PRD for our new billing feature" | Runs `prd-writing` and returns a requirements document with user stories. |
| "Review this contract from our vendor" | Runs `contract-review` and returns flagged risk clauses with suggested responses. |
| "Draft an investor update for this month" | Runs `board-update` and returns the monthly update in the format investors expect. |
| "Write a job description for a senior engineer" | Runs `job-description` with `employer-brand` for careers page copy. |
| "What should we cut from the v1 scope?" | Runs `mvp-scoping` and returns a build, cut and defer list. |

## Verification

Probe two skills on the branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/shawnpang/startup-founder-skills/main/skills/pitch-deck/SKILL.md | head -8
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/shawnpang/startup-founder-skills/main/skills/terms-of-service/SKILL.md
```

After installing, confirm 50 folders under `skills/` with one `SKILL.md` each. The repo carries 53 files in total, so there is almost no runtime surface to go wrong: a missing skill is a copy problem, not a dependency problem.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| terms-of-service | Pass | Pass | Pass |
| pitch-deck | Pass | Pass | Pass |
| landing-page | Pass | Pass | Pass |
| review-mining | Pass | Pass | Warn |
| privacy-policy | - | - | - |

Four of the 50 listings carry published verdicts at the time of the sweep and the rest show none. The skills are instruction files with no executables, which lowers the risk, and the Snyk Warn on `review-mining` sits on a skill that reads review sites and review site terms are the thing to watch there.

## Limitations

- Snapshot data, verified 2026-11-13: 10,905 combined installs across 50 indexed listings; 384 GitHub stars; MIT license; last pushed 2026-03-16. Counts drift over time.
- The legal and finance skills produce drafts and not advice. `terms-of-service` and `privacy-policy` both carry an explicit "not a substitute for legal counsel" note in the README, and `contract-review` is billed as issue spotting with a lawyer signing off.
- The pack was last pushed in March 2026, so anything that changed in agent tooling, review platforms or compliance regimes since then is not in here. Treat page-level guidance as a starting draft.
- The flat install band means the suite installs as a unit. A per-skill install count here says very little about how many people chose that skill on purpose.
- Several skills are adaptations of other authors' open-source work. The README credits each one and links the original, so a bug in an adapted framework is worth checking upstream before filing it here.

## Related

- [Startup OS Skills - Sales, Product and Video Pack](/hermes/skills/catalog/startup-os-skills-setup)
- [Startup Validation Skills - Design, Pitch and Positioning](/hermes/skills/catalog/startup-validation-skills-setup)
- [OPC Skills - Solopreneur Toolkit (SEO, Reddit, Branding, Launch) Setup](/hermes/skills/catalog/opc-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Write `startup-context` before anything else, by hand and in your own words. Every other skill's output quality is bounded by that file.
- Use the category install flag while evaluating. `--skill fundraising` pulls five skills instead of 50, which keeps the agent's context clean for the trial.
- Pair the sales and marketing skills on one campaign. `cold-outreach`, `sales-script` and `lead-scoring` were built to share an ICP definition, and running one without the others is where the inconsistency shows.
- Keep `terms-of-service` and `privacy-policy` output in version control. Policy documents are the one artifact here that a customer may audit, and a diffable history answers that faster than a search through old chats.
- Re-run `review-mining` on a schedule. The pain-point language it extracts decays as reviews age, and the switching triggers are only useful while they are current.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
