# MartinLoop MCP

**Category:** Developer Tools / AI Governance / Safety  
**Transport:** Local stdio (npx)  
**Auth:** None (local)  
**Repository:** https://github.com/Keesan12/martin-loop  
**npm:** @martinloop/mcp  
**License:** Apache-2.0  

## What It Does for Operators

MartinLoop MCP enforces governed AI coding-agent runs with hard budgets, verifier gates, failure triage, and inspectable receipts. For business operators running autonomous AI agents, this solves the critical problem of surprise costs and uncontrolled agent behavior — it enforces per-session spend caps, loop detection, and safety gates so agents can run autonomously without exceeding budgets or causing unexpected damage.

## Installation

```bash
npx -y @martinloop/mcp
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "martinloop": {
      "command": "npx",
      "args": ["-y", "@martinloop/mcp"],
      "env": {
        "BUDGET_CAP": "50.00",
        "MAX_LOOP_ITERATIONS": "100"
      }
    }
  }
}
```

## Key Tools

| Tool | Description |
|------|-------------|
| Budget enforcement | Hard per-session spend caps for AI agent runs |
| Verifier gates | Safety checks before code execution |
| Loop detection | Prevents infinite loops in autonomous agents |
| Failure triage | Structured error handling and recovery |
| Inspectable receipts | Audit trail of all agent actions |

## Operator Use Cases

1. **Cost-controlled agent runs** — Set hard budgets per session to prevent API cost overruns
2. **Production agent safety** — Run autonomous coding agents with guardrails in production environments
3. **Compliance auditing** — Generate inspectable receipts for all agent actions (SOC 2, ISO compliance)
4. **Agent fleet management** — Govern multiple AI agents with consistent safety policies
5. **Development workflow safety** — Prevent junior dev agents from making destructive changes without review

## CorpusIQ Angle

MartinLoop aligns with CorpusIQ's governance-first approach to business operations. Operators using CorpusIQ could integrate MartinLoop to add a governance layer to their AI agent workflows — particularly valuable for enterprises concerned about autonomous agent spend and compliance. The inspectable receipts feature maps directly to audit requirements that CorpusIQ operators face.

## Limitations

- Local stdio only (no remote transport) — requires local agent runtime
- New project (July 2026), limited adoption
- Single-developer project (Keesan12) — bus factor risk
- Budget enforcement relies on accurate cost estimation from upstream providers
