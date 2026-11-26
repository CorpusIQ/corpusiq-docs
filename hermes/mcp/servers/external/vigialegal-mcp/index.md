---
title: "Vigía Legal MCP - Mexican Supplier Credit Gate"
description: "SAT 69-B, article 69 and the REPSE padrón for a Mexican RFC, with three keyless tools beside two that spend a credit."
category: "Compliance"
stars: "0 (repository created 2026-11-26, vendor-hosted endpoint)"
added: 2026-11-26
source: "chatmcp submission queue, surfaced by the November 26 midday pass as the strongest unshipped arrival; official registry `mx.vigialegal/mcp` 1.0.0 published 2026-11-26T14:55:27Z (isLatest, active) with remote https://www.vigialegal.mx/mcp; repository https://github.com/Francis-builds/vigialegal-mcp created 2026-11-26T14:48:45Z, MIT, topics claude-code/compliance/mcp/mcp-server/mexico/repse/sat; driven on 2026-11-26 at the 11:00 MST tick with initialize, tools/list and six tools/call requests (fechas_icsoe_sisub, buscar_recursos for REPSE and ICSOE, leer_recurso on two slugs, consultar_rfc and consultar_rfcs), plus the gate probe on the apex host and a bogus Bearer"
relevance: "★★"
tags: [compliance, mexico, sat, 69-b, repse, supplier-risk, procurement, accounts-payable, credit-gated, streamable-http, spanish, keyless-tools]
last_updated: "2026-11-26"
---

# Vigía Legal MCP

**The most expensive supplier mistake in Mexico is not a bad price, it is a supplier that SAT has already listed for issuing simulated invoices, discovered three days after the payment run.** Vigía Legal answers that question for one RFC from the public lists: SAT article 69-B, SAT article 69, and the REPSE padrón of the STPS, each with the date of the version consulted. It is a small, new, Spanish-language, single-purpose server, and what makes it worth a guide is not its breadth but that three of its five tools answer with no credential at all, including a filing calendar an accounts-payable team needs every four months.

```
Server type:  Remote (Streamable HTTP), Vercel edge
Endpoint:     https://www.vigialegal.mx/mcp      the registry host, answers MCP
              https://vigialegal.mx/mcp          apex, serves HTML or 405, never MCP
Auth:         none on initialize, tools/list, fechas_icsoe_sisub,
              buscar_recursos, leer_recurso
              Bearer <llave> on consultar_rfc and consultar_rfcs, in band
Registry:     mx.vigialegal/mcp 1.0.0, published 2026-11-26T14:55:27Z
Instructions: "1 crédito por RFC con al menos una fuente consultada.
               No es una opinión fiscal."
Tools:        5, read from a keyless tools/list
Credits:      a free key carries 100 credits, 1 credit per RFC that returns
              at least one consulted source
```

`initialize` answers **200** at protocol **2025-06-18** as `vigia-legal` **1.0.0**, with `tools.listChanged` as its only capability and no `Mcp-Session-Id` in the response, so the transport is stateless and a client does not need to carry a session between calls. The `instructions` string is two sentences and both are load-bearing: the credit is charged **per RFC that reached at least one source**, so a miss is free, and the output is explicitly *"not a fiscal opinion"*.

## The five tools

| Tool | Arguments | Cost | What comes back |
| --- | --- | --- | --- |
| `consultar_rfc` | `rfc`, 12 or 13 characters | 1 credit | state of one RFC in SAT 69-B, article 69 and the REPSE padrón, with the date of each source |
| `consultar_rfcs` | `rfcs`, array of 1 to 10 | 1 credit per RFC that answers | the same, batched |
| `fechas_icsoe_sisub` | none | free | the next ICSOE (IMSS) and SISUB (INFONAVIT) filing window |
| `buscar_recursos` | `consulta`, 2 to 120 characters | free | guide titles and slugs from the vendor library |
| `leer_recurso` | `slug`, `^[a-z0-9-]+$` | free | the full text of one guide |

The RFC schema is strict on length and nothing else: 12 characters for a moral person and 13 for a physical one, with no pattern constraint, so format validation is the caller's job. Every tool returns a markdown `content` block and nothing else. There is no `structuredContent` on this surface, which means an agent that branches on structured output gets text and has to parse, and the paywall arrives through the same channel.

## What answers with no key, measured

Three of the five tools answered on a connection carrying no Authorization header at all, which contradicts the registry record on its face. The registry declares `Authorization` on the remote with `isRequired: true` and `isSecret: true`. The measurement: `initialize`, `tools/list`, `fechas_icsoe_sisub`, `buscar_recursos` and `leer_recurso` all answered **200** with correct payloads and no credential, while the two RFC tools answered **200** with `isError: true` and the text *"Para consultar necesita una llave gratuita con 100 créditos"*. So the gate is real, it is just not a transport gate.

`fechas_icsoe_sisub` returned, verbatim:

```text
Próxima presentación de ICSOE (IMSS) y SISUB (INFONAVIT): cuatrimestre 3 de 2026.
Ventana: del 2027-01-01 al 2027-01-17 (presentación en 2027).
El día 17 cae en domingo: al ser inhábil, el plazo se recorre al lunes 2027-01-18.
Confirme la fecha en el portal de cada autoridad antes de presentar.
```

The holiday arithmetic reproduces: **2027-01-17 is a Sunday** and **2027-01-18 is a Monday**. The tool states the quarter it is answering for, the window, the roll rule, and tells the client to confirm with each authority, which is the correct level of confidence for a date that carries a fine.

