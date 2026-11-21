---
title: "Europe Instead MCP - Sourced European Software Alternatives"
description: "Five tools over a European software directory: an origin score out of 100 and a data exposure level from 1 to 5, each backed by a quote and a check date."
category: "Business Operations"
stars: n/a (vendor-hosted)
added: 2026-11-21
source: "chatmcp/mcpso submission #7765 filed 2026-11-21T12:38:36Z; the official MCP registry record com.europeinstead/europe-instead 1.0.0; keyless initialize and tools/list, then eleven tools/call requests on 2026-11-21"
relevance: ★★★★
tags: [procurement, europe, sovereignty, gdpr, vendor-selection, directory, remote-mcp, keyless]
last_updated: "2026-11-21"
---

# Europe Instead MCP

**Remote MCP server (Streamable HTTP, no authentication)** - a directory of European software where every tool carries two separate answers built from sourced facts: how European the company is, and who can legally reach a customer's data. An agent can look up what replaces a product it already pays for, filter by how much data can leave Europe, and get the evidence behind each claim rather than a marketing sentence.

```
Server type: Remote (Streamable HTTP, stateless, no auth)
Endpoint:    https://europeinstead.com/mcp
Tools:       5
Registry:    com.europeinstead/europe-instead 1.0.0
Docs:        https://europeinstead.com/developers
             (OpenAPI 3.1 at /api/v1/openapi.json, 8,163 bytes)
Method:      https://europeinstead.com/method
Terms:       https://europeinstead.com/developers#terms
Scores:      origin 0-100, exposure 1-5, each fact with source URL,
             quoted passage and check date
```

## Why This Matters for Operators

Almost every software decision now has a European-sovereignty clause attached to it, and the usual answers are a blog post with no evidence or a vendor's own privacy page. This server answers with two numbers that are deliberately not the same number, and it attaches the evidence to each one.

- **Origin score, 0 to 100** - how European the company is, built from five weighted parts: legal entity (30), ownership (30), operations (15), data residency (15), openness (10).
- **Exposure level, 1 to 5** - who can legally reach the customer's data. Level 1 is "European stack", level 3 is "account or support data leaves Europe", level 4 is "core data leaves Europe on some paths".

The separation is the product. A perfect origin score does not mean the data stays, and the server does not let an agent pretend otherwise: Wire reads **100 / 100** with exposure **level 3**, while Brevo reads **93 / 100** with exposure **level 4**, each with its own disclosed evidence.

## Measured Behaviour

Five tools were listed and driven keyless on 2026-11-21, eleven `tools/call` requests in total. Every figure below is quoted from a response.

