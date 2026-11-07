---
title: "CarbonMeld MCP - Carbon Credits From Their Documents"
description: "Hosted MCP over 34,421 carbon projects: document-based quality scores, registry red flags, vintages, CORSIA labels and offer checks, read only."
category: "Compliance"
stars: n/a (Premium account required, EUR 9 + VAT a month)
added: "2026-11-06"
source: "mcpservers.org twelve-sitemap addition carbonmeld-com; the vendor pages at carbonmeld.com/premium/mcp/ and /premium/, llms.txt and /data/stats.json; the protected-resource document at carbonmeld.com/.well-known/oauth-protected-resource/api/v1/mcp; and a keyless initialize of carbonmeld.com/api/v1/mcp answering 401"
relevance: ★★★
tags: [carbon-credits, carbon-markets, esg, offsetting, registries, due-diligence, corsia, icvcm-ccp, oauth, remote, read-only]
last_updated: "2026-11-06"
---

# CarbonMeld MCP

**Buying a carbon credit is the last major business purchase where the buyer cannot look up the asset.** A tonne is a claim attached to a project document in a registry, and the document that decides whether the claim holds usually sits behind a registry search box in another language. CarbonMeld indexes those documents and scores them. This server puts the resulting records in front of an assistant, read only, so a due-diligence conversation can be about the evidence rather than about the brochure.

```
Server type:   Remote, Streamable HTTP
Endpoint:      https://carbonmeld.com/api/v1/mcp
Transport:     JSON-RPC 2.0 over HTTP POST, JSON responses; GET returns 405
Auth:          OAuth sign-in from the client (dynamic registration, no client
               secret) or an API key as a Bearer token
Scope:         carbonmeld.read, and nothing that writes
Protocol:      2025-06-18
Tools:         15, all read only
Coverage:      34,421 projects, 30 registries, 12 marketplaces
               (export 2026-11-07T03:30:28Z)
Method:        scoring methodology v2.2
Pricing:       Premium EUR 9 + VAT a month, Pro EUR 49 + VAT a month
```

**Evidence tier: documented, not driven.** A keyless `initialize` at the endpoint answers HTTP **401** with `{"error":"Missing or invalid API key."}` and a `WWW-Authenticate` header naming its protected-resource document, `https://carbonmeld.com/.well-known/oauth-protected-resource/api/v1/mcp`. That document, read directly, confirms the shape: resource `https://carbonmeld.com/api/v1/mcp`, authorization server `https://carbonmeld.com`, one scope `carbonmeld.read`, bearer in the header. The fifteen tools, their inputs and the quota rules below are read from the vendor's own MCP page, and the coverage figures are read from `carbonmeld.com/data/stats.json`, which is machine-addressable and live. No session was driven because every record past the public summary needs a Premium account, and there is no account on this machine.

One design note worth stating before the tool list: the handler runs no language model. It returns records and the client's assistant does the interpreting, which is the honest architecture for a due-diligence surface. A vendor that summarised the evidence itself would be asking the buyer to trust a second summary of the first.

## The tools

| Tool | What it answers |
| --- | --- |
| `search_projects` | Search by words, standard, registry, country, methodology, sector, scoring sector, developer, analysis status, minimum score or claim tag, sorted by rating or name; returns the total and one page, with `next_offset` when more remain |
| `get_project` | One full project record by slug or registry code: analysis, red flags, vintages, claims, the document links, the project page's notices as printed, similar projects and the PDF report's address |
| `get_projects` | The same record for 1 to 10 ids in one call, in the ids' order, with a per-id error where one fails |
| `check_offer` | Compare pasted offer text against recorded registration, vintages, quantities, claims and developer |
| `corsia_supply` | CORSIA registry labels by registry and phase, the highest-rated First Phase projects and each registry's average rating |
| `get_buyer` | Public retirement records for an organisation: tonnes, retirements, the quality of what it retired, the projects and each project's current rating |
| `get_developer` | A developer's project count, rated count, projects with a registry red flag, standards, countries and project list |
| `get_methodology`, `get_standard`, `get_ranking` | The catalogue behind the records: one methodology's identity card and rules, one standard's programme rules, and the leaderboards by sector, country, standard or methodology |
| `get_method` | The scoring method itself: its sections, its version, and every rule by id with its sentence, status, effect, figure and values |
| `ccp_tracker` | The ICVCM CCP tracker as the site shows it: methodology assessments by status, and the number of projects tracked under each code |
| `my_portfolio` | The projects you saved, their ratings and four dimension scores, red flags, vintages, listings, the average rating and the change alerts of the last 30 days. Uses none of the daily project quota |
| `what_changed` | The last 30 days of official rule-setter notices (ICVCM, Verra, Gold Standard, SBTi and others) and registry labels added or removed |
| `search_articles` | CarbonMeld's own analysis in English, Chinese or Japanese, by words, tag or date |

