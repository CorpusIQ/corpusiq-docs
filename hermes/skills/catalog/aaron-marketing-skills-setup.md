---
title: "Aaron Marketing Skills - Full Marketing Department Setup"
description: "Aaron Marketing Skills: 130.5K combined installs across 134 listings. 120 skills for SEO, GEO, social, email, paid ads, influencer and launch."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/aaron-marketing-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "marketing", "growth"]
---

# Aaron Marketing Skills - Setup Guide

This is an attempt to ship a whole marketing department as agent skills. The repository carries 120 skills in seven disciplines, 16 each: brand narrative, SEO/GEO, social, email, paid ads, influencer and launch, plus a protocol layer of seven append-only registries and a memory store. Each discipline runs its own four-phase lifecycle, from research through implementation and tuning to evaluation, and each ends in a typed auditor with a scoring profile rather than a free-form review.

The engineering is heavier than most prompt suites. Skills live at `<discipline>/<phase>/<skill>/SKILL.md`, the plugin exposes eight slash commands, and the repo ships 107 files under `scripts/` (93 Python, 13 Bash, standard library only) for validation, evals, registry events and release packaging, plus a hooks manifest that fires on session start, prompt submit and tool use. Version 20.1.0 is declared in the plugin manifest, and the author documents install paths for Claude Code, Codex, Cursor, Gemini CLI, OpenClaw, Hermes and the skills CLI.

