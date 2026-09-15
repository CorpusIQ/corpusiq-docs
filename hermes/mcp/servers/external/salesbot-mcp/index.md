---
title: "Salesbot MCP: LinkedIn Prospecting and CRM with Human"
description: "Hosted LinkedIn and Sales Navigator MCP server with 48 safety-gated tools for AI-assisted B2B prospecting: lead discovery, human-approved outreach, inbox workflows, campaigns, and a built-in CRM with stages, notes, tasks, and custom fields. Every send is gated by approval and server-side limits."
category: Marketing
stars: n/a (new listing)
added: 2026-08-24
source: "chatmcp/mcpso issue #3730"
relevance: ★★★
tags: [linkedin, sales, crm, prospecting, outreach, lead-generation, remote-mcp]
---

# Salesbot MCP

**Hosted LinkedIn MCP server and Sales Navigator MCP for AI-assisted B2B prospecting.** Built by Salesbot (salesbot.cz) on Supabase Edge Functions, it exposes 48 safety-gated tools for lead discovery, profile research, contact and campaign management, message drafting with approval, inbox workflows, and a built-in sales CRM. AI-initiated outbound messages require human approval, and server-side daily and hourly limits keep LinkedIn accounts inside safe ranges.

```
Server type: Remote (Streamable HTTP, Supabase Edge Functions)
Auth: API key (x-mcp-api-key header, sb_mcp_ prefix)
Endpoint: https://app.salesbot.cz/api/mcp
Tools: 48 (verified by anonymous tools/list)
Pricing: Subscription or trial required; API key minted in-app
Category: Marketing / Sales / CRM
Built by: Salesbot (repo: Kubis010/linkedin-mcp-server-salesbot, MIT)
```

## Why This Matters for Operators

LinkedIn outreach usually means choosing between spreadsheets plus manual messages and full-automation tools that burn accounts. Salesbot lands in the middle on purpose: the agent does the research, drafting, and CRM hygiene, while every send sits behind human-in-the-loop approval and enforced daily limits. **The approval gate is structural, not advisory** - drafts wait in a pending queue, the operator approves or rejects with feedback, and a second-pass quality check catches hallucinations and tone failures before anything leaves.

For a B2B operator, the practical win is volume without recklessness: one agent can research hundreds of prospects, draft personalized first messages per account context, and stage them for approval in the time a human rep writes ten.

## Tools & Capabilities

All 48 tool names captured by live anonymous `tools/list` against the endpoint. Grouped by area:

| Area | Tools |
|---|---|
| Connection | `get_linkedin_status`, `connect_linkedin` (returns a browser auth link, ~2h validity) |
| Lead discovery | `search_linkedin_people`, `search_google_xray`, `search_linkedin_navigator`, `search_job_postings`, `get_job_posting_details`, `search_web`, `scrape_website`, `enrich_contacts` |
| Contacts | `get_contact_profile`, `list_contacts`, `update_contact` |
| Campaigns | `create_campaign`, `update_campaign_settings`, `start_campaign`, `stop_campaign`, `list_campaigns`, `add_contacts_to_campaign` |
| Message workflow | `generate_campaign_message`, `list_pending_approvals`, `approve_message`, `reject_message` |
| Sending | `send_linkedin_message`, `send_connection_request`, `publish_linkedin_post`, `get_daily_limits` |
| Inbox | `list_inbox_chats`, `get_chat_messages`, `reply_to_chat`, `mark_chat_read` |
| CRM | `set_deal_stage`, `log_crm_note`, `create_task`, `list_tasks`, `complete_task`, `save_lead_message`, `list_lead_messages`, `get_lead_context`, `export_crm`, `list_crm_stages`, `add_crm_stage`, `rename_crm_stage`, `delete_crm_stage`, `list_crm_fields`, `add_crm_field`, `delete_crm_field`, `set_lead_fields` |

Notable safety mechanics: `reply_to_chat` scans inbound text for prompt injection before sending, campaigns respect allowed sending hours and return `OUTSIDE_ALLOWED_HOURS`, and connection requests always go out empty-note to avoid account blocks.

## Installation

```bash
claude mcp add --transport http salesbot https://app.salesbot.cz/api/mcp --header "x-mcp-api-key: sb_mcp_YOUR_KEY"
```

Get the `sb_mcp_` key in the Salesbot app under Settings > MCP. An active subscription or trial is required.

## Configuration

```json
{
  "mcpServers": {
    "salesbot": {
      "type": "http",
      "url": "https://app.salesbot.cz/api/mcp",
      "headers": {
        "x-mcp-api-key": "sb_mcp_YOUR_API_KEY"
      }
    }
  }
}
```

Send the key in the `x-mcp-api-key` header, not as an Authorization bearer token - the Supabase gateway rejects unknown bearer tokens before they reach the server. LinkedIn itself connects via a white-labeled auth link (`auth.salesbot.cz`): the agent calls `get_linkedin_status`, then `connect_linkedin`, and the operator finishes login in the browser.

## Business Relevance

- **B2B sales teams** run lead discovery, personalized drafting, and CRM updates from one agent surface
- **Founders doing their own outreach** keep a full contact and campaign system without a CRM migration
- **Recruiters** use `search_job_postings` plus `get_job_posting_details` to find hiring managers behind open roles
- **Agencies** stage and approve client outreach through the pending-approval queue

## Integration with CorpusIQ

CorpusIQ holds the commercial record (pipeline in HubSpot, invoices in QuickBooks, site traffic in GA4). Salesbot holds the outreach surface. An agent can pull an account's revenue history and support signals from CorpusIQ connectors, then research the buying committee on LinkedIn through Salesbot, draft the message with that context, and log the outcome back into the CRM. The CorpusIQ lead pipeline and Salesbot's built-in CRM stay reconcilable because both expose stages, notes, and contact fields over MCP.

## Limitations

- Czech-based vendor (salesbot.cz); defaults like `search_web` country/language start at cz/cs and some quality checks are Czech-aware.
- Human-in-the-loop approval adds friction by design; there is no fully autonomous send mode below the operator's setting.
- LinkedIn actions go through a third-party integration provider; account safety still depends on LinkedIn's own limits.
- New listing (Aug 24, 2026); repo has no star history yet.
- Pro-plan gating on some tools (e.g. `create_task`).

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [SalesTouch MCP](/docs/hermes/mcp/servers/external/salestouch-mcp) - LinkedIn GTM prospecting platform
- [LinkedIn Ghostwriter MCP](/docs/hermes/mcp/servers/external/linkedin-ghostwriter-mcp) - LinkedIn posts in your voice
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
