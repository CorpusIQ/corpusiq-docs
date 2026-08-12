---
title: mcp-server-malcolm (Malcolm Network Traffic Analysis)
description: "Setup and usage guide for mcp-server-malcolm (Malcolm Network Traffic Analysis). Part of the Hermes resource directory."
last_updated: 2026-08-12
---

# mcp-server-malcolm (Malcolm Network Traffic Analysis)

**URL:** https://github.com/nagameTW/mcp-server-malcolm
**mcpservers.org:** https://mcpservers.org/servers/nagameTW/mcp-server-malcolm
**Category:** Security / Network Analysis
**Priority:** MEDIUM

## What It Does for Operators

The first MCP server for Malcolm, the open-source network traffic analysis suite (Zeek + Suricata + Arkime + OpenSearch + NetBox). Gives AI agents structured, threat-hunting access: search and aggregate traffic, discover fields, query Suricata alerts, browse Arkime sessions, and resolve NetBox assets.

## Installation

```bash
pip install mcp-server-malcolm
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "malcolm": {
      "command": "python",
      "args": ["-m", "mcp_server_malcolm"],
      "env": {
        "MALCOLM_URL": "https://your-malcolm-instance",
        "MALCOLM_API_KEY": "your-api-key"
      }
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `search_traffic` | Search and aggregate network traffic |
| `discover_fields` | Discover available data fields |
| `query_suricata_alerts` | Query Suricata IDS alerts |
| `browse_arkime_sessions` | Browse Arkime packet sessions |
| `resolve_netbox_assets` | Resolve NetBox infrastructure assets |

## Operator Use Cases

1. **Security operations** — agent-driven threat hunting across network telemetry
2. **Incident response** — query Suricata alerts and trace through Arkime sessions
3. **Asset inventory** — resolve NetBox assets during investigations
4. **Compliance auditing** — agent-assisted network traffic audits
5. **SOC automation** — integrate with SIEM/SOAR workflows

## CorpusIQ Angle

For operators managing security infrastructure, this brings network forensics into the AI agent workflow. Read-only by default with opt-in, audited write classes for alerts, tagging, hunts, and PCAP upload — aligns with secure-by-default philosophy.

## Limitations

- Requires a running Malcolm deployment
- Write operations require explicit opt-in
- Python-only (pip install)

---
**Discovered:** July 24, 2026 via awesome-mcp-servers PR #10852
**Repo:** nagameTW/mcp-server-malcolm
