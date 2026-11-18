---
title: "AR Tools MCP - CUIT, CBU and Payroll for Argentina"
description: "Argentine identity and payroll tools for agents: CUIT and CBU validation, phone normalisation, gross to net, aguinaldo and monotributo."
category: "Business Operations / Regional Data"
stars: "0 (hosted Streamable HTTP at https://ar-tools-api-103907796853.us-east1.run.app/mcp, keyless handshake, thirteen tools, eight driven with a free trial key)"
added: 2026-11-18
source: "the mcp.so submission queue entry 7555 filed 2026-11-18T05:27:26Z, the registry record io.github.TorlettiJoaquin/ar-tools, and a probe session on 2026-11-18 that minted a trial key and drove eight of the thirteen tools"
relevance: ★★★
tags: [argentina, payroll, cuit, cbu, monotributo, aguinaldo, compliance, hr, remote, mcp]
last_updated: "2026-11-18"
---

# AR Tools MCP

**Before an agent can touch an Argentine customer record it has to answer three questions that a language model gets wrong quietly: is this CUIT real, is this CBU real, and what does a 1,500,000 peso gross salary actually pay out.** AR Tools answers all three from statute and from the registers rather than from a model's memory of what a percentage usually is.

It is the second of three APIs from the same author, sharing one trial key and one credit balance with [Índices AR](/hermes/mcp/servers/external/indices-ar-mcp/), which serves the index series and the adjustment arithmetic.

```text
Server type:   remote Streamable HTTP (hosted)
Endpoint:      https://ar-tools-api-103907796853.us-east1.run.app/mcp
Server info:   ar-tools 0.1.0, protocol 2025-06-18
Registry:      io.github.TorlettiJoaquin/ar-tools, latest 0.3.0 (2026-11-18T03:42:41Z)
Auth:          a trial key from POST /v1/keys, no registration, 50 credits
Tools:         13 listed, 8 driven in this pass
Language:      Spanish tool names, descriptions and results
```

## The evidence tier

Keyless discovery, keyed calls, and one credential across the suite. `initialize` and `tools/list` answered without a credential and returned all **thirteen** tools with their schemas. A call without a key returns a JSON-RPC error that names the trial-key route by URL, the same shape as its sibling. `POST /v1/keys` with an empty body issued a **50**-credit key with no registration.

Eight tools were driven. Five were not, and this guide says which rather than implying a complete surface: `escala_comercio` (the Comercio CCT 130/75 salary scale), `calcular_vacaciones`, `liquidacion_final`, `ejecutar` (JavaScript sandbox) and `comprar_creditos` (checkout).

## The tool surface

| Tool | What it returns | Cost |
|---|---|---|
| `validar_cuit` | CUIT or CUIL validity from the check digit, plus person type and canonical format | 0 |
| `validar_cbu` | CBU or CVU validity from both check digits, plus bank or wallet, branch and account | 0 |
| `normalizar_telefono_ar` | A phone in any Argentine notation to E.164, WhatsApp and national form, with mobile or landline | 0 |
| `cotizacion_dolar` | Live buy and sell for all seven dollar houses, each with its own update stamp | 0 |
| `sueldo_neto` | Gross to net with the three statutory deductions and the current ANSES taxable ceiling | 0 |
| `calcular_aguinaldo` | The half-year bonus: gross, deductions, net and the payment deadline | 0 |
| `categoria_monotributo` | The A to K category from annual revenue, with the monthly total and the next category's limits | 0 |
| `escala_comercio` | Commerce-sector salary scale by category, period and seniority | 0 |
| `calcular_vacaciones` | Vacation days by seniority or proportional | 0 |
| `liquidacion_final` | Final settlement: days worked, proportional bonus, unused vacation, notice | 0 |
| `consultar_saldo` | Balance, last ten movements and the per-tool cost table | 0 |
| `ejecutar` | JavaScript sandbox with the authenticated `api` object | varies |
| `comprar_creditos` | Credit packs and a checkout URL | 0 |

In this pass every data tool answered at **0 credits**, so the trial key covered the entire evaluation. The cost table lives in `consultar_saldo` and is the thing to read before a production loop.

