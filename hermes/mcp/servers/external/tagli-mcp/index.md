---
title: "TAGLI MCP - A Signed, Expiring Merch Quote for an Agent"
description: "A branded-merchandise supplier that hands any anonymous agent a locked quote with a three-day expiry, a server signature and a public PDF, priced all-inclusive in ILS."
category: "Commerce / B2B Procurement"
stars: "n/a (hosted vendor endpoint; no public repository)"
added: 2026-11-19
source: "the mcp.so feed card filed 2026-11-19T17:58Z under the slug tagli-branded-merchandise-promotional-products, the official MCP registry record il.co.tagli/commerce 2.0.0 dated 2026-11-19, a keyless initialize and full tools/list on 2026-11-19, seven tools/call requests across six tools including two locked quotes and three refusals, and the vendor-hosted quote page and PDF fetched to HTTP 200"
relevance: ★★★
tags: [promotional-products, branded-merchandise, b2b-commerce, quoting, procurement, agentic-commerce, israel, ils, remote, keyless, woocommerce]
last_updated: "2026-11-19"
---

# TAGLI MCP

**Most B2B suppliers answer an agent's price question with a contact form. This one answers with a quote number, a total, an expiry date and a signature.**

TAGLI is a branded-merchandise and promotional-products manufacturer in Israel, operating as Tzafon Mapping Systems Ltd. Its MCP endpoint sells the way a sales desk sells, except the sales desk is reachable by an anonymous agent at two in the morning: search the catalog, read a product contract, get a priced offer, lock a quote, and hand a human a PDF.

```text
Server type:   remote Streamable HTTP (WordPress REST route, session id issued)
Endpoint:      https://tagli.co.il/wp-json/tagli/v1/mcp
Server:        TAGLI B2B Autonomous Commerce MCP Server 2.0.0, protocol 2025-06-18
Vendor:        Tzafon Mapping Systems Ltd. (company no. 512945767, founded 2000)
Registry:      il.co.tagli/commerce 2.0.0
Auth:          none for catalog, price and quote. Agent identity only for handshake and order intent
Tools:         10         Currency: ILS (VAT included in every quoted price)
Feed card:     mcp.so, filed 2026-11-19T17:58Z
```

## What the server says about itself

The `initialize` response carries an instructions string rather than a marketing paragraph, and it is unusually direct about where credentials belong:

> TAGLI B2B Autonomous Commerce Server (Streamable HTTP 2025-06-18). Supply agent credentials via HTTP headers (X-Tagli-Agent-Key, X-Tagli-Delegation-Token) and echo Mcp-Session-Id; never pass secrets in tool arguments.

That is the right instruction and it is stated in the right place. It also tells you the product's shape before any tool is called: there is a delegation concept, so something downstream is meant to act on a principal's behalf once that principal has authorised it.

## The ten tools

| Tool | What it does | Keyless |
|---|---|---|
| `search_products` | Machine catalog search over the WooCommerce product base | yes |
| `get_product` | Full product contract: offers, tiers, media, buy actions, taxonomy | yes |
| `get_business_profile` | schema.org Organization record: legal name, company number, founding year, endpoint registry | yes |
| `get_capabilities` | Factory machinery, printing methods, fulfilment and notification stages | yes |
| `get_commercial_offer` | Validated offer with a verified checkout URL | yes |
| `agentic_estimate` | Public price estimate from the server-side price list, no customer detail required | yes |
| `agentic_quote` | Issues and persists a locked quote with a PDF and a share link | yes |
| `agentic_handshake` | Legal-entity assertion and a budget-limited delegation mandate | needs agent key |
| `agentic_order_intent` | Order intent against a quote, gated on a server signature | needs agent key, and currently on hold |
| `agentic_order_status` | Quote and order state, authenticated through transport headers | yes, returns the hold |

None of the ten carries `readOnlyHint`, `destructiveHint` or any other annotation, and none publishes an output schema. The card is thin; the behaviour is not.

## A price, reproduced

`agentic_estimate` on product **5932** (SKU `KR5351`, a metal pen with a silicone grip and a touch tip) is the clearest single call in the surface. At quantity **100**:

```json
{
  "status": "estimate_only",
  "product_id": 5932, "variation_id": 5934, "quantity": 100,
  "pricing_model": "BuyAction V2",
  "estimated_unit_ils": 6, "estimated_total_ils": 600,
  "price_policy": {"all_inclusive": true, "includes_vat": true,
                   "includes_branding": true, "includes_shipping_to_business": true}
}
```

Six shekels a pen, VAT, logo printing, the artwork proof and delivery to the business address inside the number. At the 18 percent VAT rate that is about **5.08 ILS** of product and labour per unit, and the vendor says so in its own price-policy note instead of leaving the agent to assume a bare unit price. Quantity **50** returns a different variation (**5933**) at **7 ILS**, so the tier exists and it is disclosed.

The second product tested, SKU `SW558` (two branded pens in a gift box, product **5946**), prices at **36 ILS** a box for **50** boxes, **1,800 ILS** total, same all-inclusive policy. Two products, two shapes of tier, one consistent model.

## The quote is a real document

`agentic_quote` on the same product and quantity returned a persisted instrument, not a restatement of the estimate:

```json
{
  "status": "quote_locked",
  "quote_id": "QUO-20261119-5932-100-D00BBE",
  "agent_id": "agent-public-anonymous",
  "price_total": 600, "unit_price": 6, "currency": "ILS",
  "issued_at": "2026-11-19T18:02:39+00:00",
  "expires_at": "2026-11-22T18:02:39+00:00",
  "idempotency_key": "probe-nov19-a",
  "server_signature": "963fbdabb2571ce838fd6a8fcd2a9d990d39c0485ac45cd593bcfa7e3aac63c4",
  "state_storage": "server_persisted",
  "qb_quote_id": 7240,
  "qb_share_url": "https://tagli.co.il/q/7240/d006d44115f03b960fd109f5/",
  "qb_pdf_url": "https://tagli.co.il/wp-json/tagli/v1/public-quote/7240/pdf?token=..."
}
```

Both links were fetched and both answered **HTTP 200**: the share page as HTML, the document as a **173,955-byte** `application/pdf`. A quote an agent can email to a procurement manager without a login is the whole value of the entry, and it works.

Four properties of that response are worth copying by anyone building agent-facing commerce:

- **An expiry.** Three days from issue, stated in the payload. A price cannot be relied on forever by accident.
- **A signature.** A sha256 over the quote, which is what `agentic_order_intent` demands back as an argument, so an order cannot be conjured from a price the agent made up.
- **An idempotency key.** Supplied by the caller and echoed, so a retried call does not produce two quotes.
- **Server-side persistence.** `state_storage: server_persisted`, so the agent does not have to hold the state between turns.

## Where the surface is weaker than it looks

**The refusal withholds what it knows.** Ask for **250** or **1,000** pens and the estimate fails:

```json
{"status": "error", "error": "requested_quantity_not_available_in_package_tiers",
 "available_options": null, "http_status": 422}
```

The error names the concept and then leaves `available_options` empty, so an agent that only calls `agentic_estimate` cannot discover that **50** and **100** are the tiers - it has to guess. The recovery path exists and it is good: `get_product` publishes `offers` as a list of `{variation_id, quantity, price, unit_price}` plus `minimum_order_quantity` and `price_min` / `price_max`, so the correct sequence is `get_product` then pick a package size then quote. The guide says "package size" rather than "quantity" on purpose: this supplier sells stocked packs, and a request for any other count is refused rather than rounded.

**The catalog search is Hebrew-first.** `search_products` with `"water bottle"` returned **0** items and with `"catalog"` returned **0**; `"pen"` returned **2** only because a Latin SKU and product name carry the word. Hebrew queries work - `"עט"` returned three pens, `"חולצה"` three shirts - but `"בקבוק"` (bottle) returned a hat, a keychain and a backpack, so relevance is loose even in its own language. An English-only agent should treat search as a browse-by-SKU fallback and go straight to `get_product` with a known ID.

**Autonomous ordering is switched off.** `agentic_order_status` on a valid quote returned **403** with `code: autonomous_ordering_on_hold` and a Hebrew message stating the autonomous-ordering module is in a temporary hold by TAGLI management during the pilot. That is the vendor being honest in a machine-readable code rather than a 500, and it is the correct disclosure to publish: quoting works today, ordering does not.

**Four internal fields leak into the response.** `_caller_ip`, `_session_id`, `_request_fingerprint` and a `qb_` prefix on the QuickBooks identifiers are returned to the caller. The values are the caller's own, so nothing secret is exposed, but the prefix discloses the accounting backend and the underscore-prefixed keys read like debug output in a production payload.

## How to integrate it

1. `get_business_profile` once, to hold the legal entity (Tzafon Mapping Systems Ltd., company no. **512945767**) and the endpoint registry the vendor publishes for machines.
2. `get_capabilities` to answer "can they print on fabric, metal, glass" without a human: the document lists UV, DTF and pad printing, plus laser, a custom-branding workflow and delivery tracking through Gal Delivery with five notification stages from *ready for dispatch* to *follow-up after 30 days*.
3. `search_products` in Hebrew, or `get_product` by ID when a SKU is already known.
4. `get_product` and read `offers` for the pack sizes that exist.
5. `agentic_quote` with one of those sizes and your own `idempotency_key`. Ask for `quote_locked`, then use `qb_pdf_url` and `qb_share_url` as the deliverable to a human.
6. Do not build a flow that depends on `agentic_order_intent` until `agentic_order_status` stops returning `autonomous_ordering_on_hold`.

## Who this is for

A business that buys branded merchandise - onboarding kits, conference giveaways, client gifts - and wants a defensible number in a conversation rather than a form submission. The catalog already carries the print-on-demand side ([MarketPrint](/hermes/mcp/servers/external/marketprint-print-on-demand/) fulfils a saved design to Shopify or Etsy) and the quoting side inside an ERP ([Electronics RFQ Agent](/hermes/mcp/servers/external/electronics-rfq-mcp/)). TAGLI is the first entry where the **supplier's own catalog issues the signed quote**, which is the piece a purchasing conversation actually needs.

Limits, stated plainly: one vendor, one country, one currency (ILS), a Hebrew-first catalog, and a quote engine that will only price the package sizes it stocks.

## Sources

- Endpoint `https://tagli.co.il/wp-json/tagli/v1/mcp`, `initialize` and `tools/list` keyless on 2026-11-19
- Registry record `il.co.tagli/commerce` **2.0.0**, endpoint and website URL as published
- Seven `tools/call` requests across `search_products`, `get_product`, `get_business_profile`, `get_capabilities`, `agentic_estimate`, `agentic_quote` and `agentic_order_status`
- Quote page and PDF fetched to **200** (PDF 173,955 bytes) on 2026-11-19
- Feed card on mcp.so, slug `tagli-branded-merchandise-promotional-products`, stamp **2026-11-19T17:58Z**
