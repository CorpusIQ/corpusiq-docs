---
title: "Geo-Insights MCP - Dutch Green Infrastructure Data"
description: "A keyless Dutch environmental and blue-green infrastructure catalog where five of twelve tools answer and the policy layer returns http_406."
category: "Environment / Urban Planning"
stars: "0 (hosted service; the connector repository is public)"
added: 2026-11-14
source: "the mcp.so submission #7333 filed 2026-11-14T11:54:36Z, the official registry records io.github.mathisvfr/environmental-data 1.0.0 and 1.2.0 both active and published 2026-11-14, and a live session on this host: initialize, tools/list, one tools/call per tool across all twelve, plus four measure-detail and comparison calls against https://mcp.geo-insights.nl/mcp"
relevance: ★★
tags: [environmental data, climate adaptation, blue-green infrastructure, urban heat, netherlands, knmi, luchtmeetnet, sensor community, biodiversity, municipalities, mcp, remote]
last_updated: "2026-11-14"
---

# Geo-Insights MCP

**The work of adapting a city to heat and rain is done in spreadsheets that nobody keeps current.** A municipality needs to know what a sedum roof actually retains, what a permeable pavement costs per square metre, which of forty-odd measures its own policy documents require, and what the temperature was at the nearest station last Tuesday. That information exists, but it lives in a national weather API, three sensor networks with different units, a water board's PDF and a procurement file.

Geo-Insights is a Dutch service that puts an environmental data layer and a blue-green infrastructure catalog behind one remote MCP server, keyless, so an agent can query all of it in one place. It is the first entry in this catalog for **urban climate adaptation**, a term that returns zero hits across every guide, heading and sweep note here.

The honest finding of this pass is a split: the **catalog half answers and the policy half does not**, and the sensor half was unreachable for the whole session.

```text
Server type:   remote Streamable HTTP, JSON-RPC 2.0, session header issued
Endpoint:      https://mcp.geo-insights.nl/mcp
Server:        "Geo-Insights Environmental Data", protocol 2025-06-18,
               capabilities: tools, resources, prompts, version field empty
Registry:      io.github.mathisvfr/environmental-data 1.2.0, streamable-http,
               same URL, status active, published 2026-11-14
Auth:          none, and the instructions string says so
Tools:         12
Scope:         Dutch sensor networks plus a 44-measure blue-green catalog
```

## The evidence tier

Keyless and drivable, which is the best tier available: `initialize` answered **200** with a session id and no credential, and every tool below was called at least once from a fresh session.

Five tools answered with data. Seven refused, and the refusals name their own cause:

| Tool | Result on 2026-11-14 | Cause |
|---|---|---|
| `list_sources` | answered | 4 sources returned |
| `get_parameters` | answered | 36 parameters |
| `search_bgi_measures` | answered | measure list returned |
| `get_measure_detail` | answered | full measure record |
| `compare_measures` | answered | 2 to 5 measures side by side |
| `get_latest_readings` | refused | `sensor_data_unavailable`, `http_400` |
| `get_data_freshness` | refused | `sensor_data_unavailable`, `http_400` |
| `get_readings_history` | refused | arguments require `start` and `parameter` |
| `lookup_municipality` | refused | `catalog_unavailable`, `http_406` |
| `get_policy_requirements` | refused | `catalog_unavailable`, `http_406` |
| `rank_measures` | refused | `catalog_unavailable`, `http_406` |
| `get_context_summary` | refused | `catalog_unavailable`, `http_406` |

## What the catalog half returns

`search_bgi_measures` returns measures with a 0 to 100 score per goal - flood, heat, drought, biodiversity, social, economic - each carrying a `confidence` field of `computed`, plus `data_completeness` and an `updated_at`. A sedum roof scores **75** on drought and **65** on heat against **30** on biodiversity and **12** on social; street trees score **80** on biodiversity and **70** on economic but only **18** on drought. That is the shape of a tool that is telling a municipality which goal each purchase serves rather than which measure is best.

`get_measure_detail` adds the numbers an engineer asks for. For the lightweight sedum roof:

| Field | Value |
|---|---|
| Retention capacity | 101.6 mm typical, 76.2 to 152.4 mm range |
| Peak flow reduction | 75% |
| Storage volume | 0.064 m3/m2 (minimum) |
| Typical lifespan | 15 years |
| Data completeness | 88.8 |
| Reference family | Building Solutions |

`compare_measures` puts the cost side next to it: `capex_typical` **50.0** and `opex_typical` **3.0** for the sedum roof against an extensive green roof at a lower capex, with retention, cooling effect in degrees C and infiltration rate in mm/hr on the same row.

One caution on those figures: **`capex_typical` arrives without a currency or a unit**. The number is useful for ranking measures against each other and should not be quoted as a price per square metre until the vendor states the unit.

## Why the policy tools matter more than the sensors

