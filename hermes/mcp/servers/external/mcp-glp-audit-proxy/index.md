---
title: "GLP Audit Proxy MCP - Tamper-Evident Tool-Call Trail"
description: "MIT stdio proxy that hash-chains every MCP tool call into an append-only audit trail, with deny-by-default allowlists and role separation."
category: Compliance
stars: 0
added: 2026-10-20
source: "mcpservers.org /all page 2 via the r.jina.ai reader proxy (antonio-castellon/mcp-glp-audit-proxy)"
relevance: ★★
tags: [compliance, audit-trail, glp, 21-cfr-part-11, gmp-annex-11, alcoa, hash-chain, rfc8785, mcp-proxy, python]
---

# GLP Audit Proxy MCP

**A proxy that records what an agent did, in a form an auditor can verify** - every mediated call, including the denials and the failures, becomes one canonical-JSON line in an append-only SHA-256 chain, with the caller's identity, role and reason attached.

```
Server type: Local stdio proxy (Python), no HTTP listener in 0.1.0
Package: mcp-glp-audit-proxy 0.1.0 on PyPI (MIT, author Antonio Castellon, Python 3.11 to 3.13, Development Status 3 - Alpha)
Install: pip install mcp-glp-audit-proxy
Run: mcp-glp-audit-proxy --config config.json
Env: GLP_PRINCIPAL_ID, GLP_PRINCIPAL_NAME, GLP_PRINCIPAL_ROLE
Repo: github.com/antonio-castellon/mcp-glp-audit-proxy, default branch main, created 2026-10-18, last push 2026-10-19
Tools: role dependent. qa, approver and admin see glp_verify_chain, glp_search_audit, glp_export_audit; operator sees only the proxied upstream tools, exposed as server__tool
```

Verified live in this sweep, from a clean virtual environment: `initialize` returned serverInfo `mcp-glp-audit-proxy 0.1.0` on protocol 2025-06-18, and every method was written to the trail as it happened - `audit/startup`, `initialize`, `notifications/initialized`, `tools/list`, eleven entries for one session.

## Why This Matters for Operators

An agent with write access to a lab spreadsheet, an ELN or a LIMS is a regulated activity the moment the work feeds a submission. The question a QA reviewer asks is not "was the agent right", it is "show me who changed what, when, and why, in a form I can verify".

Most agent stacks cannot answer that, because the audit trail lives in a chat transcript that the agent can edit or the vendor does not keep. This proxy moves the record out of the conversation and into a file whose integrity you can check: each entry is RFC 8785 canonical JSON, `entry_hash` is the SHA-256 of that object with the hash removed, and `prev_hash` links it to the previous entry, with 64 zero digits for the first. A sidecar `.head` file makes a cut of whole trailing lines fail verification.

The design decision worth respecting is that auditing cannot be switched off. A `glp_update_policy` call with `audit_enabled: false` is denied and logged as a denial. A control an operator can disable under pressure is not a control.

## Tools & Capabilities

Role separation is enforced, and the tool surface changes with the role - which is why an operator connection with no upstreams shows an empty `tools/list`:

| Role | May call upstream tools | Sees on the trail |
|---|---|---|
| `operator` | yes, subject to the allow and deny lists | nothing beyond the forwarded tools |
| `approver` | no | `glp_search_audit`, `glp_export_audit`, and may record an approval |
| `qa` | no | `glp_verify_chain`, `glp_search_audit`, `glp_export_audit` |
| `admin` | no, explicitly | policy changes plus the read tools |

The three audit tools, read from a live `qa` session:

| Tool | What it returns |
|---|---|
| `glp_verify_chain` | integrity result plus the head hash and entry count. Observed: `chain ok entries=11 head=6669451c...` |
| `glp_search_audit` | matching entries, filterable by record class, tool, principal, status, method, server and a time range |
| `glp_export_audit` | a searchable JSON export with a hash manifest, written to a path you name. Explicitly not a PDF |

Every record carries: principal id, name and role, the tool, inputs, outputs, a UTC timestamp with the offset, the protocol version, an optional session id, a record class (`gxp_data`, `access`, `technical`, `config`), the reason for a write, `prev_hash` and `entry_hash`, with `hash_algo` and `canonicalization` stored on the entry itself.

## Installation

```bash
pip install mcp-glp-audit-proxy
```

The `mcp` dependency is pinned to `>=2.2.0,<3`, a floor chosen to sit outside GHSA-84m7-p3x7-pcfv, and the process refuses to start on an older SDK.

```bash
export GLP_PRINCIPAL_ID=operator-1
export GLP_PRINCIPAL_NAME="Ada Analyst"
export GLP_PRINCIPAL_ROLE=operator
mcp-glp-audit-proxy --config config.json
```

Verify a chain, and print the head to paste into a ticket, an email or a LIMS record:

```bash
mcp-glp-audit-proxy-verify data/audit.jsonl --json-export exports/audit.json
mcp-glp-audit-proxy-verify data/audit.jsonl --tool excel__write_cell --status ok
mcp-glp-audit-proxy-verify data/audit.jsonl --print-head
```

The verify CLI was run in this sweep: it returned `chain ok entries=12 shown=12` with a head hash and then listed each entry as `seq=1 time=... class=config status=ok principal=operator-1 role=operator method=audit/startup tool=- server=proxy`.

