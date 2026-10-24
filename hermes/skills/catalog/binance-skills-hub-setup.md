---
title: "Binance Skills Hub - Crypto Trading Skills Setup"
description: "Binance Skills Hub: 146.7K combined installs. 35 skills for spot and futures orders, Web3 wallets, token audits and on-chain signals."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/binance-skills-hub-setup/"
robots: "index,follow"
last_updated: "2026-10-23"
tags: ["hermes skill", "agent skill", "skill setup", "crypto", "trading", "binance", "web3"]
---

# Binance Skills Hub - Setup Guide

**Source:** [binance/binance-skills-hub](https://www.skills.sh/binance/binance-skills-hub) via skills.sh - 146.7K combined installs across 35 indexed listings; first indexed March 2026, new to this catalog in the Oct 23, 2026 sweep

**GitHub:** [binance/binance-skills-hub](https://github.com/binance/binance-skills-hub) - 1,083 stars, no repository-level LICENSE while four skill directories ship their own MIT LICENSE.md, last pushed 2026-10-23, branch main, 21 skill directories split across `skills/binance/` and `skills/binance-web3/`

**Category:** Crypto Exchange / On-Chain Trading

**Quality Tier:** 🟡 Beta - official Binance repository with same-day activity and clean market-data skills, but Snyk rates thirteen of the sampled listings Fail on HIGH-risk credential handling and direct money access, so every trading path is an unattended-agent risk

Binance Skills Hub is Binance's own skill marketplace for crypto work. It ships two families: a centralized exchange family where an authenticated CLI reaches Spot, futures, margin, Convert, P2P, fiat and payment endpoints, and a Web3 family that reads chains directly for token data, token security audits, wallet tracking, smart-money signals, leaderboards and copy-trade scaffolding.

The split matters more than the install count. The Web3 half is mostly read work: audit a contract before trading it, rank smart money, snapshot a wallet. The exchange half reaches accounts that hold funds. Binance publishes both under one repository, and the auditors treat the second half the way it deserves.

The repository is young in audit terms and current in code terms: 1,083 stars, a push on the snapshot date, and a first index date in March 2026. This guide covers all 35 indexed listings, including the fourteen that map to endpoint reference files inside the `binance` skill rather than to their own directories.

## Installation

Node 22 or newer is the only prerequisite the README states:

```bash
npx skills add https://github.com/binance/binance-skills-hub
```

The exchange family drives `binance-cli`, which the skill installs for you and which you can install directly. If an old global npm package is present below 2.0.0, remove it first:

```bash
npm uninstall -g @binance/binance-cli
curl --proto '=https' --tlsv1.2 -LsSf \
  https://github.com/binance/binance-cli/releases/latest/download/binance-cli-installer.sh | sh
binance-cli --version
```

Credentials are profiles, not environment variables in a shell history. The `auth.md` reference documents the shape:

```bash
binance-cli profile create --name hermes --api-key <key> --api-secret <secret> --env prod
binance-cli profile select --name hermes
binance-cli profile list
```

The skill's own security rules are worth reading before the first call: no `printenv`, no `env`, no sourcing a secrets file, and no unanchored `grep` over an env file. `BINANCE_API_ENV` accepts `prod`, `testnet` or `demo`, and testnet is the sane place to prove a flow.

The Web3 skills need no Binance account. They read public chain data, and the wallet-driving skills ask for a wallet session when a flow reaches a signature.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| square-post | 30,544 | Publishes to Binance Square: short text posts, multi-image posts up to four images, long-form articles with an optional cover, and videos with an auto-generated cover frame. |
| binance-agentic-wallet | 12,952 | Drives the `baw` Web3 wallet CLI for connect and sign in, balances, token transfers, swaps, limit and market orders, DeFi deposits and staking, and x402 payments. |
| trading-signal | 9,671 | Per-trade smart-money signals, each a discrete buy or sell event from a tracked wallet with trigger price, current price, max gain since trigger and exit rate. BSC and Solana only. |
| crypto-market-rank | 8,925 | Market leaderboards: social hype and sentiment rank, trending, top-search, Binance Alpha and tokenized-stocks rank, and smart-money net inflow. |
| query-token-info | 7,572 | Per-token lookup by keyword, symbol or contract address: search, static metadata, social links and market fields. |
| query-token-audit | 7,363 | Token security audit before trading: contract risks, trading risks, honeypot detection and scam detection. |
| meme-rush | 7,093 | Live launchpad feed and AI hot topics for meme tokens, with lifecycle stages from brand-new launch through bonding curve to migration. |
| query-address-info | 7,023 | Snapshot of one wallet's token holdings on a chain, with name, symbol, price, 24 hour change and quantity. |
| binance-tokenized-securities-info | 4,949 | Ondo tokenized US stock data: supported stock tokens, RWA metadata and attestation reports, plus market and per-asset trading status. |
| binance | 4,704 | The `binance-cli` core skill for Spot, USD-S futures and Convert, with the helper command index that routes to every reference family below. |
| onchain-pay-open-api | 4,514 | Buy crypto with fiat, or move crypto from a Binance account to an external on-chain wallet, in one flow. The listing name does not match its directory, which is `skills/binance/onchain-pay/`. |
| fiat | 4,297 | Fiat capability data through public APIs: supported countries, currencies, payment methods and limits, plus authenticated order and payment history. |
| p2p | 4,106 | P2P and C2C market ads, own order history, order detail and appeal tracking, and advertisement publish and management. |
| payment-assistant | 3,210 | Binance Pay send and receive: QR payment from the funding wallet over C2C and PIX, with confirm, cancel and status paths. The listing name does not match its directory, which is `skills/binance/payment/`. |
| spot | 2,916 | Spot endpoint family behind `binance-cli`: account, order, order-list and market-data commands with their key parameters. |
| derivatives-trading-usds-futures | 2,253 | USD-S futures endpoints: account information and balance, position mode, and order or trade history download ids. |
| assets | 2,004 | Wallet-level asset endpoints: account info and status, API trading status and daily account snapshots. No reference file carries the listing name; the nearest is `references/wallet.md`. |
| binance-sports-ai-analyzer | 1,980 | World Cup match prediction probabilities, news insight and win-rate recomputation with custom correction weights. |
| alpha | 1,956 | Binance Alpha market data: exchange info, klines, ticker, full depth and aggregated trades. |
| margin-trading | 1,926 | Margin account endpoints: isolated margin enable and disable, cross margin leverage, account summary and BNB burn status. |
| binance-trading-signal | 1,554 | On-chain trading signals plus custom signal strategy management on Binance Web3, across three signal types. |
| binance-wallet-tracker | 1,526 | Wallet tracking across four domains: discovery through consensus and leaderboard diffs, private groups, public smart-money and KOL data, and trade monitoring. |
| binance-leaderboard | 1,511 | Top trader rankings by PnL, win rate, volume, trade count and token count across BSC, Solana, Base and Ethereum, plus single-wallet Gem Hunter analysis. |
| convert | 1,328 | Convert pairs, quantity precision per asset and authenticated convert order placement. |
| algo | 1,240 | Algorithmic order endpoints: TWAP futures algo orders, current and historical algo orders, sub orders and cancellation. |
| derivatives-trading-coin-futures | 1,208 | COIN-M futures endpoints: account information, balance, position mode and order or trade history download ids. |
| derivatives-trading-options | 1,178 | Options endpoints: margin account information, funding flow and options market data. |
| derivatives-trading-portfolio-margin-pro | 1,152 | Portfolio Margin Pro operations: BNB transfer, auto-repay futures status, margin call levels and fund collection. |
| derivatives-trading-portfolio-margin | 1,150 | Portfolio Margin endpoints: balances, account information, leverage changes and asset transfers. |
| sub-account | 1,118 | Master-account sub-account management: create virtual sub-accounts, enable futures or options, and read position risk per sub-account. |
| simple-earn | 1,080 | Simple Earn and BFUSD account data: quota details, rate history, redemption history and rewards history. |
| vip-loan | 1,035 | VIP loan market and account data: borrow interest rates, collateral assets, loanable assets and fixed rate markets. |

The remaining 3 indexed listings range from 364 to 747 installs: binance-onchain-copy-trader (747), academy-skill (531) and binance-prediction-updown (364).

## Why This Matters for Hermes Agents

Most crypto skills on skills.sh answer one question from one chain. This repository answers the questions that sit either side of a trade: is this contract safe, who is actually buying, what does the order book look like, and can I place the order from the same agent session. For a Hermes workflow that means one skill family can carry a task from screening to execution without a stack of API keys from four vendors.

The token audit and wallet tracker skills are the highest-value half for an agent that has to justify a claim. A Hermes answer that cites a honeypot check, a holder snapshot and a smart-money entry is a different class of answer from one that repeats a price. The audit response is structured, so it can be quoted with the fields a user would ask for next.

The exchange family is the opposite trade-off. It is genuinely complete: spot, three futures products, margin, portfolio margin, options, sub-accounts, earn, loans, convert, P2P, fiat and payments, each with endpoint tables an agent can follow. It also requires a live API key with trading permission, and the Snyk audits say plainly that the signing instructions put key material into the agent's command path. Run it against testnet first, scope the key to the permissions the flow needs, and whitelist the host IP as the README advises.

The repository is also a clean example of a vendor shipping skills rather than an SDK. The skills are instruction files plus reference tables, so an agent reads them the way it reads documentation, and the CLI does the work. That is the shape most enterprise platforms will copy.

## Usage

| You say | What happens |
|---|---|
| "Is this token safe to trade?" | query-token-audit returns contract, trading and scam risk fields for the contract address, so the agent can quote risks rather than a verdict. |
| "Who is buying this token right now?" | trading-signal returns discrete smart-money buy and sell events with trigger price, current price and max gain since trigger. |
| "What is in this wallet?" | query-address-info returns every token held on the named chain with price, 24 hour change and quantity. |
| "Rank the top traders on BSC by win rate" | binance-leaderboard queries the on-chain leaderboard for the chain and metric you name, then Gem Hunter analysis explains one wallet. |
| "What are my open spot orders?" | The agent routes through the `binance` skill to the spot account family and returns open orders for the symbol. |
| "Post this to Binance Square" | square-post publishes the text, image set, article or video with the cover frame the platform expects. |
| "What are the fees to buy USDT with a card in Brazil?" | fiat returns supported payment methods, limits and currencies for the country and currency pair. |

## Verification

Confirm the three layouts exist on main before installing, because this repository uses two of them:

```bash
for p in skills/binance/square-post/SKILL.md \
         skills/binance/binance/SKILL.md \
         skills/binance-web3/trading-signal/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/binance/binance-skills-hub/main/$p"
done
```

Read the credential rules in full before granting anything:

- https://raw.githubusercontent.com/binance/binance-skills-hub/main/skills/binance/binance/references/auth.md
- https://raw.githubusercontent.com/binance/binance-skills-hub/main/skills/binance-web3/binance-agentic-wallet/SKILL.md

Two local checks after install: `binance-cli --version` should report 2.0.0 or newer, and `binance-cli profile view` should show the profile you selected. A `market` or `spot` command against testnet proves the key works without touching a funded account. The Web3 skills need no key; the wallet skill needs a wallet session before any signature.

## Security

skills.sh verdicts for sampled skills (verified October 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| square-post | Pass | Warn | Pass |
| binance-agentic-wallet | Pass | Warn | Warn |
| trading-signal | Pass | Pass | Warn |
| crypto-market-rank | Pass | Pass | Warn |
| query-token-info | Pass | Pass | Warn |
| query-token-audit | Pass | Pass | Pass |
| meme-rush | Pass | Pass | Warn |
| query-address-info | Pass | Pass | Warn |
| binance-tokenized-securities-info | Pass | Pass | Pass |
| binance | Pass | Pass | Warn |
| onchain-pay-open-api | Pass | Warn | Warn |
| fiat | Warn | Warn | Pass |
| p2p | Pass | Pass | Warn |
| payment-assistant | Pass | Pass | Warn |
| spot | Pass | Warn | Fail |
| derivatives-trading-usds-futures | Pass | Warn | Fail |
| assets | Pass | Warn | Fail |
| alpha | Pass | Pass | Fail |
| margin-trading | Pass | Pass | Fail |
| binance-trading-signal | Pass | Pass | Pass |

Snyk also fails eight listings not shown above: convert, algo, derivatives-trading-coin-futures, derivatives-trading-portfolio-margin-pro, derivatives-trading-portfolio-margin, sub-account, simple-earn and vip-loan. That is thirteen Fail verdicts out of the 35 sampled, and they are not false positives. Read the detail page behind one of them and the reason is legible: the spot audit records HIGH risk W007, insecure credential handling, because the instructions require building signed requests with the `X-MBX-APIKEY` header and the secret key to create the signature, which puts key material into the agent's command path. W009, direct money access, is recorded alongside it. The wallet skill's W009 is narrower: it drives a wallet CLI that can send, swap, place limit orders and stake.

The Web3 reads are clean. query-token-audit, binance-tokenized-securities-info, binance-trading-signal, binance-leaderboard and academy-skill pass all three auditors. fiat carries the only Gen Agent Trust Hub Warn, for command execution and prompt-injection surface around interpolated currency and country parameters.

Treat an exchange API key as the most dangerous credential on the machine. Create it with trading enabled only if the flow needs trading, enable withdrawals never, whitelist the host IP, and keep it in a profile rather than an exported variable. A `testnet` profile is the cheap way to prove a flow before a real one.

## Limitations

- Snapshot data, verified October 23, 2026: 146,680 combined installs across 35 indexed listings; 1,083 GitHub stars; no repository-level LICENSE, while `skills/binance/binance/`, `fiat/`, `onchain-pay/` and `p2p/` each ship an MIT LICENSE.md and the other 17 directories ship none; last pushed 2026-10-23. Counts drift over time.
- The install index outruns the tree: 35 indexed listings against 21 skill directories. Fourteen listings, including spot, margin-trading, convert, algo, the five derivatives families, sub-account, simple-earn, vip-loan, assets and alpha, are endpoint reference files under `skills/binance/binance/references/` rather than installable directories.
- Two listing names differ from their directories: `onchain-pay-open-api` maps to `skills/binance/onchain-pay/`, and `payment-assistant` maps to `skills/binance/payment/`. Install by directory name, not by listing name.
- `assets` has no reference file of its own; the nearest is `references/wallet.md`. The row above says so rather than guessing at a separate skill.
- Every exchange skill needs a real API key. None of the read-only Web3 skills does, so the two halves have different risk profiles and should not share a credential policy.
- The Snyk audits carry dates from March to October 2026 while the repository was pushed on the snapshot date, so a current tree can be newer than its verdict.
- Fiat rails, P2P and payment availability depend on the user's country and account status. The skills document capability, not entitlement.

## Related

- [OKX CEX Agent Skills - Exchange Trading Suite Setup](/hermes/skills/catalog/okx-cex-agent-skills-setup)
- [GMGN Agent Skills - On-Chain Analytics and Trading Setup](/hermes/skills/catalog/gmgn-skills-setup)
- [Claude Trading Skills - 74-Skill Trading Workflow Setup](/hermes/skills/catalog/claude-trading-skills-setup)
- [Solana Dev Skill - Blockchain Development Setup](/hermes/skills/catalog/solana-dev-skill-setup)

## Pro Tips

- Start with the audit and tracker skills. They need no key, they answer questions users actually ask, and they build the case for connecting an account later.
- Prove every exchange flow on a `testnet` profile. `binance-cli profile create --env testnet` costs nothing and catches a signature or permission mistake before it reaches a funded account.
- Keep one profile per purpose. `profile create` plus `--profile` on a command means a read workflow never inherits trading permission.
- Read `references/auth.md` once. The skill's own security rules, no `printenv`, no unset-var `export`, anchored `grep`, exist because an agent that prints its environment has already leaked the key.
- When a listing name and a directory name disagree, trust the tree. `onchain-pay-open-api` and `payment-assistant` both install by their directory names.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
