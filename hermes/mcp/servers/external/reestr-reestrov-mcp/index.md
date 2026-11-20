---
title: "Reestr Reestrov MCP - 570 Russian Registries and One INN"
description: "A keyless catalogue of 570 Russian state registries, keyed by INN, where the law and the article come back before the record does and an invalid tax number."

category: "Public Records / Russia"
stars: "0 (remote Streamable HTTP, keyless with 30 requests a day and 10 rows per source; 8 tools, all 8 called, 6 returning substantive payloads)"
added: 2026-11-16
source: "the mcp.so submission queue entry #7429 filed 2026-11-15T03:29:00Z, and a driven session on 2026-11-16 in which all 8 tools were called over Streamable HTTP, including two registry lookups by INN"
relevance: ★★
tags: [public-records, russia, company-verification, egrul, inn, licensing, sanctions-adjacent, keyless, remote, mcp]
last_updated: "2026-11-19"
---

# Reestr Reestrov MCP

**A Russian counterparty question is the one a model will always answer from imagination.** Whether a supplier is still trading, whether it holds the licence it says it holds, whether it sits on the register of unscrupulous suppliers, whether it is a registered personal-data operator: each is a lookup against a state register, and none of them is in a language model's weights.

Reestr Reestrov is a catalogue of **570 Russian state registries across 75 agencies**, keyed by INN, with **99 of them carrying retrievable records** and **8,018,910 records** behind the keyless path. What earns it a page here is not the size. It is that **the law and the article are returned before the record**, and that an INN with a bad checksum is **refused by name** instead of being searched and returning an empty result that reads as an absent company.

```
Server type:   remote Streamable HTTP
Endpoint:      https://reestr-reestrov.ru/api/mcp
Server:        reestr-reestrov, version 1.0.0
Protocol:      2025-06-18
Auth:          none for the keyless path; a cabinet key raises the limits
Tools:         8 (catalogue, INN check, permits, registry query, OKVED map, sources)
Language:      Russian throughout, including tool descriptions and errors
Listed on:     the mcp.so submission queue as #7429
```

## The evidence tier

**Keyless and driven.** `initialize` answered **200** as `reestr-reestrov` **1.0.0** on protocol **2025-06-18**. `tools/list` returned **8** schemas and **all 8** were called: `list_agencies`, `search_registries`, `get_registry`, `check_inn`, `check_permits`, `query_registry`, `registries_for_okved`, `list_sources`. Six returned substantive payloads, `query_registry` returned a source header plus 10 matching records, and one sub-block inside `check_inn` timed out, which is recorded as a defect below rather than smoothed over.

The keyless cap is stated by the server in its own words, in its own language:

> Без ключа: до 10 строк на источник, 30 запросов в сутки. Ключ: https://reestr-reestrov.ru/kabinet/

Translated: **10 rows per source and 30 requests a day without a key**, with the key issued from a cabinet page. Every table in this guide was produced inside that budget.

## Three numbers, and they reconcile

The most useful check on a registry-of-registries is whether its own totals agree with each other.

| Measurement | Value |
|---|---|
| Agencies listed by `list_agencies` | 75 |
| Sum of the per-agency `registries` counts | 570 |
| `search_registries` total on an empty query | 570 |
| Sources with records, by `list_sources` | 99 |
| Sources whose record count is above zero | 94 |
| Records across all sources | 8,018,910 |

**75 agencies sum to 570 registries, and the catalogue total is 570.** That is the arithmetic that separates a maintained catalogue from a page count, and both numbers are returned by the server rather than by this guide.

The **570 against 99** gap is the distinction worth understanding before quoting either figure: 570 registries are **described** (who runs them, under which law, since when, whether they are open, whether they can be searched by INN), and 99 of them are **loaded**, meaning the tool can return rows from a dated copy of the official export. The other 471 are answered with a name, an agency, a law and a `check_url`, which is still an answer to *where do I check this* and is not an answer to *what does it say*.

## The eight largest loaded registers, with their own dates

