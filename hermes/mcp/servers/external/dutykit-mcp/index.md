---
title: "DutyKit MCP - The Compliance Gate Before an Agent Acts"
description: "Five keyless tools that clear a German, Luxembourg or EU invoice, marketing email or AI disclosure before the agent acts."
category: Compliance & Legal Operations
stars: "0 (renschrder-stack/dutykit; MIT; created 2026-11-08)"
added: 2026-11-08
source: "chatmcp/mcpso submission #6935 in the November 8 night window; the official MCP registry with two active records (io.github.r08150816s-star/dutykit 0.1.0 published 2026-11-07T16:05:01Z and io.github.renschrder-stack/dutykit 0.1.1); the vendor page at dutykit.dev; and the endpoint itself, where a keyless initialize answered 200 and all five tools were called live"
relevance: ★★★★
tags: [compliance, eu, germany, luxembourg, vat, vies, invoicing, ustg, uwg, ai-act, marketing-consent, remote-mcp]
last_updated: "2026-11-08"
---

# DutyKit MCP

**The expensive mistakes a business automation makes are no longer technical. An agent that sends a cold email to the wrong list, invoices without the fields the tax office requires, or starts a voice call without disclosing that it is a machine has broken a rule that already existed before the software did, and it broke it at machine speed and machine volume.** DutyKit is five small tools built for exactly that moment: the one right before the agent acts.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://dutykit.dev/mcp
Auth:        none - no account, no key, no OAuth
Protocol:    2025-06-18
Tools:       5
Coverage:    Germany, Luxembourg and EU-wide duties
Price:       free public beta, 200 tool calls per day per IP
License:     MIT (code), obligation catalogue CC BY 4.0
```

## What the endpoint says about itself

A keyless `initialize` on `https://dutykit.dev/mcp` answers **200** with no credential of any kind:

```json
{"name":"dutykit","title":"DutyKit","version":"0.1.0","websiteUrl":"https://dutykit.dev"}
```

`tools/list` then returns **five** tools with their full input schemas, also keyless. There is no account to create to read the surface, which is unusual on this catalog and matters for the integration question: an operator can attach it and test it in one minute.

## The five tools

| Tool | What it answers | Required arguments |
| --- | --- | --- |
| `pflichten` | The obligations for a country and an activity, each with legal basis, source URL, check date and verification status | `land` (`DE`, `LU`), optional `taetigkeit` |
| `rechnung_vorpruefen` | Whether a German invoice carries the mandatory fields of § 14 Abs. 4 UStG | `rechnung` (object), optional `land` |
| `werbung_vorpruefen` | Whether an agent may send this email or make this call | `kanal`, `empfaenger`, `einwilligung_belegt`, optional `bestandskunde` |
| `ki_hinweis` | The AI-disclosure wording for AI Act Art. 50 Abs. 1 in German, French, English or Luxembourgish | `firma`, optional `sprache` |
| `vat_pruefen` | A live EU VAT ID check through the European Commission's VIES service | `ust_id` |

Three of the five are pre-checks on an action, one is a lookup of what applies, and one is boilerplate text. The pre-checks are the reason this page exists.

## Two checks, driven live

**A VAT ID, checked against VIES.** `vat_pruefen` on `LU26375245` returned `gueltig: true` with the registered name and address as the Commission holds them:

```json
{"gueltig": true,
 "name": "AMAZON EUROPE CORE S.A R.L.",
 "anschrift": "38, AVENUE JOHN F. KENNEDY\nL-1855  LUXEMBOURG",
 "abfragezeit": "2026-11-08T10:02:56.221Z",
 "quelle": "VIES (EU-Kommission)",
 "nachweis": {"zeit": "2026-11-08T10:02:56.237968+00:00",
              "werkzeug": "vat_pruefen",
              "verantwortlich": "unbekannt",
              "pruefsumme_sha256": "b1f6558606a84cb2a3bd0bb740655f21b839eb4c801634e59def95f0abfcdf67"}}
```

**An email, cleared or blocked before it goes.** `werbung_vorpruefen` answers a three-valued verdict, and the third value is the interesting one.

| Call | Answer |
| --- | --- |
| email, consumer, no documented consent | `erlaubt: false` - "Ohne vorherige ausdrückliche Einwilligung unzulässig (§ 7 Abs. 2 UWG)" |
| email, business, no consent, existing customer | `erlaubt: null` - "Nur unter allen Voraussetzungen des § 7 Abs. 3 UWG ... menschliche Freigabe nötig" |

`false` stops the send. `null` does not clear it: it hands the decision back to a person and says why. A boolean would have collapsed the second case into the first or into a pass, and an agent reading a pass would have sent it.

## The catalogue behind the checker

`pflichten` for `DE` and `online_handel` returned three obligations, and each one carries what an operator needs to act without trusting the model:

