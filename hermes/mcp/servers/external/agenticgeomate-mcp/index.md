---
title: "AgenticGeoMate MCP - Australian Geoscience Data for Agents"
description: "Ninety-two tools over Australian public geoscience: drillholes, geochemistry, WA prospectivity scores and read-only SQL, behind an OAuth sign-in."
category: "Data & Research"
stars: n/a (vendor-hosted)
added: 2026-11-21
source: "chatmcp/mcpso submission #7758 filed 2026-11-21T11:00:22Z; the official MCP registry record io.github.PascalSun/agenticgeomate 1.1.0 published 2026-11-21T10:51:01Z; keyless initialize and a 92-tool tools/list, six tools/call requests refused at 401, protected-resource documents fetched 2026-11-21"
relevance: ★★★★
tags: [geoscience, mining, drillholes, geochemistry, gis, sql, australia, documented-tier]
last_updated: "2026-11-21"
---

# AgenticGeoMate MCP

**Remote MCP server (Streamable HTTP, sign-in required to execute)** - one address over Australia's public geoscience record: exploration reports from every state and territory, Western Australian drillholes and assays, geochemistry, a prospectivity model that scores ground for eight metals, and a read-only SQL surface over the same database. It is the largest single tool surface this catalogue has measured - **92 tools** - and every one of them sits behind a sign-in.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://geomate.nlp-tlp.org/mcp
Tools:       92 (listed keyless, executed with a token)
Registry:    io.github.PascalSun/agenticgeomate 1.1.0
Published:   2026-11-21T10:51:01Z
Docs:        https://geo.nlp-tlp.org/docs#agents
Platform:    geo.nlp-tlp.org (map, data catalogue, GeoThought reader)
Auth:        OAuth 2.1 with dynamic client registration; free platform
             account by email code, per the submitter
```

## Why This Matters for Operators

Exploration and mining decisions start with a question about ground: what is held, what was drilled, what came back in the assay, what the reports say, and how prospective the area is. In most of the world that work is a licence plus a GIS licence plus a week of downloads. Here it is a set of tool calls, with a prospectivity model and a SQL escape hatch on the same connection.

The tool list itself is the product brief, because the server is honest enough to publish all of it before the sign-in:

```text
tenure and title      search_tenement_holders, find_on_map
drilling              find_drillholes, find_drillhole_intercepts,
                      make_drillhole_section, get_drillhole_traces,
                      download_drillholes, find_core_scans, get_core_scan_hole
geology and geochem   get_geology_at_point, get_geochem, search_wa_data_library,
                      get_wa_library_features, get_outcrop_photos,
                      list_geophysics_grids, describe_raster, sample_raster
prospectivity         score_point, score_region, score_route, top_prospects,
                      list_targets, compare_points, get_model_inputs_at_points,
                      inspect_point, inspect_region, list_sites
reports               search_exploration_reports, document_files,
                      wamex_report_files, estimate_download, prepare_download,
                      download_status
catalogue             search_data_catalogue, get_catalogue_dataset,
                      get_place_summary, get_dataset_feature
data library          list_datasets, describe_dataset, query_features,
                      upload_data, get_download_url, get_image, export_data,
                      list_export_layers
SQL                   sql_tables, sql_describe, sql_query
long jobs             submit_job, get_job
reading (GeoThought)  24 project, schema, question, answer and reading tools
```

Two descriptions are worth quoting because they set the terms of the answer. On the SQL tool: *"Runs one read-only SELECT (or WITH/EXPLAIN) and returns the rows. Read-only is enforced by the database connection, not only checked."* On the section tool: *"The section runs along the hole's own azimuth (east-west for a vertical hole or one whose direction was not recorded)."* A model that states its own convention is a model whose output can be checked.

## Measured Behaviour

This pass measured the gate and the surface, and stopped there deliberately.

| Probe | Result |
|---|---|
| `initialize` (no token) | **200**, protocol 2025-06-18, `serverInfo.name` AgenticGeoMate |
| `tools/list` (no token) | **200**, **92** tools with full input schemas |
| `tools/call` × 6 (`list_targets`, `get_geology_at_point`, `score_point`, `top_prospects`, `find_drillhole_intercepts`, `sql_query`) | **401** every time, `{"error":"unauthorized"}` |
| `WWW-Authenticate` on `tools/call` | `Bearer realm="AgenticGeoMate MCP", resource_metadata="https://geomate.nlp-tlp.org/.well-known/oauth-protected-resource"` |
| Protected-resource document | **200**: resource `https://geomate.nlp-tlp.org`, authorization server `https://geomate.nlp-tlp.org/oauth`, `bearer_methods_supported: ["header"]`, `resource_signing_alg_values_supported: ["RS256"]` |
| Same document at the `/mcp` suffix | **200**, identical body |
| `geo.nlp-tlp.org/.well-known/oauth-protected-resource` | **404** - the document lives on the resource host |

