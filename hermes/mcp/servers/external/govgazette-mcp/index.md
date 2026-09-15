---
title: "GovGazette MCP - Federal Contract and Award Intelligence"
description: "Hosted MCP for US federal procurement: search SAM.gov opportunities, awards and vendors, resolve identifiers, check exclusions, spot recompetes, and rank opportunities against a business profile. 39 tools live-probed, 19 usable without auth, OAuth unlocks saved searches and watches."
category: Compliance
stars: n/a (hosted)
added: 2026-08-25
source: mcpservers.org homepage
relevance: ★★★
tags: [mcp-server, procurement, government, sam-gov, federal-contracts, awards, recompete]
---

# GovGazette MCP

**A full federal procurement intelligence desk behind one MCP endpoint.** GovGazette serves US federal contract opportunities, awards, vendors, exclusions, and recompete signals through a hosted MCP server. It is the largest federal data surface found in this catalog class: 39 tools covering SAM.gov search, identifier resolution, reference data, extracted fact search, market summaries, and account-gated watches, all with source links and explicit evidence discipline.

```
Server type: Remote Streamable HTTP (hosted)
Endpoint: https://govgazette.com/mcp
Auth: None for 19 public tools; OAuth for saved searches, watches, and business-profile tools
Tools: 39 verified by live probe (19 public no-auth, 20 account/OAuth-gated)
Docs: govgazette.com/agents and govgazette.com/mcp
```

## Why This Matters for Operators

Government contracting is a data problem: opportunities scatter across SAM.gov, award history hides in multiple datasets, and recompetes go unnoticed until the incumbent wins again. GovGazette compresses the workflow into agent-native tools. `get_opportunity_brief` returns a bounded, source-backed decision brief with deadline status, fit signals, requirements, submission facts, and changes. `get_award_evidence` separates the official notice awardee from linked prior recipients without claiming an incumbent. `find_recompetes` surfaces awards whose period-of-performance dates suggest a recompete window, and the account-gated business-profile tools rank open opportunities against your confirmed profile with transparent reasons instead of win-probability guesses.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `search_opportunities` | Searches public opportunity data by text, classification, buyer, location, status, and dates |
| `get_opportunity` | Gets one SAM.gov opportunity by notice ID with GovGazette and official source links |
| `get_opportunity_brief` | Bounded, source-backed decision brief with deadline status, fit signals, requirements, and submission facts |
| `get_opportunity_extracted` | Exact citations, requirements, costs, dates, forms, and submission text extracted without an LLM |
| `search_extracted_facts` | Searches exact source-backed facts extracted from official opportunity descriptions |
| `get_opportunity_documents` | Lists parsed public SAM attachments and links to plain-text chunks |
| `get_opportunity_changes` | Sanitized immutable changes with separate source and detection times |
| `get_opportunity_comps` | Historical comparable public awards; not an independent cost estimate |
| `search_awards` / `get_award` | Searches and fetches records from the selected hot award dataset |
| `get_award_evidence` | Separates official awardee from linked prior recipients and market participants |
| `search_vendors` / `get_vendor` / `get_vendor_awards` | Public SAM entity search, UEI lookup, and award history |
| `resolve_identifier` | Resolves notice, solicitation, award, PIID, UEI, CAGE, NAICS, PSC, or FAR identifiers |
| `lookup_reference` | NAICS, PSC, FAR, SBA size-standard, set-aside, and agency reference data |
| `search_exclusions` | Checks the public exclusion snapshot by UEI or CAGE, or cautious name search |
| `find_recompetes` | Finds awards whose period-of-performance dates suggest a possible recompete |
| `get_market_summary` | Summarizes selected award and opportunity signals for a market slice |
| `search_opportunities_for_business` | Ranks open opportunities against the connected business profile with transparent reasons |
| `assess_opportunity_for_business` | Compares opportunity facts with the profile without claiming eligibility or win odds |
| `track_opportunity`, `watch_award`, `watch_vendor`, `save_recompete_radar` | Account-gated tracking, watches, and radars with alert cadences |

Account tools also include `get_watch_status`, `get_business_profile`, `get_business_defaults`, `get_business_awards`, `find_recompetes_for_business`, `get_business_market`, `check_business_exclusions`, plus save/update variants and a two-step `preview`/`apply_business_profile_update` flow.

## Installation

Connect directly; 19 tools work with no account:

```bash
claude mcp add --transport http govgazette https://govgazette.com/mcp
```

## Configuration

No credentials for public tools. For saved searches, tracked opportunities, watches, radars, and the business-profile ranking tools, connect a GovGazette account via OAuth from your MCP client. The vendor publishes an A2A surface (`govgazette.com/.webmcp/bridge.js`) for browser-based agents in addition to the MCP endpoint.

## Business Relevance

- **Pipeline building:** find and rank open opportunities against your capabilities profile.
- **Incumbent intelligence:** separate awardees from participants and spot recompete windows early.
- **Compliance screening:** exclusion lookups by UEI/CAGE before partnering on federal work.
- **Market analysis:** NAICS/PSC market summaries for go/no-go decisions.

## Integration with CorpusIQ

GovGazette's source-linked JSON output pairs well with CorpusIQ connectors for the business side of federal contracting: track pursuits in your CRM (HubSpot or Close via CorpusIQ), log award values in QuickBooks, and attach decision briefs to deal records so the pipeline and the evidence live in one place.

## Limitations

- Public tools are read-only; mutations require the connected account.
- Vendor states evidence discipline explicitly: exclusion checks are not compliance certifications, and recompete results are inferences, not confirmed solicitations.
- Account-gated tools require OAuth sign-in; anonymous enumeration of those surfaces is refused.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Acquisition.gov MCP - FAR Overhaul and Agency Deviations](/docs/hermes/mcp/servers/external/acquisition-gov-mcp)
- [SAM.gov MCP - Federal Procurement Data](/docs/hermes/mcp/servers/external/sam-gov-mcp)
- [GovTrade MCP](/docs/hermes/mcp/servers/external/govtrade-mcp)
