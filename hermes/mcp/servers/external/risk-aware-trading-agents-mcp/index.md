---
title: "Risk-Aware Trading Agents MCP - A Refereed Market"
description: "Driven locally: 21 tools on a frozen 2026 market, a look-ahead check that reruns the strategy across three cut dates, and a result that loses to SPY"
category: "Finance / Research"
stars: "n/a on GitHub at time of reading (registry io.github.jackson-cmd/risk-aware-trading-agents 0.7.2, MIT, PyPI 0.7.2)"
added: 2026-11-13
source: "the submission queue entry #7288, the official registry record io.github.jackson-cmd/risk-aware-trading-agents 0.7.2 published 2026-11-13T16:48:55Z, and a local install on this host: uvx unpacked the PyPI wheel and thirteen tools/call requests were driven over stdio JSON-RPC"
relevance: ★★★
tags: [trading, backtesting, look-ahead, point-in-time, sec-filings, vix, research, local, stdio, mcp]
last_updated: "2026-11-13"
---

# Risk-Aware Trading Agents MCP

**A backtest that cannot lose is usually a backtest that saw tomorrow. The useful number is not the return, it is the proof that the decision was made before the news arrived.**

Almost every trading MCP server this catalog has read returns signals, prices or broker positions. This one ships a frozen copy of the 2026 US market and a referee: it reruns a strategy with every price and headline after a chosen cut date replaced by random ones, and reports whether the decisions up to that cut changed. If they changed, the strategy was reading the future, and the tool says so instead of printing a Sharpe ratio.

It also publishes its own losing result, which is rarer still.

```
Server type: Local (stdio)
Install:     uvx --python 3.12 risk-aware-trading-agents mcp
Transport:   JSON-RPC 2.0 over stdin/stdout
Auth:        none; no tool can place a real order
Server name: riskaware (serverInfo version field is an empty string), protocol 2025-06-18
Tools:       21, read from a live tools/list, plus prompts and resources capabilities
Built by:    jackson-cmd, MIT, PyPI 0.7.2
Registry:    io.github.jackson-cmd/risk-aware-trading-agents 0.7.2, published 2026-11-13T16:48:55Z
Bundled data: daily bars 2024-01-02 to 2026-11-11, 719 trading days, 63 stocks, 25 ETFs, four VIX indices
```

## The evidence tier

This server was installed and driven on this host on 2026-11-13 between 18:00Z and 18:25Z. `uvx` resolved `risk-aware-trading-agents` **0.7.2** from PyPI, the server completed `initialize` on protocol `2025-06-18` with tools, prompts and resources, `tools/list` returned **21** tools, and **thirteen** `tools/call` requests were driven over stdio. Four of them returned a result in the `-32000` range of behaviour: one refused a strategy name, one refused a date outside the bundle, one refused a missing argument, and one measured an experiment end to end.

## Why This Matters for Operators

An operator asking an agent about markets gets one of three answers: a price, an opinion, or a number that came from a backtest nobody checked. The third is the dangerous one, because it is reproducible-looking and almost never measured for look-ahead bias.

This surface is useful for a different reason than the usual market-data server. It is a **testing harness**: the data is frozen and hash-stamped, the decision point is defined as the close, the fill is the next open, and the look-ahead check is part of the result rather than an option. That makes it the rare finance server whose output can be cited - an experiment record with a run id, a manifest and a verdict.

## The frozen market, and what ships with it

`research_guide` states the terms rather than leaving them to be inferred:

- **Bars**: 2024-01-02 to 2026-11-11, **719 trading days**. 2026 is the test year; the two years before it exist to warm up slow indicators such as EMA200.
- **Universe**: 63 stocks and 25 ETFs, four volatility indices (`^VIX9D`, `^VIX`, `^VIX3M`, `^VVIX`) and four cross-asset series (gold, oil, dollar, bitcoin), with named universes - megacap 56, tech 18, defensive 20, core, sectors, ETF.
- **News**: 2026 headlines (titles only) and SEC 8-K filings, replayed through the same relevance filter and cross-verification used in live trading.
- **Provenance**: the data ships inside the package, so an experiment never touches the network, and each record carries the **SHA-256** of the data it ran on.
- **Protocol**: decision after the close, orders filled at the next day's open plus slippage, prices total-return, uninvested cash earns the T-bill ETF's daily return.

