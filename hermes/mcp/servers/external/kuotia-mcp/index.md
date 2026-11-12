---
title: "Kuotia MCP - Spanish Autónomo Tax, Dated and Sourced"
description: "Keyless Spanish tax calendar and RETA maths, driven live: a checked filing deadline, a refused unverified date and a reproduced worked example"
category: "Finance / Accounting"
stars: "not applicable (hosted service)"
added: 2026-11-12
source: "the submission queue entry #7219, the official MCP registry record com.kuotia/kuotia 1.0.1, the vendor pages kuotia.com/mcp.md and kuotia.com/autonomos-espana/mcp/ read the same day, and a live session on this host: initialize, tools/list and eight tools/call requests against https://kuotia.com/mcp"
relevance: ★★★
tags: [tax, spain, autonomo, accounting, deadlines, finance, keyless, oauth, mcp, remote]
last_updated: "2026-11-12"
---

# Kuotia MCP

**A tax deadline is the one number a business owner cannot afford to have estimated, and it is the number every assistant is happy to guess.** "The 303 for the fourth quarter is due at the end of January" is close enough to feel right and wrong enough to cost a surcharge. Kuotia, an online gestoría for autónomos in Spain, publishes a keyless server that answers the calendar question with a date the AEAT has published, and answers the quarter it has not verified with a refusal instead of a guess.

```text
Server type:  remote Streamable HTTP, no session, keyless for the public tools
Endpoint:     https://kuotia.com/mcp
Server:       Kuotia 1.0.1 (serverInfo), protocol 2025-06-18 (also 2025-11-25 and 2025-03-26)
Capabilities: tools only (no resources, no prompts)
Tools:        9 measured, 4 public and 5 behind OAuth
Registry:     com.kuotia/kuotia 1.0.1, active, streamable-http remote
Probe:        initialize, tools/list and eight tools/call requests in one session
```

## What the server answered

`initialize` returned **200** with no credential and an instruction block that draws the boundary before a tool is called: the public tools answer tax questions for anyone, the connected tools let a Kuotia gestoría client read their own tax status, obligations and pending requests, and `gestoria_send_message` is the only change the connection can make. It files nothing, approves nothing, uploads nothing, and returns the portal link for documents, identity numbers and bank details.

`tools/list` returned nine tools. Four are public and read-only by annotation: `kuotia_get_tax_calendar`, `kuotia_estimate_reta`, `kuotia_estimate_net_income`, `kuotia_get_autonomo_guide`. Four are the client's own record behind `kuotia:gestoria:read`: `gestoria_get_tax_status`, `gestoria_get_obligations`, `gestoria_list_requests` and `kuotia_action_receipts`. One writes, and it is annotated honestly: `gestoria_send_message` carries `readOnlyHint: false` and `destructiveHint: true`, takes an `idempotency_key` as required input, and sends exactly the text the client approved. Each tool declares its own `securitySchemes`, which is how a client can tell without probing that a tool needs a connection.

## Driven: a checked date, a refused date and a reproduced example

Eight calls in one session. The first two are the argument for the whole entry.

`kuotia_get_tax_calendar` with `modelo: "303"` and `period: "2026-T3"` returned a filed quarter in full: `deadline: 2026-10-20`, `direct_debit_cutoff: 2026-10-15`, a source link to the AEAT's own calendar page, and three assumptions stated rather than assumed. A local holiday does not move the date, a deadline falling on a weekend moves to the next business day, and the direct-debit date is the last day to pay by account charge while informative modelos have no payment at all.

`kuotia_get_tax_calendar` with `modelo: "303"` and `period: "2026-T4"` returned `isError: true` and this body:

```json
{"statutory_window": "del 1 al 30 de enero del año siguiente",
 "sources": ["https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925#a71",
             "https://sede.agenciatributaria.gob.es/Sede/ayuda/calendario-contribuyente/calendario-contribuyente-2026.html"],
 "error": {"code": "not_verified",
           "message": "Kuotia aún no ha comprobado las fechas de este periodo con el calendario de la AEAT. Este es el plazo general; la fecha exacta la publica la AEAT."}}
```

