---
title: "AWS Agent Plugins - Official AWS Plugin Suite Setup"
description: "awslabs/agent-plugins - 4.3K combined installs: AWS official agent plugins for architecting, deploying and operating on AWS."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/aws-agent-plugins-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "aws", "cloud", "serverless"]
---

# AWS Agent Plugins - Setup Guide

**Source:** [awslabs/agent-plugins](https://www.skills.sh/awslabs/agent-plugins) via skills.sh - 4.3K combined installs across 36 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 morning sweep)
**GitHub:** [awslabs/agent-plugins](https://github.com/awslabs/agent-plugins) - 949 stars, Apache-2.0, main branch, last pushed Nov 20, 2026; one plugin per directory under plugins/<name>/ with skills/<skill>/SKILL.md plus .claude-plugin and .codex-plugin manifests and MCP configs.
**Category:** AWS Cloud Development and Operations
**Quality Tier:** 🟡 Yellow - dataset-transformation (Snyk) and hyperpod-issue-report (Socket) carry Warn cells; the other 13 sampled skills pass all three checks.

Agent Plugins for AWS (awslabs/agent-plugins) is AWS's official collection of agent plugins that equip AI coding agents with the skills to architect, deploy and operate on AWS. Supported by Claude Code, Codex and Cursor, with an experimental Kiro path, the repository packages skills, MCP servers, hooks and references into per-plugin directories covering serverless, deployment, databases, migration, location services, Amplify and SageMaker AI. The README notes that the newer Agent Toolkit for AWS is the successor for production software, while this repository continues to work and accept contributions.

The 36 indexed skills are dominated by SageMaker and serverless workflows: model customization planning, dataset work, fine-tuning, deployment and evaluation, plus HyperPod cluster diagnostics. Install counts run from 20 to 403, with aws-architecture-diagram the most-installed listing.

## Installation

The README documents plugin installation for Claude Code, Codex, Cursor and Kiro rather than a skills.sh installer. Use the standard skills installer to add the skills:

```bash
npx skills add awslabs/agent-plugins
```

For Claude Code, the README documents adding the marketplace and installing individual plugins:

```text
/plugin marketplace add awslabs/agent-plugins
/plugin install aws-serverless@agent-plugins-for-aws
```

Codex discovers the repository through .agents/plugins/marketplace.json, and Cursor offers the deploy-on-aws plugin from its marketplace. Because this is a many-plugin repository, install the specific plugins you need rather than the whole tree.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| aws-architecture-diagram | 403 | generating validated AWS architecture diagrams as draw.io XML |
| aws-lambda | 265 | designing, building and debugging serverless apps with Lambda |
| deploy | 245 | deploying applications to AWS with cost estimates and IaC |
| use-case-specification | 188 | defining the business problem and success criteria for model customization |
| directory-management | 187 | managing project directory setup and artifact organization |
| planning | 172 | discovering intent and generating a plan for model customization |
| dataset-evaluation | 160 | validating dataset format and quality for SageMaker fine-tuning |
| aws-serverless-deployment | 159 | SAM and CDK deployment for serverless applications |
| model-deployment | 158 | deploying fine-tuned models to SageMaker endpoints or Bedrock |
| finetuning | 158 | generating fine-tuning code for SageMaker serverless training |
| dataset-transformation | 157 | transforming datasets between ML schemas |
| hyperpod-ssm | 154 | remote command execution on HyperPod nodes via SSM |
| hyperpod-version-checker | 153 | checking software component versions on HyperPod clusters |
| hyperpod-issue-report | 151 | generating issue reports from HyperPod clusters |

The remaining 22 indexed listings range from 20 to 144 installs.

## Why This Matters for Hermes Agents

AWS guidance is long and context-heavy, and this repository is the official effort to encode it as reusable, versioned skills that an agent invokes when relevant instead of pasting documentation into every prompt. The plugin packaging model (skills, MCP servers, hooks and references in one unit) is the emerging standard for steering coding agents, so reading this repository is also the fastest way to learn how AWS structures that packaging. The serverless and SageMaker skills are immediately practical: aws-lambda and aws-serverless-deployment cover the build-and-deploy loop, while the SageMaker set covers the whole model customization lifecycle from planning through dataset work, fine-tuning, deployment and evaluation. The HyperPod diagnostics skills (hyperpod-ssm plus version, issue and performance debuggers) fill a real gap, since they script the collection of cluster logs and node state that otherwise has to be assembled by hand for AWS Support. The tradeoff is that this is a broad, multi-plugin library rather than a single hardened product: several plugins generate infrastructure code and MCP configurations, which carries a larger audit surface than Markdown-only skills.

## Usage

| You say | What happens |
|---|---|
| Deploy this app to AWS | deploy analyzes the codebase and deploys to recommended services |
| Draw an AWS architecture diagram | aws-architecture-diagram generates validated draw.io XML |
| Build a serverless API with Lambda | aws-lambda guides design, build and debug for serverless apps |
| Is my dataset ready for fine-tuning | dataset-evaluation validates format and schema |
| Fine-tune my model on SageMaker | planning scopes the work and finetuning generates the training code |
| Deploy my fine-tuned model | model-deployment picks the pathway and generates deployment code |
| Diagnose my HyperPod cluster | hyperpod-ssm runs commands on nodes and the debuggers collect diagnostics |

## Verification

Confirm the aws-lambda skill body resolves on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/awslabs/agent-plugins/main/plugins/aws-serverless/skills/aws-lambda/SKILL.md | head -30
```

After install, confirm the skills landed in the agent skills directory. In Claude Code, confirm the marketplace was added before running /plugin install.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| aws-architecture-diagram | Pass | Pass | Pass |
| aws-lambda | Pass | Pass | Pass |
| deploy | Pass | Pass | Pass |
| use-case-specification | Pass | Pass | Pass |
| directory-management | Pass | Pass | Pass |
| planning | Pass | Pass | Pass |
| dataset-evaluation | Pass | Pass | Pass |
| aws-serverless-deployment | Pass | Pass | Pass |
| model-deployment | Pass | Pass | Pass |
| finetuning | Pass | Pass | Pass |
| dataset-transformation | Pass | Pass | Warn |
| hyperpod-ssm | Pass | Pass | Pass |
| hyperpod-version-checker | Pass | Pass | Pass |
| hyperpod-issue-report | Pass | Warn | Pass |
| model-evaluation | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 24, 2026: 4,280 combined installs across 36 indexed listings; 949 GitHub stars; Apache-2.0 license; last pushed Nov 20, 2026. Counts drift over time.
- The README positions this repository behind the newer Agent Toolkit for AWS, which it names as the recommended successor for production software.
- The README documents plugin installation for Claude Code, Codex, Cursor and Kiro, not a skills.sh installer; the npx skills add command is a standard fallback rather than a documented path.
- The databases-on-aws plugin is marked "Some Services Available" (Aurora DSQL only) in the README.
- Kiro conversion drops hooks entirely, and Claude-specific hooks are not yet wired into the Codex manifests.

## Related

- [AWS Agent Toolkit - Official AWS Skills for Hermes Agents](/hermes/skills/catalog/aws-agent-toolkit-setup)
- [AWS Skills - CDK, Serverless and Cost Ops Setup](/hermes/skills/catalog/zxkane-aws-skills-setup)
- [Cloudflare Skills - Edge Computing & Workers Platform](/hermes/skills/catalog/cloudflare-skills-setup)
- [Docker Agent Skills - Container Workflow Suite](/hermes/skills/catalog/docker-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install plugins individually (/plugin install <name>@agent-plugins-for-aws) rather than the whole marketplace.
- Review generated code before deployment and run security scanning on generated infrastructure code, as the README recommends.
- Use least-privilege AWS credentials; several plugins generate IaC that needs real AWS access to deploy.
- Keep plugins updated to pick up the latest AWS best practices.
- For production builds, evaluate the Agent Toolkit for AWS, which the README names as the successor.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
