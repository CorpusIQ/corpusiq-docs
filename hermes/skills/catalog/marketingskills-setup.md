---
title: marketingskills — Complete Marketing Suite for Hermes (160K+ installs)
description: Install and use coreyhaines31/marketingskills — 12 battle-tested marketing skills for SEO, copywriting, content strategy, lead generation, social media, and AI marketing.
---

# marketingskills — Setup Guide

**Source:** [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (160K+ combined installs)
**Category:** Marketing Suite
**Languages:** JavaScript, Python

The most comprehensive marketing skill suite on skills.sh. 12 production-grade skills covering the complete marketing stack: SEO audit (163.9K), copywriting (154.1K), marketing psychology (113K), content strategy (108.4K), programmatic SEO (104K), marketing ideas (101.1K), AI SEO (92.4K), lead magnets (70.8K), social content (67.5K), product marketing context (61.6K), image generation (44.9K), and social strategy (36.8K).

---

## Installation

Install individual skills as needed for your workflow:

```bash
# Core marketing stack (install these first)
npx skills add coreyhaines31/marketingskills@seo-audit
npx skills add coreyhaines31/marketingskills@copywriting
npx skills add coreyhaines31/marketingskills@content-strategy

# Advanced marketing
npx skills add coreyhaines31/marketingskills@marketing-psychology
npx skills add coreyhaines31/marketingskills@programmatic-seo
npx skills add coreyhaines31/marketingskills@marketing-ideas

# Growth & lead gen
npx skills add coreyhaines31/marketingskills@lead-magnets
npx skills add coreyhaines31/marketingskills@social-content
npx skills add coreyhaines31/marketingskills@product-marketing-context

# AI-powered marketing
npx skills add coreyhaines31/marketingskills@ai-seo

# Media & social
npx skills add coreyhaines31/marketingskills@image
npx skills add coreyhaines31/marketingskills@social
```

Verify:
```bash
npx skills list | grep marketingskills
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | 18+ (for npx skills CLI) |
| **Hermes Agent** | Any version |
| **API Keys** | None required — all skills are prompt/instruction based |
| **Optional** | Firecrawl API key enhances `seo-audit` and `programmatic-seo` |

---

## Skill Reference

### Tier 1: Core Marketing (Install First)

| Skill | Installs | What It Does | CorpusIQ Use Case |
|---|---|---|---|
| `seo-audit` | 163.9K | Full technical SEO analysis — crawl, index, rank | corpusiq-docs SEO optimization |
| `copywriting` | 154.1K | Persuasive marketing copy across formats | Landing pages, ads, email campaigns |
| `content-strategy` | 108.4K | Content calendars, topic clusters, pillar pages | Blog and docs content planning |

### Tier 2: Strategy & Psychology

| Skill | Installs | What It Does | CorpusIQ Use Case |
|---|---|---|---|
| `marketing-psychology` | 113.0K | Consumer behavior, persuasion frameworks, Cialdini | Conversion optimization, pricing page |
| `programmatic-seo` | 104.0K | Automated SEO at scale — 1000s of pages | corpusiq-docs programmatic pages |
| `marketing-ideas` | 101.1K | Creative campaign concepts, viral hooks | Social media campaign ideation |

### Tier 3: Growth & Lead Gen

| Skill | Installs | What It Does | CorpusIQ Use Case |
|---|---|---|---|
| `lead-magnets` | 70.8K | Lead capture design, conversion assets | Gated content, email list building |
| `social-content` | 67.5K | Platform-optimized social posts | Daily X/LinkedIn/Reddit content |
| `product-marketing-context` | 61.6K | Positioning, messaging, competitive differentiation | CorpusIQ product messaging |

### Tier 4: AI & Media

| Skill | Installs | What It Does | CorpusIQ Use Case |
|---|---|---|---|
| `ai-seo` | 92.4K | AI-optimized SEO strategies, semantic search | Next-gen SEO for AI search engines |
| `image` | 44.9K | Marketing image generation, social graphics | Social media visuals, blog headers |
| `social` | 36.8K | Social media strategy, platform selection, scheduling | Multi-platform growth strategy |

---

## Common Workflows for CorpusIQ

### Daily SEO Health Check

```bash
# Run full SEO audit on corpusiq-docs
npx skills run coreyhaines31/marketingskills@seo-audit \
  --url "https://corpusiq.io/docs" \
  --output "seo-report-$(date +%Y%m%d).md"
```

### Landing Page Copy Generation

```bash
# Generate conversion-optimized copy for a new feature page
npx skills run coreyhaines31/marketingskills@copywriting \
  --product "CorpusIQ" \
  --feature "AI Business Intelligence" \
  --audience "business operators" \
  --format "landing-page"
```

### Content Calendar Generation

```bash
# Generate 30-day content calendar for all platforms
npx skills run coreyhaines31/marketingskills@content-strategy \
  --brand "CorpusIQ" \
  --platforms "x,linkedin,reddit,blog" \
  --duration "30 days" \
  --output "content-calendar-july.md"
```

### Social Post Creation

```bash
# Create platform-optimized posts from a blog article
npx skills run coreyhaines31/marketingskills@social-content \
  --source "blog/why-operators-need-ai.md" \
  --platforms "x,linkedin,reddit" \
  --tone "technical,helpful"
```

### Lead Magnet Design

```bash
# Design a lead magnet for email capture
npx skills run coreyhaines31/marketingskills@lead-magnets \
  --audience "ecommerce operators" \
  --problem "inventory forecasting" \
  --format "calculator+guide"
```

---

## Integration with Existing CorpusIQ Stack

| Existing Skill | marketingskills Complement | Combined Power |
|---|---|---|
| `clawfu-skills` (175 methodologies) | `marketing-psychology` (113K) | Theory (ClawFu) + execution (marketingskills) |
| `firecrawl-workflows` (120K) | `seo-audit` (163.9K) | Crawl data (Firecrawl) + SEO analysis (marketingskills) |
| `corpusiq-content-strategy` | `content-strategy` (108.4K) | Brand voice (CIQ) + calendar execution (marketingskills) |
| `help-first-community-engagement` | `social-content` (67.5K) | Engagement strategy + content creation |
| `corpusiq-social-cadence-engine` | `social` (36.8K) | Posting schedule + platform strategy |

---

## Comparison: marketingskills vs clawfu-skills

| Feature | marketingskills | clawfu-skills |
|---|---|---|
| **Scope** | Execution-focused (create content, run audits) | Methodology-focused (175 frameworks) |
| **Install base** | 160K+ | 134⭐ (GitHub) |
| **Delivery** | Skills CLI (npx) | MCP server |
| **Best for** | Doing marketing work | Learning marketing principles |
| **Content creation** | ✅ Direct post/copy generation | ❌ Frameworks only |
| **SEO** | ✅ Full technical audit | ❌ Not covered |
| **Strategy** | ⚠️ Light strategy support | ✅ Deep frameworks (Dunford, Reforge) |
| **CorpusIQ use case** | Daily execution engine | Strategic decision support |

**Recommendation:** Use both. clawfu-skills for strategic direction (which frameworks apply?), marketingskills for tactical execution (create the actual content, run the audits).

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Skill returns generic output | Missing context/parameters | Provide specific `--audience`, `--product`, `--format` flags |
| `seo-audit` slow on large sites | Crawling without rate limits | Add `--max-pages 100` for initial scan |
| `copywriting` tone doesn't match brand | No brand voice guidance | Pass `--brand-voice "technical, operator-focused"` |
| `social-content` posts too generic | Missing platform context | Specify `--platforms "x"` for platform-specific formatting |
| `programmatic-seo` overwhelming | Too many pages generated | Set `--template-count 10` for initial batch |

---

## See Also

- [clawfu-skills](/hermes/skills/catalog/clawfu-skills-setup/) — 175 marketing methodologies as MCP server
- [firecrawl-workflows](/hermes/skills/catalog/firecrawl-workflows-setup/) — Web research & SEO workflows (120K installs)
- [corpusiq-content-strategy](/hermes/skills/) — CorpusIQ's belief-bridge content framework
- [seo-geo](/hermes/skills/catalog/seo-geo-setup/) — Generative Engine Optimization
