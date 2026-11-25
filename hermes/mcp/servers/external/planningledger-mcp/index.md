---
title: "PlanningLedger MCP - UK Planning Records for Agents"
description: "Fourteen read-only tools over UK planning applications, appeals and Local Plan policies, measured to the sign-in gate that holds every call."
category: "Data & Analytics"
stars: "★★★"
added: 2026-11-25
source: "Submission chatmcp/mcpso #8046 filed 2026-11-25T08:00:51Z; registry record com.planningledger/planningledger 1.0.2 with the remote https://mcp.planningledger.com/mcp; a keyless initialize and a 14-tool tools/list read 2026-11-25; the tools/call 401, the protected-resource document and the RFC 8414 document read the same day; the vendor page mcp.planningledger.com for the daily allowance"
relevance: "★★★"
tags: [real-estate, property, planning, uk, local-government, appeals, compliance, oauth, remote-mcp]
last_updated: "2026-11-25"
---

# PlanningLedger MCP

**A property decision in the UK turns on a record nobody keeps in one place: what was applied for, what officers said about it, how the council decided, whether an appeal was allowed, and what the Local Plan requires of the site.** PlanningLedger indexes that record and serves it over MCP: applications and their documents, appeal decisions from all four UK bodies, Local Plan policies, and counts of decisions by council and year, with every result linking to the council's own copy.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.planningledger.com/mcp
Auth:        OAuth 2.1, read scope only; every tool requires the sign-in
Registry:    com.planningledger/planningledger 1.0.2
Pricing:     free, 20 document searches and 100 quotes a day per person
Tools:       14, read from a keyless tools/list
Transport:   Streamable HTTP at the /mcp path; the same document serves the suffixed discovery route
```

## The gate, measured

This server publishes its tool surface before it asks for anything. A keyless `initialize` answers **200** on protocol `2025-06-18` with serverInfo `planningledger 1.0.0`, and the same session returns **all fourteen tools**. The call itself is where it stops:

```
POST https://mcp.planningledger.com/mcp
{"jsonrpc":"2.0","id":9,"method":"tools/call","params":{"name":"list_appeals","arguments":{}}}

HTTP/2 401
www-authenticate: Bearer
  resource_metadata="https://mcp.planningledger.com/.well-known/oauth-protected-resource/mcp"
content-type: application/json

{"error":"unauthorized","error_description":"a bearer token from our sign-in is required"}
```

That is the **discovery-open, execution-gated** tier, and it is a good one: an operator can read what the server does and decide whether to connect before creating an account, and a client that only renders `content` blocks still shows the refusal because the body is plain JSON with a readable description rather than an empty JSON-RPC envelope.

## The OAuth chain, end to end

`/.well-known/oauth-protected-resource` answers **200**, and the same document is served at the suffixed route the challenge names:

| Field | Value |
| --- | --- |
| `resource` | `https://mcp.planningledger.com/mcp` |
| `authorization_servers` | `["https://mcp.planningledger.com"]` |
| `scopes_supported` | `read` |
| `bearer_methods_supported` | `header` |
| `resource_name` | `PlanningLedger` |
| `resource_documentation` | `https://mcp.planningledger.com/` |
| `resource_policy_uri` | `https://mcp.planningledger.com/privacy` |
| `resource_tos_uri` | `https://mcp.planningledger.com/terms` |

The authorization server is the resource host itself, and its RFC 8414 document is complete:

| Field | Value |
| --- | --- |
| `issuer` | `https://mcp.planningledger.com` |
| `authorization_endpoint` | `/oauth/authorize` |
| `token_endpoint` | `/oauth/token` |
| `registration_endpoint` | `/oauth/register` (dynamic registration) |
| `revocation_endpoint` | `/oauth/revoke` |
| `scopes_supported` | `["read"]` |
| `response_types_supported` | `["code"]`, response modes `query` only |
| `grant_types_supported` | `authorization_code`, `refresh_token` |
| `code_challenge_methods_supported` | `S256` |
| `client_id_metadata_document_supported` | `true` |
| `authorization_response_iss_parameter_supported` | `true` |

**One scope, named `read`, against fourteen tools that only read.** There is no write scope to audit for and nothing a token can do beyond reading, which is the simplest permission story in this catalog. The sign-in is an email six-digit code valid for 15 minutes, five codes an hour, and the allowance is counted against that address.

