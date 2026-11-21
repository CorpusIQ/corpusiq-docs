---
title: "Gate Skills - Crypto Exchange & DEX Agent Suite Setup"
description: "gate/gate-skills: 85 crypto skills for market analysis, derivatives, DEX trading and one-click MCP setup - 9.0K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gate-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "crypto", "trading", "dex"]
---

# Gate Skills - Crypto Exchange & DEX Agent Suite Setup

**Source:** [gate/gate-skills](https://www.skills.sh/gate/gate-skills) via skills.sh - 9.0K combined installs across 85 indexed listings; first seen Nov 21, 2026 (Nov 21, 2026 morning sweep)
**GitHub:** [gate/gate-skills](https://github.com/gate/gate-skills) - 50 stars, no LICENSE file, master branch, last pushed Nov 5, 2026; skills live under `skills/<name>/SKILL.md` with `references/` subfolders, plus a `_shared/` directory for CEX authoring and a `gate-mcp-installer` that carries per-host MCP config fragments.
**Category:** Cryptocurrency and Exchange Operations
**Quality Tier:** 🟠 Orange - 5 Fail cells in the 20-skill sample: Gen Agent Trust Hub Fails on gate-exchange-marketanalysis, gate-dex-market and gate-dex-trade, and Snyk Fails on gate-info-coinanalysis and gate-mcp-installer.

Gate Skills is the Gate exchange's own skills marketplace for agents that work inside the Gate cryptocurrency ecosystem, from market analysis and derivatives monitoring to one-click MCP setup, all through natural language. The repository splits into several product lines: six CEX source skills (trade, earn, assets, subaccount, affiliate and bot) that build standalone packages against an approved CLI contract, a set of read-only Gate-Info and Gate-News skills for market and news queries, Gate DEX skills for on-chain swaps and wallet work, and a unified MCP installer.

The skills.sh index tells an older story than the tree. The highest-count listings carry gate-exchange-* names (futures, spot, marketanalysis) that predate the CEX 2.0 restructure and have no counterpart directory in the current repository, which ships gate-cex-* source skills instead. The index also lists low-count gate-cex-* and gate-dex-mcp* names alongside the active set, so the install counts and the current tree only partially line up.

## Installation

The six CEX skills are source packages, not install-ready directories. The README instructs building standalone packages and copying only the generated output. From the repository root:

```bash
python -m pip install -r scripts/requirements-cex.txt
python scripts/cex_skills.py build --source . --contract tests/cex/cli-contract.json --output dist/gate-cex-2.0
```

For the non-CEX skills, install interactively via the skills CLI:

```bash
npx skills add https://github.com/gate/gate-skills
```

Or install one skill directly:

```bash
npx skills add https://github.com/gate/gate-skills --skill gate-info-coinanalysis
```

For MCP and skill setup across hosts, run the unified installer, which auto-detects Cursor, Claude Code, Codex or OpenClaw:

```bash
bash skills/gate-mcp-installer/scripts/install.sh
```

Use `--no-skills` for MCP only, or `--mcp main --mcp dex` to select specific servers.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| gate-exchange-futures | 232 | index-only listing with no directory in the current tree; futures trading is covered by the gate-cex-trade source skill |
| gate-exchange-spot | 207 | index-only listing; spot trading is covered by the gate-cex-trade source skill |
| gate-exchange-marketanalysis | 206 | index-only listing; market analysis is now served by gate-dex-market and gate-info-research |
| gate-news-briefing | 201 | crypto news briefing: major events, trending news and social sentiment |
| gate-info-trendanalysis | 181 | trend and technical analysis: K-line, RSI, MACD and multi-timeframe signals |
| gate-info-coinanalysis | 176 | single-coin analysis covering fundamentals, technicals, news and sentiment |
| gate-dex-market | 175 | read-only on-chain DEX market data: token prices, K-line/OHLC, rankings and risk audits |
| gate-info-riskcheck | 170 | token and contract risk checks: honeypot, rug pull, tax and holder concentration |
| gate-dex-trade | 169 | on-chain token swaps and cross-chain bridging through Gate DEX |
| gate-news-eventexplain | 168 | event attribution: why a price moved, from impact chain to market reaction |
| gate-info-marketoverview | 168 | overall market overview: sector rankings, DeFi, events and macro summary |
| gate-news-listing | 167 | exchange listing and delisting tracker with fundamental supplements |
| gate-dex-wallet | 165 | Gate DEX wallet: authentication, balances, transfers and DApp signing |

The remaining 72 indexed listings range from 1 to 164 installs.

## Why This Matters for Hermes Agents

A crypto agent that talks to a real exchange is moving money, which makes the routing rules the product. The Gate-Info skills are built around strict single-dimension routing: gate-info-coinanalysis handles single-coin analysis, gate-info-riskcheck handles only risk, and any query that mixes dimensions routes to gate-info-research for a unified report. That discipline matters because an agent asked "is SOL worth buying" should get a fundamentals-and-sentiment report, while "is this token safe" should run honeypot and holder-concentration checks and nothing else. The write path is scoped the same way: the Gate DEX trade and wallet skills separate swap execution from read-only market data and account queries, and the CEX trade skill documents 282 owned command paths behind a CLI contract rather than an open-ended surface. For an operator the MCP installer is the entry point, wiring Cursor, Claude Code, Codex and OpenClaw to the right servers in one step. The counterweight is the security sample: three Gen Agent Trust Hub Fails and two Snyk Fails among 20 sampled skills, so this suite earns its review-before-write caution.

## Usage

| You say | What happens |
|---|---|
| Install Gate MCP for Cursor | Runs the one-click installer and wires the selected Gate MCP servers into Cursor |
| Analyze SOL | Routes to single-coin analysis and produces a fundamentals, technicals, news and sentiment report |
| Is this token safe? 0x... | Runs the risk check: honeypot, rug pull, tax and holder concentration |
| Compare BTC vs ETH | Builds a multi-coin comparison table with market snapshots and fundamentals |
| Swap 100 USDT for ETH | Executes an on-chain swap through Gate DEX after a price quote |
| Why did BTC crash? | Traces the event and builds an event-to-impact-chain-to-market-reaction report |
| What is happening in crypto today? | Produces a market overview with sector rankings, DeFi, events and macro summary |

## Verification

Confirm the selected non-CEX skill folders landed in the host's skill directory:

```bash
ls ~/.claude/skills 2>/dev/null || ls ~/.codex/skills
```

Review the DEX market skill's routing instructions before granting write access:

```bash
curl -sL https://raw.githubusercontent.com/gate/gate-skills/master/skills/gate-dex-market/SKILL.md | head -60
```

The installer accepts `--no-skills` for MCP-only setup and `--mcp main --mcp dex` to select specific servers, which is the cheapest way to verify a partial install.

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gate-exchange-futures | Warn | Warn | Warn |
| gate-exchange-spot | Pass | Warn | Warn |
| gate-exchange-marketanalysis | Fail | Pass | Pass |
| gate-news-briefing | Pass | Warn | Warn |
| gate-info-trendanalysis | Pass | Warn | Pass |
| gate-info-coinanalysis | Pass | Warn | Fail |
| gate-dex-market | Fail | Warn | Warn |
| gate-info-riskcheck | Pass | Warn | Warn |
| gate-dex-trade | Fail | Warn | Warn |
| gate-news-eventexplain | Pass | Warn | Warn |
| gate-info-marketoverview | Pass | Warn | Warn |
| gate-news-listing | Pass | Warn | Warn |
| gate-dex-wallet | Pass | Warn | Warn |
| gate-info-coincompare | Pass | Warn | Pass |
| gate-info-addresstracker | Pass | Warn | Pass |
| gate-exchange-assets | Warn | Pass | Pass |
| gate-exchange-staking | Pass | Pass | Warn |
| gate-exchange-simpleearn | Warn | Pass | Warn |
| gate-mcp-installer | Pass | Warn | Fail |
| gate-info-research | Pass | Warn | Warn |

The sample is warning-dense: Socket Warns on 16 of the 20 skills, concentrated on the trading and DEX surfaces.

## Limitations

- Snapshot data, verified Nov 21, 2026: 8,962 combined installs across 85 indexed listings; 50 GitHub stars; no LICENSE file; last pushed Nov 5, 2026. Counts drift over time.
- The install index outruns the tree: the high-count gate-exchange-* listings (futures, spot, marketanalysis and more) have no counterpart directory in the current repository, which ships gate-cex-* source skills (trade, earn, assets, subaccount, affiliate, bot) instead.
- The six CEX skills are source packages, not install-ready directories: the README instructs building standalone packages with `scripts/cex_skills.py build` and copying only the generated output, so cloning the repository does not install usable CEX skills.
- The security sample carries 5 Fail cells across the 20 sampled skills, so review each write-capable skill before connecting a live account.
- The README's own disclaimer states the output is informational, not investment or trading advice; an agent wired to a live account can move real funds.

## Related

- [OKX CEX Agent Skills - Exchange Trading Suite Setup](/hermes/skills/catalog/okx-cex-agent-skills-setup)
- [Binance Skills Hub - Crypto Trading Skills Setup](/hermes/skills/catalog/binance-skills-hub-setup)
- [Coinos Skills - AiCoin Crypto Trading Suite Setup](/hermes/skills/catalog/coinos-trading-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the read-only Gate-Info and Gate-News skills (marketoverview, briefing, riskcheck) before wiring any write-capable DEX or CEX surface, and keep write skills behind a review gate.
- Use gate-info-research for any query that mixes dimensions; the single-dimension skills deliberately reject multi-part questions rather than half-answer them.
- For CEX work, build the standalone packages from source and verify each against the CLI contract with `scripts/cex_skills.py check` instead of copying source directories directly.
- Prefer `--no-skills` when you only need the MCP servers, and scope `--platform` so you do not install servers for hosts you do not run.
- Treat the skills.sh install counts for gate-exchange-* names as historical; install the current gate-cex-* and gate-info-*/gate-news-*/gate-dex-* set instead.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
