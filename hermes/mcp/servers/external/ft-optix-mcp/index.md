---
title: FT Optix MCP Server
subtitle: Industrial automation connectivity — FT Optix Studio to LLMs
source: mcp.so
github: https://github.com/asqi-carter/ft-optix-mcp
created: 2026-07-21
category: Industrial
stars: 0
tags: [industrial, automation, factory, iot, plc, scada]
---

# FT Optix MCP Server

MCP server for **connecting FT Optix Studio to LLMs**. FT Optix is a factory/industrial automation platform (SCADA, HMI, IoT). This MCP server bridges the operational technology (OT) world with AI agents — enabling natural language queries against factory floor data.

## What It Does

- **Factory Data Access** — Query production metrics, sensor data, and machine states via MCP
- **Alarm Management** — AI agents can read and acknowledge factory alarms
- **Recipe Management** — Access and modify production recipes through LLM
- **OT/IT Bridge** — First MCP server connecting industrial automation to AI agents

## Business Operator Use Cases

| Use Case | Value |
|----------|-------|
| **Production Monitoring** | "What's the OEE on Line 3 right now?" → live factory floor data |
| **Predictive Maintenance** | "Show me all machines with vibration above threshold" → maintenance dispatch |
| **Shift Handover** | "Summarize Line 2's performance and open alarms for the next shift" |
| **Compliance Reporting** | "Generate today's production report with all quality deviations" |

## Installation

```bash
git clone https://github.com/asqi-carter/ft-optix-mcp
cd ft-optix-mcp
pip install -r requirements.txt
```

## Configuration

Add to your MCP client config:

```json
{
  "mcpServers": {
    "ft-optix": {
      "command": "python",
      "args": ["path/to/ft-optix-mcp/server.py"],
      "env": {
        "FTOPTIX_HOST": "your-ftoptix-server",
        "FTOPTIX_PORT": "443",
        "FTOPTIX_USERNAME": "your-username",
        "FTOPTIX_PASSWORD": "your-password"
      }
    }
  }
}
```

## Auth

FT Optix Studio credentials (username/password). Requires network access to the FT Optix server.

## Tools Provided

- `get_tag_values` — Read live tag values from PLCs and devices
- `list_alarms` — Query active and historical alarms
- `get_production_metrics` — OEE, throughput, downtime stats
- `acknowledge_alarm` — Acknowledge alarms via AI agent
- `get_recipe` — Read production recipe parameters

## Limitations

- **0 stars, brand new** — Created July 21, 2026. Experimental.
- **FT Optix only** — No support for other SCADA platforms (Ignition, WinCC, FactoryTalk).
- **Read-focused** — Limited write capabilities. Can't modify PLC logic.
- **Network security concerns** — Connecting factory OT networks to AI agents requires careful network segmentation.
- **Niche audience** — Only relevant for FT Optix users.

## Operator Verdict

★★ **First mover in industrial MCP, but narrow audience.** This is significant as a proof point that MCP is expanding beyond SaaS into operational technology. For manufacturers already on FT Optix, this is a compelling bridge to AI-assisted operations. Most operators won't need this — but the pattern (SCADA → MCP → AI agent) will expand to other platforms.
