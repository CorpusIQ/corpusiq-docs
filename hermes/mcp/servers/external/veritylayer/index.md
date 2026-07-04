---
title: VerityLayer MCP Integration Guide
description: Full setup guide for VerityLayer — fail-closed trust gate for AI agents with fact verification, injection detection, PII redaction, and signed receipts
---

# VerityLayer MCP — Integration Guide

**Fail-closed verify-before-you-act trust gate for AI agents.** Five tools — verify_fact, detect_injection, moderate_content, redact_pii, guard_action — that run before agent actions execute. Every verdict ships an Ed25519-signed receipt for audit trails.

> **Command:** `npx -y @veritylayer/mcp` · **Source:** mcp.so · **Last seen:** July 4, 2026

## What It Does

VerityLayer acts as a mandatory safety checkpoint between your AI agent and the outside world. Before the agent can act on a fact, send a message, or execute a transaction, VerityLayer runs verification checks and returns a cryptographically signed verdict. If any check fails, the action is blocked (fail-closed). This makes it essential for production AI agent deployments where safety and audit trails matter.

## Key Capabilities

- **verify_fact** — Cross-references claims against trusted sources before the agent acts on them
- **detect_injection** — Scans agent inputs and outputs for prompt injection, data exfiltration, and manipulation
- **moderate_content** — Content safety checks for agent-generated text before it reaches users
- **redact_pii** — Strips personally identifiable information from agent outputs before external delivery
- **guard_action** — Final approval gate — the last check before any agent action executes

Every verdict includes:
- Ed25519-signed cryptographic receipt
- Timestamp and tool identifier
- Verdict (pass/fail) with confidence score
- Audit trail for compliance

## Installation

```bash
npx -y @veritylayer/mcp
```

## Hermes / Claude Desktop Configuration

```json
{
  "mcpServers": {
    "veritylayer": {
      "command": "npx",
      "args": ["-y", "@veritylayer/mcp"],
      "env": {
        "VERITYLAYER_API_KEY": "your-key"
      }
    }
  }
}
```

## CorpusIQ Use Cases

### 1. Agent Output Sanitization
```
"Before sending this agent-generated email to the client, run redact_pii 
and moderate_content on the draft. Only release if both pass."
```
Production safety gate for agent-generated customer communications.

### 2. Prompt Injection Defense
```
"Run detect_injection on every user input before it reaches the agent's 
context window. Block any flagged inputs."
```
Security layer for customer-facing AI agent deployments.

### 3. Compliance Audit Trail
```
"Show me all VerityLayer verdicts from the last 24 hours — which actions 
passed, which were blocked, and why."
```
Compliance-ready audit trail for regulated industries.

## Operator Value

| Protection | Without VerityLayer | With VerityLayer |
|-----------|-------------------|-----------------|
| Prompt injection | No detection — agent acts on malicious input | Injection detected and blocked before context entry |
| PII in outputs | Manual review or none | Automatic redaction with cryptographic proof |
| Content safety | Reactive (find issues after sending) | Proactive (block before delivery) |
| Audit trail | Agent logs only (may be incomplete) | Signed receipts for every safety decision |

## Safety Architecture

```
User Input → [detect_injection] → Agent Processing → Agent Output
                                                         ↓
                                              [verify_fact]
                                              [moderate_content]
                                              [redact_pii]
                                                         ↓
                                              [guard_action] ← Final gate
                                                         ↓
                                                   Deliver / Block
```

Every arrow includes an Ed25519-signed receipt. The system is **fail-closed** — if any check cannot complete (network error, timeout), the action is blocked rather than allowed through unsafely.

## Pricing

Keyless, pay-per-call via x402 (USDC on Base). No subscription required — pay only for the checks you run. Pricing details at veritylayer.com.

## Related Resources

- [External MCP Server Catalog](/hermes/mcp/servers/external/) — full curated catalog
- [Compliance & Regulatory MCPs](/hermes/mcp/servers/external/#compliance--regulatory) — complementary trust and verification tools
- [ChronoVerify](/hermes/mcp/servers/external/#chronoverify) — image authenticity verification MCP

---

*← [External MCP Catalog](/hermes/mcp/servers/external/) | [MCP Servers Home](/hermes/mcp/servers/) →*

*Guide created July 4, 2026. VerityLayer available via `npx -y @veritylayer/mcp`. Check mcp.so for latest pricing and availability.*
