---
title: "runbook.v1: Governed Workflow Execution for MCP"
description: "runbook.v1 is an application-layer contract for MCP that makes enterprise workflow execution required, versioned, and auditable. Deterministic at the host boundary, free reasoning between checkpoints. Schema, reference implementation, and conformance suite."
tags: [mcp, runbook, governance, workflows, enterprise]
---

# runbook.v1: Governed Workflow Execution for MCP

MCP servers can expose a tool or workflow, but the model decides whether to invoke it and how completely to follow it. For enterprise workflows, execution must be required, versioned, and auditable. Prompt compliance is not governance.

runbook.v1 is an application-layer contract for MCP that makes governed execution possible today, with zero changes to the MCP protocol.

## What is a runbook

A runbook is a versioned manifest resolved from a trusted skills server and executed by the host with fail-closed semantics:

```json
{
  "runbook_id": "executive-snapshot",
  "version": "4.2.0",
  "mode": "required",
  "failure_policy": "fail_closed",
  "allowed_tools": ["quickbooks_profit_and_loss", "stripe_revenue", "ga4_sessions"],
  "checkpoints": [
    {"id": "cp-revenue-qb", "kind": "tool_call", "required": true,
     "match": {"tool": "quickbooks_profit_and_loss"}},
    {"id": "cp-emit", "kind": "condition", "required": true,
     "condition": "final_output"}
  ],
  "completion": {"condition": "final_output", "receipt": true}
}
```

## How it works

1. The host resolves the runbook by ID and version from a trusted skills server. No semantic search.
2. Content hash, schema, and prerequisites are validated before the first model call. Missing prerequisites fail closed.
3. Instructions are bound into a host-controlled instruction layer, not pasted into chat as untrusted prose.
4. The tool surface is an allow-list. The model can only see and call declared tools.
5. Checkpoints are observed from the tool-call stream. The model never self-reports compliance.
6. Completion is host-evaluated and emits a machine-readable receipt: runbook_id, version, content_hash, tools_called, checkpoint_states, result_summary, failure_reason.
7. Required mode is never silently downgraded. If the host cannot honor the contract, it returns runbook_failed instead of a normal answer.

## Design principles

- **Deterministic at the host boundary, free reasoning between checkpoints.** Acquisition, version pinning, tool constraints, checkpoint tracking, and fail-closed semantics are deterministic host functions. Everything between checkpoints is ordinary model reasoning.
- **No protocol change.** The manifest resolves through existing MCP resources. Enforcement is host-side.
- **The closest existing primitive is tool_choice forcing**, which proves forced selection is practical but covers one bounded call. A runbook governs multiple turns and multiple connector calls, which is why the contract lives in the host loop rather than a single API request.

## Use cases

- Reproducible analytics
- Financial reporting (revenue reconciliation across QuickBooks, Stripe, GA4)
- Compliance workflows with mandatory validation steps
- Source restrictions
- Product actions that must execute a known business process
- Scheduled executive briefs

## Invocation

Any of three application-controlled triggers, all through the same API surface:

1. Explicit user action: a "Run cash-recovery plan" button, deep link, or command
2. Product event: customer connects QuickBooks, onboarding fires the runbook
3. Schedule: weekly executive brief

Every invocation is user-visible and cancellable. This is deterministic orchestration with user controls, not hidden automation.

## Reference implementation

- Schema: schema/runbook.v1.schema.json
- Specification: spec/runbook-v1.md
- Reference host implementation (Python, against the Messages API): reference/python/runbook_host.py
- Conformance suite: 24/24 tests passing
- Example: examples/executive-snapshot.json

Repository: github.com/CorpusIQ/runbook-spec

## FAQ

### Does this require MCP protocol changes?

No. The manifest resolves through existing MCP resources. Enforcement is host-side. MCP core remains exactly as thin as designed.

### How is this different from prompt instructions?

Prompt instructions are untrusted prose competing with the model's attention. A runbook is a host-enforced contract: versioned, hashed, allow-listed, checkpointed, and receipted. The model cannot silently skip it.

### Who can author runbooks?

Trusted skills servers publish them. The host verifies content hashes and prerequisites before execution.

### Is this available today?

The reference implementation and conformance suite are public and passing. CorpusIQ operates governed runbooks in production as part of its skills framework.
