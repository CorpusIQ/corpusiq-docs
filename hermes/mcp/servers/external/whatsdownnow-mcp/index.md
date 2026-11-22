---
title: "WhatsDownNow MCP - Which AI Is Down Right Now"
description: "250 services, 27 of them AI, each with a verdict, the official status line and a live probe; when a provider degrades it ranks the healthy alternatives."
category: "Monitoring & Reliability"
stars: n/a (hosted; keyless read and alerting, no account and no key)
added: 2026-11-21
source: "chatmcp/mcpso submission #7786 filed 2026-11-21T23:11:18Z; the official MCP registry records io.github.jacobpmiller/whatsdownnow up to 1.4.0; keyless initialize and tools/list at https://whatsdownnow.com/mcp, then eleven tools/call requests driven on 2026-11-22 against live vendor status feeds"
relevance: ★★★★
tags: [monitoring, outage, status, ai-providers, dependencies, alerting, remote-mcp, keyless]
last_updated: "2026-11-21"
---

# WhatsDownNow MCP

**Remote MCP server (Streamable HTTP, no authentication for reads)** - live outage status for 250 apps, AI APIs and cloud platforms, where every answer carries three separate readings: the vendor's own status line, an HTTP probe from this service, and whatever user reports it has collected in the last hour.

```
Server type: Remote (Streamable HTTP, no auth for reads)
Endpoint:    https://whatsdownnow.com/mcp
Server:      whatsdownnow 1.6.0
Registry:    io.github.jacobpmiller/whatsdownnow, last published 1.4.0
Tools:       13 (nine read, four that provision or change alerting)
Scope:       250 services in 13 categories, 27 of them AI
Homepage:    https://whatsdownnow.com/developers
```

## Why This Matters for Operators

An operator whose business runs on three or four external services does not need another uptime dashboard for his own site. He needs to know, before he blames his own stack, whether the model API, the payment processor or the database host is the thing that is broken, and he needs it in the same chat where he is debugging.

This server answers that question for third-party dependencies rather than for your own properties. The distinction is the whole point of the entry: the catalog already carries surfaces that monitor your own sites, and this one monitors the services you depend on, including fourteen AI providers with a ranked fallback list.

## Tools & Capabilities

Thirteen tools were listed keyless on 2026-11-22.

| Tool | What it returns |
|---|---|
| `get_status` | one service: verdict (up, degraded, down, unknown), a plain-English summary, the official status object, the probe result, user reports in the last hour, a confidence label and a checked-at stamp |
| `list_services` | the tracked services by slug with category and official status page, filterable by query or category |
| `check_stack` | a readiness verdict for a set of dependencies: overall, ready, and each service with its own reading |
| `list_incidents` | recent incidents for a service: the official incident list with titles, URLs, start and resolution timestamps and impact |
| `get_ai_fallback` | the AI board: every tracked provider, and a ranked list of healthy alternatives, optionally scoped to one provider |
| `request_service` | asks the service to start tracking something it does not track |
| `report_issue` | files an issue report against a tracked service |
| `create_alert_stack` | provisions an alert stack with email or webhook delivery, without an account |
| `get_alert_stack` | reads a stack by id and management token |
| `update_alert_stack` | adds or removes services, channels and a public status page |
| `send_test_alert` | fires a test alert to every active channel of a stack |
| `rotate_alert_stack_key` | replaces the management token and link |
| `delete_alert_stack` | deletes a stack |

## Measured Behaviour

Eleven `tools/call` requests were driven keyless on 2026-11-22 between 03:56Z and 04:03Z. Every figure below is quoted from a response.

| Call | Arguments | Result |
|---|---|---|
| `list_services` | none | **250** services in **13** categories: Work and Productivity 42, Social and Streaming 39, Developer and Cloud 36, AI 27, Money and Shopping 26, Gaming 15, Banks and Investing 14, Travel and Delivery 13, Internet and Phone 10, Google 9, Apple 8, Microsoft 6, Home and Security 5 (the block sums to 250) |
| `get_status` | `openai` | resolved to the **chatgpt** slug, verdict **up**, official *"all systems operational"*, probe **200 in 103ms**, confidence label *"Official feed + live probe"*, checked at **2026-11-22T03:56:26.510Z** |
| `get_status` | `stripe` | verdict **up**, official *"no public status feed"*, probe **401 in 97ms** described as *"reachable; API answered and asked for a key, as expected"*, confidence label *"Live probe only"* |
| `get_status` | `claude` | verdict **up**, official *"all systems operational"*, probe **401 in 67ms** |
| `get_status` | `gemini` | verdict **up**, official *"no active incidents"*, probe **200 in 127ms** |
| `get_status` | `vercel` | verdict **up**, probe **200 in 123ms** |
| `get_status` | `not-a-real-service` | refused in band, naming `list_services` and `request_service` as the fix |
| `check_stack` | chatgpt, claude, aws, vercel, supabase, stripe | overall **up**, `ready: true`, *"All 6 services are up."* |
| `get_ai_fallback` | none | **13 of 14** providers healthy, overall **degraded**, generated **2026-11-22T04:03:18.470Z**; fallbacks ranked **OpenRouter 33ms**, **Perplexity 3ms**, **Together AI 23ms**, **Claude 67ms**, **ChatGPT 103ms** |
| `list_incidents` | `cloudflare` | current **up**, with incidents including *"Network Performance Issues in Chicago datacenter (ORD)"* from **2026-11-22T00:32:59Z** to **2026-11-22T01:11:58Z** and a Washington DC rise from **2026-11-20T20:35:16Z** to **2026-11-21T07:44:10Z**, each with its `cloudflarestatus.com` incident URL |
| `get_alert_stack` | fabricated id | refused in band: *"stack_id must look like stk_..."* |

