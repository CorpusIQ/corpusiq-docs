---
title: "LinkFox Skills - IP, Legal and Trade Data Setup"
description: "linkfox-ai/linkfox-skills: 58.4K combined installs. 270 API-backed skills for Amazon, Ozon, Temu and 1688 data, plus patent and trademark checks."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/linkfox-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "cross border ecommerce", "amazon data", "patent search", "ozon"]
---

# LinkFox Skills - Setup Guide

**Source:** [linkfox-ai/linkfox-skills](https://www.skills.sh/linkfox-ai/linkfox-skills) via skills.sh - 58.4K combined installs across 200 indexed listings; first seen 2026-10-30 (evening sweep)

**GitHub:** [linkfox-ai/linkfox-skills](https://github.com/linkfox-ai/linkfox-skills) - 115 stars, MIT License, branch main, last pushed 2026-10-29; 270 `SKILL.md` files, one per skill, each under `skills/<skill-name>/` with its own `references/` directory and, in 242 cases, a `scripts/` directory of Python; no root-level manifest of any kind

**Category:** Cross-border e-commerce market data, IP and compliance research

**Quality Tier:** 🟡 Yellow - Gen Agent Trust Hub passes all five sampled skills and the repository is MIT, but every sample carries a Snyk Warn and nothing runs without a paid LinkFox API key

LinkFox publishes this suite for cross-border sellers, and its scope is unusual for a single repository: 270 skill directories in the tree at main, covering Amazon storefront search and detail, Amazon Ads reporting and campaign management, Ozon through MPSTATS, Temu order and fulfillment operations, 1688 sourcing and wholesale billboards, Shopee store management, Walmart, eBay, Etsy, TikTok Shop through EchoTik and FastMoss, and a patent and trademark layer through Zhihuiya, Eureka and Ruiguan.

The shape is uniform across all 270 skills. Each directory holds a Chinese `SKILL.md` with English trigger keywords appended to the description (all 270 descriptions carry Chinese), an `api.md` under `references/` describing the endpoint schema where one exists (228 of the 270), an onboarding reference for auth and billing failures, and for most skills a `scripts/` directory of Python that calls a LinkFox gateway with the account key. That consistency is what makes a 270-skill suite usable at all: an agent that can run one `scripts/<name>.py` with a JSON argument can run the rest of its family.

## Installation

The README needs Node.js for `npx` and nothing else. Installing without `--skill` pulls the whole suite rather than one tool:

```bash
npx skills add linkfox-ai/linkfox-skills
```

Selective installs are the realistic route, because each skill brings its own scripts and reference files:

```bash
npx skills add linkfox-ai/linkfox-skills --skill linkfox-amazon-search linkfox-keepa-product-search
```

List what the CLI will actually offer before committing, since the README badge says 166 skills, the tree at main holds 270 `SKILL.md` files and skills.sh indexes 200 listings:

```bash
npx skills add linkfox-ai/linkfox-skills --list
```

Target a specific agent harness:

```bash
npx skills add linkfox-ai/linkfox-skills --agent claude-code
npx skills add linkfox-ai/linkfox-skills --agent cursor
```

Every skill is dead without an account key. The README documents one variable name, and the scripts accept either that one or the newer variant:

```bash
export LINKFOXAGENT_API_KEY=your-key-here
export LINKFOX_AGENT_API_KEY=your-key-here
```

Keys come from the LinkFoxAgent setup guide at `https://skill.linkfox.com/linkfoxskills/guide.htm`, or from the account console at `https://agent.linkfox.com/`. Requirements are Python 3.x and standard library only, and that matches the code closely: the data scripts import `urllib` and nothing outside the stdlib, and `requests` appears only in `scripts/onboarding.py`, which sets it to `None` when absent and fails only on the login path that needs it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| linkfox-multimodal-recognize-image | 1,190 | Recognizing and describing image content from a URL, including OCR and visual question answering over product photos. |
| linkfox-amazon-search | 472 | Simulating a live Amazon storefront keyword search and returning ranked SERP rows with prices, ratings, review counts and sponsored flags. |
| linkfox-dld-product-search | 457 | Searching 1688 wholesale listings for suppliers, tiered pricing and 7-day and 30-day sales when sourcing. |
| linkfox-mpstats-ozon-product-search | 449 | Looking up Ozon Russia products by Russian keyword or SKU to get the identity card that every Ozon drill-down starts from. |
| linkfox-amazon-product-detail | 446 | Pulling a full Amazon product page by ASIN: bullets, specs, A+ content, price, rating distribution and variants. |
| linkfox-sellersprite-product-search | 435 | Screening Amazon products on price, monthly sales, BSR, margin, rating and fulfillment filters across ten marketplaces. |
| linkfox-mpstats-ozon-category-products | 427 | Drilling into every Ozon SKU under a full Russian category path to find category bestsellers and niche gaps. |
| linkfox-fastmoss-product-search | 426 | Searching TikTok Shop products with GMV, commission rate, creator promotion and multi-period sales filters. |
| linkfox-mpstats-ozon-product-detail | 423 | Fetching one Ozon SKU's full card: price, Ozon Card price, stock, monthly sales, lost profit and first listing date. |
| linkfox-dld-product-billboard | 416 | Reading the 1688 weekly and monthly bestseller boards to spot trending wholesale items and suppliers. |
| linkfox-mpstats-ozon-product-trend | 415 | Charting one Ozon SKU's daily sales, price, stock and rating series to test seasonality or spot an anomaly. |
| linkfox-mpstats-ozon-seller-products | 414 | Auditing everything a single Ozon seller ID sells, for store structure work and competitor shop benchmarks. |
| linkfox-amazon-ads-report | 414 | Requesting, polling, downloading and unpacking Amazon Ads SP, SB and SD reports inside one script run. |
| linkfox-sellersprite-traffic-keyword | 412 | Reverse-looking up the keywords that send traffic to an Amazon ASIN, with organic and ad placement split. |
| linkfox-sellersprite-market-research | 411 | Ranking Amazon category markets on size, concentration, seller mix and new-product share before entering one. |
| linkfox-walmart-search | 410 | Searching Walmart listings by keyword, category and price range with live pricing and availability. |
| linkfox-amazon-search-by-image | 410 | Reverse image search across eight Amazon marketplaces to find lookalikes, sourcing alternatives or counterfeits. |
| linkfox-product-title-analyze | 409 | Tokenizing product titles already pulled in the session to surface scene, audience, material and color words. |
| linkfox-multimodal-extract-attributes | 409 | Extracting color, shape, style and material attributes plus image prompts from product main images in bulk. |
| linkfox-ebay-search | 407 | Searching eBay regional sites for pricing, sold listings, auctions and seller location comparisons. |

The remaining 180 indexed listings range from 150 to 406 installs.

The tail is not filler. It holds the Temu operations family (orders, fulfillment, returns, ads and pricing per region), the Shopee store endpoints, the Zhihuiya and Eureka patent chains (family, claims, legal status, translated abstracts, PDF data) and the AIGC image and video generators, so a buyer who filters this suite down to the twenty most-installed skills loses most of the IP and marketplace operations coverage.

## Why This Matters for Hermes Agents

Cross-border research is normally a scraping problem before it is an analysis problem. Amazon needs one approach, Ozon another, Temu's seller API a third, 1688 a fourth, and each one breaks on its own schedule. This suite collapses that into a single keyed gateway, so the agent's job becomes choosing the right tool and shaping the filters rather than maintaining five scrapers.

The chaining is explicit in the skill text, which matters more than raw coverage. `linkfox-mpstats-ozon-product-search` returns an intentionally narrow identity card and tells the agent to continue into `mpstats-ozon-product-detail` or a category, brand or seller drill-down for the 36-field version. `linkfox-product-title-analyze` reads products already retrieved in the current conversation rather than asking for them again. An agent that follows those handoffs spends fewer tokens and fewer credits than one that re-queries from scratch.

The patent and trademark layer is the unusual part for a commerce suite. Zhihuiya and Eureka skills cover patent families, claims, legal status, translated abstracts and image search, and Ruiguan adds trademark and copyright detection plus design and utility patent screening. That is the check a seller should run before a sourcing decision rather than after a takedown notice, and it is the reason this guide's title leads with IP.

Two operational details shape how a Hermes profile should run these. The scripts that follow the shared template write the full response to `./linkfox/<date>/<session>/data/` under the working directory and print a summary when the body runs past 8 KB, so an agent can page through stored JSON instead of holding a 40-field product card in context (read the docstring at the top of a given script, since the template is common but not universal). And calls cost credits, with several skills instructing the agent to confirm the added cost before looping over multiple SKUs, which is the right default for a profile that runs unattended.

## Usage

| You say | What happens |
|---|---|
| "Find me 1688 suppliers for this phone stand and what they charge in bulk" | The agent runs `dld-product-search`, then `dld-product-billboard` for the trending view, and comes back with suppliers, tier pricing and 7-day and 30-day sales. |
| "Which keywords actually send traffic to this Amazon ASIN?" | `sellersprite-traffic-keyword` returns the traffic keyword list split by organic and ad placement and flagged by conversion type. |
| "Is this Ozon product seasonal or is it dying?" | `mpstats-ozon-product-trend` returns a daily series where `hasData=false` distinguishes a missing observation from a real zero. |
| "Pull last month's Sponsored Products search term report" | `amazon-ads-report` checks that `amazon-ads-auth` is installed, creates the report, polls for 2 to 10 minutes, downloads and unpacks it. |
| "Is this design already patented, and is the brand name free?" | The agent routes to the Zhihuiya or Eureka patent skills for family and legal status, and to Ruiguan for trademark and design screening. |
| "What do the same products cost on Walmart and eBay?" | `walmart-search` and `ebay-search` return live listings with pricing, seller location and sold-item data for the comparison. |
| "Analyze these product photos before I rewrite the listing" | `multimodal-extract-attributes` extracts color, shape, style and material attributes for every image, then `product-title-analyze` tokenizes the titles. |

## Verification

The raw path below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/linkfox-ai/linkfox-skills/main/skills/linkfox-multimodal-recognize-image/SKILL.md
```

Expect `200`. Read it before installing: the frontmatter is a Chinese description with English trigger keywords appended, the body is short, and the real detail sits in `references/api.md` and in the scripts.

After the install, confirm what landed and that the key is visible to the scripts:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -c linkfox
head -3 ~/.hermes/profiles/corpusiq/skills/linkfox-amazon-search/SKILL.md
test -n "$LINKFOX_AGENT_API_KEY" || test -n "$LINKFOXAGENT_API_KEY"
echo "key present: $?"
```

If you installed into the profile skills directory, the first command should count 270 matching directories. The head of a `SKILL.md` shows `name:` and `description:` with no `license:` field, and the key test prints `0`. If the last command prints `1`, the scripts exit on stderr before any request goes out, with a message saying the API key is not configured, which is the cheapest failure to diagnose.

## Security

Every sampled skill carries a Snyk Warn, which is worth stating plainly: these skills are not passive markdown, most of them ship Python that sends your API key and query to a LinkFox-hosted endpoint over HTTPS, so Snyk is flagging networked code that handles a credential on every call, and a Warn is a prompt to read `scripts/` before pointing the suite at live store data rather than a Fail verdict or a clean bill of health.

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| linkfox-multimodal-recognize-image | Pass | Warn | Warn |
| linkfox-amazon-search | Pass | Pass | Warn |
| linkfox-dld-product-search | Pass | Pass | Warn |
| linkfox-mpstats-ozon-product-search | Pass | Pass | Warn |
| linkfox-1688-product-detail | Pass | Pass | Warn |

The data path is one directional and easy to audit. Scripts read `LINKFOX_AGENT_API_KEY` or `LINKFOXAGENT_API_KEY` from the environment, POST to `https://tool-gateway.linkfox.com` (overridable with `LINKFOX_TOOL_GATEWAY`), and write the response to disk. No script writes the key anywhere, but on the scripts that follow the shared template the full response body lands in `./linkfox/<date>/<session>/data/` under whatever directory the agent ran from, which means marketplace data and anything else in that response persists in plain JSON wherever your session happens to be working.

Two other surfaces deserve a read. The Amazon Ads skills carry OAuth state: `amazon-ads-auth` holds the authorized store and profile list that `amazon-ads-report` depends on, and the Temu skills keep access tokens in `~/.linkfox/temu-access-tokens.json`, so that file is a credential store and deserves the same handling as an SSH key. And 229 of the skills ship `scripts/onboarding.py`, which can send an SMS code, log in with a phone number and place a paid order through WeChat or Alipay. That is a purchase flow sitting inside a skill directory: do not let an unattended agent run it, and do not hand it a phone number you do not control.

## Limitations

- Snapshot data, verified 2026-10-30: 58,424 combined installs across 200 indexed listings; 115 GitHub stars; MIT; last pushed 2026-10-29. Counts drift over time.
- Three different counts describe one suite. The README badge says 166 skills, skills.sh indexes 200 listings, and the tree at main holds 270 `SKILL.md` directories. Install with `--list` and trust the directory listing, not the badge.
- The suite is Chinese-first. All 270 `SKILL.md` bodies and all 270 descriptions in the clone contain Chinese, with English trigger keywords appended, so English-only routing works but review, debugging and prompt rewriting assume a reader who can follow the Chinese.
- Nothing runs without a paid LinkFox account. The key is mandatory, calls spend credits, and a billing error routes the agent into a plan-purchase flow rather than a retry.
- Five of 200 listings were security-sampled, so the verdict table describes five skills, not the suite. The remaining 195 listings were not sampled for this guide, so their verdicts are unknown here.
- There is no MCP server and no plugin manifest: the repository root holds only `LICENSE`, `README.md` and `skills/`, so a Hermes profile gains skill directories plus Python scripts it has to shell out to, not MCP tools.

## Related

- [OpenSEO - Self-Hosted SEO Platform, MCP and Skills Setup](/hermes/skills/catalog/open-seo-setup)
- [Composio - SDK Monorepo and Agent Toolkit Setup Guide](/hermes/skills/catalog/composiohq-composio-setup)
- [Developer Kit - Java and TypeScript Skill Suite Setup](/hermes/skills/catalog/developer-kit-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install six skills, not 270. Pick the marketplace you actually sell on, add `linkfox-multimodal-recognize-image` for image work and the two or three patent skills, and skip the rest until a task needs them; most directories carry their own scripts and reference tree.
- Export both key names. The README documents `LINKFOXAGENT_API_KEY` while the scripts check `LINKFOX_AGENT_API_KEY` first, so setting both removes a class of confusing auth failures that look like a bad key.
- Run the scripts from a scratch directory. Where a script follows the shared output template, responses are written to `./linkfox/<date>/<session>/data/` relative to the working directory, so a session started inside a repository can end up with marketplace JSON in that repository.
- Install `linkfox-amazon-ads-auth` before `linkfox-amazon-ads-report`. The report script checks for its dependency at startup and exits 42 with `DEPENDENCY_MISSING`, which reads like a broken install rather than a missing sibling skill.
- Confirm credit cost before any batch loop. Several skills state that multi-SKU work should be done one call per SKU only after the user agrees to the added cost, and an agent that paginates 50 ASINs without asking will spend real money.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
