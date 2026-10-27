---
title: "GMGN Agent Skills - On-Chain Analytics and Trading Setup"
description: "GMGN Agent Skills: 156.2K combined installs. 19 skills for multi-chain token analytics, smart-money tracking, contract scoring and on-chain swaps."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/gmgn-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skill setup", "crypto", "on-chain data", "trading"]
---

# GMGN Agent Skills - Setup Guide

**Source:** [GMGNAI/gmgn-skills](https://www.skills.sh/gmgnai/gmgn-skills) via skills.sh - 156.2K combined installs across 19 indexed listings; reported as a below-floor cluster in the Aug 12, 2026 sweep and converted on 2026-10-22
**GitHub:** [GMGNAI/gmgn-skills](https://github.com/GMGNAI/gmgn-skills) (624 stars; MIT; pushed 2026-10-21; layout `skills/<name>/SKILL.md` for all 19 skills, beside a TypeScript CLI in `src/` and a `gmgn-cli` npm package)
**Category:** Crypto / On-Chain Analytics and Execution
**Quality Tier:** 🟡 Beta - active publisher, MIT, and a Pass from Gen Agent Trust Hub on both sampled skills, but Snyk fails one sampled skill on credential handling and Socket warns on the same auth path, so the execution half needs a human gate

GMGN is a multi-chain trading terminal, and this repo is its agent layer: 19 skills that reach GMGN's OpenAPI across Solana, BSC, Base and Ethereum, from token discovery and holder forensics through to executing a trade. The vendor documents 500+ data dimensions and a 1-minute minimum window on trending and candle data, served live rather than from a cache.

The suite has a clean shape. Six skills read the market (`gmgn-market`, `gmgn-token`, `gmgn-track`, `gmgn-heat-rank`, `gmgn-kline-pattern`, `gmgn-callout`), six analyse who is trading and whether they are worth following (`gmgn-portfolio`, `gmgn-holder-analysis`, `gmgn-wallet-analysis`, `gmgn-wallet-score`, `gmgn-wallet-style`, `gmgn-wallet-review`), three return a single scored verdict rather than fields (`gmgn-contract-dd`, `gmgn-dev-score`, `gmgn-callout-score`), and three can move money (`gmgn-swap`, `gmgn-token-buy`, `gmgn-cooking`). The publisher marks the last group in the skill descriptions themselves with a `[FINANCIAL EXECUTION]` prefix.

## Installation

```bash
# The skills, from the publisher
npx skills add GMGNAI/gmgn-skills

# The CLI that every skill calls
npm install -g gmgn-cli
```

An API key is required and is created at `https://gmgn.ai/ai` from an Ed25519 public key, which the README has the agent generate locally:

```bash
openssl genpkey -algorithm ed25519 -out /tmp/gmgn_private.pem
openssl pkey -in /tmp/gmgn_private.pem -pubout
```

Write credentials to the global config file yourself rather than passing them on a command line:

```bash
mkdir -p ~/.config/gmgn
echo 'GMGN_API_KEY=<your_key>' > ~/.config/gmgn/.env
chmod 600 ~/.config/gmgn/.env
```

The README's own flow pipes the key through `gmgn-cli config --apply <KEY>` and generates the key pair in `/tmp`. Both are the exact behaviours Snyk flags below, so write the env file directly and generate the PEM outside `/tmp` if the machine is shared. `GMGN_PRIVATE_KEY` is only needed for swap, order and launch skills, and the publisher states plainly that it is a request-signing key for the API, not a blockchain wallet private key.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| gmgn-market | 17,412 | Charts (K-line, OHLCV), trending rankings down to a 1-minute window, launchpad new-token feeds, hot searches, and search by name, symbol, contract or wallet |
| gmgn-token | 17,393 | Token research by address: price, market cap, liquidity, holders, top traders, Smart Money and KOL positions, honeypot and rug audit, social links |
| gmgn-portfolio | 17,101 | Wallet holdings, batch realized and unrealized P&L across up to 100 wallets, win rate, trade history, and tokens created by a dev wallet |
| gmgn-track | 16,724 | Live buy and sell activity from Smart Money, KOL and followed wallets, for whale alerts, copy-trade ideas and tracking |
| gmgn-swap | 16,532 | Execution: single swaps, multi-wallet batches, limit orders, stop loss, take profit and the trailing variants of both |
| gmgn-cooking | 15,590 | Launch a meme coin on a launchpad (Pump.fun, FourMeme, Bonk, Clanker and others) and query launchpad creation stats |
| gmgn-holder-analysis | 9,797 | Holder chip analysis: distribution, entry cost, whale, dev and KOL behavior, rat-trader, bundler and sniper exposure, structure rating |
| gmgn-kline-pattern | 6,740 | Classifies candles into a named setup (uptrend channel, breakdown, basing, distribution) and scores it 0-100 with a stated reason per point |
| gmgn-contract-dd | 6,487 | One composite 0-100 due-diligence score per token, capped by the platform rug label, where every deduction names the field it read |
| gmgn-wallet-analysis | 6,039 | Copy-trade dossier: four pass/fail gates, current holdings and buys, entry market-cap band, copy window in seconds and a size cap |
| gmgn-dev-score | 5,641 | Scores a token creator on conduct and on power from the full launch history, then returns a buy or do-not-buy call with a timing window |
| gmgn-token-buy | 5,387 | Resolves a name or symbol to the right contract among copycats and sizes the order: amount, slippage, gas and position |
| gmgn-heat-rank | 4,254 | Screens all seven chains for tokens that are hot now, gates them on liquidity, volume, concentration and rug risk, and caps the list at ten |
| gmgn-narrative | 4,076 | Narrative and social-spread due-diligence card: the story a token is telling and what is independently verifiable about its spread |
| gmgn-wallet-score | 1,982 | Scores a wallet on profitability, copy-tradeability with a latency and slippage backtest, and dev reputation, plus style tags |
| gmgn-wallet-review | 1,974 | One-screen trading portrait of a single wallet: style tag, speed subtitle, one line of record and one line of next-step advice |
| gmgn-wallet-style | 1,969 | Style tagging from a 20-cell frequency and P&L grid, a holding-speed label and up to 14 badges, each with the number that triggered it |
| gmgn-callout | 581 | Reads public call-outs: call price, market cap at call, multiplier since, thesis text and the caller current holding |
| gmgn-callout-score | 502 | Scores a caller on selection and post-call conduct from their own per-trade ledger, then returns a follow or do-not-follow verdict |

No indexed listings fall below the 500-install threshold; all 19 appear above.

## Why This Matters for Hermes Agents

Token questions are the highest-risk queries an agent answers, because every failure mode is financial. A ticker resolves to several contracts, one of which is a honeypot, and a model working from memory has no way to tell them apart. Here the resolution is a CLI call: `gmgn-token-buy` takes a name and returns the right contract among the copycats before any order is built, and `gmgn-token` returns open-source status, renouncement, honeypot detection and the rug label as fields rather than an opinion.

The second gain is that three of the skills return a score with reasons instead of a data dump. `gmgn-contract-dd` produces a single 0-100 composite where every deduction names the field it read, `gmgn-kline-pattern` scores candle structure from six measurements, and `gmgn-wallet-score` separates profitability from copy-tradeability. That is a shape an agent can quote and a reader can audit, which is a different thing from a paragraph of conviction.

The third is durability. The publisher's pitch is that the data path replaces page scraping and Cloudflare workarounds, so a Hermes cron that watches Smart Money wallets or a heat-rank list does not break when a front end changes. Each skill is a documented command returning JSON, which is what a scheduled job needs.

The last point is the warning. With `GMGN_PRIVATE_KEY` present, `gmgn-swap`, `gmgn-token-buy` and `gmgn-cooking` can spend real funds, and the publisher notes that automated trades can bypass the CLI's interactive confirmation. Install the analysis skills on any agent. Install the execution skills only where a human confirms each order, and keep the signing key out of `.env` files that a general-purpose agent can read.

## Usage

| You say | What happens |
|---|---|
| "What is smart money buying on Solana right now?" | `gmgn-track` returns live buys and sells from Smart Money and KOL wallets, with the tokens involved |
| "Is this token a rug?" | `gmgn-token` returns honeypot, open-source and renouncement fields plus the rug label for that address |
| "Score this contract before I touch it" | `gmgn-contract-dd` returns one 0-100 composite, each deduction naming the field it read |
| "Which wallets should I copy?" | `gmgn-wallet-analysis` runs four pass/fail gates and returns a copy window in seconds plus a size cap |
| "What is hot right now across chains?" | `gmgn-heat-rank` sweeps the chains, gates on liquidity and concentration, caps the result at ten names |
| "Buy 0.5 SOL of this ticker" | `gmgn-token-buy` resolves the name to a contract and sizes the order, then `gmgn-swap` submits it with confirmation |
| "Who called this token and how did it go?" | `gmgn-callout-score` scores the caller on selection and on post-call conduct from their own trade ledger |

## Verification

Confirm the skills landed and the CLI answers before any key is written:

```bash
npx skills list | grep -i gmgn
```

```bash
GMGN_API_KEY=gmgn_solbscbaseethmonadtron gmgn-cli market trending --chain sol --interval 1h --limit 3
```

That public demo key is the publisher's own smoke test. Read a skill before installing it, for example the market skill:

```bash
curl -s https://raw.githubusercontent.com/GMGNAI/gmgn-skills/main/skills/gmgn-market/SKILL.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Oct 22, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gmgn-market | Pass | Warn | Fail |
| gmgn-swap | Pass | Warn | Warn |

The Snyk failure on `gmgn-market` is HIGH W007, insecure credential handling: the skill instructs the agent to ask the user for an API key and pass it as a command-line argument, which puts the secret in the LLM context and in execution logs. The same report adds MEDIUM W011, indirect prompt injection risk, because token names and metadata from the chain are third-party text that re-enters the model. Socket raises one LOW anomaly on the same auth path: a `GMGN_PRIVATE_KEY` stored and used through an external CLI binary is disproportionate credential exposure for a market-lookup skill.

`gmgn-swap` carries MEDIUM W009, direct money access, and MEDIUM W011. The report is explicit that the safety layer is a key in the environment plus interactive CLI confirmation, and that automated trades can bypass the confirmation.

Practical mitigations, in order of value: install the read-only skills first and treat the three execution skills as a separate decision; write credentials to `~/.config/gmgn/.env` with mode 600 instead of passing them as arguments; never give a general-purpose agent that can read the whole home directory a signing key; and require an explicit human confirmation before any swap, order or token launch.

## Limitations

- The signing key is the blast radius. With `GMGN_PRIVATE_KEY` configured, three skills can move funds and one can launch a token, and the publisher states that automated calls can skip the interactive confirmation.
- `GMGN_API_KEY` is mandatory for real use. The demo key in the README smoke test is a fixed public string for installation checks only.
- The default key-pair flow writes the private PEM to `/tmp` and passes the API key on a command line. Both are flagged by the audits above, so the install commands here deviate on purpose.
- Much of the collected data is memecoin-native: rat traders, bundlers, snipers, bonding curve status, launchpad names. It assumes a reader who trades that market, not a general crypto portfolio.
- Some skill descriptions and outputs mix Chinese and English terminology (for example the wallet style tags), which can leak into agent output verbatim.
- Snapshot data, verified Oct 22, 2026: 156,181 combined installs across 19 indexed listings; 624 GitHub stars; MIT; last pushed 2026-10-21. Counts drift over time.

## Related

- [Coinos Skills - AiCoin Crypto Trading Suite Setup](/hermes/skills/catalog/coinos-trading-skills-setup)
- [Finance Skills - Financial Analysis for Agents Setup](/hermes/skills/catalog/finance-skills-setup)
- [Hithink Finance - Tonghuashun A-Share Data Skill Setup](/hermes/skills/catalog/hithink-finance-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `gmgn-heat-rank` and `gmgn-contract-dd` on a paper basis for a week. Both return scored verdicts, so you can check the reasoning against outcomes before any key with trading scope exists.
- Use `gmgn-token-buy` even when you plan to place the order by hand. Contract resolution is the step that fails silently, and that skill exists to do only that plus sizing.
- When a skill returns an address-level field the model did not have before, keep it in the reply. Crypto answers that omit the contract address are not verifiable.
- Set the agent's working directory away from `~/.config` when the execution skills are installed, and keep the signing key in a file the agent process cannot read.
- If a scheduled job needs this data, call `gmgn-cli` directly in the job and skip the skill. The skills are prompt guidance for a conversational agent; the CLI is the stable interface.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
