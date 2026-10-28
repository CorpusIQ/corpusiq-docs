---
title: "MCP Apps: Interactive UIs Inside Claude and ChatGPT"
description: "MCP Apps is the first official MCP extension. Tools can now return interactive dashboards, forms, and visualizations that render inside Claude and ChatGPT. How it works, client support, and security."
canonical: "/hermes/mcp/mcp-apps-interactive-ui/"
robots: "index, follow"
tags: [mcp, apps, ui, interactive, dashboards, claude, chatgpt, extension]
last_updated: "2026-10-24"
---

# MCP Apps: Interactive UIs Inside Claude and ChatGPT

MCP Apps is the first official MCP extension, live since January 26, 2026.
It lets tools return interactive UI components that render directly in the
conversation: dashboards, forms, visualizations, multi-step workflows, and
more. This page covers what it is, how it works, client support, and the
security model.

## What MCP Apps enables

Before MCP Apps, a tool returned text. The user read a summary and asked
follow-up questions to explore the data. With MCP Apps, a tool can return an
interactive dashboard. The user filters by region, drills into a specific
account, sorts a column, and exports a report without leaving the
conversation. The model stays in the loop and sees what the user does.

Typical use cases:

- Data exploration: a sales analytics tool returns an interactive dashboard
- Configuration wizards: a deployment tool presents a form with dependent
  fields
- Document review: a contract analysis tool displays the PDF inline with
  highlighted clauses
- Real-time monitoring: a server health tool shows live metrics that update
  as systems change

## How it works

MCP Apps relies on two MCP primitives:

1. Tools with UI metadata. A tool declares a `_meta.ui.resourceUri` field
   pointing to a UI resource.
2. UI resources. Server-side resources served via the `ui://` scheme,
   containing bundled HTML and JavaScript.

Example tool declaration:

```javascript
{
  name: "visualize_data",
  description: "Visualize data as an interactive chart",
  inputSchema: { /* ... */ },
  _meta: {
    ui: {
      resourceUri: "ui://charts/interactive"
    }
  }
}
```

The host fetches the resource, renders it in a sandboxed iframe, and enables
bidirectional communication via JSON-RPC over postMessage. The UI can call
server tools, update the model context, and send follow-up messages.

## Client support

- Claude: available on web and desktop since launch
- ChatGPT: not listed for the extension. ChatGPT renders widgets through
  OpenAI's own Apps SDK, so the same server ships both paths
- Visual Studio Code: supported
- Goose: supported

Support is per client and moves with client releases. Check the
[client matrix](https://modelcontextprotocol.io/extensions/client-matrix)
before relying on rendering in any host. For the full mechanism, the
security model, and the checks worth running before trusting an
"interactive" claim, see [MCP Apps in the product docs](/docs/mcp-apps/).

## Security model

- Iframe sandboxing: all UI content runs in sandboxed iframes with
  restricted permissions
- Pre-declared templates: hosts can review HTML content before rendering
- Auditable messages: all UI-to-host communication goes through loggable
  JSON-RPC
- User consent: hosts can require explicit approval for UI-initiated tool
  calls

## MCP Apps and CorpusIQ

CorpusIQ uses MCP Apps to render verified business answers as interactive
dashboards inside Claude and ChatGPT. The model computes the analysis, the
CorpusIQ engine validates and reconciles the data, and the app renders the
result with source citations and a reconciliation strip. See the
[runbook governance](/hermes/mcp/runbook-governance) and
[response contract](/hermes/mcp/runbook-response-contract) pages for the
governance layer behind these answers.

For the product view of the same mechanism, see
[how CorpusIQ builds a verified answer](https://www.corpusiq.io/mcp?utm_source=docs&utm_medium=organic&utm_campaign=docs-content),
and the [connector hub](https://www.corpusiq.io/connectors?utm_source=docs&utm_medium=organic&utm_campaign=docs-content)
for the tools this pipeline reads from.

## Resources

- [MCP Apps announcement](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/)
- [MCP Apps documentation](https://modelcontextprotocol.io/docs/extensions/apps)
- [Getting Started with MCP Apps](https://apps.extensions.modelcontextprotocol.io/api/documents/Quickstart.html)
- SDK: @modelcontextprotocol/ext-apps
- [Examples repository](https://github.com/modelcontextprotocol/ext-apps)
