---
title: "MCP Server Discovery - October 1, 2026 (Morning)"
description: "Morning sweep of the mcp.so feed and mcpservers.org: two new servers catalogued with integration guides."
category: mcp-directory
tags: [mcp, discovery, sweep, directories]
---

# MCP Server Discovery - October 1, 2026 (Morning)

**Date:** October 1, 2026 (morning slot)
**Sources:** mcp.so /feed (29 server blocks) via the r.jina.ai reader proxy, plus mcp.so /servers (60 slugs) and the mcpservers.org homepage (29 slugs) and /all (30 slugs) via the reader proxy. Firecrawl was unconfigured this cycle, so every directory fetch ran through the reader proxy.
**Result:** 2 new business-relevant servers catalogued with guides. Catalog 765 to 767 servers, guides +651 to +653.

## Discovery

Feed-order recency against the September 30 night anchor (PixelDojo at the top, TrackIQ below it) turned up one entry not previously disposed, and the two directory surfaces carried one more:

- **FlatHunt** - evaluated from the feed (submitted 7 hours before the sweep). A Berlin housing search aggregator at `mcp.flat-hunt.com/mcp`, remote Streamable HTTP, public search with OAuth for account features. Well documented, but it is a consumer housing marketplace rather than a business-operator data or operations surface. Consumer retail class, outside the catalog. Skipped.
- **Datris Data Platform MCP** - catalogued (see below).
- **Hourtick MCP** - catalogued (see below).

Everything else in the feed and on the two directory surfaces matched a prior disposition or an already-catalogued guide, checked against the sweep index and the `servers/external/index.md` ledger. Of note, OceanAlt AML (feed) was catalogued in the September 30 morning sweep, and Common Paper Contracts, Genchi and Manifold (feed) were catalogued in the September 30 night sweep. All were re-confirmed as already covered rather than treated as new.

## New servers catalogued

- **Datris Data Platform MCP** (Governed data acquisition for agents) - self-hosted, Docker-based open-source data platform (AGPL-3.0) that exposes 73 capabilities behind one MCP server. Agents ask Datris for data and it finds, acquires, validates and lands it in the stores the operator already runs, returning result with provenance and never holding credentials: the agent references a secret by name and generated code runs in an isolated container with no keys inside it. The operating loop runs Acquire (AI-generated taps) to Validate (plain-English rules) to Land (multi-destination pipelines) to Observe (provenance and job state) to Explain and Repair (AI error explanation). Durable pipeline state and sync bookmarks live in the platform rather than the chat, and every generated script is versioned in git. Local stdio bridge over `npx mcp-remote http://localhost:3000/sse`; a brew CLI (`datris ingest data.csv --dest postgres`) is also published. Relevance THREE because it is a genuine operator data-operations surface with a credential model that makes unattended agent ingestion safe to run. The public listing did not expose a fetchable tool list, so the guide describes capabilities by stage rather than inventing tool identifiers.

- **Hourtick MCP** (Time tracking, tasks and billing for teams and agents) - remote Streamable HTTP at `hourtick.com/api/mcp` (MCP 2026-07-28 stateless), OAuth 2.1 sign-in or a bearer token. Roughly forty tools across identity and projects, time (start/stop timer, log_time, list entries, reports, get_my_day, the fill_my_timesheet prompt), tasks, team chat, notes and files, plus a full agent-coordination set (create_agent, agent_delegate, agent_wait_for_work, agent_get_context, agent_log, agent_ask, agent_reply, agent_report_usage, agent_fail). Agents are workspace members with their own seat, token and MCP address; they log their own billable time and usage cost, which appears in Reports as the agent's own row and is marked invoiced like any other entry while never touching a person's timesheet. Chains cap at four hops and admins bound each agent by client, project, read-only mode, monthly budget and expiry date. Free forever for unlimited people (500 MB/month); Pro $29/month for 5 GB. Relevance THREE because the delivered insight is the human-plus-agent billing ledger rather than another task board. Tool list taken verbatim from the vendor's `/developers` page, which publishes the endpoint, transport, auth model and every tool name.

## Core listing verification

- **mcpservers.org:** LISTED. Direct curl returns the Cloudflare wall; the reader proxy returns the CorpusIQ MCP page, so the listing is live.
- **glama.ai/mcp:** LISTED. The `@corpusiq/corpusiq-docs` slug redirects to the canonical listing.
- **PulseMCP:** LISTED. Reader proxy title reads Official CorpusIQ MCP Server.
- **smithery.ai:** registry entry present. No submission path exists (login-walled) and the listing is unstable, so no action taken.
- **mcp.so:** NOT LISTED. The account-level instant moderation state from August 12 still stands, so no resubmission was attempted.

## Also identified (not catalogued)

FlatHunt (Berlin housing search aggregator, consumer housing/marketplace class, the TATUAT.RO precedent), SendRaven (email infrastructure for agents with campaign and thread tools, but the listing exposes no detectable tool list and only a one-line description; thin-docs class), GripForge (game asset generation for Unity/Godot/Unreal; creative and gaming class), Vibgrate (dependency drift, CVEs and EOL runtimes with DriftScores; dev-security class), Local YDB MCP (Docker-based local YDB operations over stdio; devops class), OrangePro (behavior mapping and grounded test generation; dev-QA class), GitDiagram (architecture diagrams and Mermaid source from GitHub repos; dev-utility class), Better Design (design harness for coding agents; dev-utility class), D365 Mockup Agent (Dynamics 365 and Business Central mockup drafting; dev-utility class), CycleCalcs (astronomy API; niche vertical), Reps Gym Workout Log (consumer fitness), plus the mcp.so /servers and mcpservers.org surface repeats already catalogued or disposed by the September 30 sweeps and earlier ledgers.

## Skip classes held

- **Consumer marketplaces and storefronts:** FlatHunt is a consumer housing aggregator with no operator data surface. The catalog tracks business-operator data and operations tools, so consumer marketplaces stay out unless they serve a B2B workflow.
- **Thin listings with no published tool list:** SendRaven publishes an endpoint and a one-line description but no tool identifiers. Products in this shape wait until the vendor publishes a tool reference before a guide is written.
- **Dev, QA and game-creation utilities:** GripForge, Vibgrate, Local YDB, OrangePro, GitDiagram, Better Design and D365 Mockup serve developer, QA, devops or game-creation workflows rather than business-operator data and operations, and stay outside the catalog.

## Verification

The two new guides passed the inline checks (title length, description length, required frontmatter fields, added date, dash scan, See Also path existence) and the repository frontmatter validator over the whole docs tree. The SEO validator reports 0 errors and the accepted index-coverage advisories for this file class. The class-level AEO advisory from the local pre-commit gate is accepted house style for this file class, as it is for the rest of the external catalog.