Read that as an operator: the server had a legally correct general answer available and did not dress it up as the checked one. The quarter that has been verified comes back as a date; the quarter that has not comes back as the statutory window from the IVA law with a flag saying so. That is the difference between an assistant that answers and an assistant you can quote, and it is the behaviour this catalogue keeps arguing for.

`modelo: "100"` and `period: "2025"` returned `2026-06-30` with a `2026-06-25` direct-debit cutoff, so the annual income tax return and the quarterly returns come off the same verified table.

`kuotia_estimate_reta` with `year: 2026`, `annual_income: 30000` and `annual_expenses: 5000` returned tramo **5** of the general table, `base_minima: 1209.15` to `base_maxima: 2030.00`, `cuota_minima: 380.88` to `cuota_maxima: 639.45`, `tipo_cotizacion: 31.50`, the flat-rate `tarifa_plana_cuota: 88.56`, and seven assumptions including the one that matters most: the flat rate is shown, but whether the person qualifies for it is not checked.

`kuotia_estimate_net_income` with `year: 2026`, `annual_income: 30000`, `annual_expenses: 5000` and `region: "madrid"` returned `rendimiento_neto: 19407.97`, `cuota_anual: 4570.56`, `irpf_anual: 2775.29`, `tipo_medio_irpf: 9.25`, `neto_anual: 17654.15` and `neto_mensual: 1471.18`. **Those are the vendor's own published numbers for the same example, to the cent**: the page a reader lands on shows 4,570.56 in contributions, 2,775.29 in income tax and 17,654.15 net, which is what makes this a control rather than a demo. The same call at 48,000 and 6,000 returned tramo **8** with a 14.61 percent average rate and 2,462.66 a month, and the 30,000/5,000 `estimate_reta` call returned tramo **5**, matching the vendor's own worked quote.

Two argument-shape findings worth having before wiring a prompt. `period` is validated against `^20\d\d(-T[1-4])?$`, so the natural "4T" is rejected with `invalid_arguments` on the `period` field; the accepted form is `2026-T3`. `region` is an enum of lowercase ASCII keys, so "Madrid" fails with `invalid_arguments` on `region` while `madrid` works, and the nineteen values include `pais_vasco`, `navarra`, `canarias`, `ceuta` and `melilla`.

## The connected half, measured to the gate

There is no Kuotia account behind this probe, so the five connected tools were measured to their gate rather than driven, and the gate is unusually well built.

A call to `gestoria_get_tax_status` with no connection returned **HTTP 200** with `isError: true`, a Portuguese-and-Spanish message saying the account is not connected, and this in the response metadata:

```json
{"mcp/www_authenticate": ["Bearer resource_metadata=\"https://kuotia.com/.well-known/oauth-protected-resource\",
                          error=\"insufficient_scope\", scope=\"kuotia:gestoria:read\",
                          error_description=\"Conecta tu cuenta de Kuotia para usar tu gestoría desde aquí.\""]}
```

That is a deliberate choice with a practical consequence: a client that reads only the HTTP status sees success and shows the operator nothing, while a client that reads the in-band error knows exactly which scope it is missing and where the metadata lives. `https://kuotia.com/.well-known/oauth-protected-resource` names one authorization server (`https://kuotia.com`) and two scopes, `kuotia:gestoria:read` and `kuotia:gestoria:write`; the RFC 8414 document publishes authorization, token, registration and revocation endpoints, `authorization_code` plus `refresh_token`, `none` as the only client auth method, S256 only, and `client_id_metadata_document_supported: true`. The vendor's own auth page adds the split that matters for an approval-first posture: sending a message to the gestor through ChatGPT needs `kuotia:gestoria:write`, and nothing else is changed by the connection. The client can disconnect it from Mis datos > Conexiones, or from the Autónomos and Empresas connection page.

