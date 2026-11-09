---
title: "StandbyBrief MCP - CMS Citation Leads for Contractors"
description: "Nursing homes CMS cited for generator, sprinkler or fire-alarm faults near a ZIP, ranked for the contractors who fix them."
category: Business Development
stars: "n/a (hosted; OAuth 2.1, 14-day trial from the consent screen)"
added: 2026-11-09
source: "chatmcp/mcpso submission #6972 filed 2026-11-09T06:20:03Z; the official MCP registry record com.standbybrief/standbybrief 1.0.0; the protected-resource and authorization-server documents; and the endpoints themselves, where app.standbybrief.com answers 401 with a protected-resource pointer while the published apex route still serves the parent company page"
relevance: ★★★
tags: [sales, lead-generation, healthcare, facilities, generators, fire-safety, government-data, remote-mcp]
last_updated: "2026-11-09"
---

# StandbyBrief MCP

**A generator dealer sells a thirty-thousand-dollar machine to a nursing home that has just been cited for not having a working one. The citation is public, dated and already in CMS's inspection file, and the dealer finds out months later from a competitor's win.** StandbyBrief turns that file into a ranked list of cited facilities around a ZIP, for the three trades that fix the fault.

```text
Server type: Remote (Streamable HTTP)
Endpoint:    https://standbybrief.com/mcp  (published)
             https://app.standbybrief.com/mcp  (answers the MCP handshake today)
Auth:        OAuth 2.1, authorization code with PKCE, DCR and Client ID Metadata Documents
Tools:       6, read-only
Registry:    com.standbybrief/standbybrief 1.0.0
Trial:       14 days, started from the consent screen, no card
```

## What the endpoints say about themselves

A keyless `initialize` is refused with a pointer rather than a login page:

```text
POST https://app.standbybrief.com/mcp   ->   401
www-authenticate: Bearer resource_metadata="https://standbybrief.com/.well-known/oauth-protected-resource/mcp"
{"jsonrpc":"2.0","id":null,"error":{"code":-32001,"message":"Bearer token required"}}
```

The metadata documents are served from the app host and describe the apex as the resource: `https://standbybrief.com/mcp`, scope `standbybrief`, a `registration_endpoint` for dynamic client registration, `S256` as the only challenge method and the documentation URL. One routing caveat is measured rather than assumed: at the time of this pass the apex `/mcp` route answers with the parent company's website rather than an MCP handshake, so a client configured with the published URL does not connect today. The app host accepts the handshake and returns the OAuth challenge, which is why it appears as the endpoint line above. Check the published route before reporting a broken connector, and check the app route before reporting a dead one.

That is the tier this entry rests on: **live, gated, documented by the vendor, not driven.** No tool list is visible behind the 401.

## The six tools

| Tool | What it answers |
|---|---|
| `find_cited_nursing_homes` | Facilities near a ZIP, city or address cited under the emergency-power rule (K918) or the sprinkler and fire-alarm rules (K353, K345), ranked. |
| `get_nursing_home_citations` | Every citation on one facility, with CMS's wording and survey details. |
| `explain_citation_tag` | What a tag code means and what an inspector was looking at. |
| `get_data_freshness` | The publication date of the CMS file behind the answer. |
| `get_export_links` | Download links, on paid plans. |
| `get_account_status` | Trial or plan state and the billing path. |

Each row carries the citation tag, CMS's own wording, the survey date, scope and severity, the correction status, the correction date, distance and a link to the CMS record.

## Why three trades and one tag code

The three codes are not decoration. **K918** is the emergency-power rule, which in practice means a generator that did not carry the load, was never tested or could not be shown to start. **K353** and **K345** are the sprinkler and fire-alarm rules. A generator dealer, a sprinkler contractor and a fire-alarm company each read one slice of the same citation, and each one is a purchase.

The mechanism worth understanding is that a citation has a correction date. A facility cited in the last survey cycle with an open correction is a facility under a deadline, and a deadline somebody has to spend money to meet is the cleanest sales signal in facilities work. An assistant asked about that market without this connector returns a general paragraph about the nursing-home sector. With it, the same question returns facilities by distance with the tag, the date and CMS's wording attached.

## The class it enters, with the owners named

The catalogue already carries the pattern this belongs to: [Awardlanes](/hermes/mcp/servers/external/awardlanes-mcp/) does it for USDA freight lanes in a broker's territory, and [SpendQuery](/hermes/mcp/servers/external/spendquery-mcp/) does it for federal contracting. StandbyBrief is the third form of the same discipline, a single public file reshaped into a ranked list for one trade, and the file is CMS's fire-safety inspection data rather than procurement. Nothing here covers healthcare facilities: the vertical owners are elsewhere, [Plain Freight](/hermes/mcp/servers/external/plainfreight-mcp/) on freight and [AllClear Lending](/hermes/mcp/servers/external/allclear-lending-mcp/) on commercial credit. The sibling published by the same company in this window, erateradar on USAC E-rate bids, is the same pattern applied to schools and libraries and is held in the sweep report until its published route answers.

## Limits, stated as limits

One country, one file, one building type. Read-only, so no way to log a visit or a contact inside the connector, and the export is behind a paid plan. It ranks what CMS cited, which is a record of a past inspection rather than a prediction, and a facility that fixed the fault last month still appears until the next survey updates the file, which is why `get_data_freshness` exists as its own tool.

## Frequently asked questions

### Which facilities can an assistant see?

Nursing homes CMS cited under K918, K353 or K345, filtered by distance from a ZIP, city or address, with the citation wording, survey date, scope and severity, correction status and the CMS record link on every row. The ranking is the vendor's, and the underlying facts are CMS's.

### Is it read-only?

Yes. All six tools read. There is no write path, no outreach and no CRM inside the connector, so connecting it to an assistant cannot change anything at the facility or in the file.

### How is this different from reading the CMS file myself?

The file is public and can be downloaded. What the connector supplies is the join and the ranking: the citation parsed to a tag, the tag explained, the distance computed from a place rather than a county, and the correction window presented as a filter. That is an hour of spreadsheet work per question, which is why the product exists.

### Does it need a paid plan?

The trial runs 14 days from the consent screen with no card. Export links are listed as a paid-plan tool, so a user who wants the list out of the chat should check `get_account_status` before building a workflow around it.
