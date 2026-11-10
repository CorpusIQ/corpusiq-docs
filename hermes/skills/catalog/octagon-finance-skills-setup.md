---
title: "Octagon Finance Skills - Market Data and Analyst Workflows"
description: "octagonai/skills on skills.sh: 7.2K combined installs; Octagon MCP finance skills for quotes, filings, earnings calls and ESG research"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/octagon-finance-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "octagon", "finance", "equity research", "sec filings"]
---

# Octagon Finance Skills - Setup Guide

**Source:** [octagonai/skills](https://www.skills.sh/octagonai/skills) via skills.sh - 7.2K combined installs across 20 indexed listings (7,199 exact); first seen 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 130 stars, MIT license, `main` branch, last pushed 2026-06-05, 67 `SKILL.md` files among 405 blobs, one directory per skill at `skills/<name>/` with a `references/` folder carrying the MCP setup notes
**Category:** Financial markets: quotes, filings, earnings, analyst reports and portfolio research workflows
**Quality Tier:** 🟡 Solid with caveats - MIT licensed with mostly Pass verdicts, but the sample carries seventeen Socket and twelve Snyk Warnings.

Octagon publishes these skills as the prompt layer over its own financial data API. Every listing is a thin procedure: state the metric or document you want, call the Octagon MCP server, then summarize what came back. The publisher page claims 67 skills, the skills.sh list renders 20 of them, and the tree agrees with the publisher at 67 `SKILL.md` files, so the repository is small enough that the rendered slice covers roughly a third of it.

The rendered 20 concentrate on fundamentals. Three master skills orchestrate the rest (`market-analyst-master`, `financial-analyst-master`, `earnings-analyst-master`), and underneath them sit statement retrievals, year-over-year growth variants, earnings transcript analysis, ESG scoring and one SEC filing skill. The repository goes further than the index: its README documents SEC filing analysis beyond the 10-K, separate stock performance and valuation groups, and a small prediction markets pair for Kalshi, and only one of the SEC skills appears in the rendered 20. Last push was 2026-06-05, about five months before this snapshot, which is worth knowing before you point an agent at a schema-sensitive data source.

## Installation

The README's skills route installs the whole collection, with package manager variants underneath it:

```bash
npx skills add OctagonAI/skills
```

```bash
bunx skills add OctagonAI/skills
pnpm dlx skills add OctagonAI/skills
```

Claude Code users install by skill name, and a manual install is a folder copy:

```
/plugin install <skill-name>
```

The listing pages name one skill at a time if you would rather start narrow:

```bash
npx skills add https://github.com/octagonai/skills --skill commodities-quote
```

The skills do nothing without the Octagon MCP server, which needs an API key from the Octagon account portal: sign up, open API Keys from the left menu and generate one. The README's Cursor setup is the shortest form of the wiring:

```
env OCTAGON_API_KEY=<your-api-key> npx -y octagon-mcp
```

For Claude Desktop the same server goes into the client config:

```json
{
  "mcpServers": {
    "octagon-mcp-server": {
      "command": "npx",
      "args": ["-y", "octagon-mcp@latest"],
      "env": {
        "OCTAGON_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

`npx` is the only prerequisite the README lists, and it arrives with Node.js. Each installed skill also ships `references/mcp-setup.md`, so the setup instructions travel with the skill rather than living only in the repository README.

## What It Provides

The threshold for this guide is zero installs, so every indexed listing appears below:

| Skill | Installs | Use For |
|---|---|---|
| commodities-quote | 829 | Real-time commodity price quotes with day ranges and moving averages across energy, metals and agriculture. |
| stock-quote | 693 | Real-time stock quote: price, day range, 52-week range, volume, market cap and moving averages. |
| forex-list | 528 | Lists actively traded currency pairs by category (majors, crosses, exotics) for forex research. |
| market-analyst-master | 419 | Orchestrates the stock performance and market data skills for market reports, valuation comparisons and technical or sentiment analysis. |
| financial-metrics-analysis | 366 | Year-over-year growth across income statement items and financial metrics, compared across fiscal periods. |
| commodities-list | 338 | Catalog of tradable commodities across energy, metals and agriculture, with market participants and sector coverage. |
| financial-analyst-master | 330 | Orchestrates the financial statement and ratio skills for full company analysis, initiation reports and due diligence. |
| cash-flow-statement | 312 | Cash flow statement data: operating, investing and financing flows, free cash flow and cash position. |
| earnings-call-insights | 310 | Extracts forward guidance, strategic priorities and management commentary from earnings transcripts. |
| balance-sheet | 303 | Balance sheet data: assets, liabilities, equity and net debt for capital structure and leverage analysis. |
| earnings-call-analysis | 303 | Analyzes transcripts for guidance, strategic focus and supply chain signals, and drafts follow-up questions. |
| esg-ratings | 284 | ESG scores including MSCI ratings, Sustainalytics risk and industry rank for a public company. |
| sec-10k-analysis | 279 | Pulls key metrics, risk factors, business overview and MD&A from 10-K annual filings. |
| earnings-analyst-master | 275 | Orchestrates the earnings skills for transcript analysis, guidance tracking and earnings research reports. |
| analyst-estimates | 274 | Analyst revenue and EPS estimates with low, high and consensus ranges plus coverage counts. |
| esg-benchmark-comparison | 273 | Sector-level ESG benchmarks across MSCI, S&P Global, CDP and CSRD frameworks for peer comparison. |
| income-statement | 272 | Income statement figures: revenue, net income and diluted EPS for scale and trend comparison. |
| cash-flow-growth | 272 | Year-over-year growth in operating cash flow, free cash flow and net cash flow. |
| financial-growth | 270 | Comprehensive YoY growth across revenue, gross profit, operating income, net income, EPS and free cash flow. |
| financial-health-scores | 269 | Altman Z-Score and Piotroski Score for bankruptcy risk, financial strength and credit quality screening. |

All 20 indexed listings clear the zero-install threshold, and none fall outside the table. The rendered list is a third of the repository, so the SEC, valuation and prediction market skills documented in the README are installable but not shown here.

The pull is at the edges of the table rather than the middle. Commodity and stock quotes, plus the forex listing, account for 2,050 of the 7,199 installs, which suggests people arrive looking for a price and then stay for the fundamentals. The three master skills sit in the middle of the range at 419, 330 and 275 installs, and the diff between them is scope rather than quality: one orchestrates market data, one orchestrates statements, one orchestrates transcripts.

One structural detail is worth noticing before you install. `financial-metrics-analysis` and `financial-growth` overlap heavily, and the README lists a third sibling, `income-statement-growth`, that the index does not carry. Pick one growth skill per question rather than stacking them, or the agent will produce three slightly different year-over-year figures in one answer.

## Why This Matters for Hermes Agents

Financial questions are where a plausible answer is most expensive. A model asked for a company's free cash flow will produce a number with a decimal point and no source, and the number will look exactly like a real one. These skills push the agent toward a data call with a named metric instead of a recollection, which is the only structural fix for that failure.

The second thing they add is the vocabulary of the domain in the right order. `cash-flow-statement` asks for operating, investing and financing flows plus free cash flow; `cash-flow-growth` asks for the growth rates of those same lines; `financial-health-scores` asks for Altman Z and Piotroski rather than a generic health claim. An agent working without them tends to collapse revenue and net income into one "financials" step and then reason from the wrong base.

The transcript skills are the most useful edge. Earnings calls are where guidance, capital allocation and competitive positioning live, and `earnings-call-insights` and `earnings-call-analysis` both convert a transcript into guidance items, strategic priorities and follow-up questions with attribution. That is a structured task an agent can do well, given a transcript and a rule about citing management rather than paraphrasing them into the analyst's voice.

The dependency is the caveat. Every figure comes from Octagon's API, so accuracy and latency are the vendor's, and the skills themselves carry no reconciliation step against the filed document.

## Usage

| You say | What happens |
|---|---|
| "What is NVDA trading at?" | Stock quote returns price, day range, 52-week range, volume, market cap and moving averages for the ticker |
| "Compare gross margins for these three companies over four years" | The statement and growth skills pull income statement lines and their year-over-year changes, then the master skill organizes the comparison |
| "Summarize forward guidance from the last earnings call" | Earnings call insights extracts guidance, strategic priorities and management commentary, with the management commentary attached |
| "What are the risk factors in this 10-K?" | SEC 10-K analysis pulls risk factors, business overview, key metrics and MD&A from the annual filing |
| "Score this company on financial health" | Financial health scores returns Altman Z-Score and Piotroski Score with the inputs behind each |
| "How does this company's ESG rating compare with its sector?" | ESG ratings returns MSCI and Sustainalytics scores, and the benchmark skill places them against sector peers |
| "What are analysts estimating for revenue next year?" | Analyst estimates returns low, high and consensus revenue and EPS figures with coverage counts |

## Verification

Each listing resolves to a raw `SKILL.md` one directory below `skills/`. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/octagonai/skills/main/skills/stock-quote/SKILL.md | head -6
```

It should open with frontmatter holding `name: stock-quote`, then a `# Stock Quote` heading and a `## Prerequisites` section that points at `references/mcp-setup.md`. That reference file is the practical test: a directory with `SKILL.md` and no `references/` folder is an incomplete install.

After an install, confirm the skill landed as a directory holding `SKILL.md`:

```bash
ls -d ~/.claude/skills/*/ | head -20
test -f ~/.claude/skills/stock-quote/SKILL.md && echo ok
```

Then confirm the data path rather than the file: ask the agent for a quote on a ticker you can check independently. A skill that installs but cannot reach the MCP server returns a described procedure with no numbers, which is easy to spot on a question with a known answer.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| commodities-quote | Pass | Warn | Pass |
| stock-quote | Pass | Warn | Pass |
| forex-list | Pass | Warn | Warn |
| market-analyst-master | Pass | Warn | Pass |
| financial-metrics-analysis | Pass | Warn | Warn |
| commodities-list | Pass | Pass | Pass |
| financial-analyst-master | Pass | Warn | Pass |
| cash-flow-statement | Pass | Warn | Warn |
| earnings-call-insights | Pass | Warn | Warn |
| balance-sheet | Pass | Warn | Warn |
| earnings-call-analysis | Pass | Warn | Pass |
| esg-ratings | Pass | Warn | Warn |
| sec-10k-analysis | Pass | Warn | Warn |
| earnings-analyst-master | Pass | Pass | Pass |
| analyst-estimates | Pass | Warn | Warn |
| esg-benchmark-comparison | Pass | Warn | Warn |
| income-statement | Pass | Warn | Warn |
| cash-flow-growth | Pass | Pass | Pass |
| financial-growth | Pass | Warn | Warn |
| financial-health-scores | Pass | Warn | Warn |

Agent Trust Hub passes all 20 listings. Socket warns on 17 of 20 and Snyk on 12, which is the heaviest warning load of any guide in this batch, and no listing fails outright. The warnings are the reason the tier line carries a caveat rather than a clearance.

The practical risk is not code execution, because these skills retrieve data rather than edit code. It is data and money. Every call goes to Octagon's API with your key, so the questions you ask and the companies you research are visible to that vendor, and usage is billed against your account. A loop that pulls quotes for a 500-name universe is a bill, not just a query.

The output side deserves the same care. Figures arrive from the vendor, not from the filing, and a number that reaches a model without a source label will be repeated without one. Ask where each number came from, or reconcile anything material against the SEC filing before it leaves your desk. Treat the master skills as research organizers, not as a substitute for the primary document.

## Limitations

- Snapshot data, verified 2026-11-09: 7,199 combined installs across 20 indexed listings; 130 GitHub stars; MIT license; last pushed 2026-06-05. Counts drift over time.
- The skills.sh source page renders at most 20 listings against the publisher's 67, so the SEC, stock performance, valuation and prediction market groups documented in the README are absent from this table.
- Last push was 2026-06-05, roughly five months before this snapshot. Financial data schemas and prediction market endpoints change faster than that, so check the vendor's current API before relying on a field name from a skill body.
- Every listing needs an Octagon API key and network access to the Octagon MCP server. There is no offline mode, and account limits, entitlements and pricing are the vendor's, not the skill's.
- The skills carry no reconciliation against primary filings. Figures are vendor-sourced and can differ from the 10-K or 10-Q because of restatements, adjusted metrics or timing.
- Socket warns on 17 of 20 sampled listings and Snyk on 12. Nothing fails, but the warning rate is high enough that a blanket approval of the suite is not supported by these verdicts.

## Related

- [Finance Skills - Financial Analysis for Agents Setup](/hermes/skills/catalog/finance-skills-setup)
- [Awesome Finance Skills - Market Analysis Pack](/hermes/skills/catalog/awesome-finance-skills-setup)
- [Claude Trading Skills - 74-Skill Trading Workflow Setup](/hermes/skills/catalog/claude-trading-skills-setup)

## Pro Tips

- Start with a master skill and one retrieval skill you have verified, then widen. The orchestrators route to siblings, and a broken sibling shows up as a missing section rather than an error.
- Ask for units and the as-of timestamp in the prompt. Quote and statement skills return whatever the vendor sends, and a price without an as-of time is unusable in a memo.
- Keep one growth skill per analysis. `financial-metrics-analysis`, `financial-growth` and the unindexed `income-statement-growth` all compute overlapping year-over-year figures, and stacking them produces three different answers.
- Check `references/mcp-setup.md` inside an installed skill before debugging credentials. It carries the client-specific wiring, and a wrong env var name is the usual cause of an empty result.
- Reconcile anything material against the filing. The transcript and statement skills are good at extracting and bad at auditing, so use `sec-10k-analysis` or the filing itself as the second source on any number that goes into a decision.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
