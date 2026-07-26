---
title: AWS Agent Toolkit — Official AWS Skills for Hermes Agents
description: AWS's official agent toolkit — MCP servers, skills, and plugins for building on AWS. 4.3K+ combined installs across 19 core skills covering IAM, CDK, serverless, containers, databases, and AI/ML.
---

# AWS Agent Toolkit — Setup Guide

**Source:** [aws/agent-toolkit-for-aws](https://skills.sh/aws/agent-toolkit-for-aws) (4.3K+ combined installs)
**GitHub:** [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) (2,119 ⭐)
**Category:** Platform / Cloud Infrastructure
**Quality Tier:** 🟢 Production

The AWS Agent Toolkit is the official AWS-supported collection of MCP servers, skills, and plugins for AI agents building on AWS. It provides agent-native access to IAM, CDK, CloudFormation, serverless (Lambda), containers (ECS/EKS), databases (RDS/DynamoDB), networking (VPC), observability (CloudWatch), and AI/ML (Bedrock). Every skill teaches agents the idiomatic AWS way to provision, secure, and operate cloud infrastructure.

---

## Installation

```bash
# Core infrastructure skills (highest installs)
npx skills add aws/agent-toolkit-for-aws --skill aws-iam
npx skills add aws/agent-toolkit-for-aws --skill aws-cdk
npx skills add aws/agent-toolkit-for-aws --skill aws-cloudformation
npx skills add aws/agent-toolkit-for-aws --skill aws-billing-and-cost-management

# Compute and containers
npx skills add aws/agent-toolkit-for-aws --skill aws-compute
npx skills add aws/agent-toolkit-for-aws --skill aws-containers
npx skills add aws/agent-toolkit-for-aws --skill aws-serverless

# Data and networking
npx skills add aws/agent-toolkit-for-aws --skill aws-database
npx skills add aws/agent-toolkit-for-aws --skill aws-networking
npx skills add aws/agent-toolkit-for-aws --skill aws-messaging-and-streaming

# Operations and observability
npx skills add aws/agent-toolkit-for-aws --skill aws-observability
npx skills add aws/agent-toolkit-for-aws --skill aws-deployment

# AI and ML
npx skills add aws/agent-toolkit-for-aws --skill amazon-bedrock

# SDK usage
npx skills add aws/agent-toolkit-for-aws --skill aws-sdk-js-v3-usage
npx skills add aws/agent-toolkit-for-aws --skill aws-sdk-python-usage

# Onboarding
npx skills add aws/agent-toolkit-for-aws --skill launch-with-aws
npx skills add aws/agent-toolkit-for-aws --skill signing-in-to-aws
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **aws-iam** | 4.3K | IAM policies, roles, and permissions with least-privilege access patterns |
| **aws-cdk** | 3.9K | Cloud Development Kit for infrastructure-as-code in TypeScript or Python |
| **aws-billing-and-cost-management** | 3.6K | Cost analysis, budgets, anomaly detection, and savings plan management |
| **aws-cloudformation** | 3.6K | CloudFormation templates for declarative infrastructure provisioning |
| **aws-containers** | 3.5K | ECS, EKS, and Fargate for container orchestration at any scale |
| **connecting-to-data-source** | 2.8K | Data source connectivity via VPC endpoints, proxies, and federated queries |
| **aws-serverless** | — | Lambda, API Gateway, Step Functions, and EventBridge patterns |
| **aws-compute** | — | EC2, Auto Scaling, Spot Instances, and placement groups |
| **aws-database** | — | RDS, DynamoDB, ElastiCache, and DocumentDB managed databases |
| **aws-networking** | — | VPC, subnets, security groups, load balancers, and Route 53 |
| **aws-observability** | — | CloudWatch, X-Ray, and CloudTrail for monitoring and tracing |
| **aws-deployment** | — | CodeDeploy, CodePipeline, and ECR for CI/CD on AWS |
| **aws-messaging-and-streaming** | — | SQS, SNS, Kinesis, and MSK for event-driven architectures |
| **amazon-bedrock** | — | Bedrock foundation models, knowledge bases, agents, and guardrails |
| **aws-blocks** | — | AWS Blocks visual infrastructure builder patterns |
| **signing-in-to-aws** | — | SSO, IAM Identity Center, and credential management for agents |
| **launch-with-aws** | — | New account setup, best-practice foundations, and Control Tower |
| **aws-sdk-js-v3-usage** | — | AWS SDK for JavaScript v3 with modular client patterns |
| **aws-sdk-python-usage** | — | Boto3 idiomatic Python patterns for AWS APIs |
| **aws-sdk-swift-usage** | — | AWS SDK for Swift with native iOS and macOS patterns |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **AWS Account** | Free tier available at https://aws.amazon.com/free |
| **AWS CLI** | Install via `pip install awscli` or package manager |
| **AWS credentials** | Configure with `aws configure` or IAM Identity Center |
| **Node.js 18+** | Required for CDK in TypeScript and JavaScript |
| **Python 3.9+** | Required for Boto3 SDK skills |

---

## Key Capabilities

### IAM and Security
Identity and Access Management skills teach agents to create least-privilege policies, assume roles across accounts, manage service-linked roles, configure permission boundaries, and audit access patterns. The IAM skill has the highest install count for a reason: every AWS operation starts with authentication.

### Infrastructure as Code
Three IaC paths available: CDK (high-level, TypeScript or Python), CloudFormation (declarative YAML or JSON), and AWS Blocks (visual builder). The CDK skill covers constructs, stacks, environments, and automated testing of infrastructure definitions.

### Serverless and Containers
Lambda function patterns including event sources, error handling, and cold start mitigation. API Gateway REST and HTTP API design. Step Functions state machines for complex workflows. ECS task definitions with service auto-scaling. EKS cluster management through `eksctl` and Helm.

### AI and ML with Bedrock
Invoke foundation models including Claude, Llama, and Titan. Create knowledge bases with RAG architecture. Build AI agents with action groups. Configure guardrails for responsible AI. Manage model access through the Bedrock API.

### Observability
CloudWatch metrics, logs, and alarms for proactive monitoring. X-Ray distributed tracing across microservices. CloudTrail for API audit logging. Set up dashboards and anomaly detection for Hermes-managed infrastructure.

---

## Quick Start

```bash
# 1. Install AWS CLI and configure credentials
aws configure

# 2. Add the core IAM skill
npx skills add aws/agent-toolkit-for-aws --skill aws-iam

# 3. Add CDK for infrastructure-as-code
npx skills add aws/agent-toolkit-for-aws --skill aws-cdk

# 4. Bootstrap your first CDK app
mkdir my-agent-infra && cd my-agent-infra
npx cdk init app --language typescript
npx cdk bootstrap
```

---

## Hermes Integration Notes

- **Infrastructure automation:** Use `aws-cdk` and `aws-cloudformation` to provision Hermes worker nodes, MCP servers, and data pipelines
- **Cost governance:** `aws-billing-and-cost-management` enables Hermes to monitor and optimize AWS spend within the $250/month budget
- **Serverless agents:** `aws-serverless` and `aws-containers` provide patterns for deploying agent backends on Lambda or ECS Fargate
- **AI workloads:** `amazon-bedrock` unlocks Claude, Llama, and other models for agent inference directly on AWS infrastructure
- **Event-driven growth ops:** `aws-messaging-and-streaming` enables SQS, SNS, and Kinesis pipelines for processing social signals and lead events

---

## Links

- **skills.sh:** https://skills.sh/aws/agent-toolkit-for-aws
- **GitHub:** https://github.com/aws/agent-toolkit-for-aws
- **AWS Docs:** https://docs.aws.amazon.com
- **CDK Docs:** https://docs.aws.amazon.com/cdk
