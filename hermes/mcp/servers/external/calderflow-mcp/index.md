---
title: "CalderFlow MCP - Diagrams From a Sentence"
description: "Ten chart tools that turn a described process into a flowchart, funnel, timeline or ER diagram, with the chart rendered inline as an MCP App."
category: "Diagrams / Process"
stars: "n/a (remote Streamable HTTP, API key for calls; ten tools, schema read)"
added: 2026-11-17
source: "the mcp.so feed card stamped 2026-11-17T04:43:17Z and a live session on 2026-11-17 in which initialize, tools/list and resources/list answered over Streamable HTTP, and tools/call returned its authentication message"
relevance: ★★
tags: [diagrams, flowchart, funnel, timeline, erd, mcp-apps, remote, mcp]
last_updated: "2026-11-17"
---

# CalderFlow MCP

**A process that lives in a paragraph cannot be reviewed.** The moment a workflow has to be argued about, it needs a shape: a flowchart for a sequence with branches, a funnel for stages that lose people, a lifecycle for phases and milestones, a timeline for events, an entity diagram for tables and their keys. CalderFlow turns a description into one of those five shapes and returns a share link, which is the difference between a diagram you describe and a diagram a colleague can open.

The server is worth a page for two reasons that are separate from the product. It is the **latest clear example of an MCP App**: its `resources/list` serves a `ui://calderflow/chart-<id>` resource typed `text/html`, so the chart renders inside the conversation instead of arriving as a link a reader has to trust. And its evidence tiers are split cleanly, with the handshake and the full schema open to anyone and only `tools/call` behind a key.

```
Server type:   remote Streamable HTTP
Endpoint:      https://www.calderflow.com/mcp
Server:        calderflow, version 0.1.0, title "CalderFlow"
Protocol:      2025-06-18
Auth:          API key for tool calls; initialize, tools/list and resources/list are open
Tools:         10
Resources:     ui://calderflow/chart-<id>, text/html (inline chart viewer)
Prompts:       none (prompts/list returns -32601)
Listed on:     mcp.so feed, stamped 2026-11-17T04:43:17Z
```

## The evidence tier

**Handshake open, calls gated.** `initialize` answered **200** as *calderflow* **0.1.0** on protocol **2025-06-18**, declaring `tools` and `resources` capabilities, a website URL and two icon assets. `tools/list` returned **ten** closed schemas with their required arguments. `resources/list` returned the chart viewer resource, which is the MCP Apps pattern rather than a text-only answer. `prompts/list` returned JSON-RPC **-32601**, *Method not found*, so there is no prompt surface to enumerate.

Then `tools/call` to `create_flowchart` answered HTTP **200** with `isError: true` and one sentence: *Authentication required: send 'x-api-key: <key>', append ?key=<key> to the URL, or send 'Authorization: Bearer <token>'.* Three named paths in, no tool result observed. This page therefore describes the schema as measured and the behaviour as documented, and says which is which.

## Tools & Capabilities

| Tool | Required arguments | What it produces |
|---|---|---|
| `create_flowchart` | `title`, `mermaid` | A flowchart from Mermaid source |
| `create_chevron_chart` | `title`, `steps` | A chevron process strip |
| `create_funnel_chart` | `title`, `stages` | A funnel with stage values |
| `create_lifecycle_chart` | `title`, `phases`, `milestones` | Phases with milestones on each |
| `create_timeline_chart` | `title`, `events` | An event timeline |
| `create_erd_chart` | `title`, `entities` | An entity diagram with entities and their fields |
| `edit_chart` | `chart_id` | Edits an existing chart |
| `get_chart` | `chart_id` | Reads one chart back |
| `list_charts` | none | The charts in the account |
| `delete_chart` | `chart_id` | Removes a chart |

## Installation

```sh
claude mcp add calderflow --transport http https://www.calderflow.com/mcp
```

An API key can travel in an `x-api-key` header, as a `?key=` query parameter, or as a bearer token. The MCP App resource is what makes the chart appear inline in a client that supports MCP Apps; clients without that support can still be given the returned share link.

## Why This Matters for Operators

The cost of a process diagram is not the drawing, it is the retyping: someone explains the order-to-cash flow in a chat, someone else redraws it in a slide tool, and the two versions diverge. Describing the process once and getting an editable chart back removes that second pass, and an `<iframe>`-renderable HTML resource means the artefact can be reviewed in the same thread where the process was described.

## Questions operators ask

### Why does an open schema matter if the calls are gated?

Because it settles what the tool can and cannot do without a sales conversation. The ten schemas name five chart families, one edit path, one read path and a delete; there is no data import and no third-party source. A team can decide whether that shape fits before it asks for a key.

### Is the chart data mine or the vendor's?

The chart lives on the vendor's side: every tool returns a `chart_id` and the viewer is a hosted resource. `delete_chart` exists, so removal is in the surface rather than in a support ticket.

### Does it work in any MCP client?

The transport and protocol version are the standard ones, so any Streamable HTTP client can call it. The inline chart, however, needs a client that renders MCP App resources; elsewhere the output is the share link.

## Related

- [MCP Apps - Interactive UI in the Client](/hermes/mcp/mcp-apps-interactive-ui) - how the `ui://` resource pattern works
- [MCP Specification 2026-07-28](/hermes/mcp/mcp-spec-2026-07-28) - the protocol revision this server's 2025-06-18 handshake sits behind
- [Ryze Google Ads MCP](/hermes/mcp/servers/external/ryze-google-ads-mcp) - an example of a hosted reporting surface that renders tables rather than diagrams
