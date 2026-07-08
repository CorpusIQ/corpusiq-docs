---
title: Yapp MCP Server Integration Guide
description: Publish pages, PDFs, images, and landing pages instantly through AI agents with Yapp MCP server for Hermes Agent
category: mcp
tags: [mcp, yapp, publishing, landing-pages, content, hermes-agent]
last_updated: 2026-07-08
---

# Yapp MCP — Instant Publishing for Hermes Agent

Turn "build me a page and publish it" into a live URL. Your AI agent can ship HTML, PDFs, images, ZIP sites, and landing pages to a public URL in seconds.

## What It Does

Yapp gives AI agents the ability to publish content directly to the web:

- **HTML pages** — full interactive web pages
- **PDFs** — reports, proposals, invoices
- **Images** — charts, diagrams, screenshots
- **ZIP sites** — multi-file static websites
- **Landing pages** — marketing pages, waitlists, demos

Every published item gets a public URL at `slug.yapp.page`.

## Quick Setup

### Prerequisites
- **Yapp account:** Sign up at [yapp.page](https://yapp.page)
- **Auth method:** Browser OAuth (desktop clients) or API token (terminal/headless clients)

### Add to Hermes Agent

```bash
# Streamable HTTP — connect once and publish forever
hermes mcp add yapp -- url https://yapp.page/mcp
```

Or manual config:

```json
{
  "mcpServers": {
    "yapp": {
      "url": "https://yapp.page/mcp",
      "transport": "streamable-http"
    }
  }
}
```

### Authentication
1. First connection: browser OAuth flow authorizes Yapp
2. Subsequent: token persists, no re-auth needed
3. Terminal clients: use API token from Yapp dashboard

## Key Capabilities

| Tool | Description |
|------|-------------|
| `publish_html` | Publish an HTML page to a live URL |
| `publish_pdf` | Upload and publish a PDF document |
| `publish_image` | Publish an image with optional caption |
| `publish_zip_site` | Deploy a multi-file static site |
| `publish_landing_page` | Create a landing page from template |
| `list_published` | List all your published pages |
| `delete_page` | Remove a published page |

## Use Cases for Business Operators

### 1. Instant Proposals & Reports
Have your AI agent pull data from Stripe, GA4, and HubSpot (via CorpusIQ), then publish a formatted client report as a live URL.

```
Agent prompt: "Pull our MRR from Stripe, this month's sessions from GA4, 
and active deals from HubSpot. Create an executive summary page and publish it with Yapp."
```

### 2. Rapid Landing Pages
Launch a waitlist, demo signup, or product announcement page in seconds without touching a CMS.

```
Agent prompt: "Create a landing page for our new feature launch. 
Include headline, three benefits, CTA button. Publish with Yapp."
```

### 3. Data Dashboards
Publish live-updating HTML dashboards with embedded charts from your business data.

### 4. Internal Memos & Docs
Distribute formatted internal communications with permanent URLs.

## Integration with CorpusIQ

Yapp + CorpusIQ = data-to-published-page pipeline:

1. **CorpusIQ connectors** → pull data from 37+ business platforms
2. **AI agent** → analyze, format, create content
3. **Yapp** → publish as a live URL

This is the closest thing to having an AI analyst who can both do the research AND publish the report.

## Pricing

Free tier available. Check [yapp.page/pricing](https://yapp.page/pricing) for current plans.

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Overview](/hermes/mcp/)*

*↑ [MCP Documentation](/hermes/mcp/)*
