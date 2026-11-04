---
title: "Coinbase Agentic Wallet - USDC Payments Skill"
description: "coinbase/agentic-wallet-skills: 27.3K combined installs. Single skill routing USDC sends, trades, x402 payments and onchain queries via the awal CLI."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/coinbase-agentic-wallet-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "payments", "crypto wallet", "x402"]
---

# Coinbase Agentic Wallet - Setup Guide

**Source:** [coinbase/agentic-wallet-skills](https://www.skills.sh/coinbase/agentic-wallet-skills) via skills.sh - 27.3K combined installs across 11 indexed listings; first documented November 3, 2026 (evening sweep)
**GitHub:** 127 stars, license MIT, last pushed 2026-08-04, 1 SKILL.md directories
**Category:** Agent payments: sign in, read balances, send USDC and trade tokens through the Coinbase agentic wallet CLI
**Quality Tier:** 🟡 Yellow - MIT and a small, reviewable tree, but four of the five sampled listings carry a Snyk warning and query-blockchain-data fails Gen Agent Trust Hub

Coinbase publishes this repository as Agent Skills for crypto wallet operations, built around the `awal` CLI distributed on npm. The tree holds a single `SKILL.md` directory, `skills/agentic-wallet`, and that one skill is a router: its frontmatter declares the shell tools the agent may call, and its body maps a capability to the reference document the agent should read before acting.

The reference set covers sign-in by email OTP, balances across Base, Polygon and Solana, sends of USDC, ETH, POL and SOL, token swaps on Base and Polygon, funding through Coinbase Onramp, the x402 paid-API flow in three parts (search, pay, monetize) and onchain queries through the CDP SQL API. skills.sh indexes 11 listing names against that one directory, so the per-capability rows in the table below are listing names, not 11 separate skills to install.

## Installation

The README documents one command with the skills CLI:

```bash
npx skills add coinbase/agentic-wallet-skills
```

The README states that installed skills are automatically available once installed and that the agent uses them when it detects a relevant task. No API key is provisioned at install time: wallet access is an email OTP sign-in handled at run time by the `awal` CLI, which the skill drives.

For a Hermes profile, the same tree can be dropped into the profile skills directory. The reference documents are resolved relative to the skill folder, so keep `references/` alongside `SKILL.md`:

```bash
git clone --depth 1 https://github.com/coinbase/agentic-wallet-skills.git /tmp/cbx-skills
cp -R /tmp/cbx-skills/skills/agentic-wallet ~/.hermes/profiles/corpusiq/skills/
```

The `awal` version is pinned in every code block in `SKILL.md` and in each reference document rather than in a package manifest. The repository ships `scripts/bump-awal.js` to rewrite those pins, and its own instructions require Node v22 or newer to run it. Nothing in the repository mentions Hermes, and nothing in it is chain-specific beyond the networks named in the references.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| trade | 3,096 | Swap or trade tokens on Base or Polygon; the routing table points here for `trade.md`. |
| x402 | 3,018 | Umbrella listing for the three x402 documents: bazaar search, paying an endpoint and monetizing one. |
| send-usdc | 2,951 | Send USDC, ETH, POL or SOL on Base, Polygon or Solana via `send-usdc.md`. |
| pay-for-service | 2,946 | Pay an x402 endpoint with automatic USDC payment; `x402-pay.md`. |
| monetize-service | 2,912 | Build and deploy a paid API server on x402; `x402-monetize.md`. |
| search-for-service | 2,811 | Search the x402 bazaar for paid API services; `x402-search.md`. |
| agentic-wallet | 2,739 | The installed skill itself: the router that sends the agent to the reference file matching the task. |
| authenticate-wallet | 2,438 | Sign in by email OTP; `auth.md`. |
| fund | 2,294 | Add funds through Coinbase Onramp; `fund.md`. |
| query-onchain-data | 2,051 | Query onchain data on Base through the CDP SQL API; `query-onchain.md`. |
| query-blockchain-data | 1 | No separate reference document in the tree; the nearest match is `query-onchain.md`, and the single install points to a duplicate listing rather than a second skill. |

All 11 indexed listings appear in the table above.

The drift is the story here. One skill directory sits behind 11 listing names, and the README's capability table names nine reference files: `auth.md`, `balance.md`, `send-usdc.md`, `trade.md`, `fund.md`, `x402-search.md`, `x402-pay.md`, `x402-monetize.md` and `query-onchain.md`. Ten of the eleven listings map onto those files plus the router itself. The eleventh, `query-blockchain-data`, at one install, does not.

## Why This Matters for Hermes Agents

Payment is the step where an autonomous agent either finishes the job or stops and asks a human, and this pack reduces that step to a CLI call the agent can plan around. Reading a balance, sending a stablecoin and settling a paid API call all become commands with a printed result, which is the shape a tool loop needs.

The layout is worth copying even if you never touch a chain. One `SKILL.md` with a routing table and a `references/` folder per topic keeps the always-loaded context small and pushes the detail into files the agent opens only when the task calls for it. That is the difference between a skill that fits in a prompt and a skill that drowns it, and the README's contributing notes make the pattern explicit: new capability means a new reference file plus a new routing row, and a new shell tool means a new entry in `allowed-tools`.

The x402 half is the part with no obvious off-the-shelf substitute. An agent that can search a bazaar of paid endpoints, pay per call in USDC without a subscription, and stand up its own metered endpoint closes a loop that usually needs a human with a card. For a builder, that is the difference between an agent that consumes APIs and one that can sell access to its own.

Chain work also punishes optimism. A send needs a network, an amount and a recipient confirmed before anything is signed, and a swap needs a quote before it needs a signature. The balance and send references are what make a spend preflight possible, and the pinned CLI version means the flags an agent was tested against do not move underneath it.

## Usage

| You say | What happens |
|---|---|
| "Sign in to my wallet with me@example.com" | authenticate-wallet reads `auth.md` and starts the email OTP flow for the `awal` session. |
| "What is my USDC balance on Base and Polygon?" | The balance reference is read and per-chain balances are printed for the networks named. |
| "Send 10 USDC to barmstrong.eth" | send-usdc resolves the recipient, confirms chain and amount, then sends USDC. |
| "Swap 0.05 ETH for USDC on Base" | trade reads `trade.md`, obtains a quote and executes the swap on Base. |
| "Find a paid API for this and pay for one call" | search-for-service queries the x402 bazaar, then pay-for-service settles the call in USDC. |
| "Put my endpoint behind x402 at 0.01 USDC per call" | monetize-service builds and deploys the paid server from `x402-monetize.md`. |
| "How active was this contract on Base last week?" | query-onchain-data sends SQL to the CDP API through `query-onchain.md`. |

## Verification

The raw path below is built from the layout in this pack and returned 200 on branch main when this guide was written on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  "https://raw.githubusercontent.com/coinbase/agentic-wallet-skills/main/skills/agentic-wallet/SKILL.md"
```

After a clone, confirm that the directory count matches the pack and that the reference files the routing table names are present:

```bash
git clone --depth 1 https://github.com/coinbase/agentic-wallet-skills.git /tmp/cbx-skills
find /tmp/cbx-skills/skills -name SKILL.md | wc -l
ls /tmp/cbx-skills/skills/agentic-wallet/references
grep -o 'awal@[0-9][0-9.]*' -r /tmp/cbx-skills/skills | sort -u
```

The count should be 1, because the repository ships one skill directory. The listing should include `auth.md`, `balance.md`, `send-usdc.md`, `trade.md`, `fund.md`, `x402-search.md`, `x402-pay.md`, `x402-monetize.md` and `query-onchain.md`. The last command prints the pinned CLI versions, which should be a single version across every file if the bump script was run last.

## Security

skills.sh verdicts for sampled skills (verified November 3, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| trade | Pass | Warn | Warn |
| send-usdc | Pass | Warn | Warn |
| search-for-service | Pass | Pass | Warn |
| fund | Pass | Pass | Warn |
| query-blockchain-data | Fail | Pass | ? |

Only one of the five sampled listings passes all three auditors, and it is not a clean sweep: `search-for-service` and `fund` each carry a Snyk warning, `trade` and `send-usdc` carry both a Socket and a Snyk warning, and `query-blockchain-data` is the only listing in the repository with a Gen Agent Trust Hub failure. Its Snyk verdict is unresolved in this snapshot rather than passing.

The audit surface is a router plus nine Markdown references and one bump script, which is small enough to read in an afternoon. That is the mitigating fact and also the reason the verdicts deserve attention: the risk in this pack is not a sprawling dependency tree, it is that the instructions themselves move funds. Every reference that can sign a transaction should be read before the skill is given an agent with spending authority, and `allowed-tools` in the frontmatter is the first thing to review, because it decides which shell commands the skill is permitted to run.

Two domain risks do not show up in any scanner. Sign-in is an email OTP into a wallet session, so the mailbox is a key: whoever controls the address can approve the session. And a swap or a send is irreversible once broadcast, which means a misparsed amount is a real loss rather than a failed test.

## Limitations

- Snapshot data, verified November 3, 2026: 27,257 combined installs across 11 indexed listings; 127 GitHub stars; license MIT; last pushed 2026-08-04. Counts drift over time.
- One skill directory behind 11 indexed listing names. `query-blockchain-data` has a single install, no distinct reference document in the tree and the only Gen Agent Trust Hub failure in the sample, so treat it as a duplicate listing until the repository says otherwise.
- The nine reference files carry the detail and the routing table decides which one is read. A vague request can land on the wrong reference, so name the chain and the amount when you ask.
- The CLI version is pinned per code block rather than in a lockfile or manifest, which means an out-of-date pin is only visible by reading the files or running the bump script with Node v22 or newer.
- Wallet access is an email OTP session rather than a scoped API key. There is no read-only mode documented in this snapshot, so the same sign-in that reads balances can send funds.
- The repository does not document a Hermes install path, and its own examples assume the skills CLI. The profile copy above is the closest equivalent, not a supported route.

## Related

- [Claude Trading Skills - 74-Skill Trading Workflow Setup](/hermes/skills/catalog/claude-trading-skills-setup)
- [Binance Skills Hub - Crypto Trading Skills Setup](/hermes/skills/catalog/binance-skills-hub-setup)
- [GMGN Agent Skills - On-Chain Analytics and Trading Setup](/hermes/skills/catalog/gmgn-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read `SKILL.md` before you install anything else. The routing table is the whole product, and it tells you in one screen which capability costs a reference read and which tool each one is allowed to call.
- Ask for a balance before a send or a swap. The balance reference exists, and a preflight read is cheaper than a failed transaction and a support thread.
- Name the chain explicitly. USDC lives on Base, Polygon and Solana in this pack, and an unqualified send can resolve to a different network than the one you meant.
- Pin the CLI and re-run the bump script deliberately. The version is written into every code block, so a partial bump leaves the agent mixing flag sets from two releases.
- Keep `query-blockchain-data` out of your install list until the failure verdict is explained. `query-onchain-data` covers the documented onchain query path on its own.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
