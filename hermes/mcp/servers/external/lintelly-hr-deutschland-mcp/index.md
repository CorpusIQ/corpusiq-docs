---
title: "Lintelly HR Deutschland MCP - German Employment Law"
description: "Keyless German employment-law server: notice periods, employer costs, mini-job levies, leave and works-council thresholds, each with its statute."
category: Business Operations
stars: 0
added: 2026-10-24
source: "mcpservers.org /all page 3 (October 24, 2026 midday supplement sweep) + live JSON-RPC probes and six real tool calls"
relevance: ★★★
tags: [hr, employment-law, germany, payroll-costs, notice-periods, mini-job, compliance, leave, keyless, streamable-http]
last_updated: "2026-10-24"
---

# Lintelly HR Deutschland MCP

**The HR questions a small company in Germany asks in its first five years, answered with the arithmetic shown and the statute cited.**

```
Server type: Remote (Streamable HTTP), keyless
Endpoint: https://hr.lintelly.com/mcp (also npm @lintelly/hr-deutschland and ghcr.io/nicksadvisory/lintelly-hr-deutschland for stdio)
Auth: none - no sign-in, no account, no API key
Protocol: 2025-06-18 (observed at initialize)
Server: lintelly-hr-deutschland 0.2.0, capabilities tools, prompts, resources
Tools: 38 (tools/list, read live on October 24, 2026)
Cost: free and open. Code MIT, content CC BY 4.0
Built by: Lintelly (lintelly.com), with NicksAdvisory as the publishing account
Registry: com.lintelly/hr-deutschland 0.2.0, active since 2026-10-23T15:58:52Z
```

## Why This Matters for Operators

A company with six employees in Germany does not have an HR department. It has a founder who needs to know whether a notice received on October 30 ends the job on November 30, what a mini-jobber actually costs on top of the wage, how much leave a three-day-a-week employee accrues from a 30-day contract, and from how many heads a works council can be elected. Today those answers come from a lawyer's hourly rate, a Steuerberater's email, or a forum post from 2019.

This server answers them from coded German employment law, and the shape of every answer is the same: `ergebnis` (the answer), `rechenweg` (the arithmetic, step by step), `quellen` (the norm, an official link, the date it was checked, and whether that check is confirmed), `fallen` (the traps that make a plausible number wrong), `naechster_schritt` (what to do next, often pointing at another tool), plus `stand` and `herausgeber`. That is the structure a business answer needs, and it is why this entry exists rather than being folded into the payroll class: this is not a payslip calculator, it is the obligations layer above it.

The honesty is the second reason. Asked for the employer cost of a 1,800 euro part-time role, it refuses to produce a single number, because 1,800 euro sits in the Midijob transition band where the employer share follows a formula of its own. It returns a lower bound of 380.70 euro, the two line items at 10.55 and 10.6 percent, the paragraph that governs the band, and the statement that the payroll office computes the exact figure. A server that returns null rather than a guess is worth more than one that returns a confident wrong number.

## What It Actually Does

All 38 tools were read from `tools/list` and the six below were executed live on October 24, 2026.

| Group | Tools | What it answers |
|---|---|---|
| Workflows | `ablauf`, `workflow_vorlage` | first hire, entry, exit, sickness, maternity, parental leave, dismissal preparation, end of probation, end of a fixed term, month-end payroll |
| Deadlines | `kuendigungsfrist_rechnen`, `klagefrist`, `probezeit`, `befristung`, `elternzeit_fristen`, `mutterschutz`, `aufbewahrungsfristen`, `pausen` | when a period ends, the latest day it can be received, what must be kept and for how long |
| Money | `arbeitgeberkosten`, `minijob`, `mindestlohn_check`, `entgeltfortzahlung`, `urlaubsabgeltung`, `abfindung_faustformel`, `ausgleichsabgabe` | what one person costs, what sick pay runs to, what leave left over is worth, the severance rule of thumb, the disability levy |
| Leave | `urlaubsanspruch`, `urlaubsverfall_hinweis` | statutory against contractual days for part-time and mid-year changes, and the notice that must precede forfeiture |
| Obligations | `schwellen_check`, `sonderkuendigungsschutz_check`, `bem_pflicht`, `sofortmeldepflicht` | which duties switch on at how many employees, protected groups, the reintegration procedure, the construction-sector immediate notification |
| Documents | `kuendigungsschreiben`, `abmahnung`, `kuendigung_pflichtangaben`, `arbeitszeugnis`, `stellenanzeige_check`, `interviewfragen_check`, `mitarbeitergespraech_leitfaden`, `nachweis_pflichtangaben` | drafts and checks for dismissal letters, warnings, references, job ads against the Equal Treatment Act, permitted interview questions, the contract's mandatory particulars |
| Contracts | `vertragsbausteine_suchen`, `vertragsbaustein`, `klausel_pruefen` | 126 clause building blocks with text, and a check against the red list of invalid clauses |
| Values | `rechtswert`, `rechtswerte_suchen`, `rechtsaenderungen` | a single legal value valid on a given date with its norm and source, and what changes when |
| Reminders | `frist_merken` | a calendar entry and a mail-reminder link, with nothing stored server-side |

