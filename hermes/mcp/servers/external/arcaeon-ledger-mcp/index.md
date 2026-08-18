---
title: "Arcaeon Ledger MCP - CorpusIQ Docs"
description: Tamper-evident action logging for AI agents — hash-chained ledger tools over one JSONL file with an external witness, built toward EU AI Act Article 12 logging.
category: Compliance
stars: n/a (new listing)
added: 2026-08-15
source: mcpservers.org
relevance: ★★
tags: [tamper-evident-logging, audit-trail, eu-ai-act, hash-chain, agent-governance, compliance, artifact-binding, self-hosted]
---

# Arcaeon Ledger MCP

**MCP tools (stdio, self-hosted via pip)** — Arcaeon Ledger is a tamper-evident, hash-chained action log for AI agents: `ledger_append` and `ledger_verify` tools over a single JSONL file with zero dependencies. An edit, deletion, or reorder breaks the record and names the exact line. Artifact binding records what the agent actually read, and an optional external witness catches the two attacks a chain alone cannot see — truncation and re-minting.

```
Server type: Self-hosted (stdio, pip install)
Auth: None (local files)
Endpoint: local JSONL file
Tools: ledger_append, ledger_verify, publish_head, verify_against_witness
Pricing: Free; hosted witness 100 pins/month free, $9/month for 2,000
Category: Compliance / Agent Governance
Built by: Arcaeon (arcaeon.io, sole-proprietor studio)
```

## Why This Matters for Operators

When an agent acts on your behalf, the first compliance question is always the same: can you prove what it did, in order, without trusting the record keeper? Arcaeon's answer is a hash chain over plain JSONL — cheap, local, and verifiable by anyone, with the vendor's own limits named in the README before the features. The companion `arcaeon-audit` package wraps it into an EU AI Act Article 12-style tamper-evident agent audit log with a regulator-ready export bundle.

**The differentiator is the honesty doctrine** — the vendor publishes what the ledger does NOT prove (truncation without a witness, truth of recorded content, authorship) next to every claim, and ships a mutation harness where every verifier check is observed catching its own planted defect.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `ledger_append` | Append an action record to the hash-chained JSONL log |
| `ledger_verify` | Verify chain integrity; a broken chain names the exact line and the failure |
| `publish_head` | Pin the ledger head to the hosted witness (public GitHub repo of pins) |
| `verify_against_witness` | Detect truncation and re-minting by comparing against the external pin |

Companion packages: `arcaeon-audit` (audit log + export bundle), `arcaeon-dedup` (context deduplication), `arcaeon-compact` (tamper-evident compaction receipts), `arcaeon-meter` (tool metering that chains decisions into the ledger), `arcaeon-baseline` (pre-registered probe sets for model swaps), `arcaeon-distill` (tool-output distiller with drop receipts).

## Installation

```bash
pip install arcaeon-ledger
python -m arcaeon_ledger.selftest          # recipe + witness proofs on your machine
python -m arcaeon_ledger.mutation_harness  # every check observed catching its planted defect
```

The MCP tools run locally over the JSONL file — no server, no keys. The witness pin store is a public GitHub repository where every pin is a commit, so the witness's own record is verifiable by strangers without trusting the API.

## Configuration

```json
{
  "mcpServers": {
    "arcaeon-ledger": {
      "command": "python",
      "args": ["-m", "arcaeon_ledger"]
    }
  }
}
```

Auth notes: none locally. The hosted witness (arcaeon-witness.vercel.app) is optional and free up to 100 pins/month; every pin carries a `next_pin_due_by` deadline so a missed pin is visible to a stranger.

## Business Relevance

- **Compliance operators** get a regulator-ready tamper-evident agent log with an export bundle, aimed at EU AI Act Article 12
- **Agencies running agents for clients** get receipts that survive hostile review, not just internal dashboards
- **Engineering managers** get pre-registered baseline probes for model swaps and quantization passes
- **Security teams** get artifact binding — the ledger records what the agent actually read, URL plus content digest

## Integration with CorpusIQ

Arcaeon composes with the catalogued compliance layer rather than competing with it. A composed workflow: AgenticRail Gate MCP enforces step order and writes signed receipts, glc PromptGuard gates prompts and tool outputs, and Arcaeon Ledger binds everything to a hash-chained record an auditor can verify offline — CorpusIQ's own OAuth-grant-scoped connectors then become the data sources whose reads get artifact-bound. For operators building ISO 42001 or EU AI Act evidence packs, the `arcaeon-audit` export bundle is the artifact that pairs with CorpusIQ connector access logs.

## Limitations

- Brand new listing — no long track record yet
- Self-hosted stdio only — no hosted MCP endpoint
- Named non-proofs: truncation without a witness, truth of recorded content, and authorship are outside the ledger's scope
- Witness is Stage-0 (free tier 100 pins/month; vendor pre-commits incident disclosure in writing)
- Sole-proprietor studio — bus factor of one, stated plainly by the vendor

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
