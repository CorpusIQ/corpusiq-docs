---
title: "PagoFix MCP - EU Late-Payment Interest Drafts"
description: "Free keyless EU late-payment claims: statutory interest, the fixed EUR 40 recovery compensation and three reminder letters in eight languages."
category: Legal / Finance
stars: n/a (free, no authentication)
added: 2026-10-31
source: "The chatmcp/mcpso submission issue #6511 filed 2026-10-31 at 17:53Z; a keyless initialize and tools list against https://pagofix.com/mcp returning HTTP 200 with serverInfo pagofix 1.0.1 and four tools with full input schemas; two live calc_claim calls measuring a German and a French claim; one live draft_reminder call returning a complete letter; and HTTP reads on pagofix.com, the repository and the privacy notice"
relevance: ★★★
tags: [legal, finance, receivables, late-payment, eu, interest-calculation, dunning, reminders, european-order-for-payment, keyless, free]
last_updated: "2026-10-31"
---

# PagoFix MCP

**An overdue invoice is a legal position with a number attached, and almost nobody claims the number. Under EU rules a creditor is owed statutory interest and a fixed recovery compensation the day the invoice falls due, without a reminder being sent. This connector computes that number and drafts the letter, and never sends it.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://pagofix.com/mcp
Auth:        none, free, no account required
Tools:       4 measured live
Cost:        free
```

## What it does

Four tools, one case shape. Every tool takes the same invoice fields: amount, currency, invoice and due dates, creditor and debtor countries, the law country, debtor type, and optionally the parties' names, VAT numbers, addresses, the debtor's email, IBAN, BIC and a calculation date.

- `calc_claim` returns the statutory interest, computed **per half-year period** at the reference rate in force for that period, the fixed compensation for recovery costs at a minimum of EUR 40, and the total, each with its legal reference and the primary sources behind the rate.
- `draft_reminder` drafts reminder letter 1 at day 3, letter 2 at day 10 with the interest, compensation and an attached calculation sheet, or letter 3 at day 17 as a final notice, in English, German, French, Spanish, Italian, Dutch, Polish or Estonian.
- `draft_eop` prepares a draft **European order for payment**, Form A under Regulation 1896/2006, for a cross-border claim, with the competent court, the fee information and filing guidance.
- `get_status` reports where a case stands: days overdue, which reminder is due now, the next step and its date, and the current total.

The coverage claimed is Directive 2011/7/EU plus the national rules of Austria, Estonia, France, Germany, Italy, the Netherlands, Poland and Spain.

## What this pass measured

`initialize` answered **HTTP 200** with `serverInfo` naming `pagofix` at version **1.0.1** and an instruction string that states the boundary in one sentence: PagoFix drafts, the creditor sends the letters and files the forms in their own name, and the money goes straight to the creditor. `tools/list` returned all **four** tools with full input schemas, so this is a measured surface and not a card description.

Three calls were made:

- A **German** claim, EUR 5,000 invoiced 2026-08-01 and due 2026-08-31, calculated on 2026-10-31, returned **61 days late**, interest of **EUR 87.91** and compensation of **EUR 40.00** for a total of **EUR 5,127.91**, with the interest basis given as the Bundesbank `Basiszinssatz` of **1.52 percent plus 9 points, 10.52 percent from 1 July 2026**, the citations **section 288(2) BGB** with **section 247 BGB** and **section 288(5) BGB**, and two source links, the statute text at gesetze-im-internet.de and the Bundesbank base-rate announcement.
- A **French** claim, EUR 12,500 invoiced 2026-07-10 and due 2026-08-09, returned **83 days late**, interest of **EUR 352.47** and the same EUR 40.00 compensation, for **EUR 12,892.47**, on **Code de commerce art. L441-10 II** with the statutory 30-day default in **art. L441-10 I** and the compensation in **art. L441-10 II and D441-5**. Both jurisdictions returned `status: verified` on their law block.
- `draft_reminder` for the German case at step 2 in English returned a finished letter in 0.1 seconds, subject line, body, HTML, a `mailto:` link, a send date, a payment deadline of 7 November 2026 and the attached calculation, in which the interest line reads 1 September 2026 to 31 October 2026, 61 days, 1.52 percent plus 9 points equals 10.52 percent, EUR 87.91.

The letter contains a line worth copying into any collections process, sent by the tool itself: if you think this claim is wrong, reply and say why, and we will not take any further step before we have looked at your answer. A dunning letter that invites a dispute in writing is a cheaper dispute than a court filing.

## Where the data goes

The privacy notice dated 2026-10-31 is unusually specific for a free tool. No account is needed to calculate or to draft: the calculation and the letters run in the browser, the invoice data typed or dropped as a PDF stays in the browser, and the vendor states it does not store that data on its servers, runs no analytics and sets no tracking cookies. An account adds stored cases, letters marked as sent, and a sign-in log kept 12 months with the IP address removed after 90 days. The company is Nukehive OU in Tallinn, Estonia, registry code 14647290.

One honest qualification belongs here: the browser claim describes the web calculator. An MCP call is server-side by construction, so the fields travel to `pagofix.com` on every request, and case storage only applies if a case is saved to an account. The containment is that the tool drafts and never sends: nothing leaves the vendor, no letter is posted and no form is filed.

## The operator decision this answers

Two bad outcomes compete on an overdue invoice. Chasing costs management time and a relationship, and not chasing costs the money. The rules already priced the delay, and almost no small business claims it because the calculation is fiddly: the rate changes every half year, the period has to be split, and the fixed compensation is a separate head of claim that has to be named.

The connector turns that into three tool calls and a paragraph. The interest is the argument the operator never makes, and the reminder ladder that arrives with it means day 3, day 10 and day 17 happen without anyone remembering.

## Where it sits in this catalogue

[Paidnice MCP](/hermes/mcp/servers/external/paidnice-mcp/) reads the receivables ledger and tells you what is overdue. This one starts where that stops: what the delay is worth under statute, in the debtor's jurisdiction, in the debtor's language.

Nothing else here drafts a legal claim. [Casus MCP](/hermes/mcp/servers/external/casus-mcp/) retrieves French law and grades its citations, and this tool is the executable end of the same discipline: the rule, the rate, the arithmetic and the letter that quotes all three.

## What this pass did not establish

`draft_eop` was not called, so the Form A output shape, the court mapping and the fee figures are the vendor's description rather than a measured artifact, and that is the tool that carries the most consequence. Only two of the eight jurisdictions were measured, so the other six law blocks are published coverage. The `caseId` returned for saved cases suggests account-side state that a keyless caller never creates. Whether the free surface is permanent is not stated. And the GDPR position for the MCP path specifically, where the caller's invoice data reaches their server rather than staying in a browser, is the vendor's notice read against a browser flow and not a data processing agreement.

## FAQ

### Does it need an API key or an account?
No. `initialize`, `tools/list` and both `calc_claim` calls answered without credentials, and the reminder draft came back complete. The vendor lists it as free and states it is self-service software rather than a debt collection service.

### Can it send the reminder for me?
No, and the design is deliberate. The tool returns the letter, the HTML, the `mailto:` payload and the calculation, and the creditor sends it in their own name. Filing the European order for payment is equally manual.

### Which countries and languages are covered?
Directive 2011/7/EU is the frame, with national rules published for Austria, Estonia, France, Germany, Italy, the Netherlands, Poland and Spain. Reminder letters are produced in English, German, French, Spanish, Italian, Dutch, Polish and Estonian, so the debtor's language and the law country are separate choices.

### How is the interest computed when the reference rate changes mid-claim?
Per half-year period. A German claim that runs from September into the next year is split at the half-year boundary and each segment is priced at the rate in force for it, which is why the response carries a `periods` array rather than a single rate.

### Is the calculation auditable?
Yes, and that is the strongest part. Each call returns the statute citations, the reference rate with its effective date, the source URLs behind it, and the day count and written arithmetic, so the number can be checked by an accountant or produced in a filing.

### What about a debtor who disputes the claim?
The letter itself states that a reply of "I dispute this" stops the process until the creditor has looked at the answer, which is the correct order of operations for a claim that may end in a court filing.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the full catalogue this entry belongs to
- [Paidnice MCP - Accounts Receivable for Xero and QuickBooks](/hermes/mcp/servers/external/paidnice-mcp/) - where the overdue balance is read
- [Casus MCP - French Tax and Legal Corpus in Chat](/hermes/mcp/servers/external/casus-mcp/) - the retrieval side of European legal work
- [Cobra MCP - Ecuador SRI Invoices From Chat](/hermes/mcp/servers/external/cobra-mcp/) - invoicing in another jurisdiction
