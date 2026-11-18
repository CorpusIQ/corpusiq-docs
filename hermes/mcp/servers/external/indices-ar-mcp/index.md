---
title: "Índices AR MCP - Argentine Indexes an Agent Can Adjust"
description: "Argentine indexes (UVA, CER, ICL, IPC) plus rent, fixed-term, judicial-interest and tax-deadline calculators over one remote endpoint."
category: "Finance / Regional Data"
stars: "0 (hosted Streamable HTTP at https://indices-ar-api-103907796853.us-east1.run.app/mcp, keyless handshake, twelve tools driven with a free trial key)"
added: 2026-11-18
source: "the mcp.so submission queue entry 7556 filed 2026-11-18T05:27:27Z, the registry record io.github.TorlettiJoaquin/indices-ar, and a probe session on 2026-11-18 that minted a trial key and drove ten of the twelve tools"
relevance: ★★★
tags: [argentina, inflation, uva, cer, icl, rent, payroll, bcra, indec, remote, mcp]
last_updated: "2026-11-18"
---

# Índices AR MCP

**An Argentine contract that adjusts for inflation is not a number. It is a formula that needs an index level on a specific date, and the level lives in a central bank series that a model cannot remember correctly.** Índices AR serves those levels and does the adjustment arithmetic on top of them: rent schedules under ICL or IPC, UVA conversions, fixed-term yields against measured inflation, judicial interest under the current statute, and the ARCA filing calendar for a given CUIT ending.

The distinction that matters is between a server that *looks up* a number and one that *computes from* it. This one does both, and it shows the factor it used.

```text
Server type:   remote Streamable HTTP (hosted)
Endpoint:      https://indices-ar-api-103907796853.us-east1.run.app/mcp
Server info:   indices-ar 0.1.0, protocol 2025-06-18
Registry:      io.github.TorlettiJoaquin/indices-ar, latest 0.3.0 (2026-11-18T03:42:41Z)
Auth:          a trial key from POST /v1/keys, no registration, 50 credits
Sources cited: BCRA, INDEC, argentinadatos.com, dolarapi.com, one per response
Tools:         12 listed, 10 driven in this pass
```

## The evidence tier

Keyless at the handshake, keyed at the call.

`initialize` answered **200** with no credential and `tools/list` returned all **twelve** tools with their schemas. A `tools/call` with no key answered a JSON-RPC error rather than a silent empty result:

```text
Esta tool requiere autorización. Conseguí una key de prueba con
POST .../v1/keys (sin registro) y mandala como "Authorization: Bearer ***"
```

That route exists and works. `POST /v1/keys` with an empty JSON body returned a key, fifty credits, and a checkout URL in one response, with no email and no account. The same key and the same balance cover the author's three APIs (AR Tools, Índices AR and Direcciones AR), which is the right shape for a suite: one credential, one ledger, three surfaces.

Ten of the twelve tools were driven with that key, and two were left alone on purpose: `ejecutar` runs JavaScript in a sandbox with the same authenticated API object, and `comprar_creditos` opens a checkout page. Neither is needed to measure the product.

## The tool surface

| Tool | What it returns | Cost |
|---|---|---|
| `indice_valor` | One index level on a date: `uva`, `cer`, `icl`, `ipc_mensual`, `ipc_interanual` | 0 |
| `ajustar_monto` | An amount restated between two dates, with the factor and the percentage change | 2 |
| `actualizar_alquiler` | A full rent schedule: period by period amounts, factor, and the next adjustment date | 3 |
| `convertir_uva` | Pesos to UVA or UVA to pesos at a date's UVA level | 0 |
| `dolar_historico` | Buy and sell for one dollar house on a past date (seven houses) | 0 |
| `dias_habiles` | Business days between two dates, with the holidays named, or N business days added | 0 |
| `plazo_fijo` | Fixed-term yield: interest, total, TEM, TEA, and whether it beats measured inflation | 1 |
| `intereses_judiciales` | Interest under Ley 27.802 art. 55 with the ceiling and floor computed | 2 |
| `calendario_fiscal` | ARCA due dates for a CUIT ending: IVA, monotributo, F.931, autónomos, Ganancias | 0 |
| `consultar_saldo` | Balance, the last ten movements with the API that caused each, and the cost table | 0 |
| `ejecutar` | JavaScript in a sandbox with an authenticated `api` object | varies |
| `comprar_creditos` | Credit packs and a checkout URL | 0 |

Every response carries a `fuente` field naming the source, and a `credits` object with `cost` and `balance`, so a calling model can see what a question cost it.

## What the numbers look like, and the arithmetic

The pass opened three index levels, each answering with the date of the datum rather than the date asked for:

```text
icl          2026-11-01  37.21     fuente BCRA
uva          2026-11-17  2200.38   fuente BCRA
ipc_mensual  dato 2026-10-31  2.2 %  (asked on 2026-11-18)
```

Then the adjustment path, which is where a model normally invents a plausible percentage:

```text
ajustar_monto  500,000 ARS  2026-05-01 -> 2026-11-01  index icl
               factor 1.158108   result 579,053.84   +15.81 %
               levels: 2026-05-01 = 32.13, 2026-11-01 = 37.21
```

**The factor is reproducible by hand.** 37.21 divided by 32.13 is 1.158108, and 500,000 times that is 579,053.84. The server publishes both levels it divided, so the check takes one line of arithmetic rather than trust.

The rent schedule compounds the same way, and compounds the *unrounded* factors rather than the rounded ones it prints:

```text
actualizar_alquiler  500,000 from 2026-01-01, icl, every 3 months
  2026-01-01 to 2026-03-31   500,000.00   (no factor)
  2026-04-01 to 2026-06-30   531,133.04   factor 1.062266   +6.23 %
  2026-07-01 to 2026-09-30   582,511.06   factor 1.096733   +9.67 %
  2026-10-01 to 2026-12-31   621,640.01   factor 1.067173   +6.72 %
  total change +24.33 %, next adjustment 2027-01-01
```

Multiplying the three printed factors gives 24.32 percent; the stated total is 24.33, which is the tell that the server kept full precision internally and rounded only for display. That is the correct direction to round in, and it is worth knowing before someone wires the printed factors into a spreadsheet and inherits a one-basis-point drift.

Two converters, one of which is the reverse of the other:

```text
convertir_uva  1,000,000 ARS at the 2026-11-17 UVA of 2200.38 -> 454.467 UVA
```

1,000,000 divided by 2,200.38 is 454.4671, so the answer is exact to the printed precision.

## The two tools that carry statute, not just series

`plazo_fijo` and `intereses_judiciales` are the reason this is a finance page rather than a data page.

```text
plazo_fijo  1,000,000 ARS, 30 days, no tna supplied
  TNA 24 % from the best of 33 banks reporting (Banco BICA), TEM 1.97, TEA 26.83
  interest 19,726.03, total 1,019,726.03
  against IPC 2.2 % for the term: real return -0.22 %, "le_gana" false
```

The interest is simple interest on a 365-day basis: 1,000,000 times 0.24 times 30 over 365 is 19,726.03 to the cent. The server chose the best rate of the day rather than a default, said which bank it came from, counted the banks, and compared the outcome with the most recent measured inflation instead of assuming a peso return is a real one. Its own notes are honest about the two limits: the rates are what each bank reports to the BCRA for that term and amount and home banking may differ, and the comparison assumes one inflation rate holds for the whole term.

`intereses_judiciales` is the more interesting one, because Argentine judicial interest changed shape recently and the old habit of applying a plain rate is now wrong:

```text
capital 1,000,000, 2026-01-01 -> 2026-11-01, tasa pasiva Ley 27.802 art. 55 a)
  accumulated rate 21.0883 %   total 1,210,883.02   interest 210,883.02
  series 1198: 80,629.9143 (2025-12-31) -> 97,654.4823 (2026-11-01)
  ceiling 1,258,847.25 (IPC factor 1.22816, 304 days, plus 3 % a year)
  floor   843,427.66 (67 % of the adjusted capital)   applied: tasa_pasiva
```

The accumulated rate is the ratio of the two published series values, 97,654.4823 divided by 80,629.9143, which is 1.21113. It reports which rule it applied, gives the ceiling and the floor as amounts rather than as a prose rule, and names the thing most likely to bite a lawyer using it: the IPC is published with a one-month lag, so months without a datum do not adjust the ceiling yet, and some courts use CER for the ceiling instead of IPC. The tool takes an `indice_tope` argument for that, which is the right way to handle a split jurisdiction.

## The calendar tool, and a schema mismatch

`calendario_fiscal` returns real ARCA dates for a CUIT ending, with the obligation, the period and the endings the date applies to:

```text
terminacion_cuit 3, 2026-11-01 to 2026-12-31
  2026-11-05  autónomos (2026-10)       endings 0, 1, 2, 3
  2026-11-11  F.931 employers (2026-10) endings 0, 1, 2, 3
  2026-11-16  Ganancias PH annual return (2025-12)  all
  2026-11-19  IVA return and payment (2026-10)      endings 2, 3
  2026-11-20  Monotributo monthly payment (2026-11) all
  2026-12-09  autónomos (2026-11) and F.931 (2026-11)
  2026-12-10  household employees
```

