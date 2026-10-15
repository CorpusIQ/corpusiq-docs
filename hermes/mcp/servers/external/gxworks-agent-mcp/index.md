---
title: "GX Works Agent MCP - Mitsubishi PLC Engineering"
description: "MCP tools and a Windows workbench for Mitsubishi PLC engineering: read project context, build Ladder, ST and FBD candidates, and deliver to GX Works2."
category: "Manufacturing & Industrial"
stars: 1
added: 2026-10-14
source: "mcpservers.org /all (October 14, 2026 evening sweep)"
relevance: ★★
tags: [manufacturing, industrial-automation, plc, mitsubishi, gx-works2, ladder, structured-text, engineering]
---

# GX Works Agent MCP

**A Windows MCP server and AI workbench for Mitsubishi PLC engineering: an agent reads a project's CPU and current program, retrieves CPU-scoped instruction facts and manual excerpts as evidence, builds Ladder, ST and FBD candidates, saves versioned artifacts, and delivers the current Ladder version into GX Works2 with operator-configured execution consent. Published by Arienax; the interface is MPL-2.0 and the runtime is free for internal commercial use.**

```
Component type: Local (Windows 10/11 x64; two independent packages)
MCP runtime: gxworks-agent-mcp.exe --local (stdio server; no Web or Node.js required)
Web workbench: optional browser GUI (Node.js 22.14+; model API configured in Settings)
Model: supplied by your MCP client; the server provides context, tools, persistence and receipts
Underlying: Mitsubishi Electric GX Works2 projects (Ladder, ST export, native FBD, SFC editing)
Artifacts: Ladder JSON, IR, SVG, ST derived from IR, and GX import CSVs
Delivery: GX Works2 import of the current Ladder version with MAIN and device comments (operator execution consent)
Version: GXWorks Agent 0.1.0 (released October 13, 2026)
Owner: Arienax; repo github.com/Arienax/gxworks-agent
Listing: mcpservers.org /all, October 14, 2026 evening sweep
```

## Why This Matters for Operators

PLC work is structured, repetitive and slow: read the requirement, find the right instructions in a manual, wire them correctly for a specific CPU, compile, fix, and hand the result to the engineer who owns the machine. Every step is real engineering work in a proprietary tool.

GX Works Agent puts the structured half of that inside MCP tools. The agent gets project-bound context (the CPU, the current program, applicable instructions and callable interfaces), builds or edits candidates, and saves versioned artifacts. The engineer keeps the review loop, and native saving, compilation and PLC behavior stay separate, verified operations in GX Works2. This is the Mitsubishi counterpart to the TiaLink gateway catalogued earlier today for Siemens systems.

## Capabilities

| Area | What the agent can do |
|---|---|
| Project context | Create or select a project by CPU and program type, read the CPU and current program, discover applicable instructions and callable interfaces |
| Engineering RAG | CPU-scoped instruction facts and manual excerpts with source references (entity, full-text and dense retrieval with rank fusion) |
| Ladder | Build or edit Ladder candidates, save versions with Ladder JSON, IR, SVG, ST derived from IR, and GX import CSVs |
| ST | Generate and review Structured Text from a confirmed specification; local bounded parser checks supported syntax and reports unsupported constructs |
| FBD | Edit existing GXW projects: objects, connections, declarations, networks; source-bound FB and Program creation; graphical previews and version diffs |
| Diagnostics | Compile and check a GXW matching the current version; associate diagnostics with ST lines, declarations, FBD networks or call instances |
| SFC | Import an existing SFC project and edit existing action and transition subprograms (not a complete graphical SFC IDE) |
| Simulation and monitoring | Ladder test plans with saved results; read-only PLC monitoring through MX Component with revocable, version-bound permissions |

## Setup

Two packages install independently and neither requires Python:

- **GXWorks-Agent-MCP-windows-x64.zip** - for external MCP clients: extract it and add a stdio server in your client using the extracted `gxworks-agent-mcp.exe` as the command and `--local` as its argument. Refresh the connection, call `list_projects`, then select or create a project with its actual CPU and program type.
- **GXWorks-Agent-Web-windows-x64.zip** - the optional browser workbench: run `npm install`, `npm run build`, `npm start`; the first start downloads the matching runtime.

Native saving, code checking, GX import, and simulation require the corresponding Mitsubishi software installed locally. FBD integration is tied to GX Works2 1.635.0.1. Read-only PLC monitoring requires MX Component and a configured logical station. None of these Mitsubishi applications are included in the packages.

## Business Relevance

- **System integrators and automation teams** can have an agent draft a Ladder or FBD change from a requirement, with instruction evidence attached, then import and review it in GX Works2 instead of starting from a blank screen
- **Existing-project edits** are the designed path: fault latching, resets, enable delays and similar changes go in as candidates with preserved FB implementations and wiring
- **Training and onboarding** benefit from a project that can be interrogated in plain language: what a block does, what a device address holds, what a compile reports
- **Versioned artifacts** (candidates, diffs, exports) give a reviewable trail for engineering change discussions

## Integration with CorpusIQ

Engineering change is one slice of an operations picture. CorpusIQ answers the surrounding business questions from connected sources such as accounting, CRM and email - what a change request is costing, which project consumes the most engineering time, which milestone is at risk - without wiring the shop-floor tooling to the business systems first.

## Limitations

- **Windows required:** the MCP runtime and Web workbench are Windows 10/11 x64 packages; GX integration needs an interactive Windows session
- **Mitsubishi software not included:** native saving, code checking, GX import, simulation and PLC monitoring depend on locally installed GX Works2 (and MX Component for monitoring)
- **Closed core:** the public Web interface files are MPL-2.0, while the core and native adapters ship under a separate Runtime Free Use Agreement (free internal commercial use)
- **Capability-level docs:** the listing and README document capabilities rather than a published tool list; there is no hosted endpoint to probe (the runtime is local by design)
- **Safety scope:** a saved artifact or successful import does not establish a successful compile or correct PLC behavior; generated logic must be reviewed against the CPU, wiring and operating modes, and safety functions require an independent safety system
- **Early release (v0.1.0):** CPU menu availability does not imply uniform instruction or validation coverage; version details are as the publisher states

## FAQ

### Does it require internet access or a cloud account?

No. The MCP runtime runs locally next to your GX Works2 installation; external agents bring their own model. The optional Web workbench is for generation, editing and management in a browser.

### Which AI clients can connect?

Any MCP client that can launch a stdio server, such as Codex, Claude Code or Cursor. The client supplies the model and planning loop; GX Works Agent supplies the engineering context, tools and persistence.

### Does sending to GX Works2 download code to a PLC?

No. Sending to GX Works2 does not download a program to a PLC. Native saving, compilation and behavior verification remain separate operations in the intended GX Works2 environment.

### Can AI-generated PLC logic go straight to a live machine?

No. The vendor's documentation is explicit: review generated logic against the selected CPU, wiring, motion limits and operating modes, back up the target project, compile and inspect before commissioning, and implement emergency stops and guarding with an independent safety system.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [TiaLink MCP - Siemens TIA Portal Engineering](/hermes/mcp/servers/external/tialink-mcp/)
- [MechanoFab MCP - Manufacturing Knowledge for Agents](/hermes/mcp/servers/external/mechanofab-mcp/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
