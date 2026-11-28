---
title: "Ecommerce Skill Catalog - Marketplace Scraper Skills"
description: "sam6dvpte34/ecommerce-skill: 2.5K combined installs. Independent ecommerce scraper catalog for Amazon, eBay, Shopify, TikTok Shop and more."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ecommerce-skill-catalog-setup/"
robots: "index,follow"
last_updated: "2026-11-28"
tags: ["hermes skill", "agent skill", "skill setup", "ecommerce", "scraping", "marketplace"]
---

# Ecommerce Skill Catalog - Setup Guide

**Source:** [sam6dvpte34/ecommerce-skill](https://www.skills.sh/sam6dvpte34/ecommerce-skill) via skills.sh - 2.5K combined installs across 96 indexed listings; first seen Nov 28 2026 (morning sweep)

**GitHub:** [sam6dvpte34/ecommerce-skill](https://github.com/sam6dvpte34/ecommerce-skill) - 8 stars, no LICENSE file at the repo root (GitHub reports no license), branch main, last pushed 2026-09-15; 185 skill directories under `skills/<name>/SKILL.md`, each a single markdown file carrying a `license: MIT` frontmatter field, plus a README, `assets/browseract-ecommerce.png` and `docs/GITHUB_REPO_PROFILE.md`

**Category:** E-commerce scraping skills for browser-based agents: product, price, review, seller and supplier data across 49 platforms and marketplaces

**Quality Tier:** 🟠 Orange - 16 of 20 sampled listings Fail the Gen Agent Trust Hub and 7 carry a Snyk Fail; no sampled skill passes all three scanners

sam6dvpte34/ecommerce-skill is an independent skill catalog for browser-based AI agents, indexed on skills.sh. The README counts 185 reusable skills across 49 ecommerce platforms, marketplaces and cross-store workflows, covering product detail, search results, reviews, prices, sellers and supplier research on Amazon, eBay, Walmart, Etsy, Shopify, TikTok Shop, Google Shopping, AliExpress and Temu. Each skill is a single SKILL.md markdown file that the agent copies into its skill directory and runs against a live website, with the README recommending BrowserAct as the browser runtime.

The skills.sh index is far narrower than the tree: 96 indexed listings totaling 2,489 combined installs, against 185 in-tree skills, and every listing sits between 24 and 45 installs. That flat band is the shape of a broad catalog of small single-purpose scrapers rather than a suite with flagship entries, so the index is a discovery surface, not a popularity ranking.

## Installation

The README has no CLI or plugin marketplace; install is a manual directory copy. Its three steps are to pick the skill matching your target platform and task, copy `skills/<skill-name>/` into the agent's skill directory, then ask the agent to run it. For Hermes the durable install is a clone plus a single-skill copy:

```bash
git clone --depth 1 https://github.com/sam6dvpte34/ecommerce-skill.git /tmp/ecommerce-skill
cp -r /tmp/ecommerce-skill/skills/sephora-product-scraper ~/.hermes/profiles/corpusiq/skills/
```

Install selectively: the tree holds 185 skills, one SKILL.md each, and a profile only needs the scrapers for the platforms it actually targets. The README lists Hermes among the runtimes it works with (Claude Code, OpenAI Codex, Cursor, Windsurf, OpenClaw, Hermes and other local agents), and the top skill's body states it uses the BrowserAct CLI to access real browser pages and execute tasks.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| sephora-product-scraper | 45 | Collect Sephora products: title, price, specs, images, availability. |
| facebook-marketplace-search-results-scraper | 41 | Collect Facebook Marketplace search results: titles, prices, ratings, URLs and sponsored flags. |
| ecommerce-product-detail-scraper | 38 | Collect product details from any ecommerce page: title, price, specs, images, availability and seller. |
| google-shopping-price-comparison-scraper | 34 | Compare Google Shopping prices across sellers: prices, merchants, shipping and availability. |
| alibaba-listings-scraper | 32 | Collect Alibaba listings: title, price, condition, seller and URL. |
| ecommerce-competitor-assortment-monitor | 29 | Monitor competitor assortments: catalog titles, prices and category coverage. |
| vinted-marketplace-scraper | 29 | Collect Vinted marketplace listings: item title, price, condition, seller and category. |
| aliexpress-search-results-scraper | 29 | Collect AliExpress search results: titles, prices, ratings, URLs and sponsored flags. |
| aliexpress-review-scraper | 29 | Collect AliExpress reviews: text, rating, author, date and verified status. |
| alibaba-supplier-profile-scraper | 29 | Collect Alibaba supplier profiles: name, certifications, products, MOQ and location. |
| alibaba-product-detail-scraper | 29 | Collect Alibaba product details: title, price, specs, images, availability and seller. |
| aliexpress-product-scraper | 28 | Collect AliExpress products: title, price, specs, images and availability. |
| temu-search-results-scraper | 27 | Collect Temu search results: titles, prices, ratings, URLs and sponsored flags. |
| mercadolibre-deals-scraper | 27 | Collect MercadoLibre deals: deal title, discount, original price and merchant. |
| lazada-product-scraper | 27 | Collect Lazada products: title, price, specs, images and availability. |
| etsy-trending-products-scraper | 27 | Collect trending Etsy products: titles, trending signals and category. |
| ebay-sold-listings-scraper | 27 | Collect eBay sold listings: title, final price, sold date, condition and seller. |
| allegro-search-results-scraper | 27 | Collect Allegro search results: titles, prices, ratings, URLs and sponsored flags. |
| alibaba-supplier-lead-research | 27 | Collect Alibaba supplier leads: name, products, MOQ and contact signals. |
| 1688-price-moq-scraper | 27 | Collect 1688 price and MOQ data: unit price, MOQ, supplier and payment terms. |

The remaining 76 indexed listings range from 24 to 26 installs.

The 20 rows above are the most-installed listings and are also the 20 that skills.sh sampled for security verdicts. The full catalog spans 185 in-tree skills, of which skills.sh indexes 96.

## Why This Matters for Hermes Agents

This is a reference catalog for organizing a large number of single-purpose scraping skills. Each skill is one SKILL.md with a name, a description and a `Use when` trigger, which is the same portable format a Hermes profile consumes directly. The catalog's naming convention (platform, object, then scraper) and the README's Coverage table, which maps every platform to its skills, are what make 185 skills navigable without reading each one.

The skill descriptions are also a working template for Hermes skill authors: they state the exact fields collected (title, price, rating, URL) and the trigger condition (`Use when the user wants to...`), which is precisely the shape of a well-written Hermes skill description.

The security read is the cautionary part: a repository of nothing but markdown still produces 16 of 20 Gen Agent Trust Hub Fails in the sample, a useful calibration that instruction-only skills carry scanner-flagged risk. A builder wiring these into an agent should treat them as prompts to review against each site's terms rather than a plug-and-play suite.

## Usage

| You say | What happens |
|---|---|
| "Compare sourcing costs and MOQ requirements on 1688" | Uses 1688-price-moq-scraper to collect unit price, MOQ, supplier and payment terms. |
| "Collect Alibaba product listings for a keyword" | Uses alibaba-listings-scraper to collect title, price, condition, seller and URL. |
| "Collect AliExpress reviews for sentiment analysis" | Uses aliexpress-review-scraper to collect text, rating, author, date and verified status. |
| "What are these eBay items actually selling for" | Uses ebay-sold-listings-scraper to collect final price, sold date, condition and seller from sold data. |
| "Compare prices for this product across sellers" | Uses google-shopping-price-comparison-scraper to collect prices, merchants, shipping and availability. |
| "Track what my competitors carry and how they price" | Uses ecommerce-competitor-assortment-monitor to monitor catalog titles, prices and category coverage. |
| "Collect product details from any ecommerce page" | Uses ecommerce-product-detail-scraper to collect title, price, specs, images, availability and seller without targeting one platform. |

## Verification

The raw path below returned HTTP 200 on branch main on 2026-11-28:

```bash
curl -sL https://raw.githubusercontent.com/sam6dvpte34/ecommerce-skill/main/skills/sephora-product-scraper/SKILL.md
```

After a clone, confirm the tree shape and read one skill header before copying anything:

```bash
git clone --depth 1 https://github.com/sam6dvpte34/ecommerce-skill.git /tmp/ecommerce-skill
ls /tmp/ecommerce-skill/skills | wc -l
head -6 /tmp/ecommerce-skill/skills/sephora-product-scraper/SKILL.md
```

The first command should print 185 (skill directories), and head should show the sephora frontmatter with `name: sephora-product-scraper`, a quoted `description:`, `license: MIT` and `metadata:`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sephora-product-scraper | Fail | Warn | Warn |
| facebook-marketplace-search-results-scraper | Fail | Pass | Fail |
| ecommerce-product-detail-scraper | Fail | Pass | Warn |
| google-shopping-price-comparison-scraper | Fail | Warn | Warn |
| alibaba-listings-scraper | Fail | Warn | Warn |
| ecommerce-competitor-assortment-monitor | Fail | Pass | Warn |
| vinted-marketplace-scraper | Fail | Warn | Warn |
| aliexpress-search-results-scraper | Fail | Pass | Warn |
| aliexpress-review-scraper | Fail | Pass | Fail |
| alibaba-supplier-profile-scraper | Fail | Pass | Fail |
| alibaba-product-detail-scraper | Warn | Pass | Warn |
| aliexpress-product-scraper | Fail | Pass | Warn |
| temu-search-results-scraper | Warn | Warn | Fail |
| mercadolibre-deals-scraper | Warn | Warn | Warn |
| lazada-product-scraper | Fail | Pass | Fail |
| etsy-trending-products-scraper | Warn | Pass | Warn |
| ebay-sold-listings-scraper | Fail | Pass | Warn |
| allegro-search-results-scraper | Fail | Pass | Fail |
| alibaba-supplier-lead-research | Fail | Warn | Fail |
| 1688-price-moq-scraper | Fail | Warn | Warn |

This guide is Orange because 16 of the 20 sampled listings Fail the Gen Agent Trust Hub and 7 carry a Snyk Fail; no sampled skill passes all three scanners. Socket is the quietest column with 12 Pass and 8 Warn and no Fails. The repository's executable surface is markdown only: every skill is a single SKILL.md with no bundled scripts, so the flags sit on instruction content rather than shipped code, and the README's own Notes warn against keeping cookies, account details and exported records in shared folders. Only 20 of the 96 indexed listings were sampled; the other 76 have no published verdicts in this snapshot.

## Limitations

- Snapshot data, verified 2026-11-28: 2,489 combined installs across 96 indexed listings; 8 GitHub stars; no LICENSE file; last pushed 2026-09-15. Counts drift over time.
- No LICENSE file at the repo root and GitHub reports no license, so the repository as a whole carries no stated terms even though each SKILL.md sets `license: MIT` in its frontmatter. Confirm per-file before redistributing.
- The install index covers less than the tree: 96 indexed listings against 185 in-tree skills, and the band is flat at 24 to 45 installs, so install count carries little signal about which scraper is maintained or reliable.
- The README's example requests use loose names that do not all match the tree (amazon-product-scraper versus amazon-product-detail-scraper, shopify-product-scraper versus shopify-products-scraper); copy the exact directory name from `skills/`.
- Security verdicts cover 20 of the 96 indexed listings; the other 76 have no published verdicts.
- The scrapers target live websites, and the README notes availability, visible fields, login requirements and result limits change over time, and that they are intended for public data or data you are authorized to access.

## Related

- [Awesome Ecommerce Skills - Commerce Index](/hermes/skills/catalog/awesome-ecommerce-skills-setup)
- [Nexscope E-Commerce Skills - Shopify, Etsy, TikTok Shop & Marketplace Growth Setup](/hermes/skills/catalog/nexscope-ecommerce-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy single skills by directory rather than the whole tree; 185 scrapers is far more context than any one store needs, and the per-platform directories make selective install easy.
- Read a SKILL.md before running it. Each is one markdown file with a name, description and trigger, and the instructions define exactly what the agent scrapes.
- Re-check the skills.sh security pages before production use: 16 of 20 sampled listings Fail the Gen Agent Trust Hub, so treat the suite as prompts to review, not a trusted dependency.
- Use the README's Coverage table to pick skills by platform, then copy the exact directory name from `skills/`, since a few README examples use loose names that differ from the tree.
- The skills are templates for BrowserAct or any browser-capable runtime, and nothing in the repository executes on install, so the risk is in what the agent scrapes and where the results go, not in a build step.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
