---
title: "Apify Awesome Skills - Lead and Market Intelligence"
description: "apify/awesome-skills: 4.2K combined installs across 39 listings for scraping, lead generation, ad intelligence and AI search visibility"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/apify-awesome-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-11"
tags: ["hermes skill", "agent skill", "skill setup", "apify", "scraping", "lead generation", "market research"]
---

# Apify Awesome Skills - Setup Guide

**Source:** [apify/awesome-skills](https://www.skills.sh/apify/awesome-skills) via skills.sh - 4.2K combined installs across 39 indexed listings; first seen Mar 12, 2026 (Nov 11, 2026 sweep)
**GitHub:** 294 stars, Apache-2.0 license, `main` branch, last pushed 2026-11-06, 173 tracked files with 30 `SKILL.md` files under `skills/`, one of which is a template
**Category:** Market and lead intelligence: e-commerce data, lead enrichment, ad research, AI search visibility, jobs, OSINT, app store data
**Quality Tier:** 🟡 Established - Apache-2.0, a first-party vendor pack and an active release cadence, held back by a Snyk Fail on the AI visibility skill and a Warn on the flagship.

This repository is a different set of Apify skills from the platform documentation pack. Where `apify/agent-skills` teaches an agent to build and run Actors, this one packages business processes that happen to be implemented with Actors: find e-commerce prices, build a verified email list, research competitors' ads, measure whether a brand appears in AI answers.

Each `SKILL.md` is a routing document. It names the specific Actor that does the work, the inputs that Actor takes, and the sequence to chain two of them when one output feeds the next. That chain pattern is the reason the pack is worth its size: competitor pricing is one scraping step, but a comparison across thirty platforms is input construction, pagination, deduplication and a table.

The subject matter is unusually close to operator work rather than developer work. E-commerce pricing and bestsellers, verified business emails from maps and search, lead scoring from a CSV, buying-signal detection across job posts and funding announcements, advertising research across Meta, Google and TikTok, and local business lists from OpenStreetMap instead of Google Maps.

Two skills show where the pack is heading. `apify-ai-search-visibility-tracker` measures whether a brand is cited in Google AI Overviews, Google AI Mode, ChatGPT Search and Perplexity, which is the same question many SEO teams are building bespoke tooling for. `apify-x402-agentic-wallet` discovers and pays for Actors in USDC on Base, an agent-to-agent payment path rather than a subscription.

## Installation

The README's route is the skills CLI, with a listing flag and a single-skill flag that matter for a pack this size:

```bash
npx skills add apify/awesome-skills
npx skills add apify/awesome-skills --list
npx skills add apify/awesome-skills -s apify-ecommerce
```

Installing all 39 at once is possible and usually wrong. Each skill in this pack describes an Apify Actor that costs money to run, and the agent activates a skill by matching the request, so a full install gives you 39 ways to start spending. Install the four or five that match your work.

The pack also has an MCP path: several skills are written to call Actors through Apify's MCP server at runtime, and `apify-product-data-setup` exists specifically to wire an agent to live product data either as tool calls or as a saved dataset. Whichever route you take, the account and the API token are yours.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| apify-ecommerce | 529 | Scrapes pricing, reviews, bestsellers and seller data across 30+ marketplaces including Amazon, Walmart and eBay. |
| apify-easy-competitive-intelligence | 339 | Builds a competitor comparison covering pricing, positioning and market landscape from public sources. |
| apify-verified-email-finder | 292 | Builds a verified business email list from Google Maps, search results or a URL list, with verification inside the run. |
| apify-ads-intelligence | 262 | Researches and compares ads across Meta, Google Ads Transparency and TikTok. |
| apify-link-prospecting-outreach | 224 | Finds sites ranking for target keywords, scores them by authority and traffic, and identifies the right contact. |
| apify-ai-search-visibility-tracker | 199 | Tracks whether a brand or competitor is cited across AI Overviews, AI Mode, ChatGPT Search and Perplexity. |
| apify-influencer-brand-collabs | 191 | Maps Instagram brand and creator partnerships by chaining Actors. |
| apify-lead-generation | 181 | General lead generation across search, maps and directory sources. |
| apify-financial-news | 138 | Collects financial news and announcements for a company or sector. |
| apify-financial-osint | 123 | Open-source financial research across filings, registries and public records. |
| apify-trend-analysis | 118 | Measures what is rising in a category across search and social surfaces. |
| apify-public-registries | 112 | Pulls structured records from public registries. |
| apify-market-research | 112 | Assembles a market picture from scraped pricing, listings and review data. |
| apify-booking-host-leads | 100 | Finds and enriches Booking.com host and property-manager leads. |

The remaining 25 indexed listings range from 4 to 99 installs. They cover job boards, Reddit, app store intelligence, Yandex search and image search, travel planning, Clutch agency data, Instagram niche mapping and Actor development, and each is a documented skill with its own folder in the tree.

The index carries 39 listings against 30 `SKILL.md` files in the tree, one of which is `_template`. The gap is real: a handful of listings name skills that have no same-named folder in the current checkout.

## Why This Matters for Hermes Agents

The distance between "scrape a site" and "answer a business question" is mostly plumbing, and plumbing is what agents do reliably once it is described. This pack supplies the descriptions: which Actor, which input fields, what the output keys are, and how to chain two runs when the second depends on the first.

That matters more than it sounds. A generic agent told to "compare prices across Amazon and Walmart" will write a scraper and fail at the first anti-bot response. The skill routes to an Actor that already handles the blocking, and the agent's job becomes input construction and result shaping.

The lead-generation skills are the ones with a direct commercial use. Verified emails from maps and search, enriched and scored, is a workflow most agencies bill for. The pack does not make it free, because the Actors have a cost per run, but it makes it reproducible.

The AI visibility skill deserves a specific mention for anyone doing search work. Measuring citations across four AI answer surfaces is the question that replaced rank tracking for a lot of teams, and having an Actor-backed skill for it is different from asking a model to guess.

## Usage

| You say | What happens |
|---|---|
| "Compare prices for these five products on Amazon and Walmart" | Routes to `apify-ecommerce`, builds inputs per marketplace, runs the Actors and returns one deduplicated table. |
| "Find 50 verified emails for marketing agencies in Austin" | Builds a maps or search query, runs the email finder and returns only verified addresses. |
| "What ads is this competitor running on Meta and TikTok?" | Uses `apify-ads-intelligence` and summarises creative themes across both surfaces. |
| "Are we cited in ChatGPT when someone asks about our category?" | Runs the AI visibility tracker across the four surfaces and reports which queries cite the brand. |
| "Score this CSV of leads against our ICP" | Uses `apify-lead-scoring-enrichment` to score and enrich the file in one pass. |
| "Find sites linking-adjacent to us that rank for our keywords" | Uses `apify-link-prospecting-outreach` and returns prospects with authority and contact. |
| "Why did this scrape come back empty?" | Applies `apify-blocked-scrape-triage`, which diagnoses blocking and throttling in cost order before re-running. |

## Verification

The skills live under `skills/` in the repository. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/apify/awesome-skills/main/skills/apify-ecommerce/SKILL.md | head -6
```

Before installing the whole pack, list what is in it and check the count against the tree:

```bash
npx skills add apify/awesome-skills --list
```

A skills directory holding 39 folders is expected if you installed everything. If you meant to install a subset, confirm each folder's `SKILL.md` names the Actor it uses before granting the agent a run.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-11) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| apify-ecommerce | Pass | Pass | Warn |
| apify-ai-search-visibility-tracker | Warn | Pass | Fail |

One sampled skill carries a Snyk Fail, and the other draws a Warn. The shape of the risk is consistent across the pack: these skills instruct an agent to send requests through a paid API using your token, and the Fail is attached to the skill that queries third-party AI surfaces. Whether that is acceptable depends on the account and the spend you are willing to authorize.

Three controls are worth stating. Give the agent an Apify token scoped to the work rather than an account-level token. Set a spend limit on the account before the first run, because a chain of Actors can run more times than expected while an agent iterates. And treat scraped personal data as personal data: verified emails and phone numbers carry obligations that differ by jurisdiction, and neither the skill nor the scanner will slow you down.

## Limitations

- Snapshot data, verified 2026-11-11: 4,199 combined installs across 39 indexed listings; 294 GitHub stars; Apache-2.0; last pushed 2026-11-06. Counts drift over time.
- 39 indexed listings against 30 `SKILL.md` files, one of which is a template. Several listings have no same-named folder in the current tree.
- Every skill spends money. The Actors are billed per run or per result, and the skill descriptions do not carry prices, so cost has to be checked in the Apify console.
- Some skills require further credentials beyond the Apify token: the email finder and the link prospecting skill depend on verification and authority providers that are configured per Actor.
- The pack overlaps with `apify/agent-skills` and with the older Apify growth guides in this catalog. Installing several Apify packs gives the agent redundant routes to the same Actors.
- Scraped personal data carries legal obligations that vary by jurisdiction. The skills are indifferent to that, and so is the tooling.
- One sampled skill carries a Snyk Fail and its companion a Warn.

## Related

- [Apify Agent Skills - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/apify-agent-skills-setup)
- [Apify Growth Skills - Lead Gen and Brand Monitoring](/hermes/skills/catalog/apify-growth-skills-setup)
- [Apify Ultimate Scraper](/hermes/skills/catalog/apify-ultimate-scraper-setup)

## Pro Tips

- Install by name. `-s apify-ecommerce` gives one skill and one spend surface; the full pack gives 39.
- Set an account spend limit first. An agent iterating on a scrape can run the same Actor many times before you see the invoice.
- Ask for the input before the run. Reviewing the Actor input takes a second and catches the wrong market, the wrong locale or a pagination loop.
- Use the triage skill before re-running a failure. `apify-blocked-scrape-triage` is written to stop an agent from repeating a blocked request at higher cost.
- Keep the output as a dataset, not a chat message. Every Actor run produces a dataset you can re-read, and re-running for the same data is the most common waste.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
