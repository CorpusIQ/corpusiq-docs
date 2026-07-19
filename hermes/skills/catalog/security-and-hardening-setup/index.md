---
title: Security Hardening for AI Agents — Full Setup Guide
description: Install and use addyosmani/agent-skills security-and-hardening. 12 hardening domains for production AI agent deployments by Addy Osmani (Google Chrome). 13,100+ installs.
---

# Security Hardening for AI Agents — Setup Guide

**Source:** [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
**Skill:** `security-and-hardening` (13,100+ installs)
**Category:** Security
**Author:** Addy Osmani (Engineering Lead, Google Chrome)

The first comprehensive security hardening guide purpose-built for AI agent threat models. Covers 12 hardening domains: prompt injection defense, tool call authorization, filesystem sandboxing, network egress controls, credential management, dependency auditing, telemetry minimization, runtime integrity verification, and more. Designed for agents with tool access — exactly the Hermes use case.

---

## Installation

```bash
npx skills add addyosmani/agent-skills@security-and-hardening
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any version with tool access (terminal, browser, file system) |
| **Shell access** | For filesystem hardening and permission audits |
| **Node.js 18+** | For dependency auditing tools (`npm audit`, `socket.dev`) |

---

## The 12 Hardening Domains

### 1. Prompt Injection Defense
Detect and neutralize injection attempts in user messages, tool outputs, and file contents. Pattern matching for common injection vectors (delimiter confusion, role manipulation, tool instruction override).

### 2. Tool Call Authorization
Allowlist/denylist for every tool available to the agent. Restrict `terminal()` to specific commands, `write_file()` to specific directories, `web_extract()` to allowed domains. Defense-in-depth: even if the agent is prompt-injected, tool access is bounded.

### 3. Filesystem Sandboxing
Confine agent filesystem access to a designated workspace. Prevent reads/writes outside project directories. Block access to `.ssh/`, `.aws/`, `.config/`, and other credential-rich paths. `chroot`-style isolation patterns for Linux/macOS agents.

### 4. Network Egress Controls
Restrict outbound network connections to known-safe domains. Block data exfiltration vectors. Allowlist for API endpoints, blocklist for suspicious destinations. Compatible with `iptables`, `pf`, and application-level proxies.

### 5. Credential Management
Never store secrets in agent-accessible files. Use environment variable injection with scope isolation. Rotate API keys after each session. Audit credential access patterns. Integrate with `1Password CLI`, `aws-vault`, and `gcloud auth`.

### 6. Dependency Auditing
Scan all skill dependencies for known vulnerabilities before installation. Run `npm audit`, `pip-audit`, and `socket.dev` on every skill repo. Maintain SBOM (Software Bill of Materials) for the agent's dependency tree.

### 7. Telemetry Minimization
Disable or minimize telemetry in all agent components. Audit what data leaves the machine. Strip PII from error reports before transmission. Configure privacy-preserving defaults for every tool.

### 8. Runtime Integrity Verification
Hash-verify the agent binary, skill files, and configuration before each session start. Detect tampering or unexpected modifications. Integrate with `shasum`, `gpg`, or TPM-based attestation.

### 9. Session Isolation
Isolate agent sessions from each other. No shared state, no cross-session credential leakage, no lingering file handles. Clean temp directories between sessions. Ephemeral filesystems where possible.

### 10. Audit Logging
Structured audit trail of every agent action: tool invoked, parameters passed, result returned, timestamp, session ID. Immutable log storage. Alert on anomalous patterns (unusual tool calls, off-hours activity, unexpected file access).

### 11. Rate Limiting & DoS Protection
Per-tool rate limiting to prevent runaway agent loops. Circuit breakers that halt the agent after N consecutive errors. Token budget enforcement — terminate session if context window approaches limits.

### 12. Recovery & Rollback
Snapshot agent state before destructive operations. Rollback capability for file modifications, database writes, and configuration changes. Automatic cleanup of failed session artifacts.

---

## Quick-Start Hardening for Hermes

### Minimal Production Hardening (10 minutes)

```bash
# 1. Install the skill
npx skills add addyosmani/agent-skills@security-and-hardening

# 2. Create a dedicated workspace
mkdir -p ~/hermes-workspace
chmod 700 ~/hermes-workspace

# 3. Audit current state
find ~/.hermes -name "*.env" -o -name "*token*" -o -name "*secret*" 2>/dev/null
find ~/.hermes -type f -perm /o+r 2>/dev/null

# 4. Set restrictive umask
echo "umask 077" >> ~/.bashrc

# 5. Verify no world-readable sensitive files
find ~/.hermes/profiles -name "*.yaml" -perm /o+r 2>/dev/null
```

### Filesystem Sandbox Configuration

Add to `~/.hermes/config.yaml`:

```yaml
security:
  filesystem:
    allowed_paths:
      - ~/hermes-workspace/
      - ~/corpusiq-docs/
      - ~/.hermes/profiles/corpusiq/
    blocked_paths:
      - ~/.ssh/
      - ~/.aws/
      - ~/.gnupg/
      - ~/.config/gh/
    read_only:
      - /etc/
      - /usr/
```

### Tool Allowlist

```yaml
security:
  tools:
    allowed:
      - terminal
      - read_file
      - write_file
      - web_search
      - web_extract
      - session_search
      - skill_view
      - memory
    blocked:
      - image_generate      # If not needed
      - text_to_speech      # If not needed
    require_confirmation:
      - terminal            # Command confirmation before execution
      - write_file          # File write confirmation
      - patch               # Edit confirmation
```

---

## CorpusIQ Use Cases

| Use Case | Hardening Domain |
|---|---|
| **Cron job agents** | Session isolation, rate limiting, audit logging — prevent runaway cron tasks from consuming resources or leaking data |
| **Multi-tenant Hermes** | Filesystem sandboxing, credential management, session isolation — prevent cross-tenant data leakage |
| **Customer-facing agents** | Prompt injection defense, tool call authorization, telemetry minimization — protect against adversarial users |
| **Growth agents (social)** | Network egress controls, rate limiting, audit logging — prevent platform bans from aggressive automation |
| **CI/CD integration** | Dependency auditing, runtime integrity verification, recovery/rollback — secure the software supply chain |

---

## Verification

```bash
# Verify skill installed
npx skills list | grep security-and-hardening

# Run the built-in audit
npx skills run security-and-hardening --audit

# Check filesystem permissions
find ~/.hermes -type f -perm /o+r -ls 2>/dev/null
# Should return nothing — no world-readable files

# Check for exposed credentials
grep -r "API_KEY\|TOKEN\|SECRET\|PASSWORD" ~/.hermes/profiles/ --include="*.yaml" 2>/dev/null
# Should return nothing — credentials should be in env vars, not config files
```

---

## Integration with ClawSec Suite

The [ClawSec security suite](/hermes/skills/marketplace/new-june30-2026-update2/) (10 skills, documented June 30) addresses security from the OpenClaw ecosystem side. `security-and-hardening` complements it with Hermes-specific hardening patterns:

| ClawSec Skill | Complementary Domain |
|---|---|
| clawsec-suite | General vulnerability scanning → filesystem sandboxing + network egress |
| soul-guardian | Identity/persona protection → prompt injection defense |
| clawsec-scanner | Active vulnerability scanning → dependency auditing |
| prompt-agent | Prompt-level security → tool call authorization |

Together they form a complete agent security posture: ClawSec for ecosystem-level threat detection, `security-and-hardening` for deployment-level hardening.

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Discovery Page](/hermes/skills/marketplace/new-july17-2026-update/) →*
*Powered by CorpusIQ*