The last point matters for repeatability: the same experiment on another machine returns the same numbers, which is the whole point of a citable record.

## Everything known at one close

`market_day(day="2026-11-10")` returned the state a strategy would have seen that evening, with the boundary printed: `after the close of 2026-11-10 (16:00 New York); orders fill at the next open, 2026-11-11`.

| Reading | Value that day |
|---|---|
| Regime | `UNCERTAIN`, "hold, buy only at strong support" |
| Risk score | 33.12 |
| SPY close | 749.92, one-day -0.368%, twenty-one-day -3.62% |
| VIX / VIX9D / VIX3M | 19.46 / 18.54 / 20.64, ratio 0.9428, contango |
| VVIX | 96.63 |
| Sector breadth above EMA200 | 72.7% |
| Credit z-score | -1.65 |
| Event that day | CPI inflation report, PPI three days out |
| AAPL close | 348.51, EMA200 305.67, RSI(2) 59.22, 14.0% above EMA200 |

The news block is the part worth reading closely: it declares its own visibility window - `items at or after the close count from the next day` - and then lists four stories for AAPL classified by evidence, an SEC 8-K marked `PRIMARY`, two Benzinga items marked `UNCONFIRMED` and one opinion piece. A strategy that treats an unconfirmed headline as a signal is making a choice the data makes visible.

**The chain was checked by hand across two calls.** `2026-11-10` reported SPY 749.92 with a one-day return of -0.368%, which implies a prior close of 752.69; `market_day(day="2026-11-09")` returned SPY 752.69 with a one-day return of +2.366%. The two days reconcile to the cent, so the return fields and the price fields are drawn from the same series.

## The look-ahead check, which is the reason to use it

`run_experiment(strategy="rsi2", start="2026-01-02", end="2026-11-10")` ran 215 decision days over 56 megacap stocks with news replayed for 56 of 56 symbols and returned a saved record, `20261113-110325-rsi2-news`, with the verdict attached:

| | Strategy | SPY | Equal weight |
|---|---:|---:|---:|
| Total return | +6.1% | +10.6% | +10.3% |
| Annualized | +7.2% | +12.6% | +12.2% |
| Volatility | 14.6% | 14.0% | 11.4% |
| Sharpe | 0.31 | 0.66 | 0.75 |
| Max drawdown | -10.4% | -8.9% | -7.2% |

Trades: 516 orders, 254 closed round trips, win rate 66.5%, profit factor 1.19, average holding 5.55 trading days, average exposure 66.4%. Against SPY: beta 0.72, alpha **-2.2% a year**, excess return -4.8% a year with a 95% interval of -32.5% to +19.4%, information ratio -0.42, t-statistic -0.39, and a block bootstrap (2,000 resamples, blocks of 5 days) putting the probability that this strategy's Sharpe is above SPY's at **33%**.

**The strategy loses, and the server says so in its own report.** A surface that would happily print +6.1% and stop is a marketing tool; this one prints the benchmark row beside it and a confidence interval under it.

The `leak_check` block is the referee at work:

| Cut after | Decision days compared | Same decisions? |
|---|---:|---|
| 2026-04-07 | 65 | yes |
| 2026-06-24 | 119 | yes |
| 2026-09-10 | 173 | yes |

`verdict: pass`, with the meaning stated in the payload: with every price and headline after each cut day replaced by random ones, the strategy made exactly the same decisions up to the cut, so it does not see the future. A strategy that peeks fails this by construction, because the randomized tail changes the decisions it made earlier.

## Guardrails the risk manager applies

