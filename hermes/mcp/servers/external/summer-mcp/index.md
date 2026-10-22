---
title: "Summer MCP - Support Cases Your Agent Can Work"
description: "A support operations server with 108 tools: read cases, request an investigation, prepare work for human approval, and publish help articles."
category: "Business Operations"
stars: n/a (hosted service, no public repo)
added: 2026-10-22
source: "mcpservers.org /all page 1 (summer-mcp, October 22, 2026 midday sweep)"
relevance: ★★
tags: [customer-support, helpdesk, cases, investigations, human-approval, knowledge-base, telehealth, remote-mcp, oauth]
---

# Summer MCP

**Most support tooling gives an assistant a ticket list. Summer gives it the whole operation and then makes it ask before anything reaches a customer: read the case, request an investigation, prepare the work, and stop.**

```
Server type: Remote (Streamable HTTP)
Endpoint: https://api.gosummer.ai/mcp
Auth: none for discovery; every tool call needs a Summer OAuth access token
Live check: unauthenticated POST initialize returned HTTP 200 (serverInfo summer 0.2.2, protocol 2025-03-26, tools, resources and prompts capabilities, with server instructions)
Protected resource metadata: https://api.gosummer.ai/.well-known/oauth-protected-resource returned HTTP 200 (resource https://api.gosummer.ai/v1, authorization server gosummer.ai, bearer in header)
Tools: 108 from tools/list
Scopes: setup, cases.read, investigations.request, actions.prepare, workspace.write, credentials.replace, messaging.activate, guides.publish, automation.manage
Built by: GoSummerAI (gosummer.ai)
```

## Why This Matters for Operators

The read-only half is not the interesting part. A support assistant that can search cases is a convenience. The part worth cataloguing is what happens on the write side: Summer exposes the writes, then wraps each one in a statement of what it will not do.

`summer_investigations_request` asks Summer to investigate a case or revise a saved plan, and its own contract says completion is not approval. `summer_actions_prepare` prepares the exact work in the current saved plan for a human to approve inside Summer, and does not approve or execute. `summer_guides_publish` publishes an article to the customer help center, but only the exact selected revisions, and it needs explicit publish rights. `summer_privacy_requests_create` files an export or deletion request for human review and cannot approve, perform or attest completion of the work.

That is the shape a business actually needs before it lets an agent touch customers: the agent can do the investigating, the drafting and the staging, and a person still holds the release. Almost every other support MCP catalogued so far stops at reading tickets.

## Tools & Capabilities

108 tools, in families rather than one long list:

| Family | What it covers |
|---|---|
| Cases | `summer_cases_list`, `summer_cases_search` (by name, email, phone, order, tracking number, vendor or Stripe ID), `summer_cases_get`, `summer_cases_attachment`, `summer_cases_customer_profile` |
| Investigations | `summer_investigations_list`, `summer_investigations_request`, `summer_actions_prepare`, `summer_runs_list` with approval state and execution receipts |
| Assignment | `summer_cases_assignment_read`, `summer_cases_assignment_update`, `summer_work_routing_read` / `_update` |
| Knowledge | `summer_knowledge_list`, `_get`, `_create`, `_edit`, `_history`; saved replies with revision history |
| Guides | `summer_guides_get`, `_save`, `_articles_get` / `_save`, `_preview`, `_publish`, `_unpublish`, `_history`, plus custom-domain hosting checks |
| Service reporting | `summer_reports_credits`, `_service_metrics`, `_delivery`, `_commitments` |
| Messenger | Conversations, installations, consented website leads, voice settings, support-email forwarding with DNS checks |
| Governance | Quality scenarios and assessments, capability checks with evidence, privacy requests, webhooks with signed delivery, service accounts, credentials listed by name only |

The credentials family is worth naming: `summer_credentials_list` returns names, sources and versions and never values, and the secret-bearing tools hand new keys to a trusted local helper rather than to the model.

## Installation

Claude, ChatGPT, Codex and Cursor can add the endpoint directly. Summer's own docs list `https://api.gosummer.ai/mcp` as the server URL and note that browser clients can use CORS with their own bearer token, static discovery is public, and tool calls require sign-in.

```json
{
  "mcpServers": {
    "summer": {
      "type": "http",
      "url": "https://api.gosummer.ai/mcp"
    }
  }
}
```

Start with `summer_account_me` and `summer_company_capabilities`, which is what the server's own instructions say. The second one reports what this connection can actually do and gives a reason for everything unavailable, which is a better first move than discovering a missing scope halfway through a case.

## Limits Worth Knowing

- The product is aimed at telehealth support. The tool surface is a general support operation, but the vendor's framing, examples and demo workflows are clinic-shaped, so a non-healthcare team should read what it does rather than what it is sold as.
- No published price list: the pricing page returns 404 and the path to a price is a demo booking. Budget for a sales conversation, not a self-serve tier.
- Every tool call needs OAuth, so nothing works from a bare connector until a person signs in and approves scopes. Nine scopes are advertised and a task that needs a scope the grant does not carry comes back as a permission request to approve in Summer.
- 108 tools is a lot of surface for an agent to hold at once. Expect to scope connections narrowly per role rather than connecting everything to one assistant.
- Version coupling is explicit: the live catalog is 0.2.2 and the server's own instructions ask for Summer CLI 0.2.0 or newer, so older clients get warning metadata in responses rather than silence.

## FAQ

### Can an agent act on a customer without a person approving?
The tool contracts say no for the paths that matter: investigations complete but do not approve, prepared actions wait for approval inside Summer, published articles need explicit publish rights on exact revisions, and privacy requests are filed for human review rather than executed. Whether a given company has granted those scopes is a separate question, answerable with `summer_company_capabilities`.

### Is this a ticket reader or a full helpdesk?
It is the operation: cases, assignment and routing, quality assessments, knowledge documents, customer-facing guides with hosting checks, service metrics, commitments, Intercom migration, webhooks and service accounts. The read-only half is the entry point, not the product.

### Why catalogue a telehealth product for general business operators?
Because the MCP surface is a support operation rather than a clinic tool, and because the approval pattern is the thing worth copying. The catalog's job is to show what a well-governed write surface looks like, and this is one of the few that states its refusals in the tool descriptions themselves.

## See Also

- [Runbook v1 - Governed MCP Workflow Contract](/hermes/mcp/runbook-v1)
- [Agents Handbook MCP - Tested Playbooks Before the Run](/hermes/mcp/servers/external/agents-handbook-mcp/)
