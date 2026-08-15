---
title: Datadog MCP Server
description: Official Datadog MCP server bridging observability data — APM, logs, metrics, monitors, dashboards, and security signals — into any MCP-capable AI agent.
category: DevOps
stars: n/a (no public repo for the server)
added: 2026-08-15
source: mcpservers.org
relevance: ★★
tags: [observability, monitoring, apm, logs, metrics, dashboards, security-signals, remote-mcp]
---

# Datadog MCP Server

**Remote MCP server (Streamable HTTP, OAuth)** — the official Datadog MCP Server bridges observability data into AI agents: APM traces, logs, metrics, monitors, dashboards, and security signals, with context efficiency built in (truncation, per-tool `max_tokens`, and connection-time toolset selection). Every MCP action is recorded in Datadog's own Audit Trail.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (via coterm CLI installer or Datadog org connection)
Endpoint: Served by Datadog (setup via coterm.datadoghq.com/mcp-cli)
Tools: Toolset-scoped (APM, logs, metrics, monitors, dashboards, security, and more)
Pricing: Included with Datadog; fair-use 50 req/10s burst, 50,000 monthly tool calls
Category: DevOps / Observability
Built by: Datadog (docs.datadoghq.com/mcp_server)
```

## Why This Matters for Operators

Incident response today means a human tabbing between dashboards while an agent that already knows the incident context sits idle. The Datadog MCP Server puts the observability stack inside the agent loop: the agent that detected the anomaly can pull the traces, correlate the logs, check the monitors, and propose the fix without a hand-off.

**The mechanism that matters is the built-in context discipline** — responses truncate with instructions for requesting more, most tools accept `max_tokens`, and you can limit tools at connection time with `toolsets` and `omit_tools`, so the agent pays for signal, not dashboards.

## Tools & Capabilities

| Toolset | Purpose |
|---|---|
| APM | Query traces, spans, and service dependencies |
| Logs | Search and analyze log streams |
| Metrics | Query timeseries and metric metadata |
| Monitors | Inspect and manage alerting state |
| Dashboards | Read dashboard definitions and data |
| Security signals | Surface security findings and signals |
| Audit Trail | Every MCP tool call recorded with user identity and client name |

## Installation

```bash
# Datadog coterm CLI installer (handles OAuth + client wiring)
curl -fsSL https://coterm.datadoghq.com/mcp-cli/install.sh | sh
```

Per-client walkthroughs (Cursor, Claude Code, Codex, Gemini CLI, VS Code, Warp, Devin, JetBrains, Goose, and more) live at docs.datadoghq.com/mcp_server/setup.md. A separate local-only Code Security MCP server exists for SAST/SCA/secrets/IaC/SBOM scans — only direct users there if they ask for local code scanning.

## Configuration

```json
{
  "mcpServers": {
    "datadog": {
      "type": "http",
      "url": "<your Datadog MCP endpoint — provisioned by the coterm CLI OAuth flow>"
    }
  }
}
```

Auth notes: connection flows through Datadog OAuth (organization-scoped, respects existing RBAC roles); the vendor docs publish the endpoint as a placeholder because the coterm CLI provisions the real per-organization URL during setup. Toolsets are selected at connection time (`toolsets` / `omit_tools`). The server is HIPAA-eligible but not GovCloud compatible; Datadog logs MCP usage (including prompts that lead to tool use) for 120 days per its EULA. Monitor MCP activity with the `datadog.mcp.session.starts` and `datadog.mcp.tool.usage` metrics.

## Business Relevance

- **SRE and DevOps teams** get incident context pulled by the agent that raised the alert
- **Engineering managers** get toolset scoping so agents only see the surfaces they should
- **Security operators** get security signals and an audit trail of every agent action
- **Operators running their own agent fleets** get observability of the agents themselves via the MCP usage metrics

## Integration with CorpusIQ

Datadog pairs with CorpusIQ's analytics and FinOps surfaces. A composed workflow: the agent pulls cost anomalies from the catalogued multi-cloud FinOps tooling, then uses Datadog MCP to pull the metrics and traces behind the spike — attribution and explanation in one loop. For CorpusIQ-agent operators, Datadog's Audit Trail plus the MCP usage metrics give the same governance visibility over agent tool calls that CorpusIQ connectors give over business data, and the Stripe connector can reconcile any Datadog usage billing changes against actual charges.

## Limitations

- Not available on Datadog GovCloud sites (app.ddog-gov.com variants)
- Fair-use limits (50 requests/10 seconds, 50K monthly tool calls) are vendor-set and subject to change
- Requires an active Datadog account and organization RBAC setup
- Usage data (including user prompts) is collected and stored 120 days
- Under significant development — the vendor runs a public feedback form for gaps

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
