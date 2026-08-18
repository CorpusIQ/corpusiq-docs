---
title: "Prompt Compliance Is Not Governance"
description: "An MCP server can expose a workflow, but the model decides whether to run it. For enterprise, that is a governance gap. runbook.v1 makes execution required, versioned, and auditable."
tags: [mcp, governance, runbook, enterprise, agents]
---

# Prompt Compliance Is Not Governance

Ask any AI assistant to follow a business process and it will say yes. Then it will improvise. Not out of malice, out of architecture: the model decides what to do, and a prompt is a suggestion, not a contract.

For experimentation, that is fine. For financial reporting, compliance, and product actions, it is a non-starter. An auditor does not accept "the model tried its best." A regulator does not accept "we asked it nicely."

## The gap

MCP solved the connectivity problem. A server can expose tools, resources, and workflows to any model. But nothing in the interaction model requires the model to run a workflow completely, in the right order, with the right tools, and prove it did.

The model decides. That is the design of MCP, and it is the right design for a protocol. Governance is not a protocol concern. It is a host concern.

## The missing primitive

What enterprise needs is a contract between the workflow author and the host, with the model as the reasoning engine inside it:

- **Acquisition is deterministic.** The host resolves the runbook by ID and version from a trusted skills server. No semantic search. Content hash, schema, and prerequisites are validated before the first model call.
- **Version pinning is absolute.** The exact version is bound for the life of the run, in a host-controlled instruction layer, not pasted into chat as untrusted prose.
- **The tool surface is an allow-list.** The model can only see and call declared tools. It cannot improvise with the admin tool.
- **Checkpoints are observed, not self-reported.** The host derives checkpoint state from the tool-call stream. The model never claims compliance; the host sees it.
- **Completion is host-evaluated.** The host decides when the runbook is complete and emits a machine-readable receipt: runbook_id, version, content_hash, tools_called, checkpoint_states, failure_reason.
- **Required mode is never silently downgraded.** If the host cannot honor the contract, it returns runbook_failed instead of a normal answer.

Deterministic at the host boundary. Free reasoning between checkpoints. That is the split that makes agents enterprise-grade without making them dumb.

## Why this matters now

The enterprise agent wave is hitting the same wall every new automation wave hits: pilots work, production fails, because nobody can prove what the agent did. The receipt closes that gap. When a number is wrong, the receipt shows whether the model erred or the data was bad. That clarity is what procurement requires before agents touch finance or compliance.

The vendor that provides it wins the procurement. The vendor that waits watches customers build it privately, badly, one company at a time.

## The proposal

runbook.v1 is an application-layer contract. Zero changes to the MCP protocol. The manifest resolves through existing MCP resources. Enforcement is host-side.

- Schema: schema/runbook.v1.schema.json
- Specification: spec/runbook-v1.md
- Reference implementation (Python, against the Messages API): reference/python/runbook_host.py
- Conformance suite: 24/24 passing
- Example: examples/executive-snapshot.json

Repository: github.com/CorpusIQ/runbook-spec
Proposal: github.com/modelcontextprotocol/modelcontextprotocol/issues/3270

MCP won because it made agents practical. This makes them trustworthy. In enterprise procurement, those are the same word.
