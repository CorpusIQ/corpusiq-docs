---
title: "RushCRM MCP - The WhatsApp Pipeline an Assistant Can Enter"
description: "Brazilian WhatsApp CRM: 36 tools over OAuth with read, write and delete as separate scopes, per-tool admin switches, and MCP on every plan"
category: "Sales and CRM"
stars: "not applicable (hosted service)"
added: 2026-11-12
source: "the mcp.so feed card stamped 2026-11-12 17:38Z, the official registry record br.com.rushcrm/crm 1.0.0, both OAuth metadata documents fetched the same day, the vendor's README and plans page, and a live keyless probe of the published org endpoint at 18:05Z"
relevance: ★★★
tags: [crm, whatsapp, sales-pipeline, brazil, lead-management, messaging, oauth, mcp, remote]
last_updated: "2026-11-12"
---

# RushCRM MCP

**In a WhatsApp-first sales operation the pipeline lives on somebody's phone, and the report is whatever the seller remembers.** Which deals in the commercial funnel have not moved in seven days, which conversation ended with a promise nobody logged, which follow-up task was created but never done - the CRM holds the answer and the salesperson does not open it, because opening it means leaving the conversation. RushCRM is a Brazilian CRM built around WhatsApp, Instagram, calls and ads in one funnel, and its MCP server lets an assistant work the same records: contacts, deals, pipelines, tasks, notes, WhatsApp conversations and the automation builder, inside the chat where the work already happens.

```text
Server type:  remote Streamable HTTP, OAuth 2.1 with PKCE and dynamic registration
Endpoint:     https://rushcrm.com.br/api/v1/mcp/<account-slug>
Auth:         OAuth per user, or an API key (rk_live_...) in the Authorization header
Registry:     br.com.rushcrm/crm 1.0.0, remote declared with a {slug} template
Scopes:       leitura (read), escrita (write), exclusao (delete)
Access:       respects the permission profile of the user who authorised it
Probe:        keyless initialize answered 401 with protected-resource metadata
```

## The evidence tier

The published org endpoint - the listing prints one concrete account path, `.../mcp/org-3a92f0b952e94ab698ffd38cda85fa27`, while the registry declares the `{slug}` template, so every customer gets their own resource URL - answered **401** to a keyless `initialize` with `WWW-Authenticate: Bearer realm="RushCRM MCP", resource_metadata="https://rushcrm.com.br/.well-known/oauth-protected-resource/api/v1/mcp/org-3a92f0b952e94ab698ffd38cda85fa27"`. The endpoint also carried a **100 requests** rate-limit header with 99 remaining, and Cloudflare in front of it.

The protected-resource document answered **200** with one resource, one authorization server at `https://app.rushcrm.com.br`, and exactly **three** scopes in Portuguese: **`leitura`**, **`escrita`** and **`exclusao`**. That is the first thing worth noticing about this server, and it is covered below.

The authorization-server document answered with `authorization_endpoint` `/oauth/autorizar`, `token_endpoint` `/api/v1/oauth/token`, `registration_endpoint` `/api/v1/oauth/register`, `revocation_endpoint` `/api/v1/oauth/revoke`, `code` as the only response type, `authorization_code` plus `refresh_token`, **`S256`** only, `none` as the token and revocation auth method, and a `service_documentation` pointer into the CRM's own MCP settings page.

`br.com.rushcrm/crm` **1.0.0** answers in the official registry with the same remote template and the description *Brazilian WhatsApp CRM: contacts, deals, pipelines, WhatsApp messages and automations*.

**The honest limit:** no RushCRM account exists on this host, so the tool list below is the vendor's README read on 2026-11-12 rather than a measured `tools/list`, and the collection half of the server was not driven. The 401, the three scopes and both metadata documents are the measured parts.

## What the thirty-six tools cover

The vendor's README publishes the names, in Portuguese, grouped by area:

