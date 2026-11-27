---
title: "Outscraper MCP - 29 Business-Data Tools, One OAuth Gate"
description: "Twenty-nine business-data tools over Google Maps, reviews, contact enrichment and Yellow Pages, discovery open keyless and every call gated behind OAuth."
category: "Business Data"
stars: "n/a (vendor-hosted; no public repository for the MCP surface)"
added: 2026-11-27
source: "mcpservers.org canonical slug outscraper-mcp-google-maps-business-data read on 2026-11-27; official registry io.github.outscraper/outscraper-mcp-server 0.2.3; keyless initialize 200 as outscraper 1.0.0 on protocol 2025-03-26 and a keyless 29-tool tools/list at https://api.outscraper.com/mcp on 2026-11-27, with four tools/call attempts answering 200 with isError true; protected-resource document read the same day; pricing model read from https://outscraper.com/pricing/"
relevance: "★★"
tags: [business-data, google-maps, lead-generation, enrichment, reviews, local-seo, remote-mcp]
last_updated: "2026-11-27"
---

# Outscraper MCP

**Local business data is usually bought one job at a time: a scraper for places, another for reviews, a third for contact emails, a fourth for technology detection. Outscraper already sold all of those as separate APIs, and its MCP server puts twenty-nine of them behind one OAuth grant with a price-asking router in front, so an assistant can check what a query will cost before it spends anything.**

```
Server type:  Remote (Streamable HTTP)
Endpoint:     https://api.outscraper.com/mcp
Registry:     io.github.outscraper/outscraper-mcp-server 0.2.3
Auth:         OAuth 2.1 (bearer), scopes businesses.read, profile.read, requests.read, services.run
Discovery:    initialize 200 and a 29-tool tools/list with no credential; every tools/call refused without one
Tools:        29
```

`initialize` answers **200** at protocol **2025-03-26** as `outscraper` **1.0.0** with `tools.listChanged: false`, and the full `tools/list` answers without a credential. The server is the API surface of a pay-as-you-go data platform: the vendor's pricing page states no monthly fees and no recurring billing, with free tiers that reset every 30 days per service.

## What the twenty-nine tools cover

Read from the keyless `tools/list`, grouped by the job they do rather than the order they are listed:

| Group | Tools |
|---|---|
| Business search and preview | `search`, `fetch`, `search_businesses`, `search_businesses_full` |
| Service router | `discover_services`, `get_service_schema`, `run_service` |
| Account and spend | `pricing_get`, `balance_get`, `requests_get`, `requests_list` |
| Google Maps | `google_maps_search`, `google_maps_reviews`, `google_maps_photos`, `chain_info`, `google_places_by_domain` |
| Enrichment | `emails_and_contacts`, `emails_validator`, `company_insights`, `phones_enricher` |
| Reviews elsewhere | `yellowpages_search`, `trustpilot_reviews`, `trustpilot_data`, `tripadvisor_reviews`, `booking_reviews` |
| Search and jobs | `google_search`, `google_search_images`, `indeed_search` |
| Technology detection | `builtwith` |

The annotations are honest about what spends money. `search`, `fetch`, `search_businesses`, `discover_services`, `get_service_schema`, `pricing_get`, `balance_get`, `requests_get` and `requests_list` carry `readOnlyHint: true`; `search_businesses_full` carries `readOnlyHint: false` with `destructiveHint: true` and `idempotentHint: false`, and the billable scrapers (`google_maps_search`, `emails_and_contacts`, `run_service` and the rest) carry the same shape. A client that respects annotations will ask before it charges an account.

## The gate opens after discovery, not before it

Four calls were attempted with no credential, each returning **HTTP 200 with `isError: true`** and the same sentence: *"Authentication required: provide a valid OAuth access token."*

| Call | Arguments | Result without a token |
|---|---|---|
| `search` | `{"query": "coffee shops, Austin, TX"}` | `isError: true`, authentication required |
| `search_businesses` | `{"query": "dentists", "location": "Scottsdale, AZ", "limit": 3}` | `isError: true`, authentication required |
| `discover_services` | `{"query": "reviews"}` | `isError: true`, authentication required |
| `pricing_get` | `{}` | `isError: true`, authentication required |

