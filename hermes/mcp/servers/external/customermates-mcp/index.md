---
title: "Customermates MCP - Open-Source CRM for Agents"
description: "Read and write a Customermates CRM from Claude, ChatGPT or Cursor over one MCP endpoint, with per-workspace URLs, a 40-tool surface and an AGPL core you can self-host."
category: CRM / Open Source
stars: n/a (open source AGPL-3.0 core, hosted or self-hosted)
added: 2026-10-26
source: "live MCP probe on customermates.com/api/v1/mcp (401 unauthorized without credentials, RFC 9728 protected-resource document read live with jwks_uri) + vendor protocol reference customermates.com/en/docs/mcp (tool names, toolsets, permission model) + official MCP registry entry io.github.benjiwagner/customermates + chatmcp/mcpso submission #6185"
relevance: ★★★
tags: [crm, deals, pipeline, contacts, open-source, self-hosted, oauth, knowledge-base]
last_updated: "2026-10-26"
---

# Customermates MCP

**A CRM whose MCP endpoint is the same permission layer the humans use, on a codebase you can run yourself, answers the objection that keeps most CRMs out of an agent.**

```
Server type: Remote (Streamable HTTP) or self-hosted
Endpoint:    <BASE_URL>/api/v1/mcp  and  <BASE_URL>/api/v1/mcp/w/<WORKSPACE_ID>
Transport:   JSON-RPC 2.0 over POST, JSON or SSE responses
Auth:        OAuth sign-in (custom connector) or a 64-character x-api-key
Tools:       records, workspace and messaging toolsets, names read from the vendor reference
Built by:    Customermates (customermates.com), core AGPL-3.0
Registry:    io.github.benjiwagner/customermates
```

## Why This Matters for Operators

A small client-facing team does not need another dashboard. It needs the follow-up to happen: the deal that should have moved, the contact nobody wrote back to, the task that fell off a list. That work is text-shaped and belongs in the assistant the team already has open.

The blocker is trusts. Most CRM connectors an agent can reach are either read-only exports or they ask for a token that outranks the person using it. What matters here is that the MCP endpoint is gated by the same role permissions as the CRM itself, that every operation runs inside exactly one workspace, and that the core can be self-hosted under AGPL so the data never leaves the building.

## What It Actually Does

`initialize` without credentials returned HTTP 401 `{"error":"unauthorized"}`. The discovery document answers without an account:

- `/.well-known/oauth-protected-resource` returned HTTP 200 with `resource: https://customermates.com/api/v1/mcp`, its own authorization server, `jwks_uri: https://customermates.com/api/auth/mcp/jwks`, scopes `openid`, `profile`, `email`, `offline_access`, and `resource_signing_alg_values_supported: ["RS256"]`.

Two credential paths, from the vendor reference:

- **OAuth for client apps.** A custom connector in Claude (web, desktop, mobile) or ChatGPT: paste the URL, sign in, approve, no key to manage.
- **API key for CLI and editor clients.** A 64-character key in the `x-api-key` header for Claude Code, Codex, Cursor or raw HTTP. A key carries the permissions of the user who created it and there is no per-key scoping.

The endpoint tells an agent what went wrong instead of hiding it. A request missing `Accept: application/json, text/event-stream` gets HTTP 406. No credential, or a wrong, truncated, expired or deleted one, gets HTTP 401 with a `WWW-Authenticate` header pointing at the protected-resource document so the client can authorize again. A credential from another workspace gets 403 `workspace_mismatch`; a valid token whose user lacks `Read access All` on the API and Webhooks row gets 403 `insufficient_permissions` before any tool runs.

The tool surface, read from the vendor's protocol reference:

