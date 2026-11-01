---
title: "Awesome Ecommerce Skills - Commerce Index"
description: "finsilabs/awesome-ecommerce-skills: 17.8K combined installs. 181 e-commerce skills for storefront, merchandising and marketplace work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/awesome-ecommerce-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "ecommerce", "shopify", "merchandising"]
---

# Awesome Ecommerce Skills - Setup Guide

**Source:** [finsilabs/awesome-ecommerce-skills](https://www.skills.sh/finsilabs/awesome-ecommerce-skills) via skills.sh - 17.8K combined installs across 178 indexed listings; first seen 2026-10-31 (evening sweep)

**GitHub:** [finsilabs/awesome-ecommerce-skills](https://github.com/finsilabs/awesome-ecommerce-skills) - 60 stars, MIT, branch main, last pushed 2026-10-23; 181 `SKILL.md` files under `skills/`, one per skill, nested two levels deep inside 17 category directories, with a `CATALOG.md`, `data/` JSON indexes, `tools/` maintainer scripts and a `package.json` that drives validation and catalog generation

**Category:** E-commerce operating skills for agents: storefront work, merchandising, pricing and marketplace ops

**Quality Tier:** 🟢 Green - every sampled verdict is a Pass on Gen Agent Trust Hub, Socket and Snyk, and the repository is MIT

This is a curated catalogue rather than a toolkit: 181 skills, organised into 17 categories and eight role-based bundles, covering the whole commercial surface of an online store. Each skill is a single `SKILL.md` with a `when to use` section, step-by-step instructions, best practices and a pitfalls list, and the repository's claim is that the format is what does the work: without a skill an assistant writes generic Stripe code that misses webhook signature verification and idempotency, and with one it writes the version that survives production.

The catalogue is deliberately opinionated about its own quality. Every skill was run through Tessl evaluations, where the same task is scored twice, once with the skill loaded and once without, and the README reports an average improvement from 66 to 96 across 177 skills, with the largest single gain on `win-back-reactivation` moving from 13 to 91. Those numbers are the maintainers' own runs, not an independent audit, but the harness is in the repo: 180 of the 181 skill directories carry a `tile.json` and 178 carry an `evals/` folder with a task description and machine-readable criteria.

## Installation

The README's recommended route is Tessl, which installs one skill by name into the current project:

```bash
curl -fsSL https://get.tessl.io | sh
tessl install finsi/stripe-integration
tessl install finsi/checkout-flow-optimization
```

The fallback is a manual copy, and the README is explicit that it copies a single skill file into the project's agent context folder:

```bash
git clone https://github.com/finsilabs/awesome-ecommerce-skills.git
cp -r awesome-ecommerce-skills/skills/payments-checkout/stripe-integration/SKILL.md \
  your-project/.claude/skills/
```

Neither route is written for Hermes, and the repository documents no skills CLI command, so there is no `npx skills add` line to copy here. The durable install is the same clone with a directory copy, which keeps the category structure intact and takes the packaging metadata along with the instruction:

```bash
git clone --depth 1 https://github.com/finsilabs/awesome-ecommerce-skills.git /tmp/awesome-ecommerce-skills
cp -r /tmp/awesome-ecommerce-skills/skills/. ~/.hermes/profiles/corpusiq/skills/ecommerce/
```

Install selectively. Copying all 181 skills into a working profile is a lot of context for a store that only needs checkout and inventory, and the category directories make it easy to take one vertical: `payments-checkout`, `catalog-inventory`, `marketing-growth`, `fulfillment-shipping` and `security-compliance` are the five that cover most day to day work.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| product-comparison | 301 | Side-by-side comparison tables where shoppers pick multiple products and see highlighted differences before deciding. |
| sales-reporting-dashboard | 220 | Executive dashboards for revenue, average order value, conversion rate and cohort analysis, with drill-down by date and channel. |
| product-page-design | 219 | Product detail pages with image galleries, variant selectors, social proof and calls to action that drive add to cart. |
| accounts-payable-management | 214 | Supplier invoices and vendor payments: receipt matching, payment scheduling, early discount capture and reconciliation. |
| tiktok-shop-integration | 206 | Syncing a catalogue to TikTok Shop, managing orders and inventory there, and running shoppable content with affiliate creators. |
| inventory-tracking | 187 | Real-time stock levels with reservation to prevent overselling and backorder support. |
| international-shipping | 183 | Cross-border orders: customs forms, duty and tax estimation, HS code assignment and restricted item blocking. |
| shipment-tracking | 180 | Live package tracking that aggregates carrier webhook updates and sends proactive delivery notifications. |
| ecommerce-seo | 174 | Organic search work: product page meta tags, JSON-LD structured data for Google Shopping and automated XML sitemaps. |
| vendor-management | 172 | A supplier portal for purchase orders, dropship routing, delivery tracking and vendor performance scorecards. |
| meta-ads-integration | 169 | Meta ad campaigns with Conversions API server-side tracking, dynamic product ads and catalogue sync. |
| financial-analytics-dashboard | 167 | Financial KPI dashboards with custom metrics, drill-down, variance explanations and threshold alerting. |
| marketplace-advertising | 164 | Sponsored product ads on Amazon, eBay and Walmart with bid optimisation, keyword targeting and ACOS tracking. |
| profit-margin-analysis | 162 | Gross and net margin analysis by product, category, channel and customer segment, with cost attribution and benchmarks. |
| subscription-billing | 159 | Recurring billing with dunning emails, plan proration on upgrade or downgrade, and self-serve cancellation. |
| conversion-rate-optimization | 158 | Revenue per visitor work: checkout drop-off audits, heatmap reading and CRO patterns. |
| dropshipping-integration | 149 | Supplier API connections for automatic order routing, real-time inventory sync and per-order margin calculation. |
| gift-cards | 146 | Gift card sales and redemption with secure code generation, balance tracking, partial redemption and expiry rules. |
| financial-reporting-dashboard | 146 | P&L, balance sheet and cash flow dashboards with drill-down by product, channel and period for management reporting. |
| order-management-system | 144 | Order routing to the right warehouse, split shipments and graceful backorder handling. |

The remaining 158 indexed listings range from 72 to 142 installs.

## Why This Matters for Hermes Agents

The useful thing about this pack is that it is organised by business function rather than by framework, which is how a store operator actually asks for work. A request like "our returns are eating margin" has no obvious framework, and the catalogue has `returns-management` and `returns-refund-policy` under distinct categories with `profit-margin-analysis` covering the cost side, so the agent can load the operating knowledge instead of improvising a policy.

The second reason is the pitfalls structure. Skills in this repo are written as instruction plus failure modes, and the failure modes are specific: webhook signature verification, idempotent event handling, SCA and 3D Secure on European cards, inventory reservation versus optimistic locking. Those are the details that separate a demo checkout from one that survives a chargeback, and they are exactly the details a general model omits when asked for a Stripe integration.

The catalogue is also a useful browsing surface rather than an install target. `CATALOG.md` and `data/catalog.json` list every skill with tags and eval scores, so a profile can decide which 10 of the 181 to carry instead of copying the tree and paying for all of it in context.

## Usage

| You say | What happens |
|---|---|
| "Add Stripe payments to my checkout" | The `payments-checkout` skill set writes Payment Intents with webhook signature verification, idempotent event handling and SCA handling rather than a bare card form. |
| "Shoppers are abandoning the cart at shipping" | `conversion-rate-optimization` audits the drop-off, and `international-shipping` or `free-shipping-thresholds` supplies the rate and threshold logic that fixes it. |
| "Our stock counts drift between Shopify and the warehouse" | `inventory-tracking` sets up reservation and sync, with `multi-warehouse` covering availability aggregation when there is more than one location. |
| "Which products actually make money after fees" | `profit-margin-analysis` attributes cost per order including marketplace fees, and `marketplace-fee-reconciliation` checks the settlement reports against them. |
| "Build the weekly sales dashboard" | `sales-reporting-dashboard` produces the executive view, with `financial-analytics-dashboard` for the KPI layer underneath it. |
| "We need to sell on TikTok Shop as well as our site" | `tiktok-shop-integration` syncs the catalogue and orders, and `multi-channel-selling` keeps the stock position consistent across both. |
| "Make sure the store is compliant before launch" | The `security-compliance` group covers PCI DSS scope, GDPR handling, data retention and checkout hardening. |

## Verification

The raw path for the top listing returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} product-comparison\n" \
  https://raw.githubusercontent.com/finsilabs/awesome-ecommerce-skills/main/skills/storefront-ui/product-comparison/SKILL.md
```

Expect `200`. After the clone, confirm the shape of the tree and read one skill header before copying anything:

```bash
ls /tmp/awesome-ecommerce-skills/skills | wc -l
find /tmp/awesome-ecommerce-skills/skills -name SKILL.md | wc -l
head -6 /tmp/awesome-ecommerce-skills/skills/storefront-ui/product-comparison/SKILL.md
```

The first count should print 17 categories, the second 181 skills, and the header should show `name: product-comparison`, a quoted `description:`, `category: storefront-ui` and `risk: safe`.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| product-comparison | Pass | Pass | Pass |
| email-marketing-automation | Pass | Pass | Pass |
| faceted-navigation | Pass | Pass | Pass |
| product-information-management | Pass | Pass | Pass |
| commerce-api-gateway | Pass | Pass | Pass |

The skills themselves are markdown. There is no npm package, no build step and no postinstall hook: a typical directory holds a `SKILL.md`, a `tile.json` and an `evals/` folder with a task markdown file and a criteria JSON file, with 180 of the 181 directories shipping the tile manifest and 178 shipping evals. The executable surface is confined to `tools/`, which is maintainer tooling for validation, catalogue generation and eval batches (`validate.js`, `generate-catalog.js`, `batch-run-evals.js` and friends), driven by the scripts in `package.json`. An agent does not need any of it to use a skill.

The one real risk sits in the install instructions rather than the content. The README's recommended route starts with `curl -fsSL https://get.tessl.io | sh`, which is a remote installer piped into a shell. That is standard for developer CLIs and still worth a moment: read the script, or use the manual clone and copy route, before running it on a host that holds credentials.

The repository also grades its own skills. Frontmatter carries a `risk` field, with 137 skills marked `risk: safe` and 44 marked `risk: critical`, and the critical set is concentrated where you would hope: all seven `security-compliance` skills, seven under `payments-checkout`, seven under `pricing-promotions` and four under `catalog-inventory`. Treat the critical label as guidance about which skills deserve a read before an agent follows them unattended, particularly anything touching card data, pricing rules or stock reservations.

## Limitations

- Snapshot data, verified 2026-10-31: 17,780 combined installs across 178 indexed listings; 60 GitHub stars; MIT; last pushed 2026-10-23. Counts drift over time.
- The install curve is flat, so rank carries little signal. The top 20 listings sit between 144 and 301 installs and the other 158 sit between 72 and 142, which is a few dozen installs of spread across the whole catalogue rather than a real popularity gradient.
- The index and the tree do not match one to one: the tree has 181 skill directories against 178 indexed listings, and three of them (`package-fit-optimization`, `return-fraud-prevention`, `shopify-app-review-triage`) have no listing on skills.sh. All 178 indexed listings do have a directory.
- The README's manual copy example moves a single `SKILL.md` and leaves the `tile.json` and `evals/` folder behind. That is fine for the instruction and loses the packaged metadata a validator would read.
- The eval figures (66 to 96, an average gain of 31 across 177 skills) are the maintainers' own Tessl runs and are reported, not reproduced here. They also cover 177 of the 181 skills, so the newest four are unscored.
- Breadth is the whole point and also the cost. 181 skills in one profile is a large context budget for a store that needs a handful of verticals, so install by category rather than copying the tree.

## Related

- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [Shopify Development - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/shopify-development-setup)
- [Nexscope E-Commerce Skills - Shopify, Etsy, TikTok Shop & Marketplace Growth Setup](/hermes/skills/catalog/nexscope-ecommerce-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the eight curated bundles in `data/bundles.json` rather than the full tree. They cover common needs at 15 skills, a full store build at 41, growth at 25 and migration at 30, which is a cheaper way to pick a starting set than reading 181 directories.
- Read the `risk: critical` skills before letting an agent act on them. The label is the maintainers' own and it is applied consistently to anything that touches payments, pricing rules, stock reservations or compliance.
- Use `CATALOG.md` and `data/catalog.json` for discovery and the skill directories for installation. The catalogue carries tags and eval scores, which makes it the right place to decide what a store needs, and the tree is the right place to copy from.
- Prefer the manual clone route over the Tessl installer on a host with credentials. Same content, no pipe-to-shell step, and it keeps the category layout that the copy target expects.
- When a skill's advice conflicts with the platform's current API, trust the platform. The pack is a catalogue of patterns, and the version-specific API surface for Shopify, WooCommerce or Stripe changes faster than a curated collection does.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
