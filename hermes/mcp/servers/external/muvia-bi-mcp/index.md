---
title: "Muvia BI MCP - SQL, Dashboards and Alarms on Company Data"
description: "Read datasets, run SQL on a company data lake and file dashboard, alarm or predictor changes that a person approves, over a hosted 231-tool MCP server."
category: "Business Intelligence & Analytics"
stars: n/a (hosted service, no public repo)
added: 2026-10-22
source: "chatmcp/mcpso issue #5955 (Muvia BI, October 22, 2026 midday supplement)"
relevance: ★★
tags: [business-intelligence, analytics, sql, data-lake, dashboards, alarms, predictors, lineage, oauth, remote-mcp]
---

# Muvia BI MCP

**Most BI assistants read a dashboard and stop. Muvia exposes the whole data operation to an agent: query the lake, read lineage, check a query, open an alarm, propose a dashboard widget, and every write lands as a proposal a person approves instead of a change that already happened.**

```
Server type: Remote (Streamable HTTP, JSON-RPC 2.0 over POST, SSE response)
Endpoint: https://api.muviabi.com/mcp/v1
Auth: OAuth 2.1 (PKCE S256, dynamic client registration) for a person's assistant, or an mvk_ API key as Bearer
Live check: unauthenticated POST initialize returned HTTP 401 with www-authenticate pointing at /.well-known/oauth-protected-resource/mcp/v1/ (HTTP 200, resource https://api.muviabi.com/mcp/v1/)
Tools: 231 from the vendor reference (113 read, 118 write: 96 proposal, 12 confirmed in Muvia, 10 not for API keys)
Protocol version: 2025-06-18
Built by: Superduck S.r.l. (muviabi.com)
```

## Why This Matters for Operators

The catalog holds BI readers and SQL runners. It did not hold a data platform whose agent surface carries the governance with it, and that is the part an operator actually has to answer for: who changed the dashboard, on whose authority, and what did the number say before.

Muvia answers that inside the protocol rather than in a policy document. A write tool never mutates the platform on the spot. It files a proposal, a person approves it in Muvia or the company policy applies, `get_action` reports the outcome of a write, and a key only writes when an administrator has turned on "Can write through assistants" for it. The read side is a full data lake surface: `query_sql`, `describe_sql`, `read_lineage`, `run_query_checks`, `list_quarantine`, `list_dataset_readers`.

That combination is what makes it usable next to a first-party connector rather than instead of one. The assistant can answer a question from the lake and also say which dataset it came from, whether the row count moved, and who else reads that dataset.

## Tools & Capabilities

231 tools across 14 modules, filtered per connection to what the person or key may use.

| Module | Tools | What an operator reaches |
|---|---|---|
| Core | 12 | `list_projects`, `describe_project`, `query_sql`, `describe_sql`, `find_tools`, `get_action`, `whoami` |
| Alarms | 20 | `list_alarms`, `describe_alarm`, `investigate_alarm`, `acknowledge_alarm`, `shelve_alarm`, channels, subscriptions and alarm tasks |
| Analysis | 17 | `create_analysis`, `get_analysis`, `draft_query_from_analysis`, `draft_monitor_from_analysis`, `list_analysis_versions`, visibility and share links |
| Dashboards | 18 | `list_dashboards`, `create_dashboard`, `add_widget`, `convert_chart`, widget templates and share links |
| Flows | 36 | `run_flow`, `simulate_flow`, `tune_monitor`, `check_flow`, `request_flow_approval`, run histories and libraries |
| Lab | 26 | Datasets and queries: `list_datasets`, `read_dataset`, `read_lineage`, `run_query_checks`, `set_query_checks`, `list_quarantine`, `empty_quarantine`, `list_dataset_readers`, materialization and query presets |
| Nodes | 15 | `list_nodes`, `describe_node`, `publish_node_config`, `read_node_monitoring`, tags and data caps for industrial data sources |
| Notebooks | 19 | `create_notebook`, run and read notebooks, repository and link management |
| Assets | 24 | `list_assets`, `describe_asset`, models and variables, `propose_variable_references`, `suggest_asset_bindings` |
| Sources | 18 | `browse_connection`, `browse_account`, `create_database_source`, `create_connector_source`, `append_source_load` |
| Predictors | 7 | `list_predictors`, `get_predictor`, `create_predictor`, `promote_predictor_version`, `reject_predictor_version` |
| Project | 8 | Project map and overview reads |
| Documents | 4 | `list_documents`, `update_document`, `reindex_document` |
| Annotations | 7 | `annotate_signal`, notes and attachments on signals |

