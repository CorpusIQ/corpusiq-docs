---
title: Capforge — SAP CAP/CDS MCP Server
subtitle: SAP Cloud Application Programming model scaffolding with compile validation
source: capforge
github: https://github.com/automatizatodo/capforge
created: 2026-07-22
category: Enterprise / SAP
stars: 0
tags: [sap, cap, cds, fiori, ui5, enterprise, development]
---

# Capforge — SAP CAP/CDS MCP Server

MCP server that makes AI agents **get SAP CAP/CDS and UI5 right**. Combines modern scaffolding with a real validation loop against `cds compile`. First dedicated SAP development MCP server.

## What It Does

SAP's Cloud Application Programming (CAP) model uses CDS (Core Data Services) for data modeling. Capforge gives AI agents:

- **Project Scaffolding** — Generate CAP project structure with correct CDS models
- **CDS Validation** — Validate CDS definitions against `cds compile` before deployment
- **UI5 Integration** — Generate Fiori/UI5 frontends from CDS annotations
- **Error Prevention** — Catch CDS syntax errors early, not at build time

## Business Operator Use Cases

| Use Case | Value |
|----------|-------|
| **SAP Development Acceleration** | "Scaffold a CAP service for purchase order management" → valid CDS + working service |
| **Fiori App Generation** | "Create a list-report Fiori app from this CDS entity" |
| **Code Review** | "Validate all CDS files in this project against the latest CAP runtime" |
| **SAP Onboarding** | New SAP developers get correct project structure instantly |

## Installation

```bash
git clone https://github.com/automatizatodo/capforge
cd capforge
npm install
```

## Configuration

```json
{
  "mcpServers": {
    "capforge": {
      "command": "node",
      "args": ["path/to/capforge/index.js"],
      "env": {
        "SAP_CDS_PATH": "/usr/local/bin/cds"
      }
    }
  }
}
```

Requires `@sap/cds` (CDS compiler) installed locally.

## Tools Provided

- `scaffold_project` — Generate CAP project structure
- `validate_cds` — Compile and validate CDS definitions
- `generate_service` — Create a CAP service from a CDS model
- `generate_ui5_app` — Generate Fiori/UI5 frontend
- `check_dependencies` — Verify SAP toolchain is correctly installed

## Limitations

- **0 stars, brand new** — Created July 22, 2026. Unproven.
- **SAP toolchain required** — Needs `@sap/cds` and `@sapui5` installed.
- **CAP only** — Doesn't cover SAP ABAP (see abapilot-mcp for that).
- **No BTP deployment** — Scaffolding only. Doesn't deploy to SAP Business Technology Platform.

## Operator Verdict

★★★ **First SAP CAP MCP — fills a real gap.** SAP's 400K+ enterprise customers have been underserved by the MCP ecosystem. Capforge is the first SAP development MCP. Low-risk to try because validation is local and doesn't touch SAP systems. Wait for adoption before depending on it for production projects.
