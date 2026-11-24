---
title: "Codixio MCP - E-Invoices, Tariff Codes, Localization"
description: "Three EU compliance jobs an assistant can call per use: validate XRechnung with the official KoSIT validator, suggest a CN code, localize a marketplace listing."
category: "Compliance"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-24
source: "An mcp.so feed card at 2026-11-24T17:12Z for /servers/codixio-api; keyless initialize on https://api.codixio.com/mcp and its three per-service routes answering 401 with no WWW-Authenticate header; the tool names, endpoints and service scope read from https://api.codixio.com/llms.txt on 2026-11-24; billing rules, error shape and client setup from https://api.codixio.com/en/docs; prices and the minimum top-up from https://api.codixio.com/en/pricing; worked examples from https://api.codixio.com/en, all on 2026-11-24"
relevance: "★★★"
tags: [e-invoicing, xrechnung, zugferd, factur-x, tariff-code, cn-code, product-localization, germany, eu, oauth, remote-mcp, compliance]
last_updated: "2026-11-24"
---

# Codixio MCP

**Every EU invoice that crosses a border now arrives in a format someone has to validate, and the validator is a separate product from the ERP that made the invoice.** Codixio sells three narrow, unglamorous jobs as a metered API and puts the same three behind an MCP server: check an e-invoice against the official KoSIT validator, guess the EU tariff code for a product description, and rewrite a marketplace listing for another country's rules. No subscription, no seat count, one account and one key.

```
Server type: Remote (Streamable HTTP, OAuth 2.1 sign-in)
Endpoints:   https://api.codixio.com/mcp            all six tools
             https://api.codixio.com/mcp/listing    listing localization
             https://api.codixio.com/mcp/tariff     tariff classification
             https://api.codixio.com/mcp/einvoice   e-invoice
Auth:        OAuth 2.1, sign in with the Codixio API account
Tools:       localize_listing, suggest_tariff_code, get_job_result,
             validate_einvoice, create_einvoice, get_balance_and_quota
Pricing:     per call from prepaid credit, free account, no subscription
```

## The gate, measured

A keyless `initialize` refuses on **all four** routes, and it refuses in its own words rather than in JSON-RPC:

```json
{"error": "unauthorized", "error_description": "Sign-in required for this request."}
```

That is HTTP **401** with **no `WWW-Authenticate` header** on `/mcp`, `/mcp/listing`, `/mcp/tariff` or `/mcp/einvoice`, and no protected-resource document is published for the MCP host. So the client cannot discover the authorization server from the refusal the way it can with a Spacestack or a Persado. What the documentation states instead is that the server **speaks OAuth 2.1 and signs in with the Codixio API account**, and that the client **registers itself**: in Claude you enter the server address with **no OAuth client id**, choose Connect, and sign in. That is the cleanest possible outcome for a hosted MCP and the worst possible outcome for one whose vendor forgot to publish the discovery documents. A client that supports remote OAuth works; a client that needs `resource_metadata` before it will even start the flow has nothing to read and will look broken for a reason that belongs to the vendor.

The per-service routes are the useful detail. One endpoint carries all six tools and three narrower ones carry the tools for a single service plus `get_balance_and_quota`, so a team that only wants invoice validation can hand the assistant an endpoint where listing localization does not exist as a callable. The permission boundary is therefore an **URL choice at connect time**, not a scope grant inside a token. That is coarser than an OAuth scope and considerably easier to reason about before a pilot.

## The three jobs, in the vendor's own numbers

Codixio prices each call and publishes a worked example of each. All three are worth reading as specifications of what the assistant gets back.

| Service | What it returns | Maximum price per call |
| --- | --- | --- |
| E-invoice | Validate XRechnung, ZUGFeRD and Factur-X with the official KoSIT validator; create a valid e-invoice from invoice data; render one readable | **0.10 EUR** |
| Tariff classification | EU tariff code (CN and TARIC) with reasoning, alternatives and applicable import measures | **1.50 EUR** |
| Listing localization | Title, bullet points, description and search terms for a target marketplace and language | **9.90 EUR** |

**The e-invoice check is the one with an external authority behind it.** The validator named is KoSIT, the German coordination body whose open-source validator produces the `verdict`, `validation_scenario` and `findings` a finance team reads when an invoice is rejected. The vendor's own guide, dated **2026-11-15**, is about reading that report, and the site also offers a **free in-browser e-invoice check** without sign-in where the operator has enabled it. A chat assistant that validates an invoice before it is sent to a customer is a different class of tool from one that drafts a summary of the invoice, and this is the first entry in this catalog that does the former.

