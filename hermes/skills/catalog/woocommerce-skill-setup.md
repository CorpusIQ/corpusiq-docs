---
title: "WooCommerce Skills - Store Operations via REST API Setup"
description: "navarroido/woocommerce-skill - 1.9K combined installs: 56 REST API workflow skills for operating WooCommerce stores."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/woocommerce-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "woocommerce", "ecommerce", "rest api"]
---

# WooCommerce Skills - Setup Guide

**Source:** [navarroido/woocommerce-skill](https://www.skills.sh/navarroido/woocommerce-skill) via skills.sh - 1.9K combined installs across 56 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [navarroido/woocommerce-skill](https://github.com/navarroido/woocommerce-skill) - 8 stars, MIT license, last pushed Nov 19, 2026, claude/woocommerce-ai-skills-0ZaZD branch; skills live under skills/<category>/<name>/SKILL.md.
**Category:** Ecommerce Store Operations (WooCommerce)
**Quality Tier:** 🟡 Yellow - 12 of 56 listings sampled: no Fail verdicts, but six Snyk Warn cells across six skills.

navarroido/woocommerce-skill is a community-maintained collection of 56 markdown workflow files that teach an AI agent how to operate a WooCommerce store through the REST API. The skills span merchandising, order management, customer operations and support, marketing, finance, store management, and analytics. Each skill declares which WooCommerce REST endpoints it uses and follows a four-phase model (query, dry-run preview, confirm, report), and every mutating skill defaults to dry_run on first run. The 56 listings form a flat install band: skills.sh reports between 33 and 36 installs per listing, with one unit install spreading across the whole catalog. The default branch is claude/woocommerce-ai-skills-0ZaZD, not main.

## Installation

The README documents three install paths, one per agent:

```bash
/plugin install navarroido/Woocommerce-skill
```

for Claude Code, then:

```bash
gh skill install navarroido/Woocommerce-skill
```

for GitHub Copilot, and for all other agents (Cursor, Cline, Gemini CLI, Codex):

```bash
npx skills add navarroido/Woocommerce-skill
```

After installing, connect your store with the WC_STORE_URL, WC_CONSUMER_KEY, and WC_CONSUMER_SECRET environment variables; generate keys at WooCommerce > Settings > Advanced > REST API > Add Key.

## What It Provides

skills.sh publishes per-skill install counts for all 56 indexed listings. The install band is flat (33 to 36 installs each), so the 10 listings at or above 35 installs are listed below and the remaining 46 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| woo-category-reorganization | 36 | reassign products between categories in bulk based on tag or meta_data filters, with dry-run |
| woo-webhook-health-check | 35 | list all webhooks with delivery URL, status, and failure count |
| woo-tracking-number-update | 35 | set or update tracking number and shipping provider meta on fulfilled orders, with dry-run |
| woo-shipping-cost-analysis | 35 | compare shipping_total collected from customers against configured zone rates |
| woo-seo-metadata-audit | 35 | scan products and categories for missing or short SEO titles and meta descriptions |
| woo-inventory-valuation-report | 35 | compute total inventory value by category and export a financial summary |
| woo-dead-stock-identifier | 35 | find products with zero sales in the last N days but positive stock |
| woo-customer-note-bulk-annotator | 35 | append a note to multiple customers matching role, spend, or country filters, with dry-run |
| woo-coupon-bulk-generator | 35 | create N unique coupon codes with configurable discount, amount, and expiry, with dry-run |
| woo-abandoned-cart-recovery | 35 | query pending orders older than a threshold and export a re-engagement list |

The remaining 46 indexed listings range from 33 to 34 installs.

## Why This Matters for Hermes Agents

The catalog turns a WooCommerce store into a set of named, repeatable REST API workflows, which is exactly what a store-operator agent needs instead of improvising wp-json calls. Every mutating skill defaults to dry_run and prints a preview before asking for confirmation, so an agent can propose bulk changes (price adjustments, category moves, coupon generation) without destructive surprises. The read-only reporting skills (inventory valuation, tax liability, SEO gaps, dead stock) give an agent concrete queries for the health of a store. The four-phase model (query, preview, confirm, report) is a sound default for any agent that mutates production data over an API. Because each skill names its REST endpoints and authentication requirements, the catalog doubles as living documentation for the WooCommerce v3 endpoints.

## Usage

| You say | What happens |
|---|---|
| Mark down all products in Accessories 10% | Uses woo-bulk-price-adjustment with a dry-run preview first |
| Find orders stuck in processing | Uses woo-wismo-bulk-status-report to export a WISMO CSV |
| Generate 50 coupon codes | Uses woo-coupon-bulk-generator for configurable discount and expiry |
| Audit missing SEO descriptions | Uses woo-seo-metadata-audit for a prioritized gap report |
| Move these products to a new category | Uses woo-category-reorganization with tag or meta filters |
| Add tracking numbers to fulfilled orders | Uses woo-tracking-number-update with dry-run preview |

## Verification

Confirm the README and a representative skill resolve on the claude/woocommerce-ai-skills-0ZaZD branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/navarroido/woocommerce-skill/claude/woocommerce-ai-skills-0ZaZD/skills/merchandising/woo-category-reorganization/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/navarroido/woocommerce-skill/claude/woocommerce-ai-skills-0ZaZD/README.md | head -40
```

Both URLs return 200. After installing, review each skills/<category>/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warn verdicts noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| woo-category-reorganization | Pass | Pass | Pass |
| woo-webhook-health-check | Pass | Pass | Pass |
| woo-tracking-number-update | Pass | Pass | Warn |
| woo-shipping-cost-analysis | Pass | Pass | Warn |
| woo-seo-metadata-audit | Pass | Pass | Pass |
| woo-inventory-valuation-report | Pass | Pass | Warn |
| woo-dead-stock-identifier | Pass | Pass | Warn |
| woo-customer-note-bulk-annotator | Pass | Pass | Warn |
| woo-coupon-bulk-generator | Pass | Pass | Pass |
| woo-abandoned-cart-recovery | Pass | Pass | Warn |
| woo-wismo-bulk-status-report | Pass | Pass | Pass |
| woo-variant-attribute-normalizer | Pass | Pass | Pass |

Across the 12 sampled skills there are 30 Pass, 6 Warn, and 0 Fail cells. Six skills pass all three checks; six carry a single Snyk Warn each.

## Limitations

- Snapshot data, verified Nov 26, 2026: 1,911 combined installs across 56 indexed listings; 8 GitHub stars; MIT license; last pushed Nov 19, 2026. Counts drift over time.
- The default branch is claude/woocommerce-ai-skills-0ZaZD, not main; every raw URL in this guide uses that branch, and scripts that assume main will 404.
- The install band is flat (33 to 36 installs per listing), so the counts reflect one unit install spreading across the catalog rather than per-skill popularity.
- skills.sh sampled only 12 of the 56 indexed listings; the other 44 carry no published verdict.
- Every mutating skill defaults to dry_run on first run, but the skills still hold credentials via WC_CONSUMER_KEY and WC_CONSUMER_SECRET, so keep those scoped and secret.

## Related

[Awesome Ecommerce Skills - Commerce Index](/hermes/skills/catalog/awesome-ecommerce-skills-setup) | [Nexscope E-Commerce Skills - Shopify, Etsy, TikTok Shop & Marketplace Growth Setup](/hermes/skills/catalog/nexscope-ecommerce-skills-setup) | [WordPress Agent Skills - Audit and Optimize Setup](/hermes/skills/catalog/agent-skills-wordpress-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Let the dry-run preview run first on every mutating skill; confirm before allowing any write.
- Scope the WooCommerce REST keys to read-only or the minimum permissions the workflow needs.
- Use the read-only reporting skills (inventory valuation, tax liability, SEO audit) as a safe first pass over an unfamiliar store.
- The skills.sh counts are a flat band, so choose skills by category fit rather than install count.
- The default branch is not main; keep claude/woocommerce-ai-skills-0ZaZD in any raw fetch or CI step.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
