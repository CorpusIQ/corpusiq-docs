---
title: "OceanAlt AML MCP - Payment Screening for Agents"
description: "AML and compliance screening before agent payments: sanctions, mixers, scam lists, on-chain heuristics and verifiable evidence, free keyless tools."
category: Compliance
stars: n/a (npm oceanalt-aml-mcp)
added: 2026-09-30
source: "mcp.so server page (oceanalt.com)"
relevance: ★★
tags: [compliance, aml, sanctions, payments, risk-screening, evidence, crypto, self-hosted]
---

# OceanAlt AML MCP

**A verdict with verifiable evidence before money moves.** OceanAlt screens blockchain counterparties before an agent pays or receives: OFAC sanctions, known mixers, community scam and phishing lists, stablecoin issuer freezes and on-chain heuristics like address age, activity and one-hop taint. Every verdict carries a risk score, a blocked flag and clickable evidence showing which list, label or on-chain path matched. The free tools need no key and no signup, and the package installs as a local stdio server.

```
Server type: stdio (npx)
Auth: None for free tools; OCEANALT_PAYER_KEY only for paid x402 tools
Endpoint: local process (npm oceanalt-aml-mcp)
Tools: 12 (9 free keyless, 3 paid x402)
Pricing: free tools no key; paid tools $0.10 to $0.30 in USDC on Base per call
Category: Compliance
Built by: oceanalt.com
```

## Why This Matters for Operators

Autonomous payments are where fraud enters an agentic workflow, and a black-box score is not a defense. OceanAlt's answer is receipts, not scores: each verdict lists the source category and coverage date behind it, and the agent sees why an address was flagged. A clear verdict explicitly means no match in the data held at that moment, never a guarantee of safety.

The payer-side tools matter just as much. The payee readiness check returns machine-readable status codes from the public registry enforcement ladder, the calldata intent decoder compares what a transaction will actually do against what the agent believes it is doing, and the signed requirements verifier defends against payTo tampering in transit. The wallet key stays local and signs only one authorization per paid call.

## Tools & Capabilities

| Area | Free tools (no key) |
|---|---|
| Address screening | screen_address, screen_endpoint, batch screening in one call with per-address verdicts |
| Payee readiness | payee_decide: accept, decline, hold_request_info or not_ready with reason codes |
| Agent control baseline | Self-attestation check split into verified_by_oceanalt and self_claimed sets |
| Identity chain | Resolves agent, principal, mandate, credential and wallet, reporting which links hold |
| Evidence | recent_flagged sample list, signed evidence bundle verifiable offline (10/minute) |
| Payment gate | payment_decision: allow, review or decline before any autonomous payment |
| Blind-signing guard | check_calldata_intent decodes EVM and Solana transactions, verify_payment_requirements checks signed 402 headers |

Paid x402 tools: compliance_decision (full gateway decision, $0.30), deep_trace (Tron USDT up to 3 hops, $0.20) and batch_screen (up to 25 addresses, $0.10), all settled in USDC on Base.

## Installation

```bash
npx -y oceanalt-aml-mcp
```

Add it to any MCP client with the standard npx config. Free tools work immediately with no key. The paid tools need OCEANALT_PAYER_KEY in the environment, set to a dedicated low-balance wallet, never the main funds.

## Configuration

```json
{
  "mcpServers": {
    "oceanalt-aml": {
      "command": "npx",
      "args": ["-y", "oceanalt-aml-mcp"]
    }
  }
}
```

The wallet key is used only locally to sign one EIP-3009 authorization per paid call, never uploaded and never logged. Confirm live network and price at oceanalt.com/api/x402 before relying on paid tools.

## Business Relevance

- **Fintech and crypto-adjacent operators** gate every agent payment behind a compliance decision with evidence
- **Agent builders** attach a verifiable compliance attestation to settlements so payments carry proof
- **Compliance officers** get receipts, not black-box scores, with source categories per verdict
- **Treasury-minded operators** screen before receiving, since the payer address is screened in reverse on the payee side

## Integration with CorpusIQ

OceanAlt adds a payment-safety gate to CorpusIQ's financial workflow. A composed workflow: CorpusIQ reports payables and receivables from QuickBooks and Stripe, and before any agent-initiated settlement the OceanAlt decision runs first, attaching its attestation to the payment record. Operators who hold any crypto float get the same evidence-first discipline for counterparties that CorpusIQ applies to business data.

## Limitations

- Blockchain payment rail focus: EVM, Tron, Solana and Bitcoin addresses, not fiat rails
- Paid tools move real USDC over x402 and need a dedicated payer wallet
- A clear verdict means no match at screening time, not a guarantee
- Most counterparties have not published an agent control attestation, and found:false means no information, not a bad signal

## FAQ

### Do the free tools need configuration?

No. No key, no signup; install and call. The paid tools need OCEANALT_PAYER_KEY for the x402 settlement.

### Does a clear verdict mean the address is safe?

No. It means no match in the data held at that moment. The vendor states this explicitly instead of overselling.

### What does found:false mean on a control baseline check?

The party has not attested. It is absence of information, not a bad signal; never decline a payment on that basis alone.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [PolicyForge MCP - Legal Policies Generated and Audited from Your Codebase](/hermes/mcp/servers/external/policyforge-mcp/)
- [ZTDS Data Sanitizer MCP - PII De-Identification for Agents](/hermes/mcp/servers/external/ztds-mcp/)
- [Sunglasses MCP - Local Input Firewall for AI Agents](/hermes/mcp/servers/external/sunglasses-mcp/)
