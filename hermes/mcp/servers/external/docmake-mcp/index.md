---
title: "DocMake MCP - Template-Driven DOCX and PDF Generation"
description: "Official MCP server for the DocMake document generation platform: build a template once in a visual editor and render DOCX or PDF files from data, with six tools, MCP resources and a guided render prompt; stdio via npx, MIT."
category: Productivity
stars: "0 (new listing, docmake-io/mcp)"
added: 2026-08-31
source: "chatmcp/mcpso issue #3849 (Aug 31, 2026 afternoon sweep)"
relevance: ★★
tags: [mcp-server, documents, docx, pdf, templates, automation, stdio]
---

# DocMake MCP

**Document generation from templates, driven by an agent.** DocMake is a document generation platform: you build a template once in a visual editor with variables, conditionals and loops, then render it with data. This official MCP server gives an AI assistant direct access to that pipeline - it lists the templates in your workspace, returns the field tree for any of them, renders a template to DOCX or PDF and writes the file to a local directory.

```
Server type: Local (stdio via npx)
Package: @docmake/mcp (npm, v0.1.1)
Registry: io.docmake/mcp (listed on registry.modelcontextprotocol.io)
Repo: github.com/docmake-io/mcp (MIT)
Website: docmake.io/mcp
Tools: 6 (list_templates, get_template, render_document, create_template, import_docx, get_usage)
Extras: templates exposed as MCP resources, plus a generate-document prompt for guided renders
```

## Why This Matters for Operators

Contracts, invoices, proposals and reports are the paperwork layer of every business. DocMake turns them into a repeatable agent workflow.

First, **templates separate form from data.** A human builds the template once with variables, conditionals and loops; the agent then fills it from real data - CRM records, pricing tables, compliance checklists - without ever touching the layout.

Second, **renders are strict by default.** If a variable has no value, the render fails loudly instead of shipping a document with blank fields. That fail-closed behavior matters when the output is a signed contract or a client invoice.

Third, **plan usage is self-reported.** The `get_usage` tool returns plan, render quota and rate limits for the current billing period, so an agent can pace batch renders instead of hitting a wall mid-run.

## Tools and Capabilities

Tool list verified from the official README (Aug 31, 2026):

| Tool | What it does |
|------|--------------|
| `list_templates` | List the templates in your workspace, with search and pagination |
| `get_template` | A template's field tree: every variable it expects, ready to map to render data |
| `render_document` | Render a template to PDF or DOCX and save the file locally |
| `create_template` | Create a new template from a document schema JSON |
| `import_docx` | Import a local .docx file as a new template (base64 on the remote server) |
| `get_usage` | Plan, render quota, and rate limits for the current billing period |

Templates are also exposed as MCP resources, and the server ships a `generate-document` prompt for a guided render flow.

## Installation

```bash
npx @docmake/mcp
```

Add to a client config (example for Claude Desktop or VS Code):

```json
{
  "mcpServers": {
    "docmake": {
      "command": "npx",
      "args": ["@docmake/mcp"]
    }
  }
}
```

## Configuration

Create an account at docmake.io and put your API key in the environment the stdio server inherits (the key is read from the standard environment variable the setup guide documents). Templates are managed in the DocMake visual editor; the MCP server renders them from the agent side.

## Business Relevance

- **Sales and ops teams** render proposals, quotes and invoices from CRM data without copy-paste.
- **Legal and compliance** keep one canonical contract template and fill it per counterparty with strict rendering.
- **Reporting** turns structured data into branded PDF and DOCX deliverables on a schedule.

## Integration with CorpusIQ

DocMake and CorpusIQ fit the data-to-document pipeline end to end. CorpusIQ's read-only connectors pull the source numbers - Stripe revenue, QuickBooks balances, HubSpot deal stages, GA4 metrics - with citations. DocMake renders those numbers into the branded DOCX or PDF the client actually signs or reads. An agent can ask for last quarter's numbers via CorpusIQ, map them into the field tree DocMake returns, and render the finished report, all in one workflow.

## Limitations

- Brand new: repo created Aug 31, 2026, npm v0.1.1, zero stars.
- Requires a DocMake account and API key; no anonymous mode.
- stdio transport only - no hosted MCP endpoint.
- Renders are strict by design; missing variables abort rather than produce partial documents.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
