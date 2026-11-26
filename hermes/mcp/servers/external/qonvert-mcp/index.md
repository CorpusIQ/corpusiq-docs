---
title: "Qonvert MCP - Tracking Parameters Checked After Consent"
description: "A marketing-adviser MCP that checks a URL's tracking parameters with no account, then reads Analytics, Ads and orders only after an OAuth grant."
category: "Marketing"
stars: "n/a (no public repository)"
added: 2026-11-25
source: "mcpservers.org arrival in the November 25 evening window, `servers/1..13` maps; official registry record ai.qonvert/qonvert 1.0.1; keyless initialize and an eighteen-tool tools/list over protocol 2025-11-25, plus ten tools/call requests driven against https://mcp.qonvert.ai/mcp on 2026-11-25"
relevance: "★★"
tags: [marketing, utm, tracking, google-ads, google-analytics, attribution, oauth, remote-mcp]
last_updated: "2026-11-25"
---

# Qonvert MCP

**Tracking parameters are the cheapest thing to check and the last thing anyone checks.** A campaign URL that carries `utm_source` and nothing else will still open, still render, and still land the visitor on the right page, and it will silently attribute nothing. Qonvert exposes that check as a tool that works without an account, which makes it the one part of this server an operator can use before signing up for anything.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://mcp.qonvert.ai/mcp
Auth:        none for three guide and check tools; OAuth 2.1 for every data tool
Registry:    ai.qonvert/qonvert 1.0.1
Server:      name "qonvert", title "Qonvert · AI marketing adviser", version "1"
Tools:       18, read from a keyless tools/list
```

## One interop quirk to know before the first call

`initialize` answers **200** and reports `protocolVersion: "2025-11-25"` whatever version the client offers, but the next request decides whether the session works at all:

| Client protocol sent | `tools/list` |
| --- | --- |
| `2025-06-18` | **400** |
| `2025-11-25` | **200**, 18 tools |

**A client that pins the June revision initializes cleanly and then fails on the very next call**, which reads like a broken server rather than a version mismatch. Pin `2025-11-25` in the client, or negotiate from the server's advertised version rather than the client's default, and the tool list arrives.

## The two tiers, split by what needs a grant

**Keyless, works on a cold connection:**

| Tool | What it answers |
| --- | --- |
| `check_marketing_tracking_url` | which tracking parameters the supplied URL carries, which core ones are missing, and which click identifiers are visible |
| `get_qonvert_connect_guide` | the three connected sources, the tool each one drives, the OAuth scope it needs, a worked question and a documentation URL |
| `get_free_placement_guidance` | curated placement advice keyed on business type, stage, market and goal |

**Behind OAuth, refused until a project is authorised:** `get_project`, `list_connections`, `list_scenarios`, `get_marketing_measurement_readiness`, `get_setup_requirements`, `qonvert_connect`, and the platform bridges `google_ads_mcp`, `google_search_console_mcp`, `yandex_direct_mcp`, `yandex_metrika_mcp`, `start_google_ads_optimization`, `start_yandex_ads_optimization`, `adsy_campaign_request`, `get_campaign_brief_status`.

The gate is honest when it fires. `get_project` with no credential returned **401** and *"Create a Qonvert account or sign in to connect your project and its sources."* Several tools name their scope in the description itself, for example `list_connections` carrying *"Additional consent required: qonvert.read"*, so a client can tell the difference between "no data" and "no permission" without parsing an error.

## What the tracking check returns, on three real URLs

This is the tool worth the guide. Every answer has the same five fields, and the third one is the finding:

```text
URL: https://corpusiq.io/?utm_source=x&utm_medium=social&utm_campaign=test
utm_present:                    [utm_source, utm_medium, utm_campaign]
utm_core_absent_from_supplied_url: []
click_id_fields_visible:        []
```

```text
URL: https://corpusiq.io/pricing?gclid=abc123&utm_source=google
utm_present:                    [utm_source]
utm_core_absent_from_supplied_url: [utm_medium, utm_campaign]
click_id_fields_visible:        [gclid]
```

```text
URL: https://example.com/
utm_present:                    []
utm_core_absent_from_supplied_url: [utm_source, utm_medium, utm_campaign]
click_id_fields_visible:        []
```

The three core parameters are named as a group, so a half-tagged URL is reported as missing exactly two rather than as partially present, and a click identifier is reported separately because `gclid` is not a substitute for `utm_medium`. The field name carries its own caveat: `utm_core_absent_from_supplied_url` describes the string that was handed over, not the live destination, and the notes say so twice:

> *"Only the supplied URL parameters were checked. Redirects and identifier capture were not verified."*

> *"Google Ads or Yandex Direct may add an identifier at click time. A missing identifier in this sample is not evidence of a tracking gap."*

**That second note is the reason to trust the tool.** The weak version of this product reports a missing `gclid` as a defect and sends an operator chasing a problem that the ad platform solves at click time. This one refuses the inference and keeps the check to the thing it actually measured.

Input validation is equally blunt: a bare string that is not a URL returned `isError: true` with *"Invalid tool or arguments."* There is no partial answer and no guess.

## The free guidance is narrower than it looks

`get_free_placement_guidance` validates its inputs and returns the accepted values when they fail. That rejection is the most informative thing the tool returned:

```text
business_stage: [idea, building, public]
market:         [ru, global]
goal:           [visibility, feedback, discovery]
```

**The market enum is two values, and one of them is Russia.** A call naming `US`, `saas` and `leads` returned `recommendations: []` with *"Unsupported values for: business_stage, market, goal"*. So this half of the server is built for a Russian-market operator or a global one, and a US-only business falls outside it entirely. Any assistant asked "what should I do for my US campaign" through this tool will produce an empty list, and the emptiness is a scope limit rather than an absence of advice.

## One tool is broken, and it is the one an operator would reach for first

`get_marketing_setup_guide` declares `market`, `language` and `goal` as required and returns *"Invalid tool or arguments."* on every call. Five attempts across the plausible input space failed identically:

| Input | Result |
| --- | --- |
| `market: US`, `language: en`, `goal: leads` | Invalid tool or arguments |
| `market: global`, `language: en`, `goal: visibility` | Invalid tool or arguments |
| `market: ru`, `language: en`, `goal: feedback` | Invalid tool or arguments |
| `market: global`, `language: en`, `goal: discovery` | Invalid tool or arguments |
| `market: US`, `goal: leads` (before the schema was read) | Invalid tool or arguments |

The enum values were taken from the sibling tool that does publish its enums, so this is not a case of a hidden enum rejecting the wrong word. The tool is listed, the schema is complete, and the call cannot succeed. **A listed tool that always fails is worse than an absent one**, because a planner built on the tool list will route work to it and get an argument error that looks like the caller's fault.

## What the connect guide says the gated tier does

`get_qonvert_connect_guide` needs no account and describes the shape of the paid tier precisely enough to plan around:

| Source | Tool | Scope |
| --- | --- | --- |
| Google Analytics 4 | `read_ga4_report` | `qonvert.google_analytics.read` |
| Google Ads | `read_ads_daily` | `qonvert.ads.daily.read` |
| MongoDB order collection | `read_orders_aggregate` | `qonvert.orders.aggregate.read` |

Each entry carries a worked question, for example *"How many sessions did we get in the last seven complete days? Compare with the previous week."* and *"How many orders were created in the last seven complete days?"*, with the answer format stated as the change from the previous period and as an aggregate count. The setup is three steps: save the source in the Qonvert project, add the MCP address to the assistant and approve the project and scopes, then ask a supported question in the assistant. **Each assistant is authorised separately and revocable separately**, which is the right default for an agency running several clients' data through one account.

## Limits measured this pass

- **The grant is the product.** Fourteen of eighteen tools need an authorised project. Everything measurable without one is the tracking check, the connect guide and the guidance tool with its two-value market enum.
- **Yandex carries the same weight as Google.** Four of the bridges are Yandex Direct and Yandex Metrika against two Google ones, which matches the `ru` half of the market enum. An operator outside Russia should read the tool list as a Russian-market product with a Google surface rather than the reverse.
- **`get_marketing_setup_guide` is listed and unusable**, as measured above; treat the working keyless set as three tools, not four.
- **No pricing was read this pass.** Whether the authorised tier has a free level, a per-project charge or a trial is not stated by any tool, so no cost claim is made here.
- **No write path was exercised.** `start_google_ads_optimization` and `adsy_campaign_request` are described as actions on live ad accounts; they were not called with a grant and their behaviour is unverified.

## Where it fits a business-answer system

The honest half of this server is a **pre-flight check with a citation**. Our own marketing discipline requires a UTM on every external link, and the failure mode is not the missing tag anyone notices, it is the campaign that launches with two of three parameters and reports as direct traffic for a month. A tool that names the missing two, refuses to blame the ad platform for a click identifier it cannot see, and returns a link to the page it read is doing the same job CorpusIQ does for business numbers: state the measurement, state the boundary of the measurement, and stop there.

## See also

- [Google Ads MCP](/hermes/mcp/servers/external/google-ads-mcp/) for reading ad performance directly rather than through an adviser layer.
- [Google Analytics MCP](/hermes/mcp/servers/external/google-analytics-mcp/) for the analytics half of the same stack.
- [GoodLeads MCP](/hermes/mcp/servers/external/goodleads-mcp/) for new-business lead data feeding the other end of the funnel.
- [External MCP Server Catalog](/hermes/mcp/servers/external/) for the full index.
