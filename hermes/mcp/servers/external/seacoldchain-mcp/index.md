---
title: "SEA Cold Chain MCP - Cold Storage Totals With a Floor"
description: "Keyless market totals for cold storage in seven Southeast Asian markets: operating sites, pallet positions as a floor, and the register's coverage share."
category: "Logistics"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-26
source: "mcpservers.org canonical arrival /servers/seacoldchain-com-method in the November 26 midday wave; official registry `com.seacoldchain/markets`; keyless initialize 200 as `sea-cold-chain-markets` 1.0.0 on https://seacoldchain.com/mcp with a 3-tool tools/list and five tools/call requests driven on 2026-11-26 (list_markets, market_totals on Vietnam, Thailand, Indonesia and Singapore, market_totals on a bogus market, method)"
relevance: "★★"
tags: [logistics, cold-chain, market-data, southeast-asia, keyless, citations, remote-mcp]
last_updated: "2026-11-26"
---

# SEA Cold Chain MCP

**A pallet-position total is the number a supply-chain answer reaches for first, and it is the number most easily overstated.** A model asked for cold storage capacity in Vietnam will produce a figure with no date, no coverage share and no statement of what it counts. This server answers with a dated total, the count of buildings behind it, the share of the market its own triangulated estimate says it holds, and a citation line it tells the client to keep. It covers seven Southeast Asian markets, it needs no key, and its three tools are small enough to read in one sitting.

```
Server type:  Remote (Streamable HTTP)
Endpoint:     https://seacoldchain.com/mcp      keyless, no account
Registry:     com.seacoldchain/markets
Server name:  sea-cold-chain-markets 1.0.0
              title "SEA Cold Chain market totals"
Tools:        3, read from a keyless tools/list and all three driven
Model:        market aggregates only; the site-level register is sold per market
```

`initialize` answers **200** with an `instructions` block that is unusually honest for a market-data server, and it tells the client exactly what to do:

> Call list_markets first, then market_totals for one market. Pallet positions are a floor (the capacity of the sites held), not a market size: say so, quote the coverage share, and keep the citation line and the as-of date with any figure you repeat.

That paragraph is the whole contract. A client that ignores it will quote 1,457,000 pallet positions for Vietnam as if it were the national stock, when the payload itself says `at_least` and states the coverage share beside it.

## The three tools

| Tool | Arguments | What comes back |
| --- | --- | --- |
| `list_markets` | none | each covered market with its operating site count, `as_of` date, market page and quarter page |
| `market_totals` | `market` | operating sites, pipeline sites, `pallet_positions_at_least`, `stated_share_pct`, `investment_grade_buildings`, `coverage_pct` with a note, a one-line headline, a citation line |
| `method` | none | the full method page as text: what is counted, source order, provenance, capacity conversion, tiers, refresh cadence |

## Seven markets, four read in full

`list_markets` on 2026-11-26 returned seven markets and one not-published market:

| Market | Code | Operating sites | As of |
| --- | --- | --- | --- |
| Thailand | TH | 551 | 2026-11-26 |
| Philippines | PH | 246 | 2026-11-26 |
| Indonesia | ID | 184 | 2026-11-26 |
| Vietnam | VN | 166 | 2026-11-23 |
| Singapore | SG | 63 | 2026-11-26 |
| Malaysia | MY | 51 | 2026-11-26 |
| Cambodia | KH | 25 | 2026-11-23 |

**Lao PDR is listed under `not_published`**, with the rule stated: a market holding fewer than three operating sites has no public figure, because a total over one or two buildings would identify them. That is the privacy rule working in the open, and it is why the register says market aggregates only.

`market_totals` was then driven on four markets:

| Market | Pallet positions (floor) | Stated share | Coverage | Investment-grade | Pipeline |
| --- | --- | --- | --- | --- | --- |
| Thailand | 1,487,000 | 42% | 81% | 175 | under 3 |
| Vietnam | 1,457,000 | 74% | 98% | 110 | 8 |
| Indonesia | 515,000 | 34% | 21% | 54 | 5 |
| Singapore | 403,000 | 69% | 53% | 33 | 4 |

Thailand is the market worth putting in front of a client, because the two percentages disagree in a way that reads wrong until you understand them. **`stated_share_pct` 42 and `coverage_pct` 81 are not the same measurement.** The first is the share of the market the register's own count supports as a stated figure; the second is the share of the market's capacity, on its triangulated estimate, that the register holds at all. A summary that collapses them into "42% of the Thai market" is wrong, and a summary that says "81%" without printing what it measures is worse.

