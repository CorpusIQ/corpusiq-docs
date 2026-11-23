---
title: "Avanciq MCP - VAT Rates and Invoice Checks With Receipts"
description: "Six tools that check a VAT rate on a date, a tax code in force and an invoice sum, returning the official source, the read date and a receipt id."
category: "Finance"
stars: n/a (vendor-hosted)
added: 2026-11-23
source: "mcp.so feed card stamped 2026-11-23 09:53 (UTC) for slug avanciq; keyless initialize, tools/list and six tools/call requests on 2026-11-23"
relevance: ★★★★★
tags: [vat, tax, e-invoicing, en16931, calculations, receipts, remote-mcp]
last_updated: "2026-11-23"
---

# Avanciq MCP

**Remote MCP server (Streamable HTTP, no authentication)** - six tools that answer tax and arithmetic questions with the source attached. A VAT rate comes with the tax-authority feed it was read from and the date of the read. An invoice total comes back as a verdict on a claimed number, with the corrected figure and the receipt id for the check.

```
Server type: Remote (Streamable HTTP, no auth)
Endpoint:    https://api.avanciq.com/connect/mcp
Server:      avanciq 0.1.1, protocol 2025-06-18
Tools:       6 (coverage, vat_rate, code_check, einvoice_check, einvoice_rule, verify_calculation)
Metering:    coverage and einvoice_rule free; vat_rate, code_check and verify_calculation 1 call; einvoice_check 2 calls
```

## Why This Matters for Operators

Two numbers that should agree rarely announce that they disagree. A purchase order, an invoice and a payment run each carry a total derived by a different person in a different tool, and the difference usually hides in a rounding rule or a tax rate that changed on a date nobody looked up. This server does three narrow things well: it looks up a rate as of a date, it checks whether an official code was in force on that date, and it recomputes an arithmetic claim in decimal and says whether the claim is right.

What makes it usable rather than merely interesting is that every answer carries its own provenance. A rate arrives with `source`, `source_read`, `last_rechecked` and a `receipt_id`. A calculation arrives with the assumptions it used, the rules version, and a `receipt_id`. That is the shape a finance team needs before it forwards an answer to an accountant, a customer or an auditor.

## Measured Behaviour

Six calls were driven on 2026-11-23, all keyless, every response carrying a UTC or a dated stamp.

### A VAT rate with the date it was read

`vat_rate(country="DE", date="2026-11-23")` returned:

```json
{"status":"ok","jurisdiction":"DE","tax":"VAT","date":"2026-11-23",
 "standard_rate":19.0,"reduced_rates":[7.0],"valid_from":"2021-01-01","valid_to":null,
 "source":"https://ec.europa.eu/taxation_customs/tedb/ws/ (VatRetrievalService, retrieveVatRates from 2019-01-01 to 2026-11-12)",
 "source_read":"2026-11-12","last_rechecked":"2026-11-17",
 "receipt_id":"rcp_36367ae2c54a4bed83b6"}
```

The rate is not the interesting part. The dates are: the source was read on **2026-11-12**, rechecked on **2026-11-17**, and `valid_from` says the 19 percent rate has held since **2021-01-01**. An agent quoting a VAT rate to a customer can now quote the read date in the same sentence.

### An invoice total that was nine cents wrong

`verify_calculation` with kind `gst_vat_invoice`, three units at 33.33 and a 20 percent rate, claimed total **119.90**:

```json
{"verdict":"incorrect","kind":"gst_vat_invoice",
 "result":{"lines":[{"net":99.99,"tax":20,"gross":119.99}],"subtotal":99.99,"tax":20,"total":119.99},
 "differences":[{"field":"total","claimed":119.9,"correct":119.99,"difference":-0.09}],
 "rules_as_of":"2026-11-18","receipt_id":"chk_ed9853bd3e58c9508908"}
```

Reproduced by hand: 3 x 33.33 = **99.99**, 20 percent of that is **19.998**, half-up to the cent gives **20.00**, so the total is **119.99** and the claim was **9 cents** short. The response also states the three assumptions it used, including the one that matters most: *"Tax rate per line as given by you (the tool does not decide which rate applies)."*

### A loan that reproduced to the cent