**Source:** [aaron-he-zhu/aaron-marketing-skills](https://www.skills.sh/aaron-he-zhu/aaron-marketing-skills) via skills.sh - 130.5K combined installs across 134 indexed listings; first seen Jun 28, 2026
**GitHub:** [aaron-he-zhu/aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills) (3.0K stars; Apache License 2.0; branch main, pushed 2026-10-27; layout `<discipline>/<phase>/<skill>/SKILL.md` for 120 skills plus `protocol/<registry>/SKILL.md`, with `.claude-plugin/`, `marketplace.json`, `openclaw.plugin.json`, eight `commands/` files, a `scripts/` toolchain and per-skill `evals/`)
**Category:** Marketing / Full-Funnel Marketing Operations
**Quality Tier:** 🟡 Beta - Apache-2.0, 3.0K stars, version 20.1.0, 120 skills with typed auditors, evals and CI scripts, and a documented install path for 70+ hosts, but Snyk returns a warning on all three sampled skills, Gen Agent Trust Hub also warns on keyword-research, and the install index carries 134 listings against 120 skill directories

## Installation

```bash
# Any host that reads the skills format (Codex, Cursor, OpenCode, Gemini CLI, Hermes and others)
npx skills add aaron-he-zhu/aaron-marketing-skills

# One skill only
npx skills add aaron-he-zhu/aaron-marketing-skills -s keyword-research
```

```bash
# Claude Code: register the marketplace, then install the plugin
/plugin marketplace add aaron-he-zhu/aaron-marketing-skills
/plugin install aaron-marketing@aaron
```

The marketplace step only registers the catalog; without the install step the skills and the eight slash commands are not enabled. The runtime needs Node and `npx` for the skills CLI, and Python 3 plus Bash for the repository's own scripts, which the README describes as standard library only with no `pip` step. Per-agent quirks are documented in `docs/agent-compatibility.md`, where the author records 120 of 120 skills installable as of 2026-07. The plugin adds nothing to `/mcp`; `docs/mcp-catalog.json` is a copy-paste reference, not a connection.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| keyword-research | 1,925 | Find keywords by volume, difficulty, intent and topic cluster from exports or connected tools |
| content-writer | 1,844 | Draft new SEO pages or refresh decaying content, placing keywords, headings and internal links |
| geo-content-optimizer | 1,678 | Improve citation readiness for ChatGPT, Perplexity, AI Overviews, Gemini and Claude |
| content-quality-auditor | 1,549 | Audit publish readiness with an 80-item CORE-EEAT profile, veto checks and a fix plan |
| competitor-analysis | 1,535 | Benchmark competitor keywords, content, backlinks and AI citations into an action plan |
| technical-seo-checker | 1,524 | Check crawlability, indexing, Core Web Vitals, robots.txt, sitemaps, canonicals and redirects |
| content-gap-analysis | 1,484 | Map competitor-relative coverage gaps into editorial calendar opportunities |
| short-video-scripter | 1,454 | Write TikTok, Reels and Shorts scripts with timestamped beats and a hook fix |
| serp-analysis | 1,414 | Map SERP features, layout, intent, AI Overviews and snippet opportunities for a query |
| serp-markup-builder | 1,388 | Write title tags, meta descriptions, Open Graph cards and JSON-LD schema |
| site-structure-optimizer | 1,376 | Plan page hierarchy, URL taxonomy and internal linking, and find orphan pages |
| offsite-signal-analyzer | 1,344 | Profile referring domains, anchor-text mix, toxic links and AI referral traffic |
| rank-tracker | 1,310 | Track keyword and SERP position deltas over time, including AI answer checks |
| domain-authority-auditor | 1,308 | Audit domain trust with a 40-item CITE profile and manipulation veto checks |
| on-page-seo-checker | 1,299 | Score titles, meta, headers, keyword placement, links and images on a single page |
| performance-monitor | 1,279 | Build multi-metric SEO dashboards and alert rules for ranking and traffic drops |
| page-play-builder | 1,229 | Build programmatic pages at scale, including versus and alternative pages on borrowed authority |
| pitch-narrative-builder | 1,082 | Turn the narrative canon into a pitch deck story and a sales pitch structure |
| content-amplifier | 1,059 | Choose which creator posts to boost and set up whitelisting or Spark Ads |
| memory-management | 1,056 | Store and review project context across HOT, WARM and COLD memory, or erase a subject |
| landing-optimizer | 1,052 | Check message match and conversion on a landing page built for influencer traffic |
| deliverability-qa | 1,051 | Run a pre-send check on SPF, DKIM, DMARC, BIMI and sender reputation |
| audience-mapper | 1,047 | Profile a target audience or niche community before creator targeting |
| influencer-discovery | 1,046 | Build a multi-platform creator candidate pool with evidence profiles |
| conversion-signal-qa | 1,044 | QA UTMs, pixels and event firing before launch, including dedup rules |
| search-term-miner | 1,042 | Harvest converting search terms and build negative keyword lists from paid data |
| competitor-tracker | 1,042 | Track which creators competitors partner with and benchmark their programs |
| attribution-reconciler | 1,042 | Reconcile platform-reported conversions against GA4 when Meta and Google double count |
| campaign-planner | 1,041 | Plan, track and close an influencer campaign, including late corrections |
| budget-optimizer | 1,041 | Allocate influencer budget across tiers, platforms and formats with ROI and CPM scenarios |
| brief-generator | 1,040 | Write a creator brief with deliverables, key messages, creative direction and disclosure |
| trend-spotter | 1,039 | Rank trending topics by brand fit and time a campaign around a cultural moment |
| campaign-architect | 1,038 | Design paid account structure, Search versus PMax, ad groups and cannibalization checks |
| audience-segment-builder | 1,038 | Build value-based, lookalike and suppression segments from a customer list |
| outreach-manager | 1,037 | Write creator outreach and negotiation, or pitch a journalist, hunter or launch partner |
| ad-creative-builder | 1,037 | Produce RSA headlines, descriptions, hooks and an angle matrix at volume |
| ad-account-auditor | 1,035 | Audit a paid account for incremental contribution and wasted spend before scaling |
| email-render-builder | 1,034 | Code responsive email HTML and QA dark mode and client rendering |
| contract-helper | 1,034 | Draft or review an influencer agreement: scope, compensation, rights and exclusivity |
| brand-language-codifier | 1,034 | Codify brand voice, naming rules and a tone guide with banned phrases |
| ad-test-designer | 1,034 | Design A/B, creative, landing and incrementality tests with a materiality read |
| social-creative-builder | 1,032 | Turn one idea into platform-native posts and spec carousel slides |
| performance-analyzer | 1,032 | Score influencer campaign results per creator against targets and benchmarks |
| email-creative-builder | 1,032 | Write subject line variants, preheader, body copy and one clear call to action |
| audience-belief-mapper | 1,032 | Map buyer beliefs, recurring objections and switching forces for a beachhead |
| strategic-narrative-designer | 1,031 | Build the old-world-to-new-game story arc for a category shift |
| email-sequence-designer | 1,031 | Design welcome, abandoned cart, re-engagement and cold outbound sequences |
| cold-outbound-sequencer | 1,031 | Build B2B cold outbound with reply triage, domain warmup and compliance |
| landing-experience-checker | 1,030 | Pre-launch a landing page for ad-to-page message match and quality score |
| budget-pacing-monitor | 1,030 | Check spend pacing against target and explain mid-flight spikes or stalls |
| product-feed-optimizer | 1,029 | Fix Shopping feed disapprovals and rewrite product titles and attributes |
| bid-strategy-planner | 1,028 | Choose tCPA, tROAS, max conversions or manual CPC and plan the learning phase |
| report-generator | 1,025 | Produce executive, client and team versions of a campaign report |
| fit-scorer | 1,025 | Rank creators for a campaign with a STAR suitability read and a fit rationale |
| category-narrative-mapper | 1,025 | Map the category narrative and the language conventions competitors use |
| placement-exclusion-manager | 1,024 | Build brand safety exclusions for placements, topics, networks and audiences |
| crisis-response-planner | 1,024 | Build a social crisis protocol with a 1 to 5 severity ladder and pause triggers |
| email-quality-auditor | 1,023 | Audit an email program with a 20-item SEND profile and consent and claim vetoes |
| dark-social-attributor | 1,022 | Measure dark social with a how-did-you-hear field and modeled direct traffic |
| social-calendar-builder | 1,021 | Build the posting calendar with weekly slots, queue depth and evergreen recycling |
| roi-calculator | 1,021 | Compute influencer ROI, ROAS, earned media value and LTV-based return |
| positioning-mapper | 1,021 | Produce a Dunford-style positioning canvas and name the beachhead segment |
| message-system-architect | 1,021 | Author the durable message house: main narrative, three pillars and tagline |
| dynamic-content-personalizer | 1,021 | Add merge tags and conditional blocks with fallbacks for missing fields |
| channel-portfolio-planner | 1,021 | Choose which social channels to run, starting from audience and objective |
| story-bank-builder | 1,020 | Assemble reusable origin, customer and proof stories for the message |
| list-segment-builder | 1,020 | Build engaged, lapsed, RFM and lifecycle segments plus suppression lists |
| launch-readiness-auditor | 1,020 | Audit a launch plan against the RAMP preflight, execution or outcome profile |
| social-selling-planner | 1,019 | Build a founder social-selling routine and turn funding or hiring signals into plays |
| sales-enablement-kit | 1,019 | Write battle cards, an internal launch FAQ and the sales team briefing |
| pricing-packaging-planner | 1,019 | Design launch pricing tiers, packaging and an early-bird offer |
| inbox-placement-monitor | 1,019 | Read seed-list placement and trend Postmaster and SNDS sender reputation |
| community-launch-runner | 1,019 | Prepare Product Hunt, Hacker News and directory launch submissions in waves |
| list-growth-designer | 1,018 | Design lead magnets, double opt-in and a referral loop to grow the list |
| conversion-value-mapper | 1,018 | Map margin onto conversion values so tROAS optimizes profit rather than orders |
| advocacy-program-designer | 1,018 | Design employee advocacy or founder-led sharing with a share kit for the team |
| subject-line-lab | 1,017 | Generate and pre-score subject line variants, including truncation and spam checks |
| proof-point-packager | 1,017 | Package stat cards and case snippets so each message pillar carries its own proof |
| launch-monitor | 1,017 | Watch the T-0 to T+30 launch window and track Product Hunt and Hacker News ranking |
| launch-asset-packager | 1,017 | Assemble a press kit, store listing and go-live checklist by launch tier |
| social-quality-auditor | 1,016 | Gate a social asset batch or read program maturity before publishing |
| reactivation-specialist | 1,016 | Build win-back, re-permission and sunset campaigns for lapsed subscribers |
| creator-registry | 1,016 | Query or update the creator roster: rates, rights, exclusivity and performance |
| consent-registry | 1,016 | Log opt-ins, unsubscribes and complaints, and query lawful basis per subscriber |
| message-house-builder | 1,014 | Build a message house or PR-FAQ for a launch from the positioning canvas |
| fatigue-frequency-manager | 1,014 | Read frequency and CTR decay against an early-flight baseline and decide rotation |
| engagement-inbox-manager | 1,014 | Triage comments, DMs and mentions with reply drafts, SLAs and escalation |
| social-pulse-monitor | 1,013 | Run keyless social listening for brand mentions, spikes and buying triggers |
| positioning-truth-tracer | 1,012 | Reconcile the positioning canvas with the differentiators the product can ship |
| list-hygiene-monitor | 1,012 | Flag decaying and unengaged subscribers on a schedule and explain open-rate drift |
| early-access-designer | 1,012 | Design a waitlist and beta stage ladder with graduation criteria |
| channel-registry | 1,012 | Register a social channel's state, cadence, governance and UGC permission |
| launch-feedback-synthesizer | 1,011 | Cluster launch reviews, comments and board posts into themes and a shipping loop |
| newsletter-monetization-planner | 1,011 | Model paid tiers and sponsorship inventory with a rate card |
| social-measurement-loop | 1,010 | Run the weekly social readout and name which posts won and what changes next |
| press-media-relations | 1,010 | Build a tiered media and analyst list and pitch a launch release under embargo |
| preference-frequency-manager | 1,010 | Build a preference center and a frequency opt-down ladder instead of unsubscribe |
| narrative-baseline-mapper | 1,010 | Inventory what the current surfaces say and find the gap to what you mean |
| launch-day-conductor | 1,010 | Run launch day with a runbook, a war room and a CONTINUE or ROLLBACK call |
| share-of-voice-tracker | 1,009 | Compute share of voice against competitors and trend it by quarter |
| offer-claims-registry | 1,009 | Register claim wording, evidence, disclosures, terms and review dates |
| narrative-quality-auditor | 1,009 | Audit whether a message is on canon, with separate truth, system and effectiveness reads |
| send-experiment-designer | 1,008 | Design email A/B, send-time and hold-out tests with a significance read |
| launch-window-planner | 1,008 | Compare candidate launch windows by conflict, tailwind and risk, and set the embargo |
| launch-retro-analyzer | 1,008 | Run a launch retro and compare results against targets by channel |
| launch-registry | 1,008 | Log a launch, its embargo, stage transitions and submission outcomes |
| narrative-cascade-planner | 1,007 | Map how the narrative lands on every surface with per-surface message match specs |
| message-test-designer | 1,007 | Design message-market-fit panels and five-second comprehension tests |
| launch-tier-planner | 1,007 | Decide how big a launch should be, with a risk register and kill criteria |
| voice-dossier-builder | 1,006 | Codify a founder's voice from their own posts and set content pillars |
| platform-norm-profiler | 1,006 | Build a platform norm card: character limits, visible-fold cutoffs and conventions |
| paid-measurement-loop | 1,006 | Read ROAS and CPA against a control after a paid change over a fixed window |
| narrative-enablement-kit | 1,005 | Write the pitch ladder, spokesperson Q&A and approved boilerplate pack |
| momentum-planner | 1,005 | Plan T+1 to T+30 momentum, including a changelog cadence as go-to-market |
| narrative-drift-monitor | 1,004 | Detect drift between surfaces and the canon, and watch competitor repositioning |
| participation-warmup-planner | 1,003 | Plan the participation ramp and account history a community launch needs |
| narrative-resonance-monitor | 1,003 | Measure resonance, echo rate against the canon lexicon and how AI answers describe you |

The remaining 17 indexed listings range from 3 to 998 installs, and 14 of them are legacy names such as schema-markup-generator, meta-tags-optimizer and alert-manager that have no directory in the current tree.

## Why This Matters for Hermes Agents

Most marketing agent demos collapse into one generic strategist that answers every question in the same voice. This suite refuses that shape: a question about a Shopping feed disapproval routes to `product-feed-optimizer`, a question about attribution routes to `attribution-reconciler`, and each one has its own procedure, its own inputs and its own scoring model. For an agent working across a funnel, that separation is the difference between advice and a workflow.

The auditor layer is the second useful part. Each discipline ends in a typed gate, and several state an explicit item count alongside veto checks: 80 items for CORE-EEAT content quality, 40 for CITE domain authority, 20 for ROAS ad accounts and 20 for SEND email programs. An agent can run the gate, report a score with the failing items, and stop there, which is far easier to trust than a paragraph that says the campaign looks good.

The registries are the least common feature and the most interesting. Seven append-only stores hold entities, creators, offers and claims, consent, launches, channels and narrative, so a claim reviewed once does not get re-invented next week, and an opt-in logged once is queryable later. The README is explicit that these are propose-only and that the static bundles return NOT_SCORED, which is an honest description of a system that is a record keeper rather than a source of truth.

The cost is real and should be stated: this is not a pile of Markdown. The plugin ships hooks that run Bash on session start, prompt submit and every tool use, and around 70 scripts for validation, evals and registry events. Install it where you can inspect the scripts, and read the hooks manifest before enabling the plugin on a host with production credentials.

## Usage

| You say | What happens |
|---|---|
| "/aaron-marketing:auto research keywords for my SaaS targeting small teams" | Routes to keyword-research, asks for volume, difficulty and intent inputs, and returns a clustered keyword set |
| "Draft a landing page for the launch and check it against CORE-EEAT" | Runs content-writer for the draft, then content-quality-auditor for the 80-item gate and a fix list |
| "Which of these creators should we book?" | Runs fit-scorer for a STAR suitability read, then budget-optimizer to check the tier allocation |
| "Our GA4 numbers do not match Google Ads" | Runs attribution-reconciler for a double-count reconciliation and a standing workbook |
| "Build the welcome flow and the abandoned cart sequence" | Runs email-sequence-designer, then email-quality-auditor and deliverability-qa before send |
| "Plan the Product Hunt launch and the press push" | Chains launch-tier-planner, community-launch-runner, press-media-relations and launch-day-conductor |
| "Does our positioning still match what we can ship?" | Runs positioning-truth-tracer against the offer and claims registry and reports the gaps |

## Verification

Confirm what the skills CLI installed:

```bash
npx skills list | grep -iE "keyword-research|content-quality-auditor|launch-day-conductor"
```

Read the skills before installing. All five URLs below returned 200 with `curl -s -o /dev/null -w "%{http_code}"` when checked on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/aaron-he-zhu/aaron-marketing-skills/main/README.md
curl -sL https://raw.githubusercontent.com/aaron-he-zhu/aaron-marketing-skills/main/skills.sh.json
curl -sL https://raw.githubusercontent.com/aaron-he-zhu/aaron-marketing-skills/main/seo-geo/survey/keyword-research/SKILL.md
curl -sL https://raw.githubusercontent.com/aaron-he-zhu/aaron-marketing-skills/main/seo-geo/implement/content-writer/SKILL.md
curl -sL https://raw.githubusercontent.com/aaron-he-zhu/aaron-marketing-skills/main/launch/assemble/message-house-builder/SKILL.md
```

Note the nesting: skills are not under a flat `skills/` directory, they sit at `<discipline>/<phase>/<name>/SKILL.md`, with the protocol layer at `protocol/<registry>/SKILL.md`. The registry file `skills.sh.json` lists every skill grouped by discipline and is the fastest way to see the current tree:

```bash
curl -s https://raw.githubusercontent.com/aaron-he-zhu/aaron-marketing-skills/main/skills.sh.json | grep '"title"'
```

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| keyword-research | Warn | Pass | Warn |
| content-writer | Pass | Pass | Warn |
| geo-content-optimizer | Pass | Pass | Warn |

The warnings are worth taking literally rather than dismissing. Snyk returns a warning on all three sampled skills, and keyword-research also draws a Gen Agent Trust Hub warning, while Socket passes all three. The skills.sh verdicts do not say why on the page, so treat the warning as a prompt to read the skill text and the scripts yourself before enabling the plugin.

The surface is larger than the verdict table suggests. Twelve `SKILL.md` files declare an `allowed-tools` field, so those skills ask the host for specific tool permissions. `hooks/hooks.json` registers Bash hooks on SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PostToolUseFailure, PostToolBatch and Stop, each with a timeout and pointing at `hooks/claude-hook.sh`. The `scripts/` directory holds around 70 Python and Bash files covering validation, eval runs, release packaging and publishing to external registries. Several skills also write to the append-only registries under `protocol/`, which persist across sessions.

None of that is malicious, and the repo ships `SECURITY.md` and `PRIVACY.md` alongside it. But this is not a read-only prompt pack: install it in a workspace where the scripts can be reviewed, keep the plugin's hooks in mind on hosts that auto-run them, and decide deliberately whether the registries should hold client data. The advisory outputs, particularly `contract-helper` agreements and pricing plans, are drafts for a human to sign off, not legal or financial advice.

## Limitations

- The install index outruns the tree. 134 indexed listings against 120 `SKILL.md` directories: `on-page-seo-auditor`, `entity-optimizer`, `content-reviewer`, `schema-markup-generator`, `meta-tags-optimizer`, `internal-linking-optimizer`, `seo-content-writer`, `content-refresher`, `ugc-repurposer`, `performance-reporter`, `niche-researcher`, `backlink-analyzer`, `audience-analyzer` and `alert-manager` carry install counts but have no directory in the current tree. All 14 sit below 1,000 installs.
- Usage is concentrated and noisy. The top listing is 1,925 installs and 117 of the 134 listings sit between 1,003 and 1,925, so the ordering inside that band is close to a tie and should not be read as a ranking of skill quality.
- Not a Markdown-only install. The plugin ships Bash hooks and a 107-file script toolchain (93 Python, 13 Bash), and 12 skills declare `allowed-tools`; a quick install on a locked-down host will fail or need review.
- The records are propose-only. The README states that the static bundles are Tier-1, that auditors return NOT_SCORED and that registries are propose-only, so nothing here enforces a claim or blocks a send by itself.
- Repository metadata is moving fast. The pack records the last push as 2026-10-27, one day after this snapshot date of Oct 26, 2026, and the repo declares version 20.1.0 with generated release surfaces, so expect the file layout to change between reads.
- Snapshot data, verified Oct 26, 2026: 130,549 combined installs across 134 indexed listings; 3.0K GitHub stars; Apache License 2.0; last pushed 2026-10-27. Counts drift over time.

## Related

- [Marketing Mindset - B2B Marketing OS for AI Agents Setup](/hermes/skills/catalog/marketing-mindset-setup) - a lighter B2B marketing operating system, useful as a contrast to this suite's seven-discipline structure.
- [SEO GEO Claude Skills - SEO & Generative Engine Optimization Suite Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup) - the author's earlier standalone SEO and GEO bundle, now signposted to this repo.
- [ClawFu Skills - 175 Marketing Methodologies for AI Agents Setup](/hermes/skills/catalog/clawfu-skills-setup) - methodology-first marketing skills that pair with the execution skills here.
- [Brand Building Skills - Brand Strategy Suite Setup](/hermes/skills/catalog/arnabbagxd-brand-building-skills-setup) - brand strategy depth for the narrative layer that message-house-builder only sketches.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the plugin rather than the individual skills if you want the eight slash commands and the routing in `/aaron-marketing:auto`; a bare `npx skills add` gives you the skills without the command surface.
- Read `skills.sh.json` first. It is the authoritative grouping of the 120 skills by discipline and phase, and it explains why a marketing question lands where it does.
- Use the auditors as the stopping condition. Running content-quality-auditor or ad-account-auditor gives you a score and a fix list, which is a better handoff than asking for another round of advice.
- Do not let the registries hold anything you would not put in a shared document: they are append-only and persist, and the consent and claims stores are the ones that matter legally.
- Read `hooks/hooks.json` and one or two files in `scripts/` before enabling the plugin on a host with production credentials; the toolchain is the real security surface here, not the prompt text.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
