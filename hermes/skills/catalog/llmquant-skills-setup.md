---
title: "LLMQuant Skills - Quantitative Finance Workflows"
description: "llmquant/skills: 18 quantitative finance skills for equities, options, macro, crypto and portfolio work on LLMQuant Data - 9.4K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/llmquant-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "quantitative finance", "options", "portfolio"]
---

# LLMQuant Skills - Quantitative Finance Workflows

**Source:** [llmquant/skills](https://www.skills.sh/llmquant/skills) via skills.sh - 9.4K combined installs across 18 indexed listings; first seen Nov 21, 2026 (Nov 21, 2026 morning sweep)
**GitHub:** [LLMQuant/skills](https://github.com/LLMQuant/skills) - 248 stars, MIT license, master branch, last pushed May 30, 2026; a skill catalog where each `skills/llmquant-<category>/` folder holds a router SKILL.md that indexes workflow files, plus Claude Code, Codex and Cursor plugin manifests.
**Category:** Quantitative Finance and Investment Research
**Quality Tier:** 🟡 Yellow - 18 of 18 skills sampled; every skill passes Gen Agent Trust Hub and Socket, with Snyk Warn on 2 (llmquant-prediction-markets, llmquant-events).

LLMQuant Skills is the workflow layer for LLMQuant Data, an MCP server that feeds prices, filings, 13F holdings, macro snapshots, ETF holdings and crypto data to agents. It ships 18 category skills across equities, options, macro, crypto, credit, rates, FX and portfolio work, with 9.4K combined installs across 18 indexed listings and 248 GitHub stars. Each category folder is a router: one SKILL.md that indexes the workflows under it and enforces an evidence contract so every claim is grounded in LLMQuant Data rather than recited from memory.

The install unit is the category folder, not a single SKILL.md, so an agent loads the router for the asset class in play and then the specific workflow file it needs. Without the llmquant-data MCP server connected, the workflows still run as reusable procedures, but the agent asks for user-provided data and labels anything missing. First seen in the Nov 21, 2026 morning sweep.

## Installation

Install via the skills CLI, which auto-detects the host across Claude Code, Codex, Cursor, Antigravity, OpenClaw and Hermes:

```bash
npx skills add LLMQuant/skills              # pick skills interactively
npx skills add LLMQuant/skills -g --all     # install all category skills globally
npx skills add LLMQuant/skills -g --skill llmquant-options llmquant-equities
npx skills add LLMQuant/skills -a codex     # target a specific agent
```

Manage installed skills with `npx skills list`, `npx skills update` and `npx skills remove`. The repository is also packaged as a single plugin for Claude Code:

```text
/plugin marketplace add LLMQuant/skills
/plugin install llmquant-skills@llmquant
```

To connect the data feed, add the LLMQuant Data MCP server with an API key and point it at the @llmquant/data-mcp package:

```bash
claude mcp add llmquant-data -e LLMQUANT_API_KEY=your_api_key
```

Full multi-agent setup and API key instructions live in the LLMQuant/data-mcp repository and at docs.llmquantdata.com.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| llmquant-risk | 561 | fear scoring, VIX regime, hedge design and research health checks |
| llmquant-macro | 557 | macro dashboards, Fed and central-bank previews, and macro-to-portfolio impact |
| llmquant-equities | 544 | stock analysis, equity comparison, research memos and take-profit work |
| llmquant-strategies | 543 | hedge-fund playbooks: long/short, event-driven, macro, quant and multi-strategy |
| llmquant-data | 537 | SEC filings, 13F holders and macro snapshots from LLMQuant Data |
| llmquant-etfs | 535 | ETF holdings, overlap, concentration and theme exposure |
| llmquant-crypto | 528 | crypto regime, token research, perpetual funding and basis |
| llmquant-portfolio | 527 | company profiles, thesis tracking, watchlists and alerts |
| llmquant-prediction-markets | 523 | event odds, probability gaps and prediction-market arbitrage |
| llmquant-market-intelligence | 518 | macro views, market sentiment and event probability signals |
| llmquant-options | 517 | IV rank, Greeks, P&L simulation, volatility surface and strategy building |
| llmquant-events | 512 | earnings briefs, M&A tracking and regulatory risk |
| llmquant-commodities | 507 | commodity spot, futures curve, inventory and roll yield |
| llmquant-portfolio-lab | 503 | portfolio exposure maps and what-if simulators |

The remaining 4 indexed listings range from 488 to 500 installs.

## Why This Matters for Hermes Agents

Finance is a domain where an agent can sound fluent and be wrong, because every number traces back to a data source and a time window. These skills bind the workflow to LLMQuant Data: a router SKILL.md per asset class picks the right workflow and enforces an evidence contract, so claims are grounded instead of recited. That split of router plus workflows means one category folder is the installable unit, and the agent loads only the workflow it needs.

For Hermes agents, the useful pattern is coverage by asset class. Equities, options, macro, crypto, credit, rates and FX each have a router, so the agent can answer a question about option Greeks without loading the equity research path. The options router alone spans IV rank, Greeks, volatility surface, P&L simulation and backtests. The investor-lenses skill adds an overlay that reasons like named investors over the same evidence, which is a concrete way to pressure-test a thesis before committing to it. Keep in mind these are research and simulation workflows, not a live brokerage.

## Usage

| You say | What happens |
|---|---|
| What are the risks in my portfolio right now? | Runs llmquant-risk for fear scoring and VIX regime checks |
| Build me a bull put spread and show the Greeks | Runs llmquant-options to IV rank, Greeks and P&L simulation |
| Compare these five stocks | Runs llmquant-equities for equity comparison and a research memo |
| What does the Fed decision mean for my holdings? | Runs llmquant-macro for the Fed preview and macro-to-portfolio impact |
| Do these two ETFs overlap too much? | Runs llmquant-etfs to produce an overlap report |
| What are the odds this event happens? | Runs llmquant-prediction-markets to compare event odds against options pricing |
| Analyze this stock like Warren Buffett would | Runs llmquant-investor-lenses to apply the Buffett lens over LLMQuant Data |

## Verification

Review a router's instructions before installing, and confirm the file resolves on the master branch:

```bash
curl -sL https://raw.githubusercontent.com/LLMQuant/skills/master/skills/llmquant-options/SKILL.md | head -40
```

After install, run `npx skills list` to confirm the category folders landed, then ask the agent `What skills are available?` or invoke one directly with `/llmquant-options`.

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| llmquant-risk | Pass | Pass | Pass |
| llmquant-macro | Pass | Pass | Pass |
| llmquant-equities | Pass | Pass | Pass |
| llmquant-strategies | Pass | Pass | Pass |
| llmquant-data | Pass | Pass | Pass |
| llmquant-etfs | Pass | Pass | Pass |
| llmquant-crypto | Pass | Pass | Pass |
| llmquant-portfolio | Pass | Pass | Pass |
| llmquant-prediction-markets | Pass | Pass | Warn |
| llmquant-market-intelligence | Pass | Pass | Pass |
| llmquant-options | Pass | Pass | Pass |
| llmquant-events | Pass | Pass | Warn |
| llmquant-commodities | Pass | Pass | Pass |
| llmquant-portfolio-lab | Pass | Pass | Pass |
| llmquant-investor-lenses | Pass | Pass | Pass |
| llmquant-rates-fx | Pass | Pass | Pass |
| llmquant-equity-derivatives | Pass | Pass | Pass |
| llmquant-credit | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 21, 2026: 9,393 combined installs across 18 indexed listings; 248 GitHub stars; MIT license; last pushed May 30, 2026. Counts drift over time.
- These are research and simulation workflows, not a live brokerage: they analyze data from LLMQuant Data and label anything missing, so do not treat outputs as executed trades or live positions.
- Every skill is a router over workflow files; without the llmquant-data MCP server connected, the agent asks for user-provided data and labels gaps.
- The repo is on the master branch and was last pushed May 30, 2026, months before this snapshot, so the install index can outrun the current tree.
- Two of the 18 sampled skills carry Snyk Warn cells (llmquant-prediction-markets and llmquant-events); read their instructions before use.

## Related

- [VectorBT Backtesting Skills - Quant Workflow Setup](/hermes/skills/catalog/vectorbt-backtesting-skills-setup)
- [AGI Pro Trading Skills - 68 Quant and DeFi Skills](/hermes/skills/catalog/agiprolabs-trading-skills-setup)
- [Awesome Finance Skills - Market Analysis Pack](/hermes/skills/catalog/awesome-finance-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by category with --skill rather than --all, so the agent only carries the asset classes you actually use.
- Connect the llmquant-data MCP server first; without it the workflows fall back to asking you for data and labeling gaps.
- Use llmquant-options for Greeks and volatility surface reads before committing to a specific strategy.
- Run an investor lens over the same ticker as a cross-check against your own thesis.
- Treat every output as research, not a trade signal; the workflows simulate and analyze rather than execute.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