**The tariff service has an honest ceiling and states it in the payload.** Descriptions are accepted in any language, but **confidence `high` is assigned only to descriptions in German**; everything else is capped at `medium` with the note `confidence_capped_language`. The vendor's sample turns a German description of a 150-watt electric coffee grinder into **CN 8509 40 00** at high confidence, and the page prints the caveat that the result is *"a suggestion, not a binding tariff information and not an assessment of duties."* A vendor that caps its own confidence by input language is doing the thing this catalog keeps asking for.

**Listing localization is rule-checked, not just translated.** The service aligns a listing with the target marketplace's **publicly documented rules** (title length being the visible one) and re-checks its own output against them before answering. Each response states **which rules were applied, with source and date**, which is what makes the output auditable six months later when the marketplace changes the rule. The worked example takes a German Amazon title for a 450 ml insulated travel mug and returns a **55-character French title**, bullets, search terms, and a **review note written in the language of the request** confirming that the protected brand term was carried over unchanged. It also states plainly that acceptance by the marketplace is **not guaranteed** and the listing should be reviewed before publishing. The measurement line under the example reads **15 Nov 2026, run time 4.1 s**.

## Billing that fails closed

Read from the pricing page on **2026-11-24**: a **free account**, every call **paid individually from credit**, **no subscription**. Before a call runs, the service **reserves the current maximum price**; without cover the API answers **402**; on success the **actual** price is charged and on failure the reservation is **released**. Price changes apply only to calls reserved afterwards, so a reserved call costs at most the maximum price at the moment of reservation.

The minimum top-up is **10.00 EUR**, billing runs through **Polar as merchant of record**, which shows the VAT when credit is bought. The e-invoice service at 0.10 EUR a call is the cheapest thing in the catalogue: a thousand validations is 100 EUR. Listing localization at 9.90 EUR a call is the opposite end, so the shape of a budget is one operator's actual workload rather than a plan tier.

Two more mechanics that matter to a pilot. **Listing and tariff work asynchronously**: `POST` creates a job and answers **202** with a job id, and `get_job_result` reads status and result, so the assistant has to poll once. The e-invoice check is **synchronous**. And errors from the portal are **RFC 9457 problem details** carrying `code`, `message` and `message_language` in **German or English**, chosen by `response_language` in the body or query, else by `Accept-Language`. A German-language problem document arriving in an English conversation is a real thing that will happen, and it is the operator's call whether that is a feature.

## How to connect it

1. Create a free Codixio account and get an API key (keys start `apk_`) if the REST path is also wanted; the MCP path signs in with the account rather than the key.
2. In **Claude**, open Customize, then Connectors, choose **Add custom connector**, and enter the endpoint with **no OAuth client id**. Claude registers itself. Choose Connect and sign in with the Codixio account.
3. In **Claude Code**: `claude mcp add --transport http codixio-api https://api.codixio.com/mcp`, then sign in with `/mcp`.
4. In **ChatGPT**, turn on developer mode (Settings, Apps, Advanced settings; on Business, Enterprise and Edu an admin enables it), add a custom MCP server with the endpoint, and choose **OAuth** as the authentication.
5. Point a first, cheap pilot at `/mcp/einvoice` only. It is the narrowest endpoint, the cheapest call, and the one with a third-party verdict behind it.
6. Start with the free in-browser check and the free per-IP daily quota where the operator enabled it, then fund credit: the first real test of the meter is one invoice you know the answer for.

## Boundaries recorded

- **No discovery document at the MCP layer.** The 401 carries no `WWW-Authenticate` and there is no protected-resource document, so a client that insists on discovery before sign-in cannot be helped from our side. Recorded as a vendor gap, not a credential problem.
- **The tool list is the vendor's `llms.txt`, not a measured schema.** The endpoint refuses keyless, so the six names and their per-endpoint grouping come from the published documentation on 2026-11-24. Re-probe after any release.
- **Tariff confidence is language-bound by design.** English, French or any other description cannot reach `high`. An operator classifying non-German products should expect `medium` with a review note, and the vendor refuses to pretend otherwise.
- **The catalogue does not claim marketplace acceptance.** The vendor says review before publishing, and so does this guide.
- **`create_einvoice` writes a document, and the other two spend money.** Every tool that charges is priced per call from credit; the balance tool exists so an assistant can check before a burst, and the reservation rule is what stops a burst from overdrawing.
