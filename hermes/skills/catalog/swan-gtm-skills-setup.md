---
title: "Swan GTM Skills - Go-to-Market Suite Setup"
description: "swan-gtm/gtm-skills - 3.5K combined installs: open go-to-market skills for prospecting, research, outreach, signals and pipeline."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/swan-gtm-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "go-to-market", "cold email", "outreach"]
---

# Swan GTM Skills - Setup Guide

**Source:** [swan-gtm/gtm-skills](https://www.skills.sh/swan-gtm/gtm-skills) via skills.sh - 3.5K combined installs across 96 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 morning sweep)
**GitHub:** [swan-gtm/gtm-skills](https://github.com/swan-gtm/gtm-skills) - 247 stars, MIT license, last pushed Nov 23, 2026, main branch; skills under skills/<creator>/<skill>/SKILL.md, each with an optional references/ directory and an author.md profile.
**Category:** Go-to-Market
**Quality Tier:** 🟡 Yellow - all 15 sampled skills pass Socket and none fail; icp carries a Gen Agent Trust Hub Warn and four skills carry Snyk Warns.

swan-gtm/gtm-skills is Swan's open, production-grade go-to-market skill library, built and curated by Swan and authored by the GTM community. The 96 indexed skills span prospecting, research, outreach, signals, pipeline and RevOps, and every skill is a plain SKILL.md that Claude Code, Cursor, Codex and 70+ other agents can read. The skills speak in GTM verbs rather than vendor tool names, so the guidance works whatever your stack is.

The install band is flat, 29 to 87 installs across all 96 listings, because one install pulls the whole set: a shape of the distribution rather than a defect. Skills live under skills/<creator>/<skill>/SKILL.md with optional references/ directories, and full execution runs natively inside Swan with tools wired.

## Installation

Install one skill, everything from one creator, or the whole library (interactive picker):

```bash
# one skill
npx skills add swan-gtm/gtm-skills --skill reach-out

# everything from one creator
npx skills add swan-gtm/gtm-skills/skills/ido-goldberg

# the whole library (interactive picker)
npx skills add swan-gtm/gtm-skills
```

Add -a claude-code, -a cursor, or -a codex to target a specific agent; use --list to see what is available.

## What It Provides

skills.sh publishes per-skill descriptions for all 96 indexed listings, and each has a matching skills/<creator>/<skill>/SKILL.md in the current tree.

| Skill | Installs | Use For |
|---|---|---|
| outreach-messaging | 87 | value-first B2B cold email with the R.E.P.L.Y. framework |
| icp-builder | 80 | build, validate and expand an ICP with the GAP method and SPICED |
| build-list | 72 | build prospect lists of companies, contacts or both |
| category-of-one-positioning | 66 | category-of-one positioning package via the Atticus Method |
| seo-topic-research-pipeline | 54 | B2B and SaaS SEO content roadmap in seven phases |
| anti-ai-slop-writing | 54 | strip the machine tells from GTM copy before it ships |
| cold-email-strategist | 53 | cold email sequences, deliverability and personalization |
| aeo-visibility-tracking | 52 | measure brand visibility in AI-generated answers |
| reach-out | 50 | create outreach for a company, contact, list or signal |
| b2b-cold-email-copywriting | 50 | B2B Boosted cold email system for replies at volume |
| icp | 49 | define and refine who the org sells to |
| ad-copywriting | 46 | ad copy with headline formulas and voice-of-customer |
| research | 44 | research a company, person, committee or signal |
| positioning-messaging-designer | 42 | positioning and messaging frameworks |
| josh-braun-copywriting | 42 | Josh Braun's five cold email principles |
| signal-sourcer | 41 | signal-based selling across buying signals and intent |
| cold-email-4-sequence | 40 | the standard 4-email sequence for B2B prospecting |

The remaining 79 indexed listings range from 29 to 39 installs.

## Why This Matters for Hermes Agents

Go-to-market work is judgment-heavy: which account to pursue, which signal matters, and how to write a reply-worthy cold email. This library packages operator judgment as agent-readable skills so an agent can run prospecting, research, outreach and pipeline motions with the playbook a senior operator would apply. The collection spans 96 skills across prospecting, ICP definition, positioning, cold email, signals, ads and RevOps, each a plain SKILL.md that works in Claude Code, Cursor, Codex and 70+ other agents. Because the skills speak in GTM verbs rather than vendor tool names, the guidance survives whatever stack you plug in. For a builder, "build a list and reach out" becomes a staged workflow with hooks, voice-matching and sequence shape rather than a template dump.

## Usage

| You say | What happens |
|---|---|
| Write a cold email sequence | Uses cold-email-strategist or b2b-cold-email-copywriting for sequences |
| Build a prospect list | Uses build-list to produce target accounts or contacts |
| Define who we sell to | Uses icp-builder or icp to shape and validate the ICP |
| Research this company before outreach | Uses research to produce a sourced answer with confidence notes |
| Make this draft sound human | Uses anti-ai-slop-writing to strip the machine tells |
| Track our visibility in AI answers | Uses aeo-visibility-tracking to seed prompts and track brand presence |
| Find buying signals for this account | Uses signal-sourcer for signal-based selling |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/swan-gtm/gtm-skills/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/swan-gtm/gtm-skills/main/skills/ido-goldberg/reach-out/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<creator>/<skill>/SKILL.md before relying on it.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| outreach-messaging | Pass | Pass | Pass |
| icp-builder | Pass | Pass | Pass |
| build-list | Pass | Pass | Pass |
| category-of-one-positioning | Pass | Pass | Pass |
| seo-topic-research-pipeline | Pass | Pass | Pass |
| anti-ai-slop-writing | Pass | Pass | Warn |
| cold-email-strategist | Pass | Pass | Pass |
| aeo-visibility-tracking | Pass | Pass | Warn |
| reach-out | Pass | Pass | Pass |
| b2b-cold-email-copywriting | Pass | Pass | Pass |
| icp | Warn | Pass | Warn |
| ad-copywriting | Pass | Pass | Pass |
| research | Pass | Pass | Warn |
| positioning-messaging-designer | Pass | Pass | Pass |
| josh-braun-copywriting | Pass | Pass | Pass |

Sampled 15 of 96 indexed listings. No Fail verdicts; icp carries the only Gen Agent Trust Hub Warn and four skills carry Snyk Warns.

## Limitations

- Snapshot data, verified Nov 25, 2026: 3,452 combined installs across 96 indexed listings; 247 GitHub stars; MIT license; last pushed Nov 23, 2026. Counts drift over time.
- The install band is flat (29 to 87 installs across the 96 listings) because one install pulls the whole set; it is a shape of the distribution, not a defect.
- Skills are authored by many community contributors and organized under skills/<creator>/<skill>/; some also ship an optional swan.md Swan-specific execution layer.
- Full execution (tools wired) runs natively inside Swan; elsewhere the skills are plain SKILL.md guidance.
- Only 15 of the 96 listings were sampled for the security verdicts; the other 81 have no sampled verdict in this snapshot.

## Related

[Claude GTM Plugin Skills - GTM Teams Setup](/hermes/skills/catalog/claude-gtm-plugin-setup) | [Boring Marketing Skills - Marketing Operator Suite Setup](/hermes/skills/catalog/boring-marketing-skills-setup) | [Infrasity Dev GTM Skills - SEO, GEO and Marketing Setup](/hermes/skills/catalog/infrasity-dev-gtm-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install one skill with npx skills add swan-gtm/gtm-skills --skill reach-out, or the whole library with npx skills add swan-gtm/gtm-skills.
- Add -a claude-code, -a cursor or -a codex to target a specific agent.
- Browse the full library at gtmskills.com before installing.
- Read each creator's author.md profile for context on who wrote the skill.
- Remember full execution with tools wired runs natively inside Swan.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
