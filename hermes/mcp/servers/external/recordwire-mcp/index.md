---
title: "Recordwire MCP - US Business Registry Data for Agents"
description: "Remote MCP server over official US business registries in seven states. Agents search companies, read one business in full, page its change history, search the change-event feed, and check per-state freshness - with change subscriptions and signed webhooks on the full-coverage plan."
category: Business Data
stars: n/a (new listing)
added: 2026-09-11
source: "mcp.so feed + chatmcp/mcpso issue #4079"
relevance: ★★★
tags: [business-data, company-registry, change-events, due-diligence, compliance, remote-mcp]
---

# Recordwire MCP

**Remote MCP server (Streamable HTTP, bearer API key)** - the official business registries of seven states as agent tools. Recordwire lets an agent look up real companies instead of guessing at them: search businesses, fetch one company in full, read its change history, search the change-event feed, and check how fresh each state's data is. The same `rk_live_...` key works for both the REST API and MCP, with the same state restrictions.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer API key (rk_live_ prefix) in the Authorization header
Endpoint: https://api.recordwirehq.com/mcp
Tools: 8 live-probed (tools/list open; tool calls require a key)
Pricing: Paid plans from $200/month; keys can be restricted per state
Coverage: Florida, New York, Colorado, Pennsylvania, Virginia, Connecticut, Oregon
Category: Business Data
Built by: Recordwire (recordwirehq.com)
```

## Tools

| Tool | Purpose |
|---|---|
| search_businesses | Find businesses by jurisdiction, formation window, status, entity type or free text; cursor-paginated, IDs like US-VA:11406679 |
| get_business | One business in full by ID, dates in YYYY-MM-DD |
| get_business_events | The change history for one business ID, cursor-paginated |
| search_events | Search the change feed - business.created, business.name_changed, business.status_changed, business.address_changed, business.agent_changed, business.officers_changed |
| list_sources | Available registry sources and their latest verified dates |
| create_subscription | Subscribe an HTTPS endpoint to new registry changes; the returned secret is shown once |
| list_subscriptions | List your subscriptions without exposing secrets |
| delete_subscription | Revoke a change subscription |

MCP itself is request-and-response, so an agent reads the feed rather than being pushed to; change subscriptions with signed webhooks run on the Full coverage plan.

## Connection

1. Issue an `rk_live_...` key from the Recordwire dashboard - the same key the REST API uses, with the same state restrictions.
2. Claude Code one-liner - `claude mcp add registry --transport http https://api.recordwirehq.com/mcp --header "Authorization: Bearer rk_live_..."`
3. mcp.json for Cursor or any config-based client - `{"mcpServers": {"recordwire": {"url": "https://api.recordwirehq.com/mcp", "headers": {"Authorization": "Bearer rk_live_..."}}}}`
4. A key restricted to certain states returns 403 for the others, so an agent cannot silently answer outside its subscription.

## Verification (Sep 11, 2026 evening sweep)

Endpoint live-probed over JSON-RPC: keyless `tools/list` returned all 8 tools with schemas (search parameters, pagination cursors, event-type vocabulary) - the tool surface is open for discovery while calls require the bearer key. Vendor docs at recordwirehq.com/mcp confirm Streamable HTTP, one bearer key with no OAuth flow, and per-state coverage pages with counts, cadence and file dates.

## See Also

- [CN Evidence MCP - China Supplier Due Diligence for Agents](/hermes/mcp/servers/external/cn-evidence-mcp/)
- [Nexlab MCP - Cited Data Across 23 Sources for Agents](/hermes/mcp/servers/external/nexlab-mcp/)
- [GoodLeads MCP - New-Business Leads for Agent Outreach](/hermes/mcp/servers/external/goodleads-mcp/)
