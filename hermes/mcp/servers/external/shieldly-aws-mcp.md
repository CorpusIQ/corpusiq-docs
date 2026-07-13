---
title: "Shieldly AWS Security MCP — IAM & CloudFormation Analysis"
description: "AI-powered security analysis for AWS — analyze IAM policies and CloudFormation templates from any MCP client."
category: mcp
tags: [mcp-server, aws, security, iam, cloudformation, devops]
last_updated: 2026-07-12
---

# Shieldly AWS Security MCP Server ★ New (July 12)

AI-Powered Security Analysis for AWS — the official MCP server from shieldly.io. Analyze IAM policies and CloudFormation templates from any MCP client. Catch over-privileged roles, policy violations, and infrastructure misconfigurations before they reach production.

**Source:** mcp.so (submitted July 12, 2026) · **GitHub:** shieldly-io (exact repo TBD)

## What It Is

An official MCP server from Shieldly that brings AWS security analysis into AI agent workflows. Operators can ask agents to review IAM policies for least-privilege violations, scan CloudFormation templates for security gaps, or audit existing infrastructure — all from within their MCP client.

## Business Relevance

- **DevOps/SRE teams** can shift-left security analysis into development workflows
- **Compliance operators** can audit IAM policies against SOC 2 / ISO 27001 requirements
- **Cloud architects** can validate CloudFormation templates before deployment
- **CorpusIQ complement** for businesses managing AWS infrastructure alongside business data

## Tools Available

| Tool | Description |
|------|-------------|
| `analyze_iam_policy` | Review IAM policy for over-privilege, wildcards, risky actions |
| `analyze_cloudformation` | Scan CF template for security misconfigurations |
| `audit_role` | Full role analysis — attached policies, trust relationships, last used |
| `suggest_fixes` | Generate least-privilege policy recommendations |

## Quick Start

```bash
# Install via npx
npx @shieldly-io/mcp-server

# Or add to MCP client config
{
  "mcpServers": {
    "shieldly": {
      "command": "npx",
      "args": ["@shieldly-io/mcp-server"],
      "env": {
        "SHIELDLY_API_KEY": "your-api-key",
        "AWS_REGION": "us-east-1"
      }
    }
  }
}
```

## Business Use Cases

1. **Pre-deployment security review:** "Scan this CloudFormation template for security issues before we deploy"
2. **IAM audit:** "Check all IAM roles in this account for over-privileged policies"
3. **Compliance evidence:** "Generate a report showing all IAM roles comply with least-privilege principle"
4. **Incident response:** "Analyze this IAM policy that was modified — what new risks does it introduce?"

## Limitations

- Requires Shieldly API key and AWS credentials with read access
- Analysis scope limited to IAM and CloudFormation (not full AWS security suite)
- Community-reported; verify analysis accuracy against AWS IAM Access Analyzer
- Requires outbound internet access from agent host

## See Also

- [SaferAgenticAI MCP](/hermes/mcp/servers/external/saferagenticai-mcp/) — Agentic AI security guardrails
- [AI Governance Evidence MCP](#) — EU AI Act, ISO 42001 compliance evidence
