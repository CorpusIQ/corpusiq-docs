---
title: "Zip-Codes.com MCP - US ZIP and Address Data"
description: "Zip-Codes.com validates a US address to ZIP+4 and returns the census tract, income, districts and schools behind it from USPS data."
category: Data & Analytics
stars: n/a (proprietary hosted service)
added: 2026-10-21
source: "chatmcp/mcpso issue #5818 (submitted 2026-10-20T18:23Z)"
relevance: ★★★
tags: [location-intelligence, zip-codes, address-validation, census-data, demographics, local-marketing, remote-mcp, read-only]
last_updated: "2026-10-24"
---

# Zip-Codes.com MCP

**A model asked for a ZIP Code will invent one. This server answers from USPS data refreshed monthly and Census boundaries, and an address that does not exist comes back as no match rather than as a plausible-looking invention.**

```
Server type: Remote (Streamable HTTP), stateless, read-only at https://mcp.zip-codes.com/mcp
Auth: none for the shared demo (deeper fields withheld); free API key gives 2,500 credits a day
Live check: POST initialize returned HTTP 200 (serverInfo zip-codes 1.0.0); a keyless tools/call zip_lookup code 90210 returned Beverly Hills CA, Los Angeles County (FIPS 06037), 3,516 ZIP+4 records and 10,643 active delivery points
Tools: 11 (zip_lookup, validate_address, quick_zip, radius_search, distance, suggest_places, zip_facts, about_data, city_name_rules, county_reference, metro_area_reference)
Pricing: free key at 2,500 credits a day; Developer $49/mo (100,000 credits), Professional $149/mo, higher tiers on request
Vendor: Zip-Codes.com
```

## Why This Matters for Operators

Any business that runs on geography eventually asks a model a location question, and this is the class of question models answer worst: which ZIP a customer is in, which county a site sits in, what a territory's income profile looks like, which school district a store draws from. The failure is quiet, because an invented ZIP Code looks exactly like a real one.

The second problem is that the address data most systems hold is dirty. A one-line address with a missing suite, a misspelled street or no ZIP is normal in a CRM export, and matching it to anything downstream requires standardising it first. `validate_address` returns the standard form and the ZIP+4, or it returns a low-confidence match with no ZIP+4, or no match. It does not repair an address that does not exist.

The third is territorial analysis. Census ZIP area files (ZCTA) exclude ZIP Codes with no area of their own, which is exactly the PO Box and single-organisation ZIPs that show up in B2B data. This server includes them, and it returns how much of a ZIP lies inside each county, district and metro rather than pretending a ZIP belongs to one.

## What It Actually Does

`zip_lookup` answers everything attached to a code: city, state, county and FIPS, multi-county flag, coordinates, area codes, elevation, metro area fields, ZIP classification, land and water area, ZIP+4 count and delivery point counts split into business, residential, PO Box, single-family and multi-family. On the 90210 probe this returned 3,516 ZIP+4 records and 10,643 active delivery points, of which 1,472 are business.

Enrichments are opt-in per call and each one adds a credit: `census` (tract, block group, place, county, CBSA), `cd` (congressional district), `state_leg` (state legislative districts), `school_district`, `timezone`, and the American Community Survey profiles (`acs_demographic`, `acs_social`, `acs_economic`, `acs_housing`), each available for any year from 2011 to 2024 under the same field paths, so years and places compare directly.

Around that: `validate_address` parses and places an address string, `quick_zip` reads a ZIP+4 back to its street ranges or turns coordinates into the code containing them, `radius_search` finds codes near one, `distance` measures between two, and `suggest_places` resolves a vague or misspelled place name first. Canadian FSAs and postal codes work too, with Statistics Canada geography and federal electoral districts instead of US equivalents.

`about_data` and `zip_facts` are free and keyless and state each dataset's authority, edition and refresh cadence, which is what a citation should rest on rather than an assumption about currency.

## Installation

```bash
claude mcp add zipcodes --transport http https://mcp.zip-codes.com/mcp
```

The shared demo answers without a key, with deeper values withheld and demo codes returning full depth. A free key removes the withholding.

## Configuration

```json
{
  "mcpServers": {
    "zipcodes": {
      "type": "http",
      "url": "https://mcp.zip-codes.com/mcp",
      "headers": {"Authorization": "Bearer <key>"}
    }
  }
}
```

## Business Relevance

- **Local and multi-location marketing** teams size a trade area and pull the income, housing and demographic profile behind it instead of guessing from a map.
- **Sales operations** clean and standardise address lists to ZIP+4 before territory assignment or territory rebalancing.
- **Retail site selection and franchise development** compare candidate locations on census tract economics and school districts.
- **Analytics and BI teams** join business data to census geography without buying and reconciling boundary files.
- **B2B data teams** validate an address as real rather than plausible, which is the check that stops invented ZIPs entering a pipeline.

## Integration with CorpusIQ

CorpusIQ already carries the business's own geography: Shopify orders and Stripe revenue by location, GA4 and Search Console demand by region, CRM records with addresses. The missing piece is a trustworthy join key and a profile for the place. This server supplies both, so a question like which metros drive repeat purchase and what those metros look like becomes a single composed query rather than an export and a spreadsheet.

The other direction is verification. When CorpusIQ reports on customers or leads by region, running the addresses through `validate_address` first removes the invented and malformed codes that otherwise inflate one territory and hollow out another.

## Limitations

- Proprietary hosted service under its own terms, not open source.
- One place per call on the MCP surface; long lists need the REST API's batch endpoints, which the MCP server deliberately does not expose.
- Keyless demo withholds deeper fields (masked text, null numbers, truncated lists) with a `meta.demo.withheld_count` marker, so an unkeyed answer is not the answer.
- Address validation and the Census survey estimates are US only; Canada covers postal geography.
- Usable without a key only for a few calls per question, since the demo is shared.

## FAQ

### Is the keyless data real or a sample?

Real. The shared demo returns current curated data, with some deeper fields withheld and marked. Demo codes such as 90210 or 10001 return full depth without a key, so the shape and depth of a keyed response can be inspected before signing up.

### What happens when an address does not exist?

It comes back as no match, or as a low-confidence match with no ZIP+4. The server does not invent a code, which is the whole point for a pipeline where a wrong ZIP silently misroutes a territory or a shipment.

### Can it tell me which county a ZIP is in when the ZIP spans two?

Yes, and it reports both views: the USPS assignment and the boundary intersection with `pct_of_zip` per county, district or metro. When the two disagree the honest answer is both rather than one.

### Does it cover Canada?

Yes. Canadian FSAs and postal codes are supported with Statistics Canada geography, including federal electoral districts. Address validation and the Census survey data are US only.

## See Also

- [Kirah Local Services MCP](/hermes/mcp/servers/external/kirah-local-services-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
