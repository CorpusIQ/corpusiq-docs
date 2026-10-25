---
title: "HotelVALORA MCP - Hotel Valuations With a Verifiable Receipt"
description: "Institutional hotel valuation as nine read-only tools: NOI and cap rate, five-year USALI P&L, levered IRR and MOIC, comp sets, market ADR and RevPAR, and what-if scenarios, with every full analysis carrying a public hash a reader can check."
category: Finance / Real Estate
stars: n/a (commercial, MCP included from Premium)
added: 2026-10-25
source: "mcservers.org /all listing (night sweep, October 25 2026) + live 401 probe, RFC 9728 discovery and authorization-server metadata on the endpoint + official registry"
relevance: ★★
tags: [hotels, valuation, real-estate, finance, noi, cap-rate, usali, underwriting, oauth, verifiable-receipt]
---

# HotelVALORA MCP

**A valuation you can hand to a sceptic.** Nine tools that value a hotel asset the way an institution does, and stamp every full analysis with a code and a hash so a third party can confirm the figures came from here and were not edited.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://www.hotelvalora.com/api/mcp   (use the www host)
Auth:        OAuth 2.1 with RFC 9728 discovery and dynamic client registration, or an hvk_ API key
Protocol:    initialized refused with 401 unauthenticated in this sweep
Tools:       9, read-only and ephemeral
Registry:    com.hotelvalora/mcp 1.0.0, active
Built by:    HotelVALORA (hotelvalora.com)
Coverage:    Madrid (Spain) and New York (USA), expanding
```

## Why This Matters for Operators

Hotel valuation is a business where the number and the credibility of the number are two different assets. An operator shopping a property to a lender or a buyer does not only need an NOI and a cap rate. They need the other side to believe the arithmetic.

Most valuation tooling answers the first half. This server answers both: the model output, and a receipt. Each full analysis is served with a code of the form `HV-…` and a SHA-256 hash of the figures it served, and anyone, with or without an account, can check that code at the vendor's verify page. If an AI quotes a cap rate from here and the client is suspicious, the client resolves it in one click rather than a phone call.

That is the same argument this catalog makes about answer provenance in general, applied to one vertical: a figure is worth more when the reader can trace it.

## What It Actually Does

Probed live in this sweep. Unauthenticated `POST https://www.hotelvalora.com/api/mcp` returned HTTP 401 `{"error":"invalid_token","error_description":"No authorization provided"}`. The discovery documents answered properly:

- `GET /.well-known/oauth-protected-resource/api/mcp` returned HTTP 200 with `resource: https://www.hotelvalora.com/api/mcp`, `authorization_servers: ["https://www.hotelvalora.com"]`, `bearer_methods_supported: ["header"]`, `scopes_supported: ["read","write"]` and `resource_documentation` pointing at the account's API-key page.
- `GET /.well-known/oauth-authorization-server` returned HTTP 200 with `authorization_endpoint` `/mcp/authorize`, `token_endpoint` `/api/mcp/oauth/token`, `registration_endpoint` `/api/mcp/oauth/register`, `revocation_endpoint` `/api/mcp/oauth/revoke`, `response_types_supported: ["code"]`, `grant_types_supported: ["authorization_code","refresh_token"]` and S256 PKCE.

The redirect trap the vendor documents was also confirmed rather than assumed: `POST https://hotelvalora.com/api/mcp` without the `www` returns HTTP 307 to the `www` host, and a client that follows the redirect drops the `Authorization` header on the way, which is exactly the failure the docs warn about. Use `www` in the URL, always.

| Tool | What it returns | Quota |
|---|---|---|
| `search_assets` | Candidate assets and their identity record | free |
| `get_asset` | One asset's identity and characteristics | free |
| `get_report` | The full sealed analysis: value opinion, NOI and cap rate, €/key, €/m², five-year USALI P&L, levered underwriting with IRR and MOIC, and the validity date and provenance fields | one distinct asset |
| `get_compset` | The competitive set the valuation rests on | one distinct asset |
| `get_market` | Market and submarket aggregates: census, ADR, occupancy, RevPAR | free |
| `adjust_scenario` | A CAPEX what-if with its own receipt | per the plan |
| `goal_seek` | The entry price that yields a target IRR | per the plan |
| `export_report` | A link to the watermarked institutional PDF with its receipt | per the plan |
| `list_own_usage` | Tier, consumption and limits | free |

