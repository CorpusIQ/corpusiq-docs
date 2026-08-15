---
title: "New Skills — August 14, 2026 (Evening)"
description: "skills.sh evening sweep — 8 new publisher clusters with setup guides: Flutter Agent Plugins (538.2K, official), ECC Engineering Suite (466.2K, 292 skills), Sentry CLI (127.3K, official), Awesome LLM Apps (79.7K), Pexo Video (62.5K), SEOJuice (51.8K), Better UI (51.3K), CodeRabbit (15.9K, official)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug14-2026-evening/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill marketplace", "skills.sh"]
sweep_id: aug-14-2026-evening
new_publishers: 8
new_skills: 458
guides_drafted: 8
---

# New Skills — August 14, 2026 (Evening)

**Source:** [skills.sh](https://skills.sh) leaderboards + REST API multi-query sweep
**Date:** August 14, 2026 (evening)
**Result:** 8 new publisher clusters · 458 skills · ~1.39M combined installs · 8 setup guides

Sweep combined the hot (1H delta) and trending (24h) leaderboards with 40 API queries, cross-referenced 3,944 unique skills against the existing `hermes/skills/` tree. Eight uncovered clusters with substantive Hermes value were guided; the afternoon sweep's queue (herdr, last30days, agent-config, stop-slop, web-access, brightdata, langfuse, zhaono1 agent-playbook) stays parked for the next sweep.

---

## New Publisher Clusters (8) — All With Setup Guides

### 1. Flutter Agent Plugins — `flutter/agent-plugins` (86 skills, 538.2K)

Official Flutter team skills covering the complete lifecycle: architecture best practices (29.9K), responsive layout (29.0K), layout fixes (27.8K), widget/integration testing (27.1K / 26.6K), declarative routing, JSON serialization, localization, previews, plus a dart-* series and cross-cutting skills (grill-me, api-review, code-documentation).

**Setup guide:** [Flutter Agent Plugins Setup](/hermes/skills/catalog/flutter-agent-plugins-setup/)

### 2. ECC Engineering Suite — `affaan-m/ecc` (292 skills, 466.2K)

One of the largest collections on the marketplace: frontend/backend patterns, security-review, api-design, coding-standards, TDD, docker/postgres patterns, deep-research, article-writing, seo, brand-voice, architecture-decision-records, living-docs-governance, and agent governance skills.

**Setup guide:** [ECC Engineering Skills Setup](/hermes/skills/catalog/ecc-engineering-skills-setup/)

### 3. Sentry CLI — `sentry/dev` (1 skill, 127.3K)

Official Sentry skill teaching agents to run the Sentry CLI: releases, deploys, sourcemap uploads, issue triage, project admin. Rising on the hot leaderboard (+94 in the sweep hour).

**Setup guide:** [Sentry Dev Skill Setup](/hermes/skills/catalog/sentry-dev-skills-setup/)

### 4. Awesome LLM Apps — `shubhamsaboo/awesome-llm-apps` (26 skills, 79.7K)

Role-based agent skills from the famous awesome-llm-apps repo: fullstack-developer (8.0K), academic-researcher (6.8K), content-creator, technical-writer, project-planner, data-analyst, deep-research, fact-checker, strategy-advisor, plus niche utilities (scope-creep-detector, commit-archaeologist, dependency-doctor).

**Setup guide:** [Awesome LLM Apps Skills Setup](/hermes/skills/catalog/awesome-llm-apps-skills-setup/)

### 5. Pexo Video — `pexoai/pexo-skills` (24 skills, 62.5K)

Agentic video generation: pexo-agent (39.4K), videoagent video/image/audio studios, Seedance 2.0 and Veo 3.2 prompters, and short-form skills (youtube-short-maker, tiktok-video-ad, saas-video, startup-video, launch-video).

**Setup guide:** [Pexo Video Skills Setup](/hermes/skills/catalog/pexo-video-skills-setup/)

### 6. SEOJuice — `calm-north/seojuice-skills` (14 skills, 51.8K)

Full SEO workflow: find-keywords (6.9K), optimize-for-ai (6.6K, GEO), build-links (6.5K), brief, audit, rank-local, diagnose-seo, beat-competitors, migrate-site, recover-content, build-clusters, fix-linking, target-serp.

**Setup guide:** [SEOJuice Skills Setup](/hermes/skills/catalog/seojuice-skills-setup/)

### 7. Better UI — `jakubkrehel/skills` (13 skills, 51.3K)

Interface polish discipline: better-ui (8.6K), better-typography (8.3K), better-colors (8.0K), better-interface, better-layout, better-accessibility, better-writing, interface-review, plus OKLCH color skills. All core skills on the hot leaderboard during the sweep.

**Setup guide:** [Better UI Skills Setup](/hermes/skills/catalog/better-ui-skills-setup/)

### 8. CodeRabbit — `coderabbitai/skills` (2 skills, 15.9K)

Official CodeRabbit review methodology: code-review (9.7K) and autofix (6.2K). AI code review discipline without the SaaS subscription.

**Setup guide:** [CodeRabbit Skills Setup](/hermes/skills/catalog/coderabbit-skills-setup/)

---

## Evaluated and Queued for Next Sweep

| Skill / Cluster | Installs | Status |
|---|---|---|
| `amazonappdev/devices-agent-skills` | ~23/hr hot | Official Amazon devices (Fire TV etc.) — niche, monitor |
| `lottiefiles/motion-design-skill` | 8.0K | Official Lottie motion design — overlaps existing animation stack |
| `sonilo-ai/skills` (video-to-sfx) | ~9/hr hot | Video SFX — small, media-adjacent |
| `emblemcompany/agent-skills` (emblem-market-research) | 8.8K | Market research — evaluate against existing research skills |
| `dmmulroy/anti-slop` (install-anti-slop) | ~25/hr hot | Anti-slop installer — pairs with queued stop-slop cluster |
| `mintlify/docs` | 9.1K | Official Mintlify docs skill — docs-adjacent |
| `ljagiello/ctf-skills` | 64 skills | CTF/security niche — low business value |
| `digitalsamba/claude-code-video-toolkit` | 6.3K | ffmpeg video toolkit — media-adjacent |
| `getsentry/skills` | 20.6K | Sentry sibling repo — partial overlap with sentry/dev guide |

---

## Installation

```bash
# Official vendor skills
npx skills add flutter/agent-plugins
npx skills add sentry/dev
npx skills add coderabbitai/skills

# Community suites
npx skills add affaan-m/ecc
npx skills add shubhamsaboo/awesome-llm-apps
npx skills add pexoai/pexo-skills
npx skills add calm-north/seojuice-skills
npx skills add jakubkrehel/skills
```

## Notable

- **Official vendor wave:** three of the eight clusters are first-party vendor skills (Flutter, Sentry, CodeRabbit) — the marketplace is shifting from community experiments to vendor-published agent capabilities.
- **ECC is the largest single-repo suite yet cataloged** (292 skills, 466.2K installs), spanning engineering, research, content, and agent governance in one package.
- **Pexo lands directly on the CorpusIQ media stack** — Seedance/Veo prompters plus short-form ad skills complement HeyGen, HyperFrames, and Postiz pipelines.
- **SEOJuice + the afternoon's SEO GEO Claude Skills** give the docs SEO/AEO/GEO pass two complete, complementary toolkits.

## Source

Hermes skills-monitor, evening sweep — skills.sh REST API (40 queries, 3,944 unique skills) + hot/trending leaderboards, diffed against the `hermes/` tree in corpusiq-docs.
