---
title: "Should AI Models Have Veto Power Over Workflows?"
description: "The debate behind MCP governance: when an enterprise workflow is mandated, should the model be able to skip it? Why fail-closed execution is the answer for finance and compliance."
tags: [mcp, governance, runbook, agents, enterprise, debate]
---

# Should AI Models Have Veto Power Over Workflows?

There is a quiet design question underneath the enterprise agent wave: when a workflow is mandated, can the model refuse to follow it?

The default in most agent frameworks is yes. The model sees the instructions and decides. That is how assistants are built, and for open-ended tasks it is correct. The model needs freedom to reason.

But "the model decides" is not a governance model. It is a suggestion model with extra steps.

## The two positions

**Position one: the model must always be free.** Any constraint reduces capability. A model that cannot skip steps cannot improvise around missing data. Enterprise buyers should trust the model's judgment.

**Position two: freedom belongs between checkpoints, not around them.** The model reasons freely inside the workflow: how to query, how to interpret, how to phrase. What it cannot do is skip the mandated steps, call tools outside the allow-list, or claim completion without meeting the contract. Determinism lives at the host boundary. Reasoning stays free between checkpoints.

## Why position two wins in production

The failure that kills enterprise pilots is not the model being wrong. It is the model being unverifiable. When a financial report is produced, procurement and audit need to know: which systems were queried, which checkpoints passed, which sources produced each number.

That requires three things the "model decides" model does not provide:

1. **Required execution.** The workflow runs because the host requires it, not because the model felt like it.
2. **Observed checkpoints.** The host tracks the tool-call stream. The model never self-reports compliance.
3. **A receipt.** Machine-readable proof of what ran: runbook_id, version, tools called, checkpoint states, failure reason.

A model with veto power cannot produce a receipt with a straight face. It can only produce an explanation.

## The fail-closed principle

When the host cannot honor the contract, it returns runbook_failed instead of a normal answer. No silent downgrade. No "I did my best" fallback. The user sees a structured failure: this checkpoint was not reached, this connector was unhealthy, this tool was outside the allow-list.

Fail-closed is what makes the difference between an assistant and a system.

## The proposal

runbook.v1 defines exactly this: a versioned manifest resolved from a trusted skills server, executed by the host with fail-closed semantics. Zero changes to the MCP protocol. Enforcement is host-side.

- Repository: github.com/CorpusIQ/runbook-spec
- Proposal: github.com/modelcontextprotocol/modelcontextprotocol/issues/3270
- Conformance: 24/24 tests passing

The debate is real and worth having. The answer that survives contact with an auditor is the one where the model cannot skip the workflow.

Prompt compliance is not governance.