The pricing model follows the tools: quota is measured in distinct assets analysed, not calls, so re-asking the same question about the same hotel costs nothing. That detail matters for an agent, which tends to repeat itself.

## Installation

Add the remote server URL to any MCP client:

```
https://www.hotelvalora.com/api/mcp
```

For claude.ai: Settings → Connectors → Add custom connector, paste the URL, and the OAuth consent is discovered automatically. For clients without OAuth, an `hvk_` API key from the account's API-keys page goes in the `Authorization: Bearer` header.

## Business Relevance

The operator cases are narrow and real: buy-side screening before a broker pack exists, a sanity check on a seller's asking price, or a what-if on a renovation budget where the question is how much CAPEX a 15 percent IRR can carry. The hotel-use valuation of an office or residential building is the less obvious one and the more useful in a soft office market: what is this building worth if it became a hotel, fitted automatically against cadastre data.

Because every figure arrives with a validity date and a provenance field, the right behaviour is to quote it as-is, with the receipt code, rather than to recombine it into a new number. An assistant that mixes two sealed reports into a third figure has produced something nobody can verify.

## Integration with CorpusIQ

This is the cleanest example in the catalog of an answer that carries its own proof. Ask for a valuation through a connected assistant, then hand the receipt code to the lender: the claim and its evidence travel together instead of the claim travelling alone. It is also a working precedent for the pattern this catalog argues for elsewhere, that a cited figure and a checked figure should be the same figure.

## Limitations

- No tool call was executed. Every tool that touches an asset needs an authenticated account on a paid tier, so this sweep verified the endpoint, the discovery documents and the documented surface, not the output.
- Coverage is Madrid and New York only. Anywhere else and `search_assets` has nothing to return; the vendor describes this as expanding, which is a statement about the future, not the present.
- Spanish is the primary language of the documentation and the vendor's site; the English landing page exists but the tool descriptions were read in Spanish.
- An institutional valuation is an opinion with a method behind it, and the vendor says in its own instruction block that it is informative analysis and not investment advice. An operator signing a loan on the strength of one report is using it beyond its stated purpose.
- The `adjust_scenario` and `goal_seek` tools produce figures that are not the sealed report, so their receipts cover the scenario rather than the asset. Mixing a scenario number into a report citation breaks the verification chain.
- The class is adjacent but not identical to what the catalog already carries: `valuation-api-mcp` offers deterministic IRR, NPV, DCF and WACC maths, and `dfx-real-estate-mcp` covers US parcels and recorded sales. Neither values an operating hotel with a USALI P&L, which is the capability this entry adds.

## FAQ

### Do I need the www in the URL?

Yes. The non-www host returns a 307 redirect, and clients drop the authorization header when they follow it, which shows up as an unexplained 401.

### How is quota counted?

By distinct assets analysed, not by calls. Asking again about the same hotel does not consume quota again.

### Is the analysis a certified appraisal?

No. It is an institutional-grade analysis with a stated method, a validity date and a public hash. The vendor states it is informative and not investment advice.

### What does the receipt actually prove?

That the figures an assistant quoted were served by HotelVALORA and have not been altered since, which is a narrower and more useful claim than "the valuation is correct".

## See Also

- [Valuation API MCP - Deterministic Finance Math for Agents](/hermes/mcp/servers/external/valuation-api-mcp/)
- [DFX Real Estate Intelligence MCP - US Property, Parcel](/hermes/mcp/servers/external/dfx-real-estate-mcp/)
- [Skywalk MCP - AppFolio Data for Property Managers](/hermes/mcp/servers/external/skywalk-appfolio-mcp/)
