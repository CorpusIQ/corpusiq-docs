---
title: "Global Shopaholics MCP - Landed Cost From a US Address"
description: "Live US freight to ninety destinations, a duty table by country and a fee schedule, keyless and driven across five of seven tools."
category: "E-commerce / Logistics"
stars: "0 (hosted Streamable HTTP at https://mcp.globalshopaholics.com/mcp, keyless; seven tools, five driven, two left undriven because they open a human intake)"
added: 2026-11-18
source: "the mcp.so submission queue entry #7597 filed 2026-11-18T16:40:30Z, and a driven session on 2026-11-18 in which five of seven tools were called against the live endpoint with no credential"
relevance: ★★★
tags: [logistics, shipping, landed-cost, import-duty, ecommerce, package-forwarding, keyless, remote, mcp]
last_updated: "2026-11-18"
---

# Global Shopaholics MCP

**A buyer outside the United States sees a price in dollars and has no idea what the parcel actually costs.** The item is one number, the freight is another, the duty is a third, and the forwarder's own handling fee is a fourth that appears only at invoice time. Four vendors, four answers, and the one comparison that matters - the landed cost - exists nowhere until after the purchase.

Global Shopaholics is a US package forwarder that put its own calculator behind MCP. The useful part is not that it quotes shipping. It is that the quote, the duty rule for the destination and the fee schedule arrive together, from the same server, in one call, with the rule text attached.

```text
Server type:   remote Streamable HTTP (hosted)
Endpoint:      https://mcp.globalshopaholics.com/mcp
Server:        global-shopaholics, version 1.0.0
Protocol:      2025-06-18
Auth:          none
Tools:         7 (get_shipping_rates, estimate_landed_cost,
                  get_services_and_fees, get_started, track_shipment,
                  request_assisted_purchase, request_shipment_quote)
Warehouse:     Delaware (no US sales tax)
Website:       https://globalshopaholics.com
Listed on:     the mcp.so submission queue as #7597
```

## The evidence tier

Keyless and driven. `initialize` answered **200** with no credential and returned a written `instructions` block that states the intended flow - rates, then fees, then signup or a purchase request - and, unusually, its own payment disclosure: no payment is taken in chat, and the assisted-purchase fee is **0% for bank transfer or crypto**, otherwise 5% with a $5 minimum. `tools/list` returned seven schemas. **Five** tools were then called: `get_shipping_rates` on three inputs including one deliberately wrong, `estimate_landed_cost` twice with different argument shapes, `get_services_and_fees`, and `track_shipment`.

The two `request_*` tools were **not** driven. Both open a human intake - `request_assisted_purchase` requires a name and an email and sends a buy-it-for-me request to a person, and `request_shipment_quote` does the same for a manual quote. Neither is idempotent and neither is a read, so no request was filed and no result is quoted from them.

## A rate call returns a service ladder, not a number

`get_shipping_rates` takes `country` and `weight` as its only required arguments, with an optional city, postal code and unit. The reply carries the resolved destination - a two-letter code becomes a country name and a capital city becomes a real postal code - and then the whole carrier ladder rather than a single figure:

```text
NG, 5 kg          Abuja 900241
                  FedEx Intl. Connect Plus   $174.68   7 to 10 days
                  estimated delivery 2026-12-02

GB, 2.5 kg        London E16AN
                  FedEx                      quoted, same ladder shape
```

That delivery date is the detail worth noticing. A rate quote that returns a transit band is a quote; one that also resolves the band onto a calendar date is the thing a buyer can actually plan against.

### What happens when the destination is wrong?

It refuses by name and points at the fallback:

```json
{"error": "Unknown or unsupported destination country \"ZZ\". Use a 2-letter
 ISO code (e.g. AO, SA, GB) or a country name GS ships to.",
 "kind": "input",
 "calculator": "https://globalshopaholics.com/international-shipping-calculator/"}
```

An unknown country is a boundary the server states, and the calculator link is the recovery path for anything the tool itself cannot answer.

## The duty rule is the product, not the arithmetic

`estimate_landed_cost` builds the total from four lines: the item price, optional US sales tax, the assisted-purchase fee, and an import duty and tax band. It labels the result twice, in the payload and in the sentence, as `ESTIMATE ONLY - not a quote`.

