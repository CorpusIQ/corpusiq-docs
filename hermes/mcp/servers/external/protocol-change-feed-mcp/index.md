---
title: "Protocol Change Feed MCP - DeFi Votes and Upgrades"
description: "Thirty-two DeFi protocols with free governance counts, and a half-cent x402 report on proposals, upgrades and contract admins."
category: "Crypto / Governance"
stars: "0 (hosted Streamable HTTP at https://protocols.changefeed.dev/mcp, keyless free tier; five tools, two driven free and the paid refusal measured)"
added: 2026-11-17
source: "the mcp.so submission queue entry #7521 filed 2026-11-17T16:45:28Z, and a driven session on 2026-11-17 in which six tools/call requests were run against the live endpoint with no credential, including the paid tier's refusal"
relevance: ★★★
tags: [defi, governance, snapshot, proxy-upgrade, security, x402, keyless, remote, mcp]
last_updated: "2026-11-17"
---

# Protocol Change Feed MCP

**A lending protocol is upgraded on Tuesday and the agent watching the position learns about it from the price, three days later.** Governance proposals, proxy upgrades and admin-key changes are public before they are expensive, but they are published in three different places in three different shapes, and none of them is a format an agent can read at the moment it matters.

Protocol Change Feed is 32 DeFi protocols reduced to one question per protocol: what changed in this window. The governance half is free, the detail is five tenths of a cent per call, and the interesting part is that a paid MCP surface is a thing an agent can now negotiate by itself.

```
Server type:   remote Streamable HTTP (hosted)
Endpoint:      https://protocols.changefeed.dev/mcp
Server:        protocol-change-feed, version 0.1.0
Protocol:      2025-06-18
Auth:          none for the free tools; x402 payment per call for the rest
Tools:         5 (list_protocols, quick_check free;
                  protocol_changes, contract_check, protocol_digest paid)
Website:       https://protocols.changefeed.dev
Listed on:     the mcp.so submission queue as #7521
```

## The evidence tier

Keyless, free tier driven. `initialize` answered **200** with no credential, `tools/list` returned five schemas with the free and paid split stated in each description, and **six** `tools/call` requests were run: two free calls that returned data, one free call on an invented protocol, and one paid call whose refusal is itself the measurement. No payment was made and no paid result is quoted anywhere below.

## The protocol list is the catalogue

`list_protocols` takes no arguments and returns every covered protocol with its Snapshot spaces and its watched contracts:

```text
32 protocols: aave, uniswap, lido, compound, morpho, etherfi, eigenlayer,
rocketpool, sky, frax, convex, balancer, beethoven-x, sushi, pancakeswap,
1inch, cow, synthetix, across, arbitrum, optimism, base, starknet, ens,
safe, gnosis, gitcoin, shutter, usdc, eurc, cbbtc, pyusd
```

The shape matters more than the count. Aave carries one Snapshot space (`aavedao.eth`) and **two** watched contracts, the v3 Pool on Ethereum and the v3 Pool on Base, each with a checksum-free lowercase address. Uniswap carries `uniswapgovernance.eth` and an **empty** contracts array.

That empty array is the coverage boundary, stated by the server's own data rather than inferred: the governance half runs for all 32 protocols, and the on-chain half runs only where contracts are watched. An agent asked whether Uniswap had a proxy upgrade will get `0` and should read that as "none watched", not "none happened".

## Free answers that are already useful

`quick_check` returns counts, a one-sentence verdict, and a pointer to the paid report, in one object:

```text
aave, 30 days     active_proposals 3, proposals_in_window 11,
                  contract_upgrades_in_window 2, admin_changes_in_window 0,
                  watched_contracts 2
                  verdict: "Changed: 3 governance votes open now, 11 proposals
                  in the last 30 days, 2 contract upgrades."

uniswap, 90 days  active_proposals 3, proposals_in_window 5,
                  contract_upgrades_in_window 0, admin_changes_in_window 0,
                  watched_contracts 0
                  verdict: "Changed: 3 governance votes open now, 5 proposals
                  in the last 90 days."
```

The `days` argument is honoured: the same protocol answered 11 proposals at 30 days and a different count at 90 days, and the verdict sentence changes with it. The window is capped at 90 in the schema, so a question about the last year has to be asked twice. The tool description also states its own free ceiling, about 20 calls a minute per client, which is the honest way to publish a limit.

The verdict string is the design decision worth noting. It is written for a model to repeat rather than for a dashboard to parse, so an agent can answer "did Aave change?" without composing the sentence itself, and the counts stay available for anything that needs them.

## The paid tier, measured rather than assumed

`protocol_changes` is the full report: proposal titles, live vote tallies, quorum, end times, links, the upgrade and admin-change transactions, and the current implementation and admin of each watched contract. It costs **0.005 USDC**, and the refusal is a complete machine-readable offer rather than an error message:

```text
isError: true
x402Version: 2
error: "Payment required to access this tool"
accepts[0]: scheme "exact" · network "eip155:8453" (Base)
            amount "5000" · asset 0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913
            payTo 0xb2BFA671B14fEaFf42bA098B3a09B296D8efB303
            maxTimeoutSeconds 300
```

Three things are true of that payload and each is useful. The amount is in the asset's smallest unit (5000 of a six-decimal token is five thousandths of a dollar). The network and asset are named as CAIP identifiers, so a client can check what it is being asked to pay in before it signs anything. And the `resource` block restates what the half cent buys, so the decision to pay is made with the description in hand.

Whether an agent should hold a wallet is a policy question for whoever runs it, not a property of this server. What the server does is make the price and the terms legible at the moment of refusal, which is the minimum for a paid tool in an agent loop.

## What it refuses

An invented protocol returned a structured name-and-hint rather than a paragraph:

```json
{"error": "unknown_protocol", "protocol": "nope", "hint": "See /v1/protocols"}
```

The same document is reachable over plain HTTP as `GET /v1/changes?protocol=<id>&days=<n>`, which the free tool points at directly. Anything that needs a dashboard or a cron can skip MCP entirely, and the two surfaces share one protocol id space.

### Is this governance data or price data?

Governance. Nothing here returns a token price or a yield, and the protocols listed are included because they publish proposals to Snapshot and control upgradeable contracts, not because they are tradeable. That distinction is what makes it different from the yield and market-data surfaces this catalog already carries.

### Can it tell me who can upgrade a contract?

Yes, for the contracts it watches, and that is in the paid report as the current implementation and admin address per contract. The free half tells you whether anything moved; the paid half tells you what the current admin is. The split is deliberate and stated in the tool descriptions rather than discovered by paying.

## Why it earns a page

`governance proposal` and `proxy upgrade` returned zero hits across the whole catalog before this entry, and the 30 hits for `snapshot` were data snapshots and listing snapshots, not Snapshot the voting platform. DeFi coverage here is market data and yields; nobody was tracking the votes that change the contracts underneath them.

It earns the entry on three measured things: 32 protocols enumerated with their Snapshot spaces and watched-contract coverage, a free tier whose window argument demonstrably works, and a paid tier whose price, asset, chain and scope are all readable in the refusal without paying.
