---
title: "Microsoft Learn Agent Skills - Azure and .NET Docs"
description: "microsoftdocs/agent-skills: 39.6K combined installs. Two hundred skills built from Microsoft Learn docs, covering Azure services and architecture."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/microsoftdocs-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "azure", "microsoft learn", "cloud"]
---

# Microsoft Learn Agent Skills - Setup Guide

**Source:** [microsoftdocs/agent-skills](https://www.skills.sh/microsoftdocs/agent-skills) via skills.sh - 39.6K combined installs across 198 indexed listings; first seen 2026-11-02 (morning sweep)

**GitHub:** [MicrosoftDocs/agent-skills](https://github.com/MicrosoftDocs/agent-skills) - 804 stars, CC-BY-4.0 for the documentation content with MIT for the code (`LICENSE` and `LICENSE-CODE` both in the root), branch main, last pushed 2026-11-02; 201 `SKILL.md` directories under `skills/` holding 219 Markdown files and 5.7 MB, plus native plugin manifests in `plugin.json`, `.claude-plugin/` and `.codex-plugin/`

**Category:** Microsoft platform docs for agents: Azure services, .NET, Foundry and Copilot extensibility as installable skills

**Quality Tier:** 🟢 Green - all five sampled verdicts pass Gen Agent Trust Hub, Socket and Snyk, the repository is maintained by Microsoft's docs team under a stated dual licence, and it ships first-party plugin manifests for VS Code, Claude Code and Codex

This is Microsoft's own documentation pipeline turned into agent skills. Each directory under `skills/` holds a single `SKILL.md` for one Azure service or platform area, pre-compiled from Microsoft Learn rather than retrieved at question time: the skill carries a category index with line ranges (Troubleshooting, Best Practices, Decision Making, Architecture and Design Patterns, Limits and Quotas, Security, Configuration, Integrations and Coding Patterns, Deployment) and a table of curated Learn links under each heading. An agent reads the category index, picks the slice it needs and fetches the linked page when it needs the full text.

The generated frontmatter is where the routing lives. Every description states the scope, the concrete triggers ("configuring ACA auth/networking, workload profiles/GPUs, CI/CD deployments, KEDA/Dapr scaling") and, in most cases, an explicit negative list: the Container Apps skill says not for App Service, use azure-app-service; not for Functions, use azure-functions. Across 198 listings that turns the install index into a router for Azure questions, which is a different job from a documentation dump. Metadata records the provenance too: `generator: docs2skills/1.0.0` and `generated_at: 2026-11-01`.

The repository also ships as a plugin: `plugin.json` for VS Code and the Copilot CLI, `.claude-plugin/` for Claude Code, `.codex-plugin/` and `.agents/plugins/` for Codex, all pointing at the same `./skills/` directory. The README puts the count at "193+ skills" and the tree currently holds 201 directories against 198 indexed listings, so treat any single figure as a snapshot of one of the three counts.

## Installation

The README recommends the plugin route, and documents one command pair per host. Claude Code:

```text
/plugin marketplace add MicrosoftDocs/agent-skills
/plugin install azure-agent-skills@microsoft-agent-skills
```

Codex CLI:

```bash
codex plugin marketplace add MicrosoftDocs/agent-skills
```

Then install **azure-agent-skills** from `/plugins`. In VS Code the route is the Command Palette: run **Chat: Install Plugin From Source** and paste `https://github.com/MicrosoftDocs/agent-skills`, or add `"MicrosoftDocs/agent-skills"` to `chat.plugins.marketplaces` and install it from the Extensions view under `@agentPlugins`. The plugin route needs the agent plugins preview enabled (`chat.plugins.enabled`), which an organisation may manage.

The manual route works everywhere and is the one to use for a Hermes profile, since nothing in the repository mentions Hermes:

```bash
git clone https://github.com/MicrosoftDocs/agent-skills.git
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -r agent-skills/skills/* ~/.hermes/profiles/corpusiq/skills/
```

Copy the folders inside `skills/`, not the `skills` directory itself. The README calls this out with the exact failure it produces: `.copilot/skills/azure-functions/SKILL.md` is right, `.copilot/skills/skills/azure-functions/SKILL.md` is wrong. Its own destination table maps the same copy to `.github/skills/` for Copilot, `.claude/skills/` for Claude Code, `.cursor/skills/` and `.gemini/skills/` for those editors, and `~/.copilot/skills/` or `~/.claude/skills/` for a user-wide install.

There is no `npx skills add` line in the README, and no APM manifest: the plugin manifests and the copy route are the two documented paths. Update by running `git -C agent-skills pull` and copying again, or by reinstalling the plugin, which the README says brings updates with it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| azure-container-apps | 1,296 | Container Apps: auth and networking, workload profiles and GPUs, CI/CD deployments, KEDA and Dapr scaling, Java microservices, limits, quotas, troubleshooting. |
| azure-sql-database | 1,294 | SQL Database: DTU, vCore and serverless tiers, Hyperscale, geo-replication, Data Sync, backups, CI/CD. |
| azure-well-architected | 651 | Well-Architected design reviews: checklists, recommendations, design principles, tradeoffs, service guides, workload patterns, assessment questions. |
| azure-pipelines | 446 | YAML pipelines: agents and triggers, GitHub-hosted agents, classic-to-YAML migration, Kubernetes and VM deployments. |
| azure-architecture | 423 | Solution design: reference architectures, design patterns, technology choices, architecture styles, anti-patterns, migration guides, RAG and gen AI workloads. |
| azure-devops | 416 | Azure DevOps: org and project management, repos, pipelines, work items, dashboards and analytics, server deployments. |
| azure-functions | 391 | Functions: HTTP, storage and queue bindings, VNet and managed identity security, host.json tuning, CI/CD deployment. |
| azure-monitor | 362 | Monitoring: AMA and Log Analytics, data collection rules, alerts, Application Insights, autoscale, Workbooks, container and AKS monitoring. |
| azure-blob-storage | 335 | Blob storage: tiers and cost planning, lifecycle and immutability policies, SAS and RBAC, NFS and SFTP, BlobFuse. |
| azure-key-vault | 321 | Key Vault: secrets and keys, Private Link, Entra ID auth, BYOK and HSM, ARM, Bicep and Terraform deployments. |
| azure-app-service | 316 | App Service: plans and ASEs, deployment slots, VNet and private endpoints, managed identity auth, CI/CD. |
| azure-security | 308 | Azure security: antimalware, container SBOM and signing, CMK encryption, AKS and VM hardening, Key Vault keys. |
| azure-rbac | 295 | Role-based access control: role design, ABAC conditions, PIM workflows, deny assignments, ARM and Bicep role automation. |
| azure-repos | 291 | Repos: Git and TFVC, branch policies and PR checks, CodeQL and secret scanning, ELM sync, TFVC to Git migration. |
| azure-networking | 283 | Networking: VNets and Virtual WAN, load balancers, firewalls and WAF, DDoS protection, Virtual Network Manager policies. |
| azure-cosmos-db | 270 | Cosmos DB: SQL, Mongo, Cassandra, Table and PostgreSQL APIs, change feed, multi-region HA, vector search. |
| microsoft-foundry | 264 | Foundry agents: Entra auth, Azure Policy, vector stores, VNet isolation, azd and GitHub CI/CD. |
| azure-database-postgresql | 248 | PostgreSQL Flexible Server: pgvector and AI search, Private Link and TLS, replicas and HA, point-in-time restore. |
| azure-container-registry | 245 | Container Registry: ACR Tasks, geo-replication, connected registries, image signing, Kubernetes and ACI integration. |
| azure-speech | 243 | Speech: speech to text and text to speech, custom voices and avatars, Speech containers, Voice Live, telephony and agent integration. |
| azure-logic-apps | 243 | Logic Apps: Azure and OpenAI connectors, SAP and B2B, private endpoints, DevOps deployment, disaster recovery and multi-region design. |

The remaining 177 indexed listings range from 64 to 242 installs, from azure-kubernetes-service, azure-data-factory and azure-boards at the top of that band down to azure-documentdb, azure-application-network and azure-enclave at 64; they carry the long tail of individual services, from Batch and Bastion to Quantum and CycleCloud.

## Why This Matters for Hermes Agents

Microsoft's platform changes weekly, and an agent answering from training data is wrong in a specific and expensive way: quotas that moved, tiers that were renamed, a feature that is now generally available in one region and not another. This repository attacks that directly. The skills are regenerated from Learn documentation, and each `SKILL.md` carries a `generated_at` date in its metadata, so the age of the guidance is visible in the file rather than assumed.

The category index is the part worth understanding before installing. Each skill opens with a table mapping its documentation categories to line ranges in the same file, so an agent can load the skill and then read the six lines that cover quotas instead of the whole document. That is progressive disclosure inside a single file, and it suits a Hermes run with a small context budget better than a monolithic service guide.

The negative routing is unusually disciplined. Most descriptions end with a list of near neighbours and the skill to use instead, which is exactly the failure mode an agent has with cloud services: Container Apps answers where App Service was meant, or Azure SQL answers where Cosmos DB was meant. When the descriptions are loaded, the agent has the disambiguation in front of it before it starts reasoning.

There is also an operational caveat built in. Each skill opens with an instruction to the agent: if `metadata.generated_at` is more than three months old, suggest pulling the latest version, and if the `mcp_microsoftdocs` tools are missing, suggest installing the MCP server. That is a skill telling the agent how to notice its own staleness, which is rare and useful.

For a builder working in Azure, the practical result is a small set of skills that answer configuration questions with a link to the exact Learn page. `docs/BUNDLES.md` groups them by role for that reason: a Quick Start bundle for seven core services, then Popular, Core, AI and ML, Data Engineer, Infrastructure Pro, Security and Compliance, DevOps and Automation, Integration, and a Full-Stack Azure bundle.

## Usage

| You say | What happens |
|---|---|
| "How do I configure blue-green deployments in Azure Container Apps?" | azure-container-apps answers from its Best Practices and Deployment categories, with the Learn links that cover revisions and traffic splitting. |
| "Should this workload use Cosmos DB or Azure SQL?" | azure-cosmos-db and azure-sql-database carry the decision-making categories, and each description names the other, so the comparison is grounded rather than guessed. |
| "What are the current limits on PostgreSQL Flexible Server storage" | azure-database-postgresql points at the Limits and Quotas slice and the Learn page behind it instead of quoting a remembered number. |
| "Write a YAML pipeline that deploys this Bicep file" | azure-pipelines covers triggers, agents, environments and the deployment steps, plus the classic-to-YAML migration guidance. |
| "Review this architecture against the Well-Architected Framework" | azure-well-architected answers with the design review checklist, the assessment questions and the tradeoffs per pillar. |
| "Which role do I assign so this identity can read the key vault" | azure-rbac covers role design, ABAC conditions and the ARM or Bicep form of the assignment. |
| "Set up monitoring and alerts for this AKS cluster" | azure-monitor covers data collection rules, Application Insights, container monitoring and autoscale signals. |

## Verification

The raw paths below returned 200 on branch main when this guide was written on 2026-11-02:

```bash
for p in azure-container-apps azure-sql-database azure-well-architected; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/MicrosoftDocs/agent-skills/main/skills/$p/SKILL.md"
done
```

After a clone, check the count and the two things that decide whether a skill will work at runtime, the freshness metadata and the fetch tool it expects:

```bash
git clone --depth 1 https://github.com/MicrosoftDocs/agent-skills.git /tmp/agent-skills
find /tmp/agent-skills/skills -name SKILL.md | wc -l
sed -n '1,12p' /tmp/agent-skills/skills/azure-container-apps/SKILL.md
grep -m2 mcp_microsoftdocs /tmp/agent-skills/skills/azure-container-apps/SKILL.md
```

The count should print 201. The frontmatter should show `metadata.generated_at` and `generator: docs2skills/1.0.0`, and the `grep` should return the `mcp_microsoftdocs:microsoft_docs_fetch` line the skill uses for network access. If a copied profile shows more skills than expected, compare `ls ~/.hermes/profiles/corpusiq/skills | wc -l` with the 201 directories here, since a copy of the `skills` directory itself produces one nested level that never routes.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| azure-container-apps | Pass | Pass | Pass |
| azure-defender-for-cloud | Pass | Pass | Pass |
| azure-traffic-manager | Pass | Pass | Pass |
| azure-health-bot | Pass | Pass | Pass |
| azure-application-network | Pass | Pass | Pass |

All five sampled listings pass all three scanners, and none of the sampled skills carries a Warn or a Fail. The repository is Markdown and manifests: 219 Markdown files under `skills/`, plugin JSON at the root and in three manifest directories, and no script that runs on install. The licence is stated twice, CC-BY-4.0 for the documentation content and MIT for the code, so the reuse terms are explicit rather than implied.

The runtime behaviour is the part to think about. These skills do not carry the documentation, they carry links to it plus an instruction to fetch, preferring `mcp_microsoftdocs:microsoft_docs_fetch` and falling back to `fetch_webpage`. That means every answer of substance pulls remote text into the agent's context. The content comes from Microsoft Learn over HTTPS, which is a reasonable trust anchor, but the pattern is worth naming: an unattended run will make outbound requests to `learn.microsoft.com` and will act on what comes back.

The plugin route installs a larger surface at once than the copy route makes obvious. One install adds 201 skills to the assistant's index, and every one of them is a candidate trigger for a question that mentions Azure. If the profile is shared, scope the copy to the services you actually run rather than the full tree.

Attribution is an obligation, not a courtesy, for the CC-BY-4.0 half. Quoting or redistributing the skill text in a product needs attribution to Microsoft.

## Limitations

- Snapshot data, verified 2026-11-02: 39,644 combined installs across 198 indexed listings; 804 GitHub stars; CC-BY-4.0 content with MIT code; last pushed 2026-11-02. Counts drift over time.
- Three different counts describe the same repository: the README says "193+ skills", the install index carries 198 listings, and the tree holds 201 directories. `azure-anomaly-detector` is indexed but has no skill directory, only a crawl CSV and a report under `products/`; `azure-anyscale-on-azure`, `azure-connector-namespace`, `azure-horizondb` and `azure-nutanix` are directories with no install count.
- The skills are thin by design. Each one is a single `SKILL.md` of curated Learn links with line-range categories, not a self-contained guide, and it degrades to a list of URLs when the network or the MCP server is unavailable.
- The content is a crawl snapshot. `metadata.generated_at` is 2026-11-01 for the sampled skill and the skills themselves tell the agent to flag anything older than three months, so a copied install silently ages unless it is refreshed.
- The security sample is five skills out of 201. All five pass, but 196 remain unaudited by that sample.
- Installing the full set adds 201 skill directories and 5.7 MB of Markdown to a profile, which is a lot of trigger surface for a project that uses three Azure services.

## Related

- [Microsoft Learn MCP Skills Setup](/hermes/skills/catalog/microsoft-learn-mcp-skills-setup)
- [Dotnet Skills - .NET AI Coding Setup](/hermes/skills/catalog/dotnet-skills-setup)
- [Aaronontheweb Dotnet Skills - Akka.NET Suite](/hermes/skills/catalog/aaronontheweb-dotnet-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Pair the pack with the Microsoft Learn MCP server. The skills are link tables, and the fetch tool is what turns a link into an answer; without it the agent has a reading list and no library.
- Start from `docs/BUNDLES.md` instead of the full tree. A role bundle is seven to twenty skills, which keeps the trigger surface small and the answers relevant.
- Ask the agent to read the category index line ranges before the body. That table is why the skill can answer a quotas question without loading nine categories of documentation.
- Use the negative routing deliberately. Asking "which skill covers this, and which one covers the near neighbour" surfaces the App Service versus Container Apps distinction that the descriptions already encode.
- Check `metadata.generated_at` before trusting a limit. The skills carry the date, and a stale date is the one warning the agent is instructed to raise itself.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