## The validators, with the arithmetic shown

**CUIT and CUIL are the same eleven-digit identifier** for a person or a company, and the last digit is a checksum, not data. The tool validated a canonical example and returned the decomposition:

```text
validar_cuit  20-12345678-6
  valido true, cuit 20123456786, formateado 20-12345678-6
  tipo persona_fisica, prefijo 20
```

That answer is reproducible by hand. Weight the first ten digits by 5, 4, 3, 2, 7, 6, 5, 4, 3, 2: 2x5 + 0x4 + 1x3 + 2x2 + 3x7 + 4x6 + 5x5 + 6x4 + 7x3 + 8x2 equals 148. 148 mod 11 is 5, and 11 minus 5 is 6, which is the digit printed. A model asked to "check this CUIT" without the weight table will agree with whatever looks plausible.

**A CBU is a bank account number with two check digits and a bank code inside it:**

```text
validar_cbu  0170099220000067797370
  valido true, tipo CBU
  entidad 017 BBVA Argentina, sucursal 0099, cuenta 2000006779737
```

The useful part is not the boolean. It is that `017` resolves to a named bank, so a payment record can be checked against the bank the customer said they used rather than trusted.

**Phone numbers are the third quiet failure**, because Argentine mobiles carry a `9` after the country code that landlines do not:

```text
normalizar_telefono_ar  "011 15 3456-7890"
  e164 +549****7890
  internacional +54 9 11 3456 7890
  nacional 011 15-3456-7890
  whatsapp 5491134567890
  tipo celular, pais AR
```

One input, four destination formats, and the mobile marker preserved. For any agent that sends a WhatsApp message or writes a `tel:` link, this removes the most common silent failure in the market.

## Payroll, which is where the percentages live

`sueldo_neto` computes employer-side deductions from the current statute, including the taxable ceiling that changes with an ANSES resolution rather than with the calendar:

```text
sueldo_neto  bruto 1,500,000
  neto 1,245,000
  aportes: jubilación 165,000 + ley 19.032 45,000 + obra social 45,000
  total deductions 255,000 (17 %)
  ceiling 4,861,685.38 for 2026-11, Resolución ANSES 304/2026
```

The arithmetic reconciles: 11 percent for retirement, 3 for the PAMI levy and 3 for the health fund is 17 percent, and 17 percent of 1,500,000 is 255,000. Two honest limits come with it: income tax is not included, and a collective agreement can add deductions the general regime does not know about.

`calcular_aguinaldo` is the half-year bonus, and it does the proration that most spreadsheet templates skip:

```text
calcular_aguinaldo  mejor_sueldo 1,500,000, 2026, semester 2
  period 2026-07-01 to 2026-12-31, 184 days, proportional false
  SAC gross 750,000, deductions 82,500 + 22,500 + 22,500 = 127,500
  SAC net 622,500, payment deadline 2026-12-18
```

Fifty percent of the best monthly salary is 750,000, the same three rates apply to the bonus, and the deadline is a date rather than a rule to interpret.

`categoria_monotributo` is the one that answers a question a small operator actually asks in January:

```text
categoria_monotributo  annual revenue 18,000,000, servicios
  category C, as of 2026-08-01
  monthly total 66,020.12 = impuesto integrado 18,246.86
                          + SIPA 22,078.71
                          + obra social 25,694.55
  revenue ceiling 24,670,494.31, margin left 6,670,494.31
  next category D at 30,628,651.43, whose monthly total is 84,612.93
```

Three components sum to the stated total to the cent, and the margin to the next category is given as an amount, which is the number an operator makes a decision with. It also flags that the activity type is one of the determinants and that the surface-area test is waived in towns under 40,000 people.

## The live dollar board

`cotizacion_dolar` returned all seven houses in one call, each with its own update stamp:

