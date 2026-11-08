---
title: "Worth Leaving MCP - Walk-Away Math for Unvested Equity"
description: "One deterministic tool that prices what leaving forfeits, the next vest worth waiting for, and the number an offer has to beat."
category: Finance
stars: "n/a (hosted; no public repository)"
added: 2026-11-08
source: "chatmcp/mcpso submission #6945 filed 2026-11-08T17:42:17Z; the official MCP registry record com.worthleaving/verdict 1.1.0 published 2026-11-08T17:38:20Z; the documentation at worthleaving.com/walk-away-cost; and a keyless driven call to compute_walk_away_verdict on the live endpoint that returned a full verdict, its assumptions and a share link"
relevance: ★★★
tags: [equity, vesting, compensation, offer-evaluation, deterministic, calculator, keyless, remote-mcp]
last_updated: "2026-11-08"
---

# Worth Leaving MCP

**Every other assistant that touches money does arithmetic. This one refuses to.** Worth Leaving is a single tool that answers one question an offer letter makes unavoidable: what does leaving on this date cost me, what is the next vest worth waiting for, and what does a new offer have to beat before tax. The engine is deterministic. The assistant supplies the letter's own terms and reads back a verdict, and the server's instruction says the quiet part out loud: **never compute vest dates or dollar totals yourself.**

```text
Server type: Remote (Streamable HTTP, stateless)
Endpoint:    https://worthleaving.com/api/mcp
Auth:        none (keyless, read-only, per-IP rate limit)
Tools:       1 - compute_walk_away_verdict (readOnlyHint, idempotentHint)
Registry:    com.worthleaving/verdict 1.1.0, published 2026-11-08T17:38:20Z
Protocol:    2025-06-18
Docs:        worthleaving.com/walk-away-cost
Price:       free, no account, no inputs stored
```

## The instruction is the product

The whole `instructions` string is two sentences:

> Worth Leaving computes what leaving costs in unvested equity and whether an offer is worth it. Call compute_walk_away_verdict with the offer letter's own terms; never compute vest dates or dollar totals yourself.

That second clause is the reason this belongs in the catalogue. A general assistant asked "should I leave in March" will estimate a vest schedule, multiply by an assumed price and produce a number that reads exactly like a fact. Here the tool takes the terms, **fills the gaps itself and then lists every gap it filled**, so the answer arrives with its assumptions attached instead of hidden inside a paragraph.

## Driven live, one call

A real call with a two-grant scenario, a current role and an offer side:

```json
{"leaveDate":"2026-03-01","filing":"single",
 "current":{"base":180000,"metro":"us-sfo","grants":[
   {"type":"rsu","valueUsd":200000,"grantDate":"2024-02-01","years":4,"cliffMonths":12,"cadence":"quarterly"}]},
 "offer":{"base":210000,"metro":"us-nyc","grants":[
   {"type":"rsu","valueUsd":260000,"grantDate":"2026-03-01","years":4,"cliffMonths":12,"cadence":"quarterly"}]}}
```

The answer, verbatim:

```text
Verdict: take-it (score 77/100).
Walking away on 2026-11-08 forfeits $62,500 of unvested value.
An offer has to beat $230,000 a year, before tax: what staying pays over the
next twelve months, less the housing given.
Annual net gain of the offer, after tax and housing: $28,965.
Next vest worth waiting for: 2027-02-01 ($12,500).
```

Five numbers, each with a defined meaning, produced in one round trip on a keyless endpoint. The response also carries a `structuredContent` block with `walkAwayCost`, `nextVest`, the location breakdown (`gross`, `tax`, `housing`, `discretionary` for both sides) and the resolved vest schedule the engine derived, so an agent can chart it rather than paraphrase it.

## Three answers, not one

Most offer decisions are made badly because three different questions get averaged into one feeling.

| Field | The question it answers |
| --- | --- |
| `walkAwayCost` | What does leaving on this date forfeit, in unvested value |
| `nextVest` | The next date and amount worth waiting for, so a delay can be priced |
| `offerHasToBeat` | The annual pre-tax number a new offer must exceed to be worth the move |
| `verdict` | The scored comparison, **null when there is no offer yet** |

That null matters. With no offer in the request, `hasOffer` is false and the verdict is null by design: the tool returns `offerHasToBeat` instead of inventing a comparison. A tool that refuses to answer a question it was not asked is a tool an agent can wire into a pipeline without an if-statement around it.

## What the engine takes

| Group | Fields |
| --- | --- |
| The date | `leaveDate` (required), `filing` (`single` or `married`) |
| Current role | `base`, `bonus`, `metro` (`us-sfo`, `us-sea`, `us-nyc`), `housingAnnual` |
| Grants (max 10) | `type` (`rsu`, `iso`, `nso`, `shares`), `valueUsd` **or** `shares` + `fmv`, `strikePrice` for options, `grantDate`, `vestingYears`, `cliffMonths`, `cadence`, `yearlyPercents` |
| Private stock | `isPrivate` with `privateHaircut` (default **0.3**) |
| Schedule override | An explicit `schedule` with `cliff`, `cadence`, `end` and `firstVest` (`cliff`, `even`, `backloaded` 5/15/40/40, or per-year weights) |
| The offer | Optional. Its own `base`, `bonus`, `metro`, `housingAnnual` and grants |
| Judgment | `ratings` for `growth`, `title`, `remote`, `stability`, `team`, each **-2** to **2** |

