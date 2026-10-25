---
title: "RevClamp MCP - Stripe Revenue Leakage and Chargeback Proof"
description: "Nine deterministic tools that audit unpaid usage, lint Visa CE 3.0 dispute evidence against the 18000-unit ceiling and reconcile B2B net terms in cents."
category: Finance / Revenue Operations
stars: n/a (commercial, free audit tier, hosted)
added: 2026-10-25
source: "chatmcp/mcpso submission #6110 (October 25 2026) + live keyless MCP session on api.revclamp.com + official registry entry + vendor manifest, pricing and onboarding pages"
relevance: ★★★
tags: [stripe, revenue-leakage, chargebacks, visa-ce3, vies, vat, shopify-b2b, net-terms, webhooks, finance-ops]
---

# RevClamp MCP

**The money that never arrives because nobody checked.** RevClamp answers four questions an operator asks after the invoice goes out and before the books close: is a customer using the product without paying for it, will this chargeback survive the network's evidence rubric, is this VAT number real enough to zero-rate, and did the wholesale order clear its deposit before the warehouse released it.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://api.revclamp.com/api/mcp
Transport:   JSON-RPC 2.0 over HTTP
Auth:        none for a stateless sandbox, Bearer rg_liv... workspace key for tenant data
Tools:       9 deterministic tools
Built by:    RevClamp Enterprise (revclamp.com)
Registry:    io.github.revclamp/revclamp-mcp
```

## Why This Matters for Operators

Most finance connectors read a ledger. RevClamp does arithmetic on a decision.

That distinction is the whole product. A ledger connector tells you what happened. These tools take the raw shape of a billing situation, a past due subscription with usage events behind it, a dispute with prior transactions and a deadline, a wholesale order with a deposit threshold, and return the state plus the reason. The output is a record with named fields, not a paragraph of advice.

Two of the checks are constraints that a person usually gets wrong. Visa Compelling Evidence 3.0 requires at least two prior undisputed transactions with matching IP and device fingerprint, and the access activity log field carries a hard ceiling that is not measured in bytes. The second is the reason disputes get thrown out after a perfect answer was written, because the field overflowed.

## What It Actually Does

The endpoint was driven in this sweep, without a key. An unauthenticated `POST initialize` to `https://api.revclamp.com/api/mcp` returned HTTP 200 with `serverInfo` `revclamp-mcp` 1.20.6 on protocol `2025-06-18` and a tools capability with `listChanged: false`, and `tools/list` returned nine tools in 22 KB of schema. Every response carries `mode: stateless_sandbox`, `statelessEphemeralAudit: true` and `tenantId: null`, which is how the vendor separates a live tenant from an evaluation.

Seven of the nine tools were executed with real arguments.

| Tool | What it decides |
|---|---|
| `revclamp_audit_revenue_leakage` | A 90 day read only audit across subscriptions, usage events and open disputes, returning customers scanned, ghost leak events, affected customers and estimated bleed in dollars |
| `revclamp_evaluate_ghost_usage` | One customer against the Stripe 2025-03-31.basil entitlement rules with a configurable 0 to 14 day dunning grace window |
| `revclamp_stage_stripe_dispute_ce3` | Compacts prior charge history into a CE 3.0 evidence draft and stages it with `submit: false` |
| `revclamp_lint_dispute_evidence` | Checks a dispute evidence payload against the 18,000 UTF-16 code unit ceiling and the CE 3.0 rubric |
| `revclamp_validate_eu_vat_vies` | Normalises an EU or XI VAT number and returns a reverse charge decision with the consultation record |
| `revclamp_reconcile_b2b_net_terms` | Integer cent reconciliation of a wholesale order against its deposit threshold, credit notes and payment terms |
| `revclamp_verify_webhook_signature` | HMAC-SHA256 verification for Stripe, Shopify and RevClamp webhooks with a replay window |
| `revclamp_simulate_webhook_replay` | A 72 hour state machine replay that shows what a naive handler does with duplicate or out of order events |
| `revclamp_calculate_roi_and_plan_fit` | Value protected against a contingency agency fee and the plan tier the event volume fits |

