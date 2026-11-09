---
title: "CBAM Data MCP - EU Carbon Border Cost per Import Line"
description: "Price the EU carbon border adjustment for one import line: a CN code, origin, tonnage and year become certificates and euros."
category: Finance
stars: "n/a (hosted; keyless free tier at 3 calls a day, Developer key for the rest)"
added: 2026-11-09
source: "chatmcp/mcpso submission #7001 filed 2026-11-09T14:26:23Z; the OpenAPI document at cbamdata.eu/openapi.json (1.3.0); the vendor docs at cbamdata.eu/docs; and the endpoint itself, where a keyless initialize answered 200 with six tools and cbam_resolve returned a priced import line"
relevance: ★★★
tags: [compliance, carbon, cbam, customs, import, eu-regulation, emissions, remote-mcp]
last_updated: "2026-11-09"
---

# CBAM Data MCP

**A business that imports steel, aluminium, fertiliser, cement, hydrogen or electricity into the EU owes a carbon certificate for every tonne of embedded emissions, and the number moved twice this year: the default emission values changed under Reg (EU) 2025/2621 and were corrected again by Reg (EU) 2026/1740, the benchmark changed, and the certificate price is set quarterly from the EEX auction. CBAM Data turns that into one call: CN code, origin, tonnage, year, and an answer carrying certificates and euros.**

```text
Server type: Remote (Streamable HTTP) and local stdio
Endpoint:    https://cbamdata.eu/mcp
Protocol:    2025-11-25
Server:      eu.cbamdata/cbam 1.0.0
Auth:        none for cbam_resolve and cbam_status inside 3 calls a day;
             Developer plan key for the other four tools
Tools:       6
Registry:    manifest at cbamdata.eu/server.json
Docs:        cbamdata.eu/docs, OpenAPI 1.3.0 at cbamdata.eu/openapi.json
Local:       npx -y @cbamdata/mcp  (stdio, CBAM_API_KEY)
```

## What the endpoint says about itself

This is one of the few entries here that answers without a key, so the tier is measured rather than declared. A keyless `initialize` returns `200` with the server name `eu.cbamdata/cbam` at version `1.0.0` and an instruction block that is the product in one line: calculate emissions and certificate cost, verify Annex I coverage, read the certificate price, read the default values, read the dataset change feed. `tools/list` returns all **six** tools.

The free tier is real but narrow, and the vendor states the arithmetic in the OpenAPI document: without a key each IP gets **3 calls a day** to `/v1/resolve` and `/v1/eudr/resolve` together, while `/v1/status` and `/openapi.json` are free. The other data endpoints return `401 UNAUTHORIZED` and say why:

```text
cbam_scope  ->  401
{"code": -32001, "message": "This endpoint needs a Developer plan API key.
                            Without a key, only /v1/resolve answers"}
```

The fourth call of the day returns `429` in the same voice: `3 free calls a day, and this one is over it`. A Developer plan carries **50,000 calls a month** shared by every key on the account, the Importer plan is the web app with no API access, and a key without an active plan gets `403 PLAN_REQUIRED`.

## The six tools

| Tool | What it answers |
|---|---|
| `cbam_resolve` | Emissions, certificates and euro cost for one CN code, origin, tonnage and year. |
| `cbam_scope` | Whether a CN code sits in Annex I, and which sector family it belongs to. |
| `cbam_certificate_price` | The latest published Commission certificate price, sourced from EEX EU ETS auctions. |
| `cbam_defaults` | Search the Commission default emission values under Reg (EU) 2025/2621 as corrected. |
| `cbam_changes` | The dataset change feed, one entry per amendment to scope or default values. |
| `cbam_status` | The active dataset version, build date, row counts and latest price period. |

## Driven: one import line priced end to end

The call below is a live answer from this pass, not an example from the docs. 100 tonnes of hot-rolled flat steel (CN `72085120`) from China in 2026:

```text
# CBAM Calculation for CN 72085120 (iron_steel)
- Origin: CN (Default row: CN)
- Quantity: 100 tonnes in year 2026
- Per-tonne emissions: 3.5057 tCO2e/t (direct: 3.5057, indirect: 0)
- Total emissions: 350.570 tCO2e
- CBAM benchmark (Reg (EU) 2025/2620): 1.37 tCO2e/t (route C)
- CBAM factor (Directive 2003/87/EC Art. 10a(1a)): 97.5%
- Free allocation adjustment (Art. 31): 133.575 tCO2e
- Emissions subject to CBAM: 216.995 tCO2e
- Required certificates: 217
- Certificate price: EUR 82.32/tCO2e (period: 2026-Q3)
- Total compliance cost: EUR 17,863.44
```

Every line names the instrument that produced it, which is what makes the answer usable in a cost sheet rather than in a conversation. The same call on the four-digit heading `7208` does not guess. It returns `partial` and lists the twenty in-scope eight-digit children, which is the difference between a tool that answers and a tool that invents a code.

`cbam_status` answered keylessly in the same pass with the dataset state:

```text
CBAM Data version: 2026-10-19.451099948819.
Scope rows: 572, Default rows: 10910.
Latest price: EUR 82.32 (2026-Q3).
```

## The dataset behind it