```json
{"id": "de-impressum",
 "pflicht": "Impressum mit Name, ladungsfähiger Anschrift, schneller elektronischer Kontaktmöglichkeit, ggf. Register und USt-IdNr.",
 "grundlage": "§ 5 DDG",
 "quelle": "https://www.gesetze-im-internet.de/ddg/__5.html",
 "pruefstand": "belegt",
 "geprueft": "2026-11-07"}
```

The other two in that answer were the EU provider-information duty (Directive 2000/31/EC Art. 5) and the small-business rule with its live thresholds: previous-year turnover at or below **EUR 25,000** and current-year at or below **EUR 100,000** (§ 19 Abs. 1 UStG, § 34a UStDV). A date on the check and a status word beside it is the difference between a checklist and a claim.

## The proof record

Every answer carries a `nachweis` object: a timestamp, the tool that produced it, a `verantwortlich` field for the person accountable, and a **SHA-256** of the result. Nothing else in this catalog's compliance shelf returns a hash. For a business that has to show its work later - to an auditor, a client, or a tax adviser - the hash is what turns "the agent checked it" into something that can be re-verified.

The `verantwortlich` field defaults to `unbekannt` (unknown) unless the caller passes a name, so the accountability half is only as good as the integration: an agent that never fills it produces a proof record that names nobody.

## The invoice check, and what it refuses to claim

`rechnung_vorpruefen` on a deliberately thin invoice (issuer, number, net amount only, no date, no recipient, no tax number) returned `bestanden: false` with eight specific missing fields: the issuer's address, the recipient's name and address, the issuer's tax number or VAT ID, the issue date, quantity and nature of the supply, the time of supply, and the rate and amount of tax or a reference to an exemption. It then named its own boundary: the e-invoicing **format** check against EN 16931 is not done here, and it points at a separate server for that.

That refusal is worth more than the check. A tool that says what it did not verify is a tool an agent can quote honestly.

## What it does not do

- **Output is German.** The obligations, the refusal reasons and the invoice findings come back in German, and the only language switch on the surface is `ki_hinweis`. For a French- or English-speaking owner this is a workspace tool, not a self-serve one.
- **Coverage is DE, LU and EU-wide duties.** France and Belgium are announced as next; nothing else is claimed.
- **It is a filter, not legal advice**, and it says so in every response.
- **The AI Act line is a wording suggestion.** `ki_hinweis` returned a German sentence for Art. 50 Abs. 1 and marked one language variant as unchecked rather than presenting it as reviewed.
- **The repository is hours old and empty-sized.** GitHub reports **0** stars, creation at `2026-11-08T09:23:40Z`, last push at `09:24:36Z` and a size of **0 KB**, so the obligation catalogue cannot yet be audited from source. The registry carries two active records under two owner names (`io.github.r08150816s-star/dutykit` **0.1.0** published `2026-11-07T16:05:01Z` and `io.github.renschrder-stack/dutykit` **0.1.1**), which reads as a rename in progress rather than two servers.
- **The free tier is a rate limit, not a contract.** 200 calls a day per IP, no inputs or results stored, and a paid tier with a server-side audit log announced as coming.

## Why it earns a guide rather than a hold

Each individual leg is already carried here. [EU VAT VIES](/hermes/mcp/servers/external/honest-vies-mcp/) validates a VAT number with a consultation number for audit proof, [Rechnungslotse](/hermes/mcp/servers/external/rechnungslotse-mcp/) checks § 14 UStG fields and then goes further into XRechnung and ZUGFeRD validation, and [EU AI Act Explorer](/hermes/mcp/servers/external/eu-ai-act-explorer-mcp/) covers the regulation itself. None of them is a gate on an action: they are lookups the agent may or may not consult.

DutyKit is shaped the other way round. It expects to be called *instead of* acting, returns a verdict rather than a document, refuses the ambiguous case to a human, and stamps the answer with a hash. The neighbouring entries are references. This one is a stop sign, and a stop sign is what an outbound automation is missing.

## Frequently asked questions

### What does DutyKit MCP cost?

Nothing today: it is a free public beta at **200 tool calls per day per IP**, with no account and no key. The vendor states that the free tier stores no inputs and no results, and that paid plans with higher limits and a server-side audit log will follow.

### Does DutyKit need an API key?

No. `initialize`, `tools/list` and every one of the five tools answered without a credential in this pass, which is why the whole surface could be driven before writing this page.

### Can it stop an agent from sending a non-compliant marketing email?

It can refuse one. `werbung_vorpruefen` returns `erlaubt: false` for a consumer address with no documented consent under § 7 Abs. 2 UWG, and `erlaubt: null` with "human approval required" for the business-customer exception under § 7 Abs. 3 UWG, so the integration has to treat null as a block until a person clears it.

### Which countries does it cover?

Germany, Luxembourg and EU-wide duties today, with France and Belgium announced as next. The invoice field check is German (§ 14 Abs. 4 UStG), and the AI Act disclosure covers all four of de, fr, en and lb.
