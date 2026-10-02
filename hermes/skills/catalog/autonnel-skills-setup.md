---
title: Autonnel Skills - Conversion and Funnel Optimization
description: "autonnel/autonnel-skills - 6 skills, 147.5K combined installs: landing page conversion audits, sales funnel blueprints, server-side conversion tracking, funnel platform selection, post-purchase upsell flows, and self-hosted funnel launches."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/autonnel-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-24"
tags: ["hermes skill", "agent skill", "skill setup", "conversion optimization", "sales funnel", "landing page", "server-side tracking", "upsell"]
---

# Autonnel Skills - Setup Guide

**Source:** [autonnel/autonnel-skills](https://skills.sh/autonnel/autonnel-skills)
**GitHub:** [autonnel/autonnel-skills](https://github.com/autonnel/autonnel-skills) (Apache-2.0, published Aug 19, 2026)
**Skills:** 6 skills, 147.5K combined installs
**Category:** Growth / Conversion Optimization
**First Seen:** August 24, 2026 sweep (skills.sh first-listed Aug 5, 2026)
**Quality Tier:** 🟡 Beta - 147.5K installs and clean Gen Agent Trust Hub + Socket audits, but the source repo is skills.sh-published with no star history yet and two skills carry a Snyk Warn/Fail flag; review before production pipeline use

The Autonnel pack is a complete conversion-optimization workflow for paid traffic: audit the page, blueprint the funnel, pick the platform, wire server-side tracking, bolt on post-purchase upsells, and optionally self-host the whole funnel. Every skill is written for an agent operator - the landing page audit explicitly refuses generic advice ("do not return a generic 'add more social proof' list - every finding must name the element, the failure mode, and what to change it to") and the blueprint skill turns an offer into a page-by-page funnel spec with a price ladder and per-step metric targets.

This is the first skills.sh suite covering the full conversion-funnel lifecycle in one pack, and it maps directly onto the CorpusIQ growth-operations charter: audit corpusiq.io pages, blueprint funnel flows, and fix tracking gaps.

---

## Installation

The maintained-checkout pattern (recommended - keeps the skills updateable with `git pull`):

```bash
git clone https://github.com/autonnel/autonnel-skills.git
```

```yaml
# ~/.hermes/config.yaml
skills:
  external_dirs:
    - /absolute/path/to/autonnel-skills
```

Or via the skills.sh marketplace (single skill):

```bash
npx skills add autonnel/autonnel-skills
# or one skill only:
npx skills add https://github.com/autonnel/autonnel-skills --skill landing-page-conversion-audit
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Traffic or a mockup** | The audit and blueprint skills are diagnosis-by-design; they refuse to run on a page with no traffic yet (they redirect to sales-funnel-blueprint instead) |
| **Ad platform access (tracking skill)** | Server-side conversion tracking needs access to the Meta / TikTok / Google / Bing conversion APIs (CAPI-class) |
| **Hosting (self-hosted skill)** | The self-hosted funnel launch skill needs a server or container host for the funnel builder stack |

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| landing-page-conversion-audit | 24.9K | Audit a live page (or mockup) for conversion leaks on paid traffic and return a fix list ordered by expected revenue impact. Triggers: "review my landing page", "why is my conversion rate so low", CPA above target, checkout drop-off |
| sales-funnel-blueprint | 24.6K | Turn an offer into a concrete multi-step funnel spec: page-by-page structure, price ladder, copy outline, and the metrics each step must hit |
| server-side-conversion-tracking | 24.6K | Set up server-side conversion tracking so purchases report accurately to Facebook, TikTok, Google, and Bing despite iOS restrictions, ad blockers, and cookie decay |
| funnel-platform-picker | 24.5K | Choose a landing page or sales funnel platform by working out the real total cost and lock-in for the specific case (ClickFunnels, CartFlows, and others compared) |
| post-purchase-upsell-flow | 24.5K | Design and implement one-click post-purchase upsells and downsells that raise average order value without hurting the main conversion rate |
| self-hosted-funnel-launch | 24.5K | Deploy a self-hosted funnel builder and take a funnel from empty install to published: landing page, checkout, one-click upsell, thank-you page |

## Security Audit Status (skills.sh, verified Aug 24, 2026)

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| landing-page-conversion-audit | Pass | Pass | Fail |
| server-side-conversion-tracking | Pass | Pass | Fail |
| sales-funnel-blueprint | Pass | Pass | Warn |
| funnel-platform-picker | Pass | Pass | Warn |
| post-purchase-upsell-flow | Pass | Pass | Warn |
| self-hosted-funnel-launch | Pass | Pass | Warn |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Landing page audits** | Run landing-page-conversion-audit against corpusiq.io pages before scaling ad spend - element-named fix lists beat generic CRO advice |
| **Funnel design** | sales-funnel-blueprint turns the CorpusIQ offer into a page-by-page funnel spec with per-step metric targets - a ready input for the frontend team |
| **Tracking gap fix** | server-side-conversion-tracking is the durable fix for iOS/ad-blocker tracking loss on our conversion pixels |
| **Platform decisions** | funnel-platform-picker's total-cost-plus-lock-in math is reusable for any funnel-platform buy decision, not just ClickFunnels-class tools |
| **AOV growth** | post-purchase-upsell-flow is a direct playbook for average-order-value lift without touching the main funnel |

## Limitations / Verification

- Source repo has no star history yet (skills.sh-published Aug 5, 2026); the 147.5K install count is the marketplace's own metric.
- Two skills carry Snyk Fail flags (landing-page-conversion-audit, server-side-conversion-tracking) - review dependencies before running them in a production pipeline; the other four are Warn-level.
- The audit skill is designed to refuse on zero-traffic pages and on wrong-audience problems ("a page audit cannot fix a broken offer; say so and stop") - treat that as a feature, not a bug.

## Related

- [SEO GEO Claude Skills Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup) - search-side of the same conversion funnel
- [Skills Marketplace](/hermes/skills/marketplace) - marketplace index for more discovery batches
