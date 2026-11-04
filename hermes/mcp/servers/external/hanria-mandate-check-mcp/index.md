---
title: "HANRIA Agent Mandate Check MCP - Written Consent Gates"
description: "Keyless MCP that checks a proposed agent action against an operator's written mandate and answers permit, deny or escalate with a signed receipt."
category: Compliance
stars: n/a (hosted, no public repository)
added: 2026-11-03
source: "chatmcp/mcpso submission #6696 on 2026-11-03 at 23:50:38Z, plus a keyless driven session on https://check.hanria.ai/v1/mcp: initialize 200 as hanria-check 0.7.4, tools/list returning check_action and validate_mandate, a validated 3-clause mandate and four actions checked with signed receipts"
relevance: ★★★
tags: [agent-governance, mandate, authorization, guardrails, receipts, policy, remote-mcp]
last_updated: "2026-11-03"
---

# HANRIA Agent Mandate Check MCP

**Every serious agent stack eventually has the same conversation: who wrote down what this agent is allowed to do, and what does the agent read when it is about to do something that was never written down? A prompt is not a policy, and a policy in a document nobody reads is not a control either.**

HANRIA puts the missing middle in one hosted MCP endpoint. The operator writes a mandate, the agent passes that mandate plus the action it is about to take to `check_action`, and the answer is `permit`, `deny` or `escalate` with the clause that decided it and a signed receipt. The server is keyless and needs no account:

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://check.hanria.ai/v1/mcp
Auth:        none
serverInfo:  hanria-check 0.7.4
Tools:       2 (check_action, validate_mandate)
Resources:   5 mandate templates, one write_mandate prompt
Licence:     none published; no repository on the card
Site:        hanria.ai
```

A keyless `initialize` answered **HTTP 200** with `protocolVersion 2025-06-18`, and `tools/list` returned both tools with full schemas. Nothing here needs a credential, which is why the surface could be driven rather than quoted.

## The mandate is a document, and the document is the point

A mandate is an object with a `schema_version`, a `mandate_id`, a `purpose`, a `default` for anything no clause covers, and an ordered list of clauses. Each clause carries an `id`, an `effect` of `permit`, `deny` or `escalate`, and a `match` over the proposed operation. The **first matching clause decides**, which makes clause order part of the policy rather than an implementation detail.

The operation taxonomy is closed and short, and knowing it is the difference between a mandate that validates and one that does not: `file`, `process`, `package`, `network`, `device`, `credential_use`, `transaction`, `administrative`. An action is described by `kind`, `verb`, `target`, an optional `amount` with a decimal string and a currency, and a `justification`, plus a `requested_by` block naming the agent and optionally the session and the person it acts for.

The server ships five templates as MCP resources: `payments-ceiling`, `file-sandbox`, `outbound-email`, `deploy-gate` and `read-only-research`, all readable at `hanria://mandates/<name>`. Starting from a template is not a convenience, it is the supported path, because the schema is strict enough to reject a hand-written clause over a single extra field.

## What this pass actually drove

A three-clause mandate was written for a documentation publisher and validated. The answer came back `valid: true`, `clauses: 3`, `expired: false`, a `mandate_digest` of `2efbcf8d9f97dd5e912707b75d1fb61a15ccb8d344a5c16c4a1f855c5437de17`, and the reason `the mandate is well formed: 3 clause(s), and the default for anything no clause covers is escalate`.

Four actions were then checked against it, and the four outcomes are the whole product in one table:

| Proposed action | Outcome | Clause reported |
| --- | --- | --- |
| `network` / `post` to `https://api.github.com/repos/CorpusIQ/corpusiq-docs/pulls` | `permit` | `permit-docs-publish` |
| `network` / `post` to an unrelated organisation's issues endpoint | `escalate` | none matched, so the mandate default applied, with the closest clause named |
| `transaction` / `pay` to a payment processor | `deny` | `deny-transactions` |
| `administrative` / `grant` on a repository role | `escalate` | `escalate-admin` |