The reason to reach for this server is not the temperature at a station, which a national weather API gives you anyway. It is `get_policy_requirements`, which claims to extract a municipality's blue-green obligations from its own official publications, and `rank_measures`, which is supposed to weight the 44-measure catalog by a municipality's policy profile.

Both of them, and the municipality lookup they depend on, answered `catalog_unavailable` with **`http_406`** on every attempt across two separate sessions, spaced minutes apart, while `search_bgi_measures` and `get_measure_detail` answered normally before, between and after them. One catalog tool working while another reports the catalog unreachable is a partial backend, not a credential problem: there is no key to add and no scope to grant.

`rank_measures` also cannot be reached by argument alone: it needs a numeric `gemeente_code`, the only source of which is `lookup_municipality`, the tool that is down. So the recommendation layer is unreachable end to end today, even though the measure table underneath it is intact and readable.

```json
{"error": "catalog_unavailable",
 "message": "BGI catalog data source is temporarily unreachable",
 "side_effects": "none",
 "cause": "http_406",
 "fix": "Retry after 30 seconds",
 "retry_after_seconds": 30}
```

The `retry_after_seconds: 30` was not honoured by the service on retry. Recorded as a defect rather than as a temporary blip, because the same envelope came back on every call.

## What the sensor half claims and what it returns

The server's own instructions describe ten sources and 35 normalized parameters. Measured:

- `list_sources` returned **4** sources: Sensor.Community (**807** stations, **1,862** datastreams, ODbL), Ohnics (**44** stations), KNMI weather (**46** stations, **460** datastreams) and Luchtmeetnet (**103** stations, **0** datastreams).
- `get_parameters` returned **36** parameters, not 35, and includes alias duplicates: `temperature` and `air_temperature` both read *Air temperature °C*, and `humidity` and `relative_humidity` both read *Relative humidity %*.

So a model that takes the instructions at face value will overstate the coverage of the sensor layer by a factor of two and a half, and a model that takes the parameter list at face value will treat two names for one measurement as two measurements.

## Argument names that differ from the descriptions

Three tools reject the argument the description suggests, and each rejection is a pydantic validation error rather than a helpful message:

| Tool | Rejected | Accepted |
|---|---|---|
| `get_measure_detail` | `measure_slug` | `measure_id_or_slug` |
| `get_policy_requirements` | `municipality` | `gemeente_code_or_name` |
| `rank_measures` | `gemeente_code_or_name` | `gemeente_code` |

An agent that reads the tool description and sends the obvious name gets a validation error with no hint about which name is right; only `tools/list` carries the schema. Worth knowing before concluding a tool is broken.

## What an operator should use it for

- **A green-roof or permeable-paving contractor** quoting in the Netherlands: the measure catalog gives defensible per-goal scores and engineering ranges to put in a proposal, and the numbers come from the tool rather than from a marketing page.
- **A sustainability officer** building a shortlist before a council paper: `search_bgi_measures` and `compare_measures` are enough to rank options on the six goals, as long as the ranking is done by the human and not by `rank_measures`, which is down.
- **Anyone needing actual weather or air-quality readings**: not this server today. The sensor tools returned `sensor_data_unavailable` throughout.

## What does not work

- **The policy and recommendation chain** - `lookup_municipality`, `get_policy_requirements`, `rank_measures`, `get_context_summary` all refuse with `http_406`.
- **All sensor reads** - `get_latest_readings` and `get_data_freshness` refuse with `http_400`.
- **`get_readings_history`** requires `start` and `parameter`, neither of which appears in the description.
- **Version drift** - the server reports an empty version string while the registry record is **1.2.0**.
- **Coverage overstatement** - 10 claimed sources, 4 returned; 35 claimed parameters, 36 returned with alias pairs.
- **Unitless cost** - `capex_typical` and `opex_typical` carry no currency.

## Frequently asked questions

### Does Geo-Insights MCP need an API key?

No. `initialize` and every `tools/call` below answered without a credential, and the server's instructions state that no authentication is required.

### Is this the same as a national weather API?

No. KNMI and Luchtmeetnet are two of its upstream sources; the added value is the blue-green measure catalog with costs, performance ranges and per-goal scores, which no weather API carries.

### Can an agent rely on the scores being current?

Partly. Each parameter in `get_measure_detail` carries its own confidence, and each measure carries `updated_at`; the dates read 2025-12-28 and 2026-02-27 across the measures sampled here, so the catalog is a curated reference rather than a live feed.

### What would make this a full entry rather than a partial one?

The four `http_406` tools answering, and the sensor tools returning a reading instead of `sensor_data_unavailable`. The schema, the endpoint and the measure data are already sound.

## Limits recorded

Dutch jurisdiction throughout, in Dutch or English field names. The measure catalog is a reference table, not a live price feed, and the two halves of the product fail independently. No credential is needed, so nothing here is gated - the only blocker is the vendor's own backend.
