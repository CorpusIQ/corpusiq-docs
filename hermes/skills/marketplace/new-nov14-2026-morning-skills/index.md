---
title: "New Skills - November 14, 2026 Morning"
description: "Skills.sh sweep (Nov 14 morning): 14 publisher guides for 293,560 combined installs across 293 indexed listings, plus the Obsidian rename reconcile"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov14-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 14, 2026 Morning Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. This fire ended a long silence on the standing board: the 20-query window returned 883 unique skills with 113 NEW and 300 PARTIAL rows, and its top NEW row sits at 5,677 installs (`cyxzdev/uncodixfy`), the first time in fifty-two fires that anything in that window cleared the 1,000-install trigger. That row became a guide in this batch.

The topic probe widened again rather than touching the floor. 328 fresh lanes ran on top of the 20 standing queries at 2.7-second pacing through `curl`: 348 queries in total, 17,563 rows, 3,616 distinct sources, zero failed queries. After cross-referencing against the docs tree, 2,376 sources read as uncovered, with 120 above 3,000 combined installs, 185 above 2,000 and 365 above 1,000.

The queue carried the three candidates the previous fire left sized, plus twenty-three fresh finds. Every candidate went through the exact-source filter before drafting, because the probe ranks a wide publisher far below its true size.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 883 (0 failed queries) |
| NEW (standing window) | 113 rows |
| PARTIAL (standing window) | 300 |
| Top NEW row in the standing window | 5,677 (`cyxzdev/uncodixfy`) - first above-trigger row in 52 fires |
| Fresh topic probe | 328 additional lanes, 348 queries total |
| Probe rows / distinct sources / failed queries | 17,563 / 3,616 / 0 |
| Uncovered sources after cross-reference | 2,376 |
| Uncovered above 3,000 combined | 120 |
| Uncovered above 2,000 combined | 185 |
| Uncovered above 1,000 combined | 365 |
| Single-pattern confirmed uncovered (800 and above) | 409 |
| Candidates sized from source | 29 |
| Guides published this fire | 14 |
| Guides reconciled this fire | 1 (Obsidian rename) |
| Combined installs documented (new guides) | 293,560 |
| Indexed listings covered (new guides) | 293 |
| Tier mix | 4 Green, 7 Yellow, 3 Orange |

## Published guides

| Guide | Source | Combined | Listings | Tier |
|---|---|--:|--:|---|
| Reverse Skill - Security Research Router Pack | zhaoxuya520/reverse-skill | 65,070 | 88 | Orange |
| Plannotator - Plan and Review Workspace Setup | backnotprop/plannotator | 44,929 | 12 | Yellow |
| AnySearch - Real-Time Search Engine Skill | anysearch-ai/anysearch-skill | 38,665 | 1 | Yellow |
| Arcmira MCP - YouTube Research for Agents | arcmira/mcp | 33,811 | 11 | Yellow |
| Umbraco Backoffice Skills - CMS Extension Setup | umbraco/umbraco-cms-backoffice-skills | 31,007 | 78 | Yellow |
| App Store Screenshots - Store Assets Skill | parthjadhav/app-store-screenshots | 16,069 | 1 | Green |
| Blender Agent Skills - 3D Production Workflows | el4cteo/blender-skills | 12,176 | 28 | Green |
| Dagster Skills - Data Orchestration Setup | dagster-io/skills | 11,064 | 7 | Yellow |
| NetSuite SuiteCloud - ERP Development Skills | oracle/netsuite-suitecloud-sdk | 8,165 | 11 | Orange |
| Magento 2 Agent Skills - Adobe Commerce Suite | maxnorm/magento2-agent-skills | 7,538 | 30 | Green |
| Scrapling - Web Scraping Framework Skill | d4vinci/scrapling | 6,733 | 1 | Yellow |
| Bootstrap Agent Skills - Framework Guidance | twbs/bootstrap | 6,467 | 12 | Green |
| WooCommerce Agent Skills - Store Development | woocommerce/woocommerce | 6,189 | 12 | Yellow |
| Uncodixfy - Anti AI UI Pattern Skill | cyxzdev/uncodixfy | 5,677 | 1 | Orange |

## Reconciled, not republished

`obsidianmd/obsidian-skills` is the same project the catalog already documented as `kepano/obsidian-skills`. GitHub reports the old path as moved, and the skills.sh listings, star count and install totals all live under the new owner now: 428,048 combined installs across 7 listings, against roughly 44K in the earlier snapshot. The existing page was repointed instead of duplicated, and `kepano/obsidian-skills` was added to the published rename map so a later sweep cannot publish a second page for the same project.