## Configuration

`config.json` decides the policy, the retention profile and the upstream servers:

- **Policy.** Shell-style globs on the exposed tool name (`excel__write_cell`). Deny wins over allow, and an empty allow list denies every upstream tool. Write tools require a reason by default, read from `_meta` or from a `_glp_reason` argument that is stripped before the call is forwarded.
- **Approval.** Optional per write: the call is held until a different person in the `approver` role records `approved`. An approval is single-use, bound to the SHA-256 of the canonical `{tool, arguments}` and expires (3,600 seconds by default). The vendor states plainly that this is not an electronic signature.
- **Retention.** The default is the Swiss GLP profile: 10 years after study completion with a floor of 6 months and a legal-hold flag that refuses disposal. The JSONL backend has no delete.
- **Fail closed.** The store is checked before a call is forwarded. If the append after a successful upstream call fails, the upstream payload is not returned to the host, and the vendor ships a reconciliation SOP for the case where the upstream may already have applied the write.

Upstreams are declared with a name, transport, protocol and command; the proxy reaches them over stdio or HTTPS, and receives a safe environment allow-list rather than your whole environment.

## Business Relevance

**Regulated labs and manufacturing.** The coverage table is specific rather than aspirational: OECD GLP No. 17 clause 3.4 and Swiss GLPV Annex 2, FDA 21 CFR Part 11 11.10(e), EU GMP Annex 11, MHRA and PIC/S PI 041-1, WHO TRS 1033 and ALCOA+, and EU AI Act Article 12 automatic event logging. Each is mapped to a clause by clause matrix in `docs/COVERAGE.md`, and the vendor is careful to say meeting them still depends on your validated use and SOPs.

**The AI Act angle for anyone else.** Article 12 event logging and a six-month minimum retention is now a general requirement, not a pharma one. This is the cheapest way to have that evidence for an agent that touches production systems.

**Segregation of duties on one machine.** Operator, approver, QA and admin as local roles means a single developer's laptop can demonstrate the four-eyes control an auditor expects before the platform team builds it.

## Integration with CorpusIQ

This is the mirror image of [drift](/hermes/mcp/servers/external/drift-mcp). drift refuses an action before it happens, on the basis of a signed mandate; this records what happened after, in a verifiable chain, with the reason and the role attached. Neither one alone answers "was the agent allowed to do that and what actually happened" - together they do.

For our own stack the pattern is transferable without adopting the product: an append-only, canonical-JSON, hash-chained record of tool calls, written by a proxy the agent does not control, is the right shape for any agent governance claim we make. It also sets the bar for what "audit log" should mean when a customer asks - a transcript is not an audit trail.

## Limitations

- **Community edition is not a Part 11 e-signature.** The approval record is labelled `approval` and is explicitly not an electronic signature; Part 11 signatures, WORM storage, signing and reports are Pro features under a separate licence.
- **A sidecar is not a defence on its own.** Someone who can edit both the log and the `.head` file can move them together. The vendor's own position is that the external copy is the control - print the head and keep it somewhere else.
- **Stdio only in 0.1.0, and it must sit in front of the client.** There is no HTTP listener, so the proxy has to be the thing the client launches, not a sidecar you add later.
- **Two days old.** Repository created October 18, 2026, zero stars, one maintainer, version 0.1.0, alpha. The audit format and the crypto are simple enough to read; read them before this carries evidence you care about.
- **It records, it does not judge.** A permissive allow list produces a perfect trail of an over-privileged agent.

## FAQ

### Why does an operator connection show no tools?

Because the trail tools are for the reviewing roles, not the acting one, and the proxied upstream tools only appear when upstreams are configured. An operator with no upstreams has nothing to call, which is the intended least-privilege shape rather than a fault - verified in this sweep, while the same config under the `qa` role returned the three trail tools.

### How is a denial recorded?

As a record like any other, with `policy_decision` naming the rule and the action `deny`, and the reason attached. Denials and failures are the entries an auditor reads first, which is why they are logged even though nothing executed.

### What stops the agent from editing the log?

The log is written by the proxy process, which the host launches and the agent talks to - the agent never holds the file handle. That is a real boundary for an agent, and not a boundary against a person with shell access on the same machine. For that threat the external head-hash copy is the control the vendor names.

### Can I put this in front of servers I already run?

Yes, that is the whole point: name your existing servers as upstreams and the proxy becomes the only path between the host and them, applying the allow and deny lists, the reason requirement, the approval hold and the audit write to every call.

### Does it work with a remote MCP server?

Yes for the upstream side, over HTTPS with TLS 1.3 and no token passthrough. On the host side it is stdio in 0.1.0, so a remote client cannot connect to it directly.

## See Also

- [drift MCP - Pre-Action Mandate Enforcement for AI Agents](/hermes/mcp/servers/external/drift-mcp)
- [AgenticRail Gate MCP - Step-Order Enforcement with Signed Receipts](/hermes/mcp/servers/external/agenticrail-gate-mcp)
- [Azquo MCP - Audited Shared Memory for AI Agents](/hermes/mcp/servers/external/azquo-mcp/)
- [Poison Armor MCP - Prompt-Injection Firewall](/hermes/mcp/servers/external/poison-armor-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
