---
title: "ARC MCP - Agent Commerce Checkout Reachability"
description: "A neutral, dated record of which online stores AI agents can actually buy from, with readiness checks, fix lists and monitoring for e-commerce teams."
category: Commerce & E-Commerce
stars: n/a (new listing)
added: 2026-10-13
source: "mcp.so feed + official MCP registry (ai.arcreport/mcp; October 13, 2026 evening sweep)"
relevance: ★★★
tags: [agentic-commerce, checkout, agent-readiness, ecommerce, ucp, keyless, remote-mcp]
---

# ARC Agentic Report Card MCP

**Hosted MCP service (Streamable HTTP, keyless for reads)** - ARC, the Agentic Report Card, is a free and neutral record of which online stores AI agents can actually buy from, with dated evidence, plus readiness testing and fix lists for the stores themselves.

```
Server type: Remote (Streamable HTTP), hosted service at arcreport.ai
Auth: None for the record reads and checkout reporting (vendor stated); the monitor tools manage your store checks
Connectors: https://www.arcreport.ai/api/mcp (store checks, 19 tools) and https://www.arcreport.ai/api/ask (public index, 15 tools)
Registry: ai.arcreport/mcp and ai.arcreport/ask (official MCP Registry)
Pricing: Free; the underlying dataset is open (CC-BY-4.0) at arcreport.ai/data
Built by: ARC (arcreport.ai)
Listing: mcp.so feed, October 13, 2026 evening sweep
```

## Why This Matters for Operators

Agent commerce turns "can a customer check out on my store" into "can an agent check out on my store", and that question is about to sit in front of every product conversation an assistant has. ARC keeps the checkable record: which stores support machine checkout, which protocols they speak, when the last verification ran, and which checks are failing.

For an e-commerce team the useful half is the second one. The readiness checks and the fix list turn "agents may not be able to buy from us" into a work queue: product data, checkout surface, protocol support. The monitors then keep watching, so the answer stays current instead of being a one-time audit.

## Tools & Capabilities

Store checks connector (`/api/mcp`, 19 tools):

| Tool | Purpose |
|---|---|
| check_store | Check a store for agent checkout reachability, with dated evidence |
| find_stores | Search the record for stores by reachability and result |
| can_agent_checkout | One-call answer for whether an agent can complete a checkout on a store |
| google_checkout_readiness | A store against Google's agent checkout requirements |
| product_data_check | Whether product data is ready for agent purchase |
| check_agent_readiness / get_readiness_result / list_readiness_checks | Run readiness checks and read the results and the check catalogue |
| get_fixes | The fix list for failing checks |
| get_store_hub | A store's hub: checks, history and evidence |
| ask_agents_about_brand | Agent-perspective lookups for a brand |
| report_checkout | Report a checkout attempt as dated community evidence |
| bulk_create_monitors / list_monitors / monitor_summary / update_monitor / pause_monitor / resume_monitor / run_monitor_now | The monitoring suite for store checks |

Public index connector (`/api/ask`, 15 tools):

| Tool | Purpose |
|---|---|
| ask_arc | Ask questions of the ARC index |
| find_agent_ready_stores / store_card | Find agent-ready stores and read shareable store cards |
| agent_commerce_adoption / agent_leaderboard | Adoption statistics and the readiness leaderboard |
| protocol_matrix | Which agent commerce protocols each store supports |
| validate_ucp_profile | Validate a UCP profile |
| get_agent_facts / list_category_agent_facts | Structured facts for a brand or a category |
| dataset_info | The open dataset: scope, licence, refresh cadence |
| submit_store / submit_leaderboard_run | Submit a store or a leaderboard run |

## Installation

```
claude mcp add --transport http arc https://www.arcreport.ai/api/mcp
claude mcp add --transport http arc-ask https://www.arcreport.ai/api/ask
```

Any MCP client that speaks Streamable HTTP can add the same URLs. Reading the record needs no sign-in.

## Configuration

```json
{
  "mcpServers": {
    "arc": {
      "type": "http",
      "url": "https://www.arcreport.ai/api/mcp"
    }
  }
}
```

## Business Relevance

- **E-commerce and DTC teams** test whether agents can complete a checkout on their store, get the fix list for what is broken, and monitor the result over time
- **Agencies and platforms** check client stores in one call and compare protocol coverage before recommending changes
- **Agent builders** find agent-ready stores to route purchases to, and read the protocol matrix and the adoption numbers
- **Brands and marketplaces** submit their store, add dated evidence, and watch the leaderboard

## Integration with CorpusIQ

ARC covers the agent-commerce layer: whether agents can buy, what is broken and what changed. CorpusIQ answers the surrounding business question from connected sources such as store data, spreadsheets, email and accounting, so a readiness conversation that starts in a product meeting can pull the checkout evidence into the same thread.

Used together: ask CorpusIQ for the operating view (orders, inventory, marketing, correspondence) and ask ARC for the agent-commerce view (reachability, protocol support, fixes). ARC stays the source of record for the checkout evidence; CorpusIQ remains the place the rest of the question is answered alongside.

## Limitations

- A store absent from the record is not proven non-buyable; coverage depends on the checks that have been run, so read the dates on the evidence
- The monitor tools manage your store checks and may involve an account flow; the record reads and checkout reporting need no sign-in
- The agent checkout space is young and moving fast; protocol support changes, so re-check before making claims to customers
- Operated as a free service by ARC; the dataset is published openly (CC-BY-4.0)

## FAQ

### Is it really keyless?

Yes for the record: reading saved checks (`check_store`, `find_stores`) and reporting a checkout attempt need no sign-in. A live probe returned 200 with all 19 tools on the store checks connector and all 15 on the public index connector.

### What can an assistant actually do with it?

Ask whether a store is agent-buyable and see the dated evidence, run readiness checks and read the fix list, compare protocol support across stores, read adoption and leaderboard numbers, and keep monitors watching a store over time.

### Who is it for?

E-commerce and DTC operators, agencies that manage stores, agent builders that need to route purchases, and brands that want their store on the record.

### What does it cost?

The record and the checks are free. The underlying dataset is open (CC-BY-4.0) at arcreport.ai/data.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
