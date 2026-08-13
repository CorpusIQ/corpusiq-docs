---
title: HashiCorp Agent Skills — Terraform & Packer for Hermes Agents
description: HashiCorp's official agent skills collection — Terraform and Packer workflows for infrastructure-as-code. 3.2K+ installs with agent-native infrastructure provisioning patterns.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hashicorp-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# HashiCorp Agent Skills — Setup Guide

**Source:** [hashicorp/agent-skills](https://skills.sh/hashicorp/agent-skills) (3.2K+ installs)
**GitHub:** [hashicorp/agent-skills](https://github.com/hashicorp/agent-skills) (759 ⭐)
**Category:** Infrastructure / DevOps
**Quality Tier:** 🟢 Production

HashiCorp Agent Skills provides agent-native workflows for Terraform (infrastructure-as-code) and Packer (machine image building). These skills teach Hermes agents to provision, manage, and version cloud infrastructure across AWS, GCP, Azure, and other providers using HashiCorp's industry-standard tools.

---

## Installation

```bash
# Terraform (3.2K installs)
npx skills add hashicorp/agent-skills --skill terraform-search-import

# Packer
npx skills add hashicorp/agent-skills --skill packer
```

---

## Included Skills

| Skill | Installs | Purpose |
|---|---|---|
| **terraform-search-import** | 3.2K | Import existing cloud resources into Terraform state with search and bulk import |

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Terraform CLI** | `brew install terraform` or download from https://developer.hashicorp.com/terraform |
| **Packer CLI** | `brew install packer` or download from https://developer.hashicorp.com/packer |
| **Cloud provider credentials** | AWS, GCP, or Azure credentials configured for Terraform |
| **HCP account (optional)** | HashiCorp Cloud Platform for remote state and team workflows |

---

## Key Capabilities

### Terraform Search and Import
The primary skill enables agents to discover existing cloud resources and import them into Terraform state. This is essential for brownfield adoption: taking over manually provisioned infrastructure and managing it as code. Covers resource discovery, bulk import strategies, and state file management.

### Infrastructure as Code
Terraform workflows for planning, applying, and destroying infrastructure. Module composition and versioning. State management with remote backends. Provider configuration for multi-cloud deployments. Variable management and workspace strategies.

### Packer Image Building
Machine image creation for consistent, reproducible compute environments. Build AWS AMIs, GCP images, and Azure VM images. Provision with shell, Ansible, or configuration management tools. Integrate with CI/CD pipelines for automated image pipelines.

---

## Quick Start

```bash
# 1. Install Terraform
brew install terraform

# 2. Add the Terraform skill
npx skills add hashicorp/agent-skills --skill terraform-search-import

# 3. Initialize a Terraform project
mkdir infra && cd infra
terraform init

# 4. Import existing resources
terraform import aws_instance.example i-1234567890abcdef0
```

---

## Hermes Integration Notes

- **Infrastructure as code:** Use Terraform to provision and manage all CorpusIQ cloud infrastructure declaratively
- **Brownfield adoption:** `terraform-search-import` enables Hermes to bring existing manually-created resources under version control
- **Multi-cloud consistency:** Standardize infrastructure patterns across AWS, GCP, and Azure with Terraform modules
- **Immutable infrastructure:** Packer for building golden images used by CorpusIQ worker nodes and agent runtimes

---

## Links

- **skills.sh:** https://skills.sh/hashicorp/agent-skills
- **GitHub:** https://github.com/hashicorp/agent-skills
- **Terraform Docs:** https://developer.hashicorp.com/terraform/docs
- **Packer Docs:** https://developer.hashicorp.com/packer/docs