`list_sources` returns a record count, an INN count and an `updated_at` stamp per source, which makes the freshness of each register a field rather than a footnote:

| Source | Records | INNs | Updated |
|---|---|---|---|
| `fns-msp-support` | 3,361,365 | - | 2026-11-12 23:42:48 |
| `fsrar-license` | 1,430,910 | - | 2026-11-11 23:42:30 |
| `rtn-lift` | 687,562 | 44,511 | 2026-11-16 01:30:24 |
| `rtn-opo` | 658,320 | - | 2026-11-16 01:10:57 |
| `nostroy` | 421,202 | - | 2026-11-15 23:42:31 |
| `goslog` | 90,116 | 90,102 | 2026-11-12 23:40:01 |

Two of those stamps are **hours old** at the time of this pass, which is the difference between a scraped mirror and a feed. `goslog` is the freight-forwarder notification register that became mandatory under **140-ФЗ on 2026-09-01**, and its 90,116 records against 90,102 INNs is the shape of a register where nearly every record is a distinct company.

## One INN, six registers, in a single call

`check_inn` on **7707083893** (Sberbank) returned a compound object rather than a row, and the value is in how many registers answer at once:

| Block | Result |
|---|---|
| `egrul` | Found: **ПАО СБЕРБАНК**, OGRN **1027700132195**, KPP **773601001**, registered **16.08.2002**, head **Греф Герман Оскарович**, region **Г.Москва** |
| `bankrot` | Found, fedresurs company page, status **Действующее**, **0** cases, **0** out-of-court, **3** intentions |
| `pdn` | Found, registration **11-0187199**, registered **24.03.2011**, operating since **26.07.1991**, with the RKN operator URL |
| `rnp` | **Not found**, **0** active rows |
| `lic` | Found, licence **02970**, issued **02.09.2013**, valid to **01.09.2033**, subsurface use for drinking-water supply |
| `msp` | A `TimeoutError`, recorded below |

**The negative answers are the product.** `rnp: found false` with an active count of zero is the register of unscrupulous suppliers answering a procurement question, and a model asked the same question cold will either invent a clean record or refuse. The OGRN, KPP, registration date and named head are all checkable against the official source, and the bankrot block links to the fedresurs page rather than summarising it.

## The permits pass, which is the query this server exists for

`check_permits` on the same INN walked **99** sources and returned **26** with at least one row. The register names, agencies and row counts come back per source, and the interesting ones for a counterparty check are:

| Register | Agency | Rows |
|---|---|---|
| `cbr-credit` | Bank of Russia | 1 |
| `cbr-prof` | Bank of Russia | 4 |
| `cbr-crypto-exchange` | Bank of Russia | 1 |
| `cbr-digital-depository` | Bank of Russia | 1 |
| `cbr-ops`, `cbr-ois`, `cbr-advisor`, `cbr-sro-member` | Bank of Russia | 1 each |
| `rkn-svyaz` | Roskomnadzor | 10 |
| `rkn-broadcast` | Roskomnadzor | 10 |
| `rkn-pdn`, `rkn-ori` | Roskomnadzor | 1 each |
| `rtn-opo`, `rtn-lift`, `rtn-energy-permit` | Rostechnadzor | 10 each |
| `rtn-license-opo`, `rtn-license-atom` | Rostechnadzor | 1 and 3 |
| `fsrar-license` | Rosalkogoltobakkontrol | 3 |
| `reestr-po` | Mintsifry | 1 |
| `fstec-tzki`, `fstec-szki` | FSTEC | 1 each |
| `rosgvard-chop` | Rosgvardia | 2 |
| `knd-scrap`, `fssp-ko-mfo`, `fns-edo`, `arshin-producers` | various | 1 each |

**26 registers for one company, in one call, each with the agency named and a `source_url` to the primary page.** A procurement team asking whether a Russian supplier is licensed for the work it claims gets the licence registers as a list rather than as a search plan. The cap is visible in the payload rather than hidden: several registers return exactly **10** rows, which is the keyless per-source limit and not the true count.

