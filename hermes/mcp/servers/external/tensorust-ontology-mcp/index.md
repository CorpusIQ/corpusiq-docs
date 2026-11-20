---
title: "Tensorust Ontology MCP - Who Owns a US Company"
description: "A keyless 41-tool ontology that answers who controls a US organization and which federal rule applies, with a dated table and a named source behind every."

category: "Ownership / Public Records"
stars: "0 (remote Streamable HTTP, keyless free tier with 25-row samples; 41 tools, 25 driven)"
added: 2026-11-15
source: "the mcp.so submission queue entry #7408 filed 2026-11-16T00:19:47Z, and a driven session on 2026-11-15 in which 26 tools/call requests were run against 25 distinct tools on the keyless free tier"
relevance: ★★★
tags: [ownership, public-records, due-diligence, private-credit, federal-awards, road-act, property, keyless, remote, mcp]
last_updated: "2026-11-19"
---

# Tensorust Ontology MCP

**Every due-diligence question is a join, and the models answer it without the join.** A lender asks who controls the borrower. A procurement team asks whether a vendor appears on a banned list. A fund asks what other lenders mark the same loan at. A business owner asks whether the next acquisition is already over a regulatory threshold. Each of those is one answer standing on four or five public datasets that do not share an identifier, and an assistant asked cold will produce a plausible corporate structure that nobody recorded.

Tensorust is an ontology over those datasets with **2.4 million** organizations, **1.16 million** parcels, **428,254** FCC licences, **229,502** federal awards and **50,043** aircraft, joined on a canonical organization key, and it answers the join rather than the guess. What earns it a page is not the size. It is that **every table carries an `as_of` date and a method paragraph** naming the source file and the matching rule, and that it **refuses** a malformed argument instead of improvising, which the guides in this catalog do not get to assume.

First entry here for the ROAD Act investor-purchase screen, federal banned-vendor exposure over research papers, BDC private-credit mark disagreement, and the No Surprises Act arbitration market.

```
Server type:   remote Streamable HTTP, stateless
Endpoint:      https://shop.tensorust.com/api/mcp
Server:        tensorust-ontology, version 0.6.0
Protocol:      2025-06-18
Auth:          none for the free tier (no key, no account, no OAuth);
               a bearer key raises row limits
Tools:         41 across ownership, federal exposure, private credit,
               property, spectrum and arbitration
Repository:    https://github.com/Mattbusel/tensorust-skills
Docs:          https://shop.tensorust.com/mcp
Registry:      com.tensorust/ontology
Listed on:     the mcp.so submission queue as #7408
```

## The evidence tier

**Keyless and driven.** `initialize` answered **200** as `tensorust-ontology` **0.6.0** on protocol **2025-06-18** with a full instructions field, `tools/list` returned **41** schemas, and **26** `tools/call` requests were run across **25** distinct tools, including four deliberate failure paths. No credential was used. Two of the tables below are dated by the server itself (`as_of`) rather than by me.

`describe_schema` is the first tool worth calling on any ontology, and this one returns its own inventory:

| Object type | Objects |
|---|---|
| Organization | 2,446,357 |
| Parcel | 1,161,075 |
| FCCLicense | 428,254 |
| Award | 229,502 |
| Aircraft | 50,043 |
| ControlGroup | 48,569 |
| ERateRequest | 23,332 |
| Sanction | 19,958 |
| PAC | 3,331 |
| Loan | 3,214 |
| Rule | 7 |
| FCCFiling | 454 |

## The ROAD Act screen, and the arithmetic that makes it a product

`road_monitor_summary` returns the rule before it returns the data: the **21st Century ROAD to Housing Act section 1001**, at **42 U.S.C. 19521**, enacted **2026-07-11**, effective **2027-01-07**, proposed rule **31 CFR Part 36** under RIN **1505-AC96**, docket **TREAS-DO-2026-0529**, at **91 FR 66799**, comments due **2026-11-23**, threshold **350** homes, penalty **up to the greater of $1,000,000 or 3x the purchase price per purchase**.

