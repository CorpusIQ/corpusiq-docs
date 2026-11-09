---
title: "Vericto MCP - SQL Guardrails Before the Query Runs"
description: "An agent gets SQL without getting DROP: every statement is checked against your rules before it runs, and sensitive columns come back masked."
category: Data Infrastructure
stars: "n/a (hosted, plus an AGPL-3.0 proxy image)"
added: 2026-11-08
source: "chatmcp/mcpso submissions #6960, #6961 and #6962 filed 2026-11-09T00:58:11Z to 00:58:13Z; the official MCP registry records com.vericto/mcp, com.vericto/vericto-proxy and com.vericto/account; the vendor documentation at vericto.com/docs/mcp; and the endpoints themselves, where a keyless initialize answered HTTP 401 naming the header it wants"
relevance: ★★★★
tags: [database, sql, guardrails, agent-governance, data-masking, audit-trail, postgres, mysql, remote-mcp, open-source]
last_updated: "2026-11-08"
---

# Vericto MCP

**The useful question about an agent and a database is not whether it can read the data. It is what the agent is allowed to do to it, and who can prove afterwards what it did.** Vericto is a control layer that sits between the agent and the database: every statement is parsed into an abstract syntax tree, checked against rules written on that tree rather than on the query text, and only then allowed to run. Three surfaces expose it, and one of them needs no account at all.

```text
Server type: Remote (Streamable HTTP), plus a local Docker proxy and a CLI
Endpoint:    https://mcp.vericto.com/mcp            (API key: X-API-Key or Authorization: Bearer)
             https://mcp.vericto.com/mcp/account    (OAuth 2.1 with PKCE, per workspace)
             docker run vericto/vericto-proxy:5.0.0 mcp   (read-only Postgres, AGPL-3.0-only)
Registry:    com.vericto/mcp, com.vericto/vericto-proxy, com.vericto/account
Docs:        vericto.com/docs/mcp
Licences:    engine, proxy and CLI AGPL-3.0; SDKs and the CI Action Apache-2.0
Verdicts:    BLOCKED, with a rule id and a suggested fix
```

## What the endpoint says about itself

Started with no credential, the API-key surface answers **HTTP 401** before it will list a single tool:

```json
{"error":{"code":"UNAUTHORIZED","message":"API key required. Send it in the X-API-Key header or as Authorization: Bearer ..."}}
```

That is the integration tier this entry rests on, stated plainly rather than implied: **live and gated, documented from the vendor and from its own open-source proxy, not driven.** The account surface is the one to use when a person rather than a service holds the credential: OAuth 2.1 with PKCE and both client registration paths, read scopes preselected on consent and the SQL-check and write scopes opt-in, with a free plan behind public sign-up. The proxy surface is the one to use when nobody wants a third party in the path at all.

## The finding is the shape of the control, not the feature list

Three of the four design decisions recorded here are visible in the proxy, because the proxy is published as a container and states its own behaviour: with no Vericto account it applies the built-in rules - destructive statements, a missing `WHERE`, risky DDL, data exposure - and **reports nothing anywhere**, so the free tier is a local guard rather than a free trial that phones home. Every call runs in a **read-only transaction that ends in `ROLLBACK`**, and the machine runs exactly the statement it checked, which closes the gap between what was inspected and what was executed. That gap is where most guardrail products quietly fail.

The rest of the surface, read from the vendor's own documentation:

- **Rules on the AST, not on the query text.** A pattern match against SQL text is defeated by a comment, a subquery or an encoding change. Parsing first means the rule sees the operation.
- **Per-agent allowlists of tables and columns**, so the reporting agent and the migration agent do not get the same database.
- **Column masking in the result**, which keeps a card number or an email address out of the model context even when the query is legitimate.
- **Observe before enforce**, plus a kill switch per policy, which is the only rollout path that does not break a working system on day one.
- **A rule simulator** that tests a rule change against real traffic before it is switched on.
- **An audit trail of every decision, with signed reports**, which is the half that turns a guardrail into evidence for a SOC 2 or ISO 27001 auditor.
- **CI checks** that fail a pipeline on a destructive migration, through the same engine:

```text
$ vericto check migrations/*.sql
BLOCKED VERICTO-001 DELETE without WHERE
fix -> DELETE ... WHERE id = $1
exit 0 - ship it
```

A database proxy that only guards the chat is half a product; one that guards the deploy as well covers the path that actually destroys data.

## What this changes for an operator

CorpusIQ connects to a database read-only, and that is the right default for a question-answering assistant. The moment a business gives an agent any write path - a coding agent drafting a migration, a text-to-SQL tool inside an internal app, an automation that closes out records - read-only stops being the control and policy has to take over. This catalogue already carries the compliance version of that idea: [DutyKit](/hermes/mcp/servers/external/dutykit-mcp/) pre-checks a marketing action against German law and returns a three-valued verdict that hands the ambiguous case to a person. Vericto is the same instinct applied to the database: decide before the statement runs, and keep the receipt.

## Limits, stated as limits

The tool list is not published to an unauthenticated caller, so this guide cannot quote tool names the way it quotes schemas elsewhere in the catalogue. Vericto is a control layer and not a data source: it returns no business facts of its own. The proxy has to be on the connection path, or the application has to call the check, so it is an architecture decision rather than a click. And rule authoring is a project: a team that has never written a policy will get value from the built-in rules first and from its own rules later.

## Frequently asked questions

### What stops an agent from dropping a table?

A rule evaluated on the parsed statement, before execution, returning `BLOCKED` with the rule id and a suggested replacement. The proxy variant additionally runs every statement inside a read-only transaction that rolls back, so a write that slipped past the rules still cannot commit through that path.

### Does Vericto see the rows?

It sits in the query path, so it can mask columns in the result. The free proxy tier states that it reports nothing anywhere when no account is connected, and the paid surfaces add the audit trail and signed reports, which is the opposite trade: more visibility in exchange for the evidence.

### Can it guard a deploy and not just a chat?

Yes. The same engine runs as a CI check over migration files, which is why the CLI example above fails a pipeline rather than a conversation.

### What does it cost?

A free plan with public sign-up on the account surface, an open-source proxy under AGPL-3.0 that needs no account, and paid tiers behind a 99.9% SLA with dedicated deployments at 99.95% and 99.99%. This guide does not quote per-seat pricing because the vendor's page states the SLA numbers and leaves the seats to a sales conversation.