The design that follows from it is the one worth copying: **send the letter as written, do not pre-compute.** The schema accepts `yearlyPercents` "exactly as the letter states them" and a `schedule` for letters that list dates, and it forbids sending both grant terms and an explicit schedule. The engine does the arithmetic because the engine is the thing with tests.

## The assumption log is the trust surface

The live answer ended with sixteen numbered assumptions, and they are the most useful part of the response:

- The leave date given was in the past, so the figures assume leaving **today, 2026-11-08**
- Grant 1 on the current side: assumed a **public** company, valued from the dollar figure as written, a **four-year** term, even vesting
- No bonus given on either side; **assumed none**
- Treated the offer as one being explored, **not one held in writing**
- No signing bonus; none assumed
- **No view given on growth, title, remote, stability or team; compared on money alone**

Two of those are the ones that save an operator from themselves. The past-date notice is a guard, not an error: the call asked for March and the answer said so in the first line of its assumptions rather than silently computing a schedule backwards. And the ratings notice tells the reader exactly how far the verdict went: this is a money comparison unless the request said otherwise, so a "take-it" on money alone is not a life decision.

## Share links carry bands, not figures

Every response ends with a shareable link. The server's own words are that the link **carries rounded bands only**, never exact figures, and the tool description repeats it. The reason is a real one: a compensation link gets forwarded, pasted into a group chat and indexed. Bands keep the shape of the answer without publishing the person's numbers.

## Does this overlap anything already in the catalogue?

No, and the nearest neighbours are a different job each time.

[Taxley](/hermes/mcp/servers/external/taxley-mcp/) computes UK corporation tax, including salary versus dividends, for a company's money. [Worthbase](/hermes/mcp/servers/external/worthbase-mcp/) keeps a net worth balance sheet, so it holds what you already have rather than what a move would forfeit. The jobs-class entries in this catalogue ([FoundRole](/hermes/mcp/servers/external/foundrole-mcp/) and the rest of that saturated lane) search and evaluate **listings**, not a person's own grant. Nothing here prices a vesting schedule.

It is also narrow on purpose. One tool, one document type, one decision. **That narrowness is what makes it usable by an agent:** there is no state to reconcile, no account to connect, and no way for the call to succeed halfway.

## What an operator actually asks

> "I have no offer yet. What does a new one have to beat?"

That is the cleanest call in the tool: current role only, no `offer`. The answer is `offerHasToBeat`, plus `nextVest` so a founder knows whether waiting three months is cheap or expensive.

> "Here is the offer letter. Worth it?"

Send the terms as written, including `yearlyPercents` if the letter states them, plus `ratings` for the five factors. The verdict comes back scored **out of 100** with the money comparison and the non-money factors the caller supplied, and nothing else invented.

> "My options are underwater and the cliff is in six weeks."

Send the `iso` or `nso` grant with `shares`, `fmv`, `strikePrice` and `isPrivate`. The `nextVest` answer is the one that decides: it names the date and the value, so the question becomes a date rather than a mood.

## Who should not use it

Anyone who wants a life decision, a negotiation strategy or a tax return. This tool answers one question about money on a date. It also will not help outside the United States: the metros, the tax modelling and the filing statuses are US-shaped, and the engine says so by only accepting `us-*` metro ids.

## Limits recorded

- **US only.** `us-sfo`, `us-sea`, `us-nyc` and a `remote-us` id valid on the offer side only; the tax and housing model does not generalise past them.
- **One document, one decision.** No portfolio view, no multi-offer comparison in one call.
- **Money unless told otherwise.** Without `ratings`, the verdict compares compensation only and says so in its assumptions.
- **The engine is closed.** There is no public repository, so the arithmetic is trusted as a service rather than read as code. The named assumptions and the resolved `vestSchedule` in the response are the audit trail.
- **Anonymous call counting.** One count row per call is stored, inputs are not; the vendor states it and there is no account to check it against.
- **Rate limited per IP.** Fine for a decision, not for a batch of scenarios; a loop of twenty calls will meet the limit.

## Frequently asked questions

### Why one tool and not a suite?

Because the decision is one decision. A single tool means an agent can call it without choosing among surfaces, and the caller cannot half-configure a scenario. The schema absorbs the complexity instead: grant types, cliffs, cadences, per-year percentages, explicit schedules and private-company haircuts all live in one input object.

### Does it need a key or an account?

No. The endpoint is keyless, read-only and free, with a per-IP rate limit, and the tool is annotated `readOnlyHint` and `idempotentHint`, so repeating a call costs nothing but a rate-limit slot.

### What happens if I send a leave date in the past?

It computes from today and says so in the first assumption line. That is the behaviour to expect from any money tool wired into an agent: a stale date produces a stated correction rather than a silently wrong schedule.

### Can the numbers leave the machine?

Only as much as you send. Inputs are not stored, and the share link the response returns carries rounded bands rather than exact figures, which is the one output designed to be forwarded.

## Sources checked

- `https://worthleaving.com/api/mcp`: keyless `initialize` **200** as `worth-leaving` **1.1.0** on protocol `2025-06-18`; `tools/list` **200** with one tool and its full JSON Schema (draft 2020-12); `tools/call` **200** with the verdict, `structuredContent` and the assumption log quoted above (driven 2026-11-08)
- `https://registry.modelcontextprotocol.io/v0/servers?search=worthleaving`: one record, `com.worthleaving/verdict` **1.1.0**, published `2026-11-08T17:38:20Z`
- `https://worthleaving.com/walk-away-cost` and `https://worthleaving.com/privacy` (vendor documentation and data handling, read 2026-11-08)