So the tier is precise and worth naming: **discovery open, execution gated.** An agent can read the whole 92-tool surface, decide what it would ask, and only then meet the sign-in. Six different tool families were tried and every one returned the same 401, which is a global gate rather than per-tool permissions.

The server's own instructions, in full:

> AgenticGeoMate (geo.nlp-tlp.org): Australian geoscience data and exploration reports from every State and Territory, Western Australian mineral prospectivity, drillholes, geochemistry and read-only SQL, plus the user's own data library (list_datasets, describe_dataset, query_features, get_dataset_feature, get_download_url: datasets the signed-in user uploaded, plus published public ones).

The metals the prospectivity model will score are named by its own `list_targets` description - **Au, Cu, Ni, W, Sn, Co, Ta, Mn** - and the scoring tools come in four granularities (point, region polygon, route resampled every `spacing_km`, and a precomputed `top_prospects` grid), with `uncertainty` and `coverage` returned beside every score. That is the pattern to ask for from any model that produces a number about ground: the number, the coverage behind it, and an explicit uncertainty.

## Where It Stops

- **Nothing was executed.** No tool response was read this pass, so no price, assay, score or row in this guide came from the server. The guide records the surface and the gate, and says so rather than implying a measured result.
- **A free account is still an account.** The submitter describes OAuth 2.1 with dynamic client registration and an email-code sign-in; the protected-resource document confirms the authorization server and the bearer method. The account itself was not created on this pass.
- **Western Australia is the scored half.** The prospectivity model, tenements, WAMEX reports, WAROX photographs and HyLogger core scans are WA. The data library and the report corpora are national.
- **Raster sampling is capped at 50 points.** `sample_raster` takes up to fifty WGS84 points, and a point outside the raster returns no value rather than an error.
- **Long jobs are queued.** `submit_job` returns a task id and `get_job` reads the result, so a region score is a two-call workflow by design.

### Does an agent need a key, or an account?

An account. There is no API-key path in the discovery documents this pass read: the challenge names a bearer token and a protected-resource document, and that document names one authorization server on the same host. The platform's own docs describe a personal token for the REST API, so there are two credential shapes in the product - the MCP path is the OAuth one.

### What can an agent promise a user before it signs in?

The tool surface, and only the tool surface. An assistant can tell a user exactly which questions the server will answer - "score this coordinate for gold", "list the drillholes within ten kilometres", "search the WAMEX reports for a phrase" - and cannot produce one of those answers without the token. That is still useful: it turns "can you do geoscience" into a specific, checkable offer.

### Why does the tool list matter more than a homepage?

Because it carries the conventions. `find_drillhole_intercepts` states its rule for where a run starts and stops, `make_drillhole_section` states which azimuth it draws, `score_point` returns uncertainty and coverage, and `sql_query` states that read-only is enforced at the connection. Those are the four things that decide whether an agent's answer about ground is auditable.

## Catalogue Position

Geoscience and mining had no entry in this catalogue at all - the string "geoscience" appeared in no guide, no sweep section and no catalogue row before this pass. AgenticGeoMate is therefore the first of its class, and it is the largest tool surface here as well: 92 tools against a median of five to fifteen. It is recorded at the documented tier, with the gate measured and every claim about its output left to a signed-in pass.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [MCP Server Discovery - November 21, 2026 (Midday)](/hermes/mcp/sweeps/sweep-november21-2026-midday)
