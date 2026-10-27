---
title: "Hypotize MCP - Growth Experiment Memory for Agents"
description: "Growth-experiment memory over MCP: your agent reads the backlog of what the team already tested, writes hypothesis-first ideas, scores them with ICE, PIE or RICE and records measured outcomes."
category: "Growth / Product Operations"
stars: n/a (new listing)
added: 2026-10-16
source: "chatmcp/mcpso issue #5500 (October 16, 2026 night sweep)"
relevance: ★★★
tags: [growth, experimentation, a-b-testing, product, prioritization, ice, rice, oauth, remote-mcp]
last_updated: "2026-10-24"
---

# Hypotize MCP

**A shared experiment memory for teams and their agents. Hypotize does not run A/B tests or assign traffic - it keeps the record before and after an experiment runs, so a hypothesis, its owner, its target metric, the measured result, the evidence and the learning live in one place your assistant can read and write. Remote server with OAuth sign-in; the agent reads the backlog before proposing and cannot close an experiment without a measured result and a written learning.**

```
Server type: Hosted (Streamable HTTP, JSON-RPC 2.0)
Endpoint: https://api.hypotize.ai/mcp
Auth: OAuth 2.1 (PKCE, dynamic client registration); you sign in and choose what the agent may do
Scopes: hypotize:read, hypotize:write, hypotize:delete (off by default), offline_access
Tools: 21 - 7 read the record, 12 update it, 2 delete from it (delete stays off until you grant the scope)
Scoring: ICE, PIE, RICE or a custom framework with its own dimensions and formula
Works with: Claude, ChatGPT, Codex, Cursor, Kimi, OpenClaw, Hermes and any MCP-compatible client
Publisher: Hypotize (hypotize.ai); plugin and skills repo github.com/viluca94/hypotize-plugin
Listing: chatmcp/mcpso issue #5500, October 16, 2026
```

## Why This Matters for Operators

An assistant can draft ten growth experiments before lunch, and each one sounds reasonable on its own. What it cannot do unaided is hold the line between a measured result and a confident guess, or remember that the same pricing test was already run, came in inconclusive, and was parked for a reason. That knowledge usually lives in a chat thread, a spreadsheet and someone's memory, and it evaporates.

Hypotize puts the experiment program in one structured record that both people and agents read and write. The server enforces the discipline on the agent exactly as it enforces it in the app: an experiment cannot skip a lifecycle stage, and it cannot be closed without a result and a learning. The result is that the next prompt starts from what the team already knows, not from a blank page.

## What You Can Do Today

| Capability | What it does |
|---|---|
| Read the program | List projects, load a project's context, prioritization framework and writing language, and filter the backlog and pipeline |
| Read one experiment | Hypothesis, variants, framework score, action plan, latest comments and the language to answer in |
| Read learnings | Outcomes, evidence, learnings and next steps - what the team already tested and why |
| Write hypothesis-first ideas | Create an idea in a project's backlog, with its variants when it is an A/B test |
| Score and prioritize | Record a vote in the framework (ICE, PIE, RICE or custom) and recalculate priority |
| Move the lifecycle | Transition an experiment through a validated set of stages, with no skipped steps |
| Record the outcome | Save the result, the winning variant, the learning, the evidence and the next steps together |
| Annotate as you go | Add dated comments, such as an interim reading while a test is still running |
| Import a backlog | Bring up to 50 existing experiments, variants included, into Hypotize in one all-or-nothing batch |

Two delete tools (experiment, project) are opt-in and stay off until you grant the delete scope at connection; writes are protected against duplicate requests and against silently overwriting newer work.

## Business Relevance

- **Growth and product teams** keep one record of what was tested and what it proved, so a promising idea is checked against history before it re-enters the backlog
- **Agents work to a method, not a blank page:** three bundled skills carry the workflow - `hypotize-growth-experiments` (read before proposing, follow the lifecycle, close with a measured result), `hypotize-weekly-review` (a read-only pipeline review that ends with what needs a decision) and `hypotize-backlog-import`
- **Scoring is standard:** ICE, PIE and RICE are supported out of the box, and a custom framework can define its own dimensions and formula
- **Scoped, revocable access:** read, write and delete are separate scopes chosen at sign-in, and a connection can be revoked from the project's Connections page at any time
- **Works in the assistants teams already use:** Claude, ChatGPT, Codex, Cursor, Kimi, OpenClaw and any MCP client, with a one-click Claude custom-connector link

## Integration with CorpusIQ

Experiment decisions are only as good as the data behind them, and Hypotize's record is the "why" that sits above the numbers. CorpusIQ connects the measurement side - GA4, Search Console, Google Ads, Meta Ads, Stripe, Shopify and the rest - over read-only tools, so an assistant can read the experiment record from Hypotize, pull the metric the experiment targeted from a connector, and write the measured result and learning back to the same experiment. Hypotize keeps the memory across tools and clients; CorpusIQ supplies the numbers it is measured against.

## Limitations

- **It is the record, not the test runner:** Hypotize does not run A/B tests or assign traffic, and it does not measure results itself - it stores what you and your agent report
- **Account required:** the hosted server signs in with OAuth; there is no keyless read
- **Hosted only:** the connector is a hosted remote server, not a local stdio build
- **Delete is opt-in:** destructive tools exist but are off until the delete scope is granted at connection
- **New listing:** published with the MCP server and plugin in October 2026; treat the tool surface as current for that revision (21 tools)

## FAQ

### Does the MCP server need an API key?

No key to copy. Add `https://api.hypotize.ai/mcp` as a remote MCP server (or use the one-click Claude connector link), sign in to Hypotize in the browser, and choose whether the agent gets read, write and delete access. The client then appears on the project's Connections page, where it can be revoked.

### Does it run my A/B tests?

No. Hypotize keeps the experiment record - hypothesis, score, lifecycle stage, outcome, evidence and learning - across whatever tool actually runs the test. The MCP server gives your agent a method and a memory, not test execution.
