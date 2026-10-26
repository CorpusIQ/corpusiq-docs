---
title: "Longbridge Skills - Brokerage Data and Trading Suite"
description: "Longbridge official skills: 108.2K combined installs. 13 skills for quotes, technicals, options, fundamentals, portfolio and quant via CLI and MCP."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/longbridge-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "market data", "trading"]
---

# Longbridge Skills - Setup Guide

**Source:** [longbridge/skills](https://www.skills.sh/longbridge/skills) via skills.sh - 108.2K combined installs across 134 indexed listings
**GitHub:** [longbridge/skills](https://github.com/longbridge/skills) (66 stars; MIT; pushed 2026-10-26; no repository description; layout `skills/<name>/SKILL.md` for 13 skills, each with its own `references/` directory, plus `docs/install.md`, `index.json`, `.mcp.json` and Claude and Codex plugin manifests)
**Category:** Finance / Brokerage Market Data and Trading Workflows
**Quality Tier:** 🟡 Verified with caveats - official Longbridge publisher, MIT, 13 skills and a push on the day of this sweep, but sampled scanner verdicts are mixed (two Warns on the technical skill, a Snyk Warn for direct money access on the portfolio skill), the install index carries 134 listings against 13 directories, and two of the 13 skills are marked mutating in their own frontmatter

Longbridge is a Hong Kong online brokerage, and `longbridge/skills` is its own agent layer: 13 consolidated skills that teach an assistant to pull live quotes, filings, fundamentals and account data through the Longbridge CLI and the Longbridge MCP server, and then to reason about them with named frameworks (Chan theory, Elliott Wave, Graham net-net, Buffett moat, pairs trading, VaR).

The suite is the v2 generation of a much larger set. The README states that the previous release shipped 127 skills and that `npx skills add` and `npx skills update` do not remove renamed or retired ones, so v2 collapsed the surface into 13 skills with a documented reinstall path that wipes every old `longbridge` and `longbridge-*` entry from `~/.claude`, `~/.agents`, `~/.gemini` and `~/.opencode` before installing fresh.

The split that matters operationally is CLI versus MCP. The CLI is a local Rust binary that runs in-process and authenticates with `longbridge auth login`; the install doc describes 12 read-tier skills on that path, with six analysis-tier skills depending on the hosted MCP server at `https://mcp.longbridge.com`. Both routes are OAuth against a real brokerage account, and the permission you tick during login decides whether account-level commands work at all.

## Installation

```bash
# Install all 13 skills globally, which is what the README recommends
npx skills add longbridge/skills -g

# Or install a subset
npx skills add longbridge/skills -g --skill longbridge-market-data
npx skills add longbridge/skills -g --skill longbridge-portfolio --skill longbridge-research
```

The CLI is the load-bearing prerequisite for the read tier:

```bash
# macOS
brew install --cask longbridge/tap/longbridge-terminal

# Other platforms: take a release binary from
# https://github.com/longbridge/longbridge-terminal/releases
longbridge --version
longbridge auth login
longbridge auth status
```

The analysis tier needs the MCP server instead:

```bash
claude mcp add --transport http longbridge https://mcp.longbridge.com
claude mcp list
```

Tick the Trade permission during either login only if you want account-tier actions (positions, orders, watchlist). Quote permission is enough for market data, and four analysis-tier skills need nothing more.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| longbridge | 4,310 | Entry point for any ticker question: routes to live quotes, news, filings, fundamentals and portfolio data, and declares itself the preferred skill for stock and market queries across US, HK, CN and SG |
| longbridge-quant | 4,084 | Quant frameworks: pairs trading and cointegration, volatility regime strategies, seasonality, multi-factor IC/IR models, ADF and GARCH statistics, hedging, walk-forward testing and sklearn ML strategies |
| longbridge-technical | 3,991 | Technical analysis: candlestick patterns, Ichimoku, RSI/MACD/EMA/Bollinger, harmonic patterns, Elliott Wave, Chan theory, smart money concepts and turtle signals with ATR sizing |
| longbridge-portfolio | 3,871 | Account assets, positions, P&L, cash flow, margin ratios, buy power, order placement and DCA, plus portfolio diagnosis, rebalancing, asset allocation, VaR and tax-loss harvesting frameworks |
| longbridge-earnings | 3,806 | Pre-earnings preview and post-earnings review, delivered as a fast in-chat summary card or a full Markdown research report covering beat/miss, segments, margins and guidance |
| longbridge-derivatives | 3,772 | Options chains, option quotes and volume, Greeks, implied volatility, and HK warrants and CBBCs with issuer lists |
| longbridge-watchlist | 3,640 | Watchlist groups, price alerts and community sharelists, with a preview then confirm protocol on every create, rename, delete, add or remove call |
| longbridge-research | 3,569 | Analyst ratings, consensus targets, EPS forecasts, insider Form 4 trades, short interest, fund holders, plus coverage initiation, investment proposal and competitive analysis frameworks |
| longbridge-value-investing | 3,361 | Graham NCAV and net-net screens plus Buffett moat, ROE and FCF analysis, as single stock diagnostics or batch screening, with cross-statement reconciliation before scoring |
| longbridge-fundamentals | 3,355 | Statements, business segments, dividends, PE/PB/PS multiples, industry comparison, corporate actions, DCF models and value screens |
| longbridge-market-data | 3,306 | Quotes, K-lines, order book depth, trade ticks, capital flow, market temperature, FX, IPO calendar, ADR premium, market maker participants and WebSocket subscriptions |
| longbridge-intel | 3,217 | Screener and popularity rankings, top movers, quote anomalies, index and ETF constituents, morning briefs, catalyst monitoring, ETF fund flows and sector rotation |
| longbridge-content | 3,128 | News, regulatory filings, community topics, and SEC EDGAR analysis of 10-K, 10-Q, 8-K, proxy and Form 4 documents |

The remaining 121 indexed listings range from 2 to 584 installs. They are the retired per-command skills from the pre-2.0 release that the README describes as the old 127-skill version: longbridge-subscriptions (584), longbridge-kline (575), longbridge-quote (568), longbridge-etf-analysis (557) and so on down through longbridge-quant-stats (494) and longbridge-ark-analysis (442), plus turtle-signal (170) and longbridge-core (2). None of the 121 has a directory in the current tree, so an install today gets 13 skills, not 134. Most of them survive as reference files inside the consolidated skills instead: 95 of the 121 names still match a `references/` basename, for example longbridge-news at `skills/longbridge-content/references/news.md`, longbridge-catalyst-radar at `skills/longbridge-intel/references/catalyst-radar.md` and longbridge-valuation at `skills/longbridge-fundamentals/references/valuation.md`.

## Why This Matters for Hermes Agents

A trading or research question usually arrives as one sentence and needs four or five different data sources behind it. Without a skill, a Hermes session either guesses a number or burns turns inventing HTTP calls. Here the routing is decided for it: any ticker mention lands on `longbridge`, which picks the CLI subcommand, and the CLI returns JSON that the agent can parse rather than scrape. `longbridge quote NVDA.US --format json` and `longbridge kline NVDA.US --period day --count 5 --format json` are stable, self-documenting entry points, and every subcommand answers `--help`.

The frameworks are the second gain, and they are the part a base model does badly. Chan theory buy and sell points, Elliott Wave counts with Fibonacci validation, Graham net-net thresholds, Brinson attribution and VaR/CVaR are all specified in `references/` files with the intermediate steps written out, so the agent follows a stated method instead of producing a plausible-sounding narrative. That is auditable in a way freeform analysis is not.

The third is that the account tier is honest about being dangerous. `longbridge-portfolio` documents that `order` is dry run by default and only places the order when the identical command is re-run with `--execute <CODE>` after confirmation, that `dca create` has no dry run at all and takes effect immediately, and that `fund submit-order` needs `--yes` and an interactive prompt otherwise. `longbridge-watchlist` enforces the same preview then confirm sequence on every mutation. An agent working in a brokerage account needs exactly this kind of written stop, and it is in the skill rather than in the harness.

One caution shapes how you deploy it: the trigger surface is aggressive. `longbridge` declares itself preferred for any securities analysis, any ticker in any language, and any portfolio query, and the 13 descriptions carry long bilingual trigger lists. On a machine that also runs general research or finance skills, expect this family to win routing contests, so install it deliberately rather than alongside a competing market-data suite.

## Usage

| You say | What happens |
|---|---|
| "What is NVDA trading at right now?" | Routes to `longbridge-market-data` and runs `longbridge quote NVDA.US --format json`, returning last price, change and volume with a Longbridge source line |
| "How is my portfolio doing this month?" | Routes to `longbridge-portfolio`, needs Quote permission for `portfolio` and Trade permission for `positions`, and can add a diagnosis or attribution pass on request |
| "Is GOOG expensive against its own history?" | Loads the valuation reference from `longbridge-fundamentals`, pulls multiples, and compares against the historical band instead of quoting a single PE |
| "Compare AAPL vs MSFT vs GOOG growth" | Pulls three fundamentals sets and builds the cross-stock comparison, with peer comparison from `longbridge-research` when consensus numbers are needed |
| "Give me my morning briefing" | Runs the `longbridge-intel` morning brief: movers, watchlist catalysts, sector rotation and ETF flows in one pass |
| "Show me the 700.HK option chain with Greeks" | Routes to `longbridge-derivatives` for the chain, strikes, expiry, delta, gamma, theta, vega and implied volatility |
| "Add NVDA to my watchlist" | `longbridge-watchlist` previews the change, waits for explicit confirmation, then executes and reports the result |

## Verification

Confirm what the installer put on disk:

```bash
npx skills list -g | grep -i longbridge
longbridge --version
longbridge auth status
```

Read the skills before installing. All five URLs below returned HTTP 200 when checked with curl on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/longbridge/skills/main/README.md
curl -sL https://raw.githubusercontent.com/longbridge/skills/main/docs/install.md
curl -sL https://raw.githubusercontent.com/longbridge/skills/main/skills/longbridge/SKILL.md
curl -sL https://raw.githubusercontent.com/longbridge/skills/main/skills/longbridge-market-data/SKILL.md
curl -sL https://raw.githubusercontent.com/longbridge/skills/main/skills/longbridge-portfolio/SKILL.md
```

Prove the data path before trusting an answer:

```bash
longbridge quote NVDA.US --format json
longbridge kline NVDA.US --period day --count 5 --format json
longbridge watchlist --format json
```

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| longbridge-market-data | Pass | Pass | Pass |
| longbridge-quant | Pass | Pass | Pass |
| longbridge-portfolio | Pass | Pass | Warn |
| longbridge-technical | Warn | Warn | Pass |

The two Warns are specific rather than generic. Snyk scores `longbridge-portfolio` MEDIUM with rule W009, direct money access, because the skill documents order placement and DCA recurring investment behind Trade permission. Socket scores `longbridge-technical` LOW anomaly with 89 percent confidence and names the causes: optional access to private brokerage data, unpinned third-party PyPI dependencies, and a turtle-trading workflow that supports real position sizing; it also reports no exfiltration and no hidden endpoints. Gen Agent Trust Hub flags the same skill for external downloads, dynamic execution of an unshipped `scripts/signal_engine.py`, data exposure through `longbridge assets` and `longbridge positions`, and indirect prompt injection from untrusted content.

The real permission and network profile is brokerage-shaped. Every skill needs an authenticated Longbridge session: `longbridge auth login` runs an OAuth browser flow and stores the session in the CLI, and the MCP route is a hosted endpoint at `https://mcp.longbridge.com` that starts its own OAuth on first tool call. Account commands run against your live account and return real positions and P&L. Write actions live in two skills: `longbridge-portfolio` can place, replace and cancel orders, create and pause DCA plans, and submit fund orders, and `longbridge-watchlist` can add, remove, rename and delete watchlist groups, alerts and sharelists. The guardrails are in the text (dry run plus `--execute <CODE>` for orders, explicit confirmation before every watchlist mutation, `--yes` gated fund orders), and DCA has no dry run, so a wrong confirmation is a live change.

Two more behaviours to read before enabling. Some paths reach for third-party Python packages named without version pins: `pip install czsc`, `pip install smartmoneyconcepts`, `pip install statsmodels scipy arch` and `pip install scikit-learn`. And `skills/longbridge-technical/references/elliott-wave.md` tells the agent to run `python3 scripts/signal_engine.py`, which is not present in the repository, so that step cannot execute as written.

## Limitations

- The install index is roughly ten times the tree. 134 indexed listings map onto 13 skill directories, because the index still carries the retired v1 per-command skills. Installing gets the 13 current skills, and any machine upgrading from v1 needs `curl -fsSL https://raw.githubusercontent.com/longbridge/skills/main/scripts/update.sh | bash` rather than `npx skills update`, which leaves orphans that compete for triggers.
- `docs/install.md` has not fully caught up with the consolidation: its Python library table links `../skills/longbridge-chanlun`, `../skills/longbridge-smc`, `../skills/longbridge-elliott-wave`, `../skills/longbridge-quant-stats` and `../skills/longbridge-ml-strategy`, and none of those directories exists. The content moved to `skills/longbridge-technical/references/chanlun.md`, `smc.md` and `elliott-wave.md`.
- The Elliott Wave reference still calls `scripts/signal_engine.py`, and the only Python file in the repository is `skills/longbridge-earnings/scripts/collect.py`. Treat that wave engine step as unavailable until the file ships.
- The frontmatter metadata is inconsistent. `longbridge-portfolio` and `longbridge-watchlist` are marked `risk_level: mutating` but every skill, including those two, carries `tier: read`, and `longbridge-earnings` ships no metadata block at all beyond name and description.
- The CLI covers less on Longbridge US accounts. The portfolio skill states that `portfolio`, `assets`, `cash-flow` and `exchange-rate` are unsupported there in CLI 0.30.0, and that `order executions` is AP-only.
- The repository carries no description on GitHub, so there is no publisher summary beyond the README.
- Snapshot data, verified Oct 26, 2026: 108,182 combined installs across 134 indexed listings; 66 GitHub stars; MIT; last pushed 2026-10-26. Counts drift over time.

## Related

- [Hithink Finance - Tonghuashun A-Share Data Skill Setup](/hermes/skills/catalog/hithink-finance-setup) - an A-share data source that complements the CN coverage here.
- [AI Berkshire Skills - Value Investing Setup](/hermes/skills/catalog/ai-berkshire-setup) - the same Graham and Buffett methodology without a brokerage account attached.
- [Claude Trading Skills - 74-Skill Trading Workflow Setup](/hermes/skills/catalog/claude-trading-skills-setup) - a much wider, non-brokerage trading workflow library to compare against this 13-skill consolidation.
- [OKX CEX Agent Skills - Exchange Trading Suite Setup](/hermes/skills/catalog/okx-cex-agent-skills-setup) - the same exchange-account pattern for crypto instead of HK, US and A-share equities.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with Quote permission only. Re-authenticate with Trade permission when you actually need positions, orders or watchlist writes, so a misrouted request cannot reach an order path.
- Prefer `--format json` on every CLI call. The text output is for humans, and parsing it breaks on the next release.
- Treat `longbridge-portfolio` DCA commands as immediate. Orders have a dry run and `--execute <CODE>`; `dca create` does not, so require the agent to show the plan before it runs anything.
- On a machine with other finance skills installed, check the routing after install. This family claims any ticker mention and will often win, which is fine for a brokerage workflow and wrong for a general research box.
- After any v1 to v2 upgrade, run the README's reinstall script and then restart the agent session, otherwise stale `longbridge-*` skills keep firing on the triggers the new ones need.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
