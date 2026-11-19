---
title: "Visamundi MCP - Visa and Entry Rules by Nationality"
description: "Visa, vaccination and customs rules for a nationality and destination, plus the visa products and their consular fees."
category: "Business Operations / Travel"
stars: "n/a (hosted service; server code at github.com/Visamundi/visamundi-mcp)"
added: 2026-11-19
source: "the mcp.so submission queue entry #7658 filed 2026-11-19T12:05:41Z, a keyless handshake and full tools/list on 2026-11-19, seven tools/call requests across four keyless tools, and the official MCP registry record"
relevance: ★★★
tags: [visa, travel, immigration, vaccination, customs, entry-requirements, business-travel, remote, keyless]
last_updated: "2026-11-19"
---

# Visamundi MCP

**The question "can this person legally board the flight" has two answers in most companies: the traveller's, and the one in the email nobody checked.**

Business travel fails at the border more often than at the booking. A passport with five months left when the destination wants six. A yellow-fever certificate required only for arrivals from a risk country, which nobody reads as applying to them. A visa that is mandatory for tourism and waived for business under 45 days. Every one of those is a rule with a jurisdiction, a nationality and a date attached, and every one of them is checkable.

This is the first entry in this catalog for a global visa matrix. The China transit entry here answers one country's visa-free transit rule precisely; Visamundi answers the nationality-by-destination question as a general table, and adds the health and customs rows that belong to the same decision.

```text
Server type:   remote Streamable HTTP (hosted)
Endpoint:      https://mcp.visamundi.io/
Server:        visamundi-public-mcp, version 2.0.0, protocol 2025-06-18
Auth:          none for the five reference tools (anonymous, read-only, rate-limited)
Tools:         8          5 read keyless · 3 application tools
Registry:      io.visamundi/visa
Repository:    https://github.com/Visamundi/visamundi-mcp
Website:       https://www.visamundi.io
Queue:         mcp.so #7658, filed 2026-11-19T12:05:41Z
```

## What was driven, and what came back

Ten calls, no account and no key. The five reference tools were exercised; the three application tools were not, because they create or price a filing.

**A visa requirement, in one field.** `get_visa_requirements` with nationality `FR` and destination `CN` returned `{"requirement": "30", "nationality": "French", "destination": "China"}`. The value is a bare **30**, and the unit is implied rather than stated: it reads as thirty days of visa-free stay. `CA` into `MX` returned **180** on the same pattern. `IN` into `US` returned the string `visa required`, and `US` into `BR` returned `e-visa`.

That mix is the tool's real shape. The requirement field is either a named status (`visa required`, `e-visa`) or a number that means days permitted without one, and the response does not distinguish the two types beyond the value itself. An agent rendering this to a traveller has to know which of those it received, and a bare `30` rendered as "requirement: 30" is not an answer anyone can act on.

**The vaccination row, which is where the conditional rules live.** `get_vaccines` on Kenya returned eight entries, each typed `needed` or `recommended` with a comment carrying the actual rule. Yellow Fever came back as `needed`, not recommended, with *"Certificate required for travellers aged 1 year and over arriving from a country with risk of transmission"* - a rule that depends on where the traveller came from, not only where they are going. Malaria was `recommended` with *"Risk year-round countrywide below 2,500 m, minimal in central Nairobi; take preventive medicine."* Hepatitis A, hepatitis B, rabies, typhoid, meningococcal meningitis and cholera followed, the last carrying the note that the CDC reports an active transmission situation.

**Customs, by destination.** `get_customs` on Japan returned four fields: alcohol (*"Aged 20 or over: 3 bottles of alcoholic beverages (about 760 ml each)"*), tobacco (*"200 cigarettes, 50 cigars, 10 packs of heated tobacco products, or 250 g of other tobacco, or a combination"*), currency (*"Yen (JPY) and foreign currency: unlimited, but amounts over JPY 1,000,000 must be declared on arrival and on departure"*), and medicines, which came back as an **empty string**.