| Group | Tools |
|---|---|
| Orientation | `get_workspace_context` (user, company, roles, connected accounts and Knowledge Base in one call), `discover_record_types`, `resolve_record_identifiers`, `get_record_model`, `configure_record_model` |
| Read records | `query_crm_records`, `search_crm_records`, `read_crm_record`, `query_crm_measure`, `get_activities`, `manage_data_views`, `manage_record_detail_layout`, `manage_record_files` |
| Write records | `mutate_crm_record`, `import_crm_records`, `export_crm_records`, `preview_crm_deletion`, `read_crm_operation`, `cancel_crm_operation`, `resume_crm_operation` |
| Messaging | `get_messaging_threads`, `update_messaging_thread`, `send_chat_message`, `send_email`, `save_message_draft`, `discard_message_draft`, `move_email_thread`, `manage_connected_accounts`, `connect_messaging_account`, `list_deliveries`, `resend_delivery` |
| Calendar | `get_calendars`, `manage_calendar` |
| Knowledge | `manage_wiki_pages`, `get_docs_page`, `search_docs` |
| People and admin | `list_users`, `invite_link`, `update_member`, `remove_member`, `manage_roles`, `manage_team`, `update_my_profile`, `manage_trash`, `read_trash`, `manage_widgets`, `manage_webhooks`, `manage_routines`, `run_now` |
| Sales and social | `linkedin_search_sales_leads`, `linkedin_search_sales_companies`, `linkedin_manage_sales_lists`, `get_social_profile`, `get_social_posts`, `get_social_post_engagement`, `manage_social_relations` |
| Utilities | `lookup_address`, `check_address`, `create_upload`, `request_support` |

The endpoint can be narrowed with `?toolsets=`, for example `/api/v1/mcp?toolsets=records,messaging`, so a client only sees the groups it needs. Each workspace also has its own URL, `/api/v1/mcp/w/<WORKSPACE_ID>`, which accepts only credentials of that workspace, and an OAuth token from a different workspace is rejected with `invalid_token` and a `resource_metadata` pointer to that workspace's discovery document.

The server sends workflow instructions to a connecting client: read the schema first, resolve ids before writing, change records and relations through `mutate_crm_record`, and get confirmation naming the exact records or recipients before deleting or sending. The vendor is explicit that this guidance is not a server-enforced confirmation gate, and that whether a client passes it to the model depends on the client.

## Limitations Recorded

- No tool call was executed: every path needs an account, so tool names come from the vendor's protocol reference rather than a live `tools/list`.
- **No per-key scoping.** A key carries its creator's permissions in full. The narrow instrument is the toolset parameter, not the credential.
- **The confirmation contract is advisory.** The delete and send gates live in prompts and client behaviour, so an operator granting write and messaging access should check how their client handles approvals first.
- **Plan-dependent tools.** Messaging, calendar and social tools need a cloud plan at Pro or higher; the CRM, workspace and Knowledge Base surface is available on every plan and on self-hosted instances. A cloud workspace awaiting its first plan gets 403 `plan_required`.
- The Knowledge Base is shared surface: the same pages serve people in the CRM and connected MCP clients, so a page written for staff is readable by an agent with the permissions to see it.
- The vendor documents a stale-save refusal on concurrent page edits, which is the right behaviour and also means an agent's write can be rejected rather than merged.

## FAQ

### Does an agent need an API key, or can it use sign-in?
Either. Claude (web, desktop, mobile) and ChatGPT use the OAuth custom-connector path; CLI and editor clients use the API key path. Both act inside exactly one workspace.

### Can two workspaces share one connection?
No. A workspace URL accepts only its own credentials, and a mismatched token is rejected with an explanatory error rather than silently writing to the wrong place.

### Why is the self-hosted core worth knowing about?
Because the AGPL core can be run with Docker Compose, which removes the vendor from the data path entirely while keeping the same MCP endpoint. For a client-facing team with confidentiality clauses, that is the difference between usable and not.

## See Also

- [AXL MCP - courses, CRM and checkout in one agent surface](/hermes/mcp/servers/external/axl-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ CRM connectors](/hermes/mcp/)