## Held, with the reason measured

- **whytryharder/superpowers** (43 listings, 43,179): the repository carries no description, no licence and zero stars while publishing 43 listings, so its identity cannot be confirmed from the repo alone. Held until it can.
- **gargantuax/openskills** (2 listings, 27,420): the GitHub repository returns 404 and there is no tree to verify against.
- **C3SC0-V4113/Scaffold** (5 listings, 20,781): four of five listings sit within 8 installs of each other at roughly 5,195, on a three-star repository with no description. The pattern reads as an aggregate rather than five independent skills.
- **dmmulroy/anti-slop** (1 listing, 16,123): a real repository with 6,072 stars, but the catalog already publishes a guide titled Anti-Slop for a different publisher. Held to avoid two pages competing for one query.
- **twostraws/swiftdata-agent-skill** (9,788), **kunchenguid/gh-axi** (9,803), **homeassistant-ai/skills** (9,282), **diffusionstudio/lottie** (11,470): single-skill finds, all quoted for the next fire.
- **daniel-dan-conrad/ui-designer-skill** (3,659) and **gogf/skills** (3,351): zero and 83 stars respectively with no licence, and the first publishes no repository metadata. Held pending an identity check.
- **wechatpay-apiv3/wechatpay-skills** (7 listings, 6,011): six of the seven indexed names have no matching `SKILL.md` in the tree, so the listing set cannot be grounded.
- **frappe/skills** (14 listings, 7,330) and **laravel/boost** (7 listings, 4,608): no licence file, three ungrounded names, and an MCP server rather than a pure skill set. Queued for a domain pass.
- **CDN and product domains** (`senclaw-cdn.italent.cn`, `apifox.com`, `developer.paddle.com`, `arkdocs.tos-cn-beijing.volces.com`, `evlog.dev`, `kie.ai`): no repository behind them, so there is nothing to verify.

## New pitfalls found this fire

- **The probe row and the exact-source total can disagree by an order of magnitude in the other direction too.** `whytryharder/superpowers` served a single probe row at 1,569,722 installs, and the exact-source filter returned 43,179 across 43 listings. Three fires of notes have warned that the probe undercounts wide publishers; this is the mirror case, where one aggregated row would have made an unverifiable repository the headline. Size from the exact-source filter, and sanity-check the top row against it before ranking.
- **A rename inside skills.sh does not move the source page.** `skills.sh/kepano/obsidian-skills` still returns 200 while the repository has moved to `obsidianmd`, so the old URL is not a signal that the old page is current. Compare the GitHub identity, not the skills.sh status code.
- **The standing window can fire too.** Fifty-one consecutive fires reported nothing above 350 installs in the standing window; this one returned a 5,677 row because the window carries the generic lanes. A silent window is a measurement, not a guarantee.

## Live verification

Deploy ran after the push to main. Every new guide page returns 200 with its own title on `docs.corpusiq.io` and through the `www.corpusiq.io/docs` proxy, the batch page returns 200 on both hosts, the catalog index renders the new sweep heading with all 14 links, the marketplace index carries the updated stamp and links this page, and the new URLs appear in `sitemap.xml`.

## Integration

Fourteen guides into `hermes/skills/catalog/`, one `### New - November 14, 2026 Morning Sweep (14 publisher guides)` block appended to `catalog/index.md`, the Obsidian page repointed to the current publisher with `kepano/obsidian-skills` added to `scripts/catalog_source_aliases.json`, this batch page, a Recent Sweeps entry at the top of `marketplace/index.md`, and PROGRESS counts resynced from the staged tree.

## Next-fire note

Sized and ready: `twostraws/swiftdata-agent-skill` (9,788 / 1), `kunchenguid/gh-axi` (9,803 / 1), `homeassistant-ai/skills` (9,282 / 1) and `diffusionstudio/lottie` (11,470 / 1). Needing an identity check first: `whytryharder/superpowers`, `gargantuax/openskills`, `C3SC0-V4113/Scaffold`, `daniel-dan-conrad/ui-designer-skill`. Needing a domain pass: `vasilyu1983/ai-agents-public`, `alterlab-ieu/alterlab-academic-skills`, `mohitagw15856/pm-claude-skills`, `frappe/skills`. The 409 single-pattern-confirmed uncovered sources live in the sweep cache; keep the 348-query lane list and widen it again, since query width has now restored the band three fires running.