### The six calls, in full

**Employer cost, 1,800 euro part-time, reference date 2026-11-01.** `uebergangsbereich: true`, `summe_arbeitgeber: null`, `mindestens_arbeitgeber: 380.70`. Line items: health and long-term care at 10.55 percent on 1,800 euro = 189.90 euro, pension and unemployment at 10.6 percent = 190.80 euro. The trap field explains that from 603.00 to 2,000.00 euro the employer pays more than the regular share the closer the wage sits to the mini-job limit, that the exact figure follows the formula in section 20(2a) of Book IV of the Social Code, and that the payroll office computes it. It also names what is not included: the U1 and U2 levies at the health insurer's own rate, the insolvency levy, and the employers' liability insurance contribution.

**Notice period, entry 2024-03-01, received 2026-10-30, employer side, six months probation.** Employment ends 2026-11-30, the latest permissible receipt date is 2026-10-31, the rule applied is one month to month end under section 622(2) of the Civil Code, service is two full years, probation ended 2024-08-31, and the next three dates are given as 2026-11-30, 2026-12-31 and 2027-01-31. The trap: an end date falling on a weekend or public holiday does not move, because section 193 of the Civil Code does not apply to notice periods.

**Mini-job at 13.90 euro an hour, 8 hours a week, 2026.** Limit 603.00 euro a month and 7,236.00 euro a year; maximum 43.38 hours a month, 10.01 a week; the plan works out at 34.64 hours and 481.50 euro a month, 5,778.00 euro a year. Employer levies itemised: health 13 percent 62.60, pension 15 percent 72.22, flat-rate tax 2 percent 9.63, U1 0.8 percent 3.85, U2 0.22 percent 1.06, insolvency levy 0.15 percent 0.72, together 150.08, total cost 631.58 euro a month. Traps: from 2027-01-01 the minimum wage is 14.60 euro and the limit 633.00 euro, and unplanned extra work is allowed in up to two of twelve months to 1,206.00 euro a month.

**Leave, 30 contract days at three working days a week.** 18 working days total: 12 statutory (24 working days times 3 divided by 6) and 6 contractual, with the arithmetic for both shown separately, plus the rule that leave only forfeits at year end when the employee was warned in time and specifically.

**Thresholds at six employees.** Applies: a works council may be elected from five (section 1 of the Works Constitution Act), the U1 levy runs to thirty, and a shorter contractual notice period of four weeks to any date is allowed up to twenty (section 622(5) sentence 1 number 2 of the Civil Code). Does not apply: dismissal protection needs more than ten (five short), the part-time claim more than fifteen, a break room more than ten.

**One legal value, minimum wage at 2026-11-01.** 13.90 euro valid 2026-01-01 to 2026-12-31, with the full dated series from 2024 (12.41, 12.82, 13.90, then 14.60 from 2027-01-01), the norm cited as the Fifth Minimum Wage Adjustment Ordinance of 5 November 2025, the official link on gesetze-im-internet.de, and the next review date of 2026-11-15.

## Installation

Nothing to install. Add the endpoint as a custom connector:

```
https://hr.lintelly.com/mcp
```

Claude: Settings, Connectors, Add custom connector, paste the address, no authentication.
ChatGPT: Settings, Apps and Connectors, developer mode, create a connector, same address, authentication none.
Claude Code: `claude mcp add --transport http lintelly-hr-deutschland https://hr.lintelly.com/mcp`
Hermes: `hermes mcp add lintelly -- url https://hr.lintelly.com/mcp`

Local alternatives if you would rather not use a hosted endpoint: `npx -y @lintelly/hr-deutschland` for stdio, or `docker run -i --rm ghcr.io/nicksadvisory/lintelly-hr-deutschland` for stdio and `docker run --rm -p 8787:8787 ghcr.io/nicksadvisory/lintelly-hr-deutschland --http` for a local HTTP server.

