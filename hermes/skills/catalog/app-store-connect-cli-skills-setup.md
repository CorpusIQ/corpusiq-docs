---
title: "App Store Connect CLI Skills — Mobile Release"
description: Install the rorkai/app-store-connect-cli-skills cluster (53.5K installs, 33 skills) — release flow, submission health, metadata sync, ASO audit, TestFlight orchestration, crash triage, notarization, Apple Ads, plus a Google Play Developer cluster.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/app-store-connect-cli-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-13"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# App Store Connect CLI Skills — Setup Guide

**Source:** [rorkai/app-store-connect-cli-skills](https://www.skills.sh/rorkai/app-store-connect-cli-skills) (33 skills · 53.5K combined installs)
**Repo:** [github.com/rorkai/app-store-connect-cli-skills](https://github.com/rorkai/app-store-connect-cli-skills)
**Category:** Platform Integration / Mobile DevOps
**First Seen:** August 13, 2026
**Quality Tier:** 🟢 Production (23 `asc-*` skills at 2.2K+ installs each)

The most complete agent-facing cluster for mobile release operations observed on skills.sh. Twenty-three App Store Connect skills cover the full release lifecycle — signing, builds, metadata, screenshots, TestFlight, submission health, crash triage, notarization, ASO, and Apple Ads — and ten `gpd-*` skills mirror the same flows for Google Play Developer. This is the skill set that lets an agent run an app release end to end without opening either console.

---

## Installation

```bash
# Full cluster
npx skills add rorkai/app-store-connect-cli-skills

# Hermes: install individual skills by identifier
hermes skills install rorkai/app-store-connect-cli-skills/asc-release-flow
hermes skills install rorkai/app-store-connect-cli-skills/asc-submission-health
```

---

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| `asc-cli-usage` | 2.6K | Base CLI patterns and command reference |
| `asc-release-flow` | 2.5K | End-to-end release sequencing |
| `asc-submission-health` | 2.5K | Pre-submission checks and compliance |
| `asc-metadata-sync` | 2.5K | App metadata management and updates |
| `asc-id-resolver` | 2.4K | Resolving app/bundle/team identifiers |
| `asc-signing-setup` | 2.4K | Certificates, profiles, and signing |
| `asc-xcode-build` | 2.4K | Build automation with Xcode |
| `asc-aso-audit` | 2.4K | App Store Optimization audit |
| `asc-testflight-orchestration` | 2.3K | Beta distribution management |
| `asc-screenshot-resize` / `asc-shots-pipeline` | 2.3K | Screenshot generation pipeline |
| `asc-crash-triage` | 2.3K | Crash report analysis and triage |
| `asc-notarization` | 2.2K | macOS notarization flows |
| `asc-subscription-localization` / `asc-revenuecat-catalog-sync` | 2.3K | Subscriptions, localization, RevenueCat sync |
| `asc-whats-new-writer` | 2.3K | Release notes drafting |
| `asc-apple-ads` | 1.6K | Apple Search Ads management |
| `gpd-*` cluster (10 skills) | 1 | Google Play Developer equivalents — CLI, release flow, metadata, pricing, submission health |

---

## Prerequisites

| Requirement | Details |
|---|---|
| App Store Connect API key | Team-level API key from App Store Connect |
| Google Play service account | For the `gpd-*` skills |
| `asc` CLI | The underlying App Store Connect CLI tool |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Hermes mobile deployments** | Agent-managed TestFlight and release flows for customer apps |
| **ASO competitive tracking** | `asc-aso-audit` on competitor keyword and metadata profiles |
| **Release hygiene** | `asc-submission-health` as a pre-submit gate |
| **Screenshot automation** | `asc-shots-pipeline` for localized store screenshots |

---

## Limitations / Verification

- `gpd-*` skills at 1 install each are early — verify Google Play API behavior before production use
- Requires App Store Connect API credentials with proper role scoping
- Verify install: `npx skills list | grep asc-`

---

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Platform Integrations](/hermes/skills/catalog/)
