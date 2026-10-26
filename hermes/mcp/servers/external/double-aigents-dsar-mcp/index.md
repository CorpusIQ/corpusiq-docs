---
title: "Double AIgents DSAR MCP - GDPR Deadlines and Breach Clock"
description: "Free keyless MCP server for UK, EU and Swiss data protection: DSAR deadlines, the breach notification clock, letters and breach triage."
category: "Compliance / Legal Operations"
stars: n/a (new listing)
added: 2026-10-18
source: "mcp.so /feed (October 18, 2026 night sweep)"
relevance: ★★★
tags: [gdpr, dsar, data-protection, breach-notification, compliance, eu-ai-act, dpia, keyless, remote-mcp]
last_updated: "2026-10-19"
---

# Double AIgents DSAR MCP

**A keyless read-only server for the two deadlines that catch small companies out: the statutory clock on a subject access request and the notification clock on a personal data breach. It returns the deadline, the rule that produced it and the extension position for the UK, the EU and EEA, and Switzerland, and it supplies the acknowledgement, extension and clarification letters that go with it.**

```
Server type: Hosted (Streamable HTTP, JSON responses)
Endpoint: https://www.doubleaigents.com/api/mcp
Auth: None - free, read-only, no key and no sign-up
Tools: 10 - deadlines, quotes, letters, breach clock, breach triage, DPIA and EU AI Act screening, UK HR retention, search checklist
Jurisdictions: UK, EU and EEA, Switzerland
Publisher: Double AIgents Ltd (doubleaigents.com)
Listing: mcp.so feed card, October 18, 2026
```

## Why This Matters for Operators

Data protection deadlines are arithmetic with legal consequences, and they are the kind of arithmetic an assistant answers from a vague memory of "one month" or "72 hours" and then hedges. The deadline depends on the jurisdiction, on when the clock actually starts, on whether an extension is available and on which of the two clocks is running.

This server answers the narrow question correctly and labels what it is: general information, not legal advice. For an operator without a data protection officer, that is the difference between a request that gets answered inside the statutory window and one that becomes a complaint.

## What You Can Do Today

| Capability | What it does |
|---|---|
| DSAR deadline | `dsar_deadline` returns the statutory response date for UK, EU or CH, the rule that applies and the extension position, with an option to compute the extended date |
| Breach clock | `breach_clock` calculates the personal data breach notification deadline |
| Breach triage | `breach_triage` gives a likely-reportability view on an incident |
| Letters | `dsar_letter_template` supplies acknowledgement, extension and clarification letters |
| Request scoping | `dsar_request_scoping` produces a prefilled email to start free scoping of a request |
| DPIA screening | `ai_tool_check` screens an AI tool for DPIA and EU AI Act questions |
| Retention | `hr_retention` returns UK HR record retention periods |
| Search checklist | `dsar_search_checklist` lists where to look when compiling a response |
| Service info and quote | `dsar_service_info` and `dsar_quote` describe the vendor's outsourced DSAR service and its fixed price |

## Business Relevance

- **Compliance officers and operations leads** get the deadline computed rather than recalled, with the underlying rule named next to the date
- **Breach response is time-boxed:** the notification clock is the first thing an incident team needs and the last thing anyone wants to work out from scratch at the moment it fires
- **Letter templates remove the blank page:** acknowledgement, extension and clarification letters are the three documents a DSAR workflow actually sends
- **AI governance:** the DPIA and EU AI Act screening tool is a first pass on the question every company adopting an AI tool now has to answer
- **Zero onboarding:** no key, no account, no data sent beyond the dates and jurisdiction you supply

## Integration with CorpusIQ

The hard part of a DSAR is not the date, it is finding the data. CorpusIQ's connectors reach the systems a response has to cover: email, drive, calendar, CRM, commerce, accounting and analytics, all over read-only scoped tools with source citations. An assistant can pull the deadline and the letter from this server, then use CorpusIQ to locate what the person's data actually touches, which is the search the checklist describes.

## Limitations

- **Not legal advice:** the tool descriptions say so explicitly; this is general information and it does not replace counsel on a contested request
- **Three jurisdictions:** UK, EU and EEA, Switzerland; there is no US state privacy law coverage
- **Deadlines, not case management:** it computes dates and drafts letters; it does not track requests, store evidence or run the search
- **Vendor upsell present:** two tools describe the vendor's paid outsourced DSAR service, which is where the fixed quote comes from
- **New listing:** published in October 2026; the tool surface is current for version 1.2.0

## FAQ

### Is it really free and keyless?

Yes. The endpoint answers initialize without a key, the tool list returns all ten tools, and the documented surface is free and read-only. There is no sign-up step before the first deadline calculation.

### Does it store the request or the incident?

No. The tools are calculators and templates: you send a jurisdiction and a received date, or incident facts for triage, and you get a computed answer back. Nothing about a live request is tracked between calls.
