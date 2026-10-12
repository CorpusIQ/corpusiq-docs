---
title: "Placestack MCP - US Parcel, Zoning and Permit Data"
description: "Parcels, owners, assessments, permits and zoning for any US address: cited due-diligence data for property, land and development operators."
category: Real Estate Data
stars: n/a (new listing)
added: 2026-10-12
source: "mcp.so /feed (Oct 12, 2026 midday sweep)"
relevance: ★★★
tags: [real-estate, parcels, zoning, permits, due-diligence, land-records, property-data, remote-mcp]
---

# Placestack MCP

**Remote MCP server (Streamable HTTP, OAuth sign-in)** - parcel, permit and zoning data for any U.S. address: resolve a parcel and read owners, assessments and sales; read the zoning at a place with permitted uses and dimensional standards; pull building and trade permits; and follow zoning and development cases such as rezonings and variances.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (sign in with a Placestack account on first connect)
Endpoint: https://mcp.placestack.com/mcp
Tools: 14 (parcels, zoning, permits, cases, jurisdictions, account)
Pricing: 1 credit per lookup; 1 credit per 20 search results; jurisdictions and suggestions free
Website: placestack.com (pricing at placestack.com/pricing)
Listing: mcp.so /feed (Oct 12, 2026 midday sweep)
```

## Why This Matters for Operators

The county records the parcel. The town zones it. The city issues the permits. Piecing that together for one site is already an afternoon, and doing it across a shortlist is a week. The data exists, but it lives across hundreds of county and municipal systems that each publish differently.

Placestack assembles the layers behind one address: parcels with owners, assessments and sales; the zoning that applies, including permitted uses and dimensional standards; building and trade permits; and zoning and development cases such as rezonings and variances. The point is the same data any diligence file needs, asked for in plain language and answered with the record.

For a buyer, that is a faster read on what a site is and what has been happening on it. For a developer, it is the zoning stack and the case history around a parcel before an offer. For an agent or broker, it is the same due diligence at the speed of a conversation instead of a records request.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Parcels | find_parcel and get_parcel: parcels by address, parcel number, point, area or filter, with owners, assessments, sales and boundaries; resolve_parcel_batch handles up to 500 addresses or parcel numbers in one call |
| Zoning | find_zoning and get_zoning: the zoning at a place, with permitted uses and dimensional standards |
| Permits | find_permit and get_permit: building and trade permits |
| Cases | find_case and get_case: zoning and development cases, such as rezonings and variances |
| Jurisdictions | find_jurisdiction and get_jurisdiction: counties, cities and towns, and the data available for each |
| Account | whoami, get_usage and find_request: the connection, credit balance and request log |

## Installation

```
claude mcp add --transport http placestack https://mcp.placestack.com/mcp
```

In any other MCP client, add a remote server with the URL `https://mcp.placestack.com/mcp`, then sign in with your Placestack account. The first connect opens the browser sign-in; the client reuses the credentials from then on.

## Configuration

```json
{
  "mcpServers": {
    "placestack": {
      "type": "http",
      "url": "https://mcp.placestack.com/mcp"
    }
  }
}
```

Sign-in happens through Placestack OAuth on first use. Lookups and searches draw on the account's credit balance, which `get_usage` reports inside the session.

## Business Relevance

- **Real-estate investors and agents** read parcel history, assessments, sales and permit activity for a site before making a call on it
- **Developers and land-use teams** get the zoning stack, dimensional standards and the rezoning and variance cases around a parcel
- **Property managers and insurers** check zoning and permit records as part of condition and compliance work
- **Consultants and researchers** answer land questions for clients from the record rather than from a records request queue

## Integration with CorpusIQ

Placestack covers the land-record layer that a business question usually lacks: what a site is, who owns it, how it is zoned and what has been filed on it. CorpusIQ answers the operator question from connected sources such as Gmail, Drive, Sheets and CRM, so a site evaluation that starts in email or a spreadsheet can pull the parcel and zoning facts alongside it.

Used together: ask CorpusIQ for the business view (the deal thread, the numbers in the model) and ask Placestack for the record view (parcel, zoning, permits, cases). Placestack stays the source of record for land data; CorpusIQ remains the place the rest of the question is answered alongside.

## Limitations

- OAuth account required; there is no keyless tier and lookups draw on a credit balance
- United States coverage; each county and municipality publishes differently and freshness varies by jurisdiction
- Brand new listing with no track record yet
- Data is assembled from public county and municipal sources; verify against the primary record before legal or contractual use

## FAQ

### What does Placestack cover?

Parcels with owners, assessments and sales; zoning with permitted uses and dimensional standards; building and trade permits; zoning and development cases; and jurisdictions with the data available for each, nationwide in the U.S.

### How is it priced?

Lookups cost 1 credit and searches cost 1 credit per 20 results; jurisdictions and suggestions are free. Pricing details sit at placestack.com/pricing, and `get_usage` reports the balance in the session.

### What can an agent do end to end?

Resolve one address or a batch of up to 500, pull the parcel record, check the zoning and what it permits, list permits and cases, and answer who owns what. All 14 tools are documented on the listing and appear in the connected client.

### Does it require a key?

No key. The connection is OAuth: the first connect opens a Placestack sign-in and the client reuses those credentials.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - all catalogued business-relevant servers
