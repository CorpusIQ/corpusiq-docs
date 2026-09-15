---
title: "Reach MCP - Operate a Real LinkedIn Account from Your Agent"
description: "Hosted MCP server that lets an AI agent operate a real LinkedIn account: 52 tools for the inbox, invitations, network, profiles, natural-language Sales Navigator search, posts, engagement and publishing, with server-side daily quotas, idempotent writes, signed webhooks and six ready-made playbooks served as MCP prompts."
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-09-10
source: mcp.so feed
relevance: ★★★
tags: [linkedin, sales-navigator, outreach, prospecting, social-selling, remote-mcp, oauth]
---

# Reach MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1)** - a hosted connector that puts a real LinkedIn account in the hands of an AI agent: read and answer the inbox, send and accept invitations, search Sales Navigator in plain language, publish posts and engage - with the controls an operator needs around every call. Built by the team behind Kanbox (2,000+ teams, 2 million LinkedIn messages sent). LinkedIn only, by design.

```
Server type: Remote (hosted, Streamable HTTP, stateless)
Auth: OAuth 2.1 sign-in, API key fallback (?api_key=mcp_... or X-API-Key)
Endpoint: https://app.reachmcp.com/mcp
Docs for agents: https://www.reachmcp.com/llms.txt
Tool reference: https://www.reachmcp.com/docs/mcp-tools.md
```

## What the Agent Gets - 52 Tools

| Area | Tools |
|---|---|
| Start here | `reach_playbooks` - six ready-made workflows |
| Inbox | `list_conversations`, `list_conversation_messages`, `send_message`, `react_message`, `star_conversation`, `archive_conversation`, `delete_conversation` |
| Sales Navigator inbox | `salesnav_list_messaging_threads`, `salesnav_list_thread_messages`, `salesnav_send_message` |
| Network | `list_connections`, `connect`, `invitation_status`, `withdraw_invitation`, `accept_invitation`, `decline_invitation`, `remove_connection`, `follow`, `list_received_invitations`, `list_sent_invitations` |
| Profiles & search | `scrape_profile`, `scrape_search`, `visit_profile`, `profile_viewers`, `salesnav_resolve_industry`, `salesnav_typeahead`, `salesnav_build_search_url` |
| Posts & engagement | `user_posts`, `scrape_post`, `scrape_my_posts`, `like_post`, `comment_post`, `reply_comment` |
| Publishing | `create_post`, `list_scheduled_posts`, `update_scheduled_post`, `delete_scheduled_post`, `upload_media_from_url`, `create_multi_photo` |
| Accounts & quotas | `list_accounts`, `get_me`, `get_account_quotas`, `update_account_quotas`, `get_account_request_logs`, `get_account_request_logs_stats`, `delete_account` |
| Webhooks | `list_webhook_endpoints`, `create_webhook_endpoint`, `update_webhook_endpoint`, `delete_webhook_endpoint`, `test_webhook_endpoint` |

Every tool carries MCP annotations (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`), a description on every parameter, and an output schema.

## Six Playbooks, Served as MCP Prompts

- **My LinkedIn week in review** - activity, rotting invitations, waiting conversations (read-only).
- **Wake up cold conversations** - threads where you spoke last and nobody answered, with a draft follow-up each.
- **Turn post reactions into leads** - everyone who liked or commented on your posts, qualified and messaged.
- **Turn profile viewers into leads** - the people who checked you out, scored and given an opener.
- **Reply to every comment** - a real answer to each comment on your recent posts, in the commenter's language.
- **A prospect list from one sentence** - "heads of sales at French SaaS companies" becomes a real Sales Navigator search, the rows, and a personalised invitation each.

## Guardrails Built for Agents

- **Daily quotas enforced server-side** - invitations, messages, visits, imports, posts, comments and reactions each have a per-account limit checked before every write. Exceed it and the call is refused with `daily_quota_reached` and the reset time.
- **Structured errors** - every failure carries a stable `code`, `safe_to_retry`, `retry_at` and a `remediation` sentence; MCP failures are `isError` results, not protocol errors.
- **Idempotent writes** - pass `idempotency_key` on any write; a retry after a timeout never sends twice.
- **Signed webhooks** - `message.received`, `connection.new`, `account.status_changed`, `quota.threshold_reached`, `quota.reached`. Stripe-style HMAC signature, retries for 15 hours, replay from the dashboard.
- **Natural-language Sales Navigator search** - industries resolved against LinkedIn's taxonomy, geographies and companies against live autocomplete, disambiguation on ambiguous terms.
- **Residential proxy per account** and human-like pacing.

## Connection

```
{ "mcpServers": { "reach": { "url": "https://app.reachmcp.com/mcp" } } }
```

Sign up at app.reachmcp.com/signup and connect a LinkedIn account with the Chrome extension (your own session; no password is typed into Reach; uninstalling revokes access). Ask *"What can you do with my LinkedIn?"* - the `reach_playbooks` tool returns the six workflows. Every playbook that writes shows a numbered preview and waits for your go.

## Pricing

- **Standard** - one account for a person running their own LinkedIn from Claude or ChatGPT: $39/month, graduated down to $12.
- **Builder** - for agencies and products built on the API/MCP: $10 per account for 1-4, $7 for 5-10, $6 for 11-50, $5 from 51. Ten accounts: $70/month.

7-day trial, no card. Monthly, no commitment. Also available as REST: base `https://app.reachmcp.com/api`, header `X-API-Key`, OpenAPI at `https://app.reachmcp.com/openapi.json`.

## Verification (Sep 10, 2026 night sweep)

Endpoint `https://app.reachmcp.com/mcp` live-probed over JSON-RPC: anonymous initialize rejected with HTTP 403 - live, OAuth-gated endpoint. Docs, tool table, quotas, webhooks and pricing all published on the listing page.

## Honest About Risk

Reach MCP is not an official LinkedIn API: it relies on the account owner's authenticated session and LinkedIn's internal interfaces. LinkedIn automation carries real account risk; the proxy, enforced limits and pacing reduce it, nothing removes it. Data is processed in the EU (Google Cloud, europe-west1); session cookies are stored encrypted and removed when the account is deleted.

## See Also

- [CampaignStack MCP - Safe LinkedIn and Email Outreach](/docs/hermes/mcp/servers/external/campaignstack-mcp)
- [AdPlug LinkedIn Ads MCP - B2B Campaign Control for Agents](/docs/hermes/mcp/servers/external/adplug-linkedin-ads-mcp)
- [MisarReach MCP - Outbound Sales and Lead Pipeline for AI Agents](/docs/hermes/mcp/servers/external/misarreach-mcp)
- [FoundRole MCP - Fact-Checked AI Job Search and Application Tracking](/docs/hermes/mcp/servers/external/foundrole-mcp)
