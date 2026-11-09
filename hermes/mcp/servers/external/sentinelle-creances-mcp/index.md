---
title: "Sentinelle Creances MCP - The Creditor Claim Deadline"
description: "French insolvency filings and the exact last day to file a claim, computed from the BODACC publication and paid per call in USDC."
category: Finance & Cash Recovery
stars: "n/a (hosted; the sample tool needs no account and no key)"
added: 2026-11-08
source: "chatmcp/mcpso submissions #6952 and #6956 filed 2026-11-08T20:09:13Z and 22:09:16Z; official MCP registry records io.github.Marcoco27/sentinelle-creances and io.github.Marcoco27/sentinelle-catnat; and the endpoints themselves, where a keyless initialize answered 200, creances_example was driven to a live record, and creances_lookup returned an x402 payment challenge"
relevance: ★★★★
tags: [france, insolvency, bodacc, accounts-receivable, credit-risk, deadlines, x402, pay-per-call, streamable-http]
last_updated: "2026-11-08"
---

# Sentinelle Creances MCP

**A supplier that is owed money by a company in liquidation has a fixed number of days to file a claim, counted from a publication most of them never read.** In France that window is two months from the BODACC notice, four months from abroad, under article R622-24 of the code de commerce, and missing it does not delay the claim, it forfeits it. This server does one thing: given a SIREN or a SIRET, it returns the proceedings and the exact last day.

```text
Server type: Remote (Streamable HTTP)
Endpoint:    https://creances.amacunia.fr/mcp
Auth:        none. The sample tool is free; the lookup tool is pay-per-call
Tools:       2 (creances_example free, creances_lookup paid)
Payment:     x402, 0.01 USDC per call on Base, no account and no API key
Sibling:     https://catnat.amacunia.fr/mcp (natural-disaster decrees, same shape)
Registry:    io.github.Marcoco27/sentinelle-creances
```

## What the endpoint says about itself

A keyless `initialize` answers **200** as `Sentinelle creances FR` **1.30.0** on protocol `2025-06-18`, and its instruction string is the whole product in two sentences: use the free sample to see the output shape, then the paid lookup for one to fifty SIREN. `tools/list` returns exactly two tools, and the schemas are honest about the split.

## Driven: the sample is a real record, not a mock

`creances_example` returned SIREN **910759158** (**ALTERNATIVE**), a **liquidation judiciaire** opened by judgment on **2026-10-29**, published in the BODACC on **2026-11-08**, before the Greffe du Tribunal de Commerce d'Evreux. The record carries:

- `date_limite_declaration` **2027-01-08** and `jours_restants` **60**, counted from the publication date rather than the judgment date, which is the detail that moves the deadline.
- `releve_de_forclusion_jusqu_au` **2027-05-08**, the register date after which the claim is struck.
- The full text of the judgment, naming the liquidator (SELARL Charlene Louveau, represented by Me Louveau, Rouen) and the electronic portal for declarations under articles L.814-2 and L.814-13.
- The source link to the notice on bodacc.fr.

The output is in French, keyed to French procedure, and every field is one an accounts-receivable clerk would otherwise assemble by hand from a public notice, a calendar and a rule they have to remember.

## Driven: the paid call is an x402 challenge, and that is the design

Called without payment, `creances_lookup` returns a standard **x402 version 2** payment requirement rather than an error:

```json
{"x402Version": 2, "accepts": [{"scheme": "exact", "network": "eip155:8453",
  "asset": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", "amount": "10000",
  "payTo": "0xa1ca...", "maxTimeoutSeconds": 300}]}
```

That is **0.01 USDC** on Base per call, with no account, no key and no subscription, and the resource description carries the legal rule in full. Three consequences follow, and they are worth naming because this is the first entry in this catalogue where the price of a business fact is one cent and the payment rail is a wallet: an accountant can check five clients for five cents; a collections team can run a nightly sweep across a whole ledger without negotiating a contract; and a business with no crypto wallet cannot use the tool at all, which is a real limitation rather than a footnote.

The argument schema is small and strict: `sirens` takes one to fifty comma-separated SIREN or SIRET numbers, `residence` takes `metropole` (the default), `etranger`, or an overseas department code such as `974`. The residence field exists because it changes the deadline from two months to four.

## The sibling: the same instrument pointed at insurance

`Sentinelle catnat FR` at `catnat.amacunia.fr` applies the identical shape to natural-disaster decrees: every arrete CatNat for a commune by INSEE code, with the 30-day home-insurance claim window and whether it is still open. Same author, same version, same free sample plus x402 lookup. For a business operator it is the property half of the same question; for a homeowner it is the whole question.

## The class it enters, with the owners named

French company data is well covered here: [OpenBase](/hermes/mcp/servers/external/openbase-mcp/) serves **20.5M** entities with identity, financials, directors, **BODACC** proceedings, public contracts and Judilibre rulings through a free keyless endpoint, and Corporary reads INSEE, INPI and BODACC as well. What neither of them does is the procedure. This entry exists for the computation the operator cannot do from memory: which judgment opened a claim window, which publication starts the clock, what the last day is, whether the increased period applies because the creditor sits abroad, and when the forclusion register closes. A company record tells you a supplier is in liquidation. This tells you whether you still have a claim.

## Limits, stated as limits

France only. The free tool is a fixed sample for one SIREN, not a free lookup. The paid tool needs a wallet on Base, so a finance team without one has to build that step first, and the payment rail is the same 0.01 USDC for one company as for fifty, which rewards batching. The server is hosted by a single author rather than a company, so a buyer should treat continuity as a question and keep the BODACC source link as the fallback it already is.

## Frequently asked questions

### How is the deadline calculated?

Two months from the BODACC publication of the opening judgment, four months for a creditor resident abroad, under article R622-24 of the code de commerce. The response returns the judgment date, the publication date, the computed last day, the days remaining and whether the increased period applied, so the arithmetic can be checked rather than trusted.

### Can it be used across a whole ledger?

It accepts up to fifty SIREN or SIRET numbers per call, comma-separated, which makes a supplier list or a customer ledger a small number of calls rather than a list of lookups.

### Does it need an account or a key?

No. The sample needs nothing, and the paid tool takes its payment in the request through x402 rather than through a subscription, which is why there is no sign-up screen in this guide.

### What does it not do?

It does not file the claim, draft it, or tell you whether the claim will be admitted. It returns the proceeding, the deadline, the liquidator and the source, which is the part that has a clock on it.
