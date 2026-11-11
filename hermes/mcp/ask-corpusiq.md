---
title: "ask_corpusiq: Deterministic Single-Tool Access to Business"
description: "ask_corpusiq is the high-level CorpusIQ MCP tool: it routes a business question through the engine in router-first or runbook mode"
canonical: "/hermes/mcp/ask-corpusiq/"
robots: "index, follow"
tags: [mcp, corpusiq, ask-corpusiq, router, runbook, deterministic, tool]
last_updated: "2026-11-10"
---

# ask_corpusiq: Deterministic Single-Tool Access to Business Data

`ask_corpusiq` is the high-level MCP tool that gives AI clients a single
entry point to the user's connected business data. Instead of exposing
dozens of connector tools and letting the model decide which to call, the
client sees one tool. CorpusIQ decides the rest: which skill to run, which
connectors to use, how to validate, and how to answer.

## Why one tool

Every tool exposed to a client model is a decision point. Models are good
at tool selection, but the selection is not deterministic. A user question
about revenue could route to QuickBooks, Stripe, or a generic answer
depending on the model's judgment. The one-tool design minimizes model
discretion: the model makes a single decision (does this question need
CorpusIQ?), and control transfers to the engine.

## Modes

- Router-first: the engine resolves intent, selects the skill, and routes
  to the required connectors
- Required-runbook: a named runbook is bound by version, validated, and
  executed fail-closed. If the runbook cannot complete, the tool returns
  `runbook_failed` instead of a normal answer

## Execution guarantees

- Pinned allowlisted execution: only connectors and tools declared for the
  skill are reachable
- JWT enforcement: every call is authenticated and attributed
- Bounded failures: errors fail fast with a machine-readable receipt
- Evidence: every number in the answer carries a source reference
- Routing metadata: the answer records which skill, version, and connectors
  produced it
- Execution receipts: a machine-readable record of what ran, in what order,
  and the result of each step

## Relationship to runbook.v1

`ask_corpusiq` is the production implementation of the runbook.v1 execution
contract. The specification and reference implementation are public at
[github.com/CorpusIQ/runbook-spec](https://github.com/CorpusIQ/runbook-spec).
The governance proposal was filed in the MCP repository as issue #3270 and is
now closed; the specification and conformance suite live in the runbook-spec
repo.

## Related pages

- [runbook.v1 governance](/hermes/mcp/runbook-governance)
- [runbook.v1 response contract](/hermes/mcp/runbook-response-contract)
- [MCP Apps: interactive UIs](/hermes/mcp/mcp-apps-interactive-ui)
