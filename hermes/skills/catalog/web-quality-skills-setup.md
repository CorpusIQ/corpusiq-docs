---
title: web-quality-skills — Google-Grade Web Quality Audits for Hermes (37K installs)
description: Install and use addyosmani/web-quality-skills — accessibility, SEO, performance, and comprehensive web quality audits from Google Chrome's engineering lead. WCAG 2.1, Core Web Vitals, structured data validation.
---

# web-quality-skills — Setup Guide

**Source:** [addyosmani/web-quality-skills](https://github.com/addyosmani/web-quality-skills) (37,000 installs)
**Category:** Web Quality / SEO
**Languages:** JavaScript

Web quality audit skills from Addy Osmani, Google Chrome's engineering lead. Four skills encoding Google's own web quality standards: `accessibility` (37K, WCAG 2.1 AA/AAA), `seo` (33.4K, technical SEO + Core Web Vitals), `performance` (23.5K, Lighthouse + bundle analysis), and `web-quality-audit` (16.5K, combined audit with prioritized fixes). Same criteria used by Lighthouse, PageSpeed Insights, and Chrome DevTools.

---

## Installation

```bash
# Accessibility audit
npx skills add addyosmani/web-quality-skills@accessibility

# SEO audit
npx skills add addyosmani/web-quality-skills@seo

# Performance audit
npx skills add addyosmani/web-quality-skills@performance

# Combined audit (recommended — runs all three)
npx skills add addyosmani/web-quality-skills@web-quality-audit
```

Verify:
```bash
npx skills list | grep web-quality
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | 18+ |
| **Hermes Agent** | Any version |
| **Chrome/Chromium** | For Lighthouse-based performance audits |
| **Lighthouse CLI** | `npm install -g lighthouse` (for `performance` and `web-quality-audit`) |
| **Site URL** | Publicly accessible (or localhost for dev audits) |

---

## Key Capabilities

### accessibility: WCAG 2.1 AA/AAA Audit

```
┌──────────────────┐     ┌───────────────────┐     ┌──────────────────┐
│  Site URL         │ ──▶ │  Multi-Rule       │ ──▶ │  Prioritized     │
│  (corpusiq.io)    │     │  Audit Engine     │     │  Fix List + Code │
└──────────────────┘     └───────────────────┘     └──────────────────┘
```

```bash
# Full WCAG 2.1 AA audit
web-quality accessibility \
  --url "https://corpusiq.io/docs" \
  --level "AA" \
  --output "audits/a11y-report.md"

# AAA audit (stricter, includes AA violations)
web-quality accessibility \
  --url "https://corpusiq.io" \
  --level "AAA" \
  --include-warnings \
  --output "audits/a11y-aaa.md"
```

**Audit coverage:**
- Color contrast (text, non-text, focus indicators)
- Keyboard navigation (tab order, skip links, focus trapping)
- Screen reader compatibility (landmarks, labels, live regions)
- Form accessibility (labels, error messages, autocomplete)
- Media accessibility (alt text, captions, audio descriptions)
- Dynamic content (ARIA live regions, focus management)
- Touch targets (minimum 44x44px, adequate spacing)

### seo: Technical SEO + Structured Data

```bash
# Full technical SEO audit
web-quality seo \
  --url "https://corpusiq.io" \
  --crawl-depth 3 \
  --output "audits/seo-report.md"

# Check specific pages
web-quality seo \
  --url "https://corpusiq.io/docs/hermes/skills/catalog/" \
  --check "meta,structured-data,core-web-vitals,mobile-friendly"
```

**Audit coverage:**

| Category | Checks |
|---|---|
| **Meta tags** | Title (50-60 chars), description (150-160), canonical, hreflang, robots, OG tags |
| **Structured data** | JSON-LD validation, Schema.org types, rich result eligibility |
| **Core Web Vitals** | LCP (<2.5s), INP (<200ms), CLS (<0.1) |
| **Mobile-friendly** | Viewport, tap targets, font size, content width |
| **Indexability** | Robots.txt, sitemap.xml, noindex tags, canonical chains |
| **Internal linking** | Orphan pages, click depth, anchor text quality |
| **Content quality** | Thin content detection, duplicate content, keyword usage |

### performance: Lighthouse + Bundle Analysis

```bash
# Lighthouse performance audit
web-quality performance \
  --url "https://corpusiq.io" \
  --device "mobile" \
  --throttling "4g" \
  --output "audits/perf-report.md"

# Bundle analysis (requires local build)
web-quality performance \
  --url "https://corpusiq.io" \
  --mode "bundle" \
  --build-dir "corpusiq-docs/site/" \
  --output "audits/bundle-report.md"
```

**Performance metrics:**
- FCP (First Contentful Paint)
- LCP (Largest Contentful Paint) — target <2.5s
- TBT (Total Blocking Time) — target <200ms
- CLS (Cumulative Layout Shift) — target <0.1
- INP (Interaction to Next Paint) — target <200ms
- Speed Index — target <3.4s

**Bundle analysis:**
- Chunk size breakdown (per-route code splitting audit)
- Tree-shaking effectiveness (unused exports detection)
- Third-party impact (size + blocking time per vendor)
- Image optimization (uncompressed, wrong format, missing srcset)
- Font loading strategy (FOIT/FOUT, font-display, subsetting)

### web-quality-audit: Combined + Prioritized

```bash
# Run all audits in one pass
web-quality audit \
  --url "https://corpusiq.io" \
  --checks "accessibility,seo,performance" \
  --output "audits/combined-report-$(date +%Y%m%d).md"
```

**Combined report structure:**
1. **Executive summary** — overall score, critical issues count, estimated fix time
2. **Critical issues** (must fix — blocking, legal risk, SEO penalty)
3. **High priority** (should fix — user impact, ranking impact)
4. **Medium priority** (nice to fix — minor UX, optimization)
5. **Low priority** (cosmetic — no user/ranking impact)
6. **Fix timeline** — estimated effort per issue, recommended order

---

## Common Workflows for CorpusIQ

### Pre-Deployment Quality Gate

```bash
# Run combined audit before every docs deployment
web-quality audit \
  --url "https://corpusiq.io" \
  --checks "accessibility,seo,performance" \
  --threshold "90" \
  --block-on-critical \
  --output "audits/pre-deploy-$(date +%Y%m%d-%H%M).md"

# Exit code 1 if critical issues found → CI fails
```

### Weekly SEO Health Check

```bash
# Scheduled SEO audit for corpusiq-docs
web-quality seo \
  --url "https://corpusiq.io/docs/" \
  --crawl-depth 2 \
  --compare "audits/seo-baseline.md" \
  --output "audits/seo-weekly-$(date +%Y%m%d).md"
```

The `--compare` flag diffs against a baseline to catch regressions:
- New broken links since last week
- Pages that dropped in Core Web Vitals
- Structured data that stopped validating

### Competitor Quality Comparison

```bash
# Compare corpusiq.io against competitors
for site in "https://corpusiq.io" "https://competitor1.com" "https://competitor2.com"; do
  web-quality audit \
    --url "$site" \
    --output "audits/$(echo $site | sed 's|https://||' | sed 's|/|-|g')-$(date +%Y%m%d).md"
done
```

### CI Integration

```yaml
# .github/workflows/quality.yml
- name: Web Quality Audit
  run: |
    npx skills run addyosmani/web-quality-skills@web-quality-audit \
      --url "${{ secrets.STAGING_URL }}" \
      --checks "accessibility,seo,performance" \
      --threshold "90" \
      --block-on-critical \
      --output "audits/ci-${GITHUB_SHA}.md"
```

---

## Quality Score Thresholds

| Score | Rating | Meaning |
|---|---|---|
| 90-100 | 🟢 Good | Passes all checks, no action needed |
| 70-89 | 🟡 Needs Work | Some issues, but not critical |
| 50-69 | 🟠 Poor | Multiple issues, significant user/SEO impact |
| 0-49 | 🔴 Critical | Major failures, likely legal/accessibility risk |

---

## Comparison: web-quality-skills vs Other Audit Tools

| Feature | web-quality-skills | Lighthouse CI | axe-core | Semrush |
|---|---|---|---|---|
| **Accessibility** | ✅ WCAG 2.1 AA/AAA | ⚠️ Basic | ✅ Best-in-class | ❌ |
| **SEO** | ✅ Technical + structured data | ⚠️ Basic only | ❌ | ✅ Full |
| **Performance** | ✅ Lighthouse + bundle | ✅ Lighthouse | ❌ | ⚠️ Basic |
| **Combined audit** | ✅ Prioritized fix list | ❌ Separate reports | ❌ | ⚠️ Separate |
| **Hermes integration** | ✅ CLI skill | ⚠️ Via npm | ⚠️ Via npm | ❌ |
| **Cost** | Free | Free | Free | $139+/mo |
| **Author** | Google Chrome lead | Google Chrome | Deque Systems | Semrush |
| **Install base** | 37K | N/A (tool) | N/A (library) | N/A (SaaS) |

**Recommendation:** web-quality-skills is the only tool that combines all three audit types (a11y, SEO, perf) into a single Hermes-native skill, with prioritized fix lists, from the Chrome engineering lead. Use it as the primary quality gate; supplement with axe-core for deep a11y testing.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Performance audit fails | Chrome not installed | `npx lighthouse --help` to check; install Chromium |
| SEO crawl incomplete | JavaScript-rendered content | Add `--javascript-rendering` flag (slower) |
| Accessibility false positives | Dynamic content not settled | Add `--wait-for "selector"` to wait for content |
| Structured data validation fails | JSON-LD not in `<head>` | Check placement; use `--check-inline-jsonld` |
| Audit slow on large sites | Crawling all pages | Set `--max-pages 50` for large sites |
| `web-quality: command not found` | Skill not installed | `npx skills add addyosmani/web-quality-skills@web-quality-audit` |

---

## See Also

- [marketingskills](/hermes/skills/catalog/marketingskills-setup/) — SEO audit + content strategy (160K installs)
- [firecrawl-seo-audit](/hermes/skills/catalog/firecrawl-workflows-setup/) — Technical SEO crawl (29.2K installs)
- [vercel-agent-skills](/hermes/skills/catalog/vercel-agent-skills-setup/) — Web design guidelines + optimization (29K installs)
- [seo-geo](/hermes/skills/catalog/) — Generative Engine Optimization for AI search
