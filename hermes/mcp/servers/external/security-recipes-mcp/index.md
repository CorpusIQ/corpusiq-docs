---
title: Security Recipes MCP - CVE Intelligence and Remediation
description: "Read-only CVE intelligence, remediation playbooks, and agentic security governance content over Streamable HTTP with no auth. 75 tools: CVE catalog search for Medium/High/Critical findings, recipe and playbook lookups, MCP gateway policy, agent BOM, and SOC detection content."
category: Security
stars: 1
added: 2026-08-26
source: "mcp.so GitHub issue #3783"
relevance: ★★★
tags: [security, cve, vulnerability, remediation, playbooks, mcp-governance, keyless, remote-mcp]
---

# Security Recipes MCP

**Read-only CVE intelligence, remediation playbooks, and agent-setup guidance over a keyless Streamable HTTP endpoint.** Security Recipes turns security findings into bounded agent work: one recipe, scoped context, required proof, and a documented remediation path. It is explicitly not a scanner - it does not scan, write, or deploy. The hosted server answered an anonymous live probe with serverInfo `security-recipes-mcp` v3.4.7 and exposed 75 tools covering the CVE catalog, recipe search, playbook planning, and enterprise agentic-security governance packs.

```
Server type: Remote (Streamable HTTP)
Auth: None
Endpoint: https://security-recipes.ai/mcp
Tools: 75 (all read-only)
Pricing: Free, keyless
Category: Security
Built by: stevologic (registry io.github.stevologic/security-recipes)
```

## Why This Matters for Operators

Security remediation has a knowledge problem, not a tooling problem: teams know something is vulnerable, but the fix depends on tribal knowledge about which patch applies, what config change is safe, and what evidence to collect. Security Recipes packages that knowledge as data an agent can read - CVE evidence with bounded code/config/file change plans, remediation workflows with phase gates and evidence checklists, and enterprise packs for MCP governance, agent identity, and SOC detection.

**The keyless design makes it the cheapest first stop for vulnerability triage.** An agent that spots a Medium/High/Critical CVE in a dependency can call `recipes_cve_get` and receive evidence, recipe authority, and a bounded change plan without any credential setup.

## Tools & Capabilities

| Area | Representative tools |
|---|---|
| CVE intelligence | `recipes_cve_catalog_info`, `recipes_cve_search`, `recipes_cve_get` (Medium/High/Critical scope, evidence, bounded change plans) |
| Recipes | `recipes_search`, `recipes_list`, `recipes_get`, `recipes_refresh` (full-text search over security-recipes documents) |
| Playbooks | `recipes_playbooks_list`, `recipes_playbook_get`, `recipes_playbook_plan` (deterministic phase/gate/evidence checklists) |
| MCP governance | `recipes_mcp_gateway_policy`, `recipes_mcp_connector_trust_pack`, `recipes_mcp_tool_risk_contract`, `recipes_mcp_tool_surface_drift_pack` |
| Agentic assurance | `recipes_agentic_system_bom`, `recipes_agentic_readiness_scorecard`, `recipes_agentic_posture_snapshot`, `recipes_agentic_red_team_drill_pack` |
| Detection & response | `recipes_agentic_soc_detection_pack`, `recipes_agentic_incident_response_pack`, `recipes_agentic_threat_radar` |

## Installation

No auth, no install. Add the hosted endpoint to any MCP client:

```json
{
  "mcpServers": {
    "security-recipes": {
      "url": "https://security-recipes.ai/mcp"
    }
  }
}
```

Docs: https://security-recipes.ai/mcp-servers/ · Repo: https://github.com/stevologic/security-recipes.ai (Apache-2.0)

## Configuration

Nothing to configure - the endpoint is public and stateless (session-scoped). Upstream MCP servers can optionally be configured for the recipes_mcp_upstream_* tools, which list allowed read-only tools and collect bounded context from those upstreams for remediation queries. Self-hosters can run the open-source recipes-index.json source tree and serve their own instance.

## Business Relevance

For operators building on AI agents, the governance packs are the quiet value: MCP gateway policies, connector trust tiers, tool-risk contracts, agent identity ledgers, and SIEM-ready detections for agentic telemetry. These answer the questions procurement and security teams are now asking about agent deployments - what can this agent touch, who does it act as, and what does a compromise look like. The CVE catalog is the day-to-day utility: triage findings with evidence and a bounded fix plan instead of a blog search.

## Integration with CorpusIQ

Complementary to CorpusIQ's business-data connectors: CorpusIQ answers "what is happening in my business", Security Recipes answers "what should I do about this security finding, and how do I prove it". An operator agent can pull finance and CRM context from CorpusIQ, then call `recipes_playbook_plan` to build an evidence-gated remediation checklist for the team. Both surfaces are read-only by design.

## Limitations

- Read-only by design: no scanning, no writes, no deployment actions.
- CVE catalog scoped to Medium/High/Critical findings - low-severity CVEs are out of scope.
- Young project (repo created April 2026, 1 star) - treat the governance packs as evolving guidance, not settled standards.
- A large share of the 75 tools are enterprise assurance/documentation packs rather than raw data endpoints.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [ScreenVerity MCP - U.S. Exclusion and Debarment Screening](/docs/hermes/mcp/servers/external/screenverity-mcp)
- [Poison Armor MCP - Prompt-Injection Firewall for AI Agents](/docs/hermes/mcp/servers/external/poison-armor-mcp)
- [CorpusIQ Connectors](/docs/hermes/mcp/servers)
