---
title: "Gambot MCP - WhatsApp Business Messaging and CRM for Agents"
description: "MCP server for the Gambot WhatsApp Business API, an official Meta-approved WhatsApp Business Solution Provider. 77 documented tools send messages and templates, run campaigns from Excel mail-merge or CRM-filter audiences, and manage contacts, leads, cases, tasks, quotes, invoices, orders, forms and signatures. stdio via npx gambot-mcp with a Gambot token; MIT repo."
category: Communication & Email
stars: n/a (new listing)
added: 2026-09-14
source: "mcp.so feed (gambot) + repo github.com/gambot-ai/gambot-mcp README + npm gambot-mcp"
relevance: ★★★
tags: [whatsapp, messaging, crm, campaigns, leads, sales, marketing, stdio]
---

# Gambot MCP

**stdio MCP server (npx gambot-mcp, MIT)** - the agent interface for Gambot, an official, Meta-approved WhatsApp Business Solution Provider. It wraps the Gambot REST API (api.gambot.co.il/api/v1) and exposes 77 documented tools, so a sales or support team drives the WhatsApp side of the business from Claude, Cursor or any MCP client: send messages and approved templates, run campaigns, and work the full CRM record around each conversation - contacts, leads, cases, tasks, quotes, invoices, orders, forms, signatures and users. The npm package (gambot-mcp 1.0.0) and the repo README verify every tool name below.

```
Server type: stdio (npx -y gambot-mcp, local process wrapping the Gambot REST API)
Auth: Gambot Token (gmbt_... from the admin panel, Settings, General) via env
Endpoint: https://api.gambot.co.il/api/v1 (REST base wrapped by the server; GAMBOT_API_BASE overrides)
Tools: 77 documented (messaging, templates, campaigns, CRM records, onboarding)
Pricing: Gambot account required; free-trial and paid account creation are built into the tools
Category: Communication & Email
Built by: Gambot (gambot.co.il), repo gambot-ai/gambot-mcp, MIT
```

## Why This Matters for Operators

For many businesses WhatsApp is the primary customer channel, but the CRM record lives somewhere else and the agent-accessible layer does not exist at all. Gambot MCP closes that gap: the assistant that already knows the order history can move the conversation forward in the channel the customer actually reads. Campaigns support audiences from an Excel sheet (mail-merge rows with a column-to-variable mapping) or CRM filters, with manual, scheduled and recurring send modes, and every organization has an active opt-out flow - recipients replying stop or unsubscribe are excluded from future broadcasts, and send responses echo the opt-out and consent state. That compliance plumbing is the difference between a WhatsApp integration an operator can use and one that gets the number banned.

## Tools & Capabilities

| Family | Representative tools |
|---|---|
| Messages | `gambot_send_text`, `gambot_send_template`, `gambot_get_conversation_messages`, `gambot_list_conversations` |
| Templates | `gambot_list_templates`, `gambot_get_template`, `gambot_get_template_variables`, `gambot_create_template`, `gambot_upload_template_media` |
| Campaigns | `gambot_create_campaign`, `gambot_send_campaign`, `gambot_send_campaign_from_excel`, `gambot_run_campaign`, `gambot_test_campaign`, `gambot_get_campaign_results`, `gambot_list_scheduled_campaigns`, `gambot_update_campaign`, `gambot_delete_campaign` |
| CRM records | contacts, leads, cases, tasks, quotes, orders and their field tools (`gambot_get_contact_fields`, `gambot_create_lead`, `gambot_update_case`, `gambot_create_quote`, `gambot_update_order`) |
| Money documents | `gambot_create_invoice`, `gambot_issue_invoice`, `gambot_list_invoices`, `gambot_get_signature_link`, `gambot_create_document_link` |
| Web forms | `gambot_list_forms`, `gambot_get_form_link`, `gambot_get_form_submissions` |
| Users | `gambot_create_user`, `gambot_list_users`, `gambot_update_user`, `gambot_enable_user`, `gambot_disable_user` |
| Onboarding | `gambot_check_organization`, `gambot_search_available_numbers`, `gambot_create_trial_account`, `gambot_create_paid_account`, `gambot_get_waba_connect_link`, `gambot_exchange_waba_token` |

Send and campaign responses echo consent (`consentConfirmed`, defaults to true) and opt-out state, so agents can assert consent-to-mail before broadcasts.

## Installation

```json
{
  "mcpServers": {
    "gambot": {
      "command": "npx",
      "args": ["-y", "gambot-mcp"],
      "env": {
        "GAMBOT_TOKEN": "gmbt_your_token_here"
      }
    }
  }
}
```

Node.js 18+ required. The token comes from the Gambot admin panel (Settings, General) and can be rotated or scope-narrowed there. A one-click Cursor install link is included in the repo README. The server ships a `server.json` manifest for the official MCP Registry and a `smithery.yaml`, so aggregator coverage follows the npm publish.

## Business Relevance

- **Sales teams** work leads and WhatsApp threads from the assistant, with cases, tasks and quotes in reach of the same conversation.
- **Marketing teams** run template campaigns from Excel audiences or CRM filters, with scheduling and per-campaign results.
- **Support teams** read conversation history and move cases forward without switching tools.
- **Finance and ops** generate quotes, invoices and payment/signature links for WhatsApp-first customers.
- **Founders** get an entire WhatsApp CRM operated from one assistant session.

## Integration with CorpusIQ

Gambot carries the conversation; CorpusIQ reads the business. A CorpusIQ agent can pull customer segments and revenue context (Shopify buyers, Stripe payments, HubSpot pipeline, QuickBooks balances) and hand the right audience to a Gambot campaign - for example, a mail-merge blast to numbers from a sheet, or a re-engagement run filtered from the CRM - then read campaign results and check the revenue effect back in CorpusIQ. Inbound WhatsApp activity becomes the customer-facing edge of the same operational picture the rest of the connectors describe.

## Limitations

- stdio only: no hosted remote endpoint; each client runs the npx process locally and holds the token in its env.
- Sending is regulated: WhatsApp template approval, opt-out handling and consent state apply to every broadcast, and the built-in opt-out flow is mandatory infrastructure rather than optional.
- The vendor is Israel-based (gambot.co.il) and some onboarding tools provision accounts, numbers and payment links - treat those as spend-affecting actions.
- Brand new listing: npm 1.0.0, no long third-party track record yet.
- Number purchase, paid accounts and campaign volume carry Gambot-side costs.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [Mobile Text Alerts MCP - Official SMS Sending for Agents](/hermes/mcp/servers/external/mobile-text-alerts-mcp)
- [InstantReply MCP - Instagram, WhatsApp and Messenger Inbox for Agents](/hermes/mcp/servers/external/instantreply-mcp)
