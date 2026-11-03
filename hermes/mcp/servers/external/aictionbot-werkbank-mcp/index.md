---
title: "AICTIONBOT Werkbank MCP - Seven Procurement Checks"
description: "Seven deterministic procurement checks over MCP: Eurostat price benchmarks, sanctions, notice deadlines, expiring discounts and bank-change stops."
category: Finance / Procurement
stars: ★★★ (keyless public tier, 7 of 7 tools driven)
added: 2026-11-02
source: "the chatmcp/mcpso submission #6636 filed 2026-11-02T20:48:12Z, the official MCP registry entry com.kulicadvisory/aictionbot-werkbank, the vendor partner page at kulicadvisory.com/workbench/partner/, and a driven keyless session on https://www.kulicadvisory.com/mcp: initialize HTTP 200 as aictionbot-werkbank 1.2.0, tools/list returning 7 tools, and live calls to all 7"
relevance: ★★★
tags: [procurement, purchasing, sanctions, eurostat, price-increase, invoice, approval-matrix, discounts, deterministic, keyless, remote-mcp]
last_updated: "2026-11-02"
---

# AICTIONBOT Werkbank MCP

**A procurement team does not lose money on the invoice it reads. It loses it on the renewal notice nobody diarised, the supplier increase nobody benchmarked, the discount that expired at 3 percent, and the bank change nobody phoned to confirm. Every one of those is a comparison against data the company already has, and every one of them is checkable before the money leaves.**

```
Server type:   Remote (Streamable HTTP, JSON-RPC 2.0, MCP 2025-06-18)
Endpoint:      https://www.kulicadvisory.com/mcp
Auth:          none on the public tier, rate limited per sender
Tools:         7 measured, all deterministic, no model inside
Storage:       nothing kept, no account, no key
Vendor:        KULIC Advisory, Cologne
Registry:      com.kulicadvisory/aictionbot-werkbank (registry says 1.0.0, live server says 1.2.0)
Language:      German by default, English summary on request
```

## What it does

Seven tools, each one answering a single question an accounts payable or purchasing desk asks every month.

| Tool | The question it answers |
| --- | --- |
| `check_price_increase` | Is the increase this supplier is asking for in line with the market for this category? |
| `list_categories` | Which supplier categories does the price benchmark cover? |
| `screen_sanctions` | Is this supplier name on the EU, UN, US or UK sanctions lists? |
| `calculate_notice_deadline` | When is the last day to give notice before this contract renews itself? |
| `check_discount_window` | Which early-payment discounts expire inside the next payment runs, and which are already gone? |
| `check_approval_matrix` | Are the people who sign off purchases still employed, still permitted, still covered? |
| `check_invoice_payment` | Does this invoice's bank account match the vendor master before I pay it? |

The check that carries the most weight is the first one, because it is a comparison against public statistics rather than against another AI answer. `check_price_increase` takes a category code, the month of the last agreed price, and the increase the supplier is asking for, and returns the official Eurostat producer price movement for that category since that month, the gap to the request in percentage points, a verdict, and a counter-offer ceiling.

## What this pass measured

A keyless session against the live endpoint, all seven tools called.

`initialize` answered **HTTP 200** with `serverInfo` `aictionbot-werkbank` **1.2.0** and `tools/list` returned **7** tools in one response. No credential was used, and nothing was stored.

**The price benchmark.** `check_price_increase` with category **C17** (paper, board and packaging), last agreement **2024-01** and a requested increase of **12** percent returned:

```
latest_period              2026-09
market_change_percent      4.8
requested_percent          12
gap_percentage_points      7.2
verdict                    hoch
counter_offer_max_percent  4.8
source_updated             2026-10-31
```

That is an evidence-backed counter position rather than a negotiating opinion: the market moved 4.8 percent over the same period, so 4.8 is the highest number that still matches the index, and the request is 7.2 points above it.

`list_categories` returned the **34** category codes the benchmark covers, each as a NACE code with a German name and a goods or services label. Goods include C17 paper and packaging, C24 steel and aluminium, C26 electronics, C10 food and D for electricity and gas. Services include N81 building cleaning, N78 temporary staff, H49 transport, J62 IT services, M69 legal and tax advice and I56 canteen and catering.

**The sanctions screen.** `screen_sanctions` on a supplier name returned **8** possible matches in one answer, each with list, entity type, programme and a similarity score, followed by the date every list was read: EU **2026-10-23**, UN **2026-10-31**, OFAC SDN **2026-10-28**, OFAC NS **2026-10-19**, UK **2026-10-30**. The answer states in its own text that a similar name is not proof and that no hit is not a clearance, which is the correct posture for a screening aid.

**The renewal deadline.** `calculate_notice_deadline` with start **2024-04-01**, initial term **24** months, renewal **12** months and a **3m** notice period returned term end **2027-03-31**, last notice day **2026-12-31**, **58** days remaining and the extension date **2028-03-31** if the notice date is missed.

**The discount radar.** `check_discount_window` with two open invoices as of **2026-11-03** returned **2** items, **553.50** EUR of discount expiring inside the window and **146.41** EUR already lost on the older invoice, which the finding priced at roughly **37** percent annualised. It named the payment run that still catches the live one, a Tuesday run on **2026-11-10** against a discount deadline of **2026-11-11**.

