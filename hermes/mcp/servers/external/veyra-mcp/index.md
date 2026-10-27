---
title: "Veyra MCP - Spend Limits for an Agent That Can Pay"
description: "Agent payment permission layer: per-payment and daily caps, auto-approve and ask bands, approvals that lapse, and an audit log of every decision."
category: Finance / Agent Payments
stars: n/a (free plan, Pro, Team)
added: 2026-10-27
source: "live MCP probes on veyra.money/api/mcp (initialize 200, tools/list 200 with seven tools, tools/call 401 MISSING_CREDENTIAL), official MCP registry entry io.github.zapxlabs/veyra 0.1.0, and the vendor documentation at veyra.money/docs"
relevance: ★★★
tags: [agent-payments, spend-control, approvals, usdc, base, audit-log, policy, containment]
last_updated: "2026-10-27"
---

# Veyra MCP

**The first question an operator asks about an agent that can pay is what stops it, and this server answers with a policy document rather than a promise: a per-payment cap, a daily cap, a band that auto-approves, a band that asks, and a log of every decision either way.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://veyra.money/api/mcp
Transport:   JSON-RPC over POST
Auth:        Bearer endpoint credential (veyra_...), no OAuth
Tools:       7, read live from tools/list
Rails:       USDC on Base; simulated rail for testing
Built by:    Zapx Labs (veyra.money)
Registry:    io.github.zapxlabs/veyra version 0.1.0
```

## Why This Matters for Operators

Every agent capability in this catalog stops at the same boundary: the assistant can read, draft and recommend, but a human moves the money. Spend trackers such as AgentLedger record what happened; this server is the one that decides whether the payment happens at all. The moment an agent pays for a dataset, an API call or another agent's work, two things arrive together - real money leaving, and nobody able to reconstruct afterwards who authorised what.

Veyra is one of the first servers to answer both with a policy engine rather than an instruction in a prompt. The important part for an operator is not that it can pay. It is that the limits are enforced server-side, that over-limit requests are refused rather than argued with, and that policy changes are logged with the values before and after.

## What It Actually Does

This is the rare remote endpoint that answers without a credential more than it refuses:

- `initialize` returned HTTP 200 with `serverInfo: {"name":"veyra","version":"0.1.0"}` on protocol `2025-06-18`.
- `tools/list` returned HTTP 200 with seven tools: `get_capabilities`, `get_budget`, `list_payment_sources`, `create_payment`, `get_payment`, `list_payments`, `cancel_payment`.
- `tools/call` on `get_budget` without a credential returned HTTP 401 `{"error":"MISSING_CREDENTIAL"}`, so the schema is public and the account is not.

The tool descriptions carry the operating rules rather than leaving them to documentation: `get_budget` returns "remaining daily allowance and policy summary. Read-only. If blocked by limits, ask the human user - do not retry", and `list_payment_sources` returns masked sources only with "never request secrets".

Payment status is one of `pending`, `awaiting_approval`, `submitted`, `confirmed`, `confirmed_simulated`, `failed`, `cancelled` or `expired`.

## The Containment Model, in the Vendor's Own Terms

Three bands and one honest caveat.

- **Under the auto-approve maximum:** the payment proceeds without a human prompt, still inside the per-payment and daily caps.
- **Inside the ask band:** `awaiting_approval` with a one-time link, which lapses after 24 hours if nobody acts.
- **Over the ask band or the daily cap:** blocked. The policy is enforced server-side, so the agent cannot exceed what the account owner set.
- Limits must stay consistent - auto-approve at or below ask, ask at or below per-payment, per-payment at or below daily - and a policy that violates that is rejected with a reason at edit time rather than failing later at payment time.

The part worth quoting to any operator considering this: auto-pay works by granting a capped ERC-20 `approve` to a relayer the vendor operates. The token contract caps **how much** the relayer may move, and nothing the vendor does can exceed it. It does **not** cap **who** it may move funds to - that is decided by the policy engine. The vendor states this plainly and points at the recipient allowlist as the control that constrains destination. Below the auto-approve maximum on the Free plan, every payment takes the wallet path instead, where the operator signs each transfer and Veyra only verifies the receipt.

## How It Is Contained

- **Non-custodial.** Funds never pass through a vendor-controlled balance; the operator's wallet is the source of every transfer.
- **Simulated rail is labelled everywhere.** A mock source settles instantly, returns `confirmed_simulated` with `simulated: true`, and shows as Simulated in the dashboard. The tool description tells the agent never to report that as a real payment or offer its reference as proof.
- **Audit log with the events that matter.** History is 7 days on Free, 90 on Pro, a year on Team with CSV export, and the events to watch are the ones that widen authority: `source.allowance_granted`, `agent.policy_updated` (with limits before and after) and `agent.credential_rotated`.
- **One stablecoin on one network.** USDC on Base only, chosen so limits are exact instead of needing a live price feed.

## Limitations Recorded

- No payment was created. Every money-moving path needs an account and a wallet, so the rail behaviour is documented rather than exercised here.
- **An allowance caps the amount, not the destination.** The vendor's own documentation makes this the single thing to size deliberately: treat the float as money you are willing to lose and use the recipient allowlist.
- **Base and USDC only.** An operator whose vendors invoice in fiat, or who settles on another chain, gets nothing from it.
- **Approval links are bearer-by-possession.** The approve page needs no login, by design: the secret token plus the matching wallet plus the on-chain receipt is the authentication.
- An approval nobody acts on lapses in 24 hours, which is a safety property and also a way to lose a time-sensitive purchase.

## FAQ

### Is this a wallet for the agent?
No. The agent never holds a key or a seed phrase; it holds an endpoint credential whose spending authority was set by the account owner.

### What happens when the agent hits the limit?
`get_budget` reports it and the payment is blocked or placed in the ask band. The tool description instructs the agent to ask the human rather than retry.

### Can I test it without spending money?
Yes. The mock source settles on a simulated rail and returns `confirmed_simulated`, which the vendor labels in the API, the dashboard and the tool description.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [AgentLedger MCP - per-agent spend management and audit trail](/hermes/mcp/servers/external/agentledger-mcp/)
- [CorpusIQ connectors for payments and finance data](/hermes/mcp/)
