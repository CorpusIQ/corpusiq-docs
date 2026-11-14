---
title: "AWS Skills - CDK, Serverless and Cost Ops Setup"
description: "zxkane/aws-skills: 4.6K combined installs across 6 listings, Claude Code plugins and skills for CDK, serverless, cost ops and Bedrock AgentCore."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/zxkane-aws-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "aws", "cdk", "serverless"]
---

# AWS Skills - Setup Guide

**Source:** [zxkane/aws-skills](https://www.skills.sh/zxkane/aws-skills) via skills.sh - 4.6K combined installs across 6 indexed listings; first seen Nov 13, 2026 (evening sweep)
**GitHub:** 378 stars, MIT licence, `main` branch, last pushed 2026-06-15, six skills under `plugins/<plugin>/skills/<name>/SKILL.md` with per-skill `references/` and the CDK plugin shipping a `validate-stack.sh` script, 65 files in total
**Category:** AWS infrastructure, serverless, cost and Bedrock AgentCore workflows
**Quality Tier:** 🟡 Yellow - six in-tree skills, clean verdicts on the sampled set, but the repo last pushed 2026-06-15 and two skills publish no verdict.

This pack bundles six AWS skills shipped as Claude Code plugins. Five map to plugins that each carry a SKILL.md plus reference material and, in several cases, an integrated MCP server: CDK, cost and operations, serverless event-driven architecture, Bedrock AgentCore, and the shared aws-common dependency that configures the AWS documentation MCP. The sixth, aws-sst-development, covers SST v4 (Ion) as a second infrastructure-as-code path alongside CDK.

The plugins install as a marketplace, with aws-common as a declared dependency of the others. The MCP servers are the notable part: cost and operations ships AWS Pricing, Cost Explorer and CloudWatch, and the CDK plugin ships a CDK MCP, so cost estimates and monitoring queries hit live AWS data rather than a model's memory.

## Installation

```text
/plugin marketplace add zxkane/aws-skills

/plugin install aws-common@aws-skills
/plugin install aws-iac@aws-skills
/plugin install aws-cost-ops@aws-skills
/plugin install serverless-eda@aws-skills
/plugin install aws-agentic-ai@aws-skills
```

Install aws-common first: the other plugins declare it as a dependency. To install a single skill without the marketplace, use npx:

```bash
npx skills add https://github.com/zxkane/aws-skills --skill aws-cdk-development
npx skills add https://github.com/zxkane/aws-skills --skill aws-sst-development
npx skills add https://github.com/zxkane/aws-skills --skill aws-cost-operations
npx skills add https://github.com/zxkane/aws-skills --skill aws-serverless-eda
npx skills add https://github.com/zxkane/aws-skills --skill aws-agentic-ai
npx skills add https://github.com/zxkane/aws-skills --skill aws-mcp-setup
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| aws-cdk-development | 1,193 | CDK expert for building AWS infrastructure with TypeScript or Python: app structure, construct patterns, stack composition and deployment. |
| aws-cost-operations | 914 | Cost optimization, monitoring and operational excellence: bill analysis, cost estimates, CloudWatch alarms, and log, CloudTrail and security reviews. |
| aws-mcp-setup | 756 | Configures the AWS MCP servers: the full server with uvx plus credentials, and the lightweight documentation MCP that needs no auth. |
| aws-serverless-eda | 747 | Serverless and event-driven architecture on the Well-Architected Framework: Lambda, API Gateway, DynamoDB, Step Functions, EventBridge, SQS and SNS. |
| aws-agentic-ai | 695 | Bedrock AgentCore expert for deploying and managing AI agents: Gateway, Runtime, Memory, Identity, Code Interpreter, Browser, Observability and Evaluations. |
| aws-sst-development | 315 | SST v4 (Ion) infrastructure as code: sst.config.ts, infra modules, resource links, IAM scoping, and deploy, dev, diff and remove. |

No indexed listings fall below the threshold; all 6 appear above.

## Why This Matters for Hermes Agents

These skills encode AWS knowledge that an agent would otherwise recall unreliably. CDK resource-naming rules, Well-Architected serverless patterns and Step Functions orchestration are the kind of detail where a wrong guess is expensive, and the skills keep those rules in reference files the agent can read instead of reconstructing them.

The integrated MCP servers are what make the pack more than a prompt. Cost and operations ships AWS Pricing, Cost Explorer and CloudWatch as MCP servers, so cost estimates and monitoring queries hit live AWS data rather than memory. The CDK plugin ships a CDK MCP, and aws-common configures the AWS documentation MCP, so answers track current AWS docs instead of a training snapshot.

The packaging is opinionated in a useful way. Every plugin depends on aws-common, so the documentation MCP comes along automatically rather than being a separate thing to remember. Bedrock AgentCore coverage is unusually complete, spanning the full service list from Gateway through Evaluations.

## Usage

| You say | What happens |
|---|---|
| "Create a CDK stack with a Lambda that processes S3 events" | Runs `aws-cdk-development`, applies CDK naming and bundling conventions, and uses the CDK MCP for current AWS details. |
| "Estimate the monthly cost of 10 Lambda functions with 1M invocations each" | Runs `aws-cost-operations` and uses the AWS Pricing MCP to estimate cost before deployment. |
| "Show me my AWS costs for the last 30 days broken down by service" | Runs `aws-cost-operations` against the Cost Explorer MCP. |
| "Create CloudWatch alarms for my Lambda functions to alert on errors and high duration" | Runs `aws-cost-operations` and wires alarms through the CloudWatch MCP. |
| "Create a serverless API with Lambda and API Gateway for user management" | Runs `aws-serverless-eda` and applies Well-Architected serverless patterns. |
| "Deploy a REST API as an MCP tool using AgentCore Gateway" | Runs `aws-agentic-ai` and sets up the Gateway service for the deployment. |
| "Show me all IAM changes made in the last 7 days" | Runs `aws-cost-operations` and queries CloudTrail. |

## Verification

Probe two skills on the `main` branch before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/zxkane/aws-skills/main/plugins/aws-iac/skills/aws-cdk-development/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/zxkane/aws-skills/main/plugins/aws-cost-ops/skills/aws-cost-operations/SKILL.md
```

Note the layout: skills live at `plugins/<plugin>/skills/<name>/SKILL.md`, not `skills/<name>/SKILL.md`, so a verification script pointed at the flat layout will report a false failure.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| aws-cdk-development | Pass | Pass | Pass |
| aws-cost-operations | Pass | Pass | Pass |
| aws-mcp-setup | Pass | Pass | Pass |
| aws-serverless-eda | Pass | Pass | Pass |

All four sampled skills pass all three auditors. The remaining two (aws-agentic-ai and aws-sst-development) publish no verdict, which is unverified rather than clean. The heavier risk is not the skill files themselves but what they drive: these skills create real AWS resources and configure MCP servers that hold account access, so read each SKILL.md and its references before applying changes to a live account.

## Limitations

- Snapshot data, verified 2026-11-13: 4,620 combined installs across 6 indexed listings; 378 GitHub stars; MIT; last pushed 2026-06-15. Counts drift over time.
- The repo is stale relative to the sweep: last pushed 2026-06-15, roughly five months earlier, so the CDK, Bedrock AgentCore and SST details may lag current AWS service changes.
- `aws-sst-development` sits at 315 installs, the smallest of the six, and targets SST v4 (Ion), a framework that is still moving.
- Two skills (aws-agentic-ai and aws-sst-development) publish no security verdict on skills.sh; treat them as unverified, not clean.
- The MCP servers carry real account access (Pricing, Cost Explorer, CloudWatch), so the blast radius is larger than a documentation-only pack, and credential handling stays your responsibility.
- The skills target AWS only; they do not help with multi-cloud or non-AWS infrastructure.

## Related

- [AWS Agent Toolkit - Official AWS Skills for Hermes Agents](/hermes/skills/catalog/aws-agent-toolkit-setup)
- [Terraform Skill - IaC Testing and Modules Setup](/hermes/skills/catalog/terraform-skill-setup)
- [OpenClaw Secure Linux Cloud - Setup Guide](/hermes/skills/catalog/openclaw-secure-linux-cloud-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install aws-common first. The other plugins declare it as a dependency, and the documentation MCP it configures is what keeps answers current with AWS docs.
- For CDK work, follow the skill's naming rule: do not set explicit resource names when they are optional, so the stack stays redeployable.
- Point the MCP servers at a development account first. Cost Explorer and CloudWatch read live account data, and a bad alarm or estimate against production is harder to unwind.
- Run the pre-deployment checks before committing CDK: npm run build, npm test, npm run lint, cdk synth, then the validate-stack.sh script.
- Use the marketplace path for multi-plugin work and the npx path for a single skill. Either way, keep aws-common present.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