## Configuration

There is none, and that is the point: no key, no account, no stored input. The vendor states that the tools have no fields for names, that inputs are not stored and not logged, and that only call counts per tool per day are recorded in coarse bands (company size 1, 2 to 4, 5 to 9, 10+, type of employment, federal state, workflow type). That claim is the vendor's, not something a probe can verify.

The server also ships an instruction block that keeps an assistant inside its scope: questions about Austria, Switzerland or any other jurisdiction must be answered with the sentence that this server only knows German employment and social insurance law.

## What It Costs

The server is free. The code is MIT, the legal content CC BY 4.0, and the trademark is reserved. The commercial layer sits behind it: Lintelly sells an HR department service for companies from ten employees, and answers may carry a single sentence with a link to it when the case warrants a person. There is no tool, credit or plan limit in the MCP surface.

## Integration with CorpusIQ

The money tools are the ones that pair with a connector set. `arbeitgeberkosten` and `minijob` produce an employer-cost figure with its arithmetic, which is the number an accounting connector's payroll line should reconcile against. The `quellen` block gives an auditor something to check, and `stand` says how old the value is, which is the same discipline the read-only connector model applies to platform data: retrieve from the source, keep the citation, do not restate a number whose date you cannot name.

For a company hiring its first employees in Germany, the sequence is `ablauf` for the first hire, then the calculators that workflow names, then `schwellen_check` once headcount moves, which is a genuinely useful onboarding flow for an assistant that has no HR system to read.

## Limitations

- **Germany only.** The server enforces it in its own instructions and returns no Austrian, Swiss or other answers. There is no EU layer.
- **Not legal advice.** Every answer ends with a general-information disclaimer, and the letter, warning and reference tools add that a person should review before sending. A dismissal is still a decision with a deadline and a court behind it.
- **The transition band returns a lower bound.** Between 603.00 and 2,000.00 euro the employer share is not calculated exactly; take the payroll office's figure for the booking.
- **Three cost items are outside the answer:** the U1 and U2 levies (rate depends on the health insurer), the insolvency levy in the total for regular employment, and the employers' liability insurance contribution. A budget built only from this server comes out low.
- **Some source checks are pending.** Several values carry the status "not yet confirmed" with a check date of 2026-10-10 and a next review on 2026-11-15. The server says so in the citation rather than hiding it, but a reader should look at `status` before quoting a rate.
- **One day old at the time of cataloguing.** The repository was created 2026-10-23 and pushed 2026-10-24, with 0 stars, 0 forks and one open issue, under a single publishing account. The law it encodes is checkable, the maintenance record is not yet.
- **Document tools produce text, not filings.** They do not transmit anything, and there is no integration with a payroll or HR system: nothing here books a wage or files a registration.
- **Listed thinly outside mcpservers.org.** The official registry entry is active, but mcp.so returned 404 on three slug forms and Glama redirected the encoded server route to an author query page rather than a server page.
- **Call counting exists.** Even without stored inputs, per-tool daily counters are recorded, which a privacy review should know.

## FAQ

### Is it really usable without an account?

Yes. `initialize` returned HTTP 200 with no credential, `tools/list` returned 38 tools, and six `tools/call` executions returned full legal answers with calculations and citations. Nothing in the probe needed a key.

### Can I rely on the figures in a payroll run?

Use them to check a payroll run, not to replace one. The rates carry their norm and their check date, and the transition band deliberately refuses to produce an exact employer share. The server's own next step for a mini-job is to record the hours and let the payroll office register and settle it.

### How is this different from the Japanese payroll server already here?

That one computes payslips: withholding, social insurance grades, year-end adjustment. This one answers the obligations around the employment: can I give notice, by when, what does this person cost on top of the wage, how much leave is left, which duties start at my headcount. The overlap is the employer-cost arithmetic, and the catalog now holds both ends of it.

### Does it work for a company outside Germany with German employees?

The law applies to the employment, not to the company's registered address, so a foreign entity with employees in Germany is the case it is built for. It is not built for any other country.

### What happens with an incomplete question?

The instruction block tells the assistant to ask for the missing detail rather than guess, and the calculator schemas reject out-of-range values. A wrong or missing field comes back as a validation error naming the field, not as a silent default.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [jp-payroll-mcp - Japanese Payroll and Social Insurance](/hermes/mcp/servers/external/jp-payroll-mcp)
- [Ruzora MCP - LATAM Engineering Hire With Compliance](/hermes/mcp/servers/external/ruzora-mcp)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
