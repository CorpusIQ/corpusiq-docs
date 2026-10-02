---
title: YouSpot MCP
description: Personal CRM and prospecting layer for AI agents. 64 live-verified MCP tools read and write one person's contacts, companies, notes and files plus connected Gmail, Google Calendar, HubSpot, LinkedIn, Slack, Obsidian and X, with an attention engine that surfaces dormant relationships and follow-ups. OAuth 2.1.
category: Business Operations
stars: n/a (no public repo)
added: 2026-09-05
source: mcp.so
relevance: ★★★
tags: [crm, second-brain, prospecting, relationship-management, gmail, hubspot, linkedin, sales-ops, remote-mcp]
---

# YouSpot MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1)** - a personal CRM that turns one person's network into 64 live-verified agent tools spanning the brain graph, connected Gmail, Google Calendar, HubSpot, LinkedIn, Slack, Obsidian and X, plus a company-research engine and an attention engine that computes who went quiet and who is meeting this week. Built by YouSpot (vendor footer credits HubSpot Next), listed in the official MCP registry under the DNS-verified namespace `com.youspot/youspot`, and priced at a flat $10/month.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (browser consent; member API token available for stdio)
Endpoint: https://youspot.com/mcp/v1
Tools: 64 (43 read, 21 write)
Pricing: Pro $10/mo flat (1,000 credits/mo, 1M stored objects) · keyless sandbox free
Category: Business Operations
Built by: YouSpot
```

## Why This Matters for Operators

Every founder or seller lives in the same trap: the relationship data that actually closes deals sits scattered across Gmail threads, calendar invites, a HubSpot portal, LinkedIn messages and Slack DMs, and no single surface answers "who am I forgetting right now". YouSpot puts one agent-accessible layer over all of it, scoped to a single signed-in member, so a chat client can read the network without a data migration project.

**The attention engine is the differentiator: `what_needs_attention` computes from sent mail, the calendar and the LinkedIn export which people went quiet after real correspondence, who is on the calendar this week, and which invitations nobody answered - each item carrying the reason and the numbers behind it.** An operator asks "who should I follow up with today" and gets a ranked list instead of reopening five tabs.

The write surface is real but bounded: agents can draft and send Gmail, create calendar events, log interactions, set follow-ups and send Slack messages, while every mutation routes through the signed-in member's own account permissions. A keyless sandbox endpoint serves the full read surface against a generated demo account, so the whole thing can be evaluated before a credit card exists.

## Tools & Capabilities

| Family | Tools | What they do |
|---|---|---|
| Attention | `what_needs_attention` | Ranked follow-up list: dormant contacts, this week's meetings, unanswered invitations, network shape - each with the reason and source numbers |
| Company research | `research_company`, `find_companies` | In-depth company profiles (industry, size, revenue, funding, founders, competitors, recent news) from the CompanyResearch.ai engine; discovery by criteria |
| Domains | `get_domain_info`, `get_domain_value` | WHOIS registration records and domain valuation for naming or acquisition work |
| Brain graph | `search_graph_objects`, `create_graph_object`, `record_interaction`, `set_follow_up`, `merge_graph_objects`, `find_paths`, `mutual_connections`, `similar_objects` + 12 more | Second-brain CRUD over people, companies, notes and files, with relationship paths and similarity lookups |
| Gmail | `search_gmail_messages`, `get_gmail_message`, `create_gmail_draft`, `send_email`, `archive_gmail_message` + 2 more | Read threads, draft and send from the connected mailbox |
| Calendar | `get_calendar_events`, `list_google_calendars`, `create_calendar_event`, `update_calendar_event` | Read the week ahead, create and move events |
| HubSpot | `ask_about_hubspot_contacts`, `ask_about_hubspot_companies`, `get_hubspot_summary` | Natural-language questions over a connected portal, with summaries |
| LinkedIn | `search_connections`, `get_connections_summary`, `get_my_linkedin_posts`, `linkedin_analytics`, `get_messages_summary`, `top_message_correspondents` + 3 more | Search the imported network, summarize messages, analyze post performance |
| Slack & X | `search_slack_messages`, `get_slack_thread`, `send_slack_message`, `add_slack_reaction`, `get_my_tweets`, `get_twitter_profile`, `get_twitter_following` | Read channels and threads, post and react; read the member's own X activity |
| Files & Obsidian | `read_file`, `save_file_from_url`, `import_contacts_from_file`, `parse_invoice_pdf`, `search_obsidian_notes`, `list_obsidian_vaults` + 2 more | File import with extraction, invoice PDF parsing, Obsidian vault browsing |
| Integrations | `list_integrations`, `get_integration_connect_url`, `disconnect_integration` | Check which accounts are connected, mint connect links, revoke |

The full 64-tool list is served live from the endpoint: `initialize`, `ping` and `tools/list` answer without a credential, so any client can handshake and read the schema before sign-in.

## Installation

```bash
claude mcp add --transport http youspot https://youspot.com/mcp/v1
```

Claude Code registers the client and opens the browser consent screen. In Claude Desktop and ChatGPT, add a custom connector with the same URL and choose OAuth. Clients that only speak stdio can use the `@youspot/mcp` npm shim, which forwards JSON-RPC to the hosted server:

```bash
YOUSPOT_TOKEN=... npx -y @youspot/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "youspot": {
      "type": "http",
      "url": "https://youspot.com/mcp/v1"
    }
  }
}
```

Auth is OAuth 2.1 end to end - no key is pasted into any client config, and every tool call runs under the signed-in member's own account scope. A third endpoint, `https://youspot.com/mcp/sandbox`, serves the read tools against a generated demo account with no credential and no signup; every write tool is refused there. A public server card sits at `youspot.com/.well-known/mcp/server-card.json`.

## Business Relevance

- **Founders and solopreneurs** get a second brain that answers "who am I forgetting" from real correspondence, calendar and LinkedIn signals instead of vibes
- **Sales and BD reps** research a target company, find warm paths through their own network, and set follow-ups without leaving the chat
- **Operators with scattered CRM data** get Gmail, HubSpot and LinkedIn Q&A over one connection while the data stays in the member's accounts
- **Founders naming or acquiring** can check WHOIS records and domain valuations in the same surface as the relationship research

## Integration with CorpusIQ

YouSpot complements CorpusIQ by covering the personal relationship layer that business-data connectors do not: CorpusIQ serves the company's financial and operational picture (Stripe, QuickBooks, Shopify, GA4, HubSpot), while YouSpot serves one person's network, attention and communication history. A composed workflow: an agent pulls the account health and revenue picture from CorpusIQ's Stripe and HubSpot connectors, then asks YouSpot which contacts at that account went quiet and who is meeting them this week, and drafts the follow-up in Gmail with the numbers already in hand.

The two surfaces do not overlap on writes - CorpusIQ stays read-only on business data while YouSpot's write tools run scoped to a single member's own accounts - which makes them a clean pairing for operators who want an agent to act on their behalf without giving it company-level mutation rights.

## Limitations

- Brand new listing (published September 2026) - no track record yet, no public repo to inspect
- Single-member scope: every tool reads and writes one person's own CRM, not a shared team database
- Pro plan caps at 1,000 credits/month, which budgets roughly how much agent activity is covered
- No self-host option; the stdio shim still forwards to the hosted endpoint
- Research and attention quality depends on which accounts the member connects
- The HubSpot Next affiliation appears in the vendor footer but is not independently verified

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
