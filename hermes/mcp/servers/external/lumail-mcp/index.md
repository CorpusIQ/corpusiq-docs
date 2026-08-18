---
title: "Lumail MCP - CorpusIQ Docs - CorpusIQ Docs"
description: Email marketing automation over MCP — read and manage subscribers, campaigns, workflow automation, tags, segments and analytics. Dual endpoints with a curated OAuth catalog and a full API-token catalog behind five-digit confirmation gates.
category: Marketing
stars: n/a (new listing)
added: 2026-08-16
source: mcpservers.org
relevance: ★★★
tags: [email-marketing, workflows, campaigns, subscribers, automation, confirmation-gates]
---

# Lumail MCP

**Email-marketing platform MCP (Streamable HTTP, dual endpoints)** — Lumail exposes its canonical email-marketing toolset to MCP clients: subscribers, campaigns, graph-based Workflows, tags, segments, settings, and analytics. The tool catalog is generated from the same definitions that drive Lumail's in-app agent, CLI, and SDK, so MCP tool discovery is the source of truth.

```
Server type: Hosted remote (Streamable HTTP)
Auth: Dual profile — Lumail OAuth (curated read + draft-write) or organization API token (full catalog)
Endpoints: https://lumail.io/mcp (OAuth) · https://lumail.io/api/mcp/sse (API token)
Tools: Workflows, campaigns, subscribers, segments, analytics, senders, deliverability
Pricing: Commercial — lumail.io
Category: Marketing
Built by: lumail.io
```

## Why This Matters for Operators

Lumail ships the most complete email-marketing MCP surface yet documented in this catalog. The dual-endpoint design is the standout: the OAuth endpoint cannot send, publish, schedule, delete, archive, or unsubscribe — it is a curated read-and-draft surface safe for any client — while the API-token endpoint unlocks the full organization catalog for trusted runtimes. Every high-impact action (sending, scheduling, publishing a Workflow, destructive deletion, unsubscribes) sits behind a two-call confirmation flow: the first call returns a five-digit code, and the agent must repeat the exact call with that code within five minutes.

That is the approval-gate pattern this catalog has watched spread across email, social, and content tools — now applied to an entire marketing automation platform.

## Tools & Capabilities

| Area | Tools |
|---|---|
| Workflows | `list_workflows`, `get_workflow`, `create_workflow`, `configure_workflow_draft`, `update_workflow_draft`, `publish_workflow`, `update_workflow_status`, `delete_workflow` |
| Enrollment | `add_subscriber_to_workflow`, `remove_subscriber_from_workflow` |
| Groups | `list_workflow_groups`, `get_workflow_group`, `create_workflow_group`, `update_workflow_group`, `set_workflow_group`, `delete_workflow_group` |
| Campaigns | Drafting, rendering (`render_campaign`), history, scheduling, analytics |
| Audience | Subscribers, composed filters, tags, custom fields, segments |
| Deliverability | Senders, domains, suppression management |
| Platform | Snippets, variables, images, imports, exports, transactional email |

Workflows are graph-based: a draft is configured as one complete `{ steps, edges }` object, and publishing or activating is always a separate, confirmation-gated step.

## Installation

```json
{
  "mcpServers": {
    "lumail": {
      "url": "https://lumail.io/api/mcp/sse",
      "headers": {
        "Authorization": "Bearer lum_your_api_token_here"
      }
    }
  }
}
```

Create the token at Settings → API Tokens. For a stdio-only client, bridge with `mcp-remote`. The same catalog is queryable over REST at `/api/v2/tools`.

## Business Relevance

- **Marketing operators** can delegate campaign drafting and rendering checks to an agent without handing it a send button
- **Lifecycle teams** get Workflow graph management in conversation, with every change drafted before it touches live sends
- **Compliance-minded orgs** get the two-call confirmation audit pattern on every destructive or billable action
- **Agencies** can scope a token per client organization and keep the human as the final approver

## Integration with CorpusIQ

Lumail is the marketing-execution complement to CorpusIQ's analytics layer: CorpusIQ reports campaign economics through GA4, Klaviyo, and Meta connectors, while Lumail runs the workflow engine itself. An operator could have CorpusIQ flag a cohort whose revenue dipped, then have a Lumail-connected agent draft the win-back Workflow — unpublished, rendered, and shown for review before a human confirms the activation code.

## Limitations

- OAuth endpoint is intentionally limited — full power requires managing an organization API token
- Confirmation codes are single-use and expire in five minutes, which breaks long-running unattended agent loops by design
- Commercial service; Lumail platform pricing applies outside the MCP surface
- New listing — the docs are excellent but the MCP surface has no community track record yet

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
