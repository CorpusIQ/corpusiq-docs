---
title: "Claude SEO - 31-Skill Universal SEO Suite Setup for Hermes Agents"
description: "AgriciDaniel/claude-seo - 31 Agent Skills covering technical SEO, E-E-A-T content, schema, GEO/AEO, backlinks, local, ecommerce, and international SEO with 25 sub-skills and 18 sub-agents. 160K+ skills.sh installs, 16.6K-star repo."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-seo-setup/"
robots: "index,follow"
last_updated: "2026-09-09"
tags: ["hermes skill", "agent skill", "skill setup", "seo", "geo", "content strategy", "technical seo"]
---

# Claude SEO - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/agricidaniel/claude-seo/seo) (31 skills, ~160,000 combined installs)
**GitHub:** [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) (16,628⭐, 2,436 forks, MIT, very active)
**Category:** Marketing / SEO
**First Seen:** Jul 23, 2026 sweep (rejected as "Claude Code-specific"); **overturned Sep 9, 2026** — 31 skills are now on skills.sh in open Agent Skills format with broad cross-agent adoption
**Quality Tier:** 🟡 Production (Gen Agent Trust Hub Pass / Socket Pass / Snyk Warn — W011 third-party content exposure, inherent to SEO workflows)

A universal SEO suite: 25 core skills + 6 extension skills, with the flagship `seo-audit` crawling up to 500 pages and delegating to up to 15 parallel specialist sub-agents. Covers technical SEO, E-E-A-T content quality, Schema.org, AI-search optimization (GEO/AEO), backlinks, local SEO, e-commerce, international SEO, and Google APIs — every audit output is a prioritized action plan with falsifiable recommendations grounded in Google primary-source guidance.

---

## Installation

The skills themselves are open Agent Skills format and install via skills.sh:

```bash
npx skills add agricidaniel/claude-seo
```

For Hermes Agent, copy from a clone:

```bash
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
cp -r claude-seo/skills/* ~/.hermes/skills/
```

**Heavy-tool dependency:** several skills (e.g. `seo-audit`) call `claude-seo run render_page.py` — a CLI installed by the repo's setup script (isolated Python env + Playwright Chromium). Install it once per machine:

```bash
bash claude-seo/install.sh        # from the clone; review before running
claude-seo doctor                 # verify the toolchain
```

(Claude Code users can instead use the plugin path: `/plugin marketplace add AgriciDaniel/claude-seo` → `/plugin install claude-seo@agricidaniel-claude-seo` → `/seo setup`. That path is Claude-Code-specific; the skills.sh + manual paths above are not.)

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Skills directory support (`~/.hermes/skills/`) |
| **Python 3 + Playwright** | Installed by `install.sh` for the render tooling (headless Chromium for page rendering/SPA capture) |
| **Node.js 18+** | For the `npx skills` path |
| **Optional API keys** | Extension skills: DataForSEO, Firecrawl, Ahrefs, Bing Webmaster, SE Ranking, Unlighthouse, Profound, Banana (image gen) — each extension is optional |

## Skill Roster (core)

| Skill | Installs | What it does |
|---|---|---|
| `seo` | 6,660 | Orchestrator — routes requests to the right sub-skill |
| `seo-audit` | 6,027 | Full-site audit: crawls ≤500 pages, detects business type, delegates to ≤15 specialists, health score |
| `seo-content` | 5,797 | E-E-A-T content quality analysis + optimization |
| `seo-competitor-pages` | 5,747 | Competitor page-level analysis |
| `seo-sitemap` / `seo-technical` | 5,613 / 5,427 | Sitemap audits / technical crawl diagnostics |
| `seo-geo` | 5,399 | AI-search optimization: citability scoring, llms.txt, primary-source alignment |
| `seo-schema` | 5,358 | Schema.org detect, validate, generate |
| `seo-page` | 5,273 | Deep single-page analysis |
| `seo-backlinks` / `seo-plan` | 5,247 / 5,232 | Backlink strategy / prioritized action planning |
| `seo-images` / `seo-hreflang` / `seo-programmatic` / `seo-local` / `seo-cluster` / `seo-google` / `seo-maps` / `seo-ecommerce` / `seo-drift` / `seo-sxo` / `seo-flow` | 4.1K–5.2K | Images, international, programmatic, local, semantic clustering, Google APIs, maps intelligence, e-commerce, ranking drift, search experience optimization, workflow engine |
| `seo-content-brief` | 4,115 | Content briefs grounded in SERP evidence |
| Extensions | 58–69 | `seo-firecrawl`, `seo-ahrefs`, `seo-dataforseo`, `seo-bing`, `seo-seranking`, `seo-profound`, `seo-unlighthouse`, `seo-image-gen` |

## Quick Start

1. Install skills + run `install.sh` once
2. "Audit corpusiq.io" → `seo-audit` crawls and produces a prioritized action plan
3. "Check our AI-search visibility" → `seo-geo` for citability/llms.txt/AEO
4. "Write a content brief for [keyword]" → `seo-content-brief`

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Docs SEO/AEO/GEO program** | CorpusIQ's docs SEO pass (frontmatter, llms.txt, JSON-LD) gets automated audit + fix loops via `seo-audit`, `seo-geo`, `seo-schema` |
| **Competitive SEO intelligence** | `seo-competitor-pages` + `seo-drift` for tracking competitor ranking moves — feeds the competitive-attack playbook |
| **Content briefs** | `seo-content-brief` for SERP-grounded briefs before any blog/docs page is written |
| **Technical SEO hygiene** | `seo-technical` + `seo-sitemap` as a recurring site-health check for corpusiq.io and client domains |

## Limitations / Verification

- **Snyk Warn (W011, MEDIUM):** skills ingest arbitrary third-party URLs (audited pages, SERPs) — indirect prompt-injection surface. Standard mitigation: treat page content as data, never as instructions; the skill's own workflow already separates analysis from actions
- **Distribution is Claude-Code-first upstream** (plugin marketplace, `/seo` slash commands) — but the SKILL.md layer is platform-agnostic and that is what skills.sh installs
- **Extension skills are low-install on skills.sh** (58–69) but functional; they just aren't widely adopted yet

```bash
# Verify skill installed
ls ~/.hermes/skills/seo-audit/SKILL.md ~/.hermes/skills/seo-geo/SKILL.md
# Verify toolchain
claude-seo doctor
```

## Security

Verified Sep 9, 2026 on `seo`, `seo-audit`, `seo-content`:

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Pass |
| Socket | Pass |
| Snyk | Warn (MEDIUM W011 — third-party content exposure, inherent to SEO workflows) |

## Related

- [SEO GEO Claude Skills Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup/)
- [AI SEO - Skills Marketplace](/hermes/skills/marketplace/)

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
*Powered by CorpusIQ*
