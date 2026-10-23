---
title: "PourWire MCP - Restaurants and Bars Before They Open"
description: "Liquor license and permit filings fused into per-metro feeds of venues opening in the next 60 to 120 days, with the filing behind every row."
category: Data & Analytics
stars: n/a (vendor API; Tintin-Intellegence-Limited/us-liquor-license-applications has 0)
added: 2026-10-23
source: "chatmcp/mcpso submission #5993 (2026-10-23T17:06Z), plus the official MCP registry entry com.pourwire/pourwire 1.0.0"
relevance: ★★★
tags: [hospitality, restaurant-openings, liquor-license, building-permits, prospecting, lead-generation, public-records, local-data, remote-mcp, keyless]
---

# PourWire MCP

**A restaurant that has not opened is the only time a POS rep, an insurer or an equipment supplier can win the account without a fight. The filing that announces it is public, and nobody was reading it until now.**

```
Server type: Remote (Streamable HTTP) at https://pourwire.com/mcp
Auth: None for the public tier (filings older than 30 days, block-level address, no owner contacts); an API key unlocks fresh filings and owner contacts
Live check: POST initialize without a key returned HTTP 200, serverInfo pourwire 1.0.0, protocol 2025-06-18, tools capability
Tools: 2 (search_openings, metro_stats), both read-only
Pricing: Public tier free; $149 per metro per month (Scout) or $249 (Operator), annual billed as ten months, 14-day trial with no card
Vendor: PourWire (pourwire.com)
```

## Why This Matters for Operators

Every business that sells to restaurants knows the timing problem. The buying window opens when a venue is still a permit application: the equipment list is not locked, the POS is not chosen, the insurer is not bound. By the time the doors open, the decisions were made months earlier by someone the rep has never met.

The data that announces the window has always been public. State alcohol boards publish license applications, city permit systems publish build-out filings, and both were readable before this existed in any useful shape. What was missing was the join: one venue, its applications across two or three agencies, a stage, and an estimated opening window, on a page a person can actually work from.

That is the whole product, and it is the shape this catalog keeps rewarding. The value is not the raw record, it is the record reconciled, named, staged and dated, with the original filing still attached so the claim can be checked.

## What It Actually Does

Two tools, both read-only, neither requiring a key for the public tier.

`search_openings` takes a metro, an optional status and a limit. The metros are `los-angeles`, `new-york`, `austin`, `waco-temple`, `dallas-fort-worth`, `houston` and `san-antonio`. The statuses are `new`, `in_buildout`, `approved` and `opened`, and the limit defaults to 20. Each row carries the trade name, the registered legal name, the venue type, a block-level street address, city, ZIP, an estimated opening window, the stage, a confidence value, the date first filed, the filing list and a link to the venue page on the vendor site.

`metro_stats` takes the same metro and returns the tracked total, how many are new, how many were filed in the last 30 days, and which source agencies feed that metro.

The filing list is the part that makes the row usable. A row is not a scraped listing, it is a set of dated events with the agency named:

| Field | Example from a live `search_openings` call on `austin` |
|---|---|
| Business / legal name | Proper Ash / PROPER ASH LLC |
| Venue type | bar |
| Address | Drifting Wind Run, Dripping Springs, 78620 |
| Estimated opening | Dec 2026 to Feb 2027 |
| Stage | new, confidence 0.6, first filed 2026-09-23 |
| Filings | TX TABC, `liquor_license_application`, 2026-10-14, license type MB; TX TABC, 2026-09-23, MB |

`metro_stats` on the same metro returned 237 tracked venues, 154 new and 33 filed in the last 30 days, sourced from Austin DSD and TX TABC. New York returned 2,819 tracked, 124 new and 204 filed in the last 30 days, sourced from NY SLA, NYC DOB and NYC DOHMH. The source list changing by metro is the honest signal: coverage is per-agency, not a national crawl wearing a per-city label.

A second live call, on `los-angeles` filtered to `approved`, returned chain filings where the trade name is empty and the legal name carries the brand, for example CHIPOTLE MEXICAN GRILL #4864 at a Palmdale address, confidence 0.8, one `license_issued` event from CA ABC dated 2026-09-23.

## Installation

```bash
claude mcp add --transport http pourwire https://pourwire.com/mcp
```

For Hermes:

```bash
hermes mcp add pourwire --url https://pourwire.com/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "pourwire": {
      "type": "http",
      "url": "https://pourwire.com/mcp"
    }
  }
}
```

The subscriber tier takes a key on the same endpoint; the public tier needs nothing configured.

## What It Costs

