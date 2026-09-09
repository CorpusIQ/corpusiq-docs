---
title: TrustScan MCP - Security Scanning for MCP Servers and AI Skills
description: Security scanner for MCP servers and AI skills - detects invisible Unicode prompt-injection, dangerous code patterns, hardcoded secrets and typosquat naming, free remote MCP.
category: Compliance
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★
tags: [mcp-security, prompt-injection, supply-chain-security, vulnerability-scanning, ai-security, code-scanning, remote-mcp]
---

# TrustScan MCP

**Remote MCP server (Streamable HTTP, keyless)** - scan MCP servers and AI skills before you trust them: invisible Unicode prompt-injection characters, dangerous code patterns, hardcoded secrets and typosquat naming. Two tools, free, no account.

```
Server type: Remote (Streamable HTTP)
Auth: None (keyless)
Endpoint: https://trust-scan-production.up.railway.app/mcp/
Tools: 2 (trust_scan_server, trust_scan_file)
Pricing: Free scanner, v0.1.0
Category: Compliance
Built by: entradox, registry io.github.entradox/trust-scan
```

## Why This Matters for Operators

Installing an MCP server means running someone else's code next to your data, and the prompt-injection frontier has moved into the tool surface itself: invisible Unicode characters hidden in tool descriptions are a live vector, and typosquat packages that shadow popular server names are a supply-chain hazard. **TrustScan puts a scan step between "found a new MCP server" and "installed it"** - four check classes, one keyless endpoint.

The rules are explicit rather than a black box: MCP001-MCP006 flag eval/exec, shell execution, raw sockets, unsafe deserialization and obfuscated base64, so a finding comes with a reason an operator can act on.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `trust_scan_server` | Scan a directory or file set, including typosquat check against popular MCP server names |
| `trust_scan_file` | Scan a single file |

| Check class | What it detects |
|---|---|
| unicodeInvisible | Steganographic Unicode hidden in tool descriptions and strings |
| patterns | Dangerous code patterns - eval/exec, shell, raw sockets, unsafe deserialization, obfuscated base64 (rules MCP001-MCP006) |
| secrets | Hardcoded credentials and secret material in source files |
| typosquat | Package names close to popular MCP servers via Levenshtein distance |

## Installation

```bash
claude mcp add trust-scan --transport http https://trust-scan-production.up.railway.app/mcp/
```

## Configuration

```json
{
  "mcpServers": {
    "trust-scan": {
      "type": "http",
      "url": "https://trust-scan-production.up.railway.app/mcp/"
    }
  }
}
```

No key or signup - connect and scan.

## Business Relevance

- **Operators adopting community MCP servers** get a pre-install security gate instead of trusting a README.
- **Security teams** get a repeatable scan for the MCP-specific vectors (Unicode injection, typosquat) that generic SAST misses.
- **Teams publishing their own servers** can pre-scan before shipping to partners.
- **Anyone who already runs third-party MCP servers** can retro-scan what is already installed.

## Integration with CorpusIQ

TrustScan fits the CorpusIQ governance loop: every MCP server in this catalog is a candidate to scan before production use, and the scan verdict can gate connector adoption the same way CorpusIQ gates other integrations. A composed workflow: a new server surfaces in a sweep, TrustScan clears it (or flags it), and only then does it enter the operator's stack - discovery, scan, adopt, in one loop.

## Limitations

- Brand new - v0.1.0, no track record yet.
- Two tools only; it is a scanner, not a runtime firewall or continuous monitor.
- Static analysis catches patterns, not intent - a clean scan is necessary but not sufficient.
- Remote endpoint on a railway.app host; no self-host option published.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
