---
title: "AGI Pro Trading Skills - 68 Quant and DeFi Skills"
description: "agiprolabs/claude-trading-skills on skills.sh: 33.3K combined installs; 68 crypto and DeFi quant skills for market data, backtesting, risk and tax."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agiprolabs-trading-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "trading", "defi", "quantitative finance", "solana", "backtesting"]
---

# AGI Pro Trading Skills - Setup Guide

**Source:** [agiprolabs/claude-trading-skills](https://www.skills.sh/agiprolabs/claude-trading-skills) via skills.sh - 33,316 combined installs across 68 indexed listings; first seen 2026-11-08 (Nov 8, 2026 evening sweep)
**GitHub:** 515 stars, MIT via `LICENSE.md`, `main` branch, last pushed 2026-09-03, 68 SKILL.md directories under `skills/`
**Category:** Trading research for agents: market data, on-chain analytics, backtesting, risk, tax compliance and prediction markets
**Quality Tier:** 🟡 Beta - 68 skills with a working install path and MIT licensing, but several listings carry Warn verdicts, three skills are marked as stubs, and the plugin manifest still claims 67 skills against 68 directories.

This pack is a library rather than a single skill: 68 directories under `skills/`, each with its own `SKILL.md`, plus `references/` and `scripts/` folders where a topic needs them. Coverage is crypto and DeFi first, from Solana RPC and Jupiter swap execution through Birdeye and DexScreener market data, then out to backtesting engines, portfolio risk, tax export and prediction markets.

Every file describes how to compute something, model something or measure something. None of it is a signal service, and the README says so directly: nothing produced by these skills constitutes financial advice. Read the pack that way and the value is the structure it imposes on the work, the validation rules and the accounting detail. Read it as an execution system and the risk is yours, not the repository's.

## Installation

The README offers two paths. Option A is the Claude Code plugin, which requires Claude Code v1.0.33 or newer:

```text
/plugin marketplace add agiprolabs/claude-trading-skills
/plugin install trading-skills@agiprolabs-claude-trading-skills
```

After that the skills are namespaced as `/trading-skills:skill-name`, and `/plugin` lists the install, `/plugin disable` and `/plugin enable` toggle it, and `/reload-plugins` applies changes without a restart.

Option B is a clone and copy, which is what you want for Hermes and for any other Agent Skills compatible client:

```bash
git clone https://github.com/agiprolabs/claude-trading-skills.git
cp -r claude-trading-skills/skills/* ~/.claude/skills/
```

The README gives the per-client target directories for the copy: `~/.claude/skills/` for Claude Code, `~/.cursor/skills/` for Cursor, `~/.codex/skills/` for Codex and `~/.gemini/skills/` for Gemini CLI, with the dot-directory equivalent under a project root for a single-project install. For Hermes the destination is the profile skills directory, and the copy is the same shape.

Dependencies are per skill, not per repo. The README asks for Python 3.9 or newer, 3.12 recommended, and `uv` as the package manager, installed with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version
```

Then install only what the skills you plan to use actually need, since each `SKILL.md` lists its own requirements. The README's own convention is `uv pip install package-name`. No API key is required to start: DexScreener, DeFiLlama, Jupiter quotes and the CoinGecko free tier all work unauthenticated, and keys are only needed for Birdeye, Helius and similar paid-tier sources.

## What It Provides

The threshold for this guide is 512 installs, so the 24 listings at or above it appear below and the rest are summarised in a sentence.

| Skill | Installs | Use For |
|---|---|---|
| walk-forward-validation | 784 | Time-series-aware splits, purged cross-validation, and overfit detection for strategies and ML models |
| risk-management | 699 | Portfolio drawdown controls, exposure limits, and circuit breakers for crypto trading |
| pandas-ta | 632 | 130+ technical indicators computed over crypto market data |
| position-sizing | 625 | Fixed fractional, volatility-adjusted, Kelly, and liquidity-constrained trade sizing |
| regime-detection | 624 | Volatility clustering and trend detection for adaptive strategy selection |
| kelly-criterion | 570 | Optimal sizing with fractional variants and edge estimation |
| trade-journal | 562 | Structured trade logging, performance review, and behavioral pattern detection |
| feature-engineering | 557 | Price, volume, on-chain, and microstructure features for ML trading models |
| signal-classification | 555 | XGBoost and LightGBM classifiers with walk-forward validation, SHAP, and threshold tuning |
| market-microstructure | 553 | DEX orderflow analysis, trade classification, and buyer and seller pressure on Solana |
| exit-strategies | 552 | Stop-loss methods, take-profit rules, and trailing stop implementations |
| strategy-framework | 542 | Standard template for entry rules, exit rules, sizing, risk parameters, and criteria |
| trading-visualization | 541 | Candlestick charts, equity curves, drawdowns, and correlation heatmaps |
| backtrader | 540 | Event-driven bar-by-bar backtesting with complex order types and analyzers |
| volatility-modeling | 538 | GARCH, EWMA, realized volatility, and volatility cones |
| vectorbt | 535 | Vectorized backtesting with parameter optimization and portfolio simulation |
| portfolio-analytics | 529 | Return and risk metrics, risk-adjusted ratios, and rolling analysis |
| mean-reversion | 528 | Hurst exponent, half-life estimation, z-score signals, and ADF testing |
| ta-lib | 526 | 150+ technical functions and 61 candlestick patterns through the C library |
| whale-tracking | 524 | Large wallet monitoring and accumulation and distribution signals on Solana |
| options-pricing | 522 | Black-Scholes, binomial trees, Monte Carlo, and Greeks, shipped as a stub |
| market-microstructure-traditional | 516 | Order book dynamics, market making theory, and execution quality measurement |
| slippage-modeling | 515 | Slippage curves and optimal trade sizing against AMM liquidity depth |
| ohlcv-processing | 512 | OHLCV resampling, gap handling, anomaly detection, and multi-source merging |

The remaining 44 indexed listings range from 173 to 507 installs.

The tail is where the pack turns crypto-native. Below the threshold sit the on-chain skills (`solana-rpc`, `helius-api`, `birdeye-api`, `defillama-api`, `wallet-profiling`, `token-holder-analysis`, `sybil-detection`, `liquidity-analysis`, `dex-pool-analysis`), the execution skills (`dex-execution`, `jito-bundles`, `shredstream`, `rl-execution`, `raptor-dex`), the tax cluster (`cost-basis-engine`, `crypto-tax-export`, `wash-sale-detection`, `tax-loss-harvesting`, `tax-liability-tracking`, `regulatory-reporting`) and the six prediction market skills (`kalshi-api`, `polymarket-api`, `kalshi-weather-markets`, `kalshi-crypto-index-markets`, `prediction-market-strategy`, `prediction-market-live-ops`).

The install curve is flat rather than spiky. The top skill has 784 installs and the bottom has 173, a spread of under 5x across 68 listings, which is consistent with a pack that is installed and browsed as a set rather than with individual skills winning their own distribution. Against 515 GitHub stars that is roughly 65 installs per star, a ratio that points at the plugin manifest and at agent discovery rather than at people reading the README.

Three skills are explicitly tagged `[STUB]` in their own descriptions: `options-pricing`, `fixed-income` and `regulatory-reporting`. They are scaffolding with the structure and the right vocabulary, not finished implementations, and an agent that treats them as complete will produce plausible formulas with no tested code behind them.

## Why This Matters for Hermes Agents

The useful property here is that the coding failures an agent makes in quantitative work are already written down. `walk-forward-validation` opens by explaining why k-fold cross-validation is wrong for financial time series, and lists the four mechanisms that break it: lookahead bias from random splits, autocorrelation letting Monday train on Tuesday, regime dependence, and label overlap when labels span windows. That is the exact mistake an LLM makes when asked to backtest something, and it is corrected before the agent writes a line.

The second property is that hard limits are encoded as limits rather than as advice. `position-sizing` states the thesis as a rule, that size determines survival and entries do not, then lays out fixed fractional, volatility-adjusted, Kelly, liquidity-constrained and anti-Martingale sizing with an account-level cap ladder on top. `risk-management` carries drawdown tiers and circuit breakers. The two skills cross-reference each other, and `risk-management` also names `liquidity-analysis`, `slippage-modeling` and `exit-strategies` as the places its limits get applied, so the risk framing travels with the code.

The third is coverage of the tax problem, which is where most crypto tooling stops. `cost-basis-engine` implements specific identification, FIFO, LIFO, HIFO and proportional average cost with partial sells; `wash-sale-detection` implements the 61-day window and tracks disallowed losses; `crypto-tax-export` writes Koinly, CoinTracker, CoinLedger and TokenTax formats plus IRS Form 8949. Those are checkable outputs, not opinions, which makes them a good fit for an agent that has to answer a question and show the artefact.

The honest counterweight is that this is a library, not a gate. Installing it gives an agent 68 sets of instructions, several of which end in a transaction-building path: `dex-execution` quotes, builds, signs and confirms Jupiter swaps, `solana-tx-building` assembles instructions with compute budget and priority fees, `jito-bundles` submits bundles, and `prediction-market-live-ops` is written for live-money operation. An agent with a funded keypair and these skills installed can move funds. The repository is careful about this, and the care is in prose, so it has to be matched by your own signing policy.

## Usage

| You say | What happens |
|---|---|
| "Backtest this moving average crossover on 2 years of hourly candles" | Picks `vectorbt` or `backtrader`, stages data through `ohlcv-processing`, and validates with `walk-forward-validation` splits rather than a random shuffle |
| "This strategy returned 40 percent in the backtest, is that real" | Runs the overfit checks in `walk-forward-validation`, reports purged CV results and flags label overlap as the likely source of inflation |
| "How much should I put into this Solana token at 2 percent portfolio risk" | Applies `position-sizing` with a liquidity-constrained cap from `slippage-modeling` and checks the drawdown tiers in `risk-management` |
| "Is this token's holder base concentrated" | Chains `birdeye-api` for market data with `token-holder-analysis` for distribution metrics and `sybil-detection` for coordinated clusters |
| "Who is accumulating this token before the move" | Uses `whale-tracking` for large wallet flows and `wallet-profiling` to classify the counterparties |
| "Export my 2025 trades for my accountant" | `cost-basis-engine` computes basis, `wash-sale-detection` flags disallowed losses, and `crypto-tax-export` writes the Koinly and Form 8949 files |
| "Price a Kalshi temperature contract for tomorrow in Phoenix" | `kalshi-weather-markets` maps the forecast ensemble to a probability, and `prediction-market-strategy` sizes it with fractional Kelly after fees |

## Verification

The default branch is `main`, so the raw paths resolve directly. Both of these return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/agiprolabs/claude-trading-skills/main/README.md | head -20
curl -fsSL https://raw.githubusercontent.com/agiprolabs/claude-trading-skills/main/skills/walk-forward-validation/SKILL.md | head -20
```

The README should open with the MIT licence badge and the 68 skills badge. The skill file should open with YAML frontmatter naming `walk-forward-validation` and a description scoped to time-series-aware splits and overfit detection, followed by a heading and the four-reasons section on why standard cross-validation fails.

After a clone, confirm the directory count matches the claim before trusting the install:

```bash
ls -d claude-trading-skills/skills/*/ | wc -l
ls claude-trading-skills/skills/*/SKILL.md | wc -l
find claude-trading-skills/skills -name SKILL.md | wc -l
```

All three should print 68, one SKILL.md per directory and no nested duplicates. Then check that one installed skill is loadable from the target directory, and that the frontmatter survived the copy:

```bash
head -5 ~/.hermes/profiles/corpusiq/skills/risk-management/SKILL.md
```

The cheapest functional test is the demo path the risk skills ship with, which runs on the standard library alone and needs no API keys:

```bash
python claude-trading-skills/skills/risk-management/scripts/risk_dashboard.py --demo
```

If that prints a risk dashboard, the Python side is wired. If it fails on an import, the dependency list in that `SKILL.md` is the place to look, not the repository root. Most other skills do need packages, installed per the README convention with `uv pip install`.

## Security

skills.sh verdicts for sampled skills, verified 2026-11-08, re-check the individual security pages before production use. Several skills carry Warn verdicts from Socket or Snyk, and nothing shipped here is financial advice: this catalog is analysis tooling.

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| walk-forward-validation | Pass | Pass | Pass |
| mean-reversion | Pass | Pass | Warn |
| wallet-profiling | Pass | Pass | Warn |
| dex-execution | Pass | Warn | Warn |
| prediction-market-live-ops | Pass | Warn | Pass |

The skills are markdown plus bundled Python scripts, and the scripts are where the actual surface sits. A skill directory can contain `scripts/` and `references/`, and the README's own convention is to run them with `uv pip install` dependencies. Read the script before you run it, particularly in the execution cluster, because `dex-execution` and `solana-tx-building` construct and sign transactions.

The larger risk is credential scope. Birdeye, Helius, SolanaTracker and Kalshi each need a key, and Kalshi's is an RSA private key used for request signing. Keep those in a scoped environment or a vault the agent can read but not print, and never in the working tree. A keypair with SOL balance plus these skills is a live trading account with no confirmation step unless you build one.

Two structural notes. The repository is not archived and still accepting pull requests, so the code you install can change under you, and pinning a commit is the only stable reference. And the plugin manifest describes 67 skills while the tree holds 68, which means the fastest install path is not guaranteed to expose every skill; the manual copy is the way to get a count you can verify.

## Limitations

- Snapshot data, verified 2026-11-08: 33,316 combined installs across 68 indexed listings; 515 GitHub stars; MIT license; last pushed 2026-09-03. Counts drift over time.
- Three skills are stubs by their own description: `options-pricing`, `fixed-income` and `regulatory-reporting`. They provide structure and vocabulary, not tested implementations.
- Crypto and DeFi coverage is deep, the rest is thin. Equities, futures and FX are not in the pack, and the README describes the collection as extensible to them rather than as covering them.
- Several skills carry Warn verdicts from Socket or Snyk, so the pack is not uniformly clean at the scanner level, and the sampling above covers five of 68 listings.
- The plugin manifest at `.claude-plugin/plugin.json` reads 67 skills while the tree contains 68 directories, so the plugin route and the manual copy do not necessarily install the same set.
- Many skills need API keys and paid tiers to be useful. The free sources cover market data, but holder analytics, parsed transactions and prediction market trading all assume accounts you have to provision.
- Nothing here is financial advice, and none of the skills carry a performance record. Install counts measure discovery, not accuracy.

## Related

- [Claude Trading Skills - 74-Skill Trading Workflow Setup](/hermes/skills/catalog/claude-trading-skills-setup)
- [Coinos Skills - AiCoin Crypto Trading Suite Setup](/hermes/skills/catalog/coinos-trading-skills-setup)
- [Finance Skills - Financial Analysis for Hermes Agents](/hermes/skills/catalog/finance-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy rather than install through the plugin if you need a known set. The clone lets you count directories and diff them against a pinned commit, which the plugin path does not.
- Read `walk-forward-validation` first, even if you plan to use none of the backtesting skills. It is the cheapest correction to the backtest an agent will otherwise write for you.
- Check for the `[STUB]` tag in a skill description before relying on its output. Three skills carry it, and they read as complete until you notice.
- Keep API keys out of the skills directory. Skills load whole directories into context, and a key sitting next to a `SKILL.md` is a key in a prompt.
- Treat the prediction market cluster as a unit. `kalshi-api` and `polymarket-api` hold the exchange mechanics, `prediction-market-strategy` holds sizing and validation, and the market-type skills hold contract semantics; using one without the others produces a plausible price with no settlement logic.
- Pin the commit you install. The repository is active, so a raw URL that resolves today can point at different code next month.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
