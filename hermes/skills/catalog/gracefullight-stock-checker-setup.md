---
title: "Stock Checker - Ticker Analysis for Agents Setup"
description: "gracefullight/stock-checker: 28.6K combined installs across 69 indexed listings, ticker analysis and backtesting skills plus an oma-* agent framework"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gracefullight-stock-checker-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "finance", "stock analysis", "trading", "backtesting"]
---

# Stock Checker - Setup Guide

**Source:** [gracefullight/stock-checker](https://www.skills.sh/gracefullight/stock-checker) via skills.sh - 28.6K combined installs across 69 indexed listings; first seen Nov 13, 2026 (evening sweep)

**GitHub:** 49 stars, no licence file reported by GitHub, `main` branch, last pushed 2026-11-14, 211 `SKILL.md` files in the tree against 69 indexed listings, TypeScript-heavy (307 `.ts`, 89 `.tsx` files)

**Category:** Finance skills (ticker analysis, market data, backtesting) alongside a bundled oma-* agent framework

**Quality Tier:** 🟡 Yellow - no licence file, 69 indexed listings against 211 in-tree `SKILL.md` files, and Snyk Warns on two of four sampled skills.

gracefullight/stock-checker is a stock screening application whose repository also carries a large agent-skills tree. skills.sh indexes 69 skills from it, and they fall into two distinct groups: five finance skills for ticker analysis, market data, investment reporting and strategy backtesting, and everything else.

The everything else is the caveat. The repo bundles a complete oma-* agent framework - oma-backend, oma-qa, oma-frontend and about forty more in the 150 to 164 install range - plus a set of generic development skills such as brainstorm, commit, review and plan. These share the repository with the finance skills but are not part of the finance story. stock-analysis alone holds 12,297 of the 28,638 combined installs.

## Installation

The repository is a mise-managed monorepo. The skills are plain `SKILL.md` files under `.agents/skills/` and `.claude/skills/`, repeated across `.codex/skills/`, `.cursor/skills/`, `.gemini/skills/` and other harness directories. The README quickstart runs the app rather than installing skills:

```bash
mise install        # Node 26, Bun, Python 3.14, and uv
mise run install    # dependencies and Git hooks
mise run dev        # API + web
```

The `stock_checker` MCP is registered in `.codex/config.toml` and `.mcp.json`, run over stdio with `mise run mcp`. Reopen Codex or Claude Code in the repository after installation. The skills load when an agent runs inside the repo; to use one standalone, copy its `SKILL.md` into the agent's skills directory.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| stock-analysis | 12,297 | Analyze stocks and cryptocurrencies with Yahoo Finance data: portfolio management (create, add, remove assets), crypto top-20 analysis, and periodic performance reports across 8 stock and 3 crypto dimensions. |
| yahoo-finance | 4,689 | Pull prices, quotes, fundamentals, earnings, options, dividends and analyst ratings through the yfinance library, no API key required. |
| trading-analysis | 3,231 | Generate institutional-grade investment reports for stocks and ETFs with technical indicators, AI insights, charts and recommendations. |
| backtesting-trading-strategies | 2,002 | Backtest crypto and traditional strategies against historical data; compute Sharpe, Sortino and max drawdown, generate equity curves and tune parameters. |
| financial-data-fetcher | 546 | No resolvable `SKILL.md` for this listing in the current tree; the tree carries a spaced `Financial Data Fetcher` directory that the hyphenated listing name does not match. |

The remaining 64 indexed listings range from 10 to 164 installs.

## Why This Matters for Hermes Agents

The five finance skills are the part worth wiring into a Hermes agent. stock-analysis does real portfolio work - create, add and remove assets, run daily to yearly reports - on Yahoo Finance data that needs no API key. yahoo-finance is the data layer, trading-analysis turns the data into reports, and backtesting-trading-strategies closes the loop with Sharpe, Sortino and max drawdown.

The distribution deserves a plain reading. Most of the 28.6K combined installs are one skill, stock-analysis at 12,297. The rest of the 69 listings are the oma-* framework and generic dev skills that ride along in the same repo. An agent that only needs market data should reach for yahoo-finance and leave the framework alone.

The skills are plain Markdown, so they load wherever Agent Skills load. There is no licence file, which means the terms under which they can be reused are unresolved.

## Usage

| You say | What happens |
|---|---|
| "Analyze NVDA and add it to my portfolio" | stock-analysis pulls Yahoo Finance data, runs the 8 stock dimensions and adds the ticker to the portfolio. |
| "Get fundamentals, earnings and analyst ratings for TSLA" | yahoo-finance loads and returns the yfinance data without an API key. |
| "Write an investment report on AAPL" | trading-analysis generates an institutional-grade report with indicators, charts and a recommendation. |
| "Backtest a moving-average crossover on BTC" | backtesting-trading-strategies computes Sharpe, Sortino and max drawdown plus an equity curve. |
| "Track the top 20 crypto by market cap weekly" | stock-analysis runs its crypto analysis and the periodic performance report. |

## Verification

Probe two skills on the `main` branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/gracefullight/stock-checker/main/.agents/skills/stock-analysis/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/gracefullight/stock-checker/main/.agents/skills/yahoo-finance/SKILL.md
```

The finance skills live under `.agents/skills/<name>/SKILL.md`. One directory, `Financial Data Fetcher`, uses spaces in its name, which is why the hyphenated `financial-data-fetcher` listing does not resolve.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| stock-analysis | Pass | Pass | Warn |
| yahoo-finance | Pass | Pass | Pass |
| trading-analysis | Pass | Pass | Pass |
| backtesting-trading-strategies | Pass | Pass | Warn |

Two of the four sampled skills carry a Snyk Warn: stock-analysis, the most installed skill in the pack, and backtesting-trading-strategies. No sampled skill fails, and all four pass the Gen Agent Trust Hub and Socket. The other 65 listings publish no verdict at all, which is not the same as a pass. The repository has no licence file, so reuse terms are unresolved.

## Limitations

- Snapshot data, verified 2026-11-13: 28,638 combined installs across 69 indexed listings; 49 GitHub stars; no licence file; last pushed 2026-11-14. Counts drift over time.
- No licence file is reported by GitHub, so the terms under which the skills may be copied or redistributed are unresolved.
- The install index and the tree are far apart: 69 indexed listings against 211 `SKILL.md` files. The oma-* framework and generic dev skills make up most of the tree but carry little of the install weight.
- stock-analysis holds 12,297 of the 28,638 combined installs; the distribution is dominated by one skill.
- The repository bundles a whole oma-* agent framework (oma-backend, oma-qa, oma-frontend and about forty more in the 150 to 164 install range) alongside the finance skills.
- The financial-data-fetcher listing has no resolvable `SKILL.md`; its hyphenated name does not match the spaced `Financial Data Fetcher` directory.
- The repo is TypeScript-heavy (307 `.ts`, 89 `.tsx` files), and running the full app needs mise plus Node, Bun and Python 3.14.

## Related

- [Finance Skills - Financial Analysis for Hermes Agents](/hermes/skills/catalog/finance-skills-setup)
- [Octagon Finance Skills - Market Data and Analyst Workflows](/hermes/skills/catalog/octagon-finance-skills-setup)
- [Awesome Finance Skills - Market Analysis Pack](/hermes/skills/catalog/awesome-finance-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the four finance skills first, not the oma-* framework. The finance skills are the reason the pack matters; the framework is a general agent toolkit that shares the repo.
- Give stock-analysis and yahoo-finance a spin first. They need no API key, which is the fastest way to get real market data into an agent.
- Treat backtest metrics as inputs, not forecasts. backtesting-trading-strategies reports Sharpe, Sortino and drawdown; it does not predict future returns.
- Verify the licence before redistributing. There is no licence file, so treat the skills as source-available until the author clarifies.
- Copy only the skills you need. They are standalone `SKILL.md` files, so pulling one finance skill beats cloning the whole tree.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
