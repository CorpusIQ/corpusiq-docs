---
title: "ProveCart MCP - Agent Order Checks Before Payment"
description: "Remote MCP that checks an agent's order, booking or reservation against the customer's instruction and returns a signed MATCH, REVIEW or BLOCK verdict."
category: Commerce & E-Commerce
stars: n/a (hosted vendor server, no public repository)
added: 2026-11-04
source: "mcpservers.org /all newest page slug api-provecart-com-mcp read through the r.jina.ai reader, plus a keyless driven session on https://api.provecart.com/mcp: initialize 200 as provecart 1.0.2, tools/list returning all 10 tools, provecart_scoreboard and provecart_certification_info called live with real payloads, and the three check tools refusing without an integrator key (exact error quoted in the guide), plus HTTP 200 reads of provecart.com"
relevance: ★★★
tags: [agent-commerce, order-verification, bookings, reservations, payment-gate, signed-verdict, agent-certification, remote-mcp]
last_updated: "2026-11-04"
---

# ProveCart MCP

**An agent can build a cart that looks plausible and is wrong: the wrong item, the wrong night, a table for two instead of six, terms that cannot be changed. Nothing in a normal checkout compares what the agent built against what the customer actually asked for, and the business pays to undo the difference, in returns, fees and empty slots.** ProveCart is a check that sits between the two: the customer's instruction is captured as a signed reference, the agent's cart is compared against it, and a verdict gates the payment.

```
Server type: Remote (Streamable HTTP, stateless)
Endpoint:    https://api.provecart.com/mcp
Auth:        none for initialize, tools/list, the scoreboard and the
             certification reference; an integrator API key in the
             X-API-Key header for the three check tools
serverInfo:  provecart 1.0.2 (title ProveCart)
Tools:       10
Site:        provecart.com
```

A keyless `initialize` answered **HTTP 200** as `provecart` **1.0.2** and `tools/list` returned all **10** tools, so the surface was driven rather than quoted. **The evidence tier is stated rather than implied:** the two tools that publish reference data were called live and returned real payloads (the scoreboard and the certification programme), and the three check tools answered with a refusal that names what they need, quoted verbatim below, so the check payload is schema-read and not measured.

```
{"content":[{"type":"text","text":"This tool requires an integrator API key:
 send it in the X-API-Key header of the MCP request.
 Contact ProveCart (hello@provecart.com) for a key."}],"isError":true}
```

## The verdict is three-valued, and the schema says why

