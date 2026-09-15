---
title: "Relm MCP - API-First CRM for AI Agents"
description: "Official MCP server from Relm: 41 typed tools over contacts, companies, deals, pipelines, automations, sequences, templates and webhooks with OAuth 2.1 or bearer keys, sandboxed test mode, and errors that tell agents what to fix."
category: Sales
stars: "n/a (no public repo)"
added: 2026-08-30
source: mcpservers.org /all
relevance: ★★★
tags: [mcp-server, crm, sales, pipeline, automation, sequences, webhooks, oauth, remote-mcp, streamable-http]
---

# Relm MCP

**Official MCP server from Relm, an API-first CRM built for AI agents.** 41 typed tools cover contacts, companies, deals, activities, pipelines, automations, drip sequences, email templates and webhooks from a single Streamable HTTP endpoint at `api.relmcrm.com/mcp`. Everything an agent can do in the dashboard it can also do over the MCP server with the same bearer key - and the error contract is built for agents: every failure is an RFC-9457 problem+JSON response that carries `valid_options` and a `suggestion`, so the agent self-corrects instead of guessing.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (DCR + PKCE, rotating refresh tokens, scope "crm") or bearer key (relm_live_ / relm_test_)
Endpoint: https://api.relmcrm.com/mcp
Tools: 41 (verified via public tools/list, Aug 30, 2026)
serverInfo: relm v0.17.1 - "Relm CRM" (live-verified)
Pricing: Free 1,000 req/mo · Pro $29/mo (100k) · Scale $249/mo (2M), overage $0.0001/req, spend caps
A2A: https://api.relmcrm.com/a2a · OpenAPI: https://relmcrm.com/openapi.json
SDK: npm i relmcrm (zero-dependency TypeScript)
Built by: Relm (relmcrm.com)
```

```json
{
 "mcpServers": {
 "relm": {
 "type": "http",
 "url": "https://api.relmcrm.com/mcp",
 "headers": { "Authorization": "Bearer relm_live_..." }
 }
 }
}
```

## Why This Matters for Operators

Relm is one of the few CRM vendors whose MCP surface was designed for agents first and humans second. Three design decisions stand out.

First, **the "never confused" error contract.** Send an unknown contact type and you get back `422 unknown_value` with the exact list of valid options; send a stale update and you get `412 version_conflict` telling you to re-fetch and reapply. The server's own instructions tell the agent to call `relm_describe_schema` first - the live schema (objects, fields, enum groups) is the source of truth, and if a needed enum value or custom field doesn't exist, the agent creates it (`relm_create_enum_value`, `relm_create_field`, `relm_create_type`) rather than improvising.

Second, **test mode is a sandbox, not a storage tier.** `relm_test_` keys write to an isolated dataset that is free, invisible to billing and the dashboard, and auto-deleted 7 days after creation - an agent can rehearse a full pipeline-building sequence before a single `relm_live_` call touches production. OAuth grants always act on live data.

Third, **write safety is layered.** Creates take an `Idempotency-Key` (a retry returns the original record), updates use optimistic concurrency (`If-Match` against a per-record `version`), and webhooks are HMAC-signed (`Relm-Signature: t=...,v1=...`) with retry backoff (1m/5m/30m/2h/6h) and dead-lettering after six attempts. Spend is capped explicitly - `relm_set_spend_cap` - and quota headers (`X-RateLimit-*`, `X-Quota-*`) ride every response.

## Tool Groups (41 tools, all verified from the public tools/list)

- **Schema first:** `relm_describe_schema` (live objects, fields, enums), `relm_get_usage`, `relm_set_spend_cap`
- **Core CRUD:** `relm_create`, `relm_get`, `relm_list`, `relm_update`, `relm_delete`, `relm_restore`, `relm_search` (cross-entity search over contacts, companies, deals), `relm_batch` (multi-operation single round-trip), `relm_log_activity`
- **Pipelines:** `relm_create_pipeline`, `relm_get_pipeline`, `relm_list_pipelines`, `relm_manage_pipeline`, `relm_manage_stage`
- **Automations:** `relm_create_automation`, `relm_get_automation`, `relm_list_automations`, `relm_manage_automation`, `relm_automations_capabilities`
- **Sequences:** `relm_create_sequence`, `relm_get_sequence`, `relm_list_sequences`, `relm_manage_sequence`, `relm_enroll`, `relm_preview_sequence`
- **Templates:** `relm_create_template`, `relm_list_templates`
- **Webhooks & connections:** `relm_create_webhook`, `relm_get_webhook`, `relm_list_webhooks`, `relm_manage_webhook`, `relm_delete_webhook`, `relm_connect_channel`, `relm_list_connections`, `relm_delete_connection`
- **Schema extension:** `relm_create_enum_value`, `relm_create_field`, `relm_create_type`

## Verification (Aug 30, 2026)

Live probe against `https://api.relmcrm.com/mcp`: unauthenticated `initialize` returns `serverInfo: {"name": "relm", "title": "Relm CRM", "version": "0.17.1"}` with instructions to call `relm_describe_schema` first; unauthenticated `tools/list` returns the full 41-tool catalog (public discovery - `tools/call` requires a credential, returning 401 with OAuth metadata for a Connect flow).

## Notes and Caveats

- Keys are shown once and SHA-256 hashed at rest; `live` and `test` variants never cross data.
- List endpoints use cursor pagination (keyset over `created_at, id`, stable under writes; `limit` capped at 100).
- Webhook endpoints on live-mode keys must be public HTTPS; test-mode keys may point at localhost.
- Free tier: 2 automations / 1 sequence; hard-stops at quota (429) rather than silent overage.
