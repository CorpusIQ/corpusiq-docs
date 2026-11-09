---
title: "frag.hugo MCP - German GDPR Duties on a Calendar"
description: "Fines, deadlines, subprocessor changes and the 72-hour breach clock for German GDPR work, with the legal source on every line."
category: Compliance
stars: "n/a (hosted; public tools need no account)"
added: 2026-11-08
source: "chatmcp/mcpso submission #6957 filed 2026-11-08T23:25:59Z; the official MCP registry record de.fraghugo/frag.hugo; the server card at mcp.fraghugo.de/.well-known/mcp/server-card.json; and the endpoint itself, where a keyless initialize answered 200 with 14 tool schemas, and two of them were driven live"
relevance: ★★★★
tags: [gdpr, compliance, datenschutz, germany, ai-act, nis2, deadlines, breach-notification, remote-mcp, oauth]
last_updated: "2026-11-08"
---

# frag.hugo MCP

**Compliance work is not a document, it is a calendar.** Every German business carrying personal data has dates it cannot miss: the 72 hours after a breach, the one month to answer a data subject request, the day an AI Act obligation starts, the moment a subprocessor changes its terms. frag.hugo is a German data protection platform with an external data protection officer attached, and its MCP server publishes those dates, the fines behind them and the paperwork around them as tools an assistant can call.

```text
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.fraghugo.de/mcp
Auth:        none for the public tools; OAuth 2.1 for the 42 account tools
Tools:       14 listed on a keyless call
Registry:    de.fraghugo/frag.hugo
Docs:        fraghugo.de/en/ai-assistant/
Language:    German output, including the source pages
```

## What the endpoint says about itself

A keyless `initialize` answers **200** as `frag.hugo` **1.0.0** and returns instructions that read as a working agreement rather than a pitch. The public half, without an account: GDPR fines, the deadline calendar, the software review bench, the subprocessor monitor, the supervisory authorities, the ransomware situation, plus free checks on email security, a website and a supplier. The account half reads and fills the booked sections with the same rights the person has in the app. Two rules are stated by the server and both matter: mail to people and deletion run in **two steps, preview then confirmation**, and everything a tool changes is written to a log and **can be undone for 90 days** through `undo_changes`. What is submitted is reviewed by the data protection officer, and the server states its own boundary in the same breath: no legal advice in an individual case.

## Two tools driven, and both returned dated, sourced records

`search_gdpr_fines` reported **101 cases** in the database with the newest three attached:

- **2026-10-02** - Xandr Inc. (Microsoft) - **EUR 8,600,000** - Datatilsynet, Norway - Art. 6 and Art. 9 GDPR, for real-time bidding data that allowed inference about sexual orientation.
- **2026-09-23** - IQVIA Solutions Italy - **EUR 7,000,000** - Garante, Italy - Art. 5, 9, 13, 25, 28 and 35.
- **2026-09-21** - Google Ireland - **EUR 403,000,000** - Data Protection Commission, Ireland - Art. 5, 6, 12 and 13.

Each line carries the authority, the articles, a summary and the regulator's own URL. That is the difference between a fines table and a fines database: a table gives a number, this gives the decision behind it.

`get_compliance_deadlines` reported **18 deadlines** counted from the day of the call, and the first three show why the calendar is the product:

- **2026-12-02** - AI Act, new prohibitions on sexual deepfakes without consent (Art. 5(1)(ba) and (bb), Art. 113(3)(a), Regulation (EU) 2024/1689 as amended by 2026/1744).
- **2026-12-02** - AI Act, machine-readable marking of AI-generated content for systems already on the market (Art. 50(2), Art. 111(4)).
- **2026-12-09** - Product liability, software is a product (Directive (EU) 2024/2853 Art. 2(1) and Art. 22, with the German modernisation act of 22 October 2026).

Every entry pairs the legal provision with a directive, a concrete "to do" and a EUR-Lex link, which is what an operator needs to hand a task to somebody who is not a lawyer.

## The rest of the surface

Fourteen tools, and the account ones are where the work happens. `check_software_gdpr` looks up whether a cloud service has been reviewed as a contract partner, with the processing agreement, subprocessors, data location and third-country transfer. `get_subprocessor_changes` watches the subprocessor lists of **17** widely used providers, Microsoft 365, Google Workspace, AWS, Salesforce, HubSpot and Stripe among them, and reports what changed and when, which is the single most missed obligation in a small company's GDPR file. `find_supervisory_authority` resolves the competent German authority from a federal state or a postcode. `get_cyber_threat_picture` counts how many German organisations ransomware groups named on their leak sites in 30 days and 12 months, by industry and group. `check_email_security` reads SPF, DKIM across common selectors, DMARC, DNSSEC, MTA-STS, TLS-RPT, BIMI and CAA. `start_website_check` looks at cookies and tracking before consent, the consent banner, Google Fonts, the privacy policy and the imprint. `report_data_breach` records a breach and starts the Art. 33 clock, and `create_data_subject_request` logs a request and calculates the one-month deadline under Art. 12. `vendor_profile` assembles a due-diligence note from those parts.

## How this differs from the compliance entries already here

[ISMS Copilot](/hermes/mcp/servers/external/isms-copilot-mcp/) carries the certification programme: gap analysis, risk registers and audit preparation across ISO 27001, SOC 2, GDPR, NIS 2 and DORA. [DutyKit](/hermes/mcp/servers/external/dutykit-mcp/) pre-checks a marketing action against German law and returns a verdict with a hash. frag.hugo is neither: it is a dated reference registry - fines, provisions, deadlines, subprocessor changes - plus the operational paperwork around a single named data protection officer who reviews what is submitted. A company that already runs an ISMS still needs the calendar, and a company that cannot afford a full-time DPO is exactly the customer this is shaped for.

## Limits, stated as limits

German, both in the interface and in the legal readings, so a company operating in another jurisdiction gets a partial fit. The output is German even where the underlying decision is in English. It is not legal advice and says so. The account tools need an OAuth connection, and this guide hands them a public-surface probe rather than an account session, so the write path is documented and not driven.

## Frequently asked questions

### Which deadlines does the calendar actually cover?

GDPR, NIS2, the AI Act, the Cyber Resilience Act, DORA, the Data Act and the European accessibility act, each with the legal provision, the status and the action.

### Can it watch for a breach notification?

Yes, through the account surface: `report_data_breach` records the incident and starts the 72-hour clock of Art. 33, and `my_privacy_deadlines` lists open deadlines for the connected organisation.

### Does it hold the personal data itself?

It is the register and the workflow, not the HR file: what it stores is the organisation's compliance objects - breaches, requests, software reviews, notes on vendors - behind an OAuth connection that carries the same rights the person has in the app. The two-step confirmation on mail and deletion, and the 90-day undo, are what a reviewer should test first.

### Is the free half useful on its own?

Yes. The fines database, the deadline calendar, the subprocessor monitor, the authority finder and the email and website checks all answer without an account, which makes it a reference an assistant can call before anybody signs anything.