`verify_calculation` with kind `loan_interest`, principal **250,000**, rate **4.49 percent**, **365** days, claimed interest **11,225**:

```json
{"verdict":"correct","kind":"loan_interest","result":{"interest":11225,"total":261225},
 "main_field":"interest",
 "assumptions":["Simple interest: principal x rate x days / day count, rounded half up to the cent."],
 "rules_as_of":"2026-11-18","receipt_id":"chk_ffa8c9f4c195992069fa"}
```

250,000 x 4.49 percent = **11,225.00** exactly, so the tool agrees with the hand calculation and with the claim. Nine kinds are offered in total: depreciation, fx_with_fees, gst_vat_invoice, inventory_fifo_avg, invoice_or_claim_total, loan_amortisation, loan_interest, payroll_overtime and trade_quote.

### The free floor, and what it publishes about itself

`coverage` costs nothing and returns the whole map. Its `cost` field reads: *"coverage + einvoice_rule free; vat_rate, code_check (per code), verify_calculation = 1 call; einvoice_check = 2 calls."* So an agent can read the catalogue before it spends anything, which is the correct order.

The same response names **71** jurisdiction codes served and **30** not covered. Served is the EU states plus GB, CH, NO, IN, JP, SG, NZ, AE, Canada with its 13 province and territory codes, and **22** US states. Not covered is AU, SA and the other **28** US states, with the note *"US = state-level rate only. Canada: use country CA + region (e.g. QC)."*

### Official rule text on demand

`einvoice_rule(rule_id="BR-CO-15")` returned the rule as published:

```json
{"rule":"BR-CO-15","found":true,"flag":"fatal",
 "text":"[BR-CO-15]-Invoice total amount with VAT (BT-112) = Invoice total amount without VAT (BT-109) + Invoice total VAT amount (BT-110).",
 "fix":"Correct the amounts so that: ... (fields BT-109, BT-110, BT-112)",
 "in":["en16931-ubl","en16931-cii"]}
```

That is the exact validation artefact text, not a paraphrase, which is what makes it quotable in a dispute.

## What It Does Not Do

- **It does not decide the rate.** `verify_calculation` takes the rate you give it. Asking the tool to check the rate is a separate step: add `country` and `tax_date` to the input.
- **The code tables are three countries.** `code_check` covers Brazil (6 tables, NCM and CFOP among them, updated 2026-09-02 and 2026-09-04), Mexico (18 tables, most updated 2026-11-20) and Poland.
- **The e-invoice syntaxes are two.** `einvoice_check` reports `en16931-ubl` and `en16931-cii` at validation artefacts **v1.3.17**, with `peppol-bis3` and `xrechnung` listed as *coming*.
- **Metering binds without a key.** The calls answered here without an API key, but the tool descriptions price each one in calls, so a client should read `coverage` first and treat the allowance as finite.

## Measured Ergonomics

Two failure paths were driven, and both were answered usefully rather than silently:

- A wrong parameter name returned `{"error":"missing_input","message":"'rule_id' is required.","next_step":"Call again with rule_id = an EN 16931 rule id like BR-CO-15 or BR-S-08."}`
- An unknown tool name returned `Unknown tool: fetch_tools_coverage. Tools: coverage, vat_rate, code_check, einvoice_check, einvoice_rule, verify_calculation`, naming the whole set instead of failing anonymously.

### Can an agent use this without an account?

Yes for reading. `coverage` and `einvoice_rule` are free and answered keyless, and the metered tools answered here too. A production client should confirm its own allowance before looping over a batch of invoices.

### What happens when a claimed number is right?

It says so, without noise: `verdict` is `correct`, `differences` is empty, and the receipt id is still issued. A clean pass is a receipt, not a silent success.

### Does a tax rate answer tell you if it changed recently?

Only if you read the dates. `valid_from` gives the start of the current rate, `source_read` gives when the authority feed was last read, and `last_rechecked` gives when the server last verified it. There is no "changed on" field, so a rate that moved five years ago and one that moved last month look identical until you read `valid_from`.

## See Also

- [Finance and accounting data sources in the external catalogue](/hermes/mcp/servers/external/)
- [Sweep report for November 23, 2026 (night)](/hermes/mcp/sweeps/sweep-november23-2026-night)
