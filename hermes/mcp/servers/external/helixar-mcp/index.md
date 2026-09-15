---
title: Helixar MCP - Supply-Chain Security Scanning for MCP Servers
description: Agentic-AI security tools exposed as an MCP server. Scan any MCP server against 26 Sentinel detection rules before installing it, validate HDP delegation chains against the IETF draft, and run ReleaseGuard artifact checks. Public no-auth endpoint with two remote tools confirmed by live probe plus a third stdio-only tool.
category: Security
stars: n/a (new listing)
added: 2026-09-04
source: mcpservers.org
relevance: ★★★
tags: [mcp-security, supply-chain, vulnerability-scanning, sentinel, hdp, security, remote-mcp]
---

# Helixar MCP

**Remote MCP server (Streamable HTTP, public in v1)** - three agentic-AI security tools: scan any MCP server against Sentinel detection rules before installing it, validate HDP (Human Delegation Provenance) delegation chains, and check release artifacts for secrets and metadata leaks. Two tools remote, one stdio-only; OAuth lands with Phase 8.

```
Server type: Remote (Streamable HTTP) + stdio for the full three-tool set
Auth: None in v1 (public); deep-mode Sentinel and Phase 8 add keys/OAuth
Endpoint: https://mcp.helixar.ai/mcp
Tools: 2 remote (helixar_inspect_mcp, helixar_hdp_validate) + 1 stdio-only (helixar_releaseguard)
License: Apache-2.0 · Repo: Helixar-AI/helixar-mcp (org: Helixar-AI/HDP)
```

## Why This Matters for Operators

MCP adoption is a supply-chain problem: every directory listing promises capability, and nothing verifies safety. Helixar's Sentinel scan is a pre-install gate - **an operator pastes a manifest URL and gets a risk score, findings and a security brief before the server is ever added to a client.** The quick mode runs 8 rules free and authless; deep mode runs all 26 with an API key.

The fixture in the vendor repo shows what it catches: missing auth blocks, plaintext transport, destructive tools without confirmation requirements, unbounded data dumps, sensitive field names in tool descriptions, and prompt-injection phrasing aimed at the calling model - each finding tagged with a severity and rule id. The HDP validation tool is the governance half: it checks delegation chains against the IETF draft, surfacing scope escalations, depth violations, expired hops and missing signatures with citations to the draft and a Zenodo DOI.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `helixar_inspect_mcp` | Scan an MCP server (URL or raw manifest JSON) against Sentinel rules; risk score, findings, Claude-generated brief. Quick mode free + authless (top 8 rules); deep mode runs all 26 with an API key |
| `helixar_hdp_validate` | Validate an HDP delegation chain against IETF draft-helixar-hdp-agentic-delegation-00; flags scope escalations, depth violations, expired hops, missing signatures |
| `helixar_releaseguard` | Wraps Helixar-AI/ReleaseGuard: quick mode scans dist/ artifacts for secrets, metadata leaks, license gaps; deep mode runs the full harden pipeline. Requires the releaseguard binary on PATH; stdio-only |

Both remote tools were live-probed and confirmed in this sweep (serverInfo helixar-security v0.0.1).

## Installation

```bash
claude mcp add --transport http helixar https://mcp.helixar.ai/mcp
```

No auth in v1. For the full three-tool set including `helixar_releaseguard`, clone the repo, build (`npm install && npm run build`) and point the client at `node /absolute/path/to/dist/server.js`.

## Configuration

```json
{
  "mcpServers": {
    "helixar": {
      "url": "https://mcp.helixar.ai/mcp"
    }
  }
}
```

Smoke-test the live server with `curl https://mcp.helixar.ai/health` or a JSON-RPC tools/list POST. The Workers deployment exposes two of three tools; the ReleaseGuard tool has no Workers equivalent.

## Business Relevance

- **MCP adoption governance** gets a pre-install scan gate with rule ids for every finding.
- **Security teams** audit third-party servers before they reach internal clients.
- **Agent platform operators** validate delegation chains and catch scope escalations.
- **Release pipelines** run artifact checks for secrets, metadata leaks and license gaps.

## Integration with CorpusIQ

CorpusIQ publishes MCP servers and connects to dozens of third-party ones - exactly the surface Sentinel scans. A CorpusIQ agent evaluating a new connector can run the manifest through `helixar_inspect_mcp` first and cite the findings in the adoption decision, keeping the same evidence trail CorpusIQ's governance workflows already produce.

## Limitations

- v1 is public and unauthenticated; OAuth and keys arrive with Phase 8 (deep-mode Sentinel already keyed).
- Only two of three tools are remote; ReleaseGuard requires a local binary.
- Young connector repo (0 stars, v0.0.1 server); the underlying HDP protocol repo (Helixar-AI/HDP) is more established.
- Risk scores are detection rules, not a guarantee - deep mode covers more rules than quick mode.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [CTlogs.io MCP - Certificate Transparency Search for Agents](/docs/hermes/mcp/servers/external/ctlogs-mcp)
- [mcp-sanctions - Watchlist Screening for KYC and AML](/docs/hermes/mcp/servers/external/mcp-sanctions)