The experiment reports what it **refused**, not only what it bought: `refused: {"max positions": 106}` on a strategy that wanted more concurrent positions than the ceiling of ten. Execution defaults are declared in the record - long only, no leverage, market orders at the next open, sells before buys, 5 bps slippage, a $100,000 start, a 30% cash floor in the vendor's own description. `strategy_guide` adds the code-level rules that make the check meaningful: no dates in the code, no tickers in the code, no files, network, `eval`, `exec` or private attributes, and `ctx` holds nothing after `ctx.day`.

That last rule is the design decision worth copying: look-ahead is prevented by the shape of the API, and then checked anyway.

## What a strategy author gets

Sixteen strategies ship on day one - `risk_aware`, `buy_and_hold`, `ema_bounce`, `rsi2`, `golden_cross`, `momentum_rotation`, `donchian_breakout`, `bollinger_reversion`, `fear_greed_dca`, `aggressive_calls`, `wheel`, and four swing variants. `backtest_code` accepts a `Strategy` subclass written by the caller, `run_experiment` saves the run, `list_experiments` lists runs and trading sessions, and `experiment_report` returns a markdown report ready to paste, as the section above demonstrates. `trading_session_start` and `trading_session_step` let an agent trade the same frozen market one decision at a time.

`market_regime` also works against live data: on 2026-11-13 it returned `UNCERTAIN` with VIX 19.63, a fear and greed reading of 32.4 labelled "fear", 73% sector breadth, SPY trend mixed, and the next four scheduled events (PPI that day, jobs report 2026-12-04, FOMC 2026-12-09, CPI 2026-12-10). The regime is the same word the frozen market used, which makes the live and frozen surfaces comparable.

## Setting it up in Hermes

```bash
hermes mcp add riskaware --command "uvx --python 3.12 risk-aware-trading-agents mcp"
hermes mcp test riskaware
```

The first launch unpacks dependencies (pandas, numpy, matplotlib, yfinance, bs4, feedparser), so allow a couple of minutes. The CLI itself is `risk-aware-trading-agents`, with `init`, `doctor`, `regime`, `calendar`, `news` and `mcp` subcommands and a `--profile conservative|balanced|aggressive` switch; its help output is bilingual and defaults to both languages, so pass `--lang en` if the interface matters.

## Defects and frictions recorded

- `serverInfo` has name `riskaware` and an **empty** `version` string, so a client that reports versions from `initialize` reports nothing while the registry and PyPI both say 0.7.2.
- `market_day` takes `day`, not `date`. A wrong key returns a pydantic validation trace (`1 validation error for market_dayArguments`) rather than a sentence a model can act on.
- `run_experiment` with an unknown strategy returns **`ok: false` inside a successful result** rather than `isError: true`, so a client that only checks the error flag will treat the refusal as an answer. The message itself is complete: it lists the sixteen built-ins and the file and module forms it accepts.
- A date outside the bundle is refused cleanly: `2027-01-04 is outside the bundled data (2024-01-02 to 2026-11-11)`.
- The bundle ends at 2026-11-11, two days before this reading, so "today" is not in the frozen market by design.

## Where this sits in the catalog

This is the first research-harness entry in the external catalog rather than a data-feed entry. It does not compete with a market-data connector: it answers whether a rule survives contact with a market where the future was withheld, and it keeps the receipt. The nearest existing surfaces cover prices and news; none of them carries a look-ahead verdict.

### Is this investment advice?

No, and the server says so in its own instructions and in the report footer: nothing here is investment advice and no tool can trade a real account. The broker integrations named in the package description require the caller's own credentials, and the paper-trading tools act on simulated accounts.

### Does the look-ahead check guarantee a strategy is sound?

It guarantees one narrow thing, which is what makes it worth publishing: the decisions up to each cut do not depend on data after that cut. It does not correct an overstated story, a survivorship-biased universe or an over-fitted parameter, and the bootstrap interval in the same record is the honest companion to the verdict.

### Can it be used without an account or a key?

Yes. The frozen market ships inside the package, and the thirteen calls driven here needed no credential. Only the broker-backed paths would need one, and they were not touched.
