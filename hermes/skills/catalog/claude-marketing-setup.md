---
title: "Claude Marketing - Full Marketing Department Skills Setup"
description: "thatrebeccarae/claude-marketing: 56 marketing skills for paid media, SEO, analytics, content and reporting in Claude Code - 7.5K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-marketing-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "marketing", "paid ads", "seo", "analytics"]
---

# Claude Marketing - Full Marketing Department Skills Setup

**Source:** [thatrebeccarae/claude-marketing](https://www.skills.sh/thatrebeccarae/claude-marketing) via skills.sh - 7.5K combined installs across 57 indexed listings; first catalogued Nov 21, 2026 (Nov 21, 2026 evening sweep)
**GitHub:** [thatrebeccarae/claude-marketing](https://github.com/thatrebeccarae/claude-marketing) - 209 stars, MIT, main branch, last pushed May 14, 2026; skills live under `skills/<name>/SKILL.md` with `REFERENCE.md` and `EXAMPLES.md` alongside, plus `skill-packs/` grouped collections, three `agents/`, and a `workflows/` n8n pipeline.
**Category:** Marketing Operations and Growth Strategy
**Quality Tier:** 🟡 Yellow - no Fail cells in the 20-skill sample; 12 Warn cells (10 Snyk and 2 Socket) with every Gen Agent Trust Hub verdict a Pass.

claude-marketing is Rebecca Rae Barton's marketing experience layer for Claude Code: 56 open-source skills, three specialized agents, and an autonomous n8n workflow for marketing teams. It spans paid media, SEO and AI search, content, CRO, analytics, ecommerce, email and lifecycle, strategy and research, creative and design, reporting, and developer tooling. Each skill ships three layers: SKILL.md (frameworks and decision trees), REFERENCE.md (benchmarks, API schemas, rate limits), and EXAMPLES.md (worked prompts with expected output), which the README describes as implementation-grade tools tested in real engagements rather than prompt templates.

The suite works beyond Claude Code through integration folders for Cursor, Aider, Windsurf, GitHub Copilot, and Gemini CLI, and the skills were tested March 2026 against Claude Code v2.1. Install counts concentrate in the paid-media and analytics skills, with facebook-ads and competitor-ads-analyst leading the sample at 200 and 196 installs.

## Installation

The README's Quick Start clones the repository and copies any skill into Claude Code, or runs a setup wizard for a related group:

```bash
git clone https://github.com/thatrebeccarae/claude-marketing.git
cp -r claude-marketing/skills/google-ads ~/.claude/skills/
```

Install a full group (for example the paid media set) with its setup wizard:

```bash
python claude-marketing/skill-packs/scripts/setup-paid-media.py
```

For multi-tool setup, the interactive installer auto-detects your installed tools:

```bash
bash scripts/install.sh
```

Each skill works independently, so install only what you need.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| facebook-ads | 200 | Meta Ads (Facebook & Instagram) platform expertise: audit campaigns, audiences, creative strategy, pixel tracking, and CAPI |
| competitor-ads-analyst | 196 | Extract and analyze competitor ads from public ad libraries (Facebook, Google, TikTok, LinkedIn) for messaging patterns and positioning gaps |
| google-tag-manager | 176 | Audit GTM containers, design tag and trigger architecture, debug firing issues, implement consent mode v2, and advise on server-side tagging |
| html-report-builder | 169 | Build polished HTML technical reports and multi-page documents with KPI cards, data tables, and recommendation cards that print to PDF |
| social-media-strategy | 159 | Platform-specific organic social strategy, content calendars, engagement tactics, community building, and performance measurement |
| looker-studio | 155 | Build dashboards, design data visualizations, connect data sources, and create marketing reports in Looker Studio |
| pro-deck-builder | 149 | Create polished HTML slide decks and PDF-ready documents with dark covers, Lora/Inter typography, and a data visualization palette |
| klaviyo-analyst | 148 | Audit Klaviyo flows, segments, campaigns, deliverability, and revenue attribution for email/SMS automation and lifecycle marketing |
| google-ads | 145 | Audit Google Ads campaigns, keywords, audiences, bidding, and conversion tracking with scored audits and wasted-spend identification |
| wasted-spend-finder | 143 | Analyze Google Ads and Meta spend to find wasted budget and produce actionable exclusion lists with thematic categorization |
| copywriting-frameworks | 143 | Framework-driven copywriting (AIDA, PAS, BAB, 4Ps, StoryBrand, QUEST, FAB) for ads, landing pages, emails, and CTAs |
| tiktok-ads | 139 | Audit TikTok Ads campaigns, creative strategy, Spark Ads, TikTok Shop integration, pixel/Events API setup, and performance |
| brand-dna | 138 | Extract brand identity (voice, colors, typography, values, audience) from a website into a brand-profile.json for downstream skills |
| utm-attribution-strategy | 137 | Build consistent UTM taxonomies, configure attribution models, and connect marketing spend to revenue across channels |
| landing-page-optimizer | 137 | Audit and optimize landing pages for conversion: above-the-fold design, value props, CTAs, social proof, forms, speed, mobile |
| google-analytics | 135 | Analyze Google Analytics data, review performance metrics, identify traffic patterns, and suggest data-driven improvements |
| icp-research | 134 | Build ideal customer profiles with pain points, objections, buying triggers, and community research for targeted messaging |
| account-structure-review | 134 | Evaluate Google and Meta account structure against conversion volume minimums and budget floors, with consolidation roadmaps |
| shopify | 133 | Audit Shopify store performance, optimize conversion funnels, configure tracking, and integrate marketing tools |
| pro-report-builder | 133 | Create polished HTML technical reports with KPI cards, data tables with severity coloring, and PDF export via Chrome headless |
| klaviyo-developer | 133 | Event schema design, SDK integration, webhook handling, rate limit strategy, and catalog sync for Klaviyo |
| content-pipeline | 133 | Multi-agent orchestration that chains research, editorial review, and social distribution agents in sequence |
| technical-seo-audit | 132 | Deep crawl analysis, Core Web Vitals, indexation health, site architecture, canonical tags, and structured data validation |
| brand-voice-guidelines | 132 | Voice development, personality archetypes, tone matrices, messaging frameworks, and style guides |
| aeo-geo-optimizer | 132 | AI search optimization to appear in ChatGPT, Perplexity, and AI Overviews with content scoring and citation patterns |
| cro-auditor | 130 | Conversion rate optimization with LIFT model heuristic evaluation, ICE/PIE prioritization, and A/B test hypothesis generation |
| ab-testing-framework | 129 | Experiment design, sample size calculation, statistical significance, and Bayesian vs frequentist analysis |
| seo-content-writer | 128 | SEO-optimized content with brand voice analysis: blog posts, social media, email campaigns, landing pages |
| retention-churn-prevention | 128 | Churn analysis, customer health scoring, cohort analysis, win-back campaigns, and CLV calculation |
| microsoft-ads | 128 | Scored Microsoft Ads audits (30 checks), Google import optimization, LinkedIn Profile Targeting, UET tracking, Clarity integration |
| market-research | 128 | Consulting-grade research reports (50+ pages): Porter's Five Forces, PESTLE, SWOT, TAM/SAM/SOM, competitive positioning |
| cross-platform-audit | 127 | Unified multi-platform scored audit across Google, Meta, and Microsoft with a budget-weighted aggregate health score |
| content-workflow | 126 | End-to-end content pipeline: research, draft, editorial review, social distribution |
| cold-email-outreach | 126 | Outbound prospecting sequences, deliverability optimization, personalization tiers, and CAN-SPAM/GDPR compliance |
| research-digest | 125 | Structured research digests from RSS feeds and web sources with source synthesis and credibility assessment |
| content-creator | 125 | Brand voice analysis, SEO optimization scripts, content calendar planning, and multi-platform strategy |
| tech-diagram | 124 | Technical architecture diagrams as standalone HTML: pipeline flows, layer stacks, component maps, timelines |
| remotion-video | 124 | Programmatic video production: spring animations, chart animations, scene transitions, audio sync |
| llms-txt | 124 | Generate llms.txt files for AI discoverability so answer engines surface your project accurately |
| customer-journey-mapping | 124 | Journey stage mapping, touchpoint inventory, drop-off analysis, and persona-based journey variants |
| linkedin-ads | 123 | B2B advertising: campaign setup, professional targeting, Lead Gen Forms, ABM campaigns, Matched Audiences |
| github-readme | 123 | Project-type-aware README generation, audit (scored 0-100), and update with voice calibration |
| data-viz-deck | 123 | PPTX decks, interactive HTML dashboards, and chart generation from audit data |
| pricing-strategy | 122 | Pricing models, value metric selection, competitive analysis, pricing page optimization, and tier design |
| email-composer | 120 | Client outreach, deliverable handoffs, scope discussions, and follow-up cadence with tone calibration |
| braze | 120 | Canvas audit, segmentation, cross-channel orchestration, data architecture, deliverability, and IP warming |
| social-preview | 118 | Generate OG social preview images (1280x640) for GitHub repos with branded dark/light themes |
| schema-markup-generator | 118 | JSON-LD structured data: Article, FAQ, HowTo, Product, Review, LocalBusiness, BreadcrumbList |
| repo-health | 118 | One-command repo health audit: standard files, GitHub config, branch protection, documentation quality |
| programmatic-seo | 118 | Template-based page generation at scale: integration pages, location pages, comparison pages, internal linking |
| dep-audit | 118 | Cross-repo dependency audit: outdated packages, security advisories, version conflicts, license issues |
| repo-scaffold | 117 | Initialize repos with standard files: LICENSE, CONTRIBUTING, SECURITY, issue/PR templates, CI config |
| frontend-design | 117 | Distinctive production-grade web interfaces: typography, color theory, motion, spatial composition |
| safe-push | 116 | Pre-push hygiene: PII/secrets scanning, commit message audit, rate-limited pushing, allowlist support |
| release-notes | 116 | Generate changelogs and GitHub releases from git history: conventional commits, PR grouping, semver |
| sync-repos | 115 | Manage public/private repo pairs: verify parity, detect drift, run sync scripts, validate no data leaks |

The remaining 1 indexed listings range from 1 to 1 installs.

## Why This Matters for Hermes Agents

The suite turns a general-purpose agent into a marketing specialist by loading platform-specific reference data, industry benchmarks, API schemas, and rate limits that the model does not have out of the box. The scored audits are the most reusable pattern here: google-ads runs 74 checks to an A-F health grade, facebook-ads runs 46, and microsoft-ads runs 30, so an agent produces a deterministic checklist instead of open-ended advice. The skills are built to chain, with each skill's output becoming context for the next, for example wasted-spend-finder feeding google-ads and account-structure-review into a restructuring roadmap. Credential handling is deliberate: API keys live in gitignored .env files, read-only API access is the default, and skills work with aggregates rather than customer PII, which matters when an agent is handed a live ad account. The klaviyo-analyst skill is MCP-first against the official Klaviyo MCP server, but every skill also works without MCP by pasting data or sharing screenshots. Portability across Cursor, Aider, Windsurf, Copilot, and Gemini CLI means the same marketing context can run wherever an agent already operates.

## Usage

| You say | What happens |
|---|---|
| Run a scored audit of my Google Ads account | Loads the google-ads framework and reference data, then walks 74 checks to an A-F health grade |
| Audit my Klaviyo flows and tell me what's missing | Runs the four-phase Klaviyo audit with flow gap analysis, segment health, and deliverability diagnostics |
| Optimize this page for AI search citations | Applies the AEO/GEO optimizer to score content and improve citation patterns for AI answer engines |
| Pull competitor ads from Meta Ad Library for these 3 brands | Extracts competitor creative from public ad libraries and surfaces messaging gaps and positioning angles |
| Build an ICP for our SaaS product targeting VP of Marketing | Produces an ideal customer profile with pain points, objections, buying triggers, and messaging angles |
| Create a dark-mode deck summarizing this month's email performance | Generates a polished HTML slide deck with a dark cover and data visualization palette for PDF export |
| Generate release notes from the last 20 commits | Writes a changelog with conventional commits, PR grouping, and semver versioning |

## Verification

Confirm the skill folders landed in the Claude Code skills directory:

```bash
ls ~/.claude/skills 2>/dev/null || ls ~/.claude/skills/google-ads
```

Inspect the google-ads and klaviyo-analyst skill instructions directly from the repository:

```bash
curl -sL https://raw.githubusercontent.com/thatrebeccarae/claude-marketing/main/skills/google-ads/SKILL.md | head -60
```

```bash
curl -sL https://raw.githubusercontent.com/thatrebeccarae/claude-marketing/main/skills/klaviyo-analyst/SKILL.md | head -60
```

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| facebook-ads | Pass | Pass | Warn |
| competitor-ads-analyst | Pass | Pass | Warn |
| google-tag-manager | Pass | Pass | Pass |
| html-report-builder | Pass | Pass | Pass |
| social-media-strategy | Pass | Pass | Pass |
| looker-studio | Pass | Warn | Warn |
| pro-deck-builder | Pass | Warn | Warn |
| klaviyo-analyst | Pass | Pass | Pass |
| google-ads | Pass | Pass | Pass |
| wasted-spend-finder | Pass | Pass | Warn |
| copywriting-frameworks | Pass | Pass | Pass |
| tiktok-ads | Pass | Pass | Warn |
| brand-dna | Pass | Pass | Warn |
| utm-attribution-strategy | Pass | Pass | Pass |
| landing-page-optimizer | Pass | Pass | Pass |
| google-analytics | Pass | Pass | Warn |
| icp-research | Pass | Pass | Warn |
| account-structure-review | Pass | Pass | Pass |
| shopify | Pass | Pass | Warn |
| pro-report-builder | Pass | Pass | Pass |

The sample carries no Fail cells; the 12 Warns split across Snyk (10) and Socket (2), concentrated on the ad-platform and dashboard skills that ship .env.example files and requirements.txt.

## Limitations

- Snapshot data, verified Nov 21, 2026: 7,464 combined installs across 57 indexed listings; 209 GitHub stars; MIT; last pushed May 14, 2026. Counts drift over time.
- The index carries 57 listings but the tree holds 56 skill directories; the 1-install gtm listing is an index-only alias with no directory, while google-tag-manager is the in-tree skill.
- Security verdicts are sampled (20 of 57 listings), not exhaustive; the remaining 37 skills were not sampled and should be checked on skills.sh before use.
- Several skills require per-platform API keys (Klaviyo pk_ key, Google service account JSON, Shopify admin token, Looker Studio Sheets credentials) stored in .env files, so setup is not zero-config.
- The reference data (benchmarks, API schemas, rate limits) reflects a March 2026 test pass against Claude Code v2.1; platform APIs change and the reference files may drift.

## Related

- [Aaron Marketing Skills - Full Marketing Department Setup](/hermes/skills/catalog/aaron-marketing-skills-setup)
- [ClawFu Skills - 175 Marketing Methodologies for AI Agents Setup](/hermes/skills/catalog/clawfu-skills-setup)
- [Kostja94 Marketing Skills - Copywriting, SEO, Ads Setup](/hermes/skills/catalog/kostja94-marketing-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with a grouped collection (setup-paid-media.py or setup-dtc.py) to install a tested set instead of copying 56 skills one at a time.
- Install only what you need; each skill works independently, so copy a single skill folder with cp -r rather than the whole tree.
- Keep API keys in .env files at the project root and never hardcode them; run python scripts/setup.py to re-validate all keys.
- Chain skills for client work: run wasted-spend-finder before google-ads and account-structure-review to turn waste analysis into a restructuring roadmap.
- For Klaviyo work, use the official MCP server or its read-only audit mode when you only need to read, and keep write scopes opt-in.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
