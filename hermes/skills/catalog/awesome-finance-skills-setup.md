---
title: "Awesome Finance Skills - Market Analysis Pack"
description: "rkiding/awesome-finance-skills: 6.8K combined installs. Ten AlphaEar skills for finance news, stock data, sentiment and forecasting."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/awesome-finance-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "finance", "market data", "sentiment"]
---

# Awesome Finance Skills - Setup Guide

**Source:** [rkiding/awesome-finance-skills](https://www.skills.sh/rkiding/awesome-finance-skills) via skills.sh - 6.8K combined installs across 10 indexed listings; first seen 2026-11-01 (morning sweep)

**GitHub:** [rkiding/awesome-finance-skills](https://github.com/rkiding/awesome-finance-skills) - 3,094 stars, Apache-2.0, branch main, last pushed 2026-03-29; 10 `SKILL.md` files under `skills/<name>/`, most with a `scripts/` folder of Python tools and a `references/` folder holding `PROMPTS.md` and `sources.md`, plus `figs/` and `tests/` at the top level

**Category:** Finance research, news aggregation and market analysis skills for agents

**Quality Tier:** 🟡 Yellow - Snyk returns a Warn on the two most-installed skills (alphaear-news and alphaear-stock, codes W011 and W012) while Gen Agent Trust Hub and Socket pass on all three sampled

The README makes a large claim in its first line, promising to turn an agent into a Wall Street analyst in seconds, and then describes something narrower and more defensible: a collection of skills that give a model real-time news, stock data, sentiment scoring, logic visualisation and time-series forecasting. The news skill aggregates more than ten sources, naming Cailian, the Wall Street Journal, Weibo and Polymarket among them. The unit of work throughout is one instrument or one thesis at a time, not a portfolio view.

What makes the pack worth reading is that the eight core skills form a pipeline with real handoffs rather than a menu of unrelated tools. Search and news gather material. Stock supplies OHLCV history and fundamentals for a ticker. Sentiment scores the text, either with a local FinBERT model or by handing the agent a prompt to call an LLM with and writing the score back to the database. The predictor runs a Kronos forecast and then adjusts it against news. The signal tracker takes an existing thesis and decides whether new information strengthens, weakens or falsifies it. The logic visualiser renders the transmission chain as Draw.io XML, and the reporter clusters the signals and assembles a document. State lives in a shared SQLite database behind `scripts/database_manager.py`.

The division of labour is explicit and unusual in a pack of this kind. Several skills state outright that the agent, not a script, performs the reasoning step, and they supply the prompt to do it with: the sentiment prompt returns strict JSON with a score, a label and a short reason, the signal tracker supplies researched, analyst and tracking prompts in sequence. The scripts handle what should be deterministic, which is fetching, storing, chart configuration and XML generation. That is a more honest split than pretending a small local model does the analysis.

Two skills sit outside the README's own table of eight. `alphaear-deepear-lite` fetches pre-computed signals from a hosted endpoint, and `skill-creator` is a generic guide to writing skills, apparently carried in from the wider ecosystem the author works in; its body still refers to Codex rather than to this pack.

## Installation

The README documents a one-step CLI install per skill and a manual copy. The CLI line uses the `@` selector rather than a flag, and reproduces the repository owner in upper case:

```bash
npx skills add RKiding/Awesome-finance-skills@alphaear-news
npx skills find "alphaear"
```

The README also gives a manual route, cloning the repository and copying every skill into an agent framework's skills directory. It uses OpenCode as the example target, so translate the destination for Hermes:

```bash
git clone https://github.com/rkiding/awesome-finance-skills.git /tmp/awesome-finance-skills
cp -r /tmp/awesome-finance-skills/skills/alphaear-news ~/.hermes/profiles/corpusiq/skills/
```

The clone and copy line above is our adaptation of the documented manual step, not a Hermes-specific instruction from the project. Install one skill rather than all ten when you first try the pack, because the dependency set is heavy: `pandas`, `akshare` and `yfinance` for prices, `duckduckgo-search` and `requests` for retrieval, and `torch`, `transformers` and `sentence-transformers` for FinBERT and Kronos, with `agno` and `scikit-learn` behind the agent framework and forecasting paths. The sentiment and predictor skills download model weights on first use, so the first run is slow and needs a working path to the model hosts.

Data access has regional quirks the skills document themselves. US prices come through `yfinance`, which may need `HTTP_PROXY` and `HTTPS_PROXY` exported if the host cannot reach Yahoo Finance directly. A-share and Hong Kong data come primarily through `akshare` against EastMoney and work best on a direct connection, and the stock tool is written to detect a proxy problem and retry directly for those markets.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| alphaear-news | 1,544 | Pulling hot finance news and unified trend reports across sources such as Cailian, Weibo, Zhihu and WallstreetCN, plus summaries of active Polymarket prediction markets. |
| alphaear-stock | 1,240 | Searching A-share, Hong Kong and US tickers and returning OHLCV history plus fundamentals including sector, industry, market capitalisation and price-to-earnings. |
| alphaear-sentiment | 646 | Scoring finance text between -1.0 and 1.0 with a local FinBERT model, or handing the agent a JSON-returning prompt to score with an LLM and write the result back. |
| alphaear-predictor | 585 | Forecasting with the Kronos model and then adjusting the numbers against recent news, with an explicit caution that only trusted checkpoints belong in `exports/models`. |
| alphaear-signal-tracker | 561 | Rating an existing investment signal as strengthened, weakened or falsified as new price and news information arrives, updating confidence and intensity. |
| alphaear-search | 543 | Web search across Jina, DuckDuckGo and Baidu plus a local RAG pass over stored news, with an aggregate mode that combines engines and a cache-relevance prompt. |
| alphaear-reporter | 536 | Clustering signals, writing one section per cluster and assembling a financial report, with charts emitted as `json-chart` blocks from a visualiser script. |
| alphaear-logic-visualizer | 497 | Converting an investment thesis or transmission chain into Draw.io XML and rendering it to a viewable HTML file. |
| alphaear-deepear-lite | 335 | Fetching the latest signals, confidence scores and reasoning from the hosted DeepEar Lite endpoint, with no local database required. |
| skill-creator | 284 | A generic skill authoring guide bundled alongside the finance skills: `SKILL.md` anatomy, scripts, references and assets, and context-budget advice. |

All ten listings map to a directory in the tree, so there is no index-versus-tree gap to warn about. The two rows below `alphaear-search` are the ones the README's own table omits: `alphaear-deepear-lite` and `skill-creator`.

## Why This Matters for Hermes Agents

Most agent finance work fails on provenance rather than arithmetic. A model asked about a ticker will produce a plausible price, a plausible cause and no source, and the operator cannot tell which part came from a feed. This pack inverts that by separating retrieval from reasoning: every number has a function behind it, and the analysis step is a named prompt the operator can read before running it. When an answer is wrong you can tell whether the data was stale or the reasoning was bad, which is the only useful diagnostic.

The stateful design is the other half. Signals, news and sentiment live in a SQLite database that several skills read and write, so tracking a thesis over weeks becomes a query rather than a fresh conversation. The signal tracker is the clearest expression of that: it takes an existing signal with a confidence score and asks what new information does to it, with falsification as an explicit outcome instead of an afterthought.

For builders, the pack is also a worked example of how to wrap a domain library for an agent. Each skill names the class and method the agent should call, lists which package manager or model it depends on, and states when not to use it. Nothing is hidden behind a framework that has to be installed whole.

Two cautions belong in the prompt rather than the README. News text is untrusted input that flows into prompts, so an instruction embedded in an article is an injection vector, not just noise. And the output is research material assembled from public feeds, which is a long way from advice; the forecast skill is a model run against history, not a prediction you should size a position on.

## Usage

| You say | What happens |
|---|---|
| "What is moving in A-shares this morning" | `alphaear-news` pulls hot items across the configured sources and `alphaear-stock` adds price and volume for the names it surfaces. |
| "Give me the last quarter of daily prices for 600519" | `alphaear-stock` resolves the ticker, returns OHLCV as a frame with dates in `YYYY-MM-DD`, and can add fundamentals such as sector and market cap. |
| "Is this article bullish or bearish, and how strongly" | `alphaear-sentiment` scores it locally with FinBERT, or the agent applies the supplied prompt and stores the score and reason against the article record. |
| "Forecast the next seven days and adjust for today's news" | `alphaear-predictor` produces the base Kronos forecast, then the agent applies the adjustment prompt using the latest headlines and returns the revised series. |
| "Is my gold thesis still holding after this week" | `alphaear-signal-tracker` compares new information against the thesis and returns strengthened, weakened, falsified or unchanged with a revised confidence. |
| "Draw how a rate cut reaches bank margins" | `alphaear-logic-visualizer` generates Draw.io XML for the transmission chain and renders it to an HTML file you can open. |
| "Turn these signals into a report" | `alphaear-reporter` clusters the input, writes a section per cluster, assembles the document and adds chart configurations. |

## Verification

The raw path for the news skill returned HTTP 200 on branch main when this guide was written on 2026-11-01:

```bash
curl -sL -o /dev/null -w "%{http_code} alphaear-news\n" \
  https://raw.githubusercontent.com/rkiding/awesome-finance-skills/main/skills/alphaear-news/SKILL.md
```

Expect `200`. After the clone, confirm that the tree holds ten skills and that the one you are installing carries its scripts and the sources reference the entrypoint relies on:

```bash
find /tmp/awesome-finance-skills/skills -name SKILL.md | wc -l
ls /tmp/awesome-finance-skills/skills/alphaear-news /tmp/awesome-finance-skills/skills/alphaear-news/references
head -4 /tmp/awesome-finance-skills/skills/alphaear-stock/SKILL.md
```

The count should print 10, the listing should show `SKILL.md`, `scripts/` and `references/` with `sources.md` inside it, and the header should show `name: alphaear-stock` with a one-line `description:`. The `deepear-lite` skill ships its own smoke test, which is the cheapest way to prove the Python environment and outbound network both work:

```bash
python3 /tmp/awesome-finance-skills/skills/alphaear-deepear-lite/scripts/deepear_lite.py
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| alphaear-news | Pass | Pass | Warn |
| alphaear-stock | Pass | Pass | Warn |
| alphaear-sentiment | Pass | Pass | Pass |

Unlike a markdown-only pack, this one ships executable Python, and the two Warns sit on exactly the two skills that reach the network for market content. `alphaear-news` calls news sources and a prediction-market endpoint; `alphaear-stock` calls `akshare` against EastMoney and `yfinance` against Yahoo Finance. Snyk codes W011 and W012 are recorded on both, and the skill that only scores local text, `alphaear-sentiment`, is the one that passes clean. Read that pattern before deciding what to allow: the review surface here is outbound requests, not the prompt text.

The larger risk in this pack is what flows back in. News headlines and article bodies are attacker-influenced strings, and they end up in a SQLite table and then, via the reporter and tracker prompts, inside an LLM context. A headline that reads like an instruction is a prompt injection with a plausible delivery route, and no scanner will flag it. Treat fetched text as data, keep the score-and-summarise prompts narrow, and do not let a fetched document change what the agent does next without a human step.

Model loading deserves its own line. `alphaear-predictor` loads `.pt` checkpoints from `exports/models` using `weights_only=True` and only scans for the `kronos_news_*` pattern, and its own documentation warns that only trusted checkpoints belong in that directory. The sentiment and predictor skills also pull weights from model hosts on first run, which puts the Hugging Face supply chain in scope. Credential exposure is low: the pack needs no API keys, and the only configuration surface is proxy variables and the model path overrides. The licence is Apache-2.0, which requires you to keep the notice and state changes rather than to publish anything.

## Limitations

- Snapshot data, verified 2026-11-01: 6,771 combined installs across 10 indexed listings; 3,094 GitHub stars; Apache-2.0; last pushed 2026-03-29. Counts drift over time.
- Last push was in late March 2026, roughly seven months before this snapshot. These skills wrap live third-party sources, so an endpoint that moved since then will fail at the script rather than at the skill.
- The README's included-skills table lists 8 of the 10 directories. `alphaear-deepear-lite` and `skill-creator` exist in the tree and are indexed but are undocumented there.
- The dependency footprint is large: `torch`, `transformers` and `sentence-transformers` for the models, `akshare` and `yfinance` for prices, `agno` for the agent framework. Expect a slow first run and model downloads measured in hundreds of megabytes.
- Market data access is network-dependent and regional. US quotes through `yfinance` may need a proxy, A-share data through `akshare` works best on a direct connection, and either can fail silently into an empty frame if the source changes shape.
- Proofreading is uneven across the bodies: duplicated `## Capabilities` headings appear in two skills and duplicated section numbers in two more. Nothing breaks, but treat the documents as working notes rather than a specification.
- Output is research assembled from public feeds, not investment advice, and the Kronos forecast is a model run against history. Neither the pack nor its licence transfers any suitability judgement to you.

## Related

- [Finance Skills - Financial Analysis for Agents Setup](/hermes/skills/catalog/finance-skills-setup)
- [Finance Skills - Financial Services Suite Setup](/hermes/skills/catalog/joellewis-finance-skills-setup)
- [Hithink Finance - Tonghuashun A-Share Data Skill Setup](/hermes/skills/catalog/hithink-finance-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `alphaear-news`, `alphaear-stock` and `alphaear-search`. They carry the retrieval layer and none of the model dependencies, so you can prove the network and the database before installing torch.
- Let the agent do the scoring when accuracy matters. The sentiment skill offers a local FinBERT path and an LLM prompt path, and the prompt path is the one that can read context, sarcasm and a hedge buried in a third paragraph.
- Run the sentiment batch update after the news pull, not before. `batch_update_news_sentiment` only processes rows already in the database, so ordering decides whether a morning's headlines are scored at all.
- Keep `exports/models` under review control. The predictor loads picked tensors from that directory by pattern, and the pack's own warning about trusted checkpoints is the whole defence.
- Ask for the ticket and the date on every number. The stock tool takes explicit `YYYY-MM-DD` bounds and the tools return frames, so a request that names the window produces something auditable, while "how is it doing" produces a guess.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