Write modes are stated per tool: proposal (a person approves), confirmed in Muvia (applied at once by company policy), and not available to API keys at all for the tools that act as a person, such as their own notes and public links.

## Live Check

The server answered an unauthenticated `POST initialize` with HTTP 401 and an RFC 9728 pointer, `www-authenticate: Bearer resource_metadata="https://api.muviabi.com/.well-known/oauth-protected-resource/mcp/v1/"`. That metadata returned HTTP 200 with resource `https://api.muviabi.com/mcp/v1/`, authorization server `https://api.muviabi.com/mcp/v1` and `bearer_methods_supported: ["header"]`. The authorization server metadata returned `authorization_endpoint`, `token_endpoint`, `registration_endpoint` (`/mcp/v1/register`), `revocation_endpoint`, grants `authorization_code` and `refresh_token`, and `code_challenge_methods_supported: ["S256"]` with `client_id_metadata_document_supported: true`.

The tool inventory and the write modes above come from the vendor's published reference at `developers.muviabi.com/mcp-tools`, which states the same 231 tool count the submission quoted. **No tool call was made:** every tool needs an OAuth session or an `mvk_` key, and this sweep does not create accounts. That is the gap in this entry, stated rather than papered over.

## Installation

```json
{
  "mcpServers": {
    "muvia": {
      "type": "streamable-http",
      "url": "https://api.muviabi.com/mcp/v1"
    }
  }
}
```

For an unattended agent, issue an `mvk_` API key in Muvia with only the scopes the job needs and send it as `Authorization: Bearer`. Scopes are Muvia's own permission names (`datasets_read`, `nodes_read`, `settings_read`, `muvia.read`, `muvia.write`, `muvia.alarms`), an administrator can grant a key only scopes they hold themselves, `superadmin` can never be granted to a key, and a company's enabled modules cap every key.

Rate limits are 120 requests a minute per key and 100,000 a day per company, in fixed windows, with `X-RateLimit-Limit`, `X-RateLimit-Remaining` and `X-RateLimit-Reset` on every response, success or error.

## Limits Worth Knowing

- An account is required. Muvia is a hosted platform sold with an AI connectors module, and the only public entry is the 14-day trial at `app-demo.muviabi.com/try`. No price list was reachable: `/en/pricing` and `/it/pricing` both returned 404, so the cost of the module is a sales conversation.
- The platform is industrial by design, with machine and OT data next to financial and commercial sources. A services business with no operational data will use the lake, dashboards and alarms and little else.
- 231 tools is a surface an assistant can get lost in. `find_tools` exists for that reason, and a connection scoped to read-only tools is the sane default.
- The protected-resource metadata advertises an empty `scopes_supported` list while the tools declare scopes individually, so scope discovery has to come from `tools/list` and the scope guide rather than from the discovery document.
- A proposal is not an answer. Until a person approves it in Muvia, the change does not exist, and an agent that reports "dashboard updated" after filing a proposal is wrong.

## FAQ

### Does the agent change my dashboards without asking?
No. A write files a proposal, and a person approves it in Muvia or the company's policy applies it. From an API key it is always a proposal a person confirms. `get_action` returns the outcome of the write you filed.

### Can I point it at one project instead of the whole company?
Yes. An `mvk_` key carries scopes chosen when it is issued, an administrator can narrow them later without changing the key, and the company's enabled modules cap what any key can reach. Start with `muvia.read` and add write rights per module.

### Why catalogue this when Metabase MCP is already here?
Metabase is a BI reader over your warehouse. Muvia is a data platform whose agent surface also carries lineage, query checks, quarantine, alarms and model promotion, with a stated approval step on every write. Same question, different half of the job.

## See Also

- [Metabase MCP](/hermes/mcp/servers/external/metabase-mcp/)
- [MCP Server Discovery - October 22, 2026 (Midday Supplement)](/hermes/mcp/sweeps/sweep-october22-2026-midday-supplement/)
