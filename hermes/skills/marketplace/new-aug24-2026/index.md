---
title: "New Skills - August 24, 2026"
description: "skills.sh three-board sweep (all-time + trending + hot, full slug extraction): Autonnel Conversion Suite (147.5K installs, 6 skills), GPT-Image-2 Style Library (14.7K⭐, 1.5K), gh-issue-sync by mitsuhiko (2.5K), System Atlas (94) - 4 new publisher clusters, 9 skills, 4 setup guides."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug24-2026/"
robots: "index,follow"
last_updated: "2026-08-24"
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills"]
sweep_id: "2026-08-24"
new_publishers: 4
new_skills: 9
guides_drafted: 4
---

# New Skills - August 24, 2026

Morning sweep of August 24. Full three-board leaderboard extraction (all-time, trending 24h, hot) - direct curl from Spark to skills.sh, then regex slug extraction of every publisher link across all three boards. 68 unique publisher slugs surfaced; cluster-level grep (owner, repo, site-domain, and skill-name variants) against the full hermes/ tree cut that to four genuinely new publisher clusters. Everything else on the boards was already documented across catalog and marketplace pages.

## New Publisher Clusters - Guided This Sweep

| Cluster | Skills | Installs | GitHub | Tier | Guide |
|---|---|---|---|---|---|
| autonnel/autonnel-skills | 6 | 147.5K | 0⭐ Apache-2.0 | 🟡 | [Autonnel Skills Setup](/docs/hermes/skills/catalog/autonnel-skills-setup) |
| freestylefly/awesome-gpt-image-2 | 1 | 1.5K | 14.7K⭐ MIT | 🟢 | [GPT-Image-2 Style Library Setup](/docs/hermes/skills/catalog/gpt-image-2-style-library-setup) |
| mitsuhiko/gh-issue-sync | 1 | 2.5K | 160⭐ Apache-2.0 | 🟢 | [gh-issue-sync Setup](/docs/hermes/skills/catalog/gh-issue-sync-setup) |
| inkboard/system-atlas | 1 | 94 | 164⭐ MIT | 🔵 | [System Atlas Setup](/docs/hermes/skills/catalog/system-atlas-setup) |

## Method Notes

- Direct curl to skills.sh now works from Spark (previous sweeps had to route through web_extract because the network path hung) - all three leaderboards pulled as raw HTML (945KB all-time, 376KB trending, 373KB hot) and slug-extracted with a regex script over relative hrefs (`/owner/repo`, `/owner/repo/skill`, `/site/domain`).
- 68 publisher slugs across the three boards; 64 already documented. The zero-hit set was re-checked at skill-name level (not just publisher level) per the Aug 21 calibration - all 9 skills below are name-level new.
- autonnel/autonnel-skills is the standout find: 147.5K combined installs across a six-skill conversion suite (audit → blueprint → platform pick → server-side tracking → upsells → self-hosted launch), the first skills.sh pack covering the full conversion-funnel lifecycle. It sits on the trending board; skills.sh first-listed it Aug 5, 2026.
- freestylefly/awesome-gpt-image-2 pairs a 14.7K-star MIT repo (530+ reverse-engineered GPT-Image-2 cases, 20+ industrial templates) with a thin skill wrapper - the skill is modest (1.5K installs) but the knowledge base is the asset, and it matches the Hermes image_generate backend (gpt-image-2-medium) one-to-one.
- mitsuhiko/gh-issue-sync (2.5K installs, Armin Ronacher) turns GitHub issues into local Markdown under `.issues/open/` and `.issues/closed/` - a scriptable triage path for the corpusiq-docs issue backlog.
- inkboard/system-atlas (94 installs, 3 days old) is below the 100-install bar but on the hot board with a clean audit record - guided as 🔵 Community rather than parked.
- Security audit statuses taken verbatim from the skills.sh skill pages (Gen Agent Trust Hub / Socket / Snyk); no fabricated verdicts. autonnel carries Snyk Warn on four skills and Snyk Fail on two (landing-page-conversion-audit, server-side-conversion-tracking) - flagged in the guide.
- Mac Mini still unreachable - sweep ran entirely from the Spark canonical clone.

## Evaluated and Queued

None parked this sweep - all four zero-hit clusters cleared the bar (the two sub-100-install skills carried clean audits and real relevance: GH issue workflow + architecture documentation).

## Notable Signals for CorpusIQ

- **landing-page-conversion-audit** is a direct tool for the growth charter: element-named, revenue-ranked fix lists for corpusiq.io pages before scaling paid spend. Its refusal behavior (no traffic → redirect to blueprint; wrong offer → say so and stop) matches our own help-first, no-slop discipline.
- **server-side-conversion-tracking** is the durable fix class for iOS/ad-blocker conversion loss - relevant to the GA4/GSC/Ads reporting stack.
- **gpt-image-2-style-library** upgrades our image pipeline's consistency: named styles instead of per-prompt improvisation, against exactly the backend we run.
- **gh-issue-sync** gives the agent a file-based triage path for open community epics (issues #18, #12, #7) - grep-and-edit backlog management instead of web-UI clicking.

## Index State After Sweep

- catalog/index.md: +4 entries
- marketplace/index.md: header 906 → 910, footer 957 → 961
- last_updated on both indexes: 2026-08-24
