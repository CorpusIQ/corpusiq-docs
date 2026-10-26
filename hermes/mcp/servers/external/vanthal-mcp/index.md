---
title: "Vanthal MCP - LatAm SMB Sales, Stock and Cash"
description: "One server over a Latin American small business: counter sales, stock, cash register shifts, customer accounts and appointments, in Spanish."
category: Business Operations / Commerce
stars: n/a (hosted, OAuth or key)
added: 2026-10-24
source: "mcpservers.org /all p1-20 fresh cohort (late sweep, October 24 2026) + live endpoint probe, official registry entry and vendor documentation"
relevance: ★★★
tags: [latam, small-business, point-of-sale, cash-register, stock, appointments, customer-accounts, spanish, oauth, argentina]
last_updated: "2026-10-24"
---

# Vanthal MCP

**A small company's whole operating day behind one server, in Spanish.** Vanthal runs sales, cash, stock, customer accounts, appointments and team tasks for small and medium companies in Latin America, and its MCP server exposes those records with the owner choosing, at connect time, whether the assistant reads or also writes.

```
Server type: Remote (Streamable HTTP)
Endpoint: https://vanthal.com/api/mcp
Auth: OAuth 2.1 (Claude and ChatGPT custom connector) with the owner choosing consulta (read) or carga (read and write), or an assistant key starting vth_
Tools: 34 documented (24 read, 10 write)
Limit: 300 calls per day per key
Pricing: US 19, 49 or 99 per month by Lumi message volume, modules and users not counted
Registry: com.vanthal/vanthal 1.1.0, active since 2026-10-19
Built by: Vanthal (vanthal.com)
```

## Why This Matters for Operators

A counter business does not run on a database, it runs on a till, a stock room, a notebook of who owes what and a calendar. That is the layer agents have had no access to: every connector in this catalog talks to a cloud platform, and a Latin American shop, clinic or services company often runs on a local system of record with no developer API at all.

Vanthal is the first entry in this catalog whose unit of work is the trading day: what was sold, what is in the till at the end of the shift, what needs restocking, who owes money, who is coming in tomorrow, and which team tasks are overdue. Data and tool descriptions are in Spanish, which matters because the answer has to land in the language the operator actually uses.

## What It Actually Does

Live probe this sweep: `POST initialize` on `https://vanthal.com/api/mcp` returned HTTP 401 with the server saying, in Spanish, that the connection is not authorised and that Vanthal must be connected from the assistant or a key sent as a bearer credential. A real endpoint, gated as expected.

The published documentation lists 34 tools. The read side (24 tools) answers the recurring questions:

| Question | Tools |
|---|---|
| How did today go | `ver_negocio_hoy` (income, money owed to the business, products to restock, pending team tasks) |
| What sold | `ver_ventas` by period, product, payment method or seller |
| What is in the till | `ver_caja` for the current shift and its movements |
| What is in stock | `ver_variantes` for variant stock, `ver_gestion` for live records across modules |
| Who owes me | `cuenta_corriente` for customer accounts |
| Records | `listar_registros`, `buscar_registros`, `ver_registro` with history and comments |
| Calendar | `ver_turnos` for a day or range, free slots and a customer's history |
| Team | `ver_mi_dia`, `ver_tareas_asignadas`, `ver_objetivos`, `ver_equipo`, `quien_falta`, `ver_pulso_equipo` |
| Reporting | `ver_informe` for the weekly or monthly report |
| Shipping | `ver_envios`, `cotizar_envio` (quotes with the connected carrier, nothing booked) |
| Compliance | `estado_factura_electronica` for Argentina e-invoicing status, read only |
| Anything else | `preguntar_a_lumi`, which answers only with the tools the key allows |

The write side (10 tools) covers `registrar_venta` for a counter sale that decreases stock and adds the income to the till or the customer account, `guardar_registro`, `comentar_registro`, `crear_tarea`, `asignar_tarea`, `avisar_avance`, `agendar_turno`, `cambiar_turno`, `crear_evento` and `crear_nota`.

The boundary the vendor drew is unusually explicit for a small business system. A write key logs sales, appointments, tasks, notes and records, and records sales and deposits as income, but it never withdraws cash, records expenses, deletes, approves, charges a card or wallet, issues invoices, changes pipeline stages, or touches Finance, HR, Legal or Management records. Each key is capped at 300 calls a day on top of the company's own limits, every write appears in the owner's activity log with an undo button, and every connection can be revoked from the same screen it was created on.

## Installation

Two paths, both self-serve:

1. **OAuth.** Add `https://vanthal.com/api/mcp` as a custom connector in Claude or as an app in ChatGPT. The company owner signs in, picks read only or read and write, and approves. Nothing is copied.
2. **Key.** In the Asistentes conectados module, create a key with the scope you want; it is shown once. Send it as `Authorization: Bearer` against the same URL.

## Business Relevance

This is the retail and services counterpart to the cloud platform connectors. A shop, a salon, a clinic or a small distributor in Argentina, Mexico or Colombia can now ask its own till and stock room a question in the language it works in, with a scope the owner chose and a log that shows what the assistant did.

## Integration with CorpusIQ

Where a business runs on Vanthal, this is the system of record for revenue and stock, so a CorpusIQ answer about the week can draw on the same numbers the owner saw at closing rather than a re-entry. The `ver_avisos` alerts surface, which names prices behind inflation, overdue accounts and tax category limits, is the natural cross-check against a banking or payments connector.

## Limitations

- Latin America only, and Argentina-specific where it counts: the e-invoicing tool reads ARCA status and never issues an invoice.
- Spanish throughout. Tool names, descriptions and answers are in Spanish, so a client expecting English output will need that stated up front.
- 300 calls per day per key, which is low compared with cloud connectors and worth knowing before building a loop.
- No tool call was possible in this sweep, because every tool needs an owner-approved connection or key that only exists inside a customer account. The probe confirmed the endpoint answers and the tool surface comes from the vendor's documentation.
- Writes are limited by design: no expenses, no cash withdrawals, no card charges, no invoices issued, and no Finance, HR, Legal or Management records.
- The marketplace search covers companies inside the Vanthal Ecosystem, not the open market.

## FAQ

### Can the assistant take money or issue invoices?

No. A write key records sales and deposits as income, but it cannot charge a card or wallet, withdraw cash, record expenses, approve anything or issue an invoice. Argentina e-invoicing status is read only.

### Who controls what the assistant can do?

The company owner. At connect time the owner chooses read only or read and write, each key carries the permissions of the person who created it, and every connection is listed and revocable in the Asistentes conectados module.

### Is there a record of what the assistant changed?

Yes. Everything written through a key appears in the owner's activity log with an undo button.

### What does it cost?

US 19, 49 or 99 per month depending on how much you ask of Lumi, at 60, 250 or 400 messages a day. Modules and users are not counted, and there is a free trial.

## See Also

- [ProShip MCP - Thai Parcels and Shipping Labels](/hermes/mcp/servers/external/proship-mcp/)
- [Kirah Local Services MCP - Book a Real Local Business](/hermes/mcp/servers/external/kirah-local-services-mcp/)
- [ATLASS OS MCP - Trades Business With Real Books](/hermes/mcp/servers/external/atlass-os-mcp/)
