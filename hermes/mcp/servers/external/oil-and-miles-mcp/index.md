---
title: "Oil & Miles MCP - Repair Costs Before the Quote Lands"
description: "Free keyless car data: OBD-II meanings, the coolant the owner's manual names, repair ranges at an independent shop and a dealer, warranty extensions."
category: "Data & Analytics"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-25
source: "Submission chatmcp/mcpso #8063 filed 2026-11-25T12:56:24Z; registry record io.github.oilandmiles/oil-and-miles 1.0.0 with the remote https://oilandmiles.com/api/mcp; keyless initialize and a six-tool tools/list read 2026-11-25; get_trouble_code, list_trouble_codes, get_repair_cost, list_repair_cost_jobs, get_coolant_spec and find_warranty_coverage driven the same day; vendor rate limit 60 requests a minute published by the submitter"
relevance: "★★★"
tags: [automotive, obd-ii, repair-costs, warranty, coolant, cc-by, remote-mcp]
last_updated: "2026-11-25"
---

# Oil & Miles MCP

**A dashboard light and a repair estimate are two facts a driver is asked to accept without a second opinion.** Oil & Miles publishes the second opinion: what an OBD-II code means in plain words, what it does not prove, which coolant the car's own owner's manual names, and what a repair costs at an independent shop against a dealer, per car, in US dollars. It is keyless, read-only, licensed CC BY 4.0, and every answer links the page it came from.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://oilandmiles.com/api/mcp
Auth:        none, no key and no account
Registry:    io.github.oilandmiles/oil-and-miles 1.0.0
Pricing:     free, read-only, CC BY 4.0 with attribution
Rate limit:  60 requests a minute per client, as published by the submitter
Tools:       6, read from a keyless tools/list
```

The `instructions` string is a single paragraph and it sets the boundary the tool keeps: *"Read-only car repair facts from Oil & Miles: OBD-II trouble code meanings, the coolant each car's owner's manual names, repair cost ranges per car (independent shop and dealer, US dollars), and carmaker warranty extensions. Every answer links the page it comes from."* Nothing is written, nothing is booked, and there is no account to create before the first question.

## The six tools

| Tool | What it needs | What it answers |
| --- | --- | --- |
| `get_trouble_code` | `code` | meaning, what the computer saw, what gets checked first, what the code cannot prove |
| `list_trouble_codes` | nothing | all **21** codes with a page, read this pass |
| `get_coolant_spec` | `make`, optional `model`, `year` | the coolant the owner's manual names, and the manual |
| `list_repair_cost_jobs` | nothing | the jobs with per-car ranges and how many cars each covers |
| `get_repair_cost` | `job` | parts and labour per car, independent shop against dealer |
| `find_warranty_coverage` | `make`, optional `model`, `year` | extensions and special coverage programmes by cause |

## A code, explained past the headline

`get_trouble_code` on **P0420** returns the layered answer: official name *Catalyst System Efficiency Below Threshold Bank 1*, the plain reading **bank 1 converter reads weak**, the area *auxiliary emission controls*, the family *catalyst*, and the related code **P0430**. Then the three fields that separate this from a code list.

- **What the computer saw:** *"The engine computer swung the fuel mixture rich and lean, and the oxygen sensor after the bank 1 converter started to mirror the one before it."*
- **What gets checked:** *"Whether the oxygen sensor after the converter stays flat while the one before it swings."*
- **What it does not prove:** *"It doesn't prove the converter is bad. An exhaust leak or the engine's software can set the code with nothing wrong inside it."*

That third field is the whole reason to use this endpoint. A converter replacement is one of the expensive repairs a code can be blamed for, and the record says in the vendor's own words that the code is a symptom, naming two cheaper causes first. The code's name is sourced to *FCA bulletin 08-054-25*, and the list of **21** codes this pass spans fuel trim (P0171, P0172, P0174), misfires (P0300 to P0305), EVAP (P0440, P0443, P0446, P0455, P0456), EGR (P0401), catalyst (P0420, P0430), sensors (P0102, P0113), turbo underboost (P0299) and output speed (P0720).

## Independent shop against dealer, per car

`list_repair_cost_jobs` reports **six** jobs with a car count each: **fuel pump 10 cars**, **wheel bearing 9**, **timing belt 6**, and **ABS sensor, blend door, brake pad and rotor 2 each**. Two cars is thin, and the tool says so through the data rather than a disclaimer.

`get_repair_cost` for **brake pad and rotor replacement** returns one range per car, never a blended one:

| Vehicle | Independent shop | Dealer | Dealer markup at the low end |
| --- | --- | --- | --- |
| 2025 Subaru Crosstrek 2.0 | $391 to $488 | $530 to $565 | $139, or 35.5% above $391 |
| 2021 Chevrolet Silverado 2500HD 6.6 | $415 to $690 | $768 to $844 | $353, or 85.1% above $415 |

Those percentages are arithmetic on the returned figures, not new data: `(530 - 391) / 391 = 35.5%` and `(768 - 415) / 415 = 85.1%`. The spread is the story. On the Crosstrek the dealer is a modest premium; on the Silverado the dealer's *floor* sits $78 above the independent shop's *ceiling*, and the independent range is four times wider (a **275** dollar spread against **76**), which is what you would expect from a heavy-duty truck where parts choice moves the price more than labour does.

### Why the headline range is not the job's range

The response carries a `headline` of **$391 to $565** and, in the same payload, a `note`: *"Parts and labor per car, as the page shows them. Each car has its own range, never one across cars."* The two do not agree. The headline low is the Crosstrek's independent floor and the headline high is the Crosstrek's dealer ceiling, so it describes **one** car while the Silverado in the same response reaches **$844**. Read the per-car rows and ignore the headline; the note is honest about the intent and the field quietly contradicts it.

## The coolant the manual actually names

`get_coolant_spec` for **Honda** returned three cars, each citing its own manual: **2016 Pilot**, **2017 CR-V** and **2018 Accord**, all **Honda Long Life Type 2, 50/50**, sourced to *Honda 2016 Pilot Owner's Manual*, *Honda 2017 CR-V Owner's Manual* and *Honda 2018 Accord Owner's Manual* respectively. That is the right shape for this question, because coolant specification is a per-manual fact and mixing the wrong type is how a water pump fails early.

The same call for **Toyota Camry 2019** failed honestly: `isError: true` with *"No owner's manual entry for this car yet."*, plus a link to the vendor's article on choosing coolant. **Three Honda cars is the entire Honda coverage**, so treat this tool as a lookup that frequently has no row rather than a coolant database. The registry description advertises coolant specs generally; what arrived on the two makes tested was three entries and one honest miss.

### Which repairs a carmaker quietly extended

`find_warranty_coverage` for **Honda** returns programmes by cause rather than a warranty table. The first is a **powertrain warranty extension** for **oil dilution**, effective **5 April 2019**, term **6 years** with no mileage cap in the record, covering **2017 to 2018 CR-V** and **2016 to 2018 Civic**, both the 1.5 litre turbo. A second entry covers **head gasket** with an end date of **31 May 2027** across **2017 CR-V**, **2016 to 2017 Civic** and **2017 Civic Si**, and a third extends CR-V coverage from **2017 to 2026** including the hybrid from 2020.

This is the field where an owner finds money: a six-year extension on oil dilution is a repair that would otherwise be quoted as customer-pay, and the record names the cause and the start date so a service adviser can be met with a specific question.

## Limits measured this pass

- The coolant tool covered three Honda cars and had no row for a 2019 Toyota Camry. Coverage is the constraint, not the interface.
- The `headline` range on `get_repair_cost` describes only the first car in the list while the response contains a second car above it. Read the per-car rows.
- Make, model and year come back lowercased in the data (`honda`, `crv`) while the source strings are properly cased (*Honda 2018 Accord Owner's Manual*). Display the source string, not the key.
- Two cars per job is the thin end of a sample. A single dealer quote from a second shop is still the check that matters before money moves.

## See also

- [CarChat Inventory MCP](/hermes/mcp/servers/external/carchat-inventory-mcp/) for live US dealership inventory and market price.
- [Dutch Vehicle Context MCP](/hermes/mcp/servers/external/dutch-vehicle-context/) for registration and MOT history from Dutch official registers.
- [External MCP Server Catalog](/hermes/mcp/servers/external/) for the full index.