| Plan | Price | What changes |
|---|---|---|
| Public tier | $0, no key | Filings older than 30 days, block-level address, no owner contacts |
| Scout | $149 per metro per month, $1,490 a year | Weekly Monday digest, web dashboard, full names and evidence, CSV export |
| Operator | $249 per metro per month, $2,490 a year | Daily digest and alerts, owner names and business contact details, webhook or Zapier into a CRM, REST and MCP access |

Annual billing is ten months for twelve. The trial is 14 days with no card and no password, and the vendor states it emails before the first charge, cancels in one click and allows a three-month pause. Seat availability is capped at five per trade per metro and published as a live table (Los Angeles 101 filings in 30 days with four POS seats left, New York 204 with two, Austin 33 with three, Dallas-Fort Worth 63 with five).

The metro cost is worth stating plainly because it changes the buyer. At $249 per metro per month, this is not a tool a rep buys for all seven markets on a whim; it is one or two territories where the coverage pays for itself in a single closed account.

## Integration with CorpusIQ

The pairing is a prospecting question that the operator's own systems cannot answer. CorpusIQ reads what the operator already owns: opportunities and pipeline from a CRM connector, invoices from QuickBooks or Stripe, campaign performance from the ad connectors. PourWire answers what is not in any of those systems yet, because the company that will appear in them next quarter filed a liquor license nine days ago.

The sequence that works: pull the operator's own won accounts for the last four quarters, ask which of them were new openings, then ask PourWire what is at the same stage in the same metro. The gap between the two lists is the territory's next ninety days of prospecting, with a filing date behind each name. Every row resolves to a source agency, so an operator can check the claim before a rep calls, which is the same evidence discipline the rest of this catalog is built around.

## Limitations

- **Public rows are deliberately stale and thin.** Filings older than 30 days, block-level address rather than a suite, and no owner contacts. The freshest signal and the person to call are the paid tier, which this sweep did not test because it does not create accounts.
- **Seven metros, three states.** New York, Los Angeles, Austin, Waco-Temple, Dallas-Fort Worth, Houston and San Antonio, from NY SLA, NYC DOB, NYC DOHMH, CA ABC, TX TABC and Austin DSD. Nothing outside those agencies is covered, and a metro's depth varies with how complete its source is.
- **`count` in `search_openings` is the rows returned, not the metro total.** A `limit` of 3 returned `count: 3` while `metro_stats` reported 237 tracked. Read totals from `metro_stats`, and page with `limit` if the full set matters.
- **Confidence is stated, not explained.** Rows carried 0.6 for an application-only venue and 0.8 where a license had been issued, and the vendor does not publish how the number is computed. Treat it as a ranking hint between rows, not a probability.
- **Chain filings arrive with an empty trade name.** The Chipotle and Sodexo rows returned `business_name: null` with the brand inside `legal_name`. Any downstream join on business name has to handle that case.
- **Fine dining and existing-venue changes are not the same thing as a new opening.** A license transfer can look like a new venue in the filing record. The vendor separates stages, but a transferred license and a new build-out reading `new` are worth checking before a rep treats one as a lead.
- **The free CSV carries the claim, not the license file.** The vendor publishes the last 30 days as a weekly CSV at `github.com/Tintin-Intellegence-Limited/us-liquor-license-applications`, described as CC BY 4.0, while the repository has no LICENSE file and no stars. Attribute to PourWire and keep the terms claim in view until a license file lands.

## FAQ

### Is it really keyless?

Yes for the public tier. `POST initialize` returned HTTP 200 with no credentials, `tools/list` returned both tools, and two `tools/call` requests returned real venue rows. It is one of the few data servers in this catalog an agent can query before anyone signs anything.

### How fresh is the public data?

The vendor's public rule is filings older than 30 days. In practice the rows returned carried filing dates from late September and mid-October 2026, so "public" means delayed, not ancient. The fresh window is the subscription.

### Can an agent read it inside CorpusIQ?

Yes. It is a standard Streamable HTTP MCP server, so it attaches as an external connector beside the operator's own systems, and the answers cite the filing agency per row. The pairing that matters is PourWire's prospective list against the operator's own historical wins, not PourWire on its own.

### Who is this actually for?

Trade sellers with a territory: POS and payments, insurance, restaurant equipment and build-out, food and beverage distribution. The vendor names those four in its own pricing page, and the seat caps per trade per metro are the same segmentation. A general-purpose analyst gets less from it than a rep with a quota.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [JENNi MCP](/hermes/mcp/servers/external/jenni-mcp)
- [disclosedby MCP](/hermes/mcp/servers/external/disclosedby-mcp)
- [CNC Compass MCP](/hermes/mcp/servers/external/cnc-compass-mcp)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