## The conversion, reproduced

The method tool states the capacity unit conversion: **6.65 cubic metres per pallet position**. Thailand's floor of 1,487,000 pallet positions is therefore about 9,888,550 cubic metres of cold space, and Vietnam's 1,457,000 is about 9,689,050. Both figures are floors for the reason the instructions give: an estimate counts at the low end of its range, so the total is the capacity of the buildings held, never the size of the market.

The method page also carries the parts that make the numbers auditable:

- **What is counted:** buildings that hold goods under refrigeration, whether for their owner or for customers. One row is one building. Market stalls and shop cold rooms are excluded.
- **Pipeline:** sites under construction or planned are held separately and never added to operating stock. Closed buildings leave the count.
- **Source order:** dated registers and filings before descriptions in prose, and a more recent stated figure replaces an older one.
- **Provenance:** every value carries its own record, marked stated by a named source, estimated with its method, or ruled.
- **Tiers:** T1 is Large or Mega at Grade A, T2 Medium and above at Grade A or B, T3 smaller or older at Grade B or C, T4 small at Grade C. Investment-grade means T1 or T2.
- **Refresh:** each site is due a re-check within 90 days of its last one.
- **Quarters:** each market has a dated figure per quarter, fixed when the quarter closes, at `/markets/<country>/<yyyy-qN>`.

## What a wrong argument gets

`market_totals` with `market: "atlantis"` returned **HTTP 200 with `isError: true`** and a sentence naming the seven covered markets rather than a stack trace. A refusal that lists the valid values is the shape that lets an agent retry correctly on the next call, and it costs nothing.

## Two shape defects, measured

1. **`pipeline_sites` is `null` for Thailand while the headline says "fewer than 3 sites under construction or planned".** The tool knows the number is suppressed by the small-group rule, but it returns `null` with no `nullReason`, so a client rendering the structured field shows blank where the prose field shows a fact. Every other market read returned an integer.
2. **`as_of` is per market, not per response.** Vietnam and Cambodia were dated 2026-11-23 while the other five were dated 2026-11-26, so a multi-market answer built from one "as of today" claim is wrong by three days on two of the seven.

## What is not on this surface

The headline totals are the free, public layer. The **site-level register**, meaning each building with its operator, capacity, year opened, temperature regime, grade, tier and a source for every value, is sold per market and named only as a contact address in the payload. A client that needs a specific building, an operator or a competitor's portfolio has to buy that, and the tools should not be presented as if they return it.

## Where it fits a business-answer system

Cold-chain capacity is a supply question that turns up in food and pharma distribution, retail expansion and logistics procurement, and until now it was the kind answered from a consultant deck with no date on it. This server answers it as a dated, cited, coverage-qualified total, which is the shape a business-answer system can carry into a board pack without a caveat glued on. Pair it with a trade or customs source and it answers "can this market take our volume, and who already holds the space" rather than just "how many buildings are there".

## Is cold storage capacity the same as market size?

No, and the server says so itself. Pallet positions are the capacity of the buildings the register holds, printed as a floor, and the coverage share beside them says how much of the estimated market that is. Indonesia at 21% coverage and Vietnam at 98% are not comparable totals; they are comparable counts of what one register has documented.

## Does it need an account or a key?

No. `initialize`, `tools/list` and all three tool calls answered without any credential on 2026-11-26, and the only gated material is the site-level register, which is a commercial product sold per market.

## How do I cite a figure from it?

Use the `citation` line the payload returns, for example *Source: SEA Cold Chain, seacoldchain.com/markets/vietnam/2026-q4, as of 2026-11-23*, and keep the `as_of` date with the number. The instructions ask for exactly that.

## Connecting it

Add `https://seacoldchain.com/mcp` as a remote MCP server in any client that speaks Streamable HTTP. No OAuth, no header, no key. Start with `list_markets`, then `market_totals` for one market, then `method` if the answer is going in front of someone who will ask how the number was made.

## See also

- [PlainFreight MCP](/hermes/mcp/servers/external/plainfreight-mcp/) for the freight side of the same question
- [Dataddo MCP](/hermes/mcp/servers/external/dataddo-data-to-ai-mcp/) for getting warehouse data out to an agent
- [External MCP server catalog](/hermes/mcp/servers/external/index.md) for the rest of the group