| Call | Arguments | Result |
|---|---|---|
| `list_categories` | none | Security **63**, HR **61**, Cloud infrastructure **53**, AI platform **51**, Messaging **49**, Collaboration **47**, Compliance **47**, Cloud storage **46**, Scheduling **39** |
| `list_replaced_products` | none | **50** products returned (the tool's own cap), AWS **39** alternatives, Azure **34**, Google Drive **34**, DigitalOcean **33**, Dropbox **33** |
| `find_european_alternatives` | `Slack`, limit 3 | **20** alternatives, Wire ranked **1** |
| `search_european_tools` | category `crm` | **27** CRM tools, The-Y CRM and Brevo both at origin **93** |
| `search_european_tools` | query `analytics`, `max_level` 1 | exactly **2** tools at level 1: Plausible **100** (EE), TWIPLA **80** (DE, `provisional: true`) |
| `get_tool_details` | `wire` | full fact set with sources (below) |
| `get_tool_details` | `brevo` | full fact set with sources (below) |
| `get_tool_details` | a slug that does not exist | refused in band: `No listed tool "nope-not-real".` |

### The 100 / 100 that still leaks

Wire's detail response returns a per-part breakdown and the evidence behind each part:

```text
legal_entity   30 / 30   Wire Swiss GmbH, CH
                         source wire.com/en/imprint
                         quote  "Imprint Wire Swiss GmbH Untermüli 9 6300 Zug (Switzerland)"
                         checked_at 2026-11-15
ownership      30 / 30   control european, parent Wire Group Holdings GmbH (DE)
operations     15 / 15
data_residency 15 / 15
openness       10 / 10   open_source
exposure       level 3, "Account or support data leaves Europe", disclosed false
review         ai_reviewed, checked_at 2026-11-15, human_verified_at null
```

That is a company that is European at every scored point and still has data paths leaving the region at level 3, with `disclosed: false` - the exposure was not disclosed by the vendor and the directory says so.

Brevo shows the other shape: origin **93**, with `openness` at **3 / 10** because the export path is limited, exposure **level 4** with `disclosed: true`, and a residency note that names the arrangement instead of summarising it - *"OVH in France and Google Cloud in Belgium"* - sourced to the vendor's own terms of use and checked on 2026-11-11.

### Two filters worth knowing

- `max_level` works as a ceiling, not a suggestion: `max_level: 1` on the analytics query returned two tools and nothing above level 1.
- `country` and `open_source` narrow the same lists. `open_source: true` on Google Analytics returned **6** alternatives led by Plausible and Litlyx.

One quirk is recorded rather than smoothed: on a name search the `rank` field is a place in the whole directory, not in the filtered result. The analytics query returned Plausible at `rank 2` beside TWIPLA at `rank 349` - both correct, different lists.

## What the server asks of the agent

Every response carries a `meta` block with the terms of use of the data inside it:

```json
{"attribution": "Data from Europe Instead (https://europeinstead.com). Link the tool's \"page\" when you cite a fact.",
 "ordering": "Tools for a product or a category are in the directory's ranking order: origin score, then exposure level, then review state.",
 "sponsored": "Answers never contain sponsored positions, and no one can pay to change a rank."}
```

So an answer built from this server is expected to carry the tool's page link, and a rank is defined in the payload itself. That is the rare case where the ordering rule travels with the data instead of living on a page an agent never reads.

## Where It Stops

- **A directory, not an audit.** Review state is `ai_reviewed` on every tool read this pass, with `human_verified_at: null`. A `provisional: true` origin score (TWIPLA at 80) is explicitly provisional.
- **European tools only.** The useful query is always "what replaces X", never "tell me about X".
- **Lists are capped at 50.** `list_replaced_products` and `list_categories` both stop there, and the response does not say how many more exist.
- **Exposure is about legal reach, not certification.** Level 1 is the best reading available here; it is not a compliance opinion.
- **No pricing or feature depth.** A summary and a website link, not a comparison table.

### Does a 100 origin score mean the data stays in Europe?

No, and this server is the clearest place in this catalogue to see why. Wire scores **100 / 100** and still reads exposure **level 3**. The two questions are answered separately on purpose, and an agent that collapses them into one recommendation has thrown away the more useful half.

### How should an agent cite it?

Quote the ticker-style pair - origin score and exposure level - and the check date, then link the tool's `page`. The `meta.attribution` string asks for exactly that, and the fact objects carry the `source_url` and the `quote` if a reader wants the primary evidence.

### Is it keyless?

Yes. `initialize` and `tools/list` answer 200 without a token and all eleven calls above were made with no credential. There is also a JSON API behind the same data with an OpenAPI 3.1 document, so the MCP server is one surface on a documented dataset rather than a wrapper around a page.

## Catalogue Position

This is the first entry here whose subject is vendor selection itself, and the first that scores a company on two independent axes with the evidence attached to each. Near neighbours cover adjacent jobs - privacy and consent scanning, AI-visibility scoring - but none of them answers "what European tool replaces this, and how much of my data can leave if I switch".

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [MCP Server Discovery - November 21, 2026 (Midday)](/hermes/mcp/sweeps/sweep-november21-2026-midday)