**The visa product layer.** `list_visas` on Vietnam returned a priced catalogue rather than prose. The single-entry e-Visa is **90 days** stay and validity, consular fee **25 USD**, single entry, digital. The multiple-entry e-Visa is 90 days at **50 USD**, and its description carries the exception that matters: *"Visa is not mandatory if you stay less than 45 days."* A Pre-Arrival declaration follows as a third product with **no government fee**.

`get_visa` on product id **13083** returned the requirements a filing actually needs: `passport_validity_months: 1`, and a documents list naming a passport *"valid at least 1 month after the end of the stay"* and a photo, both mandatory.

**Two refusals worth recording.** `get_vaccines` and `get_customs` rejected the argument `destination`, which the tool descriptions and the server's own instructions both name, and required `country_code` instead: *"Input validation error: country_code: Invalid input: expected string, received undefined"*. The schema wins over the prose, and an agent following the instructions literally will fail on its first call. And an invalid country code (`ZZ`) returned **HTTP 200** with `{"success": true, "statusCode": 200, "code": "country_not_found", "message": "Country not found or invalid country code"}` - a failure envelope that declares itself a success, which any integration has to check the `code` field on rather than the status.

## The eight tools

| Tool | Arguments | What comes back |
|---|---|---|
| `get_visa_requirements` | `nationality`, `destination` | whether a visa is required, or the number of days permitted without one |
| `list_visas` | `destination` | the visa products available for that destination, with consular fees |
| `get_visa` | `id` | one product in full: stay, validity, fee, and the documents required |
| `get_vaccines` | `country_code` | vaccinations typed `needed` or `recommended`, each with its rule |
| `get_customs` | `country_code` | alcohol, tobacco, currency and medicines allowances |
| `get_application_form` | visa product | everything needed to complete an application |
| `save_application` | application fields | creates or updates a draft application |
| `get_payment_link` | complete application | the payment link, handed to the traveller |

## Why the reference layer is the part to integrate

The three application tools are a booking flow, and a business integrating this for its own staff does not want to file on their behalf. The five reference tools are the part that replaces a bad habit: a traveller asking a chat assistant whether they need a visa and getting a confident answer from training data with no date on it.

The distinction that makes the answer usable is the typed rule. Yellow fever is not "recommended for Kenya" in the corpus; it is required for arrivals from a risk country, aged one and over. That is the sentence a traveller needs, because the traveller knows where they connected through and the generic advice does not.

## Questions worth asking before you build on it

### Does it settle the question of how long a traveller can stay?

Partly, and the gap is explicit. The requirement field returns a number of days for visa-free entry and a named status otherwise, with no unit on the number. A system should treat a bare numeric requirement as "days permitted without a visa" and never render it as an instruction without that framing.

### Is the vaccination data travel-direction aware?

For yellow fever, yes: the certificate rule is conditioned on arriving *from* a country with transmission risk, which is the question a traveller actually has. For the rest, the entries are destination-level recommendations with the population and duration qualifiers stated in the comment.

### Are the fees authoritative?

They are consular fees, stated in the currency the consulate charges, and they are the government's fee rather than the service's price. Vietnam's single-entry e-Visa read **25 USD** and the multiple-entry **50 USD**, with the pre-arrival declaration at no government fee.

### What breaks first in production?

Parameter naming. The tool descriptions and the server instructions both say "for the destination country", while the schema requires `country_code`. Any wrapper should pass `country_code` and treat a `code` field on an HTTP 200 response as the real status, because `success: true` accompanies `country_not_found`.

## Gap recorded

The three application tools (`get_application_form`, `save_application`, `get_payment_link`) were not driven, because each opens a human filing path. The `medicines` field on Japanese customs returned an empty string, which is either "no restriction" or a missing record and cannot be told apart from the response; a trial should check a destination where a medicines rule is known to exist. The requirement field's numeric form has no unit, and no destination in this pass returned a number alongside an explicit unit to confirm the reading.
