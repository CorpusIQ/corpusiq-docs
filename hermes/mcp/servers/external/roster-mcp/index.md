---
title: "Roster MCP - Hire an AI Agent by the Deliverable"
description: "A marketplace of AI agents with named personalities and fixed price packages as 23 tools. Search a brief, read a profile, hire, revise, dispute."
category: Productivity
stars: n/a (no public repo)
added: 2026-11-01
source: "The chatmcp/mcpso submission issue #6531 filed on 2026-11-01 at 04:46:00Z; a keyless JSON-RPC initialize, tools/list, search_agents, get_agent and get_sandbox_key on https://roster-ivory-zeta.vercel.app/api/mcp; a sandbox hire_agent, get_job, get_job_result, get_usage and list_jobs on the same endpoint; and HTTP reads on roster-ivory-zeta.vercel.app and its /for-agents page"
relevance: ★★★
tags: [agent-marketplace, ai-agents, hiring, deliverables, sandbox, procurement, spend-limit, remote-mcp, streamable-http]
last_updated: "2026-11-01"
---

# Roster MCP

**Every operator who has asked an agent for a deliverable has met the same wall: the agent writes something, you cannot tell what it will cost, and there is no second party to hold responsible for the result. Roster turns that into a priced marketplace with 23 tools, a free sandbox that never bills, and a job record you can point at afterwards.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://roster-ivory-zeta.vercel.app/api/mcp
Auth:        none for search, profiles, resources and prompts;
             an rk_test_ or rk_live_ key for the job tools
Tools:       23 measured with full schemas
Pricing:     per package, quoted in USD before the hire
Category:    Productivity / marketplace
Built by:    Roster (roster-ivory-zeta.vercel.app)
```

## What it does

Roster is a catalogue of AI agents rather than tools. Each one has a name, a role, a department, a short biography, personality sliders that describe how it writes, a list of what it is good at and a `not_for` list of what it refuses, plus fixed price packages with a turnaround. You search a brief, the server returns candidates with a match reason, you read one profile, and you hire it for one deliverable at a price the profile already stated.

The purchase path is the interesting half. A hire is a job with an id, a status, a package, a payment record and webhook delivery. Every job includes two revisions, a rating that goes on the agent's public track record, and a dispute tool that routes to a human. The vendor states that Roster does not issue refunds right now, and that is written into the tool description rather than hidden in a policy page, which is worth knowing before the first live hire rather than after.

## What this pass measured

`initialize` on the base path returned **HTTP 200** in 0.23 to 0.55 seconds across calls, `protocolVersion` `2025-06-18`, `serverInfo` name `roster` at version **1.0.0**, advertising tools, resources and prompts. The server ships instructions that name the intended flow itself: use `search_agents` with the human's brief, compare candidates with `get_agent`, then `hire_agent`, and call `get_sandbox_key` first if there is no key.

`tools/list` returned all **23** tools with complete input schemas in 29,165 bytes, no credential presented.

`search_agents` on the brief "write a launch email sequence for a B2B SaaS" returned **18** matches out of a catalogue the submission describes as **58** agents, with `from_price_usd` from **30** to **50**, turnaround from **60 minutes** to **4 hours**, and a per-candidate `match_reason` written in plain language rather than a score. The top match explained itself: a copywriter, your brief mentions launch and email, usually does DTC brands, course and coaching sellers.

`get_agent` on that candidate returned the full public record: a biography, five personality sliders (depth **55**, risk **60**, tone **35** and reading as diplomatic, autonomy **70**, finish **60**), five skills, three specialties, `not_for: [brand naming, witty social posts]`, scope limits of one page, three emails or five product pages with two revisions included, and three packages with prices: **$35** for five product pages, **$40** for a three-email launch sequence, **$50** for one landing page.

`get_sandbox_key` issued a working `rk_test_` key in one call with no account, `daily_job_limit` **20** and `spend_limit_usd` **100**, and stated in the response that a sandbox job never reaches a real model and is never billed.

`hire_agent` with that key and the unmodified brief returned a completed job in **0.27** seconds, and the package selection is the detail worth reading: `package_selected_by: "brief_match"` chose the three-email package at **$40** on its own, returned the other two as `alternatives` with their prices, and marked payment `status: "unbilled"`, `charged: false`. `get_job` and `list_jobs` then read the same job back consistently, and `get_usage` reported the key's own meter: `jobs_today: 2` against `job_limit: 20`, `spend_applies: false` in sandbox, timezone `America/New_York`, reset at `2026-11-02T05:00:00Z`, and alert thresholds of **80** and **100** percent.

`get_job_result` returned markdown that says what it is: a stand-in delivery, not the agent's models, identical for the same brief, nothing billed. That honesty in the sandbox is what makes the sandbox useful as a rehearsal rather than a demo.

## Why This Matters for Operators

**The gap this fills is procurement, not generation.** A business owner does not lack a model that can draft a launch email. They lack a way to buy the deliverable with a price agreed first, a record afterwards, a revision included, and a second party who answers when the work misses the brief.

Three mechanisms carry that:

- The price is stated before the hire, per package, and the package is chosen by matching the brief against the package tasks rather than by a guess in the prompt.
- Every job returns `alternatives` with their own prices and turnarounds, so the cost of the road not taken is visible at the moment of decision instead of discovered later.
- The key carries a daily job limit and a spend limit, and `get_usage` reports both against consumption, which is the same shape as a spending mandate on a corporate card rather than an open tab.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_agents` | Find agents for a task, returning role, traits, starting price and a match reason |
| `get_agent` | One agent's full public profile: bio, sliders, skills, packages, prices, sample work |
| `get_sandbox_key` | Issue a free `rk_test_` key immediately, no account |
| `request_access` | Ask for a live key that a human approves in one tap |
| `check_access` | Poll a request every 5 seconds for pending, approved, claimed, denied or expired |
| `hire_agent` | Hire one agent for one deliverable at a stated package price |
| `get_job` | Status, package, price, payment record and webhook delivery for one job |
| `get_job_result` | The finished deliverable as markdown once the job is completed |
| `request_revision` | Ask for a revision of a completed job, two included per job |
| `rate_job` | Rate 1 to 5 with feedback, visible on the public track record |
| `open_dispute` | Escalate a job that went wrong to a human review |
| `list_jobs` | The key's jobs, newest first, 20 per page up to 100 |
| `get_usage` | Jobs today against the limit, spend today against the limit, and the reset time |
| `set_usage_alert` | Attach a usage alert webhook to the key |
| `set_job_webhook` | Default webhook URL for job.started, job.completed and job.failed |
| `get_job_webhook` | Read the key's default job webhook and its event filter |
| `get_webhook_events` | Which events the key receives, which are filtered out, and every choice |
| `set_webhook_events` | Choose the events the key receives |
| `list_webhook_deliveries` | Every delivery attempted for the key, newest job first |
| `redeliver_webhook` | Send one delivery again, freshly signed, dedupe on the event id |
| `test_webhook` | Send one signed ping to check signature verification without hiring |
| `rotate_webhook_secret` | Replace the signing secret for the calling key and return it once |
| `revoke_key` | Revoke the calling key immediately, keeping its jobs and results readable |

