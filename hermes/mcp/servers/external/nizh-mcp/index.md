---
title: "Nizh MCP - Compliance Frameworks for AI Agents"
description: SOC 2, ISO 27001, CMMC 2.0 and NIST compliance programs delivered to AI agents as MCP tools - posture checks, control objectives and hash-chained attestations with evidence references
category: Compliance
stars: n/a (new listing)
added: 2026-09-04
source: "mcp.so feed"
relevance: ★★★
tags: [compliance, soc2, iso-27001, cmmc, governance, audit-trail, remote-mcp]
---

# Nizh MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1) that gives agents read access to an organization's compliance program - SOC 2, ISO 27001, CMMC 2.0, NIST and more - so they can check posture, read a control's objectives before changing code, and record where evidence lives.** One connection per organization, every tool call audited in a hash chain reviewable in the portal, and no files are ever stored - Nizh records where proof lives (a commit, a ticket), never the proof itself.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (one connection per organization)
Endpoint: https://mcp.nizh.com/mcp
Tools: 7 (compliance summary, controls, projects, attestations)
Pricing: Sign up at nizh.com
Category: Compliance & Governance
Built by: Nizh
```

## Why This Matters for Operators

The gap between "we are SOC 2 compliant" and "our agents actually operate inside the controls" is where audit findings are born. Nizh closes it by putting the compliance program in the agent's tool surface: before an agent changes code or config, it can read the control objective that governs the change and check current posture. After the change, it attaches an attestation that carries the commit SHA, PR or ticket URL - evidence by reference, not by upload.

**The hash-chained audit log makes agent actions auditable.** Every tool call lands in a tamper-evident chain your team can review in the portal, which converts "the AI did something" from a liability into a record. No uploads and no attachments mean the compliance data itself never leaves the governance boundary as files.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `get_compliance_summary` | Current posture for a project and framework |
| `list_controls` | Enumerate controls across a framework |
| `search_controls` | Find controls by keyword or scope |
| `get_control` | Requirement text, objectives and recorded evidence for one control |
| `list_projects` | Projects visible to this connection |
| `whoami` | What this connection can see |
| `attest_control` | Append an attestation with references (commit SHA, PR or ticket URL) and short text |

## Installation

```bash
claude mcp add nizh --transport http https://mcp.nizh.com/mcp
```

Works with Claude, Cursor, VS Code and any MCP client that supports remote OAuth servers. Sign up at nizh.com first - one connection per organization.

## Configuration

```json
{
  "mcpServers": {
    "nizh": {
      "type": "http",
      "url": "https://mcp.nizh.com/mcp"
    }
  }
}
```

On first connect the client opens a browser window for OAuth 2.1 sign-in; the connection is then scoped to your organization's compliance program.

## Business Relevance

- **CTOs and engineering leads** make compliance readable to the agents that write the code - control objectives are checked before changes, attestations reference real commits
- **Compliance officers** get a hash-chained audit trail of every agent tool call instead of a spreadsheet of after-the-fact claims
- **Auditors and security reviewers** see posture summaries and control evidence without digging through repos

## Integration with CorpusIQ

CorpusIQ delivers governed read-only business data to agents; Nizh delivers governed compliance context. Together they form a two-layer control story for agentic operations: CorpusIQ provides the business facts an agent needs, Nizh provides the framework rules it must satisfy - posture, controls and attested evidence - before acting. Operators running agent workflows inside SOC 2 or ISO 27001 scope can pair Nizh's attestation trail with CorpusIQ's read-only connector policy as complementary governance surfaces.

## Limitations

- Read and attest only - no evidence-file uploads (by design; references only)
- One OAuth connection per organization - multi-tenant setups need multiple connections
- Brand new listing - framework coverage depth beyond the named four is early
- Commercial pricing not published

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Raposa Aval MCP - Human Approval Gates with Audit Chains](/hermes/mcp/servers/external/raposa-aval-mcp)
- [Fallax MCP - Phishing Simulation Results for Audit Evidence](/hermes/mcp/servers/external/fallax-mcp)
- [mcp-sanctions - Watchlist Screening for KYC and AML](/hermes/mcp/servers/external/mcp-sanctions)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