## The tool surface, all fourteen

| Tool | Inputs | What it returns |
| --- | --- | --- |
| `search_applications_nearby` | postcode, point or UPRN, radius | applications near a place, nearest first, up to 5 km |
| `get_application` | `{lpa_slug}:{app_ref}` or lpa plus reference | one application: site, proposal, dates, decision, appeal, conservation area |
| `get_application_record` | `lpa`, `reference` | the 13-key canonical projection plus every field the LPA published |
| `list_application_documents` | `lpa`, `reference` | the documents the council published, each with a link and whether it is searchable |
| `quote_application_documents` | `lpa`, `reference` | passages of at most 40 words from officer reports and decision notices |
| `search_applications` | `query` | hybrid dense plus BM25 search across application documents, with the matching passage |
| `aggregate_applications` | optional filters | counts by council, year, outcome and type, each with its base |
| `search_appeal_precedents` | `query` | semantic search over appeal decision letters across all four UK bodies |
| `get_application_appeals` | stable id or lpa plus reference | the appeals made on one application |
| `list_appeals` | council, decision, type, date | appeal decisions, newest first |
| `get_appeal` | `pins_case_number` or national reference | one appeal: council, type, decision, dates, the application it was about |
| `search_policies` | `query` | adopted Local Plan policies with the plan they come from |
| `get_policy` | `lpa`, `policy_code` | one policy in full, with plan and in-force date |
| `get_search_coverage` | optional council | which council-years are open for document search |

The coverage tool is the honest one and the reason this guide leads with caution rather than with a feature list. The vendor states plainly that document search **opens council by council and year by year** as indexing proceeds, and that "not yet searchable here" means the council-year has not been indexed yet, not that nothing exists. Any workflow built on the document tools must read the `search_coverage` line and pass it on, which the server's own `instructions` requires of the assistant.

## What the vendor states about the data

Three constraints are recorded here because they change how an answer should be phrased, and all three come from the vendor's own page and instruction string:

- **Quotes are capped at 40 words** and never come from neighbours' letters or application forms, only from officer reports, decision notices and applicants' statements.
- **People's names and contact details are withheld** from the record tools.
- **Every result links to the council's or the appeals body's own copy**, and the assistant is told to cite it. Text inside results is applicant and officer prose, so the server instructs clients to treat it as data and never as instructions.

The four appeal bodies are the Planning Inspectorate for England, PEDW for Wales, DPEA for Scotland and PAC for Northern Ireland, which makes this one index covering four jurisdictions with different case references.

### What does the free allowance actually allow?

Free, per person, counted in UK time and reset at midnight: **20 document searches and 100 quotes a day**, plus **300 calls a day at 20 calls a minute** across all fourteen tools. Finding applications, counting decisions, listing documents, appeals and policies by code are not counted separately. A search means a search across documents, appeal decisions or Local Plan policies.

### Can an agent use it without an account?

Read the tool list, yes. Call a tool, no. Every `tools/call` answers 401 until a bearer token from the sign-in arrives, so any workflow needs one interactive sign-in per person, and the allowance follows that address rather than the client.

### Is it listed in any assistant directory already?

The vendor states that PlanningLedger is listed in Claude's connector directory and gives the in-app path for adding it, and it publishes the plain MCP address for Claude Code, ChatGPT and other clients. The address in both cases is the same `https://mcp.planningledger.com/mcp`.

## What an operator does with it

A developer checking a site before an offer, a planning consultant pricing an appeal, and a lender testing a pipeline all ask the same three things: what was decided nearby, how often this council refuses, and what the Local Plan requires. Those are `search_applications_nearby`, `aggregate_applications` and `get_policy`, and all three carry their base counts, which is what makes the answer defensible rather than illustrative. An accountant or surveyor will find the appeal precedents the most reusable part: the same scheme argued in a comparable borough is the evidence a client wants before paying for a submission.

## See Also

- [BADideas.fund MCP - CEE Pre-Seed Fund and Portfolio](/hermes/mcp/servers/external/badideas-fund-mcp/) for the funding side of a property or proptech venture
- [Investor Shelf MCP - Funders, Deals and Cited Reports](/hermes/mcp/servers/external/investorshelf-mcp/) for funders of the businesses that build on this data