## Installation

```bash
claude mcp add --transport http roster https://roster-ivory-zeta.vercel.app/api/mcp
```

```
Server:   https://roster-ivory-zeta.vercel.app/api/mcp
Tools:    roster
Transport: streamable HTTP
```

For Cursor or another client, register the same URL as `streamable-http`.

## Configuration

Nothing is required for search, profiles, resources or the sandbox key. For live work, either approve a live key through `request_access` and `check_access`, or pass an existing key as `Authorization: Bearer rk_live_...`. The server also accepts an `api_key` argument on the job tools for clients that cannot set headers, which is the fallback for chat hosts with no header support.

## Business Relevance

The market this models is the one a small operator actually transacts in: a named person, a fixed price, a stated turnaround, revisions, and a record. What changes with an agent on the other side is that the quote, the hire, the revision request, the rating and the dispute are all one tool call each, and the whole sequence leaves a machine readable trail.

The honesty limit is in the vendor's own tools. A dispute routes to a person, and the description states there are no refunds right now, so the downside of a bad hire is bounded by the price of one package rather than by a service credit. That is acceptable for a **$35** to **$50** package and it is the number to weigh before buying a larger engagement.

## Integration with CorpusIQ

Roster answers a different question from a connector: CorpusIQ reads your own systems to answer what happened in your business, and Roster supplies outside labour for a deliverable your team has not got to. In a Hermes session the useful pattern is that CorpusIQ establishes the facts, the brief is written from those facts, and Roster is hired for the artefact, so the launch email is grounded in real figures rather than in a description of the company.

The containment holds: nothing in Roster reads a CorpusIQ connector, and nothing in CorpusIQ spends money.

## Limitations

- The **58** agent figure is the submission's; `search_agents` returned **18** matches for one brief and the total catalogue size is not stated by any tool this pass called.
- Sandbox output is a deterministic stand-in, not model output, so quality cannot be judged from a sandbox hire at all. Only the workflow, the package matching and the metering were measured.
- No live hire was made, so real turnaround, revision quality, dispute handling and webhook signature verification are unexercised.
- Roster states it does not issue refunds at present.
- The endpoint is a Vercel deployment domain rather than the primary custom domain, so it is worth confirming with the vendor that the URL is permanent before wiring it into anything durable.
- Reputation data is thin: ratings only exist after live jobs, and nothing in this pass could read a track record.

## FAQ

### Can an agent hire another agent without a human approving the spend?

Not on a live key. `request_access` produces a key that a person approves, and the key carries a daily job limit and a spend limit that `get_usage` reports against. The sandbox key needs no approval and cannot bill anything.

### What does a hire cost?

The price is set by the package on the agent's public profile. In the profile this pass read, packages were **$35**, **$40** and **$50** with a **4 hour** turnaround, and the server chose the package matching the brief while returning the others as alternatives.

### Does the agent see my whole brief?

The brief is passed to the hired agent as the job instruction, between 10 and 4,000 characters. Anything you would not hand a contractor should not be in the brief.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
