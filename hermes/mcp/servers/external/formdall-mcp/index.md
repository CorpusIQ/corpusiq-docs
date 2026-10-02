---
title: Formdall MCP - GDPR Form Backend for Agents
description: "German GDPR-by-design form backend for AI agents. The assistant creates forms, sets the field schema, wires email or webhook notifications, and gets back the finished embed snippet - no backend code, no cookies, encrypted storage with retention-based deletion, and a self-hosted proof-of-work captcha. Ten OAuth tools, 120 requests per minute, free to start."
category: Business Operations
stars: n/a (hosted platform)
added: 2026-09-07
source: mcpservers.org
relevance: ★★
tags: [forms, lead-capture, gdpr, dsgvo, webhooks, email-delivery, captcha, remote-mcp]
---

# Formdall MCP - GDPR Form Backend for Agents

**Remote MCP server (Streamable HTTP, OAuth)** - a German-hosted form backend (formdall.de) with DSGVO compliance as architecture rather than a checkbox. The assistant creates the form, defines the field schema, wires email or webhook notifications, and receives the finished embed snippet - the operator's static site just posts to Formdall, which validates, filters spam, encrypts and notifies.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth browser login with the operator's Formdall account (no API key needed); submissions:read is a separate consent scope
Endpoint: https://app.formdall.de/mcp
Tools: 10 (create_form, update_form_fields, create_action, get_embed, get_form, list_forms, list_actions, list_organizations, list_submissions, get_submission)
Pricing: Free to start, no credit card
Category: Business Operations
Built by: Formdall (formdall.de), hosting in Germany
```

## Why This Matters for Operators

Every contact form is a liability stack the operator did not ask for: a mail server whose reputation needs managing, a spam filter that needs weekly rule updates, captcha keys to rotate, and a deletion concept that a DSGVO inquiry can demand at any time. Formdall collapses that to one attribute on a form tag - the static page posts to `https://api.formdall.de/api/v1/f/<key>`, and everything else happens on Formdall's side.

**The privacy mechanics are the product**: submissions are encrypted at rest on German servers and physically deleted on their retention date, IP addresses are stored only as a daily rotating hash with server logs deleted after 14 days, the default captcha is a self-hosted proof-of-work widget with no cookies, no tracking and no US transfer - so no cookie banner is needed - and Article 15/17 requests are handled from the inbox with CSV export or deletion. Webhooks are HMAC-signed and SSRF-protected.

The MCP surface makes the agent the form builder: ten tools cover creating forms, updating field schemas, wiring actions (email, webhook, ntfy, Telegram, Slack, Discord) and fetching the HTML or AJAX embed snippet. `list_submissions` and `get_submission` only appear in the client's tool list when the operator explicitly consents to `submissions:read`.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `create_form` | Create a form with a field schema; returns the key and the ready embed snippet |
| `update_form_fields` | Add or change fields on an existing form, including required flags and captcha settings |
| `create_action` | Wire a notification: email, webhook, ntfy, Telegram, Slack or Discord, with per-action auth options |
| `get_embed` | The HTML snippet (with hidden anti-spam field and captcha when enabled) or the AJAX snippet |
| `get_form` / `list_forms` | Read one form or list all forms on the account |
| `list_actions` | List notification actions on a form |
| `list_organizations` | List workspaces so the assistant can decide where a new form belongs |
| `list_submissions` / `get_submission` | Read submissions (only present with explicit `submissions:read` consent) |

Rate limit: 120 MCP requests per minute per authenticated account, independent of the submission endpoint's limits.

## Installation

```bash
claude mcp add --transport http --scope user formdall https://app.formdall.de/mcp
```

A Formdall account (free, no credit card) is required. On the first tool call the client opens a browser window for OAuth login, where the operator confirms the permissions - including the optional `submissions:read` scope. `claude mcp login formdall` starts the sign-in immediately.

## Configuration

```json
{
  "mcpServers": {
    "formdall": {
      "type": "http",
      "url": "https://app.formdall.de/mcp"
    }
  }
}
```

Docs live at docs.formdall.de/mcp (German), covering the endpoint, the connect flow and the full tool reference.

## Business Relevance

- **EU operators with static sites** add lead capture without standing up a backend or a mail server.
- **Agencies** let an agent build and wire client forms in one conversation, with the GDPR burden handled by the platform.
- **Marketing teams** run form experiments by updating field schemas through the agent instead of asking a developer.
- **Data-protection officers** get Article 15/17 search, CSV export and deletion built into the inbox, not a project.

## Integration with CorpusIQ

Formdall feeds CorpusIQ's lead pipeline directly: a CorpusIQ agent creates the form and wires a webhook action, so every submission lands in the lead tracker with the HMAC signature verified before the lead is enriched and scored. The agent can update field schemas as campaigns evolve - adding a budget field or a consent checkbox - without a deploy. Because submissions are only readable with explicit `submissions:read` consent, the integration keeps the operator in control of what the agent may access, matching CorpusIQ's permission model. For operators running German sites, the combination gives lead capture, DSGVO compliance and agent-driven follow-up in one flow.

## Limitations

- German-language docs and German-centric compliance focus (DSGVO); the service itself is usable anywhere.
- OAuth connection requires an existing Formdall account.
- Submission read access is opt-in via the `submissions:read` consent scope.
- Hosted platform only - the form backend is the product, not a self-host build.
- Rate limit of 120 MCP requests per minute per account.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
