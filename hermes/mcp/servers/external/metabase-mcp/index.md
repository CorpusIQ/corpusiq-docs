# Metabase MCP Server ★★★ Official

**Source:** mcpservers.org · **Last updated:** July 27, 2026 (early morning sweep)  
**GitHub:** [metabase/metabase](https://github.com/metabase/metabase) ⭐ 48,400+  
**Endpoint:** `https://<your-metabase-instance>/api/mcp` (Streamable HTTP, built-in)  
**Auth:** Metabase API key or session token  
**Category:** Business Intelligence / Data & Analytics

---

## Overview

**Metabase** ships a built-in MCP server starting from its July 2026 release. AI clients connect directly to your Metabase instance and use the semantic layer to search, query, and visualize data — no separate connector required. It builds on Metabase's Agent API to expose tools for navigating your entire BI surface area: databases, tables, questions, dashboards, and collections.

This is the first major BI platform to ship MCP natively — a paradigm shift for how operators interact with business data.

## Key Capabilities

- **Search** — Find tables, metrics, cards, dashboards, and collections using keywords or natural-language queries
- **Navigate entities** — Read metadata for databases, schemas, tables, questions, dashboards, and metrics via `metabase://` URIs
- **Build and run queries** — Construct queries against tables or metrics, execute them, and get structured results with column metadata
- **Run raw SQL** — Execute native SQL against databases (requires native-query permission)
- **Save and update questions** — Create or modify saved questions (cards) from agent-constructed queries
- **Dashboard management** — Create new dashboards with auto-positioned saved questions, update metadata, archive

## Tools Reference

| Tool | Description |
|------|-------------|
| `search` | Search Metabase content by keyword/query |
| `read_resource` | Read entity metadata using `metabase://` URIs |
| `construct_query` | Build a query against a table or metric |
| `execute_query` | Execute a constructed query and return results |
| `execute_sql` | Run native SQL (requires permissions) |
| `create_question` | Save a query as a question/card |
| `update_question` | Modify an existing question, including archiving |
| `create_dashboard` | Build a new dashboard with auto-positioned cards |
| `update_dashboard` | Modify dashboard metadata or archive |

## Integration

### Prerequisites

- Metabase instance (self-hosted or Metabase Cloud) running the July 2026+ release
- API key with appropriate permissions (Admin > Settings > Authentication > API Keys)

### 1. Claude Desktop

```json
{
  "mcpServers": {
    "metabase": {
      "type": "http",
      "url": "https://metabase.yourcompany.com/api/mcp",
      "headers": {
        "x-api-key": "mb_YOUR_API_KEY"
      }
    }
  }
}
```

### 2. Hermes Agent (config.yaml)

```yaml
mcp:
  servers:
    metabase:
      type: http
      url: https://metabase.yourcompany.com/api/mcp
      headers:
        x-api-key: ${METABASE_API_KEY}
```

### 3. Cursor / VS Code

Connect via Streamable HTTP at `https://metabase.yourcompany.com/api/mcp` with the `x-api-key` header.

## Business Operator Use Cases

1. **Natural Language Analytics** — "What was our MRR last month broken down by plan tier?" — agent queries Metabase and returns formatted results
2. **Automated Board Reports** — Agent pulls KPIs from Metabase dashboards weekly, formats into a report
3. **Anomaly Detection** — Agent monitors key metrics and alerts on unexpected deviations
4. **Ad-Hoc Data Exploration** — "Show me churn by acquisition channel for Q2" — agent builds and executes the query
5. **Dashboard Creation** — Agent auto-builds dashboards for new initiatives based on natural language descriptions

## Pricing

- **Metabase MCP server:** Free (included with Metabase)
- **Metabase Open Source:** Free (self-hosted)
- **Metabase Cloud:** Starter at $85/month (includes MCP support)

## Security Considerations

- API key scoped to specific Metabase permissions
- Native SQL execution requires explicit permission (disabled by default)
- All queries respect Metabase's existing data sandboxing and row-level permissions
- ⚠️ Write operations (create/update questions and dashboards) should be tested in a staging instance first

## Verdict

★★★★★ — The first major BI platform to go MCP-native. Essential for any business operator running Metabase who wants AI agents to interact with their BI layer directly. The built-in semantic layer means agents query meaningful business concepts ("MRR", "churn"), not raw table names — this is the right architecture for AI-powered analytics.
