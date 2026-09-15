---
title: "New Skills - August 31, 2026"
description: "skills.sh 46-query API sweep (4,743 unique skills) plus hot-leaderboard finds: Hallmark (48.6K), Dart Language Skills (144.0K), LJG Skills (124.5K), Meng To Skills (76.2K), Daymade Claude Code Skills (58.4K), Low-Level Dev Skills (41.5K), HubSpot Agent CLI Skills (17.8K), Basic Memory Skills (9.7K) - 8 new publisher clusters, 8 setup guides."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug31-2026/"
robots: "index,follow"
last_updated: "2026-08-31"
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills"]
sweep_id: "2026-08-31"
new_publishers: 8
new_skills: 517
guides_drafted: 8
---

# New Skills - August 31, 2026

Forty-six-query skills.sh API sweep (4,743 unique skills, zero query failures) with cross-reference against the full hermes/ tree, plus hot-leaderboard candidate discovery with publisher-page verification. 117 clusters known, 3 API candidates, 2 of which resolved to existing coverage (`useosint/skills` source-string variant of the guided osint-skills cluster; `github/awesome-copilot` already guided). The hot leaderboard surfaced a further 9 candidates; publisher-page fetches promoted 8 to drafts and parked the rest.

## New Publisher Clusters - Guided This Sweep

| Cluster | Skills | Installs | GitHub | Tier | Guide |
|---|---|---|---|---|---|
| lijigang/ljg-skills | 30 | 124.5K | 7.2K⭐ | 🟡 | [LJG Skills Setup](/docs/hermes/skills/catalog/ljg-skills-setup) |
| dart-lang/skills | 30 | 144.0K | 463⭐ | 🟢 | [Dart Language Skills Setup](/docs/hermes/skills/catalog/dart-lang-skills-setup) |
| mengto/skills | 155 | 76.2K | 5.6K⭐ | 🟢 | [Meng To Skills Setup](/docs/hermes/skills/catalog/mengto-skills-setup) |
| daymade/claude-code-skills | 106 | 58.4K | 1.4K⭐ | 🟡 | [Daymade Claude Code Skills Setup](/docs/hermes/skills/catalog/daymade-claude-code-skills-setup) |
| nutlope/hallmark | 1 | 48.6K | 27.6K⭐ | 🟢 | [Hallmark Setup](/docs/hermes/skills/catalog/hallmark-setup) |
| mohitmishra786/low-level-dev-skills | 142 | 41.5K | 188⭐ | 🟡 | [Low-Level Dev Skills Setup](/docs/hermes/skills/catalog/low-level-dev-skills-setup) |
| hubspot/agent-cli-skills | 15 | 17.8K | 21⭐ | 🟡 | [HubSpot Agent CLI Skills Setup](/docs/hermes/skills/catalog/hubspot-agent-cli-skills-setup) |
| basicmachines-co/basic-memory | 38 | 9.7K | 3.8K⭐ | 🟢 | [Basic Memory Skills Setup](/docs/hermes/skills/catalog/basic-memory-skills-setup) |

## Method Notes

- 46-query API sweep returned 4,743 unique skills; the top-120 cluster diff flagged 3 candidates. `useosint/skills` (236.3K API sum) is the documented source-string variant of the already-guided `useosint/osint-skills` cluster - skipped. `github/awesome-copilot` (1.42M API sum) is already guided. `dart-lang/skills` was genuinely new (13.5K API sum undercounted the 144.0K publisher total 10x).
- The hot leaderboard was the primary discovery channel this sweep, per the Aug 17 calibration: `mohitmishra786/low-level-dev-skills` (6 skills at +1 1H), `basicmachines-co/basic-memory` (3 skills), `mengto/skills` (2 skills), `hubspot/agent-cli-skills`, `daymade/claude-code-skills`, and `lijigang/ljg-skills` all surfaced via hot-page deltas the API never ranked.
- Publisher-page totals are cited in guides (authoritative over API sums): dart-lang 144.0K vs 13.5K API sum, mengto 76.2K, daymade 58.4K, low-level-dev 41.5K, hubspot 17.8K, basic-memory 9.7K.
- Below-20K drafting justifications: hubspot/agent-cli-skills on first-party `hubspot` org authority plus direct CRM domain relevance (github/gh-stack precedent); basicmachines-co/basic-memory on YC-backed vendor authority plus agent-memory domain relevance (makerskills suite-cohesion precedent).
- Quality tiers follow audit badges: 🟢 where all three audits Pass (hallmark, dart-lang, mengto, basic-memory), 🟡 where Snyk (and Socket for hubspot) carry warnings, each named in the guide.
- `lijigang/ljg-skills` ships Chinese-language SKILL.md content; the source language is named in the guide's Limitations per the non-English-suite precedent (wecomteam, genshijin).

## Evaluated and Queued

| Skill | Source | Installs | Disposition |
|---|---|---|---|
| effective-html (6 skills) | plannotator/effective-html | 10.7K | Parked - below bar, no named publisher authority; hot momentum on html-wireframe; watch for growth |
| lark-apps, lark-vc, lark-openapi-explorer | site/open.larksuite.com | 1+1 1H each | Parked - site publisher (no GitHub repo segment), brand-watch queue |
| apifox-workflow-api-lifecycle | site/apifox.com | 1+1 1H | Parked - site publisher, brand-watch queue |
| byted-serverlessflink-volc-flink | site/skills.volces.com | 1+1 1H | Parked - site publisher, brand-watch queue |

## Notable Signals for CorpusIQ

- Hallmark (nutlope, 27.6K⭐) encodes the anti-AI-slop design consensus CorpusIQ already enforces in content rules; it is the design-side counterpart to our content-voice gates.
- HubSpot's official agent skills are the vendor's own CRM operations playbook - direct material for CorpusIQ's HubSpot connector and data-quality use cases.
- Basic Machines' memory suite is the reference implementation of graph-first agent memory; its notes / observations / relations pattern maps onto how CorpusIQ agents structure session context.
