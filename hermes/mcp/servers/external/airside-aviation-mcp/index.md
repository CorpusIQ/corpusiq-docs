---
title: Airside Labs Aviation Tools MCP - Provenance-Backed Aviation Reference Data
description: Hosted MCP server with 22 tools that resolve airports, airlines, aircraft types, registrations and flight designators to canonical entities with confidence, alternates, validity dates and per-field provenance, plus airport facts cited to public documents and a 6,700-case aviation AI use-case atlas screened against the EASA AI framework.
category: Location Data
stars: n/a (new listing)
added: 2026-09-10
source: mcp.so feed
relevance: ★★★
tags: [aviation, airports, airlines, aircraft, entity-resolution, reference-data, provenance, easa, remote-mcp]
---

# Airside Labs Aviation Tools MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 or API key)** - a hosted reference service that gives an AI agent defensible answers to aviation reference questions. Every answer arrives with its evidence attached - confidence, alternates, temporal validity and per-field provenance - and a question the data cannot answer comes back as unanswerable rather than as a plausible guess. Built for the failure mode most aviation data trips on: codes are reused, names collide, registrations move between operators, and most reference data online carries no date and no source.

```
Server type: Remote (hosted, Streamable HTTP, protocol 2025-06-18)
Auth: OAuth 2.1 (primary), X-API-Key or Bearer (alternative), no credential for 3 free-tier tools
Endpoint: https://mcp.airsidelabs.com/mcp
Registry: com.airsidelabs/aviation-tools (Official MCP Registry, v1.1.0)
Docs: https://airsidelabs.com/tools/docs
```

## Tools - 22 in Three Groups

**Identity (six tools).** `resolve_airport`, `resolve_airline`, `resolve_aircraft_type`, `resolve_registration` and `parse_flight_identifier` turn IATA/ICAO codes, names, tail numbers, Mode-S hex and flight designators into canonical entities. `validate_identifiers` checks a set of them against each other on a given date. Pass `as_of` for any historical question: codes are reused over time and an undated answer is silently wrong for past data.

**Airport facts (five tools).** `airport_network_integration`, `airport_operator`, `airport_operations_status`, `airport_connectivity` and `airport_size_band` answer what is true of an airport, each field cited to the public document that states it.

**Use-case atlas (eight tools).** `use_case_landscape`, `search_use_cases`, `get_use_case`, `similar_use_cases`, `data_requirements`, `trace_data_lineage`, `trace_workflow` and `easa_ai_framework` cover 6,700+ aviation AI use cases by organisation type and role, the data each needs and how fresh, the lineage from a requirement to the message that evidences it, 33 operational workflows, and a screen against the EASA AI-level and hazard framework.

**Feedback (three tools).** `report_unmet_need`, `submit_suggestion`, `feedback_status` let an agent tell the vendor what it could not get and see what happened to it.

Three tools (`use_case_landscape`, `get_use_case`, `submit_suggestion`) work without any credential, subject to a per-address daily cap.

## Pricing

| Plan | Price | Calls / month | Keys |
|---|---|---|---|
| Explorer | $0 | 500 | 1 |
| Pro | $59 | 10,000 | 1 |
| Team | $249 | 50,000 | 5 |

Self-serve, monthly, USD. Over the cap, a call answers in-protocol with the reset time rather than failing silently.

## Example Prompts

- "Which airline operated flight BA2668 on 14 March 2024, and what type flew it?"
- "Resolve G-XLEA and tell me who operates it as of today."
- "Is LGW integrated with the EUROCONTROL network, and who is the operator?"
- "What AI use cases exist for an MRO planning role, and what data do they need?"
- "Screen 'automated NOTAM triage' against the EASA AI framework."

## Why It Matters for Operators

An agent working on an aviation problem - reconciling an MRO work order to the right airframe, checking a customer's booking against the operating carrier, scoping an AI project for an airport operations team - can produce a confident answer easily and a defensible one with difficulty. These tools are built around that failure mode: every field says where it came from and when it was valid, alternates are listed rather than silently dropped, and a question the evidence cannot settle returns "unresolved" instead of a plausible number.

## Verification (Sep 10, 2026 night sweep)

Endpoint `https://mcp.airsidelabs.com/mcp` live-probed over JSON-RPC: keyless initialize answered with server info (Airside Labs Aviation Tools v1.1.0, matching the listing), and keyless `tools/list` captured all 22 tools exactly as documented. Fully live-verified.

## See Also

- [DFX Real Estate Intelligence MCP - US Property, Parcel and Debt Data](/docs/hermes/mcp/servers/external/dfx-real-estate-mcp)
- [WaitingForPower MCP - US Energy Permitting Tracker for Agents](/docs/hermes/mcp/servers/external/waitingforpower-mcp)
