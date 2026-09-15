---
title: "Strac MCP DLP - Sensitive Data Redaction for AI Agents"
description: Detect and redact PII, PHI, PCI and secrets - SSNs, cards, passports, API keys and cloud credentials - in text and local files before they reach the model, using the Strac DLP API classification engine inside any MCP client
category: Security
stars: n/a (new listing)
added: 2026-09-03
source: "mcp.so feed"
relevance: ★★
tags: [dlp, data-protection, pii-redaction, compliance, security, stdio, api-key]
---

# Strac MCP DLP

**Open-source MCP server (stdio, or Streamable HTTP as a service) that puts a DLP check in front of the model.** Agents are now wired into inboxes, ticketing systems, CRMs and file stores - every tool call is a chance for an SSN, a card number, a patient record or an AWS key to be pulled into a prompt and from there into a model provider's logs. Strac's server detects first and redacts before the agent reasons over the text, using the Strac DLP API for classification. Five tools, thin client, MIT-licensed repository.

```
Server type: Local (stdio via pip install strac-mcp-dlp; --transport streamable-http for services)
Auth: Strac API key (request at strac.io/mcp-integrations)
Tools: 5 (redact_text, detect_sensitive_data, detect_file, redact_file, detokenize)
Pricing: Free tier; classification runs server-side at Strac
Category: Security / Data Protection
Built by: Strac (strac.io)
```

## Why This Matters for Operators

Filtering sensitive data AFTER the model has seen it is too late - it is already in a provider's logs, a vector store or a support ticket. This server moves the check in front of the model: detect, redact, then let the agent work on text that no longer carries the values. The classification catalog covers personal, health and payment data plus secrets - AWS access and secret keys, GitHub, GitLab and Slack tokens, GCP credentials, Azure keys, private keys, and JDBC and MongoDB connection strings.

**Redaction that does not leak.** By default the tools return the TYPES and POSITIONS of what they found, not the values - handing the raw values back would undo the redaction. `include_matched_text=true` is an explicit opt-in. `redact_file` never modifies the original: it writes a copy, refuses an output path that resolves to the source, and will not overwrite an existing file without permission.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `redact_text` | Redact PII/PHI/PCI/secrets from text; modes REDACTED, BLANK, MASK_SEVEN_X, TOKEN_LINK_PLAINTEXT |
| `detect_sensitive_data` | Report which sensitive types are present, unchanged |
| `detect_file` | OCR + classify a local image, PDF, scan, config or source file |
| `redact_file` | Write a redacted copy to disk; original untouched |
| `detokenize` | Resolve Strac vault tokens back to values for authorized, IP-allowlisted callers |

Files under 4 MB are classified inline without storage; larger files go to your Strac document vault. On an unparseable API response the tool errors - it never reports a clean scan it could not verify, because a silent false negative is the one failure a DLP tool cannot have.

## Installation

```bash
pip install strac-mcp-dlp
```

Configure it as a stdio MCP server in Claude Desktop, Claude Code, Cursor or VS Code. Run it as a service with `--transport streamable-http` if you need a shared endpoint. Bring the Strac API key from strac.io/mcp-integrations; every call is authenticated, no anonymous mode.

## Configuration

The key rides in the server environment. `redact_text` takes a `redact_field_mode` (default REDACTED) and the opt-in `include_matched_text`. `detect_file`/`redact_file` take local paths; nothing is classified locally - all detection runs server-side over HTTPS.

## Business Relevance

Compliance-adjacent operations (finance, healthcare-adjacent SaaS, agencies handling client PII) get a cheap first-line control: agents that process support tickets, contracts, invoices or HR files can be pointed at Strac so sensitive values never enter the prompt. It complements the SaaS-side Strac product, which discovers and remediates data across 60+ integrations under policy.

## Integration with CorpusIQ

CorpusIQ agents read sensitive business data (invoices, transactions, payroll) across 40+ connectors. Pairing a DLP gate like Strac means that when an agent composes a summary or a report, the sensitive fields are redacted or tokenized at the tool boundary before they enter the model context - preserving the analysis while keeping PII out of model logs and downstream artifacts.

## Limitations

- All classification runs in Strac's cloud - no local detection models; data in transit is HTTPS
- `detokenize` requires an IP-allowlisted server-to-server key in live mode
- Redaction fidelity depends on Strac's classifiers; positions, not values, are the default return

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [Fallax MCP - Phishing Simulation Results for Audit Evidence](/docs/hermes/mcp/servers/external/fallax-mcp)
- [mcp-sanctions - Watchlist Screening for KYC and AML](/docs/hermes/mcp/servers/external/mcp-sanctions)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
