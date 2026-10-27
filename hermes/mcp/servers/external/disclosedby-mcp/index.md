---
title: "disclosedby MCP - Dated Subprocessor Lists for Agents"
description: "Every version of hundreds of vendors' GDPR subprocessor lists, quoted and dated, over a keyless MCP server with seven tools for lists, changes and paths."
category: "Compliance"
stars: n/a (hosted record, no public repo)
added: 2026-10-22
source: "chatmcp/mcpso issue #5949 (disclosedby, October 22, 2026 midday sweep)"
relevance: ★★
tags: [gdpr, subprocessors, vendor-risk, dpia, compliance-evidence, data-processing, remote-mcp, keyless]
last_updated: "2026-10-24"
---

# disclosedby MCP

**A vendor's subprocessor list is the only supply-chain statement a software company signs its name to, and almost nobody keeps old versions of it. disclosedby keeps every version, dated, quoted word for word, and serves the whole record over a keyless MCP server.**

```
Server type: Remote (Streamable HTTP), no key
Endpoint: https://disclosedby.com/api/mcp
Auth: none for the record tools
Live check: keyless POST initialize returned HTTP 200 (serverInfo disclosedby version 2, protocol 2025-03-26, tools capability, with server instructions)
Tools: 7 from tools/list
Record size: 352 companies with a list read, 9,806 entries quoted, 563 subprocessors with their own page, 4,901 changes on record, checked up to 2026-10-22
Pricing: free to read, cite and link with no account; the watch is $99 a month for up to 200 lists
Built by: disclosedby (disclosedby.com)
```

## Why This Matters for Operators

Every company that buys software is a data controller with an Article 28 obligation, and the subprocessor list is where that obligation becomes checkable. The problem is temporal: a vendor can add a subprocessor after you sign, and your record of what the list said when you approved the vendor is usually a PDF nobody can find.

disclosedby answers the two questions that actually come up. What did this vendor's list say on the date we signed? And who, eventually, touches our data through this vendor's own suppliers? The first is `as_of`, which returns the reading held nearest before the date you give it, with that reading's own capture. The second is `in_chain`, which takes the companies you buy from and returns every path to a subprocessor, named directly or named by a company that is itself a subprocessor.

This is a first for the compliance class in this catalog. What is already listed checks licenses, leases and incidents by location, or audits a tool-call trail. This one is the vendor supply chain, with a date on every row.

## Tools & Capabilities

| Tool | What it answers |
|---|---|
| `list` | What one company's published list says as the record holds it: every row quoted as the company wrote it |
| `as_of` | What one company's list said on a given date, from the reading nearest before it |
| `changes` | The dated changes to one company's list, each derived from two readings and carrying both |
| `changes_across` | The same, for several companies at once |
| `named_by` | Which companies name one subprocessor, with the name each company prints for it and when it was first seen |
| `resolve` | What company a name on a list refers to, through a hand-checked identity table, exact match only |
| `in_chain` | Every path from the companies a reader buys from to one subprocessor |

`resolve` is deliberately literal: exact match only, never a guess. That is the right call for evidence work, and it means the agent should confirm an identity before running a chain analysis on it.

## Installation

```json
{
  "mcpServers": {
    "disclosedby": {
      "type": "http",
      "url": "https://disclosedby.com/api/mcp"
    }
  }
}
```

## Live Check

Called `list` with `notion.so`, and it returned the company page plus the readings held: 14 rows in the 2022 capture, 17 in the 2023 and 2024 captures, each reading carrying a capture timestamp, a row count, a status and an evidence hash. The suppliers named only in the later readings include Anthropic and OpenAI. That is the whole point of the record in one response: the list moved, the record shows when, and each version is quoted rather than summarized.

Site-wide the numbers are larger than one vendor: 352 companies read, 9,806 entries quoted, 4,901 changes on record.

## Limits Worth Knowing

- The identity table behind `resolve` is hand-checked and exact-match only. Two companies printing the same supplier under different names stay separate rows until a person joins them, so a chain analysis can under-report.
- Coverage is whoever publishes a list and gets read. 352 companies is a strong start for a software vendor review and far from the whole market; a missing company means no published list was found, not that the vendor has no subprocessors.
- Readings are dated by when disclosedby read the page, not by when the vendor changed it. The vendor's own "last updated" line is carried inside the quote, and several are vague (Notion's reads "Last Monday" in the captured text).
- Free is the record. The watch, with alerts and a key for agents, is $99 a month up to 200 lists, VAT where it applies, so a programmatic monitoring workflow needs the paid tier.
- TDM reservation is declared on the site's terms, so reuse of the pages beyond reading and citing is a licensing question rather than an open one.

## FAQ

### Can this replace a DPIA or a vendor review?
No. It supplies the evidence layer: what the list said, when it changed, and who is upstream. The judgment about whether a new subprocessor is acceptable is still a person's, and the record is explicit that a row is a quote, not an assessment.

### What is the difference between the free record and the watch?
The lists, versions, changes, feed and MCP server are free with no account and no key. The $99 monthly watch adds monitoring: paste up to 200 vendors, get the before and after when a list moves, and use a key for agent access to date-stamped answers.

### How does an agent use `in_chain` safely?
Resolve the names first, then run the chain. `resolve` is exact-match against a hand-checked table, so a chain built on an unresolved name is a chain built on nothing, and the tool returns paths rather than a yes-or-no answer that would invite being quoted as one.

## See Also

- [Copliancy MCP Suite - Licenses, Leases and Incidents per Location](/hermes/mcp/servers/external/copliancy-mcp/)
- [GLP Audit Proxy MCP - Tamper-Evident Tool-Call Trail](/hermes/mcp/servers/external/mcp-glp-audit-proxy/)