`provecart_check_order`, `provecart_check_booking` and `provecart_check_reservation` each take a **mandate** (the customer's instruction) or a `mandate_id`, plus the cart, booking or reservation the agent assembled, and return one of three answers:

- **MATCH** - the cart matches the instruction; the payment proceeds and the sealed record backs the transaction.
- **REVIEW** - genuinely in-between; the case pauses instead of going through on a guess.
- **BLOCK** - a clear mismatch, such as the wrong item, the wrong day, or a price over the limit.

A non-MATCH answer carries the **Agent Correction Format**: a machine-readable `corrections` array with `dimension`, `action`, `expected`, `actual` and `reason`, a retry budget, and a pointer to the sealed evidence record, so the agent can fix the specific difference and resubmit rather than guess. The format is published as a spec at `provecart.com/standards/correction-format`.

What is compared is the same seven dimensions on every check: item, name, date, time, party size, terms and price, with category-specific rules on top (airports and fare class on a trip, room and seating details elsewhere).

## The mandate is the part that makes this different

The mandate is not a prompt, it is a structured instruction with the limits a human actually set. The order mandate carries **18** fields: `item_description`, `item_keywords`, `category`, `brand`, `max_total_price`, `currency`, `max_quantity`, `merchant_allowlist`, `merchant_blocklist`, `variant_constraints`, `category_required`, `price_basis`, `type`, `period_budget`, `period_start`, `period_end`, `expires_at` and `user_id`. That is a spend policy in the same object as the item: an allowlist and a blocklist on the merchant, a quantity cap, a ceiling on the total, an expiry, and an optional period budget with its own window for repeat purchases.

The booking mandate is the travel version and runs to **26** fields, including `origin`, `destination`, `acceptable_alternates_origin`, `acceptable_alternates_destination`, `airport_substitution`, `date_flex_days`, `departure_window`, `cabin`, `fare_terms`, `max_connections`, `min_connection_minutes`, `max_layover_minutes`, `allow_overnight_layover`, `allow_airport_change_connection` and `hotel`. The reservation mandate covers the service case in **17**: `provider_name`, `location`, `location_exact`, `time` with `time_tolerance_minutes`, `party_size` with `party_size_max`, `name_on_reservation`, `max_deposit`, `cancellation` and the price limits.

Both sides are structured, so the check is a comparison of two records rather than an opinion about a sentence. The `cart` object carries `previous_record_id` and `cart_changed` alongside `merchant`, `items`, `total_price`, `tax`, `shipping` and `fees`, which is what makes a resubmitted cart traceable to the check that rejected the earlier one.

## Certification: the exam is public, the score is measured

The other half of the server is a certification programme, and it is the part that can be driven without a key. `provecart_agent_signup` needs only `agent_name` and returns an `agent_id` plus a scoped `X-API-Key` shown once that works only for the Verified Agent endpoints on the caller's own `agent_id`. `provecart_agent_exam_start` opens a live exam session where the agent receives, per task, a customer instruction and the shopper-facing shelf of buyable options, and makes **its own** purchase decisions; `provecart_agent_exam_answer` submits them and returns a score.

Read live, the rules are specific: an agent is certified when its **latest completed live exam** scores **80 or above**, a pass is **CURRENT for 90 days** from the graded instant and then lapses, status is computed from the sealed record at read time, and renewal is a **newly generated exam, never the same one**. The fixed self-test is a system check and never certifies. Cohorts are assigned in first-pass order and never reissued. The proof surfaces are a permanent result object, a `badge.json` for Shields-style live badges, a `badge.svg`, a `share.txt`, a per-agent `trophy`, and on a pass a signed **Open Badges 3.0 / W3C Verifiable Credential** with issuer `did:web:api.provecart.com`.

The scoreboard read on 2026-11-04 was not empty, and it is more useful than a headline number:

| Agent | Score | Checks | Origin | Certification |
| --- | --- | --- | --- | --- |
| GrokBot Shopper | 100.0 | 29 | external | CURRENT, expires 2027-02-02, cohort 2 |
| ProveCart House Examinee (Claude) | 100.0 | 29 | house | CURRENT, expires 2027-02-02, cohort 3 |
| Milan Agent-Friendliness Audit 2026-11-04 | 13.8 | 29 | audit | none |
| Milan Audit Fix-Pass Probe 2026-11-04 | 11.1 | 36 | audit | none |

Two agents at 100 and two audit probes at 13.8 and 11.1 on the same exam is the evidence that the exam discriminates: a shopper agent that reads the shelf clears it, and a probe that is not trying to buy does not. The `origin` field separates external agents from house examinees and audits, so the scoreboard does not quietly mix a vendor's own runs with a customer's.

## Limits, stated

- The three check tools need an integrator key. Everything else works without one.
- It never holds or moves money. The verdict is advisory to the caller: it gates a payment only where the integrator's code calls the check first and honours the answer. Nothing in the protocol enforces that.
- The AI layer is bounded on purpose and the vendor says so: it cannot overturn a block, and when it is unsure the case stays in review. The behavioural flags it raises over an agent's traffic are advisory and never change a verdict.
- Business onboarding is a **free 90-day design-partner pilot** with a small number of slots, not a self-serve price list, so the cost after the pilot is not published on the site.
- The badge is proof of practice, not a gate: the vendor states that nobody is blocked for lacking certification and a business stays free to take any agent.
- The site is patent pending and the homepage quotes third-party research (86% of AI shopping answers contained a factual conflict, $300 median error on big-ticket items, 19.3% online returns in 2025 at roughly 30% of item value to process) which is the vendor's argument rather than a measurement this pass made.
- `provecart.com` answers **401** to a plain reader-proxy fetch, so the marketing pages were read with a browser user agent directly.

## Where it sits in this catalogue

The neighbours here are payments and reachability, not verification. [Agentcard](/hermes/mcp/servers/external/agentcard-mcp/) issues prepaid virtual cards with spend caps and human approval, which is the instrument that spends; [FiatDock](/hermes/mcp/servers/external/fiatdock-mcp/), CoinVello, SnapEX Pay and Spectra carry agent payments and wallets; ARC and Agent Outposts measure whether an agent can transact at a merchant at all. **None of them reads the customer's instruction and returns a sealed verdict about the cart**, and that is the gap this entry fills: the difference between a payment that was authorised and an order that was correct.

## FAQ

### Does it replace a fraud check?

No. It compares an order against the customer's own instruction. Fraud, authorisation, chargebacks and spend caps are the neighbours above.

### Can an agent self-approve a check?

Not for a check: the verdict comes from the server against the signed mandate, and the check tools need an integrator key. Certification is separate and deliberately self-serve.

### What happens on a REVIEW?

The case pauses for a decision rather than completing or failing, and the response names the dimension that is in-between so the agent can correct and resubmit.

### Is the evidence record usable in a dispute?

That is its purpose. Every check leaves a sealed record, and a certified pass additionally produces a signed verifiable credential.