`get_method` is the unusual one and the reason this dataset can be argued with. A score is only useful if the rule that produced it can be read, and here the ruleset is a queryable surface with rule ids, versions and the pages that apply each rule.

## What is free and what is not

The free tier is a real summary, not a teaser of nothing: the overall quality score when one exists, the analysis summary, the number of red flags, marketplace listings and vintage data, the CORSIA registry-label directory, and public buyer profiles. Premium adds the per-dimension scores, the full red-flag text and risk indicators, the factor detail, the curated registry documents, the extended description, the PDF due-diligence reports, the API and this MCP server, a portfolio of 20 saved projects with change alerts, and 20 offer checks a day.

The commercial line matters if an assistant is going to do the reading rather than the buyer:

| Plan | Price | Different projects a day | API requests a day |
| --- | --- | --- | --- |
| Premium | EUR 9 + VAT a month, or USD 9 for one 30-day crypto payment | 30 | 300 |
| Pro | EUR 49 + VAT a month, or USD 49 for one 30-day crypto payment | 300 | 1,000 |

Both counts are shared across the website, the PDF reports, the REST API and MCP, and reopening a project on the same day counts once. The counter that bites an agent is the project quota rather than the request quota: `search_projects` is free of it, `get_project` spends one per project not already opened today, and `get_projects` spends one per record returned, so a careless batch of ten can burn a third of a Premium day. A burst limit of **120 requests a minute per IP** sits on top, daily counters reset at **00:00 UTC**, and a failed call still counts as a request.

## The boundaries the vendor draws

These are printed by CarbonMeld about its own product, and they are the right way to use it:

- **Document-based screening, not verified impact.** A score is a reading of registry documents and published methodology, not a measurement of tonnes avoided.
- **Not investment advice and not certification.** No endorsement, no rating agency role.
- **A retirement beneficiary is not necessarily the purchaser.** `get_buyer` returns public retirement records, and the vendor says ambiguous names need clarification rather than a guess.
- **CORSIA balances are unretired units of every vintage, not CORSIA-eligible units.** A registry's supply figure is not an eligibility claim.
- **The CCP tracker counts projects under a methodology code, not CCP-labelled credits**, and it counts every version.
- **There is no company-level score for a developer**, and 16,591 of the indexed projects are queued rather than assessed, so a missing score is a state and not a verdict.
- **Scores withdrawn for review are not shown**, and a score computed under method v2.1 or earlier stays visible with its analysis date and a `rescore_pending` status instead of being silently refreshed.

## Can an assistant buy or retire a credit with this server?

No. Every tool is read only, the scope is `carbonmeld.read`, and the vendor states the handler reads records and does not issue, buy or transfer carbon credits. `check_offer` compares an offer's text against the recorded registration, vintages and claims, which is a screening step before a purchase, not the purchase.

## What does a CarbonMeld score measure?

The project's registry documents against a published method, and nothing else. The method is queryable by rule id, the analysis carries its date and version, and the vendor labels the output screening signals rather than verified impact, investment advice or certification. A project with no score is usually one of the 16,591 queued for assessment rather than a project that failed one.

## Does it work without a Premium account?

Partly. The free tier returns the overall score, the analysis summary, the red-flag count, listings and vintages, so a public question can be answered. The MCP server itself, the per-dimension scores, the red-flag text, the documents and the portfolio are Premium, and every call past the public summary needs the account.

## Connecting it

Claude, ChatGPT, Claude Code, Cursor, VS Code and Microsoft 365 Copilot agents all connect with a sign-in rather than a pasted key: register the client dynamically, then approve the connection on a CarbonMeld page. The same URL serves the API-key route for any client that can set a static header:

```json
{
  "mcpServers": {
    "carbonmeld": {
      "type": "http",
      "url": "https://carbonmeld.com/api/v1/mcp",
      "headers": { "Authorization": "Bearer ${CARBONMELD_API_KEY}" }
    }
  }
}
```

All connected assistants share one daily request limit, and each one can be disconnected from the account page, which ends access at once without invalidating the key. Le Chat is listed as not yet supported.

## Why it earns a guide

Because the catalogue could account for carbon but could not buy it. **GreenCalculus** is the neighbour and the contrast: it looks up emission factors and calculates activity, electricity, freight, travel and financed emissions, each value carrying its source cell and a pinned data version, which answers how much a company emits. Nothing here answered what the offset market actually contains: which registry holds the project, what the project document says, whether the registry has flagged it, which marketplace lists it and at what vintage, which labels it carries, and who has already retired units from it.

That gap is the difference between a sustainability report and a procurement decision. An operator under a buyer's due-diligence questionnaire is asked for the registry, the vintage, the methodology code and the retirement evidence, and until now the assistant could only help draft the question. The `check_offer` tool is the shape to hold on to as well: paste the text of an offer a broker sent and get it compared against the recorded registration, vintages and claims, which is the one control a small buyer has against a resold or mislabelled credit.
