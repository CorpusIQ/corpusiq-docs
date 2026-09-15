---
title: revenue-centric-design - SaaS Revenue Design
description: "heliocosta-dev/revenue-centric-design - revenue-centric-design skill, 1.3K installs: a 101-principle SaaS playbook distilled from @richardrx covering conversion, onboarding, pricing, churn, positioning, and AI-era differentiation for any skills.sh-compatible agent."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/revenue-centric-design-setup/"
robots: "index,follow"
last_updated: "2026-08-28"
tags: ["hermes skill", "agent skill", "skill setup", "saas", "cro", "conversion", "pricing", "retention", "behavioral-science", "product-design"]
---

# revenue-centric-design - Setup Guide

**Source:** [heliocosta-dev/revenue-centric-design](https://skills.sh/heliocosta-dev/revenue-centric-design/revenue-centric-design)
**GitHub:** [heliocosta-dev/revenue-centric-design](https://github.com/heliocosta-dev/revenue-centric-design) (custom license - Richard's writing used with permission, educational/reference use, no gambling/betting products)
**Skill:** `revenue-centric-design`, 1.3K installs, ~570 GitHub stars
**Category:** Growth / Product Design
**First Seen:** Jul 2, 2026 on skills.sh (repo created Jun 11, 2026); catalogued in the Aug 28, 2026 sweep
**Quality Tier:** 🟢 Production - Gen Agent Trust Hub Pass, Socket Pass, Snyk Pass (verified Aug 28, 2026)

revenue-centric-design packages 101 CRO and growth principles distilled from the X/Twitter writing of Richard ([@richardrx](https://x.com/richardrx), "Design for startups" - ex-Volkswagen, ex-PayPal, ex-IBM) into a single agent skill. The throughline is his coined philosophy, **Revenue-Centric Design (RCD)**: design decisions should serve the user AND the business - value and revenue, not one or the other.

The skill is a pure knowledge playbook: one SKILL.md plus ten themed reference files that load progressively. No APIs, no CLI, no credentials - any skills.sh-compatible agent can apply it to landing pages, onboarding, pricing, trials, churn, UX flow, feature scope, positioning, or growth questions.

---

## Installation

```bash
npx skills add heliocosta-dev/revenue-centric-design
```

Verified live Aug 28, 2026: `npx skills add heliocosta-dev/revenue-centric-design --list` clones the repo and finds exactly 1 skill (`revenue-centric-design`).

Update an existing install:

```bash
npx skills update revenue-centric-design
```

Manual install (into your agent's skills directory):

```bash
git clone https://github.com/heliocosta-dev/revenue-centric-design.git ~/.claude/skills/revenue-centric-design
```

The README names Claude Code, Cursor, Codex, Copilot, Gemini, and "any skills.sh-compatible agent" as supported targets - the SKILL.md is agent-agnostic and loads in Hermes as a normal skill.

## Prerequisites

| Requirement | Details |
|---|---|
| **Agent harness** | Any skills.sh-compatible agent (Hermes, Claude Code, Cursor, Codex, Copilot, Gemini) |
| **Dependencies** | None - ships only SKILL.md plus 10 themed reference files |
| **Credentials** | None required - no API keys or accounts |

## What It Provides

The skill loads only the theme relevant to the current question (progressive disclosure). Each principle follows a fixed shape - **Principle → Apply when → The move → Evidence → Visual → Source** - so the agent gets the named lever (decoy effect, Swiss Knife Index, GBB, Eugene Schwartz's awareness levels, loss aversion, peak-end rule), the concrete action, and the proof.

| Theme | Principles | Covers |
|---|---:|---|
| Conversion & Landing Pages | 16 | hero/copy, CTAs, social proof, awareness levels, CRO |
| Onboarding & Activation | 19 | empty states, aha moment, TTV, activation, trials |
| Revenue-Centric Design | 13 | the RCD principles, design process & method |
| Pricing & Monetization | 11 | decoy/anchoring, GBB, trial-with-card, upgrades |
| Churn & Retention | 9 | cancellation UX, expectation debt, NRR, JTBD |
| Behavioral Science Toolkit | 7 | cross-cutting biases & persuasion levers |
| Product Strategy & Features | 7 | Swiss Knife Index, feature adoption, attention |
| Positioning, ICP & GTM | 8 | ICP, niche, PLG, Bullseye, first customers |
| AI-Era Differentiation | 7 | moats, commoditization, vibe-coding pitfalls |
| Metrics & Experimentation | 4 | A/B rigor, vanity metrics, churn-to-LTV math |

Source coverage: @richardrx's curated posts from 14 Jan 2026 → 1 Jul 2026 (101 posts). The entry point is `SKILL.md`; informational diagrams referenced by the principles live in `assets/`.

## Quick Start

Trigger the skill when helping improve how a digital product **acquires, activates, retains, monetizes, or differentiates** - landing pages, onboarding, pricing, trials, churn, UX flow, feature scope, positioning, or growth.

The RCD spine in 9 principles:

1. **Neutrality is omission** - an interface that doesn't direct hurts conversion
2. **Who talks to everyone convinces no one** - no ICP → generic value → worse retention
3. **Value first, ask later** - proof must arrive before the user questions their choice
4. **Your promise is the size of your proof** - the market believes what you demonstrate, not what you claim
5. **Same competes on price, different on category** - no contrast, no margin

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Landing page conversion** | The 16 conversion principles apply directly to corpusiq.io hero copy, CTAs, and social proof ordering - the awareness-levels ladder informs how we speak to cold vs warm operator traffic |
| **Pricing page design** | Decoy/anchoring and trial-with-card principles feed the CorpusIQ plan-page layout; GBB (good-better-best) math for the tier structure |
| **Onboarding & activation** | 19 activation principles for shortening time-to-value on first CorpusIQ run - empty states and the aha moment, not feature tours |
| **Churn & retention** | Cancellation UX and expectation-debt principles for the churn-survey flow; NRR math for operator retention reporting |
| **ICP & positioning** | The positioning/GTM theme sharpens operator ICP messaging - "who talks to everyone convinces no one" is our segmentation rule |
| **AI-era differentiation** | Moats and commoditization principles for positioning the data-layer moat against generic AI-tool noise |

## Limitations / Verification

- **Usage boundary:** the author permits use only on condition the skill is never applied to betting, casino, or gambling products (including loot-box / real-money-gaming mechanics) - encoded in the custom LICENSE and instructed inside the SKILL.md itself.
- **Content snapshot ends Jul 1, 2026:** @richardrx posts after that date are not included; run `npx skills update revenue-centric-design` to pull the latest.
- **Knowledge-only skill:** no tools or automated pipelines - output quality depends on the agent applying the principles, not on any service.
- **Below the 20K cluster bar:** 1.3K installs as a single-skill repo; drafted on capability fit (SaaS conversion/retention is CorpusIQ's core domain), clean triple-Pass audits, and hot-board momentum (+3 installs in 1H on Aug 28, 2026).

Verification after install:

```bash
npx skills add heliocosta-dev/revenue-centric-design -g -y
# Confirm the skill file landed in the agent's skills directory
ls ~/.claude/skills/revenue-centric-design/SKILL.md
```

## Related

- [Autonnel Skills - Conversion & Funnel Optimization Suite Setup](/docs/hermes/skills/catalog/autonnel-skills-setup) - funnel-blueprint and AOV plays from the same conversion domain
- [design-review - Visual UI Audit & Fix Setup](/docs/hermes/skills/catalog/design-review-setup) - the visual-audit companion for the design side
- [Skills Marketplace](/docs/hermes/skills/marketplace) - marketplace index for more discovery batches