## The law comes back with the record

`get_registry` on `reestr-operatorov-pdn` returns the citation before the description:

```
law:      152-ФЗ от 27.07.2006 "О персональных данных", ст.22
year:     2006
agency:   Роскомнадзор
access:   open
by_inn:   true
law_ref:  {short: 152-ФЗ, article: 22, page: .../zakon/152-fz-2006/}
```

That block is what makes a compliance answer quotable: **152-ФЗ article 22** with a page for the statute, not a paraphrase. `registries_for_okved` applies the same discipline to a business type: **OKVED 62.01** (software development) maps to **10** registers a software company is expected to appear in, starting with the RKN personal-data operator register under that same article and carrying a `for_any_business` flag on the entries that are not optional.

## The refusal that justifies the tool

An INN of **9999999999** was rejected rather than searched:

> Неверный ИНН: нужно 10 или 12 цифр с верной контрольной суммой

The message names the rule: **10 or 12 digits with a correct check digit**. That is the difference between a lookup that says *no such company* and one that says *that is not an INN*. In a jurisdiction where a wrong digit returns an empty result that reads as a clean company, the checksum refusal is the safety property.

## Where the surface is thin, measured rather than assumed

- **One sub-call timed out.** `check_inn`'s `msp` block (the register of SMEs) returned `{"error": "TimeoutError"}` while the other five blocks answered in the same response, so the compound call degrades in pieces rather than failing whole. Re-running for a single block is the workaround and the payload tells you which block to re-run.
- **Russian only.** Tool descriptions, errors and every field are in Russian, including the refusal message above. An English-speaking operator will read the payload through a translation step, and the tool descriptions are worth translating once rather than per call.
- **30 calls a day without a key.** A counterparty sweep over 50 companies at one `check_inn` each plus a permits pass is over budget on the keyless path, and the cabinet key is the documented way past it.
- **A row cap that reads as a count.** A register returning exactly 10 rows is the keyless limit, not the population: `rtn-lift` holds **687,562** records against **44,511** INNs, and `query_registry` on it returned 10. Treat `found: 10` as `10 or more`.
- **Not a sanctions list.** The registers here are Russian state registers. A sanctions screen is a different surface, and [TollNode](/hermes/mcp/servers/external/tollnode-mcp/) prices one at **$0.010 a name** across OFAC, UK, EU and UN lists if that is the question being asked.

## FAQ

### Does it need a key?

No. The catalogue, the INN check, the permits pass and the registry queries all answered without one, capped at **10 rows per source and 30 requests a day**. The cabinet key raises both and is linked from the limits sentence the server returns with the data.

### What does one INN buy?

Six register answers from `check_inn` (EGRUL, bankruptcy, personal-data operator, unscrupulous suppliers, licences, SME register) and, separately, a **26 register** walk from `check_permits` with the agency and primary URL for each hit. Both are one call each on the keyless path.

### Can I tell how fresh an answer is?

Yes, and it is the strongest part of the surface. `list_sources` carries `updated_at` per register, and two of the largest were stamped **hours** before this pass. A record also carries its own `date_from`, `date_to` and status, so a licence that expired in 2019 cannot be reported as current.

### Where does this fit a business?

Supplier onboarding, procurement eligibility, licence verification before a contract, and personal-data operator checks for a company handling Russian data are the four places this beats a chat answer. It is the first entry in this catalog for **Russian state registries keyed by INN**, and the same INN keying is what makes a 26-register answer one call rather than 26.

## Related reading

- [External MCP server catalog](/hermes/mcp/servers/external/) for the rest of the servers evaluated and catalogued here
- [firmy.ai](/hermes/mcp/servers/external/firmy-ai-mcp/) for the Polish company registry surface this sits beside as a second national register
- [TollNode](/hermes/mcp/servers/external/tollnode-mcp/) for a priced sanctions screen across OFAC, UK, EU and UN lists
- [CorpusIQ connectors](https://corpusiq.io/connectors) for the read-only business systems this catalog is built around
