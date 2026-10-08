---
title: "mbfinotti Business Skills - Sales, RevOps & Advertising"
description: "Setup guide to the mbfinotti family: 108 interview-based sales, RevOps, advertising, and partnerships skills across 4 MIT repos, ~637K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mbfinotti-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-08"
tags: ["hermes skill", "agent skill", "skill setup", "sales", "revops", "advertising"]
---

# mbfinotti Business Skills - Setup Guide

**Source:** [mbfinotti/sales-skills](https://github.com/mbfinotti/sales-skills), [advertising-skills](https://github.com/mbfinotti/advertising-skills), [revops-skills](https://github.com/mbfinotti/revops-skills), [partnerships-skills](https://github.com/mbfinotti/partnerships-skills) (0-1 stars each, MIT LICENSE; last pushed Sep 14, 2026)
**Skill family:** mbfinotti business-skills family - 4 repos, 108 skills (sales 27, advertising 31, revops 20, partnerships 30)
**Combined Installs:** ~637,148 across 108 skills in 4 repos (Oct 8, 2026 snapshot)
**Category:** Business Operations / Sales, RevOps & Advertising
**Quality Tier:** Beta - high-quality operator content, MIT, interview-based design, single-author with modest stars; verified Oct 8, 2026

mbfinotti is a four-repo, 108-skill family for running the revenue side of a business: sales-skills (27) for running a sales org and closing deals, advertising-skills (31) for spending paid media budget on purpose, revops-skills (20) for the systems behind the number, and partnerships-skills (30) for channel, affiliate, referral, and creator operations. The author (Maya-Beth Finotti) built the collections for colleagues at Nativa Labs, and the design is consistent across all four: every skill is interview-driven - it asks multiple-choice clarifying questions before acting - and every skill ends in a decision or a ship-able artifact (a scorecard, a routing spec, a metric tree, a rate card), never a generic explainer. Coverage spans market sizing, ICP, quota and comp design, MEDDPICC and negotiation in sales; channel selection, budget policy, audience design, creative development, and measurement across search, paid social, video, native, and AI-answer surfaces in advertising; funnel design, lead scoring and routing, pipeline hygiene, forecasting, health scoring, and CRM data governance in RevOps; and partner economics, co-selling, affiliate program mechanics, referral incentives, and influencer deals in partnerships. The evidence standard is real: alliance-prioritization cites Kale, Dyer & Singh (2002), finding 63% vs 50% alliance success across 1,572 alliances, and diagnosis skills such as ad-account-diagnostic return a prioritised verdict with evidence and confidence.

---

## Installation

```bash
# Full family (recommended - install all four repos, not single skills)
npx skills add mbfinotti/sales-skills
npx skills add mbfinotti/advertising-skills
npx skills add mbfinotti/revops-skills
npx skills add mbfinotti/partnerships-skills

# Or pick a single skill
npx skills add mbfinotti/sales-skills --skill sales-pipeline-coverage-modeling
```

The READMEs ask for a full-repo install: the skills are atomic by design and reference each other freely, so a single-skill install leaves sibling references and routed handoffs pointing at skills that are not present. Host-specific install paths for Claude.ai, Claude Code, Codex, Cursor, and Gemini CLI are documented in each README.

## Roster - mbfinotti/sales-skills (27 skills, ~208,882 installs)

The sell-side surface, from market sizing to negotiation:

| Skill | Installs | What It Does |
|---|---|---|
| sales-pipeline-coverage-modeling | 7,877 | Models how much pipeline the team needs relative to quota: coverage ratios from win rates, segment targets, and pipeline-gap math with in-quarter timing |
| sales-icp-definition | 7,888 | Defines the ICP with weighted scoring criteria, explicit disqualifiers, and a refresh cadence, from closed-won data or founder discovery |
| sales-market-sizing | 7,864 | Estimates TAM, SAM, and SOM by triangulating top-down, bottom-up, and value-theory methods, capped by sales-capacity limits |
| sales-account-tiering | 7,852 | Sets tier cutoffs above a fit score, with accounts-per-rep caps, a coverage model per tier, and a recalibration cadence |
| sales-career | 7,849 | Coaches a candidate through breaking into sales, SDR-to-AE promotion, interview prep, and evaluating an offer against dated benchmarks |
| sales-kickoff | 7,817 | Router: sends any broad sales request to the one skill that fits and bootstraps the project's shared sales-context file |
| sales-hiring | 7,851 | Builds the employer-side hiring loop: outcome scorecard, structured interview bank, scored mock-call work sample, 30-60-90 ramp plan |
| sales-objection-handling | 7,690 | Diagnoses what an objection really means - writes rebuttals a rep can say out loud, or calls the deal dead when the constraint is real |
| sales-radar | 7,838 | Assembles a dated, verified watch list of sales podcasts, newsletters, communities, and benchmark reports matched to your role |
| sales-account-segmentation | 7,654 | Builds the weighted account fit score from firmographic, technographic, and intent signals, calibrated on closed-won deals |
| sales-meeting-recap | 7,670 | Converts raw call notes into a recap email where every next step carries an owner, a date, and a deliverable |
| cold-email-deliverability | 7,759 | Audits sending setup and draft mechanics for inbox placement: SPF/DKIM/DMARC alignment, sender reputation, body hygiene, regional compliance |

## Roster - mbfinotti/advertising-skills (31 skills, ~184,239 installs)

Paid media work across search, paid social, video, native, and AI-answer surfaces:

| Skill | Installs | What It Does |
|---|---|---|
| ad-creative-brief | 5,934 | Turns a campaign goal and audience insight into a brief a designer or creator can execute, with specs and a revision loop |
| ad-account-diagnostic | 5,914 | Diagnoses the root cause of an underperforming ad account and returns a prioritised verdict with evidence and confidence |
| ad-spend-allocation | 5,910 | Splits a fixed budget across campaigns, platforms, funnel stages, and audiences based on expected marginal return |
| retargeting-funnel | 6,048 | Designs a staged retargeting sequence with recency windows, behavioural depth tiers, a message ladder, and per-stage frequency caps |
| advertising-career | 6,165 | Plans a paid media career: the junior-to-lead ladder, interview formats, an NDA-safe portfolio, and pay conversations |
| ad-conversion-tracking | 5,929 | Verifies conversion events fire once and deduplicate before launch, then turns the evidence into a GO or NO-GO decision |
| paid-media-scaling | 6,080 | Decides when a proven campaign has earned a budget increase, how large each step should be, and what triggers a rollback |
| ad-budget-pacing | 5,914 | Tracks spend against budget and flags under- or over-pacing early: pacing ratio, projected spend, corrective daily spend |
| ad-swipe-file | 5,908 | Builds a queryable library of competitors' running ads by format, hook, offer, and funnel stage, then ranks test hypotheses |
| ad-audience-targeting | 5,895 | Turns an ICP and buying signals into layered audience tiers sized against platform floors and exclusion rules |
| ad-platform-selection | 5,906 | Decides which paid channel families fit the business economics, audience, funnel stage, and budget before campaigns get built |
| ad-creative-test-plan | 5,924 | Designs a pre-launch creative test with a falsifiable hypothesis, per-cell budgets, required sample, and kill or scale rules |

## Roster - mbfinotti/revops-skills (20 skills, ~125,281 installs)

The systems behind the number, from funnel design to CRM governance:

| Skill | Installs | What It Does |
|---|---|---|
| sales-forecast-diagnostic | 6,297 | Diagnoses why a forecast misses, separating data-quality problems from rep behaviour from genuine demand, and recommends targeted fixes |
| pipeline-stage-definition-audit | 6,322 | Audits stage definitions against buyer-verifiable milestones and flags exit criteria built on rep activity instead |
| revenue-funnel | 6,325 | Designs a revenue funnel model from scratch: stage set, unit of analysis, conversion assumptions, ownership handoffs |
| revops-radar | 6,297 | Assembles a time-budgeted watch list of RevOps podcasts, newsletters, communities, events, and people, each verified active |
| revops-hiring | 6,292 | Produces a complete RevOps hiring packet: outcome scorecard, interview stage map, work-sample rubric, and a 30-60-90 ramp |
| revenue-kpi-framework | 6,313 | Designs the org-wide KPI tree: metric math from board to IC, branch ownership, and guardrail counter-metrics per owned number |
| revops-kickoff | 6,315 | Router: sends any RevOps task to the right skill and bootstraps a versioned project context so later sessions start warm |
| crm-data-governance | 6,372 | Produces CRM field-level governance: field dictionary, per-field ownership, write-precedence rules, freshness SLAs, enforcement |
| revops-career | 6,320 | Builds a RevOps career plan: ladder placement by scope, competency gap roadmap, evidence ledger, and a compensation ask |
| sales-pipeline-hygiene | 6,324 | Runs a checklist audit over a live pipeline snapshot and returns an exception list, a disposition per deal, and a pass threshold |
| revenue-leakage | 6,314 | Traces where deals silently exit one funnel and sizes the loss in recoverable dollars, separating leaks from healthy disqualification |
| revenue-data-governance-strategy | 6,261 | Sets org-wide source-of-truth policy per object class, an identity-resolution spine, and a data-contract register |

## Roster - mbfinotti/partnerships-skills (30 skills, ~118,746 installs)

Channel, alliance, affiliate, referral, and creator operations:

| Skill | Installs | What It Does |
|---|---|---|
| alliance-prioritization | 4,073 | Ranks named candidate alliances by expected value, effort, and risk into a shortlist and a go/no-go recommendation memo |
| partner-ecosystem-expansion | 3,959 | Sequences which partner categories to launch next into a staged roadmap with readiness gates, capacity limits, and kill criteria |
| influencer-campaign-brief | 3,953 | Writes the creative brief for a signed creator: deliverable specs, key messages, guardrails, disclosure, bounded review rounds |
| partnerships-kickoff | 3,947 | Router: sends a partnerships task to exactly one sibling skill and bootstraps the shared project context file |
| co-selling-strategy | 3,945 | Defines how direct and partner sellers share deals: registration policy, deal credit splits, rules of engagement, comp neutrality |
| influencer-discovery-brief | 3,944 | Defines weighted sourcing criteria and knockout screens, then produces a ranked creator shortlist with evidence per score |
| affiliate-payout-audit | 4,102 | Audits a commission payout run before disbursement and returns findings by severity with recommended holds |
| partner-economics | 3,932 | Models one partner's P&L - margin, cost-to-serve, partner CAC, ramp, payback - to decide sign, scale, renegotiate, or exit |
| partner-tiering | 3,929 | Designs the tier ladder inside an existing program: qualification criteria, benefit bundles, promotion and demotion rules |
| partner-channel-conflict | 3,929 | Writes the channel conflict rules for contested deals: account segmentation, carve-outs, tie-breaks, escalation ladders |
| partnerships-hiring | 3,928 | Plans partnerships hiring: job posting and scorecard, interview loop, sourcing, and compensation stance |
| partner-channel-program | 3,927 | Designs a partner program from scratch: readiness gate, partner value proposition, motions, tiers, benefits, economics envelope |

## Why This Matters for Hermes Agents

These are operator-level business workflows - pipeline coverage modeling, ICP definition, ad account diagnosis, partnership and affiliate operations - which is exactly the kind of work business teams bring to AI agents once the agent can hold context and produce artifacts. Each skill runs as a short interview and returns something ship-able (a scorecard, routing spec, concession plan, or rate card), so a Hermes agent can run a sales, RevOps, advertising, or partnerships engagement end to end without improvising its own structure. Because sibling skills read the same shared context file, a session that starts at a kickoff router can hand off to pipeline, comp, or negotiation skills with the context intact.

## Verification

```bash
# Confirm the family is installed (all four repos should appear)
npx skills list | grep mbfinotti

# Smoke-test the interview flow with your agent host
# Prompt: "Run sales-pipeline-coverage-modeling for a 6-rep team carrying a $4M quota"
# Expected: clarifying questions first, then a coverage model with segment-level gap math.
```

## Security

skills.sh per-skill verdicts (sampled 3 skills, verified Oct 8, 2026). All sampled verdicts were Pass across scanners; verdicts vary per skill, so check a skill's security page on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sales-pipeline-coverage-modeling | Pass | Pass | Pass |
| ad-creative-brief | Pass | Pass | Pass |
| alliance-prioritization | Pass | Pass | Pass |

## Limitations

- Verified Oct 8, 2026: four MIT repos, created Sep 5, 2026, first seen on skills.sh Sep 13, 2026, and last pushed Sep 14, 2026; 0-1 stars and 0-1 forks each.
- Single-author family (mbfinotti, built per the READMEs for colleagues at Nativa Labs). Modest community traction: the case for installing rests on content quality and the interview-based design, not stars.
- Dormant since Sep 14, 2026, so platform-adjacent details in the skills (ad platform behavior, CRM fields) should be sanity-checked against the current tools.
- Install counts are a single Oct 8, 2026 skills.sh snapshot; the ~637,148 combined figure (108 skills) moves with the index, so treat it as approximate.
- Roster tables show 12 representative skills per repo; the full repos ship 27 / 31 / 20 / 30 skills.
- No live install test was performed as part of this guide; design details come from the repo READMEs and the Oct 8, 2026 data snapshot.

## Related

- [HubSpot Agent CLI Skills - CRM Operations Setup](/hermes/skills/catalog/hubspot-agent-cli-skills-setup)
- [Digital Marketing Pro - AI Marketing OS Setup](/hermes/skills/catalog/digital-marketing-pro-setup)
- [Apify Growth Skills - Lead Gen and Brand Monitoring](/hermes/skills/catalog/apify-growth-skills-setup)
- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

1. **Install whole repos, not single skills.** Each collection is designed to cross-reference; a single-skill install breaks routed handoffs to sibling skills.
2. **Start at the kickoff router.** sales-kickoff, advertising-kickoff, revops-kickoff, and partnerships-kickoff route the request and bootstrap the shared context file that makes later sessions start warm.
3. **Answer the clarifying questions.** The multiple-choice interview is what keeps outputs specific to your situation; telling the agent to skip it degrades the artifact toward generic advice.
4. **Feed real data first.** Point the agent at your CRM export, ad platform report, or partner tracker before running a skill; the models and scorecards are only as good as the inputs.
5. **Sample before you standardize.** Run one skill per repo against live data, review the artifact quality, then decide which of the four repos to roll out to the team.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