The results are specific enough to check by hand. A wholesale order of 250,000 cents paid at 75,000 with Net-30 terms returned `state: DEPOSIT_CLEARED_ACTIVE`, `requiredDepositCents: 75000`, `remainingBalanceCents: 175000`, `fulfillmentHold: false`, `releaseHoldAction: true` and the tag `b2b_net_terms:deposit_cleared`, which is the exact decision a warehouse needs to release or hold the pallet.

A dispute evidence payload returned `utf16CodeUnits: 19113` against `maxUtf16Ceiling: 18000`, `withinCeiling: false`, and `overallVerdict: FAIL_UTF16_OVERFLOW` while the rubric itself passed with `priorMatchedCount: 2`, `hasIpMatch: true` and `hasDeviceMatch: true`. That is the useful failure mode: the evidence was strong and the submission would still have been rejected for size.

A signature check on a Stripe style payload computed from a test secret returned `signatureValid: true`, `timingSafeCompared: true`, `toleranceSeconds: 300`, `withinReplayWindow: true` and the payload SHA-256, and the same call with a wrong `v1` value returned `signatureValid: false` with `HMAC_SIGNATURE_MISMATCH`. The response also names the integration trap it sees most: letting a framework parse and re-serialise the body before verification, which breaks the digest.

The replay simulator is the sharpest demonstration in the set. Two copies of an event older than the idempotency horizon were both dropped with `EXPIRED_OUTSIDE_72H_DEDUP_WINDOW`, the final status stayed `unprovisioned`, and the response reported what a naive handler would have concluded from the same stream: `naiveFinalStatus: active`, `naiveFinalTier: growth_59`, `naiveHandlerBug: APPLIED_EXPIRED_REPLAY_OUTSIDE_72H_WINDOW`. A stale webhook would have granted a paid tier for free, and the tool names that outcome rather than describing it.

The VIES tool is honest about the thing that matters in a tax file. A Greek number sent as `GR123456789` normalised to `EL123456789` and came back `status: FORMAT_VALID_UNVERIFIED`, `zeroRateAllowed: false` and `reverseChargeReason: LOCAL_FORMAT_CHECK_ONLY_NO_LIVE_VIES_CONSULTATION`. A format check does not authorise a zero rate, and the tool says so instead of returning a green light.

One guard is worth knowing before the first call. Passing a secret that looks live into a sandbox request returned a JSON-RPC error `-32602` with `LIVE_SECRET_FORBIDDEN_IN_SANDBOX`, described as a zero trust guard that refuses production credentials as tool arguments. So webhook verification in the free tier only accepts test material, and live secrets stay in the workspace.

## What It Does Not Do

RevClamp is not a Stripe connector. It does not read an operator's Stripe account through an API key. Its tools take the relevant objects as arguments, or read telemetry the operator forwards into RevClamp, through a webhook guard or `POST /v1/events/ingest`. An assistant asking "how much did we collect last month" will not find that answer here, and no tool lists customers or invoices.

There is no OAuth. `/.well-known/oauth-protected-resource` on the API host returned HTTP 404 `NOT_FOUND`, so the connection is a workspace key pasted into the client configuration, not a consent flow that a finance lead can grant and revoke per user.

The staging tool drafts evidence and never submits it. `submit: false` is the design, not a default that can be flipped from the chat, and the vendor states that no tool mutates Stripe, Shopify or any external system.

Outside `LIVE` mode the VIES tool is a deterministic simulation, and the modes are deliberately exhaustive: `FORMAT_ONLY`, `VALID`, `INVALID`, `MS_UNAVAILABLE` and `GLOBAL_MAX_CONCURRENT_REQ` exist so an operator can rehearse the circuit breaker behaviour when the Commission's service answers HTTP 200 with an error wrapper, which is the failure the real API produces most often.

