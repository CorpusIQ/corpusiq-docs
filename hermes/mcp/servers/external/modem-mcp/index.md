---
title: Modem MCP - Customer Feedback Intelligence for AI Agents
description: Modem connects AI assistants to customer feedback across Slack, support tickets, email, calls and issue trackers. Fourteen tools search feedback with natural language, run the Modem Agent against connected tools, and write topics, companies and people back to the workspace.
category: Business Operations
stars: n/a (new listing)
added: 2026-09-04
source: mcpservers.org
relevance: ★★★
tags: [customer-feedback, voice-of-customer, support-analytics, feedback-intelligence, oauth, streamable-http, remote-mcp]
---

# Modem MCP

**Remote MCP server (Streamable HTTP, OAuth)** - the external client surface of Modem, the customer-feedback intelligence platform. Fourteen tools search feedback across Slack, support, email, calls and issue trackers, run the full Modem Agent against connected tools like Linear and GitHub, and write topics, companies and people back to the workspace.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth with data:read and agent:invoke scopes
Endpoint: https://mcp.modem.dev/mcp
Tools: 14 (4 agent-run, 1 search, 9 workspace writes)
Pricing: Modem plans (agent runs consume credits, search_modem does not)
Category: Business Operations
Built by: Modem
```

## Why This Matters for Operators

Customer feedback is scattered across Slack threads, support tickets, emails and call notes, and the only people who read all of it are the people with no time to read all of it. Modem centralizes it, and the MCP server makes it queryable from any assistant. **An agent can answer "what are customers saying about the new pricing page this week" against real feedback rows, then write the resulting topic back with a priority and lifecycle state.**

The write surface is deliberately careful: all write tools require the agent:invoke scope, are marked destructive so most clients confirm each call, and act as the signed-in user under their existing role. If the account cannot make the change in the dashboard, the tool cannot either.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `modem_agent_invoke` | Start an agent conversation; returns conversation_id and run_id |
| `modem_agent_get_run` | Poll a run's status and, once complete, its answer |
| `modem_agent_send_message` | Send a follow-up turn in an existing conversation |
| `modem_agent_cancel_run` | Request cancellation of a running agent turn |
| `search_modem` | Natural-language question against your Modem data, returns matching rows |
| `update_topic` | Update priority, lifecycle state, issue type, keywords or archived status |
| `bulk_update_topics` | Update up to 100 topics at once |
| `merge_topics` | Merge up to 50 source topics into a target |
| `create_companies` / `update_companies` | Create or update up to 50 companies |
| `merge_companies` | Merge source companies into a target |
| `add_people_to_company` | Associate people with a company |
| `update_people` / `merge_people` | Update up to 50 people or merge duplicates |

## Installation

```bash
claude mcp add --transport http modem https://mcp.modem.dev/mcp
```

Then run `/mcp` inside Claude Code and complete the browser authorization. Cursor, VS Code and GitHub Copilot, Codex, opencode and ChatGPT developer mode are all documented by the vendor.

## Configuration

```json
{
  "mcpServers": {
    "modem": {
      "url": "https://mcp.modem.dev/mcp"
    }
  }
}
```

Auth notes: approve the data:read scope for search_modem and agent:invoke for agent runs plus workspace writes. No API key exists; the OAuth token resolves the organization, and rate limits are 20 calls per minute per organization per tool.

## Business Relevance

- **Product operators** query the real voice of the customer instead of a stale NPS dashboard.
- **Support leaders** merge duplicate topics and companies so feedback stops double-counting.
- **Research-heavy teams** run multi-step agent investigations that pull Linear, Slack and GitHub through connected tools.
- **Executive summaries** become one prompt: what changed in feedback this month, with priorities attached.

## Integration with CorpusIQ

Modem reads what customers say; CorpusIQ reads what they do. A churn investigation becomes: Modem searches feedback for the exit reasons and surfaces the top topics, while CorpusIQ pulls Stripe subscription cancellations, HubSpot ticket volume and Shopify order trends to correlate. The operator gets the qualitative and the quantitative in one conversation instead of two dashboards and a spreadsheet.

## Limitations

- Agent-run tools consume credits, so multi-step investigations have a per-run cost.
- Writes apply immediately with no undo; merges in particular are not reversible from the client.
- Rate limited to 20 calls per minute per organization per tool, with agent runs additionally capped by credit allowance.
- Tool access depends on the scopes approved at consent; read-only connections see search_modem only.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [BoldDesk MCP - Helpdesk Ticket Operations for AI Agents](/docs/hermes/mcp/servers/external/bolddesk-mcp)
- [Buska MCP - Social Listening and Buying Signals for AI Agents](/docs/hermes/mcp/servers/external/buska-mcp)
