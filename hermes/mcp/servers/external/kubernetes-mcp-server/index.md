---
title: "Kubernetes MCP Server — Manage Clusters, Pods, Deployments"
description: "Integration guide for Manusa/kubernetes-mcp-server. MCP server for Kubernetes and OpenShift — native binary, npm, Python, or Docker. 1,814 stars."
category: mcp
tags: [mcp-server, kubernetes, devops, cloud, infrastructure, hermes-agent]
last_updated: 2026-07-16
mcp_server: Manusa/kubernetes-mcp-server
stars: 1814
source: mcpservers.org
---

# Kubernetes MCP Server — Manage K8s/OpenShift via MCP

**Repository:** [Manusa/kubernetes-mcp-server](https://github.com/Manusa/kubernetes-mcp-server)
**Stars:** 1,814 ★
**Category:** DevOps / Infrastructure
**Language:** Go
**License:** Apache 2.0
**Last Updated:** Active (July 2026)

## What It Does

A versatile Model Context Protocol server for Kubernetes and OpenShift. Distributed as a native binary, npm package, Python package, or Docker image. AI agents can interact with Kubernetes clusters — list pods, create deployments, check service status, view logs — all through MCP tools without kubectl CLI access.

### Key Capabilities

| Capability | Description |
|-----------|-------------|
| **Cluster Management** | List nodes, check cluster health, view resource utilization |
| **Pod Operations** | List pods, get pod details, view logs, exec into containers |
| **Deployment Management** | Create, update, scale, and rollback deployments |
| **Service & Ingress** | List services, check endpoints, view ingress rules |
| **Config & Secrets** | Read ConfigMaps and Secrets (read-only recommended) |
| **Namespace Operations** | List namespaces, create/delete (with guardrails) |
| **OpenShift Support** | Full OpenShift compatibility including Routes, BuildConfigs, DeploymentConfigs |

## Why Business Operators Care

- **Infrastructure visibility:** Non-technical operators can query cluster state via natural language — "how many pods are running in production?"
- **Deployment auditing:** Track what's deployed, when, and by whom without kubectl access
- **Incident response:** AI agent can surface pod failures, crash loops, and resource exhaustion before humans notice
- **Multi-cluster:** Single MCP server can connect to multiple clusters via kubeconfig contexts

## Setup for Hermes Agent

### Prerequisites

- Access to a Kubernetes cluster (kubeconfig file)
- `kubectl` or `oc` (for OpenShift) CLI authenticated

### Option 1: Native Binary (Recommended)

```bash
# Download the latest binary for your architecture
curl -L "https://github.com/Manusa/kubernetes-mcp-server/releases/latest/download/kubernetes-mcp-server-linux-arm64" -o /usr/local/bin/kubernetes-mcp-server
chmod +x /usr/local/bin/kubernetes-mcp-server

# Verify
kubernetes-mcp-server --version
```

### Option 2: Docker

```bash
docker run -d \
  -v ~/.kube/config:/root/.kube/config:ro \
  -p 8080:8080 \
  ghcr.io/manusa/kubernetes-mcp-server:latest
```

### MCP Configuration

Add to `~/.hermes/config.yaml`:

```yaml
mcp_servers:
  kubernetes:
    type: stdio
    command: kubernetes-mcp-server
    args:
      - --kubeconfig
      - ~/.kube/config
      - --read-only  # Recommended for AI agent access
    env:
      KUBECONFIG: ~/.kube/config
```

### Security Recommendations

1. **Use read-only mode** for AI agent access — prevents accidental deletion
2. **Dedicated service account** with minimal RBAC permissions
3. **Namespace isolation** — scope the kubeconfig context to non-production namespaces first
4. **Audit logging** — all MCP actions are logged; forward to SIEM if in production

## Comparison: Kubernetes MCP vs CLI vs Dashboard

| Feature | K8s MCP Server | kubectl CLI | K8s Dashboard |
|---------|---------------|-------------|---------------|
| **Access method** | MCP tools (AI-native) | Terminal commands | Web UI |
| **Natural language** | Yes — AI translates | No | No |
| **Automation** | AI agent driven | Script-driven | Manual |
| **Multi-cluster** | Single config | Switch contexts | Per-dashboard |
| **Audit trail** | MCP logs | Shell history | Dashboard logs |
| **Best for** | AI-assisted operations, incident response | DevOps engineers | Visual monitoring |

## Common Queries via Hermes

Once configured, ask Hermes:

- "Show me all failing pods in the production namespace"
- "What deployments were updated in the last 24 hours?"
- "Scale the api-gateway deployment to 5 replicas" (requires write mode)
- "Get logs from the payment-service pod for the last hour"
- "Are there any nodes running low on memory?"

## Pitfalls

1. **RBAC scope:** AI agents inherit the kubeconfig permissions. A cluster-admin kubeconfig gives the AI full cluster control — use dedicated service accounts.
2. **Rate limiting:** Large clusters with thousands of pods can produce verbose output. Use namespace and label filters.
3. **OpenShift vs vanilla K8s:** Some tools (Routes, BuildConfigs) only work on OpenShift. Check API compatibility.

---

*Discovered July 16, 2026 during mcpservers.org sitemap scan. 1,814 stars at time of discovery.*
