---
title: "Azquo MCP - Audited Shared Memory for AI Agents"
description: "Official Azquo MCP: a persistent, auditable store where every write is attributed and every figure traces back to its source file, user and change."
category: Data and Analytics
stars: 0
added: 2026-10-20
source: "mcpservers.org /all page 1 via the r.jina.ai reader proxy (azquo-mcp)"
relevance: ★★★
tags: [business-intelligence, finance, agent-memory, multi-agent, audit-trail, data-lineage, hierarchical-data, remote-mcp, oauth]
last_updated: "2026-10-24"
---

# Azquo MCP

**A store built for what agents learn, not just what they are asked** - every write is attributed to the agent and the person behind it, hierarchies are added without a migration, and every single figure traces back through each transformation to the file it came from.

```
Server type: Remote (Streamable HTTP) at https://data.azquo.ai/mcp
Auth: OAuth 2.1 (bearer header, scope "mcp") for the Claude app custom connector; API key from the Azquo admin site for agent runtimes
Live check: POST initialize returned HTTP 401 "Unauthorized : no key" with WWW-Authenticate pointing at https://data.azquo.ai/.well-known/oauth-protected-resource
Access: evaluation granted on request, with your own Azquo account
Vendor: Azquo (azquo.com), a finance-owned consolidation and business-intelligence platform
```

The published resource metadata, read live at probe time:

```json
{"resource":"https://data.azquo.ai/mcp",
 "authorization_servers":["https://data.azquo.ai"],
 "bearer_methods_supported":["header"],
 "scopes_supported":["mcp"],
 "resource_name":"Azquo"}
```

## Why This Matters for Operators

Every agent session starts by re-deriving what the last one worked out. A convention gets discovered ("Q3 revenue excludes intercompany"), the session ends, and the next agent has no way to inherit it. The result is the same recurring cost: a fresh model reading the same CSV and getting the same question slightly differently wrong.

Azquo's argument is that the missing piece is not a smarter model, it is a place to put what the model learned that survives the session and can be audited later. The architecture behind that claim is unusual and it is the reason this entry earns its place: Azquo stores names in hierarchies rather than rows in tables. There is no schema to design before data arrives. A new dimension is a new lens over existing data, not a migration, so the business question that used to wait in the data team's queue gets answered in the same conversation.

The second half is provenance. Most stores can tell you which row was written when. Azquo attributes every individual figure, so the answer to "where did this number come from" is a cell, a source file, a person and a time - and the conventions agreed while the database was built are stored in the database, for the agent that connects next.

## Tools & Capabilities

Capabilities stated by the vendor for the hosted server. Azquo documents these as outcomes rather than a public `tools/list`, so tool names are not quoted here - they appear once you connect with an authenticated account:

| Capability | What an agent does with it |
|---|---|
| Build and extend | Create databases, import raw files as they arrive, design and refine import templates |
| Query | Ask questions in AQL, the Azquo query language, against the loaded model |
| Structure | Browse and extend hierarchies (for example Division to Region to Office) without disturbing what is already loaded |
| Report | Build and run reports over the live model |
| Audit a figure | Walk any single value back through every transformation to its source file, the user and the date |
| Rehearse | Try a risky change on a copy of the database first, then commit |
| Recover | See the history of any name, every earlier value with who changed it and where the change came from, and restore a name that was deleted |
| Inherit | Leave the conventions and decisions in the store, where the next agent is told to read a starting note that points into a skills base of several hundred notes |

Beside your own databases, the server exposes a shared example library the agent can copy rather than build from nothing: budgeting, management accounts, time and expenses, pivot analysis, property insurance premiums and a US auto quote.

## Installation

For the Claude app there is nothing to install: add `https://data.azquo.ai/mcp` as a custom connector and sign in with an Azquo login.

For an agent runtime, point it at the same address with an API key issued from the Azquo admin site. The unauthenticated probe recorded above confirms the endpoint is live and answering; it will not serve a tool call without a credential.

```bash
curl -s -X POST https://data.azquo.ai/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"probe","version":"1.0"}}}'
```

Adding a system is described as a data-download task, not a migration project: the people who already have access download what they already have access to, and Azquo loads those files. Your databases, permissions and routines stay where they are.

## Configuration

There is no client-side configuration beyond the credential. The two decisions that matter are made inside Azquo:

- **Who the agent is.** Each write is attributed to the agent and the person behind it, which is what makes the audit trail usable for a team rather than a single operator.
- **What it can reach.** Data arrives as downloads you make, so the connector inherits the scope of what your people can already export, not a new grant to a third party.

## Business Relevance

**Month-end and board packs.** A folder of monthly exports with different shapes and column names, some PDFs of board minutes, a spreadsheet of regions and divisions. The worked demonstration the vendor publishes is exactly this: an agent loads each file as it finds it, proposes Division to Region to Office, commits the hierarchy, anchors the PDF commentary to the months it describes, and every cell keeps its source.

**The question that arrives two weeks later.** "Split Q3 by product line, not just region." Product line did not exist when the first agent ran. It gets added, anchored into the existing hierarchy, and answered, with week one's audit trail still resolving cleanly. Compare that with the schema-first path, where the answer waits for a migration.

**Several agents, one record.** Work divided between agents usually loses track of who did what. Attributing every write to both the agent and the human behind it is the control that makes multi-agent work reviewable rather than mysterious.

**Spreadsheets stay in the loop.** The store speaks Excel both ways: analysts pull live data in, write changes back, and both sides see one source of truth with every change on the record.

## Integration with CorpusIQ

This is the clearest third-party expression of the problem CorpusIQ exists to solve, approached from the storage side rather than the retrieval side. CorpusIQ answers a business question across connected systems and cites the source of each number; Azquo keeps the numbers an agent has already reconciled, with the lineage attached, so the next answer starts from the reconciled set instead of re-deriving it.

Where they differ matters for buying decisions. CorpusIQ connects read-only to the systems you already run and moves nothing; Azquo becomes a new store that you load with exports and that agents then write to. Both end in a cited number. One is a retrieval layer over live sources, the other is an audited memory of what has been decided about those sources.

For teams running several agents against the same financial model, the attribution model - every write to an agent and a person - is the part worth copying into your own governance, whether or not you adopt Azquo.

## Limitations

- **It is a second copy of your data, by design.** The vendor is explicit: the two-way risk is accepted only as long as downloads are made, and the backup is a plain file precisely so you are not locked in. That still means a new store to keep current.
- **Commercial terms are not published.** Evaluation access is "on request" and no price appears on the listing or the endpoint. Treat cost as unverified until you have a quote.
- **The tool surface is not public.** No `tools/list` is reachable without a credential, so tool names, annotations and schemas could not be verified in this sweep. The capability list above is the vendor's own wording.
- **AQL is its own language.** An agent can write it, but a team reading the queries needs the several hundred notes in the skills base to work fluently.
- **The demonstration is the vendor's.** The ISO Commercial Auto worked example (a 168-page filing, 73 territories) is published by Azquo, not reproduced here, and this sweep did not run a tool call.

## FAQ

### How is this different from a vector database or a "memory" MCP server?

A vector store retrieves the right paragraph and cannot tell you whether the number inside it is canonical, an old draft or something pasted into a slide. Azquo stores figures with per-cell provenance and hierarchies that aggregate correctly. If your question is "what did we say about this" a memory server is enough; if it is "what is the number, and why is it that number" the lineage is the point.

### Do I have to migrate my databases?

No, and the vendor's position is the opposite of a migration: your systems stay as they are, and the people who use them download what they already have access to. Azquo loads those exports. Nothing is redirected and no connector is installed in your database.

### What happens when a new dimension shows up?

It is added as a new hierarchy over the existing data. Nothing already loaded breaks and reports built on the earlier structure keep resolving, which is the specific claim that separates this from a schema-first warehouse.

### Can two agents write at the same time?

Yes. Several agents and the people working with them can work in the same database, and each write is attributed to the agent and the person behind it, so dividing work does not lose the record of who did what.

### Is the audit trail enough for a regulated review?

It is a per-figure lineage and attribution trail, which is what an auditor asks for when they ask where a number came from. It is not a validated GxP audit trail with hash-chained records and role separation; if that is the requirement, the [GLP Audit Proxy](/hermes/mcp/servers/external/mcp-glp-audit-proxy/) is the entry for that job.

## See Also

- [Linksee Memory MCP - 6-Layer Cross-Agent Memory](/hermes/mcp/servers/external/linksee-memory)
- [GLP Audit Proxy MCP - Tamper-Evident Tool-Call Trail](/hermes/mcp/servers/external/mcp-glp-audit-proxy/)
- [drift MCP - Pre-Action Mandate Enforcement for AI Agents](/hermes/mcp/servers/external/drift-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
