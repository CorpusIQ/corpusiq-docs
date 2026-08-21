---
title: "den MCP - Korean AEC Standards with Clause References"
description: "Remote MCP server for Korean construction and building standards: KDS, KCS, KS and building statutes. Every answer carries the source clause number (for example KDS 14 20 22 section 4.3.1) and the server abstains rather than guessing when it has no grounds. Ten tools including k_snippets, answer_why, compare, scenario, site_context and review_plan; Bearer token, free beta, no query logging."
category: Compliance
stars: n/a (new listing)
added: 2026-08-21
source: "mcp.so GitHub issue #3671"
relevance: ★
tags: [korean-standards, construction, kds, kcs, compliance, building-codes, aec, remote-mcp, regulation]
---

# den MCP

**Korean architecture, engineering and construction standards, answered with the clause number attached.** den is a hosted MCP server for KDS (design standards), KCS (construction specifications), KS standards and Korean building statutes. When it answers, the response carries the source reference (for example `KDS 14 20 22 §4.3.1`). When it has no grounds, it says so explicitly instead of fabricating a citation.

```
Server type: Hosted remote (Streamable HTTP)
Endpoint: https://mcp.den.archi/mcp
Auth: Bearer token (free beta access at den.archi)
Tools: 10 (k_snippets, answer_why, evidence_for, compare, path_between, scenario, enumerate, traverse, site_context, review_plan)
Registry: archi.den/den_archi_mcp v1.1.0 (official MCP registry)
Built by: den (den.archi)
```

## Why This Matters for Operators

Construction in Korea means KDS and KCS compliance, and the standards are dense, versioned and cross-referenced. A project manager, estimator or legal reviewer who needs "which clause governs concrete curing in this climate region, and what does the clause text actually say" currently works through printed volumes and portal searches. den answers in conversation, with the citation, and marks its own limits: responses carry `relevance` and `lacks_answer` flags so a client can tell "we don't hold this yet" apart from "here is the number".

Two behaviors make it trustworthy for review work. Scope labelling marks every snippet as Korean national norm, foreign reference or den's own analysis, so foreign material is never presented as a domestic requirement. And the server stores no query text on disk, which matters when pasting contract clauses or unpublished project details into a prompt.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `k_snippets` | Find numeric values and clause text in standards and statutes |
| `answer_why` | Explain why a regulation exists, via the causal path |
| `evidence_for` | Find the supporting clauses for a claim |
| `compare` | Compare two standards or construction methods side by side |
| `path_between` | Show how two concepts connect across the standards |
| `scenario` | Given a situation, gather the standards that apply |
| `enumerate` / `traverse` | List and walk adjacent concepts |
| `site_context` | Convert a place name or coordinates into climate and jurisdiction conditions |
| `review_plan` | Review a plan against the applicable standards |

Queries accept an `as_of` parameter to answer against the standards as they stood at a past date, for reviewing old tender documents or disputes. Truncated clause text is marked, so a client knows provisos or exceptions remain unread.

## Installation

Request free beta access at den.archi; on approval you receive a Bearer key:

```json
{
  "mcpServers": {
    "den": {
      "url": "https://mcp.den.archi/mcp",
      "headers": { "Authorization": "Bearer <your-key>" }
    }
  }
}
```

Anonymous probes return HTTP 401, which is the expected gate. The GitHub repository (odd-Innocent/den_archi_mcp) publishes the README, server.json and example transcripts; the server implementation itself is not public.

## Configuration

No local configuration beyond the header. The vendor reports a golden-evaluation score of 35/38 with 3 known failures on contract-document questions, and states clause coverage is partial: a missing clause reads as "not held yet", not "out of scope". Treat abstention-heavy responses as a coverage signal and escalate to the primary source when a query returns empty.

## Business Relevance

- **Korean AEC firms** check KDS/KCS/KS requirements in conversation instead of portal searches
- **Foreign contractors bidding Korean work** verify compliance clauses with scope labels that separate domestic norms from references
- **Estimators and reviewers** use `review_plan` to check a design against standards before submission
- **Dispute and claims work** uses `as_of` to reconstruct the standards in force at a past date

## Integration with CorpusIQ

den is a regional compliance layer that pairs with CorpusIQ's horizontal business connectors. A Korean construction operator can hold the project's financials (QuickBooks, ERP) and documents in CorpusIQ while den answers the regulatory questions, with clause citations that go into reports, submittals and claims. CorpusIQ's connector surface covers the business; den covers the jurisdiction.

## Limitations

- Korean standards only: KDS, KCS, KS and building statutes; no value elsewhere
- Partial clause coverage, stated by the vendor; abstention means some queries return empty
- Requires an API key; no anonymous introspection
- Beta and free today, with no published pricing for general availability
- Server implementation is not open source; the repo publishes docs and transcripts only

## See Also

- [FCA Handbook MCP - UK Financial Regulation for AI Agents](/hermes/mcp/servers/external/fca-handbook-mcp/)
- [Cliometry MCP - Korean Market Data for Agents](/hermes/mcp/servers/external/cliometry-mcp/)
- [Opportunity Atlas MCP - Northeast Ohio Construction Opportunity Intelligence](/hermes/mcp/servers/external/opportunity-atlas-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
