---
title: "Carrier Ledger MCP - FMCSA Checks Before Booking"
description: "Check US trucking companies and freight brokers against FMCSA public records: authority, insurance, suspension notices and contact-change alerts."
category: Logistics & Transportation
stars: n/a (new listing)
added: 2026-10-10
source: "mcpservers.org /all (page 1 cohort) + vendor page (carrier-ledger.neoaethel.workers.dev); catalogued at the October 10, 2026 evening sweep"
relevance: ★★★
tags: [logistics, freight, fmcsa, compliance, risk, fraud-prevention, remote-mcp]
---

# Carrier Ledger MCP

**Free read-only MCP server that checks a trucking company or freight broker against FMCSA public records** - before you book or pay them: operating authority, liability insurance and bond on file, suspension or revocation notices, and plain-English red flags, each citing the FMCSA dataset it came from. Three keyless tools cover a single carrier, a whole list, and the day's suspension notices. The logistics find of the October 10 evening sweep, catalogued with the endpoint probed live (initialize returns 200, `carrier-ledger` v1.1.0).

```
Server type: Remote (Streamable HTTP at https://carrier-ledger.neoaethel.workers.dev/mcp, keyless)
Auth: None for the MCP tools (read-only; no contact details returned)
Tools: 3 (lookup_carrier, check_carrier_list, recent_suspension_notices)
Category: Logistics & Transportation
Built by: Carrier Ledger (official MCP Registry listed; Pro tier adds an API and webhooks)
```

## Why This Matters for Operators

Freight fraud runs on timing. A carrier's insurance lapses, FMCSA serves a suspension notice weeks before it takes effect, and the snapshot still says "Active" until the effective date - plenty of window for a load to be booked by a company that is about to lose its authority. Worse, load thieves take over a real carrier by changing the phone and email on its FMCSA record and then book freight as that company. Carrier Ledger watches those records daily and surfaces exactly these changes, with the government source printed next to every fact, so a dispatcher or broker can check in seconds instead of trusting a static certificate.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `lookup_carrier` | Looks up one US motor carrier or freight broker by USDOT or MC number: operating authority, liability insurance and bond, suspension and revocation notices, and red flags, each citing its FMCSA dataset |
| `check_carrier_list` | Screens up to 25 carriers or brokers at once (MC numbers up to 10) and returns each one's most important red flag, urgent ones first - built for carrier lists and load-board shortlists |
| `recent_suspension_notices` | Lists carriers and brokers recently served an involuntary suspension notice (usually a cancelled insurance policy), with the date each suspension takes effect (up to 100, newest first) |

Around the MCP surface, the product adds what the records cannot: change history for every watched carrier (phone, email and address changes are logged and flagged for 30 days), look-alike detection (the same phone, email or street address on other USDOT numbers), a dated, printable record of what FMCSA showed at the moment a load was booked (free with an account), and broker bond-cancellation tracking. The Pro plan ($29 a month, 14-day trial; free for 5 watched carriers) adds a JSON API and webhooks for a TMS. The vendor's own caveat is refreshingly clear: this is not a rating and not a vetting decision, it is the public record, faster.

## Installation

```json
{
  "mcpServers": {
    "carrier-ledger": {
      "url": "https://carrier-ledger.neoaethel.workers.dev/mcp"
    }
  }
}
```

No sign-in needed for the three read tools; the endpoint is listed in the official MCP Registry. Clients that only run local commands can bridge to the remote URL; there is nothing to install or pay on the read side.

## Configuration and Safety

- Read-only and keyless: look up carriers, screen lists, read recent suspension notices. The tools do not return contact details and cannot change anything.
- Every fact cites its FMCSA dataset (Motus RevokeSuspend file, Company Census file, licensing and insurance files), and the product distinguishes facts read from the new Motus system versus the legacy file FMCSA froze in May 2026.
- Monitoring side effects (alerts, watchlists, dated records, history) live in the account product, not in the MCP tools.
- The suspension-notices tool is the one to wire into a daily routine: notices are served weeks ahead of the effective date, which is exactly the window where a check changes a booking decision.

## Business Relevance

- **Freight brokers and 3PLs**: screen every carrier before tendering a load - screen the shortlist in one call, then pull the full record on anyone with a flag.
- **Shippers and manufacturers with inbound freight**: check the carriers your partners use and watch for contact-change patterns that precede double-brokering fraud.
- **Carriers themselves**: watch your own USDOT number - FMCSA's 2026 Motus rollout has wrongly marked some carriers inactive - and check brokers' authority and bond before hauling for them.

## Integration with CorpusIQ

Vendor checks answer "is this counterparty safe to book"; CorpusIQ answers "what does this counterparty mean to my business" - open orders, unpaid invoices, shipment history from the connectors you already run, with each number cited to its source. Run the FMCSA check in chat, then ask CorpusIQ what you already know about the company, and keep both answers in one thread.

## Limitations

- The MCP tools are read-only and omit contact details; full monitoring, dated records and alerts are account features of the paid product.
- Coverage is US FMCSA data only: operating authority, insurance, bonds, notices and record changes. No identity checks, ELD or GPS tracking, or onboarding workflows - the vendor lists those as out of scope.
- Free checking is unlimited for lookups, but watched-carrier monitoring is capped by plan (free for 5, Pro for 250).
- The vendor states plainly it is not a rating or a vetting decision; it returns the public record with sources, and the booking judgement stays with your team.

## FAQ

### Does the MCP server cost anything?

No. The read-only tools are free and keyless: single lookups, screening a list of up to 25, and reading recent suspension notices. Paid plans cover monitoring, alerts and the API.

### What is the most useful routine check?

`recent_suspension_notices` for the daily sweep, then `check_carrier_list` against your active carrier list - a suspension notice appears weeks before FMCSA flips the public snapshot from "Active", so the notice is the early warning.

### Is this a vetting or rating service?

No, by design. It copies FMCSA public records and reports changes with each fact's dataset cited. There is no score, and the vendor says so on the tin - it gives teams the facts faster, the decision stays human.

## See Also

- [Plain Freight MCP - China to US Freight Quotes for Agents](/hermes/mcp/servers/external/plainfreight-mcp/)
- [Ship24 Tracking MCP - Package Tracking Across 2,500+ Carriers](/hermes/mcp/servers/external/ship24-tracking)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