The refusal is a clean in-band error rather than a transport 401, which matters for two reasons: a client that only inspects HTTP status will read every call as succeeded, and a client that renders only the `content` block will show the sentence to the user, which is the better failure. Nothing on this server is usable on an unauthenticated path, so the entry is documented at the discovery tier and not driven.

### Does the free preview work without a token?

No, and this is the defect worth recording. Five tool descriptions advertise a free, masked preview that needs no payment: `search` calls itself a *"Free catalog preview for a natural-language query"*, `fetch` promises a *"free, masked preview for a business by ID"*, and `search_businesses` is the *"default business search returning a free preview with masked business and enrichment data"*. On this endpoint all three refused without a token, exactly like the tools that bill. Either the free preview lives inside an authenticated account's allowance rather than on an anonymous connection, or the descriptions are written for the paid key path and read as anonymous by anyone browsing the tool list. A customer who connects expecting a free look should be told which one it is.

### A registry remote that does not answer

The official registry publishes the remote as `https://mcp.outscraper.com/mcp`, and that host answers **404** with an HTML page for a JSON-RPC `initialize`. The same request against `https://api.outscraper.com/mcp` answers **200** with the JSON result quoted above, and `https://mcp.outscraper.com/` serves the vendor's setup page. A client that follows the registry record literally will report a dead server; the working address is the API host. The protected-resource document confirms it, published at `https://api.outscraper.com/.well-known/oauth-protected-resource/mcp`:

```json
{"resource":"https://api.outscraper.com/mcp","authorization_servers":["https://api.outscraper.com"],
 "scopes_supported":["businesses.read","profile.read","requests.read","services.run"],
 "bearer_methods_supported":["header"]}
```

**The scopes are the useful part.** Four grants separate looking up business records, reading the account profile, reading request history, and running a billable service, so an assistant can be given a read-only research role while the ability to spend stays with a human.

## The router is the design

Most data vendors ship one tool per endpoint and let the tool list grow. This one ships **both**: named shortcuts for the popular jobs, and a schema-driven router for everything else. `discover_services` takes a query, tags, a limit up to ten and a cursor; `get_service_schema` returns one service's parameters and schema version at no charge; `run_service` starts an asynchronous request against that version; `pricing_get` returns organisation-specific rates, the recorded free allowance and optional cost estimates; `requests_get` pages a finished result without additional usage. An assistant that is asked "what would this cost" has a tool for the question, which is rare on a scraping platform and is the reason this entry exists.

Two details in the schemas deserve a line. The billable tools take `query` as an **array** of 1 to 1,000 strings in one request, so batching is the intended unit of work rather than a loop of single calls. And `booking_reviews` says plainly that *"bare hotel IDs or slugs are unsupported by the active worker"* and wants full Booking.com URLs, which is a vendor documenting its own worker limit instead of failing quietly.

## What this pass could and could not drive

- **Read keyless:** `initialize` (200), the **29-tool** `tools/list` with full descriptions, input schemas and annotations, and the protected-resource document.
- **Refused keyless:** four `tools/call` attempts across a read tool, a preview tool, the router and the pricing tool, all 200 with `isError: true`.
- **No payload was driven.** No business record, review or price figure appears in this entry, because none was returned. Issuing an OAuth grant on a vendor's behalf is not something this pass does.

## Frequently asked questions

### Is connecting Outscraper safe for business data?

Safest reading of the evidence: the scope split lets an account holder grant `businesses.read`, `profile.read` and `requests.read` without `services.run`, and the annotations mark every billable tool as non-read-only. A deployment that wants research without spend has a documented way to get it. What cannot be verified from outside is the server's own handling of returned records, so treat the output as third-party data about third parties, which is what it is.

### What does it cost at volume?

The vendor sells pay-as-you-go with no monthly fee, free tiers that reset every 30 days per service, and per-service unit prices. The MCP server exposes those prices to the assistant through `pricing_get` and the balance through `balance_get`, which is more transparent than a pricing page and the reason the router is worth using rather than memorising the shortcuts.

### Does it replace a CRM connector?

No. It finds and enriches companies and contacts, including emails, phones, firmographics, technology stack and reviews; it does not hold a pipeline, notes or deals. The honest pairing is enrichment into a CRM that already speaks MCP, not a replacement for one.

## See also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
