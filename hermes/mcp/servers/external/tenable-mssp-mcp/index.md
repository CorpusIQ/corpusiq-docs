---
title: "Tenable MSSP MCP - CorpusIQ Docs"
description: Tenable MSSP portal orchestration over MCP — bulk CVE queries, scoped Hexa AI tool runs and child-container management across managed security tenants.
category: Development
stars: n/a (new listing)
added: 2026-08-17
source: mcpservers.org
relevance: ★★
tags: [tenable, vulnerability-management, mssp, security-ops, cve, enterprise-security, python, self-hosted]
---

# Tenable MSSP MCP

**MCP server (stdio, self-hosted Python)** — an MSSP-aware orchestration layer around the Tenable Hexa AI MCP Server. Run Hexa AI tools across MSSP child containers through a scoped layer, query CVEs across tenants in bulk, and control exactly which child containers an action touches.

```
Server type: stdio (Python 3.14, uv or pip install)
Auth: Tenable MSSP Portal API keys (access + secret)
Endpoint: local process
Tools: 9 (child-container listing, scoped Hexa tool runs, bulk CVE export)
Pricing: free software (MIT); requires Tenable MSSP Portal and hexa/vm licenses
Category: Development
Built by: Andrew Spearson (github.com/andrewspearson/tenable-mcp-mssp)
```

## Why This Matters for Operators

Managed security providers run dozens of Tenable tenants. Answering one CVE question across all of them manually means the same query in every portal — or a script someone maintains. This server gives the agent the orchestration layer: one prompt can query a CVE across every eligible child container, run a validated Hexa AI recipe across tenants with controlled fan-out, and return a CSV report of findings.

**Scope control is explicit**: a plain-text allowlist file restricts action tools to named child-container UUIDs, and expired containers, malformed data, missing child accounts, and `licenseType: "ao"` containers are blocked regardless. Queries and actions against child containers run concurrently on up to 10 containers at a time. The bulk CVE tool is deliberately conservative — it starts a server-managed background run and returns a run ID, with separate status and result tools, and the prompt must name the tool explicitly before it executes.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `list_mssp_child_accounts` | Raw MSSP child account objects including license data |
| `list_available_tenable_mcp_tools` | Discover the Hexa AI MCP tool catalog for one child container |
| `get_child_container_scope` | Show the configured allowlist scope for action tools |
| `run_tenable_mcp_tool_for_child` | Run one Hexa AI tool on one child container |
| `run_tenable_mcp_recipe_for_child` | Validate a known tool-call sequence on one child container |
| `run_tenable_mcp_recipe_across_child_containers` | Run a working recipe across multiple containers with controlled fan-out |
| `bulk_vm_cve_query` | Server-managed pyTenable vulnerability export across eligible containers (explicit-request only) |
| `get_bulk_vm_cve_query_status` | Check a bulk run's status |
| `get_bulk_vm_cve_query_result` | Read the final summary and CSV artifact paths |

## Installation

```bash
git clone https://github.com/andrewspearson/tenable-mcp-mssp.git
cd tenable-mcp-mssp
uv venv && uv pip install .
cp .env.example .env && chmod 600 .env   # fill in portal access + secret keys
```

## Configuration

```bash
claude mcp add tenable-mcp-mssp -- /path/to/tenable-mcp-mssp/.venv/bin/python -m tenable_mcp_mssp.server
```

Environment: `TENABLE_MSSP_PORTAL_ACCESS_KEY`, `TENABLE_MSSP_PORTAL_SECRET_KEY`, optional `TENABLE_MCP_MSSP_CHILD_CONTAINER_SCOPE_FILE` (allowlist, one UUID per line) and `TENABLE_MCP_MSSP_LOG_LEVEL`.

## Business Relevance

- **MSSP operators** answer one CVE question across every managed tenant in a single run
- **Security analysts** get scoped Hexa AI tool runs with an explicit tenant allowlist
- **Compliance teams** get CSV evidence of findings across child containers
- **Tenable shops** get bulk tagging and query patterns without building their own scripts

## Integration with CorpusIQ

Tenable MSSP composes with the CorpusIQ reporting and governance stack as the security-evidence source. A CorpusIQ operator workflow can run the bulk CVE query, collect the CSV report, and fold it into the standard reporting pipeline the CorpusIQ connectors already serve — findings beside financials, one evidence package. The child-container allowlist mirrors the CorpusIQ scoping doctrine: credentials act only where explicitly permitted, and the audit trail records what ran. For MSPs running their own CorpusIQ instance, the security posture of managed tenants becomes another connector-backed data source instead of a manual portal crawl.

## Limitations

- Brand new — no track record yet; listed August 17, 2026
- Requires Tenable MSSP Portal API keys with Administrator privileges
- Child containers need `hexa` licenses for Hexa AI tools and `vm` licenses for bulk CVE export
- Python 3.14+ required — newer than many enterprise Python installations
- Self-hosted stdio server: you operate the process and the credential hygiene

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
