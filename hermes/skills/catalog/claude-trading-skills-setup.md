---
title: "Claude Trading Skills - 74-Skill Trading Workflow Setup"
description: "Claude Trading Skills: 233.5K combined installs. 74 skills for market regime, screening, position sizing, discipline gates and trade journaling."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-trading-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-22"
tags: ["hermes skill", "agent skill", "skill setup", "trading", "investing", "market research"]
---

# Claude Trading Skills - Setup Guide

**Source:** [tradermonty/claude-trading-skills](https://www.skills.sh/tradermonty/claude-trading-skills) via skills.sh - 233.5K combined installs across 74 indexed listings; new to this catalog in the Oct 22, 2026 sweep
**GitHub:** [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) (3,166 stars; MIT; pushed 2026-10-20; layout `skills/<name>/SKILL.md` for 94 SKILL.md files in the tree, including 20 under `examples/`, plus `workflows/`, `skillsets/` and a machine-readable `skills-index.yaml`)
**Category:** Finance / Trading Workflow
**Quality Tier:** 🟢 Production - MIT, a machine-readable skill index with verification fields, workflow manifests with sample runs, 3,166 stars, a documentation site, and Pass on Gen Agent Trust Hub and Socket for both sampled skills

This is a process toolkit for individual investors, not a signal service. The publisher says so in the README in as many words: the goal is to structure market review, risk management, trade planning, journaling and continuous improvement, and the repo is explicit that it does not place orders or act as a broker. Every skill is a Claude Skill folder with a Python implementation, and the suite is organised into eight categories from market regime to strategy research.

The structure is the interesting part. Five workflow manifests under `workflows/` name the exact skills, decision gates and artifacts in order, so a session follows a path instead of improvising: a 15-minute daily market check, a weekly portfolio review, a swing-opportunity screen that only runs when risk allows, a trade-memory loop after every closed trade, and a monthly performance review. `skillsets/` bundles those into five purpose-specific install sets, and `skills-index.yaml` describes every skill with category, status, integrations, inputs, outputs and a `verification` block.

That `verification` block is worth reading before trusting anything. Every skill in the published index currently reports `not_verified` on instruction contract, unit tests, workflow contract, end-to-end replay, data provenance, financial logic review, empirical validation and security review. The repo also ships a Quality Dashboard and an audit trail, and the skills-index is honest rather than promotional. Treat the suite as a disciplined framework, not as validated alpha.

## Installation

The skills.sh route, which is the shortest path to a Hermes agent:

```bash
npx skills add tradermonty/claude-trading-skills
```

Install only the skills a workflow needs when you want a smaller surface:

```bash
npx skills add tradermonty/claude-trading-skills --skill vcp-screener position-sizer pre-trade-discipline-gate
```

The README documents two first-party paths as well. For Claude Code, clone the repo and copy a skill folder into `~/.claude/skills/` or `.claude/skills/`; for the Claude web app, download the `.skill` asset for that skill from the latest GitHub Release, verify it against `SHA256SUMS`, then upload it under Settings, Capabilities and Customize, Skills.

The shared project environment supports Python 3.10 to 3.13; packaged standalone skills keep a Python 3.9 floor. Several skills call a market data API: the Financial Modeling Prep key covers the screeners and calendars, and `portfolio-manager` expects the Alpaca MCP server. The README notes that the basic market-regime path needs no paid API at all, which is the right place to start.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| us-stock-analysis | 5,563 | Full US equity analysis: fundamentals, business quality, valuation, technicals, comparisons, written report |
| market-news-analyst | 4,159 | Maps recent market-moving news onto equity and commodity impact |
| backtest-expert | 4,072 | Systematic backtesting guidance: what to test, overfitting control, how to score results |
| market-environment-analysis | 3,896 | Market environment report: trend, volatility, breadth and risk posture in one pass |
| technical-analyst | 3,890 | Weekly chart read for stocks, indices, crypto and forex: trend structure, levels, setups |
| portfolio-manager | 3,824 | Portfolio review over Alpaca MCP: allocation, risk metrics, position detail, diversification |
| value-dividend-screener | 3,728 | Dividend screen on P/E under 20, P/B under 2, yield above 3 percent, dividend growth consistency |
| options-strategy-advisor | 3,681 | Options strategy analysis and payoff simulation for a stated view and risk budget |
| position-sizer | 3,655 | Risk-based share size from entry, stop and account risk budget |
| macro-regime-detector | 3,624 | Detects 1 to 2 year macro regime shifts from cross-asset ratio analysis |
| canslim-screener | 3,546 | O'Neil CANSLIM growth screen over US stocks |
| institutional-flow-tracker | 3,527 | 13F ownership changes and institutional flow per stock |
| earnings-calendar | 3,497 | Upcoming earnings dates for US stocks via the FMP API |
| sector-analyst | 3,470 | Sector rotation and market cycle positioning read |
| stanley-druckenmiller-investment | 3,463 | Synthesises eight upstream skill outputs into one Druckenmiller-style position view |
| economic-calendar-fetcher | 3,449 | Upcoming macro releases and events via the FMP API |
| vcp-screener | 3,423 | Minervini volatility contraction pattern screen over the S&P 500 |
| market-breadth-analyzer | 3,407 | Breadth health score from the publisher public CSV feed |
| finviz-screener | 3,383 | Builds and opens FinViz screener URLs from plain language |
| pair-trade-screener | 3,381 | Statistical arbitrage candidate finder for pair trades |
| edge-strategy-designer | 3,365 | Turns an abstract edge concept into strategy draft variants and ticket YAML |
| scenario-analyzer | 3,362 | 18-month scenario tree from headlines with primary, secondary and tertiary impact plus stock picks |
| edge-strategy-reviewer | 3,359 | Adversarial review of a strategy draft: edge plausibility, overfitting, sample size, execution realism |
| breadth-chart-analyst | 3,357 | Reads S&P 500 breadth and uptrend ratio chart screenshots |
| earnings-trade-analyzer | 3,352 | Scores post-earnings setups on gap size, prior trend, volume, and MA200 and MA50 position |
| us-market-bubble-detector | 3,344 | Bubble risk read on a revised Minsky and Kindleberger framework |
| market-top-detector | 3,331 | Top risk heuristic from distribution days, leading stock deterioration and defensive rotation |
| uptrend-analyzer | 3,325 | Diagnoses the current environment from the uptrend ratio dashboard |
| dividend-growth-pullback-screener | 3,308 | High dividend growth names in temporary RSI-oversold pullbacks |
| theme-detector | 3,306 | Finds and analyses trending sector themes |
| data-quality-checker | 3,290 | Validates numbers and sourcing in an analysis before publication |
| ftd-detector | 3,286 | Follow-through day signals for market bottom confirmation |
| strategy-pivot-designer | 3,281 | Detects backtest stagnation and proposes structurally different pivots |
| kanchi-dividend-us-tax-accounting | 3,278 | US dividend tax and account-location workflow for income portfolios |
| edge-candidate-agent | 3,277 | Generates and ranks long-side edge research tickets from end-of-day observations |
| pead-screener | 3,264 | Post-earnings announcement drift screen on gap-up stocks |
| edge-concept-synthesizer | 3,253 | Abstracts tickets and hints into reusable edge concepts with thesis and invalidation signals |
| trader-memory-core | 3,251 | Thesis tracking from screening idea to closed position, with postmortem |
| edge-hint-extractor | 3,248 | Extracts edge hints from daily observations into a canonical hints file |
| dual-axis-skill-reviewer | 3,230 | Reviews a project's skills on deterministic checks plus LLM review findings |
| signal-postmortem | 3,207 | Records and analyses post-trade outcomes for pipeline signals |
| trade-hypothesis-ideator | 3,172 | Falsifiable trade hypotheses from market data, trade logs and journal snippets |
| exposure-coach | 3,161 | One-page market posture: exposure ceiling, growth versus value bias, breadth, entries allowed or cash |
| kanchi-dividend-sop | 3,155 | Kanchi-style dividend investing as a repeatable operating procedure |
| edge-pipeline-orchestrator | 3,141 | Runs the full edge pipeline from detection through design, review and export |
| kanchi-dividend-review-monitor | 3,135 | Review triggers on dividend portfolios that surface anomalies without auto-selling |
| edge-signal-aggregator | 3,130 | Ranks signals from several edge skills into one conviction dashboard |
| skill-designer | 3,109 | Designs new skills from a structured idea specification |
| skill-integration-tester | 3,098 | Validates multi-skill workflows: skill existence, data contracts, naming, handoff integrity |
| skill-idea-miner | 3,096 | Mines session logs for skill ideas |
| breakout-trade-planner | 3,056 | Minervini-style breakout plan from VCP output with worst-case risk and order templates |
| downtrend-duration-analyzer | 3,048 | Historical downtrend lengths as interactive HTML histograms by sector and market cap |

The remaining 22 indexed listings range from 1,547 to 2,931 installs.

The remaining 22 indexed listings range from 1,547 to 2,931 installs, and several of them are the load-bearing ones: trading-skills-navigator (2,931) picks a workflow from a plain-language goal, pre-trade-discipline-gate (2,642) blocks planless or oversized entries, drawdown-circuit-breaker (2,641) decides whether new risk is allowed today, weekly-performance-digest (2,639) writes the review, and trailing entries cover the Stockbee, Kanchi and contrarian families plus the two backtest engines (mt5-robot-tester 2,272, manifoldbt-backtester 1,623) and us-undervalued-growth-screener (1,547).

## Why This Matters for Hermes Agents

An agent runs a checklist well and forgets to run one at all. This suite exists to make the checklist the path of least resistance: regime first, then candidates, then size, then a discipline gate, then a journal entry, then a review. Each step is a skill with named inputs and outputs, so a Hermes session can be told to run a workflow and will follow the same order twice.

The publisher ships the workflow layer as data, not prose. `workflows/*.yaml` names the skills and artifacts in sequence with sample runs under `examples/`, which means a Hermes cron can read the manifest and dispatch the steps instead of a human retyping the routine. That is the same pattern as a Commander task list, expressed for a different audience.

There is also a directly relevant find for anyone running Hermes: the same author publishes a companion [Hermes Trading Research Agent work package](https://github.com/tradermonty/hermes-trading-research-agent-work-package) that packages these skills into a Hermes profile with slash-command routines such as `/pre-market-routine`, `/after-close-review` and `/trade-journal`. It states plainly that human decision gates stay central and that no orders are placed.

The honest caveat matters more than the feature list. Every verification field in the published index reads `not_verified`, the README disclaims advisory status, and the outputs are frameworks and reports rather than predictions. Wire the suite to a journal and a review, where a wrong answer costs time. Do not wire it to an execution path.

## Usage

| You say | What happens |
|---|---|
| "Run my daily market check" | The market-regime workflow chains breadth, uptrend and exposure-coach into a one-page posture with an exposure ceiling |
| "Is the market healthy enough to add risk?" | `market-breadth-analyzer` and `uptrend-analyzer` return scores, and `exposure-coach` converts them into entries-allowed or cash-priority |
| "Find swing candidates" | `vcp-screener` and `canslim-screener` return candidates, and `drawdown-circuit-breaker` decides whether the screen is even allowed today |
| "How many shares should I buy?" | `position-sizer` returns size from entry, stop and risk budget, and `pre-trade-discipline-gate` blocks the plan if it fails the checklist |
| "Review my portfolio" | `portfolio-manager` pulls holdings over Alpaca MCP and reports allocation, concentration and risk metrics |
| "What did I learn from last month?" | `trader-memory-core`, `signal-postmortem` and `weekly-performance-digest` produce the review from closed trades |
| "Was this strategy real or curve-fit?" | `backtest-expert` scores the backtest, and `edge-strategy-reviewer` argues against the draft |
| "Which workflow fits me?" | `trading-skills-navigator` recommends a workflow, skillset, API profile and setup path from the goal |

## Verification

Confirm what was installed:

```bash
npx skills list | grep -iE 'screener|position-sizer|trader-memory'
```

Read a skill before installing it, for example the backtest skill:

```bash
curl -s https://raw.githubusercontent.com/tradermonty/claude-trading-skills/main/skills/backtest-expert/SKILL.md | head -40
```

Check whether the skill you plan to run declares its data dependency:

```bash
curl -s https://raw.githubusercontent.com/tradermonty/claude-trading-skills/main/skills-index.yaml | grep -A4 'id: vcp-screener'
```

## Security

skills.sh verdicts for sampled skills (verified Oct 22, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| us-stock-analysis | Pass | Pass | Warn |
| backtest-expert | Pass | Pass | Pass |

The single Snyk warning on `us-stock-analysis` is MEDIUM W011, third-party content exposure: the workflow uses web search to gather market data and news, so unvalidated web text reaches the model. Backtest-expert is clean on all three scanners. No sampled verdict reports malware, credential handling or data exfiltration, and the suite has no execution path to a broker.

The permissions to review are data-side, not money-side. The screeners and calendars need a Financial Modeling Prep key, `portfolio-manager` needs Alpaca credentials through an MCP server, and both are read scopes that should be created as such. Keep those keys out of prompts: put them in the environment the skill's script reads, not in a chat message.

## Limitations

- The publisher marks every skill `not_verified` across the eight verification axes in `skills-index.yaml`. The suite is a framework, not a validated strategy, and the README disclaims advisory status in bold terms.
- It is built for US markets. Earnings, 13F, CANSLIM, Stockbee and Kanchi material all assume US equities, and the tax and account-location skill is explicitly US-only.
- Several skills need paid data. FMP covers the screeners and calendars, Alpaca covers portfolio review, and the README's no-paid-API path covers only the market-regime basics.
- 94 SKILL.md files exist in the tree but 74 listings are indexed, the difference being the 20 copies under `examples/weekly-trade-strategy/`.
- The suite is opinionated about method. Minervini, O'Neil and Druckenmiller patterns are presented as the way to trade, which suits a student of those methods and frustrates anyone else.
- Snapshot data, verified Oct 22, 2026: 233,532 combined installs across 74 indexed listings; 3,166 GitHub stars; MIT; last pushed 2026-10-20. Counts drift over time.

## Related

- [Coinos Skills - AiCoin Crypto Trading Suite Setup](/hermes/skills/catalog/coinos-trading-skills-setup)
- [Finance Skills - Financial Services Suite Setup](/hermes/skills/catalog/joellewis-finance-skills-setup)
- [Finance Skills - Financial Analysis for Agents Setup](/hermes/skills/catalog/finance-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `trading-skills-navigator` and answer its questions honestly. It returns a workflow and an API profile, which stops you installing 74 skills you will not run.
- Install only the six to eight skills a single workflow names. The suite is deliberately modular, and a smaller install makes the agent's skill descriptions cheaper to read.
- Run `drawdown-circuit-breaker` and `pre-trade-discipline-gate` before any screener. They are the two skills that turn a research session into a risk-managed one.
- Keep `trader-memory-core` fed from day one. The review skills are worthless without a journal, and the journal is the only artifact that compounds.
- If you use Hermes, look at the companion work package before wiring your own crons. It already expresses the daily and weekly routines as profile commands.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