The free guide behind it agrees and cites the statutes: `calendario-sisub-icsoe` returns **9,303 characters**, maps each of the four windows from September 2026 to September 2027 to the quarter it reports (January reports September to December, May reports January to April, September reports May to August), names the aplicativo for each authority, and grounds the deadline in **article 15 A of the Ley del Seguro Social** and **article 29 Bis of the Ley del INFONAVIT**. The guide and the tool agree on the January date and on the roll to Monday, which is the cross-check worth doing before quoting either.

`buscar_recursos` is a real index rather than a stub. A query for `REPSE` returned **eight** guides with slugs, among them `que-es-repse` (the 2026 guide for the contracting company), `como-verificar-repse-proveedor`, `validar-proveedor-antes-del-pago`, `actas-de-servicio-por-periodo-real` and `portal-proveedores-no-es-validar`; a query for `ICSOE` returned **three**, including `documentos-cumplimiento-repse`, a checklist of folio, SISUB, ICSOE, IMSS, INFONAVIT and CFDI to collect before the purchase order and before payment.

`leer_recurso` on `como-verificar-repse-proveedor` returned **6,079 characters** with the single most useful distinction in the whole catalogue for this class, stated as a table: **vigencia REPSE** answers whether the STPS registry is valid for the provider to operate, and **al corriente** answers whether the provider is current with IMSS, INFONAVIT and SAT, and the two do not imply each other in either direction. A provider can hold a valid folio and a negative compliance opinion on the same day. An assistant that reports one as the other is wrong in the direction that costs money.

## The gate, and the two shapes it does not distinguish

`consultar_rfc` with a well-formed but non-existent RFC, `consultar_rfcs` with two of them, and `consultar_rfc` carrying `Authorization: Bearer bogus` all returned the **same** response: HTTP **200**, `isError: true`, and the identical sentence pointing at `https://www.vigialegal.mx/mcp` for a free key. Four defects follow from that measurement and they are worth recording because each one misleads an agent in a different way.

**A bad key and no key are indistinguishable.** An expired, revoked or mistyped `llave` produces the sentence that means *get a key*, so a caller who already has one is told to get one, and the operator goes looking for a credential problem that does not exist. An `invalid_token` or a differentiated message costs one branch to write and is what every other OAuth surface in this catalogue does.

**The paywall is in band, not at the transport.** There is no `401` and no `WWW-Authenticate` header anywhere on this server, and the discovery documents are absent: `/.well-known/oauth-protected-resource`, `/.well-known/oauth-authorization-server`, `/.well-known/mcp.json` and `/.well-known/ai-plugin.json` all answer **404** with the site's HTML error page. Every compliant MCP client is therefore unable to discover the credential path programmatically, and any client that maps `isError: true` to a tool failure rather than to an onboarding message will surface *"the tool failed"* to the user on first contact, which is the worst possible first impression of a paid surface.

**The registry overstates the gate.** `isRequired: true` on the remote reads as *this server needs a credential to function*. Three of its five tools, including one that carries a statutory deadline, work with no credential, and the two that do not are gated in band. A directory that renders the registry record will tell a prospective user to obtain a key before they discover that the calendar is free.

**The apex host does not speak MCP.** `https://vigialegal.mx/mcp` answers **405** with `Allow: POST, DELETE` when the request advertises `Accept: text/event-stream`, and **200** with the marketing page's HTML when it asks for `application/json` or `*/*`. Only `https://www.vigialegal.mx/mcp` answers JSON-RPC. The registry and the vendor's own copy both point at `www`, so the risk is bounded, but an operator who trims the `www` out of the URL by habit gets a Next.js page where a server should be, and the failure mode looks like a broken endpoint rather than a hostname.

One note that is not a defect but will cost an English-speaking operator time: the entire surface is `es-MX`. Tool names, argument names, the instructions block and every payload are Spanish, the guides are written for a Mexican comptroller rather than a US controller, and the legal citations are Mexican statutes. An agent can translate on the way out, but the vocabulary an assistant must match is `RFC`, `69-B`, `REPSE`, `SISUB`, `ICSOE` and `opinión de cumplimiento`.

## What it costs, and where the paid side goes

The entry point is a free key with **100 credits**, and a credit is spent per RFC that reaches at least one consulted source, so routine screening of a vendor list is priced in tens of credits rather than thousands. The vendor's commercial product behind the MCP is a supplier-compliance platform priced by the number of suppliers registered in the buyer's portal, in bands of **up to 100**, **101 to 500**, **501 to 5,000** and above 5,000 at custom, on an annual subscription with a one-time implementation fee and, stated plainly on the pricing page, **no SLA and no credits for downtime**. The number that frames the purchase is on their home page: a **5.87 million MXN** maximum REPSE fine **per non-compliant supplier**, which is the exposure the supplier gate exists to price.

## Add it to Hermes

```bash
hermes mcp add vigialegal --url https://www.vigialegal.mx/mcp
```

Add the Bearer header only when the RFC tools are needed:

```yaml
mcp_servers:
  vigialegal:
    url: https://www.vigialegal.mx/mcp
    headers:
      Authorization: "Bearer ${VIGIALEGAL_LLAVE}"
```

Request the key at `https://www.vigialegal.mx/mcp`. Check that the host carries `www` before blaming the server. Treat `isError: true` on `consultar_rfc` as *no credential or bad credential* and read the message before retrying, because the two are the same failure here.

## Why this one is in the catalogue

The vendor is small and the repository is hours old, so this is not a recommendation of the company. It is in the catalogue because the surface answers a question the operator audience actually pays to have answered, **is this supplier on a government list before we pay them**, and because three of its five tools answer without a key, which makes it a zero-cost first contact for an agent. The calendar tool alone is worth wiring: it is the same four-month deadline problem every Mexican contractor carries, it returns the window with the roll rule applied, and it costs nothing to ask.
