---
title: "New Skills — August 18, 2026"
description: "skills.sh sweep: WeCom CLI Skills (153.4K, 28), WeCom Unified (4.4K, 1), Mastra AI Skills (32.6K, 5), Strix Security Skills (9.6K, 8) — 4 publisher clusters, 42 skills, 4 setup guides."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug18-2026/"
robots: "index,follow"
last_updated: "2026-08-18"
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills"]
sweep_id: "2026-08-18"
new_publishers: 4
new_skills: 42
guides_drafted: 4
---

# New Skills — August 18, 2026

First sweep of August 18. The API surface stayed fully caught up (40 queries, 3,943 unique skills, all top-120 clusters known per the diff script), so the entire batch came from the hot page, which delivered the biggest vendor cluster the sweeps have seen this month.

## New Publisher Clusters — Guided This Sweep

| Cluster | Skills | Installs | Tier | Guide |
|---|---|---|---|---|
| wecomteam/wecom-cli | 28 | 153.4K | 🟡 | [WeCom CLI Skills Setup](/hermes/skills/catalog/wecom-cli-skills-setup/) |
| mastra-ai/skills | 5 | 32.6K | 🟡 | [Mastra AI Skills Setup](/hermes/skills/catalog/mastra-ai-skills-setup/) |
| usestrix/strix | 8 | 9.6K | 🟡 | [Strix Security Skills Setup](/hermes/skills/catalog/strix-security-skills-setup/) |
| wecomteam/wecom-unified | 1 | 4.4K | 🟡 | [WeCom Unified Skill Setup](/hermes/skills/catalog/wecom-unified-skills-setup/) |

## Method Notes

- wecomteam/wecom-cli surfaced at #1 on the hot page (wecom-unified at 233+231 1H) and its publisher page reads 153.4K across 28 skills with 2.7K GitHub stars — the largest single publisher cluster catalogued this month, from Tencent's official WeCom org. The API never ranked it (API-omission trap, fourth recurrence).
- mastra-ai/skills surfaced on the hot page at 33+12 1H; publisher page reads 32.6K with the mastra flagship at 32.3K. Official vendor org.
- usestrix/strix surfaced with four skills at +12 installs in one hour; 54.1K GitHub stars on the repo, first seen on skills.sh 11 days before the sweep. Below the 20K guide bar — drafted on repo authority, hot-page momentum, and security relevance to agent operations.
- wecomteam/wecom-unified is a 1-skill routing layer for wecom-cli (4.4K, 59 stars); drafted on official-vendor brand authority plus its guardrail role for the 153.4K suite.
- Security audits per flagship: wecom-cli 🟡 (Snyk Warn; GATH and Socket Pass), mastra 🟡 (Snyk Warn; GATH and Socket Pass), strix 🟡 (Socket Warn + Snyk Fail; GATH Pass), wecom-unified 🟡 (GATH Warn + Snyk Warn; Socket Pass).
- Mac Mini unreachable Day 9 (SSH timeout) — sweep ran entirely from Spark canonical clone, push auth via gh auth token.
- Queue carried over unchanged from Aug 17 evening: uni-stack/uniwind 5.4K, amazonappdev 5.2K, asksurf 3.8K, ningzimu 3.6K, dmmulroy/anti-slop 2.4K, streakyc 1.8K, steel-dev 1.3K — all re-verified flat on this sweep's publisher-page pass, re-parked.

## Notable Signals for CorpusIQ

- **WeCom CLI** is first-party Tencent enterprise automation — the largest cluster we have catalogued from a Chinese vendor org, and the entry point for WeChat Work agent workflows.
- **Mastra AI Skills** codifies version-accurate framework usage (verify against installed embedded docs, never training data) — the same discipline our own docs management follows.
- **Strix** brings PoC-validated autonomous pentesting with a CI mode — a natural fit for the security-auditor role in our orchestration patterns.

## Index State After Sweep

- catalog/index.md: +4 entries
- marketplace/index.md: header 891 → 895, footer 942 → 946
- last_updated on both indexes: 2026-08-18
