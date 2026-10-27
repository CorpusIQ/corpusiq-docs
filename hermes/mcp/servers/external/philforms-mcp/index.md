---
title: "PhilForms MCP - Philippine Forms Filled into Sealed PDFs"
description: "MCP server for the PhilForms API: search 1,342 BIR, SSS, PhilHealth, Pag-IBIG and GSIS forms, fill values into their printed boxes, verify the PDF."
category: Compliance
stars: 0
added: 2026-10-19
source: "mcpservers.org /all page 1 (philforms/philforms-mcp)"
relevance: ★★
tags: [philippines, bir, government-forms, payroll, compliance, pdf, tax-forms, tamper-evident, mit-client]
last_updated: "2026-10-24"
---

# PhilForms MCP

**The long tail of Philippine government paperwork as five tool calls: find the form, read its fill contract, check the values, fill it so every digit lands in its printed box, then verify the finished PDF has not changed.** It covers 1,342 forms across BIR, SSS, PhilHealth, Pag-IBIG, GSIS, COA, CSC and GPPB - the certificates, returns and remittance forms a Philippine employer or supplier files every month.

```
Server type: Local (stdio) - `npx -y github:philforms/philforms-mcp`
Transport to PhilForms: HTTPS API at https://philforms.com (OpenAPI 3.1, api version 1.0.0)
Auth: PhilForms API key in `PDFPHILE_API_KEY` - `pk_test_...` is free and watermarked
Output: PDF written to `PDFPHILE_OUT_DIR` (default ./pdfphile-out) + document id
Requires: Node 18+, no dependencies
License: MIT for this client; the PhilForms service itself is proprietary
Publisher: philforms.com (github.com/philforms/philforms-mcp, created October 17, 2026)
```

## Why This Matters for Operators

Filling a government form is not a text task, it is a layout task. A TIN is not a string, it is a fixed number of cells on a specific line of a specific revision of a specific form, and every field has to land in the box that the agency prints. The failure mode of "let the model write the PDF" is a form that looks right, prints wrong, and gets rejected weeks later - after the deadline.

This server is built the other way around. Each of the 1,342 forms has a published fill contract: parameter names, labels, types, formats and allowed choices. Values are checked before filling and shown as they would print. A value the form cannot hold is refused with the reason instead of being silently coerced. The filled PDF comes back with a tamper-evident document id, and `verify_pdf` proves the file has not been altered since.

## What You Can Do Today

| Tool | What it does |
|---|---|
| `search_forms` | Search the catalogue in plain words ("2307", "philhealth claim") and get form ids |
| `get_form_parameters` | Read one form's fill contract: every parameter, label, type, format and choice list |
| `check_form_values` | Validate values before filling, each rendered as it would print |
| `fill_form` | Produce the filled PDF, saved to disk with a tamper-evident document id |
| `verify_pdf` | Check that a filled PDF is byte-identical to what was issued |

Behind the five tools sits a wider documented API - form pages, dossier and ingestion endpoints, extraction, a verification ledger, key rotation and account and plan endpoints - so a workflow can grow past single forms without changing vendors.

## What It Is Not

PhilForms fills and prints; **you file**. It is not affiliated with BIR, SSS, PhilHealth, Pag-IBIG, GSIS, COA, CSC or GPPB, and it does not submit anything to an agency. Treat the output as a correctly prepared document, not as a filed return.

## Setup

1. Create an API key at `philforms.com/account`. The `pk_test_...` key is free and watermarks its output; it exists to prove the workflow before anyone pays.
2. Register the server:

```json
{
  "mcpServers": {
    "philforms": {
      "command": "npx",
      "args": ["-y", "github:philforms/philforms-mcp"],
      "env": { "PDFPHILE_API_KEY": "pk_test_..." }
    }
  }
}
```

Claude Desktop users can instead open the `philforms-mcp-1.0.0.mcpb` release artifact, which prompts for the key. Set `PDFPHILE_OUT_DIR` if filled PDFs should land somewhere other than `./pdfphile-out`.

## Pricing, in the Vendor's Terms

The published schedule is in PHP, and the free tier is a real tier rather than a trial countdown:

- **Free (watermarked):** the first form of each pack comes out clean, plus 5 clean BIR 2307s a quarter and 5 clean 2316s a year; preview, check and verify are always free; a 30-day Pro trial is available.
- **Test fills:** 500 test fills on a test key.
- **Credits:** a fill costs 1, check/preview/verify cost 0, a revise costs 0 (same form, within 7 days, at most 5 edits), a scan page costs 3 and an ingest costs 10.
- **Form packs:** one form 79 PHP, five forms 299 PHP, both valid for 12 months.

At the time of this sweep the plans endpoint reported `is_checkout_available: false`, so treat the price list as the schedule and confirm the purchase path before promising a customer a cost. The API itself is live: `https://philforms.com/api/v1/openapi.json` returns 200 with API version 1.0.0 and the 1,342-form claim is stated in the API description.

## Integration with CorpusIQ

The part that breaks a forms workflow is the data, not the PDF. Three numbers have to agree before a 2307 is worth printing: the supplier's registered name and TIN, the amount withheld, and the period. Those live in accounting, commerce and payroll systems, which is exactly what CorpusIQ's read-only connectors reach - with citations, so a filled certificate can be traced back to the invoice it came from. The pattern is: pull the source figures with source citations, run them through `check_form_values`, fill, verify, then file.

## Limitations

- **Philippines only.** Other jurisdictions have equivalent local tools, not this one.
- **Vendor service, open client.** The five tools are a thin MIT client; the mapping and rendering are the proprietary service, and an account is required for anything beyond the free allowance.
- **Fills and prints, does not file.** No agency submission, no payment, no acknowledgement tracking.
- **Revisions change.** Forms are versioned by the agencies; the mapping is served per form id, so a stale local template is not a failure mode - but a form id that is not in the catalogue is a real one to plan for.
- **Young listing.** Repository created October 17, 2026, no stars yet, single-publisher service.

## FAQ

### Can it fill a form without an API key?

No. Search and parameter reads still go through the PhilForms API, which requires the key. The free test key covers the evaluation path.

### Does it handle the numbers, or just place text?

Both: `check_form_values` validates format and eligibility before filling, and `fill_form` refuses values the form cannot hold rather than repairing them. The refusal is the feature - a quietly corrected TIN is worse than a rejected one.

### How do I know the PDF was not edited afterwards?

`verify_pdf` checks a filled PDF against the issued document id. Combined with the per-form revision mapping, that is the chain a finance team needs when a certificate is challenged.

## Sources

- mcpservers.org listing `philforms/philforms-mcp` (page 1 of `/all`, October 19, 2026)
- README at `github.com/philforms/philforms-mcp` (created October 17, 2026, last push October 17, 2026, MIT, JavaScript)
- `https://philforms.com/api/v1/openapi.json` - OpenAPI 3.1, PhilForms API 1.0.0, 1,342 forms (probed October 19, 2026, HTTP 200)
- `https://philforms.com/api/v1/plans` - plan, credit, pack and allowance schedule in PHP (probed October 19, 2026, HTTP 200)