```text
oficial        1525.00 / 1575.00    updated 2026-11-17T18:00Z
blue           1585.00 / 1605.00    updated 2026-11-17T20:57Z
bolsa (MEP)    1591.50 / 1603.30    updated 2026-11-17T20:57Z
contado con liq 1694.20 / 1697.20   updated 2026-11-17T20:57Z
mayorista      1543.00 / 1552.00    updated 2026-11-17T16:23Z
cripto         1687.92 / 1694.83    updated 2026-11-17T20:57Z
tarjeta        1982.50 / 2047.50    updated 2026-11-17T18:00Z
```

Seven legally distinct exchange rates in one currency is the reality of operating there, and the per-house `actualizado` stamp is what makes the answer usable: a quote last refreshed eight hours ago is a different fact from one refreshed eight minutes ago.

## Why this earns a page

The catalogue already carries [Japanese payroll](/hermes/mcp/servers/external/jp-payroll-mcp/) and [German HR](/hermes/mcp/servers/external/lintelly-hr-deutschland-mcp/), both of which established that a country's statutory arithmetic is a legitimate MCP product because a model cannot hold it reliably. This is the first Argentine entry, and it is the pair to Índices AR: that server owns the index layer, this one owns the identity and labour layer.

It earns three stars because it was driven, every figure reconciles by hand, and the ceiling and the source resolution are dated rather than asserted. It is not four because five tools went undriven here, the outputs are Spanish-only (an English-language agent needs a translation step for every result), and the two argument-type mismatches found on the sibling API are the same author and the same framework.

## Installation

```json
{
  "mcpServers": {
    "ar-tools": {
      "url": "https://ar-tools-api-103907796853.us-east1.run.app/mcp",
      "headers": {
        "Authorization": "Bearer ${INDICES_AR_KEY}"
      }
    }
  }
}
```

Use the key from either API's `POST /v1/keys`. One balance covers ar-tools, indices-ar and direcciones-ar, so a deployment that needs payroll and rent adjustment configures one secret.

## Configuration

- Set the key as one environment variable shared by all three endpoints. A second key means a second balance and a second checkout URL for no benefit.
- Check the `periodo` field on payroll answers. The ceiling in `sueldo_neto` is dated `2026-11`; a stored ceiling from an older month is a wrong answer that looks right.
- Treat tool results as Spanish text. `tipo: persona_fisica` and `obra_social` are the vocabulary the rest of the pipeline has to accept, not translate on the way in.

## Limitations

- Argentina only, and the labour tools assume the general regime. Collective agreements, provincial taxes and income tax are explicitly out of scope in the tool's own notes.
- Validation is checksum and register-based, not a live taxpayer-status lookup: `validar_cuit` proves the number is well formed, not that the company is active or that it is the right company.
- Five tools were not driven in this pass, so their return shapes are recorded from the listing rather than from a call.
- The live endpoint reports version **0.1.0** while the registry carries **0.3.0** published 2026-11-18T03:42:41Z, the same stale-string pattern as its sibling.

## FAQ

### Does AR Tools MCP need a credit card?

No. `POST /v1/keys` returns fifty credits with an empty JSON body and no registration, and every data tool in this pass answered at zero credits, so a full evaluation fits inside the trial.

### Can it be trusted on payroll percentages?

On the general regime the arithmetic reconciles to the cent: 17 percent of gross for the three statutory deductions, 50 percent of the best salary for the half-year bonus, and a ceiling dated to the ANSES resolution in force for the month. It does not model income tax or collective agreements, and it says so.

### What is the CUIT check actually doing?

The weighted sum of the first ten digits with the 5-4-3-2-7-6-5-4-3-2 pattern, modulo 11, complemented to eleven. The example in this guide reproduces the digit by hand, which is the test to run before trusting any validator.

## See Also

- [Índices AR MCP - Argentine Indexes an Agent Can Adjust](/hermes/mcp/servers/external/indices-ar-mcp/)
- [jp-payroll-mcp - Japanese Payroll and Social Insurance](/hermes/mcp/servers/external/jp-payroll-mcp/)
- [lintelly-hr-deutschland-mcp - German HR Rules in Chat](/hermes/mcp/servers/external/lintelly-hr-deutschland-mcp/)
- [Cobra MCP - Ecuador SRI Invoices From Chat](/hermes/mcp/servers/external/cobra-mcp/)
