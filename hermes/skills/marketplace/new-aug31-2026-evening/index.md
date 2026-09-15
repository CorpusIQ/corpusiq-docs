---
title: "New Skills - August 31, 2026 (Evening)"
description: "Evening leaderboard sweep (95 publisher slugs, 11 zero-hit): InsForge (144.5K), Matt Pocock Skills zh-CN (138.8K), Owl Listener Designer Skills (124.7K), TanStack Skills (36.6K), Archify (32.5K, 39.2K⭐), QA Skills (25.3K), Paperthin (22.1K), Inkeep Open Knowledge (17.1K), Vigiles (12.3K), Hithink Finance (1.8K) - 10 new publisher clusters, 325 skills, 10 setup guides."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug31-2026-evening/"
robots: "index,follow"
last_updated: "2026-08-31"
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills"]
sweep_id: "2026-08-31-evening"
new_publishers: 10
new_skills: 325
guides_drafted: 10
---

# New Skills - August 31, 2026 (Evening)

Evening sweep: three skills.sh leaderboards (all-time, trending, hot) pulled via curl, 95 publisher slugs extracted from raw HTML (relative-href patterns, per the Aug 24 calibration), 11 zero-hit publishers after grepping the full `hermes/skills/` tree. Publisher-page fetches verified 10 as genuinely new and promoted them to guides; 1 parked (site-registry page 404s).

## New Publisher Clusters - Guided This Sweep

| Cluster | Skills | Installs | GitHub | Tier | Guide |
|---|---|---|---|---|---|
| insforge/insforge-skills | 7 | 144.5K | 36⭐ | 🟡 | [InsForge Skills Setup](/docs/hermes/skills/catalog/insforge-skills-setup) |
| vinvcn/mattpocock-skills-zh-cn | 54 | 138.8K | 3.9K⭐ | 🟢 | [Matt Pocock Skills (简体中文) Setup](/docs/hermes/skills/catalog/mattpocock-skills-zh-cn-setup) |
| owl-listener/designer-skills | 107 | 124.7K | 2.4K⭐ | 🟢 | [Owl Listener Designer Skills Setup](/docs/hermes/skills/catalog/owl-listener-designer-skills-setup) |
| tanstack-skills/tanstack-skills | 14 | 36.6K | 31⭐ | 🟢 | [TanStack Skills Setup](/docs/hermes/skills/catalog/tanstack-skills-setup) |
| tt-a1i/archify | 1 | 32.5K | 39.2K⭐ | 🟢 | [Archify Setup](/docs/hermes/skills/catalog/archify-setup) |
| petrkindlmann/qa-skills | 50 | 25.3K | 102⭐ | 🟡 | [QA Skills Setup](/docs/hermes/skills/catalog/petrkindlmann-qa-skills-setup) |
| lilmgenius/paperthin | 36 | 22.1K | 945⭐ | 🟢 | [Paperthin Setup](/docs/hermes/skills/catalog/paperthin-skills-setup) |
| inkeep/open-knowledge-skills | 33 | 17.1K | 6⭐ | 🟢 | [Inkeep Open Knowledge Skills Setup](/docs/hermes/skills/catalog/inkeep-open-knowledge-skills-setup) |
| zernie/vigiles | 21 | 12.3K | 15⭐ | 🟢 | [Vigiles Setup](/docs/hermes/skills/catalog/vigiles-setup) |
| hithink-tech/financial-api | 2 | 1.8K | 2.1K⭐ | 🟢 | [Hithink Finance Setup](/docs/hermes/skills/catalog/hithink-finance-setup) |

## Method Notes

- Discovery: all three leaderboards pulled with curl + browser UA from Spark (~940KB/375KB/366KB), slugs extracted with the skill's `ssh_extract_publishers.py` against the Mac Mini docs tree (95 slugs, 11 zero-hit).
- Skill-name-level re-check caught two near-misses: `mattpocock` (10 hits) and `tanstack` (4 hits) already appear in the tree - the English mattpocock suite is documented (catalog/mattpocock-skills-setup.md + matt-pocock-engineering-setup/), so the zh-CN fork is guided as a variant with cross-links rather than a new workflow set; tanstack mentions were incidental, so the dedicated tanstack-skills cluster is a genuinely new guide.
- Publisher-page totals are cited in guides (authoritative): insforge 144.5K, vinvcn 138.8K, owl-listener 124.7K, tanstack 36.6K, archify 32.5K, qa-skills 25.3K, paperthin 22.1K, inkeep 17.1K, vigiles 12.3K, hithink 1.8K.
- Below-20K drafting justifications: hithink-tech on first-party vendor authority (Tonghuashun, 2.1K⭐ official repo) plus A-share data-domain relevance (wind-skills precedent); inkeep on vendor authority (Inkeep) plus knowledge-base domain relevance (basic-memory precedent); vigiles on harness-verification domain relevance to CorpusIQ's own audit stack (trailofbits/review-loop precedent).
- Quality tiers follow audit badges: 🟢 where all three audits Pass; 🟡 where a Fail/Warn exists - insforge (Snyk Fail on flagship) and petrkindlmann/qa-skills (Gen Agent Trust Hub Warn on playwright-automation), each named in the guide.
- `hithink-tech/financial-api` and `vinvcn/mattpocock-skills-zh-cn` ship Chinese-language SKILL.md content; the source language is named in each guide's Limitations per the non-English-suite precedent (wecomteam, genshijin, lijigang).
- tanstack-skills repo self-describes as UNOFFICIAL - the tier stays 🟢 (all audits Pass) but the guide flags the community-collection status prominently.

## Evaluated and Queued

| Skill | Source | Installs | Disposition |
|---|---|---|---|
| ick-skill | site/walle.17usoft.com | hot-board entry | Parked - site-registry publisher page 404s; no GitHub repo segment; brand-watch queue |

## Notable Signals for CorpusIQ

- Archify (tt-a1i, 39.2K⭐) is the highest-starred single-skill repo seen to date in a sweep - its validate-before-deliver gate is the diagram-world equivalent of CorpusIQ's pre-publish content gates, and its self-contained HTML output fits CorpusIQ's visual-answer architecture.
- Paperthin's re0 "ground-zero" family and ssotize's audit→approve→consolidate gate encode the exact SSOT + context-discipline doctrine CorpusIQ agents already operate under - a public reference implementation of our internal rules.
- InsForge at 144.5K installs with a 36⭐ repo confirms the skills.sh-native adoption channel: agents install via the registry, not via GitHub stars - tiering and coverage decisions must weight install counts first.
- The zh-CN Matt Pocock fork (138.8K) is evidence of strong Chinese-market agent demand - relevant to CorpusIQ's worldwide promotion surface.
