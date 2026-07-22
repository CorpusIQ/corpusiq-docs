---
title: "Hermes Traffic Guardian — Runtime Traffic Monitoring Baseline Setup"
description: "42+ installs. Hermes runtime traffic monitoring baseline for opt-in proxy inspection, egress detection, and attestation-aware traffic posture. Setup guide for Hermes agents."
---

# Hermes Traffic Guardian — Setup Guide

**Source:** [prompt-security/clawsec](https://skills.sh/prompt-security/clawsec/hermes-traffic-guardian) (42+ installs)
**Category:** Agent Infrastructure / Security & Monitoring
**Quality Tier:** 🔵 Community

A baseline specification skill from Prompt Security for Hermes runtime traffic monitoring. Provides opt-in proxy inspection, egress detection, outbound exfiltration monitoring, and attestation-aware traffic posture reporting. Currently a specification (v0.0.1-beta5) — builders implement the runtime components using the spec's safety contract.

---

## Installation

```bash
npx skills add prompt-security/clawsec --skill hermes-traffic-guardian -a hermes-agent -y
```

### Verified Installation

For security-critical deployments, verify the signed release manifest:

```bash
# Clone and verify
set -euo pipefail
SKILL_NAME="hermes-traffic-guardian"
VERSION="0.0.1-beta5"
REPO="prompt-security/clawsec"
TAG="${SKILL_NAME}-v${VERSION}"
BASE="https://github.com/${REPO}/releases/download/${TAG}"

curl -fsSL "$BASE/checksums.json" -o checksums.json
curl -fsSL "$BASE/checksums.sig" -o checksums.sig
curl -fsSL "$BASE/signing-public.pem" -o signing-public.pem
# Verify signature and checksums (see SKILL.md for full verification script)
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | For proxy runtime (when implemented) |
| **Python 3** | For detector rules and report formatting |
| **Hermes Agent** | Target agent to monitor |

---

## Key Capabilities

### Operator-Scoped HTTP Proxy Inspection
Configured per-service — no global proxy environment changes. Inspects HTTP request/response text up to a bounded byte limit.

### Outbound Exfiltration Detection
Detects patterns in outbound traffic without sending data to external services. JSONL findings with redacted snippets.

### Optional HTTPS Inspection
Per-process CA trust configuration — operator explicitly opts in. No automatic system CA installation.

### Attestation-Aware Posture Export
Exports a posture JSON file that `hermes-attestation-guardian` can include as a trust anchor. Keeps state under `HERMES_TRAFFIC_GUARDIAN_HOME` or `$HERMES_HOME/security/traffic-guardian`.

### Safety Contract (First Implementation)
- Opt-in only
- Detect-and-log by default
- No automatic system CA installation
- No global proxy environment changes
- No blocking in first implementation
- Redact secrets before logs
- All state under controlled directory

---

## Quick Start

```bash
# Install
npx skills add prompt-security/clawsec --skill hermes-traffic-guardian -a hermes-agent -y

# Builder entry points (implementation):
# lib/    — Detector rules, redaction, posture export, report formatting
# scripts/ — Start, stop, status, config validation, attestation export
# test/   — Unit tests, proxy fixture tests, redaction tests

# Read the spec
cat $(npx skills path hermes-traffic-guardian)/SPEC.md
```

---

## Verification

```bash
# Check installation
npx skills list | grep hermes-traffic-guardian

# Verify state directory
ls $HERMES_HOME/security/traffic-guardian/

# Verify posture export (after implementation)
cat $HERMES_HOME/security/traffic-guardian/posture.json
```

---

## Notes

- **v0.0.1-beta5 is a specification** — builders implement the runtime components using the spec's safety contract
- Out of scope for v0.0.1: automatic system trust-store mutation, transparent network interception, default blocking, sending traffic to external services
- Designed to complement `hermes-attestation-guardian` — traffic monitoring and attestation are separate concerns
- AGPL-3.0 licensed — be aware of copyleft implications for derivative works
- Published by Prompt Security (prompt.security) as part of the ClawSec security suite

---
