---
title: "pacs008-mcp — ISO 20022 Credit Transfer Generator MCP"
description: "Generate, validate, parse & audit ISO 20022 pacs.008 credit transfers from MCP clients. 10 tools, scheme-aware (CBPR+/HVPS+/Fedwire/CHAPS/T2/SCT-Inst). Part of ISO 20022 MCP Suite."
source: github.com/sebastienrousseau/pacs008-mcp
stars: 0
language: Python
transport: stdio
category: Finance & Fintech
last_updated: 2026-07-20
---

# pacs008-mcp — ISO 20022 Credit Transfer Generator

**Generate, validate, and audit ISO 20022 pacs.008 FI-to-FI Customer Credit Transfer messages from AI agents.** Part of the [ISO 20022 MCP Suite](https://github.com/sebastienrousseau).

## Installation

```bash
pip install pacs008-mcp
pacs008-mcp
```

## Config

```json
{
  "mcpServers": {
    "pacs008": { "command": "pacs008-mcp" }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `generate_transfer` | Generate a pacs.008 XML message from structured input |
| `validate` | Validate against ISO 20022 XSD + scheme rules |
| `parse` | Parse an incoming pacs.008/004/002 message |
| `convert_mt103` | Convert legacy SWIFT MT103 to pacs.008 |
| `structured_address_check` | November 2026 structured address cliff toolkit |

## Operator Use Cases

- Generate ISO 20022-compliant credit transfers from AI agents
- Validate outgoing payments before submission to banking rails
- Convert legacy SWIFT MT103 messages to pacs.008 format
- Audit payment messages for CBPR+ compliance

## Limitations

- Early-stage (0⭐), part of newer suite
- Requires pacs.008 domain knowledge
