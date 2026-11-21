---
title: "Marsellus MCP - Israeli Form 1301 Return in Hebrew"
description: "Seven Hebrew-language tools that lay out an Israeli annual return, estimate tax or refund from Form 106 figures, and save a 72-hour draft."
category: "Finance"
stars: n/a (vendor-hosted)
added: 2026-11-21
source: "chatmcp/mcpso submission #7757 filed 2026-11-21T09:44:41Z; keyless initialize, tools/list and six tools/call requests on 2026-11-21; no record in the official MCP registry on the same day"
relevance: ★★★★
tags: [tax, israel, form-1301, income-tax, refund, hebrew, remote-mcp, keyless]
last_updated: "2026-11-21"
---

# Marsellus MCP

**Remote MCP server (Streamable HTTP, no authentication)** - an Israeli annual income tax return, Form 1301, prepared in a chat. The server returns the questions the return needs, estimates the tax, the refund or the balance from Form 106 figures, walks a foreign broker report step by step, and saves a draft the person completes on the vendor's site.

```
Server type: Remote (Streamable HTTP, no auth, no session id)
Endpoint:    https://marsellus.co.il/api/mcp
Tools:       7, every call carrying connector_rev: 6
Years:       2020 to 2025
Language:    Hebrew
Registry:    no record found on 2026-11-21
Vendor:      https://marsellus.co.il/ai
Fee:         NIS 329 per tax year, per the server's own triage text
```

## Why This Matters for Operators

Country tax is the last process most operators hand to a person, and it is the one where an assistant can do real damage by guessing. This server is built the opposite way. Its initialize instructions open with a rule that every figure must come from the user in this conversation or from a form they attached, never from the model's memory and never from an earlier conversation, and that anything recalled rather than read is prefixed with "according to what I remember" and confirmed year by year.

The structure also deals with the part that breaks most tax chats: the household. Marital status, children and employers are asked for each tax year separately, and a change of marital status triggers a date question, because the Israeli return is filed per person per year and the family status is read at the end of the tax year by identity number.

## What the Seven Tools Do

| Tool | What it returns |
|---|---|
| `marsellus_get_questions` | The whole return structure: supported years, the Form 106 field map, family questions, ten foreign-asset declarations, the income catalogue and the credit catalogue |
| `marsellus_estimate` | Tax due, withheld tax, and the refund or balance. Saves nothing |
| `marsellus_create_draft` | Saves the figures as a draft and returns a personal link valid 72 hours |
| `marsellus_draft_status` | Reads a draft link back: what was completed, which 106 forms arrived |
| `marsellus_triage_years` | Which past years are worth checking, up to six years after the tax year ends |
| `marsellus_guide` | The steps for pulling reports from a foreign broker (IBKR, Colmex, TradeStation) or for uploading a report |
| `marsellus_ibkr_reports_guide` | The two Interactive Brokers Custom Statement reports the return needs |

`connector_rev: 6` is mandatory on every call, and the server states that in its own structure response, so a client that drops it gets a correction message rather than a silent default.

## Measured Behaviour

Three estimates were driven on 2026-11-21 with a single Form 106 (gross salary in field 158, tax withheld in field 042), single marital status, tax year 2025:

| Salary (field 158) | Withheld (field 042) | Tax due | Verdict |
|---|---|---|---|
| NIS 240,000 | NIS 40,000 | **NIS 34,488** | refund **NIS 5,512** |
| NIS 240,000 | NIS 60,000 | **NIS 34,488** | refund **NIS 25,512** |
| NIS 120,000 | NIS 0 | **NIS 5,449** | balance due **NIS 5,449** |

The tax figure is a function of income only, and the withholding moves the verdict and nothing else. That is the correct shape: a refund is what was over-withheld, not what the engine returns by accident.

## The Arithmetic, Reproduced by Hand

The NIS 120,000 case reproduces to the shekel from the 2025 bracket scale:

```text
10% on the first 84,120        =  8,412.00
14% on the next 36,480         =  5,023.20
gross tax                      = 13,435.20
less 2.75 credit points
at NIS 2,904 a point           =  7,986.00
tax due                        =  5,449.20   ->  server says 5,449
```

The NIS 240,000 case does not reproduce, and the gap is recorded rather than smoothed. The same scale applied to 240,000 gives 38,719.20 before credits. The server reports 34,488, which is 4,231.20 below that, and 4,231.20 is 1.457 credit points at NIS 2,904. Nothing in the response explains a credit of 1.457 points for a single filer. Either the engine applies a rule it does not state, or one of its bands differs from the published scale. An operator should treat the estimate as an indication until the vendor explains that figure, and the return itself is still reviewed by the vendor's staff before filing.

## What Refusals Look Like

The server rejects a malformed call with a correction list rather than an error code, which is the behaviour an agent can act on. A Form 106 without an employer name and a salary:

```text
צריך לתקן לפני החישוב:
- forms_106[0].employer_name חובה
- forms_106[0]: חסרה משכורת (שדה 158/172)
```

A married request without a spouse object and without the joint-source answer:

```text
- נשוי/אה: צריך spouse עם first_name, last_name ו-gender
- answers.spouse_joint_source: לנשוי/אה צריך לשאול אם אחד מבני הזוג עובד בעסק או בחברה של השני (true/false)
```

Both arrive with HTTP 200 and `isError: true`, and both name the exact field, so a retry is mechanical.

## Privacy and Consent

`marsellus_create_draft` requires a contact email and `user_confirmed: true`, and the server instructs the model to show a consent paragraph verbatim before it is set. That paragraph names the data controller (אלאס השקעות בע״מ, company number 516961083), the 72-hour deletion of an untaken draft, the processors (Supabase, Vercel) and the business mailbox (Zoho), and it states that the Israeli identity number is never requested. The estimate tool saves nothing, so a person can price a year before deciding to hand over anything.

## Where It Stops

- **Six years, one country.** 2020 to 2025, Israeli residents, Form 1301 only. No company returns, no VAT, no payroll.
- **Forms it cannot process.** The IBKR guide is explicit that the broker's annual Activity Statement, Tax Documents, form 1042-S and FX reports are not accepted, and that the only accepted files are two Custom Statement CSV exports.
- **An exempt dealer above the ceiling.** A business with revenue over NIS 120,000 moves to an accountant rather than through this flow.
- **No filing.** The person files at the Israel Tax Authority. The server prepares a draft and, per its own text, adds no indexation or interest, which the Authority calculates by submission date.
- **Hebrew only.** Every instruction, question and answer text is Hebrew, including the field names on the Form 106 map.

### How is this different from Marsell, which is already catalogued?

Different company and different job. **Marsell** (getmarsell.com) is a marketing platform with 126 tools that plans content. **Marsellus** (marsellus.co.il) prepares one country's annual income tax return in seven tools. The names differ by one letter, so a search for either returns both, and the catalogue keeps this entry under the tax category and the marsellus-mcp slug to keep them apart.

### Can an agent file the return for someone?

No. The flow ends with a draft link the person opens on the vendor's site, where staff review the return and the person submits it. The server's own step list names filing at the Tax Authority as the final step and never claims to perform it.

### What happens to the figures after the conversation?

An estimate leaves nothing behind. A draft lives 72 hours and is deleted if it is not taken, per the consent paragraph, and `marsellus_draft_status` can read back what arrived on a live link without exposing an identity number, a birth date or a phone number.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [jp-payroll MCP - Japanese Payroll and Social Insurance](/hermes/mcp/servers/external/jp-payroll-mcp/)
- [MCP Server Discovery - November 21, 2026 (Night)](/hermes/mcp/sweeps/sweep-november21-2026-night)
