---
title: "SaferAgenticAI MCP — AI Safety Governance for Agentic Coding"
description: "Apply the Safer Agentic AI safety framework to coding assistants over MCP. Governance guardrails, safety checks, and policy enforcement for agentic workflows."
category: mcp
tags: [mcp-server, ai-safety, agentic-ai, governance, security, guardrails]
last_updated: 2026-07-02
---

# SaferAgenticAI MCP — AI Safety Framework

## What It Is

SaferAgenticAI MCP (`NellInc/SaferAgenticAI`) brings the Safer Agentic AI safety framework to coding assistants over the Model Context Protocol. It enforces governance guardrails, safety checks, and policy constraints on agent actions — ensuring agentic workflows comply with organizational safety policies before executing tool calls, file operations, or external API requests.

## Tools Available

| Tool | Description |
|------|-------------|
| Safety check | Pre-execution validation of agent actions against policy |
| Policy enforcement | Rule-based guardrails for tool calls and code execution |
| Audit logging | Record of all safety decisions and policy violations |

## Quick Start

```bash
uvx saferagenticai-mcp
```

## Business Use Cases

1. **Production agent guardrails**: Deploy Hermes agents in production with safety checks on file writes, network calls, and tool invocations
2. **Compliance enforcement**: Ensure agents never access PII, write to restricted directories, or call unapproved APIs
3. **Multi-agent governance**: Apply consistent safety policies across all agent instances in a team
4. **Audit trail**: Every safety decision logged for SOC 2, HIPAA, or internal compliance review

## Limitations

- **Research-stage**: Part of the NellInc research repository — not yet production-hardened
- **Coding assistant focus**: Primarily designed for coding agents (Codex, Claude Code); may need adaptation for business operations agents
- **No remote transport**: Local-only via `uvx`

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [VRules MCP — AI Governance](/hermes/mcp/servers/external/vrules/)
- [CorpusIQ Governance System](/hermes/governance/)
