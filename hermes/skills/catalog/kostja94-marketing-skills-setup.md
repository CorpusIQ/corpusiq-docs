---
title: Kostja94 Marketing Skills — Copywriting, SEO, ads, and content for Hermes Agents
description: 7+ marketing-focused skills covering copywriting (3K), programmatic SEO (1.7K), Meta ads (1.7K), Google Search Console (1.3K), TikTok ads (1K), legal pages, and website structure. 7.6K+ combined installs, 760⭐.
---

# Kostja94 Marketing Skills — Setup Guide

**Source:** [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) (760⭐, 7,600+ combined installs)
**Category:** Marketing & Growth
**Quality Tier:** 🟡 Beta

A focused collection of marketing execution skills for Hermes agents managing growth operations. Covers the full marketing stack: short-form copywriting (PAS/AIDA/BAB frameworks), programmatic SEO at scale, paid advertising on Meta and TikTok, Google Search Console analytics, legal page generation, and website structure optimization.

---

## Installation

```bash
npx skills add kostja94/marketing-skills --skill copywriting
npx skills add kostja94/marketing-skills --skill programmatic-seo
npx skills add kostja94/marketing-skills --skill meta-ads
npx skills add kostja94/marketing-skills --skill google-search-console
npx skills add kostja94/marketing-skills --skill tiktok-ads
npx skills add kostja94/marketing-skills --skill legal-page-generator
npx skills add kostja94/marketing-skills --skill website-structure
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **copywriting** | 3.0K | Short-form marketing copy — headlines, CTAs, ad copy, landing pages, email copy. Uses PAS, AIDA, BAB, FAB, and 4 U's frameworks. Checks project context for brand voice |
| **programmatic-seo** | 1.7K | Generate SEO-optimized pages at scale using data sources, templates, and keyword research |
| **meta-ads** | 1.7K | Create and manage Meta (Facebook/Instagram) ad campaigns — targeting, creative, budget, optimization |
| **google-search-console** | 1.3K | Query GSC data — search performance, indexing status, sitemaps, core web vitals. API-first approach |
| **tiktok-ads** | 1.0K | TikTok advertising — creative best practices, audience targeting, Spark Ads, TikTok Shop integration |
| **legal-page-generator** | 958 | Generate privacy policies, terms of service, cookie notices, and GDPR/CCPA compliance pages |
| **website-structure** | 953 | Audit and optimize website information architecture — URL structure, internal linking, crawl depth |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Google APIs** | GSC skill needs Google OAuth with Search Console scope |
| **Meta Business** | Meta Ads skill needs Meta Business Suite access and ad account |
| **TikTok Business** | TikTok Ads skill needs TikTok Ads Manager account |
| **Python 3.8+** | Required for programmatic SEO and GSC API scripts |

---

## Key Capabilities

### Copywriting Engine
Framework-driven copywriting that adapts to brand voice. Reads `.claude/project-context.md` or `.cursor/project-context.md` on first use to extract positioning, value proposition, and brand voice. Supports five proven frameworks: PAS (Problem-Agitation-Solution), AIDA (Attention-Interest-Desire-Action), BAB (Before-After-Bridge), FAB (Features-Advantages-Benefits), and the 4 U's (Useful, Urgent, Unique, Ultra-specific).

### Programmatic SEO
Generate hundreds or thousands of landing pages from structured data. Combine keyword research, templates, and data sources to create SEO-optimized content at scale. Ideal for directory sites, location pages, and product variant pages.

### Paid Advertising
End-to-end campaign management for Meta and TikTok. Covers creative generation, audience targeting, budget optimization, A/B testing, and performance analysis. Distinct from strategy skills — these are execution-focused.

### Google Search Console API
Direct API access to search performance data — clicks, impressions, CTR, position. Query by page, query, country, device. Monitor indexing status, submit sitemaps, and track core web vitals.

---

## Quick Start

```bash
# Copywriting — generate ad headlines using PAS framework
npx skills use kostja94/marketing-skills@copywriting

# Check GSC performance for last 28 days
npx skills use kostja94/marketing-skills@google-search-console

# Generate programmatic landing pages
npx skills use kostja94/marketing-skills@programmatic-seo
```

---

## Verification

```bash
npx skills list | grep kostja94
```

---

## Notes

- Copywriting skill auto-detects project context files for brand voice — works seamlessly with Hermes projects that have CONSTITUTION.md or brand guidelines
- Programmatic SEO is particularly powerful for CorpusIQ's growth strategy — generate landing pages for each vertical/use case
- GSC skill uses Google API directly, not scraping — requires OAuth setup but provides reliable data
- Legal page generator covers GDPR (EU), CCPA (California), and standard privacy policies — useful for rapid landing page deployment
- Complements existing catalog entries: `seo-audit`, `content-strategy`, `copywriting` skills from other publishers
- MIT licensed — safe for commercial use
