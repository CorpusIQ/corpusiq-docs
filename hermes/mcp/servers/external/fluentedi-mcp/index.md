---
title: "FluentEDI MCP: Hosted X12 EDI Processing for Supply-Chain Agents"
description: "Keyless hosted MCP server with 17 live-probed tools for X12 EDI document workflows: parse, validate, build and acknowledge 850/856/810/855/997 transactions, plus JSON repair, contract-drift detection, cron and time utilities for retail and supply-chain automation. Free, no signup, stateless."
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-08-23
source: "mcp.so GitHub issue #3701"
relevance: ★★★
tags: [edi, x12, supply-chain, e-commerce, retail, json, remote-mcp, hosted]
---

# FluentEDI MCP

**One keyless URL gives an MCP client a full X12 EDI document toolbelt: parse, validate, build and acknowledge the retail transaction set (850, 856, 810, 855, 997), plus the JSON, HTTP, time and checksum utilities an EDI workflow needs around the edges.** FluentEDI is a hosted streamable-HTTP MCP server at `https://fluentedi.com/mcp`, free with no API key, no signup and no stored state. Every tool is read-only and idempotent; request bodies are processed and discarded.

```
Server type: Remote (Streamable HTTP, hosted)
Auth: None (keyless, stateless)
Endpoint: https://fluentedi.com/mcp
Tools: 17 exposed (live-probed; server v1.0.0, protocol 2025-03-26)
Batch: POST /v1/batch - up to 20 tool calls per round trip
HTTP fallback: GET/POST https://fluentedi.com/v1/{tool} for every tool
Built by: FluentEDI (fluentedi.com)
```

## Why This Matters for Operators

EDI is the plumbing of retail and CPG: purchase orders, advance ship notices, invoices and functional acknowledgments move between trading partners as X12 files, and partners reject documents on structural errors before a human ever reads them. **FluentEDI puts those checks in the hands of an agent: `edi_validate` runs the same structural checks a trading partner runs (control-number matching, ISA/GS/ST envelope integrity) before a file goes out, and `edi_parse` turns any raw interchange into clean JSON.** Operators automating supplier onboarding, invoice flows or drop-ship integration can parse and build X12 without licensing a commercial translator or maintaining parser scripts.

The server also covers the glue an EDI workflow actually needs: `api.diff` contract-drift detection for API payloads, RFC 8785 canonical JSON hashing for action receipts, JSON repair for sloppy payloads, and time-window and cron helpers for deadline math.

## Tools & Capabilities

17 tools confirmed by live probe (the submission issue claims 36; the probe is the ground truth - the exposed surface is 17 tools, with `tool_call` as a dispatcher that reaches the full catalogue so MCP clients with tool caps do not drop coverage).

| Tool | Purpose |
|---|---|
| edi_parse | Read a raw ASC X12 interchange and return it as JSON: delimiters from the ISA header, ISA/GS/ST envelope decoded |
| edi_validate | Structural checks a trading partner runs before rejecting a file: control numbers matching between ISA/IEA, envelope integrity |
| edi_build | Compile structured JSON into standards-valid X12 for the 850/856/810/855/997 transaction set, including 856 HL hierarchy checks |
| http_check | Resolve a URL and report what actually happens: final status, full redirect chain, content type, page title |
| http_assert | Assert a URL matches expected status/redirect/header/content rules - the difference between believing and knowing |
| json_query | JSONPath queries with concrete paths for every match |
| json_repair | Fix JSON that almost parses: markdown fences, trailing commas, prose-wrapped objects |
| time_now / time_convert / time_diff | Authoritative current time, cross-timezone conversion with DST handling, elapsed-time math |
| time_window | Deadline questions: is this instant inside the window, how long until it opens or closes |
| cron_next | Parse and validate 5/6-field cron expressions or macros like @daily, describe next run |
| hash | Cryptographic digests and HMAC signatures, hex and base64 at once for webhook signature comparison |
| math_eval | Arithmetic with operator precedence, factorials, variables and 30+ functions |
| tool_search / tool_describe | Search the catalogue by name, summary and keywords; return any tool's complete JSON Schema |
| tool_call | Dispatches to any tool in the catalogue - keeps full coverage alive in clients that cap tool counts |

## Installation

```json
{
  "mcpServers": {
    "fluentedi": {
      "type": "http",
      "url": "https://fluentedi.com/mcp"
    }
  }
}
```

For the Claude Code CLI: `claude mcp add --transport http fluentedi https://fluentedi.com/mcp`

## Configuration

None. There is no API key, no account and no signup. Requests are stateless and discarded after processing, which the vendor states makes the service safe for handling trading-partner payloads. For bulk work, `POST https://fluentedi.com/v1/batch` accepts up to 20 tool calls in one round trip.

## Example Prompts

- "Parse this 856 advance ship notice and show me the line items."
- "Validate this 850 purchase order before we acknowledge it - do the control numbers match?"
- "Build an 810 invoice from this order data and check the GS1 digits."
- "Does our API response still match the schema we shipped last quarter? Show drift findings with JSON Pointer paths."

## Business Relevance

Retail and CPG operations live on EDI, and the failure mode is silent: a rejected 856 or mismatched 997 discovered days later means chargebacks and dock delays. FluentEDI converts that from tribal knowledge into deterministic tool calls: an agent can validate outbound documents, parse inbound ones into JSON for downstream systems, and diff API contracts over time. Deepest coverage is retail EDI (850/856/810/855/997 with GS1 check digits), with the JSON, hash and cron utilities doubling as general-purpose operations glue for webhook verification, deadline windows and payload repair.

## Integration with CorpusIQ

CorpusIQ reads the business systems of record (orders, invoices, inventory across 40+ connectors). FluentEDI supplies the document layer those systems speak: an agent can parse an inbound X12 invoice (FluentEDI), validate its structure, then reconcile the line items against order data in CorpusIQ. EDI is the transport, CorpusIQ is the ledger.

## Limitations

- Read-only and idempotent by design: parse, validate and build tools only, no EDI submission or trading-partner connectivity.
- The repository (mastermanas805/fluentedi-mcp) was created Aug 23, 2026 with 0 stars and no declared license in the README - brand-new surface, verify licensing before enterprise embedding.
- X12 only; no EDIFACT support documented.
- The submission claims 36 tools but the live server exposes 17; the rest are reachable through the tool_call dispatcher, which some strict clients may not surface natively.
- No state: batch workflow orchestration must live on the client side.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [Atoa MCP](/docs/hermes/mcp/servers/external/atoa-mcp) - UK instant payments for agents with 14 payment tools
- [Storepilot MCP](/docs/hermes/mcp/servers/external/storepilot-mcp) - e-commerce store operations from an agent
- [MCP Integration Guide](/docs/hermes/mcp) - connecting MCP servers to Hermes Agent
