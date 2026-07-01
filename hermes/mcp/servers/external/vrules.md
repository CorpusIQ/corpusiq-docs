---
title: "vrules — Agent Governance & LLM Guardrails Integration Guide"
description: "Connect AI agents to vrules for policy-as-code governance, guardrail enforcement, and programmable agent fleet control. Vendor-neutral, open-source framework for production AI deployments."
---

# vrules — Agent Governance & LLM Guardrails

**Open-source, vendor-neutral agent-governance and LLM guardrails framework.** A vector-enabled rules engine that provides MCP proxying, policy-as-code enforcement, conditional organizational memory, and browser/WASM execution. Designed for operators deploying AI agent fleets in production who need programmable guardrails without vendor lock-in.

| Detail | Value |
|--------|-------|
| **GitHub** | [ops-ping/vrules](https://github.com/ops-ping/vrules) |
| **Language** | TBD (check repo) |
| **Transport** | MCP proxy (stdio) |
| **Stars** | ★0 (new — July 1, 2026) |
| **License** | Open source |

## Why This Matters for Operators

As AI agent deployments move from experimental to production, operators face three hard problems:
1. **Guardrails**: How do you prevent agents from taking dangerous actions without blocking legitimate work?
2. **Policy enforcement**: How do you ensure every agent follows organizational rules (data handling, spend limits, approval chains)?
3. **Vendor independence**: How do you avoid locking governance into a single AI provider's framework?

vrules solves all three:
- **Vector-enabled rules engine**: Rules match semantically, not just by exact string — an agent asking "delete the prod database" and "clean up the main DB" both trigger the same guardrail
- **MCP proxying**: Sits between your agents and their MCP servers, intercepting every tool call for policy evaluation
- **Policy-as-code**: Define rules as version-controlled code, not UI click-ops
- **Conditional organizational memory**: Agents can access approved knowledge while being blocked from sensitive data
- **Browser/WASM execution**: Run rules securely in a sandboxed environment

## Use Cases for Operators

| Scenario | How vrules Helps |
|----------|-----------------|
| **Multi-agent deployments** | Enforce consistent policies across Claude Code, Cursor, Codex, and custom agents through one proxy |
| **Financial operations** | Block agents from initiating transactions above thresholds, require human approval for payments |
| **Customer data handling** | Ensure agents never expose PII in logs, responses, or external API calls |
| **Compliance automation** | Codify regulatory rules (GDPR, SOC 2, HIPAA) as enforceable policies |
| **Agent fleet management** | Apply organization-wide policies while allowing team-specific overrides |

## Prerequisites

- **MCP-compatible agent** (Claude Desktop, Claude Code, Cursor, Windsurf, etc.)
- **Node.js or Python** (check repo for runtime requirements)
- **Vector store** (optional — for semantic rule matching)

## Installation

```bash
git clone https://github.com/ops-ping/vrules.git
cd vrules
# Check repo README for specific install instructions
# Typically: npm install or pip install
```

## MCP Client Configuration

Add vrules as a proxy between your agents and their MCP servers:

```json
{
  "mcpServers": {
    "vrules-proxy": {
      "command": "npx",
      "args": ["-y", "@ops-ping/vrules"],
      "env": {
        "VRULES_POLICY_PATH": "/path/to/policies",
        "VRULES_MODE": "enforce"
      }
    },
    "corpusiq": {
      "url": "https://mcp2.corpusiq.io/mcp",
      "transport": "streamable-http",
      "proxy": "vrules-proxy"
    }
  }
}
```

## Policy Examples

### Block destructive database operations
```yaml
# policy: block-destructive-db.yaml
name: block-destructive-db
match:
  semantic: ["drop database", "delete all records", "truncate table", "rm -rf /data"]
  tools: ["database_query", "terminal"]
action: require_human_approval
message: "Destructive database operation detected. Human approval required."
```

### Enforce spend limits
```yaml
# policy: spend-limits.yaml
name: enforce-spend-limits
match:
  tools: ["stripe_charge", "create_payment", "x402_pay"]
  conditions:
    - field: amount
      operator: gt
      value: 100
action: block
message: "Payment exceeds $100 limit. Request manager approval."
```

### PII redaction
```yaml
# policy: pii-redaction.yaml
name: redact-pii
match:
  patterns: ["\\b\\d{3}-\\d{2}-\\d{4}\\b", "\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b"]
  scope: all_outputs
action: redact
message: "PII detected and redacted from agent output."
```

## Verification

After setup, verify vrules is intercepting:

```bash
# Test that a blocked action is caught
# In your MCP client, try: "Delete all test data from the database"
# The agent should respond with the vrules rejection message
```

## Complements CorpusIQ

CorpusIQ provides read-only access to 37+ business data sources with OAuth 2.1 PKCE. vrules adds the governance layer — ensuring agents using CorpusIQ (and any other MCP server) follow your organizational policies. Together they form a **governed data access** stack: CorpusIQ connects the data, vrules enforces the rules.

## Notes

- This server was discovered on July 1, 2026 via GitHub API. It is brand new — check the repo for latest installation instructions and API changes.
- The vector-enabled rules engine means policies can match intent, not just exact strings — a significant advantage over regex-based guardrails.
- Vendor-neutral design means the same policies work across Claude, GPT, Gemini, and open-source models.

---

*Integration guide created July 1, 2026 (PM evening) by CorpusIQ MCP Discovery Scanner*
*Server source: [github.com/ops-ping/vrules](https://github.com/ops-ping/vrules)*
