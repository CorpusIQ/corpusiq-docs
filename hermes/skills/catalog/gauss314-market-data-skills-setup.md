---
title: "Market Data Skills - Trading and Fundamentals Setup"
description: "gauss314/skills: 8.5K combined installs across 32 listings for market data - FRED, SEC filings, TradingView, Yahoo Finance and Argentine exchanges."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gauss314-market-data-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "market data", "finance", "backtesting"]
---

# Market Data Skills - Setup Guide

**Source:** [gauss314/skills](https://www.skills.sh/gauss314/skills) via skills.sh - 8.5K combined installs across 32 indexed listings; first seen Nov 13, 2026
**GitHub:** 253 stars, MIT licence at the repository root, `main` branch, last pushed 2026-06-14, 32 `SKILL.md` files under `skills/` against 32 indexed listings, 218 files in total
**Category:** Market data, fundamental data and quantitative tools for equities, macro and Argentine exchanges
**Quality Tier:** 🟡 Established - a 32-for-32 tree and a per-source Type, Cost and API key table, held back by a June 2026 last push, a lot of scrapers and API keys required on several skills.

This is the data layer of a finance agent: 32 skills that each wrap one market data source and hand back JSON. The collection was developed for the AI courses at UCEMA, and it shows in the structure. Skills are grouped into global market data, Argentine market data, brokers and tools, and every data skill carries a row in the README saying whether it is an API or a scraper, whether the source is free, freemium or paid, and whether you need an API key before anything returns.

The coverage is wider than the install count suggests. On the global side there is FRED with 840,000+ macro series, SEC EDGAR filings mapped into structured statements, TradingView's scanner with roughly 300 columns, Yahoo Finance endpoints, Finnhub and Alpha Vantage, a set of site scrapers (Finviz, Macrotrends, MarketScreener, MarketWatch, Investing, Barchart, CompaniesMarketCap) and API wrappers for Nasdaq, CBOE, Morningstar, SimplyWallSt and EarningsWhispers. On the Argentine side there are six skills covering BCRA, BYMA, MAE, CAFCI, INDEC and Data912, which is a market most vendors do not cover at all.

Three skills are pure computation rather than fetches: option pricing across nine methods with greeks and implied vol, an academic backtesting framework, and portfolio construction from Markowitz to hierarchical risk parity. Those work without any feed or key.

## Installation

The README documents three forms. Global install of selected skills, then everything, then one skill at a time:

```bash
npx skills add gauss314/skills -g
```

```bash
npx skills add gauss314/skills --all
```

```bash
npx skills add gauss314/skills --skill fred-macro
```

Per-skill commands exist for all 32 and are listed in the README's installation tables, keeping the same `npx skills add gauss314/skills --skill <name>` shape. Installing the whole collection pulls 218 files, including the `references/`, `scripts/` and `assets/` folders that each skill loads only when it needs them.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| fred-macro | 365 | FRED macro series (GDP, CPI, rates, employment, M2, VIX), search, tags and release calendars. Free API key required. |
| backtesting | 337 | Event-driven backtest engine with 30+ risk and performance ratios, 10 indicator classes, walk-forward validation and stress tests. |
| tradingview | 329 | TradingView scanner with about 300 columns, symbol search by ISIN or CUSIP, news headlines and scraped subpages. |
| yahoo-finance | 327 | Unofficial Yahoo endpoints: quotes, intraday and daily OHLCV, statements, options chains, futures, news and insider transactions. |
| sec-data | 287 | SEC EDGAR filings into structured income, balance sheet and cash flow data, with US-GAAP and IFRS concept mapping. |
| indec | 286 | Argentina's official Series de Tiempo API: IPC, EMAE, unemployment, poverty line, wages and about 4,250 series with server-side transforms. |
| data912 | 277 | Argentine live market data: local stocks, CEDEARs, bonds, MEP and CCL, refreshing every 20 seconds. |
| byma | 276 | BYMA panels, CEDEARs, sovereigns, corporate bonds, repos and options, plus MERVAL and BURCAP history. |
| bcra-macro | 276 | Central Bank of Argentina statistics: 638 national series, reserves, exchange rates, BADLAR, CER, UVA and LELIQ. |
| option-pricing | 272 | Nine pricing methods from Black-Scholes to Heston and Bates, greeks, implied vol solver and 15 CLI modes. |
| cafci | 271 | Argentine mutual funds: 1,152 funds and 4,615 classes with fees, daily snapshots and portfolio composition. |
| investing | 270 | Investing.com scrape: quotes, OHLCV history, statements, dividends, earnings and screener across 81,000+ equities. |
| portfolio | 268 | Portfolio construction: Markowitz, Black-Litterman, HRP, HERC and NCO with risk measures and 12 CLI modes. |
| google-finance | 262 | Internal Google Finance RPC: quotes, 1-minute intraday bars, financials, per-analyst detail and global indices in one call. |
| finnhub | 262 | Finnhub REST: quotes, company profile, financials, earnings calendar, price targets, insider trades and ESG scores. |
| cboe-data | 261 | CBOE indices, VIX futures chains, options with greeks, 1-minute intraday bars, exchange summaries and most-active lists. |
| alpaca-data | 260 | Alpaca market data for 5,000+ US stocks plus crypto and options, historical and real time over the IEX feed. |
| nasdaq-data | 259 | Nasdaq.com internal REST: quotes, short interest, financials, 13F institutional holdings and options chains. |
| earningswhispers | 257 | Full earnings call transcripts, prepared remarks plus Q&A, for 33,500+ stocks without authentication. |
| alpaca-trading | 257 | Alpaca trading API: orders, positions, account, paper and live, for stocks, crypto and options. |

The remaining 12 indexed listings range from 120 to 256 installs.

## Why This Matters for Hermes Agents

Market data is where an agent workflow fails quietly. A stale price or a mis-mapped statement line looks exactly like a correct one, and most of the effort is not analysis but plumbing: which endpoint, which key, which ticker convention, which field holds the number you want.

That plumbing is what this pack sells. Each skill names its endpoint, its parameters and the shape of the response, so the agent spends its context on the question rather than on reverse engineering a JSON tree. The Type and Cost columns in the README do the triage for you: you can see at a glance which skills will work with no account at all and which need a key before they return a single field.

The split between API and scraper matters more than it looks. An API skill breaks when the provider changes a schema and says so; a scraper breaks when someone ships a new front end, often with no error, just empty rows. Knowing which is which before wiring a skill into a daily job is the difference between a pipeline that fails loudly and one that quietly reports nothing.

The tools trio is the part that compounds. Option pricing, backtesting and portfolio optimisation need no feed, no key and no rate limit, so they can run inside a research loop as often as you like, and the outputs are deterministic for a given input set.

## Usage

| You say | What happens |
|---|---|
| "Pull the last ten years of US CPI and unemployment and chart the spread" | Runs `fred-macro` against FRED and returns the two series plus the derived spread. |
| "Get Apple's revenue, gross margin and cash flow for the last five years" | Runs `sec-data` against EDGAR and returns mapped statement rows rather than raw XBRL facts. |
| "Screen US stocks over 10 billion market cap with positive EPS growth" | Runs `tradingview` or `finviz` with the filter set and returns the matching tickers and columns. |
| "What is the Argentine inflation print for last month?" | Runs `indec` with the IPC shortcut and returns the series with the period-over-period change. |
| "Price a European call at 20 percent vol, 5 percent rate, one year out" | Runs `option-pricing` and returns the price, greeks and implied vol check across methods. |
| "Backtest a 50/200 moving average crossover on this ticker" | Runs `backtesting` and returns equity curve, drawdown and the risk ratio table. |
| "Build a minimum variance portfolio from these eight tickers" | Runs `portfolio` and returns weights, frontier points and risk contributions. |

## Verification

The tree is `skills/<name>/SKILL.md` on `main` for every listing. Two probes returned 200 when this guide was written:

```bash
curl -fsSL https://raw.githubusercontent.com/gauss314/skills/main/skills/fred-macro/SKILL.md | head -8
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/gauss314/skills/main/skills/backtesting/SKILL.md
```

After `--all`, confirm 32 directories under the skills target, each with a `SKILL.md`. The count is the check that matters: an interrupted install leaves some skills present and others missing, and the agent will not tell you which.

Read the skill's own references before a first live call. Several of these skills ship a limitations file next to the endpoint documentation, and it is the fastest place to learn a provider's rate limit or which fields are known to be unreliable.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| fred-macro | Pass | Pass | Warn |
| backtesting | Pass | Pass | Pass |
| tradingview | Pass | Pass | Warn |
| yahoo-finance | Pass | Pass | Warn |

The other 28 indexed listings carry no published verdicts. Three of the four sampled skills carry a Snyk warning, which fits the design: the scrapers and unofficial endpoints fetch pages and internal APIs whose owners never published a contract for them, so the content can change without notice. The skills are instruction and script files, not services, so the risk is what they fetch and what credentials you hand them, not what they execute on install.

## Limitations

- Snapshot data, verified 2026-11-13: 8,490 combined installs across 32 indexed listings; 253 GitHub stars; MIT LICENSE at the repository root; last pushed 2026-06-14. Counts drift over time.
- The MIT licence covers the skill text and scripts, not the data they retrieve. Provider terms, free-tier call limits and redistribution rules still apply to anything you store, cache or republish.
- Seven of the 21 global data skills are labelled Scraper (Finviz, Macrotrends, MarketScreener, MarketWatch, Investing, Barchart, CompaniesMarketCap) and two more are labelled API/Scraper. A page redesign breaks them, often silently, and scraping can sit outside a provider's terms of use.
- Several skills need an API key or an account before they return anything: FRED, Alpha Vantage, Finnhub, Alpaca data and Alpaca trading. The broker skills can place real orders if handed live credentials.
- The collection was built for a university course, so the framing is teaching-first. Expect worked examples and validation suites rather than hardened error handling for unattended production jobs.
- Nothing here is investment advice, and none of the ratios or backtests account for your costs, taxes or slippage.

## Related

- [Awesome Finance Skills - Market Analysis Pack](/hermes/skills/catalog/awesome-finance-skills-setup)
- [Claude Trading Skills - 74-Skill Trading Workflow Setup](/hermes/skills/catalog/claude-trading-skills-setup)
- [Hithink Finance - Tonghuashun A-Share Data Skill Setup](/hermes/skills/catalog/hithink-finance-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install one skill first, not all 32. Each skill's references are dense, and a single working fetch teaches you the response shape faster than reading twelve of them.
- Use the README's Cost and API Key columns as the triage. If a task needs to run unattended, prefer the free no-key skills and keep the keyed ones for interactive sessions.
- Pair a scraper with an API skill for the same instrument. When the scrape returns empty rows, the API skill tells you whether the market moved or the page broke.
- Keep `option-pricing`, `backtesting` and `portfolio` installed permanently. They are dependency-light, need no credentials, and are the cheapest way to sanity-check a number that came out of a feed.
- Treat every price as delayed until you have read that skill's own notes. Yahoo runs about 15 minutes behind, Investing 15 to 20, and the CBOE quotes are delayed too.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
