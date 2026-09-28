---
title: Sunglasses MCP - Local Input Firewall for AI Agents
description: "Sunglasses is a local input firewall for AI agents: scans text and files for prompt injection, leaks and exfiltration."
category: Security
stars: n/a (new listing)
added: 2026-09-27
source: "mcpservers.org + github.com/sunglasses-dev/sunglasses"
relevance: ★★★
tags: [prompt-injection, security, input-firewall, credential-leaks, data-exfiltration, agent-security, self-hosted]
---

# Sunglasses MCP

**A local input firewall that screens everything your agent reads.** Sunglasses runs offline on the operator's machine and exposes MCP tools that scan text and files for prompt injection, credential leaks and data exfiltration against 1,554 patterns across 118 categories. A third tool reports the active pattern set, so operators know exactly what the scanner is enforcing.

```
Server type: Local (stdio, self-hosted)
Auth: none (local process)
Endpoint: python -m sunglasses.mcp
Tools: 3 (scan_text, scan_file, scanner_info)
Pricing: free and open source
Category: Security
Built by: Sunglasses (github.com/sunglasses-dev/sunglasses)
```

## Why This Matters for Operators

Agents read untrusted content constantly: web pages, documents, tickets, emails. Prompt injection hides in that content, and a compromised agent with access to business tools is a real loss vector. Sunglasses gives operators a local, offline gate that screens text and files before the agent acts on them, without sending any data to a third-party scanner.

For operators who handle client or regulated data, the offline property is the point: the scan runs entirely on the machine, so documents never leave the environment to be checked for leaks.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| scan_text | Screen a text block for injection, leaks and exfiltration patterns |
| scan_file | Screen a file's contents with the same pattern set |
| scanner_info | Report the active pattern set and version |

## Installation

```bash
pip install sunglasses
python -m sunglasses.mcp
```

Start the module and connect it to any MCP client as a stdio server.

## Configuration

```json
{
  "mcpServers": {
    "sunglasses": {
      "command": "python",
      "args": ["-m", "sunglasses.mcp"]
    }
  }
}
```

## Business Relevance

- **Ops teams** gate agent input against injection and leak patterns
- **Security leads** get a local, offline screening layer with no data egress
- **Agencies handling client documents** scan before the agent processes files
- **Founders** add defense in depth around agents with business tool access

## Integration with CorpusIQ

Sunglasses fits the CorpusIQ security posture: before external content from email connectors or web fetches enters an agent workflow, scan_text can screen it. For CorpusIQ-powered agent deployments, Sunglasses is a complementary local layer to the guardrails doctrine, screening untrusted input before any external action fires.

## Limitations

- Pattern-based: novel injection techniques may slip past static rules
- Local stdio server; each agent host needs its own installation
- Single-purpose security tool, not a full agent security platform
- New listing with no long track record

## FAQ

### Does any data leave the machine?

No. Sunglasses runs fully offline as a local process.

### What does it scan for?

Prompt injection, credential leaks and data exfiltration across 1,554 patterns in 118 categories.

### What are the three tools?

scan_text, scan_file and scanner_info, the last reporting the active pattern set.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