The escalation that no clause covers is the most useful answer of the four. It does not fall back to a bare refusal: it explains that no clause matched, that the mandate default therefore applies, and that the closest clause was `permit-docs-publish` whose permitted prefix the target failed. That sentence tells an operator what to add to the mandate, which is what a policy engine usually leaves them guessing.

Every answer also carried a `receipt`: type `hanria-receipt-v1`, a `kid`, the `mandate_digest`, the `action_digest`, an `issued_at` and a `not_after` fifteen minutes later, and an Ed25519-style `signature` over the decision. The decision is a record someone else can verify later, not just a message to the caller.

## Validation catches the mistakes that make a policy decorative

`validate_mandate` is not a schema linter. It reports clauses that can never run because an earlier clause already decides them, unbounded prefixes, credential material found in a mandate, and expiry. A clause that is unreachable is the exact failure mode of hand-written policy: the rule exists, the operator believes it applies, and the first matching clause upstream has already answered.

The strictness was demonstrated the hard way in this pass. A first attempt used `kind` values of `payment` and `access` plus a free-text `reason` field on each clause. The validation refused it three ways: the outcome was `error`, which the vendor instructs clients to treat as a deny, and the message named the offending field and the accepted `kind` values rather than returning a generic failure. A second attempt passed cleanly.

## What the surface is honest about, and what it is not

The server states its own ceiling in the tool description: a mandate is **advisory**, it describes intended authority and supports a local check, and enforcement requires a component that exclusively holds the credentials and can refuse. Everything here is guidance to a cooperative agent, plus a record that it asked. Nothing prevents an agent that never calls the tool, and the vendor says so instead of implying a fence it does not operate.

There is no listing tool and no server-side mandate store, so the mandate travels with the request and lives wherever the client keeps it. The check therefore proves what the agent asked and what the answer was, which is an audit question, and not what the agent then did, which is an enforcement question. Pair it with a gate that holds the credentials when the difference matters.

## Why this earns a guide

The catalogue carries agent governance as separate pieces: [AgenticRail Gate MCP](/hermes/mcp/servers/external/agenticrail-gate-mcp/) enforces deterministic step order and verifies a hash-chained receipt chain, [AgentLedger MCP](/hermes/mcp/servers/external/agentledger-mcp/) caps and records spend, [agent-bom MCP](/hermes/mcp/servers/external/agent-bom-mcp/) maps the blast radius of an agent's supply chain, and [glc PromptGuard MCP](/hermes/mcp/servers/external/glc-promptguard-mcp/) scores a prompt or a tool output.

None of them holds an **operator-authored authorisation document** with clauses, ordering and a three-way outcome. AgenticRail answers "did the right steps run in the right order" from a sequence definition; HANRIA answers "was this action ever granted, by whom, and what happens when the mandate is silent" from a written mandate. On an operator surface the second question is the one that arrives before the first, because it is the question a founder asks about their own agent.

## FAQ

### Do I need an account or a key?

No. `initialize` and `tools/list` answer without a credential, and both tools can be called keyless. That is also why this entry was driven rather than documented.

### What happens when no clause matches?

The mandate's `default` applies, which is `escalate` in every shipped template. The reason string names the closest clause and why it did not match.

### Can it stop an agent from acting?

No. The vendor states the mandate is advisory and that enforcement needs a component holding the credentials that can refuse. HANRIA produces the decision and the receipt, and something else has to act on it.

### Is the decision verifiable later?

Each answer carries a `hanria-receipt-v1` receipt with the mandate digest, the action digest, an issue time, a fifteen-minute window and a signature. The check is confirmable by a third party, and the server keeps no request content.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [AgenticRail Gate MCP - Deterministic Step-Order Enforcement](/hermes/mcp/servers/external/agenticrail-gate-mcp/)
- [AgentLedger MCP - Per-Agent Spend Management for Operators](/hermes/mcp/servers/external/agentledger-mcp/)
- [agent-bom MCP - The Blast Radius of an AI Supply Chain](/hermes/mcp/servers/external/agent-bom-mcp/)
- [glc PromptGuard MCP](/hermes/mcp/servers/external/glc-promptguard-mcp/)
