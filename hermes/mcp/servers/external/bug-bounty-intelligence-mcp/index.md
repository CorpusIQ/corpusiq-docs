---
title: "bug-bounty-intelligence-mcp — Smart Contract Security Analysis"
description: "AI-powered smart contract security analysis trained on 27,681 real Sherlock/Code4rena findings. USDC/scan via x402 on Base."
source: github.com/holistis/bug-bounty-intelligence-mcp
stars: 0
language: TypeScript
transport: stdio
auth: x402 micropayments (USDC on Base)
category: Security
last_updated: 2026-07-20
---

# bug-bounty-intelligence-mcp — Smart Contract Security

**AI-powered smart contract security analysis** trained on 27,681 real-world findings from Sherlock and Code4rena audit contests. Pay-per-scan via x402 USDC micropayments on Base.

## Installation

```bash
npx -y bug-bounty-intelligence-mcp
```

## Config

```json
{
  "mcpServers": {
    "bug-bounty": { "command": "npx", "args": ["-y", "bug-bounty-intelligence-mcp"] }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| `scan_contract` | Analyze a smart contract for vulnerabilities |
| `get_finding_detail` | Detailed report on a specific vulnerability class |
| `list_audit_contests` | Browse past Sherlock/Code4rena contests |

## Operator Use Cases

- Web3 operators: pre-audit smart contracts before formal audit firms
- DeFi teams: continuous security scanning in CI/CD
- Bug bounty hunters: AI-assisted vulnerability research
