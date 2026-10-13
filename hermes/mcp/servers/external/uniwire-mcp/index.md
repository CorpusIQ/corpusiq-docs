---
title: "uniwire MCP - Electrical Diagrams and Installation Checks"
description: "Electrical single-line and multi-line diagrams as code: validate, check against NF C 15-100 and IEC 60364 rules, render and export wire lists and BOMs."
category: Manufacturing & Industrial
stars: n/a (new listing)
added: 2026-10-13
source: "chatmcp/mcpso issue #5242 + official MCP registry (Oct 13, 2026 midday sweep)"
relevance: ★★
tags: [electrical, engineering, diagrams, nf-c15-100, iec-60364, construction, keyless, remote-mcp]
---

# uniwire MCP

**Remote MCP server (Streamable HTTP, no account or API key)** - electrical diagrams as code: an assistant describes an installation in plain words, writes it as a `*.uniwire.json` document, and gets back a validated, rule-checked drawing and a PDF.

```
Server type: Remote (Streamable HTTP); local option via pip install "uniwire[mcp]"
Auth: None required (the hosted server is public; result documents kept for 30 days so links stay short)
Endpoint: https://mcp.uniwire.sh/mcp
Tools: 14 (reference card, types, validate, check, describe, patch, render, links, wiring, BOM, examples, normalize)
Pricing: Free hosted server; Apache-2.0 open source, self-hostable
Built by: uniwire (uniwire.sh; repo github.com/uniwire-dev/uniwire)
Listing: chatmcp/mcpso issue #5242; official MCP registry io.github.uniwire-dev/uniwire (published October 13, 2026)
```

## Why This Matters for Operators

An electrical diagram is a document with rules attached. Protection ratings have to match cable cross-sections, 30 mA protection has to land on the right circuits, and every circuit has an ampacity story. In a CAD tool those rules live in the reviewer's head; the check happens after the drawing is done, and the rework happens after that.

uniwire moves the check next to the drawing. The installation lives in a text document an agent can write, review and diff; the server validates it, runs it against the installation rules and produces the single-line and multi-line diagrams, the wire list and the bill of materials. For teams that quote, install and inspect electrical work, that turns a drawing into something checkable before it leaves the office.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| get_reference_card | The document format summarised for the model: skeleton, node types, fields, enums and pitfalls |
| list_types / type_info | The reference library of component and device types |
| validate | Validate a document against the published format and JSON schema |
| check | Check the installation against electrical rules (NF C 15-100, IEC 60364): protection ratings against cable cross-sections, 30 mA protection and more |
| describe | A compact outline of a document with stable ids, for the agent to read |
| apply_patch | Edit a document by node id, with validation and precise errors |
| render | Draw the single-line and multi-line diagrams |
| viewer_link | A link that opens the document in the web editor (drawing, findings, PDF and SVG downloads) |
| wiring | The wire list and labels for panel wiring |
| bom | The bill of materials |
| list_examples / get_example | Worked example documents |
| normalize | Normalise a document to its canonical form |

## Installation

```
claude mcp add --transport http uniwire https://mcp.uniwire.sh/mcp
```

Any MCP client that speaks Streamable HTTP can add the same URL, with no sign-in. For private documents or offline work, run the server locally: `pip install "uniwire[mcp,pdf]"`, then `uniwire-mcp` (stdio).

## Configuration

```json
{
  "mcpServers": {
    "uniwire": {
      "type": "http",
      "url": "https://mcp.uniwire.sh/mcp"
    }
  }
}
```

## Business Relevance

- **Electrical contractors** draft and check diagrams without CAD, and keep the reviewable document behind the drawing
- **Engineering and design offices** run the NF C 15-100 and IEC 60364 rule checks before anything reaches a client or an inspector
- **Solar, EV-charging and renovation teams** add circuits and check protection ratings against cable cross-sections in the same pass as the edit
- **Facility and maintenance managers** keep diffable documents instead of a drawing someone has to interpret

## Integration with CorpusIQ

uniwire covers the engineering document layer: the installation, validated and checked. CorpusIQ answers the surrounding business question from connected sources such as email, spreadsheets and accounting, so a project discussion that starts in an email can pull the checked diagram, wiring list and bill of materials into the same thread.

Used together: ask CorpusIQ for the project view (quotes, suppliers, invoices, correspondence) and ask uniwire for the technical view (the checked document, the drawing and the BOM). uniwire stays the source of record for the installation document; CorpusIQ remains the place the rest of the question is answered alongside.

## Limitations

- Electrical installations only, focused on the French (NF C 15-100) and international (IEC 60364) families of rules
- v0.1.x, brand new: the registry listing was published October 13, 2026
- The hosted server bounds every call (document size, sheets and time) and keeps result documents for 30 days so the links it returns stay short
- It validates and checks documents; it is not a design authority, so verify against your local standards before construction

## FAQ

### Is it really keyless?

Yes. The hosted endpoint answers without an account or API key: a plain initialize and `tools/list` return all 14 tools with no credentials.

### What can an assistant actually do with it?

Describe an installation in plain words, write or patch the `*.uniwire.json` document, validate it, check it against the NF C 15-100 and IEC 60364 rules, draw the single-line and multi-line diagrams, and export the wire list and bill of materials. Results carry two links: the drawing in the web editor and the PDF.

### Who is it for?

Electrical contractors, engineering and design offices, solar and EV-charging installers, and anyone who reviews or signs off electrical installation documents.

### What does it cost?

The hosted MCP server is free, with no account. The library behind it is open source (Apache-2.0) and can be self-hosted for private or offline work.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - all catalogued business-relevant servers