**The pre-payment stop.** `check_invoice_payment` with an invoice whose IBAN differed from the vendor master by one digit matched the vendor on the VAT ID at similarity **1**, then returned verdict `stopp` with one stop signal stating that the account stands in no vendor record and that the change should be confirmed on the number from the master, not on contact details from the mail or the invoice. That is the fraud pattern that costs small businesses the most and it was caught by a comparison, not by a language model.

**The approval matrix.** `check_approval_matrix` with one departed approver still sitting in the matrix returned **1** stop and **1** check: the departed approver flagging as still named, and the missing deputy flagging beside it.

## The interface defects worth knowing before you connect

These are reproducibility findings, not opinions.

- **The free-text item lists have no schema.** `matrix`, `people`, `open_items`, `vendor_master` and `open_approvals` are declared as bare arrays of objects with no properties, so a wrong key is not rejected. A people row written as `name` produced "person not in the list" for a person who was in the list; the same row written as `person` produced the correct departure stop. Field names are only described in the tool description text.
- **English covers the summary, not the findings.** `language: "en"` switches the headline sentence to English, and the finding list underneath stays in German. Structured content keys are German too (`stufe`, `regel`, `wo`, `text`, `tun`). An English-only operator will read German sentences on every finding. The German is plain, but it is German.
- **Unit-bearing arguments are strings.** `notice_period` is a string pattern (`3m`, `14d`, `2w`), and sending the integer `3` returns a German error asking for the number plus a unit. `last_agreement` is a `YYYY-MM` string, not a date.
- **The registry lags the server.** The official registry lists version **1.0.0** and the live server reports **1.2.0**, so the registry description names the price check alone while the server serves seven tools. Read the live `tools/list`, not the registry entry.
- **The price index is Germany only.** Every category is a German NACE code against German producer and services prices. A supplier in another country can still be benchmarked against German input costs, but that is an assumption to state, not a given.

## Where this sits in the catalog

The neighbours are single-purpose and this is the bundle. [Sanctions Screening MCP](/hermes/mcp/servers/external/sanctions-screening-mcp/) and [mcp-sanctions](/hermes/mcp/servers/external/mcp-sanctions/) screen names against the same public lists and stop there. [Monitly MCP](/hermes/mcp/servers/external/monitly-mcp/) serves Eurostat and OECD series as searchable datasets, which is the raw index rather than the verdict on a supplier request. [Invoice Parser MCP](/hermes/mcp/servers/external/invoice-parser-pro-mcp/) reads a document, and [byondr Receipts MCP](/hermes/mcp/servers/external/byondr-receipts-mcp/) turns receipts into checked line items and a QuickBooks CSV. [Gov Contract Radar](/hermes/mcp/servers/external/gov-contract-radar-mcp/) finds public tenders.

None of them returns a stop, a check or an in-line verdict on an invoice, a renewal or a price request. What makes this entry worth a guide is that the answer is a decision with a number attached, computed from a public index and from the operator's own master data, and that the same seven checks run with no account and no key.

## Connect it

Keyless, so a client that accepts a plain Streamable HTTP server needs only the URL.

```json
{
  "mcpServers": {
    "aictionbot-werkbank": {
      "type": "http",
      "url": "https://www.kulicadvisory.com/mcp"
    }
  }
}
```

A first call that proves the connection in one shot:

```bash
curl -sS -X POST https://www.kulicadvisory.com/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```

Two worked prompts that match the tools:

- "Our packaging supplier wants 12 percent from January, we last agreed in January 2024. Is that in line with the market, and what should we counter with?"
- "Here are this month's open items with their discount terms. Which discounts expire before the next payment run, and which have we already lost?"

## Do not use it as

- **A legal or tax opinion.** The vendor states this on every answer. The contract wording decides a notice deadline, and a screening result neither clears nor condemns a supplier.
- **A stored system of record.** Nothing is kept. Every call is a fresh comparison against the payload you send, so the quality of the answer is the quality of your extract from the ERP.
- **A replacement for the vendor master.** It reads the master you send it. If the master is wrong, the check agrees with the wrong data.

## FAQ

### Is it free?
The public tier is keyless and rate limited per sender. The vendor sells a paid workbench, and the partner page at `kulicadvisory.com/workbench/partner/` carries the terms; the seven checks answer without an account.

### Does it send my data anywhere?
The vendor states nothing is stored and no AI runs inside the checks. The document you send is the invoice extract, so treat the payload as you would any document sent to an outside endpoint.

### Which sanctions lists, and how current?
EU, UN, US (OFAC SDN and non-SDN) and UK, screened on normalised name tokens with legal forms ignored, and every answer carries the read date of each list. The dates observed here were between five and fifteen days old.

### Can it tell me a supplier is clean?
No, and it says so. A similarity match is not proof and no match is not a clearance.

### Does it work in English?
Partly. The summary sentence follows `language: "en"`; the findings and the structured keys stay German.

### Do I need the Eurostat series myself?
No. The index and the source update date travel inside the price answer, and `source_updated` tells you how fresh the observation is.