## What a small business owner actually asks it

The guide tool carries the operator questions with their basis marked `official` and a `reviewed` date rather than a marketing line. On the `alta` topic it returned three points: the alta in Hacienda is modelo 036 and the 037 was suppressed with effect from 3 February 2025, the RETA alta can be filed up to 60 days before the activity starts or on the same day, and the reduced quota is 80 euros a month plus MEI for twelve months with a 2026 figure of 88.56 euros (the MEI being 0.90 percent of the 950.98 minimum base, or 8.56 euros), extendable by twelve months when income sits below the minimum wage. Every point carries its BOE or Seguridad Social link and a review date of 2026-10-21.

On the `need_gestoria` topic it states the part most accounting content skips: no autónomo is obliged to have a gestoría, representation is voluntary, and the AEAT registry of apoderamientos can be consulted and revoked by the owner. That is the same principle the guide uses when it hands the portal link back instead of collecting an identity number.

## Where it sits

The Spanish tax slice is not empty here. [OpenAccountants MCP](/hermes/mcp/servers/external/openaccountants-mcp/) answers across 83 jurisdictions with passages that cite skills, [BeeL MCP](/hermes/mcp/servers/external/beel-mcp/) carries Spanish VeriFactu invoicing against AEAT, and contix was held at submission as class-covered because it returns Modelo 303 box sums and IRPF arithmetic. The deadline-calendar class also carries [Reg Monitoring MCP](/hermes/mcp/servers/external/regmonitoring-mcp/) across twenty jurisdictions, [frag.hugo MCP](/hermes/mcp/servers/external/frag-hugo-mcp/) with German GDPR duties on a calendar, and [Double AIgents DSAR MCP](/hermes/mcp/servers/external/double-aigents-dsar-mcp/) with the GDPR breach clock.

What none of them carry is the client side of an accounting engagement. Kuotia's four connected tools read the state of a real gestoría relationship (which periods are being prepared, ready or filed, what the gestor has asked for, whether a delivery arrived) and its one write is a message the client approves and can receipt-check afterwards. The catalogue holds bookkeeping surfaces such as [Mighty Accounting MCP](/hermes/mcp/servers/external/mighty-accounting-mcp/) and [Paidnice MCP](/hermes/mcp/servers/external/paidnice-mcp/), and none of them lets the owner ask their own accountant a question through the agent they are already talking to. That, plus the refusal behaviour on an unverified quarter, is why this one has a file.

## Limits worth stating

The knowledge is Spanish and the tool text is Spanish, so an assistant will answer in Spanish unless it is told otherwise. The tables were last revised on 2026-10-12 per the response itself. The estimator assumes a full year of activity on the simplified direct-estimation method for common-regime IRPF: it does not apply the 20 percent start-of-activity reduction, does not apply regional deductions, treats children at 50 percent, and says that the tramo can differ under the foral regimes of the Basque Country and Navarra and under modules. The flat rate is displayed without checking eligibility, and the Seguridad Social regularises the quota later against Hacienda's data.

And the honest gap: the connected half was measured to its gate and the protected-resource and authorization-server documents, not driven with a Kuotia account. Nothing above should be read as a claim about what a client's status page returns.

### How would an assistant know a tax date is verified rather than guessed?

Because the tool returns a different answer when it is not. A verified period comes back as a deadline with a `direct_debit_cutoff`, the AEAT source and its assumptions; an unverified one comes back with `isError: true`, the code `not_verified` and the statutory window from the law. An agent told to quote the source will show the difference, and a person can see which answer they are holding.

### Can an agent file a Spanish tax return through this server?

No. The server states it files nothing, approves nothing, deletes nothing and uploads nothing, and the only write it exposes is a text message to the client's gestor after the client confirms the exact text. Modelos, payments and identity documents are handed back as portal links.