Then the population: **43** covered control groups holding **166,797** homes, of which **28** sit in the 350 to 700 band, **19** hold more than 350 homes with no *single* entity above 350, and **6** are hidden from a name search entirely (**3,442** homes held by groups a name query does not surface), across **2,325** covered legal entities.

`road_investor_group` on Invitation Homes returns the shape of the problem in one object: **32,315** homes in coverage, **251** legal entities, sixteen counties from Bexar to Travis, a largest single entity of **2,079** homes (SRP SUB LLC), and `over_threshold_by` **31,965**. The check is one subtraction: 32,315 minus the 350 threshold is 31,965. **A 251-entity structure where no entity crosses the threshold is exactly why a group-level screen and an entity-level screen disagree**, and the `link_kinds` block shows where the structure was recovered from: 180 root links, 90 parent, 81 mailing-address and 14 SEC.

`road_purchase_stream` extends it to transactions: **19,688** purchases in the stream, the newest from Mecklenburg County NC on **2026-11-02** with county, parcel id, situs address, buyer entity, the buyer's own home count, the group, the group status and a signal string, so a single purchase can be read as `BUYER_ENTITY_UNDER_350` inside a `COVERED` group. That is the exact case the 350 test was written around, returned as a field.

**One inconsistency recorded rather than smoothed:** `road_monitor_summary` reports **43** covered groups while `rule_coverage` on `ROAD-1001` returns a count of **64** items and lists 64 of them. Two different definitions in two tools on one server, and a caller who quotes one without naming which will be wrong by twenty-one groups.

## Private credit: what two lenders say the same loan is worth

`credit_disagreements` is the strongest table in the whole surface. It is dated **2026-06-30**, covers **2,189** companies held by **2 or more** managers, and returns **71** where the marks differ by ten points or more, with the source named as BDC schedules of investments, first-lien term loans, fully funded, cost 85 to 110 percent of par.

The first row: **Assembly Intermediate LLC**, an **80.2** point gap, lowest mark **0.198** (Goldman) against highest **1.000** (Morgan Stanley) on **$53,825,000** of par across two funds. The second: **Norvax LLC**, **69** points, **0.1651** against **0.855** across three funds, par **$4,366,000**. Check the gap: 0.855 minus 0.1651 is 0.6899, which is **69** points to the nearest whole. `lender_marks` on the same company returns the fund-level rows underneath (Blue Owl Capital Corp at **0.1649** and **0.1651**, Midcap Financial at **0.855**), the **2029-08-05** maturity, and a backtest sentence with its own numbers: lenders sitting ten to twenty points above the lowest other manager cut their own mark by five or more points the next quarter **20.4%** of the time, against **2.8%** when they agreed.

`credit_q3_cuts` shows the same table moving: dated **2026-09-30**, **123** funds filed, last filing **2026-11-13**, **209** cuts of five points or more. The largest is **Wash And Wax Holdings LLC**, from **0.9514** to **0.1684**, which is **-78.3** points, and the arithmetic is the subtraction. `contractor_credit_watch` then joins marks to federal money: of **202** contractors, **28** are stressed and carry **$6,748,062,967** of federal FY2025 obligations, with a private-only cut of the same population at **150** contractors and **19** stressed.

## Federal exposure: the banned-vendor question, with the method attached

`exposure_summary` is dated **2026-11-13T11:32:16Z** and opens with the method rather than the answer: a paper counts only when Europe PMC finds the vendor in its methods, results, figures, tables, supplement or acknowledgements and a sentence names it; engineering and physical-science papers come from the OpenAlex full text; **author affiliations and reference lists never count**; grant numbers are matched exactly to USAspending FAINs. The tiers are named (broad, and the narrower one), which is the difference between a screen and a rumour.

`perf_summary` is dated **2026-11-06T03:54:03** and names its own inputs by file and date: USAspending award archive FY2025 and FY2026 with FY2027 to date, DOL EFAST2 Form 5500 and 5500-SF bulk filings received 2024 to 2025, FSRS subawards, and **13 CFR 121.201** size standards from the eCFR API on **2026-10-30**. Its capacity method divides set-aside obligations by the prime's own active participants on its largest Form 5500 plan, with the exclusion list spelled out (**D?1x** as-a-Service, **V2xx** travel, construction and specialty-trade NAICS).

