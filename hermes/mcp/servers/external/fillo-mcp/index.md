---
title: "Fillo MCP - Headless Form Infrastructure for AI Agents"
description: "Official MCP server for Fillo headless form infrastructure: provision workspaces, build and publish forms, and read responses, with forms rendering natively via React and DOM SDKs instead of iframes, MIT licensed"
category: Operations
stars: n/a (new listing)
added: 2026-08-18
source: "mcp.so GitHub issue #3629"
relevance: ★★
tags: [forms, lead-generation, surveys, headless-forms, operator-automation, remote-mcp, open-source]
---

# Fillo MCP

**Official MCP server for Fillo, a headless form infrastructure product.** A coding agent can provision a workspace, build and publish forms, and read responses through MCP. Forms render natively inside the host product via the `@usefillo/react` and `@usefillo/dom` SDKs instead of an iframe, and file uploads go browser-direct to customer-owned storage.

```
Server type: Remote (Streamable HTTP) or stdio
Auth: Fillo workspace credentials
Endpoint: https://fillo.so/api/mcp  |  npx -y @usefillo/mcp
Tools: workspace provisioning, form build/publish, response reading
Pricing: Free tier; paid plans for production volume
Category: Forms / Lead Generation
Registry: io.github.jacobfunch/usefillo
Built by: Fillo (fillo.so)
```

## Why This Matters for Operators

Forms are the quiet plumbing of every operator's funnel: lead capture, surveys, intake, applications. Historically they live in a form SaaS with a dashboard, siloed from the agent workflows doing the follow-up. Fillo flips that: the MCP server makes forms programmable, so an agent can spin up a lead form, publish it, and read responses in the same session where it updates the CRM and drafts the follow-up.

The native-rendering SDKs solve the classic embedded-form problem (janky iframes), and browser-direct uploads to customer-owned storage keep file data out of the form vendor's hands — a real compliance advantage for intake forms.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| Workspace provisioning | Create and configure a form workspace from chat |
| Form building | Define fields, validation, and logic as structured calls |
| Form publishing | Publish forms and retrieve embed or SDK configuration |
| Response reading | Pull submissions with their metadata |

## Installation

```bash
# remote
claude mcp add --transport http fillo https://fillo.so/api/mcp

# stdio
npx -y @usefillo/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "fillo": {
      "command": "npx",
      "args": ["-y", "@usefillo/mcp"]
    }
  }
}
```

## Business Relevance

- **Growth operators** generate lead forms inside the same agent session that qualifies the leads
- **Agencies** provision per-client forms programmatically instead of clicking through dashboards
- **Product teams** ship native-feeling forms inside their apps without iframe compromises
- **Compliance-conscious teams** keep file uploads on customer-owned storage
- **Automation builders** fold form creation and response reads into multi-step agent workflows

## Integration with CorpusIQ

CorpusIQ closes the loop Fillo opens: Fillo captures the response, CorpusIQ tracks the resulting business — the lead in the CRM, the invoice in QuickBooks, the charge in Stripe. An agent can read new form submissions, qualify them against historical customer data through CorpusIQ connectors, and log the follow-up in the pipeline, all in one session.

## Limitations

- New listing (Aug 2026), early product stage
- Form feature depth (logic, branching, payments) less proven than established form SaaS
- Free tier limits undisclosed at listing time
- Requires coding-agent workflows; no no-code builder path documented
- SDK ecosystem young (React and DOM only)

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