**The defect is in the argument type, not the data.** The first call sent `"terminacion_cuit": "3"` as a string and was refused with `expected number, received string`, while the tool description presents the argument as a CUIT ending with no type hint. A model that reads language and writes JSON strings will hit this on the first try. The same shape appears one level up: `indice_valor` accepts `uva|cer|icl|ipc_mensual|ipc_interanual` in lowercase, and the natural uppercase `ICL` that matches the description's own wording is rejected.

## Why this earns a page

Argentina is one of the few markets where an operator cannot answer a routine business question without a lagged statistical series: what this lease costs next quarter, what this debt is worth today, what the pesos in a fixed term actually earned. Existing entries here cover Japanese payroll, German HR, Ecuadorian invoices and French tax, and this is the first server on the list whose whole product is the Argentine index layer itself.

It earns three stars rather than two because it was driven, the arithmetic reconciles by hand, and every answer names its source. It is not four because the two argument-type mismatches are the kind of thing that turns a first integration into a support thread, and because the credit ledger, while visible, is a per-call cost model an operator has to read before pointing an agent at it in a loop.

## Installation

Add the remote endpoint. The handshake needs no credential; the calls do.

```json
{
  "mcpServers": {
    "indices-ar": {
      "url": "https://indices-ar-api-103907796853.us-east1.run.app/mcp",
      "headers": {
        "Authorization": "Bearer ${INDICES_AR_KEY}"
      }
    }
  }
}
```

Get the key once, with no account:

```bash
curl -s -X POST https://indices-ar-api-103907796853.us-east1.run.app/v1/keys \
  -H 'Content-Type: application/json' -d '{}'
```

The response contains `key` (shown once), `credits: 50`, and a `checkout_url`. The key works on all three APIs of the suite, so the same value can be reused for AR Tools and Direcciones AR rather than minting three balances.

## Configuration

- Read the cost table from `consultar_saldo` before wiring a loop. Index reads and business-day counts are **0 credits**, an adjustment is **2**, a rent schedule is **3**, a fixed term is **1**. A monthly rent review for one contract costs three calls and five credits.
- Budget for the trial: **50 credits** covers a full evaluation of the suite and then stops. The ledger keeps the last ten movements with the API that caused each, which is the cheapest instrumentation this catalogue has seen on a credit-based server.
- Check `fecha_dato` rather than the date you asked for. `ipc_mensual` answered a question asked on 2026-11-18 with the datum dated **2026-10-31**, which is correct behaviour and the only way a caller can tell a lag from a bug.

## Limitations

- Coverage is Argentina only: one country, one currency, one calendar. It is not a general macro data server.
- The index series and the dollar quotes come from public sources (BCRA, INDEC, argentinadatos.com, dolarapi.com), so the server is only as fresh as they are; it reports the datum date instead of pretending otherwise.
- The judicial-interest tool encodes one statute that is contested. Its notes say plainly that some courts have struck down art. 55 and others, including the Supreme Court, have applied it, so it produces a calculation and not a legal opinion.
- `ejecutar` runs arbitrary JavaScript with the authenticated API object. That is powerful and it is also a surface to reason about before enabling it in an unattended agent.
- The live server reports itself as version **0.1.0** while the registry carries **0.3.0** published 2026-11-18T03:42:41Z. The tool list is the authority; the version string is stale.

## FAQ

### Does Índices AR MCP need an API key?

For discovery, no: `initialize` and `tools/list` answered without one. For data, yes: a tool call without a key returns an authorisation error that names the `POST /v1/keys` route, and that route issues a 50-credit trial key with no registration.

### Can it compute a rent schedule under ICL?

Yes. `actualizar_alquiler` takes the start amount, the start date, the index, the cadence in months and a consultation date, and returns every period with its amount, factor and percentage change, plus the next adjustment date and a note to check the contract's own clause.

### Is the arithmetic verifiable?

Yes, and that is the point. `ajustar_monto` publishes both index levels so the factor can be divided by hand, `plazo_fijo` uses simple interest on a 365-day basis that reproduces to the cent, and `intereses_judiciales` exposes the BCRA series values it divided.

### What does it cost after the trial?

Credit packs sold through a checkout page, with a published per-tool cost table in `consultar_saldo`. Index reads and business-day counts are free; adjustments cost two or three credits.

## See Also

- [AR Tools MCP - CUIT, CBU and Payroll for Argentina](/hermes/mcp/servers/external/ar-tools-mcp/)
- [jp-payroll-mcp - Japanese Payroll and Social Insurance](/hermes/mcp/servers/external/jp-payroll-mcp/)
- [lintelly-hr-deutschland-mcp - German HR Rules in Chat](/hermes/mcp/servers/external/lintelly-hr-deutschland-mcp/)
- [Cobra MCP - Ecuador SRI Invoices From Chat](/hermes/mcp/servers/external/cobra-mcp/)
