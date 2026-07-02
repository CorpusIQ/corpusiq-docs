---
title: "Container Tracking MCP — Ocean Freight Visibility for AI Agents"
description: "Track ocean containers across 200+ shipping lines by container number, bill of lading, or booking reference. Live milestones, vessel positions, and supply chain visibility from any MCP client."
category: mcp
tags: [mcp-server, logistics, shipping, supply-chain, container-tracking, ocean-freight]
last_updated: 2026-07-02
---

# Container Tracking MCP — Supply Chain Visibility

## What It Is

Container Tracking MCP (`lxxmng/container-tracking-mcp`) provides real-time ocean container tracking across 200+ shipping lines. Supply chain operators can query live container milestones, vessel positions, and estimated arrivals directly from their AI agent — no portal-hopping across carrier websites.

## Tools Available

| Tool | Description |
|------|-------------|
| Track by container | Live milestones for a specific container number |
| Track by BOL | Bill of lading lookup across carriers |
| Track by booking | Booking reference tracking |
| Vessel position | Current vessel location and ETA |

## Quick Start

```bash
npx mcp-remote https://mcp.trackingmcp.com/mcp
```

## Business Use Cases

1. **Exception monitoring**: "Which containers are delayed beyond their ETA — flag with customer name and PO number"
2. **Inventory planning**: "When does container MSCU1234567 arrive at LA/Long Beach?"
3. **Customer updates**: "Generate a status update for all 15 containers for Customer X — include current location, ETA, and any delays"
4. **Carrier performance**: "Compare on-time percentage across Maersk, MSC, and CMA CGM for my Q3 shipments"

## Limitations

- **Ocean only**: No air freight, trucking, or rail tracking
- **Remote service**: Depends on trackingmcp.com uptime
- **No booking**: Read-only tracking — no booking or documentation changes

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
