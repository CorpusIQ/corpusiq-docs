---
title: "NexaLayer MCP - Proxies With a Spend Cap Built In"
description: "Residential proxy sessions an agent can open and close, with sticky exit IPs and soft spend caps that stop a loop overnight."
category: Infrastructure
stars: ★★ (package and guardrail model verified, v0.2.0, MIT)
added: 2026-10-29
source: "npm package @nexalayer/mcp 0.2.0 read from the npm registry on 29 October 2026 (MIT, repository NexaLayer/nexalayer-agent) and the vendor submission with its budget guardrail scope"
relevance: ★★
tags: [proxy, residential-proxy, scraping, spend-controls, sticky-session, local-mcp]
last_updated: "2026-10-29"
---

# NexaLayer MCP

**Any agent that scrapes is a metered process. The failure everyone experiences once is a retry loop that runs all night against a pipeline that charges per gigabyte.**

```
Server type: Local (stdio)
Install:     npx -y @nexalayer/mcp@0.2.0
Package:     @nexalayer/mcp 0.2.0, MIT
Registry:    io.github.NexaLayer/nexalayer
Website:     nexalayer.net/agents
Pricing:     early-access launch pricing about $0.23 per GB, per the live products API
```

## Why This Matters for Operators

Proxy access is infrastructure that a business buys when it collects public data at volume: competitor prices, marketplace listings, search results, ad libraries. The connector question is not whether an agent can route a request through a proxy. It is whether the agent can be trusted with the meter.

What distinguishes this surface is that **budget guardrails are part of the server's stated scope**, alongside creating and listing sessions, soft spend caps and sticky exit IPs. Sticky exits are the other half of the same idea: a task that needs the same apparent origin across several requests depends on the session holding still, and an identity that changes on every request breaks the very thing the task needed.

An operator running a scrape on a schedule should be able to say what one run may cost. That is the property being catalogued here.

## What It Does

Three capabilities are named in the submission, and they cover the lifecycle:

- **create and list sessions**, so a working session is a thing the agent opens, names and closes rather than ambient state
- **soft spend caps**, which is the guardrail that turns an unbounded meter into a bounded one
- **sticky exit IPs**, so a multi-request task keeps one origin for its duration

The entry point is the npm package, installed at a pinned version:

```json
{
  "mcpServers": {
    "nexalayer": {
      "command": "npx",
      "args": ["-y", "@nexalayer/mcp@0.2.0"]
    }
  }
}
```

## What Was Verified

The npm registry entry for `@nexalayer/mcp` resolved on 29 October 2026 at version **0.2.0**, licence **MIT**, repository `github.com/NexaLayer/nexalayer-agent`, binary `nexalayer-mcp`, described as an MCP server for NexaLayer managed proxy sessions. The official registry entry is `io.github.NexaLayer/nexalayer` at the same version.

The per-gigabyte figure is recorded as the vendor's own statement, drawn from a live products API at submission time, and the vendor states it may change. It is early-access pricing, not a list price, so it belongs in the guide as a dated observation rather than a quote.

## Limits Worth Recording

**A soft cap is soft.** It is a guardrail that the agent's own session respects, not a hard billing ceiling enforced by the provider, and treating the two as the same thing is how a cap fails. Anyone planning an unattended scrape should pair it with a billing-side limit they control.

A pinned version is deliberate. This is a `0.2.0` package, and an unpinned `npx` will move under an automation that nobody is watching.

There is a **name collision worth recording**: an unrelated mcp.so listing called `nexlayer-cloud` installs as `npx -y nexlayer-mcp`, which is not this server. The `nexalayer` Python package on PyPI is an SDK only and is not the MCP entry point either.

## FAQ

### What are the guardrails actually for?
Bounding what one agent run may spend. Sessions are created, listed and closed, and a soft spend cap applies to the session rather than to the account's whole bill.

### What is a sticky exit IP for?
Keeping the same apparent origin across several requests in one task, which is required whenever a workflow needs continuity rather than a fresh identity per call.

### How much does it cost?
Early-access launch pricing was about $0.23 per GB at submission, read from the live products API, and the vendor notes it may change. Confirm at purchase rather than relying on this figure.

### Is this the same as nexlayer-cloud on mcp.so?
No. `nexlayer-cloud` installs as `nexlayer-mcp` and is a different server. This entry is `@nexalayer/mcp` from the NexaLayer organisation, and the PyPI `nexalayer` package is an SDK, not the MCP server.
