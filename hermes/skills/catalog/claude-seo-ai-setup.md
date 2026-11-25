---
title: "Claude SEO AI - GEO and AEO Audit Toolkit Setup"
description: "hainrixz/claude-seo-ai - 7.3K combined installs: SEO and AI-search (GEO/AEO) audit toolkit for Claude Code with dual scores and an opt-in fixer."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-seo-ai-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "seo", "geo", "aeo", "ai search"]
---

# Claude SEO AI - Setup Guide

**Source:** [hainrixz/claude-seo-ai](https://www.skills.sh/hainrixz/claude-seo-ai) via skills.sh - 7.3K combined installs across 34 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 morning sweep)
**GitHub:** [hainrixz/claude-seo-ai](https://github.com/hainrixz/claude-seo-ai) - 87 stars, MIT license, last pushed Oct 25, 2026, main branch; 34 skills under skills/<name>/SKILL.md plus a zero-dependency Node scripts/ acquisition layer, agents/, hooks/, schema/ and bilingual docs.
**Category:** SEO and AI Search (GEO/AEO)
**Quality Tier:** 🟡 Yellow - all 15 sampled skills pass Socket and none fail; geo carries a Gen Agent Trust Hub Warn and ten skills carry Snyk Warns.

hainrixz/claude-seo-ai audits any website on two independent axes, classic Search SEO and AI Visibility (GEO/AEO), and can optionally apply the safe fixes it finds. The 34 indexed skills break into five command skills (audit, geo, score, compare, fix) plus 23 seo-* audit modules spanning structured data, meta tags, Core Web Vitals, robots.txt, sitemaps, AI-crawler access and E-E-A-T. The README positions it as honest and agent-native: the four read-only commands never touch files, while fix previews everything by default and writes only after per-change confirmation.

The skills.sh index lists 34 listings at 7.3K combined installs, each with a matching skills/<name>/SKILL.md in the current tree. The deterministic half of the audit is a registry of 25 checks emitting 151 finding ids that run with no model in the loop, backed by the repo's zero-dependency Node scripts.

## Installation

The recommended path is the Claude Code plugin:

```text
/plugin marketplace add hainrixz/claude-seo-ai
/plugin install claude-seo-ai@claude-seo-ai
/reload-plugins
```

Cross-agent (Cursor, Codex, Gemini CLI, Windsurf) via Vercel Skills:

```text
npx skills add hainrixz/claude-seo-ai
```

The plugin works fully offline (Tier 0, no keys). The skills-only channel ships the Markdown but not the scripts/ acquisition layer, so the full audit pipeline runs through the plugin channel.

## What It Provides

skills.sh publishes per-skill descriptions for all 34 indexed listings, and each has a matching skills/<name>/ directory in the current tree.

| Skill | Installs | Use For |
|---|---|---|
| seo-schema-jsonld | 251 | structured data (JSON-LD) audit and generation of Tier-1 schema.org types |
| audit | 242 | full SEO and AI-search audit reporting two independent 0-100 scores |
| geo | 240 | AI-search visibility (GEO/AEO) scoring with a citability breakdown |
| fix | 240 | opt-in fixer applying safe, deterministic fixes from a persisted audit |
| seo-sitemaps | 238 | sitemaps and discovery files audit and generation |
| seo-ai-crawlers | 237 | AI-crawler access and Google AI-feature eligibility check |
| score | 237 | recompute the two scores from a persisted audit run |
| seo-meta-onpage | 235 | document head audit of title, meta description, viewport and lang |
| seo-international | 235 | hreflang annotations for multilingual sites |
| seo-internal-linking | 235 | internal-linking topology and semantic HTML audit |

The remaining 24 indexed listings range from 97 to 234 installs.

## Why This Matters for Hermes Agents

AI answer engines now sit beside classic search as a primary discovery channel, and the rules for being cited differ from the rules for ranking. This suite gives an agent both signals instead of one: a Search SEO score and an AI Visibility (GEO/AEO) score, kept separate so a page that ranks well in Google can still be flagged as uncitable by ChatGPT, Perplexity or AI Overviews. The deterministic half runs 25 checks emitting 151 finding ids with no model in the loop, so the scores are reproducible rather than vibes. The opt-in fixer writes safe, additive changes (meta, JSON-LD, robots.txt AI directives, hreflang, sitemaps) through platform adapters, with dry-run previews and per-change confirmation. For a builder running Hermes agents on customer sites, that means "is this page ready for AI search" resolves to evidence-backed findings with a runnable reproduction command instead of an opinion. The collection is large (34 skills) but organized: five command skills plus 23 seo-* modules, each with a single responsibility.

## Usage

| You say | What happens |
|---|---|
| Audit this site for SEO | Runs /claude-seo-ai:audit and reports Search SEO and AI Visibility scores |
| Will AI engines cite this page | Runs /claude-seo-ai:geo for an AI Visibility score and citability breakdown |
| Fix the SEO issues you found | Runs /claude-seo-ai:fix with a dry-run preview and per-change confirmation |
| Re-show the scores from my last audit | Runs /claude-seo-ai:score to recompute both scores from the persisted run |
| Check this page's structured data | Uses seo-schema-jsonld to validate and complete JSON-LD |
| Compare my staging and production sites | Runs /claude-seo-ai:compare to diff two URLs or runs |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/hainrixz/claude-seo-ai/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/hainrixz/claude-seo-ai/main/skills/audit/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| seo-schema-jsonld | Pass | Pass | Warn |
| audit | Pass | Pass | Warn |
| geo | Warn | Pass | Warn |
| fix | Pass | Pass | Pass |
| seo-sitemaps | Pass | Pass | Pass |
| seo-ai-crawlers | Pass | Pass | Pass |
| score | Pass | Pass | Pass |
| seo-meta-onpage | Pass | Pass | Warn |
| seo-international | Pass | Pass | Warn |
| seo-internal-linking | Pass | Pass | Warn |
| seo-core-web-vitals | Pass | Pass | Pass |
| seo-orchestrator | Pass | Pass | Warn |
| seo-local | Pass | Pass | Warn |
| seo-eeat | Pass | Pass | Warn |
| seo-crawlability | Pass | Pass | Warn |

Sampled 15 of 34 indexed listings. No Fail verdicts; geo carries the only Gen Agent Trust Hub Warn and ten skills carry Snyk Warns.

## Limitations

- Snapshot data, verified Nov 25, 2026: 7,275 combined installs across 34 indexed listings; 87 GitHub stars; MIT license; last pushed Oct 25, 2026. Counts drift over time.
- The skills-only channel (npx skills add) ships the Markdown but not the scripts/ acquisition layer, so the deterministic checks only run through the plugin channel.
- The fixer writes only after per-change confirmation, but some platform adapters (WordPress, BigCommerce) have no staging surface, so changes are live on write.
- Tier 0 works offline; browser rendering (Tier 1) and Search Console or Merchant Center data (Tier 2) need extra setup.
- By design, llms.txt and the other AI discovery files (M21) are reported but scored 0, and the optional web-search and Search Console import results carry severity 0.

## Related

[Infrasity Dev GTM Skills - SEO, GEO and Marketing Setup](/hermes/skills/catalog/infrasity-dev-gtm-skills-setup) | [AI Marketing Skills - 24-Skill Operator Toolkit](/hermes/skills/catalog/ai-marketing-claude-code-skills-setup) | [Boring Marketing Skills - Marketing Operator Suite Setup](/hermes/skills/catalog/boring-marketing-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the plugin rather than only npx skills so the scripts/ acquisition layer runs the deterministic checks.
- Keep the two scores separate: a page can rank well in Google yet be uncited by AI engines.
- Run audit or geo read-only first; fix always previews and writes only after you confirm each change.
- Leave render on the static default so a run never launches a browser unless you ask for it.
- Review the skills.sh verdicts above before relying on the module skills in production.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
