---
title: "Asyntai MCP - AI Support Agent for Websites"
description: "Hosted MCP for Asyntai, an AI support agent that answers website visitors from the site's own content. 54 tools to manage the knowledge base, read conversations and leads, take over live chats, edit agent instructions and check plan usage. OAuth 2.1, free with every Asyntai account."
category: Customer Support
stars: "n/a (new listing, asyntai/mcp-bridge)"
added: 2026-09-03
source: "mcp.so GitHub issue #3907"
relevance: ★★
tags: [customer-support, chatbot, knowledge-base, live-chat, leads]
---

# Asyntai MCP - AI Support Agent for Websites

**Hosted MCP server (Streamable HTTP, OAuth 2.1)** - the connector that puts an Asyntai website support agent inside any MCP client. The agent answers visitors from the site's own content; the MCP exposes 54 tools for managing its knowledge base, conversations, leads and plan usage.

## Spec Block

| Field | Value |
|---|---|
| Server name | Asyntai support agent (com.asyntai/support-agent) |
| Repo | github.com/asyntai/mcp-bridge (stdio-to-hosted bridge) |
| Endpoint | https://asyntai.com/mcp |
| Transport | Streamable HTTP |
| Auth | OAuth 2.1 with dynamic client registration, no API key |
| Tools | 54 tools (knowledge base, conversations, leads, live-chat takeover, plans, webhooks) |
| npm | @asyntai/mcp |
| License | MIT |
| Pricing | Free with every Asyntai account |

## Why This Matters for Operators

A website chatbot is only as good as the content behind it. Asyntai's MCP gives an agent the same controls a support manager has in the dashboard: see what the AI could not answer, correct the knowledge base, watch conversations and captured leads, and step into a live chat to reply as a human. The verified endpoint (401 on anonymous probe) is maintained by the Asyntai team with an official registry record.

## Tools & Capabilities (54 tools)

Capability-level table from vendor documentation; exact schemas require OAuth sign-in (anonymous enumeration is refused).

| Group | Representative tools |
|---|---|
| Knowledge base | list_knowledge, add_knowledge_text, add_knowledge_url, start_crawl, search_knowledge_base, get_knowledge_entry, delete_knowledge_entry, set_knowledge_tags, list_knowledge_gaps |
| Websites and widget | list_websites, get_website, create_website, get_widget_settings, update_widget_settings, update_website_features, list_widget_translations |
| Conversations and leads | list_conversations, take_over_conversation, send_agent_reply, release_conversation, list_leads, list_tickets, list_active_sessions |
| Plans and admin | list_plans, list_team_members, list_webhooks, delete_webhook, list_audit_log, get_daily_report, set_daily_report |

## Installation

Remote (Claude, Cursor, ChatGPT, VS Code): add `https://asyntai.com/mcp` as a remote MCP server and sign in when prompted.

Stdio clients:

```json
{ "mcpServers": { "asyntai": { "command": "npx", "args": ["-y", "@asyntai/mcp"] } } }
```

## Configuration

OAuth 2.1 sign-in with dynamic client registration - no API key to create or paste. Each tool works on your account only, scoped by your Asyntai login.

## Business Relevance

Support operations without leaving the agent: list knowledge gaps to know what documentation to write next, review conversations and leads the chat widget captured, take over live chats for escalations, and check plan usage before committing to volume. Useful for SaaS operators, agencies managing client sites, and any business running a website support agent.

## Integration with CorpusIQ

Chat-captured leads complement CorpusIQ's connector data: route Asyntai leads into the CRM alongside GA4 and Stripe figures, and feed unanswered-question reports back into CorpusIQ to prioritize content and product decisions.

## Limitations

Brand new (repo created Sep 2, 2026, 0 stars). Anonymous enumeration of the 54 tools is refused by the OAuth gate - the table above is capability-level from vendor docs. The product is a website widget chatbot, not a full helpdesk replacement.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [AnswerLoops MCP - Community Support Knowledge Base for Agents](/docs/hermes/mcp/servers/external/answerloops-mcp)
- [imap-mcp - Read-Only IMAP Mailbox Operations for Agents](/docs/hermes/mcp/servers/external/imap-mcp)
- [BusyMail MCP - Human-Approval Email over MCP](/docs/hermes/mcp/servers/external/busymail-mcp)
