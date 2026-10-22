---
title: "ASO Skills - App Store Optimization Suite Setup"
description: "ASO Skills: 106.5K combined installs. 40 skills for store keyword research, metadata, screenshots, launch, paywall and retention work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/aso-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-22"
tags: ["hermes skill", "agent skill", "skill setup", "app store optimization", "mobile growth", "marketing"]
---

# ASO Skills - Setup Guide

**Source:** [appeeky/aso-skills](https://www.skills.sh/appeeky/aso-skills) via skills.sh - 106.5K combined installs across 40 indexed listings; new to this catalog in the Oct 22, 2026 sweep
**GitHub:** [appeeky/aso-skills](https://github.com/appeeky/aso-skills) (2,199 stars; MIT; pushed 2026-10-06; layout `skills/<name>/SKILL.md` for 40 skills, plus `tools/integrations/`, a `tools/REGISTRY.md` capability matrix and a `.claude-plugin/` marketplace manifest)
**Category:** Marketing / Mobile App Growth
**Quality Tier:** 🟢 Production - MIT, 40 skills that each match a directory in the tree one to one, a documented Agent Skills structure with a validation script, 2,199 stars, and Pass on both sampled skills from Gen Agent Trust Hub and Socket

Forty skills covering the whole App Store and Google Play lifecycle, written as frameworks with scoring rubrics and output templates rather than as links to blog posts. The publisher's framing is that ASO knowledge is usually locked in courses and consultants, so the skills encode the rules and let the agent apply them to real listing data.

Two details separate this from the average skill dump. First, every skill carries the store's own character limits in context: an iOS title is 30 characters, a subtitle 30, the keyword field 100, a description 4000 and not indexed for search; Play allows a 30-character title, an 80-character short description and an indexed 4000-character full description, and the repo states that the title carries the highest keyword weight and that keywords should not be repeated across fields. Second, there is a router. `aso-router` reads a natural-language request and dispatches to the right specialist skill, so a user does not need to memorise 40 names.

## Installation

```bash
npx skills add appeeky/aso-skills
```

```bash
# Cursor
npx skills add appeeky/aso-skills -a cursor

# A subset
npx skills add appeeky/aso-skills --skill aso-audit keyword-research

# As a Claude Code plugin
/plugin marketplace add appeeky/aso-skills
/plugin install aso-skills@aso-skills
```

The skills work standalone on general ASO knowledge. Live data comes from the Appeeky API, either as an MCP server:

```json
{
  "mcpServers": {
    "appeeky": {
      "url": "https://mcp.appeeky.com/mcp",
      "headers": { "Authorization": "Bearer apk_your_key_here" }
    }
  }
}
```

or through Appeeky Connect, which syncs first-party App Store Connect data for the `asc-metrics` skill and requires the Indie plan at eight dollars a month or higher.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| aso-audit | 4,452 | Scores a listing across 10 factors out of 100, flags problems and returns a prioritized fix list |
| monetization-strategy | 3,674 | Pricing tiers, paywall timing, trial structure and category benchmarks |
| keyword-research | 3,671 | Keywords by volume, difficulty and relevance, grouped into primary, secondary and long tail |
| metadata-optimization | 3,554 | Title, subtitle, keyword field and description with three variants and character counts |
| competitor-analysis | 3,511 | Keyword gaps, creative teardown, positioning map and the specific openings to exploit |
| screenshot-optimization | 3,473 | 10-slot screenshot strategy with design briefs, overlay copy and a competitor audit |
| app-marketing-context | 3,358 | Shared context about the app, audience and goals that the other skills read first |
| localization | 3,339 | Market prioritization matrix, per-country keyword research and cultural adaptation checklist |
| app-analytics | 3,316 | Event tracking plan, dashboard setup and a KPI framework with category benchmarks |
| app-launch | 3,308 | 8-week launch timeline with daily checklists, channel strategy and press outreach templates |
| retention-optimization | 3,295 | Activation to habit framework, push sequences and churn prevention |
| app-store-featured | 3,284 | Featuring readiness score, Apple technical checklist, pitch template and events calendar |
| review-management | 3,225 | Sentiment analysis, HEAR-framework reply templates and rating recovery tactics |
| ua-campaign | 3,217 | Apple Search Ads, Meta and Google UAC structure, bidding, creative specs and budget split |
| ab-test-store-listing | 3,211 | Hypothesis to variant design, sample size and interpretation for store listing tests |
| market-pulse | 3,136 | One-screen market briefing: chart moves, trending keywords, featured apps and new launches |
| market-movers | 3,116 | Top chart gainers and losers, new entries and drops, with the likely driver |
| apple-search-ads | 2,861 | Deep Apple Search Ads work: campaign structure, match types, custom product page routing, bids, weekly checklist |
| android-aso | 2,669 | Google Play specifics: indexed description, short description, Play Experiments, rating recovery |
| app-icon-optimization | 2,656 | Icon principles, PPO and Play Experiments testing, category differentiation, icon briefs |
| onboarding-optimization | 2,538 | First-run flow audit, activation event definition, permission prompt timing and sign-up friction |
| rating-prompt-strategy | 2,445 | Review prompt timing, pre-prompt survey, version gating and rating recovery |
| subscription-lifecycle | 2,424 | Trial nurture, voluntary and involuntary churn, dunning and win-back |
| competitor-tracking | 2,412 | Weekly competitor surveillance: metadata and keyword shifts, rating trends, chart deltas |
| asc-metrics | 2,409 | Your own App Store Connect numbers over Appeeky Connect: downloads, revenue, subscriptions, countries |
| in-app-events | 2,396 | Plans In-App Events: copy, image brief, keyword strategy and submission timeline |
| crash-analytics | 2,367 | Crashlytics setup, P0 to P3 triage, symbolication, phased release and rating recovery |
| seasonal-aso | 2,352 | Seasonal keyword calendar, metadata swap strategy and timing checklist |
| press-and-pr | 2,332 | Media targeting tiers, pitch templates, press kit checklist, embargoes and a Product Hunt launch |
| app-clips | 2,320 | App Clip use cases, card design, URL scheme, SKOverlay handoff and measurement |
| paywall-optimization | 1,869 | Paywall funnel diagnostic, 7-element audit and an A/B playbook for Superwall, RevenueCat or Adapty |
| app-preview-video | 1,828 | Up to three App Preview videos per locale with a script template and rejection avoidance |
| creator-ugc-marketing | 1,816 | Creator programme briefs, sourcing, hook angles, Spark and Partnership Ads, measurement |
| app-rejection-recovery | 1,775 | Diagnoses Apple or Google rejections by guideline and drafts a Resolution Center reply |
| category-positioning | 1,772 | Primary and secondary category choice: competitive density, featuring odds, switch cost |
| custom-product-pages | 1,751 | Apple custom product pages: variant strategy, Search Ads routing, measurement floor, common mistakes |
| attribution-setup | 1,729 | SKAdNetwork 4 and AdAttributionKit setup, conversion values and deep link debugging |
| web-to-app-funnel | 1,714 | Web to app funnels that route subscriptions around store fees, with deferred deep links |
| referral-program | 1,697 | Referral mechanics: reward sizing, K-factor math, fraud prevention and deep link flow |
| aso-router | 231 | Single entry point that reads a request and routes it to the right specialist skill |

All 40 indexed listings clear the 200-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

App store copy is a hard-constraint writing job, and hard constraints are where language models fail quietly. A model asked for a subtitle will happily return 47 characters, and a model asked for a keyword field will repeat the app name and waste the 100-character budget. Here the limits and the weighting rules are in the skill text, so the agent drafts inside the box instead of producing something a reviewer has to fix.

The suite also encodes sequence. A listing audit scores 10 factors out of 100 and returns a prioritized fix list, which is the difference between "improve your listing" and a work queue. The growth skills then extend the same discipline past the listing: screenshot slots with design briefs, a paywall funnel diagnostic, a launch timeline with daily checklists, an attribution schema.

The market-intelligence skills are the part that needs live data, and they are honest about it. `market-pulse`, `market-movers` and `competitor-tracking` become useful when Appeeky is connected and stay generic when it is not, which is a better failure mode than pretending to know chart positions.

For a Hermes setup, the practical shape is a monthly routine: audit, fix the prioritized items, check competitor deltas, review the ratings. Each step is one skill call with a written output, so the routine can be scheduled and diffed against last month.

## Usage

| You say | What happens |
|---|---|
| "Run an ASO audit for my app" | `aso-audit` scores the listing on 10 factors out of 100 and returns a prioritized fix list |
| "Find keywords for a meditation app" | `keyword-research` returns volume, difficulty and relevance, grouped into primary, secondary and long tail |
| "Rewrite my title and subtitle" | `metadata-optimization` returns three variants with character counts inside the store limits |
| "What are competitors ranking for that I am not?" | `competitor-analysis` returns keyword gaps, a positioning map and the openings worth taking |
| "What is moving in Health and Fitness?" | `market-pulse` returns chart moves, trending keywords, featured apps and new launches in one briefing |
| "My ratings dropped" | `review-management` runs sentiment analysis and returns HEAR-framework reply templates plus recovery tactics |
| "Plan my Christmas in-app event" | `in-app-events` returns copy, an image brief, keywords and a submission timeline |
| "I do not know which skill I need" | `aso-router` reads the request and dispatches to the right specialist |

## Verification

Confirm the install and the router:

```bash
npx skills list | grep -i aso
```

Read a skill before installing it, for example the audit skill:

```bash
curl -s https://raw.githubusercontent.com/appeeky/aso-skills/main/skills/aso-audit/SKILL.md | head -40
```

Check which tool a skill expects before wiring data:

```bash
curl -s https://raw.githubusercontent.com/appeeky/aso-skills/main/tools/REGISTRY.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Oct 22, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| aso-audit | Pass | Pass | Warn |
| keyword-research | Pass | Pass | Pass |

The one warning, on `aso-audit`, is MEDIUM W011: the workflow optionally fetches app metadata, reviews and competitor information, so untrusted text from other apps' listings reaches the model. That is inherent to competitor analysis and worth knowing rather than fixing. `keyword-research` is clean on all three scanners.

The credential to protect is the Appeeky key. It belongs in the MCP server configuration, not in a prompt, and it should be a scoped key rather than an account-level one. Nothing in the suite writes to a store listing: every skill produces copy or a plan for a human to publish.

## Limitations

- Live data needs Appeeky. Without the MCP server or an API key, the market-intelligence skills fall back to framework advice.
- `asc-metrics` reads first-party App Store Connect data only through Appeeky Connect on the Indie plan or higher, which is a paid dependency the free skills do not advertise loudly.
- The suite is ASO-first. Paid user acquisition is documented in a separate repo, ua-skills, and the boundary is easy to miss when you only install this one.
- Store rules change. The character limits and keyword rules are correct at this snapshot but Apple and Google revise them, so verify against the current guidelines before shipping copy.
- Outputs are templates and plans. Publishing still needs store credentials and a human review pass, and one skill, `app-rejection-recovery`, exists precisely because that last mile goes wrong.
- Snapshot data, verified Oct 22, 2026: 106,503 combined installs across 40 indexed listings; 2,199 GitHub stars; MIT; last pushed 2026-10-06. Counts drift over time.

## Related

- [App Store Connect CLI - Mobile Release Automation Setup](/hermes/skills/catalog/app-store-connect-cli-skills-setup)
- [Marketing Skills - Content Ops Setup](/hermes/skills/catalog/zc277584121-marketing-skills-setup)
- [Kostja94 Marketing Skills - Copywriting, SEO, Ads Setup](/hermes/skills/catalog/kostja94-marketing-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load `app-marketing-context` first. It carries the app, audience and goals that the other skills read, and skipping it makes every later answer generic.
- Ask for three metadata variants every time. The skill produces them by default and the comparison is where the useful judgment happens.
- Connect Appeeky before running `competitor-tracking`. Without live data it produces a surveillance plan, not a delta report.
- Treat `aso-audit` scores as a baseline, then re-run after changes. The 0-100 score is only useful as a trend.
- Hand the output to a person before publishing. Character limits are checked in the skill, but naming, claims and screenshots still need an owner.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
