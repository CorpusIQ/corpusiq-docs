---
title: Microsoft Azure AI Foundry Skills — Enterprise Agent Infrastructure for Hermes Agents
description: Microsoft's official Azure AI Foundry agent skills with 478K+ combined installs. Deploy, manage, and optimize AI agents on Azure with enterprise-grade infrastructure, CI/CD, observability, and fine-tuning.
---

# Microsoft Azure AI Foundry Skills — Setup Guide

**Source:** [microsoft/azure-skills](https://skills.sh/microsoft/azure-skills) (478K+ combined installs)
**Category:** Agent Infrastructure / Cloud
**Quality Tier:** 🟢 Production

Microsoft's official skills for building, deploying, and managing AI agents on Azure AI Foundry. Covers the full agent lifecycle: project creation, model deployment, agent scaffolding, CI/CD pipelines, observability, evaluation, fine-tuning, and troubleshooting. Enterprise-grade infrastructure for production agent deployments.

---

## Installation

```bash
npx skills add microsoft/azure-skills --skill microsoft-foundry
npx skills add microsoft/azure-skills --skill azure-ai
npx skills add microsoft/azure-skills --skill azure-deploy
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **microsoft-foundry** | 478.2K | Full Azure AI Foundry agent platform — create, deploy, invoke, observe, CI/CD, routines, fine-tuning |
| **azure-ai** | 474.4K | Azure AI Services resource and project management |
| **azure-deploy** | 474.1K | Agent deployment, versioning, and multi-environment management |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Azure subscription** | Active Azure account with AI Foundry access |
| **Azure CLI (`az`)** | Install via `curl -sL https://aka.ms/InstallAzureCLIDeb` |
| **Azure Developer CLI (`azd`)** | Install via `curl -fsSL https://aka.ms/install-azd.sh` |
| **Python 3.10+** | For hosted agent development |

---

## Key Capabilities

### Agent Lifecycle Management
- **Create**: Scaffold new agents end-to-end (quick-start) or customize with existing code, A2A, and advanced setups
- **Deploy**: Deploy hosted agents to Foundry, manage versions, multi-environment deploys
- **Invoke**: Send messages to agents, single or multi-turn conversations, WebSocket duplex for voice/real-time
- **Routines**: Schedule or event-trigger agents with CRUD, enable/disable, manual dispatch

### Observability & Quality
- **Observe**: Evaluate agent quality, run batch evals, analyze failures, optimize prompts
- **Trace**: Query traces, analyze latency/failures, correlate eval results
- **Agent Optimizer**: Run optimization jobs, apply candidates locally, deploy through azd
- **Eval Datasets**: Harvest production traces into datasets, version management, regression detection

### Infrastructure
- **Project/Resource Creation**: Create Foundry projects with public or VNet-isolated access
- **Model Deployment**: Unified deployment with intelligent routing (preset, custom, capacity discovery)
- **Fine-tuning**: SFT distillation, DPO preference optimization, RFT with graders
- **CI/CD**: Set up deployment pipelines with azd, continuous evaluation monitoring

---

## Quick Start

```bash
# 1. Authenticate
az login

# 2. Create a new Foundry project (public access)
azd init --template microsoft/azure-ai-foundry-agent
azd up

# 3. Deploy and test an agent
azd deploy
azd invoke --agent my-agent --message "Hello"

# 4. Set up CI/CD
azd pipeline config
```

---

## Verification

```bash
npx skills list | grep microsoft/azure-skills
az account show  # Verify Azure auth
azd version      # Verify azd CLI
```

---

## Notes

- Official Microsoft-maintained skills with 478K+ combined installs — the standard for Azure AI agent infrastructure
- Requires active Azure subscription and cloud resources (not local-only)
- Best for production-grade agent deployments with enterprise requirements (VNet, CI/CD, observability)
- Complements local agent development (Hermes, Claude Code) with cloud deployment capabilities
- Fine-tuning supports SFT, DPO, and RFT with custom graders
