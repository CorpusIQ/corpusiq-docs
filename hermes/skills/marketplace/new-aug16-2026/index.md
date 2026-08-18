---
title: "New Skills — August 16, 2026 - CorpusIQ Docs"
description: "skills.sh sweep: Vercel AI SDK (51.1K, 3), Cursor Plugins (72.0K, 79), Angular Skills (40.1K, 2), Inngest Skills (19.3K, 14), OXC Project (9.9K, 4), Alibaba Open Code Review (4.3K, 2) — 6 publisher clusters, 104 skills, 6 setup guides."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug16-2026/"
robots: "index,follow"
last_updated: "2026-08-16"
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills"]
sweep_id: "2026-08-16"
new_publishers: 6
new_skills: 104
guides_drafted: 6
---

# New Skills — August 16, 2026

First skills.sh sweep of August 16. 40 API queries collected 3,945 unique skills; all top-120 clusters reported known (same-day triage trap), so the recovery pass excluded `new-aug15-2026*` dirs, then hot/trending leaderboard finds and the carry-over queue were re-verified on publisher pages. The queue-underestimation pattern held again, this time for brand suites the API never surfaced: **cursor/plugins was 0 in the API sweep and 72.0K on its publisher page; vercel/ai 51.1K; angular/skills 40.1K** — all official vendor orgs, all missed by the previous sweeps entirely.

## New Publisher Clusters — Guided This Sweep

| Cluster | Skills | Installs | Tier | Guide |
|---|---|---|---|---|
| cursor/plugins | 79 | 72.0K | 🟢 | [Cursor Plugins Skills Setup](/hermes/skills/catalog/cursor-plugins-skills-setup/) |
| vercel/ai | 3 | 51.1K | 🟡 | [Vercel AI SDK Skills Setup](/hermes/skills/catalog/vercel-ai-skills-setup/) |
| angular/skills | 2 | 40.1K | 🟢 | [Angular Skills Setup](/hermes/skills/catalog/angular-skills-setup/) |
| inngest/inngest-skills | 14 | 19.3K | 🟡 | [Inngest Skills Setup](/hermes/skills/catalog/inngest-skills-setup/) |
| oxc-project/oxc | 4 | 9.9K | 🟡 | [OXC Project Skills Setup](/hermes/skills/catalog/oxc-project-skills-setup/) |
| alibaba/open-code-review | 2 | 4.3K | 🟡 | [Alibaba Open Code Review Setup](/hermes/skills/catalog/alibaba-open-code-review-setup/) |

## Method Notes

- 40 API queries → 3,945 unique skills → all top-120 clusters in-tree (same-day triage) → recovery diff excluding `new-aug15-2026*` dirs → only resend/ react-email + email-best-practices surfaced, both skipped (family already guided via resend-skills-setup).
- Hot/trending leaderboards surfaced 16 fresh finds; publisher-page verification turned 5 brand-authority vendor orgs into guides (cursor, vercel, angular, inngest, oxc).
- Carry-over queue re-verified: alibaba open-code-review promoted from brand-watch to guided at 4.3K with 20.5K GitHub stars; uniwind, asksurf, ningzimu stayed flat and re-parked.
- Security audits per top skill: cursor 🟢 (3/3 Pass), angular 🟢 (3/3 Pass), vercel/ai 🟡 (Snyk Warn), inngest 🟡 (Snyk Warn), oxc 🟡 (Snyk Warn), alibaba 🟡 (Snyk Fail named).

## Evaluated and Queued (next sweep)

| Cluster | Installs | Reason parked |
|---|---|---|
| uni-stack/uniwind | 5.4K | Flat since Aug 15 (5.3K); RN tooling, at bar |
| asksurf-ai/surf-skills | 3.8K | Flat; crypto-adjacent, below drafting bar |
| ningzimu/codex-ppt-skill | 3.6K | Flat; below drafting bar |
| streakyc/googleworkspacecli | 1.8K | 95 skills but 1.8K total; watch |
| steel-dev/skills | 1.3K | Browser-automation vendor, brand watch |
| zhaono1/agent-playbook | 34.0K API | Top skill already guided via charon-fan; rest ≤1.2K |

Dropped below minimum: irpsv/ai-bro (341), coji/natural-japanese (420), byte-me-labs/github-actions-catalog (36), felixgeelhaar/skills (33).

Carry-over queue remains parked per playbook: herdr, last30days, agent-config, stop-slop, web-access, amazonappdev/devices-agent-skills, dmmulroy/anti-slop.

## Notable Signals for CorpusIQ

- **cursor/plugins** is the largest engineering-discipline cluster catalogued to date (79 skills). thermo-nuclear-code-quality-review and the CI loop skills map directly onto our PR gate and CI retry discipline.
- **vercel/ai** is the canonical AI SDK reference — its "never code from memory, verify against bundled docs" doctrine matches our own verification-before-assertion rule and informs client agent work.
- **angular/skills** encode a build-verify gate (`ng build` before delivery) worth adopting as a delivery discipline.
- **inngest** durable functions are the pattern layer between our fire-and-forget crons and reliable background execution.
- **oxc-project** Rust-native linting is a direct CI speed and cost win.
- **alibaba open-code-review** gives a second, independent AI review path with 20.5K GitHub stars behind it.

## Index State After Sweep

- catalog/index.md: +6 entries
- marketplace/index.md: header 876 → 882, footer 927 → 933
- last_updated on both indexes: 2026-08-16
