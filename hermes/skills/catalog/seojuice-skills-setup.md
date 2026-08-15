---
title: SEOJuice Skills — SEO Suite Setup Guide for Hermes Agents
description: "calm-north/seojuice-skills — 14 skills, 51.8K total installs. find-keywords (6.9K), optimize-for-ai (6.6K), build-links (6.5K), brief, audit, rank-local, audit-speed, diagnose-seo, beat-competitors, migrate-site, recover-content, build-clusters, fix-linking, target-serp."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/seojuice-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill setup", "seo", "geo", "keyword research", "link building"]
---

# SEOJuice Skills — Setup Guide

**Source:** [calm-north/seojuice-skills](https://skills.sh/calm-north/seojuice-skills)
**GitHub:** [calm-north/seojuice-skills](https://github.com/calm-north/seojuice-skills)
**Skills:** 14 skills · 51.8K total installs
**Category:** SEO & Search Optimization
**First Seen:** August 14, 2026 evening sweep
**Quality Tier:** 🟡 Beta (community suite)

SEOJuice packages the full SEO workflow into 14 skills: keyword research (find-keywords, 6.9K installs), AI/GEO optimization (optimize-for-ai, 6.6K), link building (build-links, 6.5K), content briefing (brief), technical audit (audit, audit-speed, diagnose-seo), local ranking (rank-local), competitive analysis (beat-competitors), site migration (migrate-site), content recovery (recover-content), topic clustering (build-clusters), internal linking (fix-linking), and SERP targeting (target-serp). The suite mirrors the same SEO/AEO/GEO thesis CorpusIQ docs already ship, making it a natural fit for the docs pipeline.

---

## Installation

```bash
npx skills add calm-north/seojuice-skills
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the `skills add` installer |
| **Hermes Agent** | Any recent version |
| **SEO tools (optional)** | Some skills pair well with Search Console, Ahrefs, or Semrush data for verification |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| find-keywords | 6.9K | Keyword discovery and prioritization |
| optimize-for-ai | 6.6K | Generative Engine Optimization — optimize content for AI answer engines |
| build-links | 6.5K | Link building workflow and outreach guidance |
| brief | 6.4K | Content briefs from search intent |
| audit | 6.3K | Full technical + on-page site audit |
| rank-local | 2.4K | Local SEO ranking playbook |
| audit-speed | 2.3K | Page speed audit workflow |
| diagnose-seo | 2.1K | Rank drop diagnosis |
| beat-competitors | 2.1K | Competitor gap analysis |
| migrate-site | 2.1K | SEO-safe site migrations |
| recover-content | 2.0K | Recover lost rankings on existing content |
| build-clusters | 2.0K | Topic cluster architecture |
| fix-linking | 2.0K | Internal linking structure fixes |
| target-serp | 2.0K | SERP feature targeting |

## Quick Start

1. `npx skills add calm-north/seojuice-skills`
2. "Run find-keywords for 'business analytics platform'" — get a prioritized keyword list
3. "Audit docs.corpusiq.io for technical SEO issues"
4. "Optimize this page for AI answer engines with optimize-for-ai"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Docs SEO/AEO/GEO pass** | audit + optimize-for-ai + target-serp applied to docs.corpusiq.io pages |
| **Keyword expansion** | find-keywords and build-clusters to grow the docs keyword surface |
| **Recovery sweeps** | recover-content and diagnose-seo on pages that lost rankings |
| **Competitive tracking** | beat-competitors against data-platform competitors |

## Limitations / Verification

- Community suite — cross-check keyword and audit findings against Search Console/Ahrefs data before acting
- No bundled API tools; skills guide the agent but data sources must come from your own connectors

```bash
npx skills list | grep -i seojuice
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [SEO GEO Claude Skills Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup/) — companion GEO toolkit
- [Docs SEO/AEO/GEO strategy](/hermes/skills/catalog/) — CorpusIQ docs optimization standards

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
