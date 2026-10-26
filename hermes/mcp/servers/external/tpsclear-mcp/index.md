---
title: "TPSClear MCP - UK TPS Screening Before a Sales Call"
description: "Outbound-calling compliance MCP server: screen up to 1,000 numbers per call against UK TPS and CTPS and Australia's Do Not Call Register."
category: "Sales Operations / Compliance"
stars: n/a (new listing)
added: 2026-10-18
source: "mcpservers.org /all pages 1-5 (October 18, 2026 night sweep)"
relevance: ★★★
tags: [outbound-sales, tps, ctps, pecr, do-not-call, compliance, telephony, hlr, api-key, remote-mcp]
last_updated: "2026-10-19"
---

# TPSClear MCP

**A pre-dial screening server for outbound calling. It checks a list of phone numbers against the UK TPS and CTPS registers, washes Australian numbers against the ACMA Do Not Call Register, and flags mobiles that are switched off or dead, so the dialler spends its time on numbers that are both reachable and permitted.**

```
Server type: Hosted (Streamable HTTP, JSON-RPC 2.0)
Endpoint: https://tpsclear.co.uk/api/mcp
Auth: API key in the Authorization header; test keys (tpsc_test_) return fixtures for UK screening at no cost, live keys (tpsc_live_) draw prepaid balance
Tools: 6 - screen_numbers, wash_au_numbers, check_dead_numbers, get_account, set_company_name, buy_credits
Pricing: From £95/month ex VAT for 2,500 UK screening checks per 28 days, then £15 per 1,000
Docs: tpsclear.co.uk/developers and tpsclear.co.uk/pricing
Publisher: TPSClear (tpsclear.co.uk)
Listing: mcpservers.org entry (October 18, 2026)
```

## Why This Matters for Operators

Screening against the Telephone Preference Service is not a nice-to-have in the UK. Under PECR, calling a number registered on TPS or CTPS without consent is a rule breach, and the volume-based dialling that agents now make easy is exactly the activity the registers exist to constrain. The practical answer is a check before the call, recorded against a campaign reference.

The second half of the same problem is waste. A meaningful share of a purchased or aged list is dead numbers, and an agent that reasons about a calling list without knowing which mobiles are live will happily schedule work on numbers that cannot answer.

## What You Can Do Today

| Capability | What it does |
|---|---|
| Screen UK numbers | `screen_numbers` checks up to 1,000 numbers per call against TPS and CTPS and returns one state per number: clean, tps-listed, ctps-listed, unknown, suppressed or consented |
| Keep an audit record | An optional `campaign_ref` is stored on the screening record, so a campaign can be tied to the check that cleared it |
| Wash Australian numbers | `wash_au_numbers` checks numbers against the ACMA Do Not Call Register (live key only, since that register has no test mode) |
| Find dead mobiles | `check_dead_numbers` runs live HLR lookups and reports live, switched off or dead |
| Read the account | `get_account` returns balances and the company name on record |
| Top up | `buy_credits` issues a Stripe Checkout link that a person pays, so an agent cannot spend on its own |
| Test before spending | A `tpsc_test_` key returns UK fixtures for free, which lets an integration be verified before a live balance is touched |

## Business Relevance

- **Sales operations teams** can gate a calling list inside the assistant, before it reaches a dialler, rather than policing it after the fact
- **Compliance evidence:** each screening result is one of six explicit states, and the campaign reference ties a list to the check that cleared it; the vendor advertises a nightly re-check and a full audit trail on the plan
- **Cost control is structural:** agents can read balance and prepare a top-up, but a person completes the payment through Stripe, so a runaway loop cannot spend budget
- **List hygiene and permission in one step:** the same call that clears a number also tells you whether it is reachable
- **Two markets covered:** UK TPS and CTPS plus the Australian Do Not Call Register

## Integration with CorpusIQ

A calling list usually starts as CRM data, and the answer to "who should we call" is a join across systems. CorpusIQ's connectors cover the CRM, commerce and analytics side over read-only tools, so an agent can pull a segment, hand the numbers to TPSClear for screening, and return a filtered list with the reason each number was removed. The screening result is compliance evidence; the segment is the business context around it.

## Limitations

- **UK and Australia only:** there is no US DNC, Canada DNCL or EU register coverage
- **Screening is not consent:** a clean result means the number is not on the register, not that the person has agreed to be called
- **Live keys cost money:** UK screening draws prepaid credits at the plan rate, and Australian washing is live-key only
- **Account tools are write-capable:** `set_company_name` and `buy_credits` change account state; grant the key to a client you trust to hold it
- **New listing:** published in October 2026; the tool surface is current for version 1.0.0

## FAQ

### Can an agent spend money through this server?

Not by itself. `buy_credits` returns a Stripe Checkout link that has to be paid by a person, and live screening draws from a prepaid balance the account holder funded. The spend ceiling is the balance, not the agent's judgement.

### What does a screening result actually tell me?

One of six states per number: clean, tps-listed, ctps-listed, unknown, suppressed or consented. Clean is the only state that clears a cold call on its own; suppressed and consented reflect the account's own records, and listed means the register holds the number.