`who_owns_home` answers the property question or says it cannot: **1 Infinite Loop, 95014** came back `covered: false` with the note *Outside the counties covered so far*, which is the honest version of a **17-county** coverage limit rather than a zero that reads as *no owner*.

## The refusals, which is why this one is quotable

Four failure paths were driven and each answered as a failure rather than as a guess:

- `idr_offer` with `code: 11` refused: **code must be a CPT or HCPCS code, e.g. 99284, 99285, 36415, A0427.** The code space was validated, not coerced.
- `erate_deadline_check` on BEN **16012345** returned *No funded E-Rate requests from funding year 2023 on, and no Category 2 budget*, rather than a deadline for a nonexistent applicant.
- `perf_firm` on **Booz Allen Hamilton** returned `found: false` with *Not a set-aside recipient with $250K+ in FY2025-27 to date*, which is a scope statement and not a claim that the company does not exist.
- `get_dataset_sample` on **private-credit-marks** returned `isError: true` and *has no public sample file yet* instead of an empty sample that would read as a dataset with no rows.

## Where the surface is thin, measured rather than assumed

`aircraft_owner` with `owner: APPLE` returned **13** rows and every one was a substring match: **APPLEBEE AVIATION INC**, **APPLE REALTY GROUP INC**, and other names that merely contain the four letters. The FAA lookup is a name search, not an entity resolution, so pin it with an N-number when the question is *does Apple own an aircraft*. `exposure_awards` with `q: BGI` returned **0** rows across every counter, which is a naming problem rather than an absence, and the same tool accepts a `vendor` argument for exactly that reason.

`idr_scorecard` is a market table rather than a lookup: CMS Federal IDR Public Use File **2025 Q4**, altered and aggregated by Tensorust and labelled as such. FHAS carries **135,347** disputes at a **525** dollar single fee, a **77.5%** provider win rate on disputes, a median prevailing multiple of **3.72**, a **20** day median and **$61,454,979** of fees in the quarter; PRI carries **60,796** disputes at **518** dollars, a **94.3%** win rate, **4.43** and **47** days. The fee totals are the vendor's arithmetic on a two-sided fee model and are not reproducible from the dispute count alone, so they are quoted as the server's figure.

## Limits

The property layer covers **17 large counties** and says so at the point of failure rather than in a footnote. The ontology is US-only. The free tier truncates to samples and row limits, so a full export is a paid dataset product, and the offers sit on the same host. Coverage dates differ per table (June 30 for marks, September 30 for cuts, November 6 and November 13 for the exposure and performance builds), so two answers from two tools are two vintages and should be labelled that way.

## FAQ

### Does it need a key?

No. `initialize`, `tools/list` and the read tools answered without one, with sample rows and row limits. A bearer key raises the limits, and the dataset catalogue on the same host sells the full extracts.

### What makes it different from a search engine?

The join and the date. A search returns a page about a company; this returns the control group, the federal awards, the FCC licences, the private-credit marks and the rules that apply, from one key, with the build date of each table printed in the answer.

### Can I rely on the ROAD Act numbers?

The statute, effective date, threshold and penalty are quoted with citations you can check, and `over_threshold_by` reconciles by subtraction against the stated threshold. The one number to watch is the covered-group count, because `road_monitor_summary` says 43 and `rule_coverage` says 64, so name the tool you are quoting.

### Where does this fit a business?

Procurement screening, credit and valuation checks, real-estate acquisition diligence, and the regulatory answer to *is this investor already over the line* are the four places this beats a chat answer. It is the first entry in this catalog for all four.

## Related reading

- [External MCP server catalog](/hermes/mcp/servers/external/) for the rest of the servers evaluated and catalogued here
- [CorpusIQ connectors](https://corpusiq.io/connectors) for the read-only business systems this catalog is built around