Germany, $400 of items:

```text
items                  400.00
us_sales_tax             0.00
gs_assisted_purchase    20.00   5% of order cost, $5 minimum
international_shipping   null    (no package supplied)
import_duty_and_tax  79.80 to 139.78
total_landed_usd    499.80 to 559.78
```

What makes that band defensible rather than arbitrary is that the server also returns the rule it applied:

```text
country        Germany
tax_name       VAT, 19%
de_minimis     No VAT threshold (VAT from EUR 0). Duty-free EUR 150
               threshold abolished 1 Jul 2026; temporary EUR 3 customs
               duty per item category for consignments under EUR 150
               until 1 Jul 2028.
typical_duty   0% to 12%
```

The German threshold change is the kind of fact an operator needs and a general model will get wrong: the low-value duty exemption is gone, replaced by a flat per-category charge with an expiry date attached. The United Arab Emirates call returns the same shape with a different rule - 5% VAT, and a Dubai-only e-commerce duty exemption for goods under AED 1,000, roughly $272, from 3 August 2026.

## The fee schedule is published, including the small ones

`get_services_and_fees` with `topic: "plans"` returns both tiers with a `last_checked` date and a source URL per plan:

```text
Basic      free forever
           free US address (Delaware, no sales tax), consolidation,
           30 days free storage
           Express Processing $5 · Extra Padding $3 · Equipment Testing $10
           Detailed Item Photo $10 · Private Address 10% of items cost
           Fast Lane: 2 free packages/month then $1 each
           Insurance: $10 minimum, at most 2% of declared value
           Shipment Cancellation $10
Premium    $9.99/month
           everything in Basic, unlimited 2% cashback, 180 days storage
```

A forwarder that publishes the $3 padding fee and the $10 package photo is a forwarder whose invoice can be predicted before the parcel exists. That is the entire difference between this and calling a freight desk.

## A live quote needs a package, and a wrong argument is ignored

The first landed-cost call to the UAE included `"weight": 2` and `"shipping_mode": "cheapest"` at the top level. Both were **silently discarded** - `weight` belongs inside a `package` object and `shipping_mode` does not exist - and the reply came back with `international_shipping: null` and a total of **275.63 to 289.41** for a $250 order.

Supplying the documented shape produced a materially different answer for the identical order:

```text
destination   AE
items         250.00
gs_fee        12.50
shipping      48.58   DHL - DHL Express (3 to 5 Days)
duty and tax  15.55 to 31.88
total        326.63 to 342.96
```

**Fifty-one dollars between the two readings, and the wrong one is the one that looks finished.** The tool does not declare `additionalProperties: false` and does not warn on an unknown key, so a caller that guesses an argument name receives a total that omits the largest component. Read the reply for `international_shipping: null` before quoting the number; that null is the only signal that the total is incomplete.

## Tracking is a link, and the server says so

`track_shipment` takes a tracking number and returns carrier links for all four carriers plus the detected one:

```text
1Z999AA10123456784  carrier ups, carrier_detected "guessed_from_format"
note: GS has no public tracking-lookup page; tracking comes from the
      carrier. GS emails the tracking number when the shipment leaves
      the warehouse.
```

Returning four links and flagging the guess as a guess is honest behaviour, and the note prevents the obvious wrong conclusion - that a tracking tool which returns no status is broken.

## Where it fits

An agent that can price a US purchase end to end - item plus freight plus duty plus handling - can answer the question every cross-border buyer actually asks, which is not "how much is it" but "how much will it be in my hands". Ninety destinations of live freight and a dated duty table is a real capability for anyone reselling, importing, or simply buying from a US store abroad.

### Can it be used without an account?

Yes, for everything measured here. `initialize`, `tools/list` and all five read tools answered with no credential. An account adds a permanent US address, higher limits and a dashboard; the pricing calls do not need one.

### Does it store the order?

Only the two `request_*` tools send anything, and both send it to a person who then emails an invoice. No payment is collected in chat, and the server states that itself in its `instructions` block.

## Sources

- Endpoint: https://mcp.globalshopaholics.com/mcp
- Homepage: https://globalshopaholics.com
- Calculators: https://globalshopaholics.com/international-shipping-calculator/
- Submission: the mcp.so queue as #7597 on 2026-11-18
