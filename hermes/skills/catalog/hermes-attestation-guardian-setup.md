---
title: Hermes Attestation Guardian — Security Verification Skill Setup
description: Install and configure hermes-attestation-guardian, a security attestation skill from prompt-security/clawsec for verifying Hermes CLI, Gateway, and profile-managed deployments — 94 installs.
---

# Hermes Attestation Guardian — Setup Guide

**Source:** [prompt-security/clawsec](https://skills.sh/prompt-security/clawsec/hermes-attestation-guardian) (94 installs)
**Category:** Security / Verification
**License:** Apache 2.0 · **Platforms:** Linux, macOS, Windows
**Dependencies:** Hermes Agent (CLI/Gateway/profile-managed)

The Attestation Guardian verifies the integrity and authenticity of Hermes infrastructure components — CLI binaries, gateway deployments, and profile-managed environments. Performs release artifact verification, runtime attestation checks, and signed manifest validation.

⚠️ **Important scope:** This skill targets Hermes infrastructure only (CLI/Gateway/profile-managed deployments). Not an OpenClaw runtime hook package.

---

## What It Does

| Capability | How |
|-----------|-----|
| **Release artifact verification** | Validate signed release manifests before trusting SKILL.md, skill.json, or archives |
| **Checksum validation** | Verify `checksums.json` against the ClawSec release key |
| **SBOM inspection** | Review `skill.json` package metadata and software bill of materials |
| **Runtime attestation** | Verify running Hermes components match signed releases |
| **Trust chain verification** | Validate the signing key chain for all installed skills |

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add prompt-security/clawsec --skill hermes-attestation-guardian -a hermes-agent -y
```

### Vercel Skills CLI

```bash
npx skills add prompt-security/clawsec --skill hermes-attestation-guardian -a hermes-agent -y
```

---

## How It Works

1. **Release pipeline** signs `checksums.json` with the ClawSec release key
2. **skill.json** serves as the package metadata/SBOM source
3. **Attestation Guardian** verifies the signature chain before trusting any artifact
4. **Runtime checks** compare running components against verified release manifests

---

## Verification Commands

```bash
# Verify an installed skill's attestation
hermes attestation verify <skill-name>

# Check all installed skills for attestation status
hermes attestation list

# Verify the Hermes binary itself
hermes attestation self-check
```

---

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.16.0+ (CLI/Gateway/profile-managed) |
| ClawSec release key | Bundled with the skill |
| Internet access | For fetching release manifests |

---

## Verification

After install, test attestation:

```
Hermes, verify the attestation of all installed skills
```

The agent should check each skill's signature, report pass/fail, and flag any unverified artifacts.

---

## Pitfalls

- **Hermes-only scope:** Does NOT apply to OpenClaw deployments. The skill explicitly scopes to Hermes CLI/Gateway/profile-managed infrastructure.
- **Offline operation:** Cannot verify attestations without internet access to fetch release manifests.
- **Not a runtime monitor:** This is a point-in-time verification tool, not continuous monitoring. Run before trusting new artifacts.
- **Snyk warning:** The skill carries a SnykWarn security audit status. Review security findings before deploying in high-security environments.

---

**Installed via:** `npx skills add prompt-security/clawsec --skill hermes-attestation-guardian -a hermes-agent -y`