```text
Contacts            contato_list, contato_get, contato_create, contato_update, contato_delete
Deals and pipelines oportunidade_list, oportunidade_get, oportunidade_create,
                    oportunidade_update, funil_list, produto_list
Activity            tarefa_list, tarefa_create, tarefa_update, nota_list, nota_create,
                    reuniao_list
WhatsApp            conversa_list, mensagem_list, mensagem_send, mensagem_pronta_list
Tags and forms      etiqueta_list, etiqueta_aplicar, formulario_list, submissao_list
Team and targets    usuario_list, meta_list
Automations         automacao_guia, automacao_list, automacao_get, automacao_validar,
                    automacao_simular, automacao_create, automacao_update,
                    automacao_status, automacao_delete
```

Two things in that list are unusual for a CRM connector. The **automation** group includes `automacao_validar` and `automacao_simular` beside create and update, so an assistant can check and dry-run an automation before it goes live - the same plan-then-apply shape, one step earlier in the pipeline. And `mensagem_send` exists at all: most CRM connectors stop at reading, and this one lets an agent send the WhatsApp message, under the CRM's own rate protections.

## Two switches, and one of them is per tool

The operator controls here are set in the product rather than argued about in a prompt:

- **Per-tool switches.** The account administrator turns each tool on or off in Settings → API → MCP Server, so an assistant can be given the deals and denied the deletion without writing a policy.
- **Scope choice at authorisation.** When a client connects, the OAuth grant is **read, write or delete** - chosen by the person authorising, as separate scopes rather than one "full access" grant. `exclusao` being its own scope is the whole argument: an assistant asked to keep the pipeline tidy never needs it.
- **Per-user permissions.** Each connection respects the permission profile of the user who authorised it, so an SDR's assistant is not a manager's assistant.
- **A key path for clients without OAuth.** An API key (`rk_live_...`) created in Settings → API is accepted in the `Authorization` header; that key is not scope-limited by a consent screen, so it belongs to a service, never to a laptop.
- **Tokens expire and rotate.** Access tokens last **one hour** and the refresh token rotates on every use; connected apps are listed and disconnectable in Settings → MCP Server → Apps conectados.

## What it costs

Published BRL pricing from `rushcrm.com.br/planos`, read on 2026-11-12. The page was in a launch/Black Friday campaign when it was read (promotional annual pricing plus free implementation, marked as running to the end of November), so treat the promotional figures as dated and the list figures as the set:

```text
plan        users  WhatsApp  pipelines  automations  list price   API and MCP
Starter     4      4         5          20           R$ 208/mo    300/hour
Growth      15     15        20         60           R$ 348/mo    1,000/hour
Scale       -       -         -          -            R$ 698/mo    5,000/hour
Enterprise  100    -         -          -            from R$ 1,997/mo  5,000/hour
```

**API and MCP are a row in the plan comparison, included as a rate limit rather than sold as an add-on.** A Starter account can make 300 MCP calls an hour and an Enterprise account 5,000, which is a legitimate way to meter an agent surface - the assistant inherits the plan's throughput the same way a dashboard user does. It also means a heavy automation on the cheapest plan will meet a ceiling that has nothing to do with how much data the account holds.

## Where it sits

[WhatsApp Business Tools MCP](/hermes/mcp/servers/external/whatsapp-business-tools-mcp/) is Meta's own server for the WhatsApp Business Platform - numbers, templates, webhooks, sending - and it knows nothing about your pipeline. RushCRM is the opposite trade: the pipeline, the deals, the tasks and the message history are the objects, and the WhatsApp number is one channel inside them. On the CRM side, [Perfex CRM MCP](/hermes/mcp/servers/external/perfex-crm-mcp/) serves a self-hosted PHP CRM and [QoreNext CRM MCP](/hermes/mcp/servers/external/qorenext-crm-mcp/) is company-hierarchy intelligence rather than deal records. This is the first entry here where **deletion is a separate OAuth scope and every tool has an admin switch**.

### Can an assistant send WhatsApp messages through RushCRM?

Yes - `mensagem_send` is in the tool list, and the vendor states that sending passes through the CRM's own pacing protections so the number is not put at risk. The account administrator can switch that tool off for any connection.

### Is a full-access grant the only option?

No. Authorisation asks for `leitura`, `escrita` or `exclusao` separately, and `exclusao` is not implied by `escrita`. A read-only assistant never needs to be trusted with the other two.

### Does the assistant see more than the person using it?

No. Each connection respects the permission profile of the user who authorised it, and the connected apps list shows every connection with the ability to disconnect it immediately.
