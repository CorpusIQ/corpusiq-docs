---
title: "Lowdown MCP - Dated Facts About an MCP Server, Not a Score"
description: "Two keyless tools recording daily initialize checks, registry declarations, package state and tool-definition changes across the public MCP fleet."
category: "Developer Tools"
stars: n/a (vendor-hosted index)
added: 2026-11-22
source: "mcpservers.org sitemap arrival petshopbros/lowdown-proxy stamped 2026-11-22T06:02:29Z; repository README at github.com/petshopbros/lowdown-proxy; keyless initialize, tools/list and nine tools/call requests at lowdown-proxy.vercel.app/mcp on 2026-11-22"
relevance: ★★★★
tags: [tool-discovery, vetting, supply-chain, maintenance, uptime-evidence, registry, remote-mcp, keyless]
last_updated: "2026-11-22"
---

# Lowdown MCP

**Two servers can both be "maintained". Only one of them can show you twenty-seven consecutive days of answering `initialize` and `tools/list`, and the exact date its tool definitions last changed.** Lowdown records those facts about the public MCP fleet and deliberately refuses to turn them into a score.

```
Server type: Remote (Streamable HTTP, no auth)
Endpoint:    https://lowdown-proxy.vercel.app/mcp
Tools:       2 (get_lowdown, find_servers)
Handshake:   lowdown 0.1.23 on protocol 2025-06-18
Dataset:     open daily observations, CC BY 4.0
Also:        HTTP API at /api/reputation/…, and `npx lowdown-proxy -- <server>` to wrap any stdio server
Observations recorded from: 2026-10-20
```

## Why This Matters for Operators

The question an operator asks before connecting an agent to a business system is not "is this good". It is "is this still there, is it still the same, and does anyone stand behind it". Those are recordable facts, and Lowdown is the first entry in this catalogue whose entire product is recording them with a date, at a stated cadence, from a stated location.

The epistemic discipline is the interesting part, and it is written into every response: *"A protocol check (initialize and tools/list) shows that a server answered; it does not show that its tools run successfully."* The tool returns `evidence_levels` naming exactly what it has - `registry_declaration`, `protocol_check_without_credentials` - and what it does not: `tool_execution.verified_by_lowdown: false`, `agent_reported_tool_calls: 0`.

## Our Own Record, Read Back

`get_lowdown` on the CorpusIQ registry name is the cleanest demonstration of the mechanism, because the numbers can be checked against a server we run:

```text
target            mcp:io.corpusiq/multi-source-mcp
state             answered
checks_30d        27 answered / 27 observed / 27 scheduled   (2026-10-27 to 2026-11-22)
consecutive_days  27, since 2026-10-27   basis fixed_cohort, one check per day
scanner.latest    HTTP 200, latency_ms 204, tool_count 121, schema_hash ebb8c6…
tool_set_since    2026-10-29
last_definition_change 2026-11-06
registry          active, first_recorded 2026-10-19, last_change_30d 2026-10-25
payment           payment_required false, no 402 seen on initialize or tools/list
auth              not_required
```

That is a listing check with a fingerprint: 121 tools, a schema hash, and a definition-change date. A monthly report that needs to prove the endpoint has been up all month, or that an agent was pinned to a tool surface that has not silently changed, has this to cite.

## The Cadence Is Part of the Record

The same call on CoreHu returned a different shape, and the difference is the honest one:

```text
target   com.corehu/gpu-cloud
state    "On the latest check (2026-11-22) its remotes differed:
          1 answered tools/list, 1 required authentication."
basis    one check every 3 days, rotating cohort, since 2026-11-13
tool_count null            (a mixed result has no single tool list)
payment    payment_required false
```

Servers in the fixed cohort are checked daily; the wider fleet rotates every three days, and the response says which basis applies (`observation_basis: fixed_cohort` or `rotating`) and how many days since the last check. `stale: false` appears with a date rather than a reassurance.

## What It Refuses to Do

`find_servers` is where the philosophy bites. The catalog's own sweep found four PrestaShop MCP servers on 2026-11-22 by searching descriptions; the same question asked of Lowdown returns **`total: 0`**, because `does=` matches only the Registry name and tool names from the last observed list - *"Tool descriptions are not searched"*. So it cannot answer "which PrestaShop server", and it does not pretend to.

What it can answer is a filtered shortlist with facts attached: `state` (answered, auth_required, payment_required, list_failed, no_response, invalid_response, mixed), `no_auth=1`, `answered_days` up to 30, `stable_days` for how long the tool list has held, `tools_min` and `tools_max`, `registry` status, and `package` readiness (`ok`, `flagged`, `none`, where flagged means a deprecated, yanked, quarantined or 404 package). Sorting is by a named key - `name`, `newest`, `updated`, `tools`, `stable`, `answering`, `changed`, `release` - and the basis states the rule: *"No score or ranking: order is only the chosen sort key."*

## Payment Terms as an Observed Fact

One field has no equivalent elsewhere in this catalogue: `payment`. Lowdown watches for **HTTP 402** on `initialize` or `tools/list` and records the terms in the same response, with its own limits stated - it does not pay, does not call tools, and *"payment asked only when a tool is called is not seen here"*. For an operator scanning for pay-per-call infrastructure, that is a measurable signal rather than a claim on a landing page.

## The Data Under It

- **Daily dataset** published openly under CC BY 4.0, one observation per server per cadence, from a single network location, with a day without a check treated as a gap rather than a failure.
- **HTTP API** at `https://lowdown-proxy.vercel.app/api/reputation/mcp:<name>` for the same record outside MCP.
- **A stdio wrapper** - `npx lowdown-proxy -- npx some-mcp-server` - which adds the record to the wrapped server's `initialize` response and contributes the session's interactions back to the network, creating a node identity at `~/.lowdown/node.json` on first run. That contribution is the vendor's model and is stated in the README rather than buried.

## Limits, Stated

- **One location, one shape.** A check proves the endpoint answered from Lowdown's network, not from yours, and not that a tool returned a correct answer.
- **Tool descriptions are not searched**, so discovery by capability is weaker than in [KitScout](/hermes/mcp/servers/external/kitscout-mcp/), which indexes 94,077 tools with descriptions.
- **Early version.** The server answers `0.1.23`, and its records begin 2026-10-20, so `stable_days` cannot yet exceed about a month.
- **Korean text in the tool descriptions** (`Lowdown(로우다운)`) ships as-is, which is worth knowing if a client displays descriptions verbatim.
- **The wrapper is a network participant.** Wrapping a server contributes interaction data; read the README before putting it in front of a client's internal tooling.

## Two Entries, One Class, Opposite Answers

This pass catalogued both halves of the pre-install check that arrived on the same day. KitScout returns a **verdict** and says plainly that `ok` is not a security review. Lowdown returns **no verdict at all**: a state, a cadence, a fingerprint, and the evidence levels behind them. An operator who wants an opinion takes the first; an operator who wants a record to cite takes the second. Both are keyless, and neither can tell you whether the code is safe.

## See Also

- [KitScout MCP - Vetting a Tool Before It Gets Your Keys](/hermes/mcp/servers/external/kitscout-mcp/)
- [MCP Server Discovery - November 22, 2026 (Night)](/hermes/mcp/sweeps/sweep-november22-2026-night)