- **Scope.** **572** Annex I CN codes in six families: iron and steel **479**, aluminium **58**, fertilisers **27**, cement **6**, electricity **1**, hydrogen **1**. A code comes back `in`, `out` or `partial`, and a partial answer lists the covered children.
- **Thresholds.** A **50 tonne** de minimis applies to iron and steel, aluminium, fertilisers and cement; electricity and hydrogen carry none.
- **2028 mark-up.** The vendor publishes the phase-in as a column: **30%** for iron and steel, aluminium and cement, **1%** for fertilisers, **30%** for electricity and hydrogen once 2028 arrives.
- **Default values.** **10,910** Commission default emission values, with route C used where the regulation offers alternatives, and the regulation number attached to the row.
- **Price.** The certificate price comes from EEX EU ETS auction results, published quarterly. The pass measured **EUR 82.32** for 2026-Q3 against a documented 2026-Q2 value of **EUR 75.28**, so the number moves and the answer says which period it used.
- **Versioning.** Each answer carries `meta.dataVersion`, the publication date plus a content hash (`2026-10-19.451099948819` in this pass, `2026-09-15.d560045608f6` in the vendor's documented sample). `/v1/changes` is a feed of one entry per dataset version, so a stored answer can be tied to the data that produced it.
- **Filing date.** The resolved block includes `declarationDeadline` (the documented sample returns `2028-09-30` for a 2027 import), which turns a cost into a calendar item.

The API behind the connector is plain `GET` JSON on seven documented paths: `/v1/resolve`, `/v1/eudr/resolve`, `/v1/scope/{cn}`, `/v1/defaults`, `/v1/certificate-price`, `/v1/changes` and `/v1/status`. The second regulation on it is EUDR, Reg (EU) 2023/1115, the deforestation due diligence file, served by the same shape: scope and duties for a commodity and an origin.

## Why this matters for operators

An importer finds out what CBAM costs at the customs declaration, which is the worst possible moment to learn a number. The compliance cost on the line above is **EUR 17,863.44** on a hundred tonnes of steel: not a rounding error, and not something a purchasing team can leave to an annual review. The decisions it should change are made months earlier, when the supplier, the route and the tonnage are chosen.

The second reason is that the arithmetic is not obvious to anyone outside customs. Free allocation is still being phased out, so the certificates owed are not total emissions; the benchmark for the product route subtracts from what you owe, and the factor applied to that benchmark changes with the year. An assistant asked to "work out the carbon cost of this shipment" without the regulation will produce a number that looks right and cannot be defended. This connector returns the intermediate lines, each tagged with the article, so a person can check the work instead of trusting the total.

## The class it enters, with the owners named

Carbon is not unclaimed here, and the distinction matters. [CarbonMeld](/hermes/mcp/servers/external/carbonmeld-mcp/) reads corporate emissions out of documents, which is the reporting side: what did we emit, from what evidence, for a disclosure. CBAM Data answers a different question with a different instrument: how much does the border charge for this consignment, and which regulation set the number. On the trade side, [Tariff Monitor](/hermes/mcp/servers/external/tariff-monitor-mcp/) stacks MFN, Section 301 and Section 232 duty rates for a local HTS lookup, and the catalogued Customs MCP serves classification and landed cost; a carbon certificate is a third charge on the same import line, evaluated against emissions rather than a duty schedule. [frag.hugo](/hermes/mcp/servers/external/frag-hugo-mcp/) and [DutyKit](/hermes/mcp/servers/external/dutykit-mcp/) carry the dated compliance calendar and the policy gate, and neither prices a border adjustment.

## Limits, stated as limits

Three free calls a day per IP, which is enough to try the thing and not enough to run a book of imports, so production use means a Developer plan and a key. Four of the six tools need that key, so scope checks, default-value search and the change feed are closed to a keyless client. The answer uses Commission default values unless verified installation-level emissions are supplied, which is a conservative estimate rather than the importer's actual figure. It prices the certificate; it does not file the CBAM declaration, hold an authorised declarant identity or read the CBAM registry. And the vendor's own plan structure puts the web app on a separate Importer plan, so an ERP integration is a Developer subscription, not the calculator.

## Frequently asked questions

### Can an assistant answer what CBAM costs without a paid key?

Yes, for three calls a day: `cbam_resolve` and `cbam_status` answer keylessly, and `cbam_resolve` returns the full calculation with certificates and euros against the latest bundled certificate price. Everything else, including the scope lookup and the default-value search, needs a Developer plan key.

### What happens when I give it a four-digit CN heading?

It refuses to guess. `7208` returns `partial` with the twenty in-scope eight-digit children listed, and the answer says the code requires a more specific child, which is the behaviour that keeps a wrong classification out of a declaration.

### Which certificate price does the answer use?

The latest quarterly price bundled with the active dataset version, named in the answer (`2026-Q3`, EUR 82.32 in this pass). Prices come from EEX EU ETS auction results, the dataset version carries a date and a content hash, and `/v1/changes` lists every version so a stored answer can be traced to the data behind it.

### Does it cover the deforestation regulation as well as carbon?

Yes, through a separate endpoint and a separate tool argument set: `/v1/eudr/resolve` follows Reg (EU) 2023/1115 and returns scope and duties for a commodity and origin, which is the same shape applied to a different regulation.

### Is this a filing tool?

No. It calculates the obligation and the cost. The CBAM declaration, the authorised declarant identity and the registry filing stay with the importer or their customs agent, and the connector's job is to make the number arrive before the declaration rather than after it.
