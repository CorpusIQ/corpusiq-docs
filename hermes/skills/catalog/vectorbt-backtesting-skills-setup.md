---
title: "VectorBT Backtesting Skills - Quant Workflow Setup"
description: "marketcalls/vectorbt-backtesting-skills: 15.2K combined installs. Six skills that turn a strategy idea into a costed, benchmarked VectorBT backtest."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vectorbt-backtesting-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "backtesting", "quant", "vectorbt"]
---

# VectorBT Backtesting Skills - Setup Guide

**Source:** [marketcalls/vectorbt-backtesting-skills](https://www.skills.sh/marketcalls/vectorbt-backtesting-skills) via skills.sh - 15.2K combined installs across 6 indexed listings; first seen 2026-11-01 (morning sweep)

**GitHub:** [marketcalls/vectorbt-backtesting-skills](https://github.com/marketcalls/vectorbt-backtesting-skills) - 217 stars, no LICENSE at the repo root, branch master, last pushed 2026-07-12; 6 `SKILL.md` files under `.claude/skills/`, one per command directory, backed by around 20 rule files and 12 strategy templates

**Category:** Quantitative backtesting: strategy simulation, parameter optimisation, cost modelling and benchmark comparison

**Quality Tier:** 🟡 Yellow - all three sampled skills pass every scanner, but the repository ships no LICENSE file at its root, so the terms for reuse are unstated

This pack is a set of commands for a coding agent rather than a library of documentation. Five of the six skills are user-invocable commands that generate a Python script into a `backtesting/<strategy>/` folder in your project; the sixth, `vectorbt-expert`, is marked as not user-invocable and exists as the shared reference those commands read first. The README describes the surface as five commands, twelve pre-built strategy templates and roughly 20 rule files, covering Indian, US and crypto markets.

The design assumption is that a backtest is only meaningful when costs, benchmark and signal hygiene are part of it. The rules require market-specific fee models, a benchmark per market (NIFTY, the S&P 500, Bitcoin), signal cleaning before simulation, whole-share sizing for equities and lot sizes for index futures. The backtest command is also required to print a strategy-versus-benchmark table and to explain the report in plain language, which is as close to an anti-overclaiming device as a skill file gets.

## Installation

The README documents the skills CLI, including per-skill selection:

```bash
npx skills add marketcalls/vectorbt-backtesting-skills
npx skills add marketcalls/vectorbt-backtesting-skills -s backtest
npx skills add marketcalls/vectorbt-backtesting-skills -l
npx skills add marketcalls/vectorbt-backtesting-skills -g
```

The README says the CLI detects which agents are installed and writes to the right directory, naming Claude Code, Cursor, Codex, OpenCode, Cline, Windsurf, GitHub Copilot, Gemini CLI and Roo Code among 40+, and that `-g` installs globally. The files in the tree sit under `.claude/skills/`, so a manual copy needs that mapping:

```bash
git clone --depth 1 https://github.com/marketcalls/vectorbt-backtesting-skills.git /tmp/vectorbt-backtesting-skills
cp -r /tmp/vectorbt-backtesting-skills/.claude/skills/. ~/.hermes/profiles/corpusiq/skills/
```

Installing the skills does not install the environment they describe. That is the job of the `setup` skill, which detects the operating system, creates a virtual environment, installs the package set (`openalgo vectorbt plotly pandas numpy yfinance python-dotenv tqdm scipy numba duckdb psutil` and others), creates a `backtesting/` folder and writes a `.env` from the bundled `.env.sample`. TA-Lib is optional: OpenAlgo's own indicator library is the default with 100+ indicators, and TA-Lib is only needed if you explicitly want to name it in a request. On Linux, the TA-Lib route compiles from source, so budget a few minutes and a C toolchain if you opt in.

The pack expects an OpenAlgo API key for Indian data. US and crypto backtests run on `yfinance` or CCXT and need no key, so a first run against a US symbol is the cheapest way to confirm the environment works.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| backtest | 3,409 | Writes a complete script for one strategy on one symbol: data fetch, signals, portfolio, stats, benchmark table, tearsheet, plots and CSV. |
| vectorbt-expert | 2,991 | The shared rulebook: data sources, signal cleaning, sizing, fee models per market, DuckDB loading and plotting conventions. |
| optimize | 2,374 | Parameter grid search with progress bars, return and Sharpe heatmaps, top-ten tables and the best combination against the benchmark. |
| strategy-compare | 2,283 | Several strategies, or long versus short versus both, on one symbol with a side-by-side metric table and overlaid equity curves. |
| quick-stats | 2,051 | An inline code block with a default EMA crossover and a compact stats printout including alpha over the benchmark, no file written. |
| setup | 2,044 | Environment bootstrap: OS detection, virtual environment, dependency install, `backtesting/` folder and `.env` configuration. |

Six listings, six directories. This pack has no index-to-tree gap and no row below the cut, so the table is the whole index rather than a sample of it. The commands also inherit from one another: `backtest`, `optimize`, `strategy-compare` and `quick-stats` each begin by reading the same `vectorbt-expert` rules, which is why the second row carries the second-highest install count despite never being invoked directly.

## Why This Matters for Hermes Agents

Backtesting is the domain where an agent's fluent output is most expensive to be wrong. A strategy that looks good in a chart because the simulation ignored fees, sized positions in fractional shares and compared itself to nothing is not a weak result, it is a misleading one. This pack is built around preventing exactly that: the fee model is a required parameter, the benchmark is a required comparison, and signal cleaning happens before the portfolio is built.

The rule files encode the details an agent would otherwise skip. Signals are cleaned with a removal helper so a held position is not re-entered on every bar of a condition. Candlestick plots set a categorical axis so weekends do not leave gaps that look like crashes. Futures sizing uses the revised index lot sizes rather than a guess. DuckDB loading auto-detects between two table layouts. None of that is interesting finance, and all of it changes the numbers.

The plain-language reporting rule is the part worth copying into other domains. Every command ends by explaining the result to someone who is not a quant, which forces the agent to state what the drawdown was and what it means rather than presenting a Sharpe ratio as a verdict.

The pack also demonstrates a clean division between a reference skill and command skills. Five commands stay short because one skill holds the rules, which keeps context small and makes the rules consistent across commands.

## Usage

| You say | What happens |
|---|---|
| "Backtest an EMA crossover on RELIANCE daily" | `backtest` writes `RELIANCE_ema-crossover_backtest.py` with delivery fees, the NIFTY benchmark, a strategy comparison table, a tearsheet and equity plus drawdown plots. |
| "Is RSI 14 actually better than RSI 21 on SBIN" | `optimize` sweeps the window and threshold ranges, prints the top ten by return and by Sharpe, and heatmaps both. |
| "Compare EMA crossover, RSI and Donchian on the same data" | `strategy-compare` runs all three on one fetch, prints a side-by-side table with the benchmark and overlays the equity curves. |
| "Just give me the numbers for HDFCBANK without creating files" | `quick-stats` returns a single code block for a notebook cell with return, Sharpe, Sortino, drawdown, win rate and alpha over NIFTY. |
| "Set this machine up for backtesting" | `setup` detects the OS, builds the virtual environment, installs the package set, creates the folder and writes `.env` from the sample. |
| "Why does my equity curve show gaps at weekends" | `vectorbt-expert` points at the plotting rule that sets the x axis to a category type, and the data rules that resample intraday bars correctly. |
| "Load this DuckDB file instead of calling the API" | The commands auto-detect the two supported table layouts and switch to a read-only local connection. |

## Verification

The raw path for the backtest command returned HTTP 200 on branch master when this guide was written on 2026-11-01:

```bash
curl -sL -o /dev/null -w "%{http_code} backtest\n" \
  https://raw.githubusercontent.com/marketcalls/vectorbt-backtesting-skills/master/.claude/skills/backtest/SKILL.md
```

Expect `200`. After the clone, confirm all six command directories arrived and that the rule files came with them:

```bash
ls /tmp/vectorbt-backtesting-skills/.claude/skills | wc -l
find /tmp/vectorbt-backtesting-skills/.claude/skills -name SKILL.md | wc -l
ls /tmp/vectorbt-backtesting-skills/.claude/skills/vectorbt-expert/rules | wc -l
```

Both counts should print 6, and the last command should show a rules folder with roughly 20 files. A missing rules folder is the failure worth catching: five commands depend on it, and they will still generate scripts without it, just less accurately.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| backtest | Pass | Pass | Pass |
| vectorbt-expert | Pass | Pass | Pass |
| optimize | Pass | Pass | Pass |

Half the pack was sampled and all of it is clean, which is the strongest coverage ratio in this catalogue batch. The repository itself holds no installer, no package manifest at the root beyond `requirements.txt`, and no post-install hooks, so the skills cannot execute anything on their own.

What the skills instruct is a different question, and it is worth reading before the first run. `setup` tells the agent to create a virtual environment and `pip install` a package list with no version constraints, which means the environment is only as reproducible as the day it was built. On the Linux TA-Lib path it downloads a source tarball over plain `http` from SourceForge and compiles it, so that single line is the one place in the pack where transport security, not just supply chain, is in play.

The data path also deserves a decision. The Indian workflow reads its API key from `.env` and calls a broker-side client for history. If the key you place there carries anything beyond market data, an agent that decides to write its own order-placing script is one step from live trading, so issue a data-only key and keep the `.env` out of version control.

## Limitations

- Snapshot data, verified 2026-11-01: 15,152 combined installs across 6 indexed listings; 217 GitHub stars; no LICENSE at the repo root; last pushed 2026-07-12. Counts drift over time.
- No licence file at the root. The README advertises use across 40+ agents but states no grant, so the reuse terms for the rule files and templates are unstated.
- The rules bake in dated market facts: revised SEBI index lot sizes effective December 2025, and fee tiers for delivery, intraday, futures and options. Those constants age, and nothing in the pack checks them against the current schedule.
- `setup` installs unpinned dependencies. A breaking release of VectorBT or its pandas and numba requirements changes behaviour without any file in the repository changing.
- `vectorbt-expert` is marked as not user-invocable. Invoking it directly does nothing; it is a reference that the other five commands read, which is easy to misread as a missing command.
- The Indian path needs an OpenAlgo API key and a reachable broker-side service, so a first run depends on account setup that the skills do not walk you through. US and crypto backtests avoid that dependency.
- Install counts sit between 2,044 and 3,409 across only six skills, so the ordering says more about which command people reach for first than about quality.

## Related

- [Claude Trading Skills - 74-Skill Trading Workflow Setup](/hermes/skills/catalog/claude-trading-skills-setup)
- [Longbridge Skills - Brokerage Data and Trading Suite](/hermes/skills/catalog/longbridge-skills-setup)
- [GMGN Agent Skills - On-Chain Analytics and Trading Setup](/hermes/skills/catalog/gmgn-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `setup` first even if you think the environment is fine. It detects the OS, writes the `.env` from the sample and creates the folder structure the other commands assume, and every one of them writes scripts relative to that folder.
- Start with a US symbol. `yfinance` needs no key, so an AAPL backtest proves the whole chain, data to fees to tearsheet, without waiting on broker credentials.
- Read the rule files before tuning parameters. Optimisation over a look-ahead bug produces a beautiful heatmap of a result you cannot trade, and the rules are where that class of error is documented.
- Change fee constants to your own broker rather than trusting the defaults. The pack calls itself broker-neutral for exactly this reason, and a backtest that assumes 0.111% delivery fees will flatter a strategy you run through a discount broker.
- Use `quick-stats` for a first look and `backtest` for anything you will act on. The inline version writes nothing and skips the tearsheet, which is the right trade for a sanity check and the wrong one for a decision.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
