---
title: "Day1Global Finance Skills - 5-Skill Market Setup"
description: "star23/day1global-skills: 3.0K combined installs across 5 listings, five finance frameworks for US stocks, macro, tech earnings and Bitcoin."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/star23-day1global-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "finance", "investing", "crypto", "market analysis"]
---

# Day1Global Finance Skills - Setup Guide

**Source:** [star23/day1global-skills](https://www.skills.sh/star23/day1global-skills) via skills.sh - 3.0K combined installs across 5 indexed listings; first seen Nov 13, 2026 (evening sweep)
**GitHub:** 1,064 stars, MIT licence, `main` branch, last pushed 2026-08-18, five SKILL.md files at the repository root (one folder per skill, no `skills/` wrapper)
**Category:** Finance and investment analysis: US stock value, market sentiment, macro liquidity, tech earnings and Bitcoin cycle timing
**Quality Tier:** 🟡 Yellow - five in-tree skills and a clear bilingual README, but three Snyk Warns across the four sampled skills.

This five-skill suite from Day1Global (authors Ruby and Star) covers the analysis stack a finance-curious agent needs: US stock value investing, market sentiment, macro liquidity, tech earnings deep dives, and Bitcoin cycle timing. Each skill is a structured framework that produces a rating or a recommendation, not raw market data.

Every skill ships as a single SKILL.md at the repository root, one folder per skill, with no `skills/` wrapper. The README is bilingual (English and Chinese) and closes with an explicit disclaimer: these are research frameworks built on public information, not licensed investment advice.

## Installation

```bash
# Install all five skills (skills.sh auto-discovery)
npx skills add https://github.com/star23/Day1Global-Skills --all

# For Claude Code slash commands, clone and copy into .claude/skills/
git clone https://github.com/star23/Day1Global-Skills.git
mkdir -p your-project/.claude/skills
cp -r Day1Global-Skills/us-value-investing your-project/.claude/skills/
# repeat for us-market-sentiment, macro-liquidity, tech-earnings-deepdive, btc-bottom-model
```

Skills install to `.agents/skills/` and activate automatically when the conversation matches a topic. The slash-command path also works against `~/.claude/skills/` for global access; restart Claude Code afterwards to use `/btc-bottom-model`, `/us-value-investing` and the rest.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| us-value-investing | 728 | Buffett-style four-dimension value scoring (ROE, debt safety, free cash flow quality, economic moat) with 0-12 ratings and A-to-D grades. |
| us-market-sentiment | 593 | US market sentiment and position recommendations from five indicators: NAAIM, institutional allocation, retail flows, forward P/E and hedge fund leverage. |
| macro-liquidity | 571 | Global liquidity monitoring and risk early-warning from Fed net liquidity, SOFR, MOVE and yen carry trade signals. |
| tech-earnings-deepdive | 542 | Institutional-grade earnings deep dives across 16 modules and 6 investment philosophies, ending in a full investment memo. |
| btc-bottom-model | 536 | Bitcoin cycle timing with a 0-100 Market Heat Score from 13 indicators, producing buy and sell recommendations. |

No indexed listings fall below the 500-install threshold; all five appear above.

## Why This Matters for Hermes Agents

These skills give an agent a structured financial reasoning layer instead of freeform market commentary. Each one ends in a concrete output: a 0-12 value score, a sentiment rating with a position recommendation, a liquidity warning, a full investment memo, or a 0-100 Bitcoin heat score.

The value is the method, not the data. us-value-investing scores four dimensions against an explicit rubric, so the answer is reproducible and auditable rather than a vibe. tech-earnings-deepdive pins down evidence tiers and anti-bias checks before it lets the agent reach a verdict.

The models are also composable. The README's synergy table pairs tech-earnings-deepdive with us-value-investing for cross-validation, and with macro-liquidity when liquidity is a key force in an earnings call.

The honest caveat is the one the README prints: these are research frameworks, not investment advice, and they do not fetch live market data for you. An agent still needs the raw indicator values to score against.

## Usage

| You say | What happens |
|---|---|
| "Is AAPL worth holding long-term?" | Runs us-value-investing and returns a four-dimension score with an A-to-D rating and reasoning. |
| "Is the US market overheating right now?" | Runs us-market-sentiment and returns a greed/fear rating plus a position recommendation. |
| "Is the Fed injecting or draining liquidity?" | Runs macro-liquidity and returns a liquidity rating and a risk response recommendation. |
| "Analyze NVDA's latest earnings report" | Runs tech-earnings-deepdive and produces a multi-perspective investment memo with action prices and triggers. |
| "Has Bitcoin bottomed out?" | Runs btc-bottom-model and returns a 0-100 Market Heat Score with buy or sell framing. |
| "Is MSFT a buy from a value and a growth lens?" | Chains tech-earnings-deepdive with us-value-investing for a cross-checked verdict. |

## Verification

Probe two skills on the branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/star23/Day1Global-Skills/main/us-value-investing/SKILL.md | head -20
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/star23/Day1Global-Skills/main/btc-bottom-model/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/star23/Day1Global-Skills/main/tech-earnings-deepdive/SKILL.md
```

The layout matters: skills live at the repository root as `<skill>/SKILL.md`, not under `skills/`. Point any verification script at the root layout or it will report a false failure.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| us-value-investing | Pass | Pass | Warn |
| us-market-sentiment | Pass | Pass | Warn |
| macro-liquidity | Pass | Pass | Warn |
| tech-earnings-deepdive | Pass | Pass | Pass |

Three of the four sampled skills carry a Snyk Warn; only tech-earnings-deepdive is clean across all three auditors. Read the Snyk advisory for each Warned skill before you install, and do not treat a Warn as an automatic pass. btc-bottom-model was not sampled and publishes no verdict, which is not the same as a pass.

## Limitations

- Snapshot data, verified 2026-11-13: 2,970 combined installs across 5 indexed listings; 1,064 GitHub stars; MIT licence; last pushed 2026-08-18. Counts drift over time.
- These are analysis frameworks, not licensed investment advice. The README disclaimer states the output is for research only and that investing carries risk, so treat every rating and position recommendation as a model output, not a directive.
- The frameworks are indicator-based and reference live market data (NAAIM, SOFR, MOVE, on-chain metrics), but the SKILL.md files do not fetch that data for you. You supply or look up the figures, then the skill scores them.
- btc-bottom-model was not part of the sampled security verdict set, so it publishes no skills.sh verdict. Three of the four sampled skills carry a Snyk Warn.
- The repository has not been pushed since August 2026. The frameworks still apply, but the indicator sources and thresholds they reference may have drifted.

## Related

- [Finance Skills - Financial Analysis for Hermes Agents](/hermes/skills/catalog/finance-skills-setup)
- [Octagon Finance Skills - Market Data and Analyst Workflows](/hermes/skills/catalog/octagon-finance-skills-setup)
- [Awesome Finance Skills - Market Analysis Pack](/hermes/skills/catalog/awesome-finance-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with us-value-investing. It is the smallest, most mechanical rubric (four dimensions, 0-12 score) and tells you fast whether the agent applies the framework or just restates the question.
- Read tech-earnings-deepdive's anti-bias and evidence-tier sections before you trust its memo output. The model is only as good as the tier-1 primary sources you feed it.
- The frameworks do not fetch live data. Keep a source for NAAIM, SOFR, MOVE and on-chain metrics handy so the scoring has real inputs.
- Mind the disclaimer. Anything these skills output is research, not investment advice, so do not wire a recommendation into an automated trading action.
- Try the Claude Code slash-command path if you want deterministic invocation rather than topic auto-detection.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