Scope is B2B and subscription commerce. Shopify reconciliation covers Net-15, Net-30 and Net-60 in euro cents. There is no equivalent for other currencies, other billing platforms or payroll.

## Pricing

| Tier | Price | Volume | Included |
|---|---|---|---|
| Free Audit | $0/month | 5,000 events | 90 day leak detection, VAT format normalisation, all nine MCP tools |
| Starter | $19/month | 100,000 events | Signed unpaid account lock, non-destructive CE 3.0 staging, live VIES validation and outage hold |
| Growth | $59/month | 1,000,000 events | Custom 0 to 14 day grace rules, quarterly VAT report, Shopify B2B net terms reconciliation |
| Scale | $199/month | 5,000,000 events | Multi-subscription guard, two tier CE 3.0, remote MCP |

Every tier is flat rate with a stated 0 percent commission on recovered disputes, against the 25 to 30 percent contingency that a chargeback agency charges. The ROI tool reproduces the comparison: 10,000 dollars of monthly won disputes at a 25 percent fee is 2,500 dollars of commission against a 59 dollar Growth plan. Payment is by card through Lemon Squeezy as merchant of record, or in USDC on Base, Arbitrum, BSC, Polygon and Ethereum.

## How to Connect

Keyless evaluation needs no account. A client pointed at the endpoint can call the read only tools immediately, which is how this guide was produced.

```json
{
  "mcpServers": {
    "revclamp": {
      "type": "streamable-http",
      "url": "https://api.revclamp.com/api/mcp"
    }
  }
}
```

Tenant data needs a workspace key, minted free with no email required from the vendor's `/dashboard`, or by `POST /v1/tenants/provision`. The key goes in as `Authorization: Bearer rg_liv...`, and the same console issues the `whsec_rg_...` signing secret that the webhook guard uses. A stdio install is also published as the npm package `revclamp-mcp`, and the manifest at `https://revclamp.com/.well-known/mcp.json` lists the tarball and its SHA-256 for anyone who prefers to pin the artefact.

## Who Should Connect This

A B2B SaaS with usage based billing who suspects dunning is leaking usage. A merchant whose chargebacks arrive without an evidence process. A Shopify Plus wholesaler whose net terms live in a spreadsheet. A European seller who needs a VIES decision on record before zero rating an invoice.

Anyone who only wants to read revenue should use a ledger connector instead. The catalog carries QuickBooks, Xero and Stripe readers already, and RevClamp is the layer after those, not a replacement for them.

## FAQ

### Does RevClamp need my Stripe secret key?

No. No tool accepts a Stripe API key, and the sandbox refuses live secrets in arguments with a named `LIVE_SECRET_FORBIDDEN_IN_SANDBOX` error. The relevant billing objects or forwarded telemetry are the input, which keeps a production credential out of the chat transcript entirely.

### Can an assistant submit a chargeback response on its own?

No. The staging tool writes a draft with `submit: false` and the vendor states there is no mutation of Stripe, Shopify or any external system. A person reviews and submits the evidence.

### Is the VAT check a real VIES lookup?

Only in `LIVE` mode. The default and the other four modes are deterministic simulations built to rehearse format checks and member state outages. The decision record states which mode produced it, and a format only result sets `zeroRateAllowed: false`.

### How is this different from a receivables or VAT connector?

Paidnice chases invoices that were already issued and honest-vies validates a number. RevClamp works on the three records that sit between them: unpaid usage on a subscription that is still live, dispute evidence measured against the network rubric, and a wholesale order measured against its deposit gate. It is a decision layer, and the catalog had nothing that priced a chargeback in those terms.

---

**Source:** submission `#6110` in the chatmcp/mcpso window, then read live on 2026-10-25: keyless `initialize` and `tools/list` on `https://api.revclamp.com/api/mcp`, seven tool executions with real arguments, the vendor manifest at `https://revclamp.com/.well-known/mcp.json`, the official registry entry `io.github.revclamp/revclamp-mcp` (active, published `2026-10-25T02:54:03Z`), and the pricing and onboarding pages.
