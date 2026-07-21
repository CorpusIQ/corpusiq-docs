---
title: "Hermes Agent Helm Chart — Kubernetes Deployment"
description: "Deploy Hermes Agent on Kubernetes using the community Helm chart with persistence, ingress, and auto-scaling."
---

# Hermes Agent Helm Chart Setup Guide

**Repo:** [jyje/hermes-agent-helm](https://github.com/jyje/hermes-agent-helm)
**Stars:** ⭐3 | **License:** MIT

## Overview

A community-maintained Helm chart to run Hermes Agent on Kubernetes. Lightweight, configurable, and production-ready.

**Key capabilities:**
- Single-command K8s deployment
- Persistent storage for skills, memory, and sessions
- Ingress support with TLS
- Resource limits and auto-scaling

## Installation

```bash
git clone https://github.com/jyje/hermes-agent-helm.git
cd hermes-agent-helm
helm install hermes-agent . --set persistence.enabled=true --set ingress.enabled=true
```

## Pitfalls

- Community-maintained (3 stars) — verify chart before production use
- Persistent volumes required for session continuity across pod restarts
