---
title: "New Skills - November 9, 2026 Evening"
description: "Skills.sh sweep (Nov 9 evening): 12 publisher guides for 66,916 combined installs across 209 indexed listings from a fresh 190-query topic probe"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov9-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 9, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 885 unique skills across 0 failed queries: 81 NEW rows and 252 PARTIAL, with the top NEW row at 332 installs and nothing above the 1,000-install trigger. That is the forty-fourth consecutive silent window.

With the standing window silent, this fire ran a fresh topic probe instead of re-reading the trending board: 190 domain queries across billing, procurement, analytics, engineering, databases, agents, communications, marketing, verticals and office automation. The probe returned 14,546 unique rows, 4,236 distinct sources and no failed query after a serial retry pass, and 3,061 of those sources had no page in the catalog.

Sizing every uncovered source by its own repository rather than by its best window row sank two large probe candidates that have no reachable public repository (`vasilyu1983/ai-agents-public` at 9,987 combined and `sales-skills/sales` at 2,053, both GitHub 404) and left twelve publisher clusters. All twelve are documented here.

Every guide was built from a pre-verified pack holding the exact per-listing install figure for every indexed skill, the repository metadata, the real skill layout read from the GitHub tree and the frontmatter description of each skill. Each draft was then checked with three gates: the format gate, the pack cross-check at threshold zero and the frontmatter audit. All 36 gate runs are green on the orchestrator re-run against the canonical scripts.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 885 (0 failed queries) |
| NEW (not in catalog) | 81 rows |
| PARTIAL (source known, skill not cataloged) | 252 |
| Above-floor finds in the standing window | 0 (top row 332) |
| Fresh probe queries | 190 (0 failed after serial retry) |
| Unique rows from the probe | 14,546 |
| Distinct sources from the probe | 4,236 |
| Uncovered sources from the probe | 3,061 |
| Sources excluded (no reachable repository) | 2 |
| Guides published this fire | 12 |
| Combined installs documented | 66,916 |
| Indexed listings covered | 209 |
| Green / Yellow tiers | 0 / 12 |

## New Setup Guides

- [ToolUniverse](/hermes/skills/catalog/tooluniverse-science-skills-setup) - mims-harvard/tooluniverse, 10,545 combined, 20 listings, 1,780 stars, Apache-2.0, Scientific research: biomedical and chemistry tooling, literature review, sequence retrieval and clinical guideline lookup
- [PostHog Skills](/hermes/skills/catalog/posthog-analytics-skills-setup) - posthog/skills, 10,120 combined, 20 listings, 79 stars, MIT, Product analytics: instrumentation, session replay, feature flags, experiments, data warehouse and HogQL
- [Octagon Finance Skills](/hermes/skills/catalog/octagon-finance-skills-setup) - octagonai/skills, 7,199 combined, 20 listings, 130 stars, MIT, Financial markets: quotes, filings, earnings, analyst reports and portfolio research workflows
- [n8n Engineering Skills](/hermes/skills/catalog/n8n-engineering-skills-setup) - n8n-io/n8n, 6,336 combined, 20 listings, 209,960 stars, NOASSERTION, Repository engineering: contribution conventions, PR creation, bug reproduction, content design and review workflows
- [Agentic QE Skills](/hermes/skills/catalog/agentic-qe-skills-setup) - proffesor-for-testing/agentic-qe, 5,949 combined, 20 listings, 524 stars, MIT, Quality engineering: test strategy, API and load testing, coverage analysis, defect triage and release gates
- [Twilio Agent Skills](/hermes/skills/catalog/twilio-agent-skills-setup) - twilio/ai, 5,524 combined, 20 listings, 40 stars, MIT, Communications: SMS, WhatsApp, voice, email and conversation APIs for customer messaging
- [Google Ads Skills](/hermes/skills/catalog/google-ads-skills-setup) - eliasmalmsandberg/google-ads-skills, 4,900 combined, 20 listings, 14 stars, MIT, Paid media: Google Ads account structure, bidding, ad copy, keyword and search term analysis
- [NotFair Plugin](/hermes/skills/catalog/notfair-meta-ads-skills-setup) - nowork-studio/notfair-plugin, 4,378 combined, 20 listings, 4,133 stars, MIT, Paid social: Meta Ads auditing, campaign structure, creative testing and ad account diagnostics
- [HyperFX Marketing Skills](/hermes/skills/catalog/hyperfx-marketing-skills-setup) - hyperfx-ai/marketing-skills, 4,193 combined, 20 listings, 112 stars, MIT, Growth marketing: audience research, ad library analysis, campaign planning and creative briefs
- [Zapier Agent Skills](/hermes/skills/catalog/zapier-skills-setup) - zapier/agent-skills, 3,087 combined, 7 listings, 24 stars, MIT, Workflow automation: Zapier app actions, trigger design, workflow diagnostics and cross-app data flow
- [Neon Postgres Skills](/hermes/skills/catalog/neon-postgres-skills-setup) - neondatabase/postgres-skills, 2,481 combined, 2 listings, 55 stars, Apache-2.0, Databases: Postgres schema design, indexing, query performance and connection handling
- [Local SEO Skills](/hermes/skills/catalog/local-seo-skills-setup) - garrettjsmith/localseoskills, 2,204 combined, 20 listings, 147 stars, MIT, Local search: Google Business Profile, local citations, reviews, service pages and local rank tracking

## Verification

Every guide carries its exact per-listing install figures, a snapshot line with the verified date and the sampled skills.sh verdicts. Re-check the security pages on skills.sh before production use: install counts and verdicts drift.

## Related

- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)
- [November 9, 2026 Morning Sweep](/hermes/skills/marketplace/new-nov9-2026-morning-skills)