### The one degraded provider, quoted exactly

The AI board read **degraded** at 04:03Z because of a single entry. Mistral returned verdict **degraded** with the official line *"Vibe Work issues with GLM 5.3 Short"* and a probe of **403 in 423ms** marked *"reachable; site blocks automated checks"*. The other thirteen providers read up, including DeepSeek at **200 in 848ms** (the slowest of the healthy set) and Together AI at **23ms**.

Two things about that reading are worth keeping:

- `status.mistral.ai` answers **403** to this host, so the vendor's sentence could not be independently confirmed here; it is recorded as the server reported it, with the timestamp.
- The latency in the board is explicitly not model latency. The server says so itself: *"Latency is from our HTTP probe of the provider's public website, API endpoint, or status page, not model inference latency."*

## Installation

Reads need no credential.

```json
{"mcpServers":{"whatsdownnow":{"type":"http","url":"https://whatsdownnow.com/mcp"}}}
```

```
claude mcp add whatsdownnow --transport http https://whatsdownnow.com/mcp
```

## Business Relevance

- **Triage before blame.** When three tools fail at once, `check_stack` over the actual dependency set separates "our code" from "their outage" in one call, and `list_incidents` then supplies the vendor's own incident record with timestamps.
- **AI provider fallback, measured not guessed.** `get_ai_fallback` returns the healthy providers with probe times, which is the input an agent needs before it retries a different model.
- **Alerting without a console.** `create_alert_stack` provisions email or webhook alerting with no account and no key, which is unusual and is also why it was not driven on this pass.
- **A status page you can publish or hide.** The stack tools include a read-only public page with an optional password, so a client-facing "are we up" page can come from the same object.

## Integration with CorpusIQ

CorpusIQ answers are assembled from live external sources, which means an outage upstream can look like a wrong answer downstream. Attaching this server gives an operator a way to say, in the same conversation, which dependency was failing when the number looked wrong, and to know whether the retrieval failure was ours or the platform's.

## Limitations

- **A 401 is scored as up.** The `verdict` field reads up when the probe gets an authentication challenge, because the endpoint is reachable and asking for a key. The summary says exactly that, but a dashboard that reads only the verdict can present an auth wall as health.
- **One provider flips the whole board.** `overall: degraded` came from a single degraded provider out of fourteen, so the headline reads worse than the components; count before quoting it.
- **The registry lags the deployment.** The last published registry record is **1.4.0** while the running server reports **1.6.0**. A registry version is a date, not a deployment.
- **The slug you ask for may not be the slug you get.** `openai` resolved to `chatgpt`, with the resolution stated in the response; a parser keyed on the request slug will mismatch.
- **Four alerting tools were left undriven.** `create_alert_stack`, `update_alert_stack`, `send_test_alert` and `delete_alert_stack` provision real state and email a real address that a human must confirm, and `report_issue` files a report against a live service. None of them was called, and no claim in this guide depends on them.
- **One vendor feed is not reachable from here.** `status.mistral.ai` answers **403** to this host, so that incident line is second hand.
- **Coverage is a list, not an inventory.** The 250 services are the ones this vendor tracks; a dependency outside that list is refused with an invitation to request it.

## FAQ

### Is this a monitor for my own site?

No. It tracks third-party services: AI APIs, cloud platforms, payment processors, banks, ISPs, travel and streaming. The catalog carries separate entries for monitoring your own properties.

### Does it need an API key?

No for reads. `initialize`, `tools/list` and eleven `tools/call` requests answered without a credential, and the submission states that alert stacks need no account either.

### How current is a status answer?

Each response carries `checked_at`; on this pass ChatGPT read **2026-11-22T03:56:26.510Z** and the AI board **2026-11-22T04:03:18.470Z**.

### Can it tell me which model to use when one is down?

It returns a ranked list of healthy AI providers with probe times, and it states those times are HTTP probes rather than inference latency.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [RealUptime MCP - Uptime, Status and Outage Intelligence](/hermes/mcp/servers/external/realuptime-mcp)
- [World Monitor MCP](/hermes/mcp/servers/external/world-monitor-mcp)
- [RulesWatch MCP - Rule Changes on Prediction Markets](/hermes/mcp/servers/external/ruleswatch-mcp)
