---
title: "Cybersecurity Skills - 42 Audit and Pentest Skills"
description: "briiirussell/cybersecurity-skills on skills.sh: 13.3K combined installs; 42 skills for OWASP audits, pentests, forensics and compliance."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/briiirussell-cybersecurity-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "cybersecurity", "owasp audit", "penetration testing"]
---

# Cybersecurity Skills - Setup Guide

**Source:** [briiirussell/cybersecurity-skills](https://www.skills.sh/briiirussell/cybersecurity-skills) via skills.sh - 13,252 combined installs across 42 indexed listings; first seen 2026-11-08 (Nov 8, 2026 evening sweep)
**GitHub:** 513 stars, MIT via LICENSE, `main` branch, last pushed 2026-11-02, 42 SKILL.md directories at `skills/<name>/SKILL.md`
**Category:** Security
**Quality Tier:** 🟡 Beta - a Snyk Warn on one sampled skill, 513 stars, and a large catalog that is one sweep old.

This is a catalog rather than a single skill: 42 markdown instruction files that cover security work end to end, from an OWASP Top 10 source sweep and API auditing through dependency and cloud review, incident triage, forensics, detection engineering and compliance mapping for SOC 2, ISO 27001, HIPAA, PCI and GDPR. Each skill is a `SKILL.md` file with frontmatter, a workflow and references, written so an agent can run the work and explain the findings to a reader who is not a security specialist.

The parts worth knowing before install are the shared contract and the authorization posture. Most audit skills write findings to a common `findings.json` schema with a confirmed, needs validation or rejected verdict per finding, plus a coverage ledger that records what was actually read. The four offensive skills (`recon`, `osint-recon`, `web-pentest`, `red-team-engagement`) open with an authorization check and refuse ambiguous requests, which is the right default for an agent that could otherwise be pointed at any host.

## Installation

The README's recommended path is the generic skills installer, which reads the canonical `skills/` directory. List what is available first:

```bash
npx skills add briiirussell/cybersecurity-skills --list
```

Then install the whole catalog, or pick the skills you need:

```bash
npx skills add briiirussell/cybersecurity-skills
npx skills add briiirussell/cybersecurity-skills --skill owasp-audit api-audit
```

Installs land in `.agents/skills/` with a symlink into `.claude/skills/` for Claude Code. On Claude Code, the plugin marketplace route is one step:

```bash
/plugin install cybersecurity-skills --marketplace briiirussell/cybersecurity-skills
```

The plugin also ships one subagent, `finding-verifier`, which takes a single candidate finding and tries to disprove it in a fresh read-only context. Cursor and Codex do not get that subagent and follow the same steps from `verification.md` instead.

For a project-level or personal copy there is a plain `git clone` and `cp`, and the repo ships generated adapters for Cursor (`.cursor/rules/*.mdc`) and Codex. The skills themselves have no npm dependencies. The repository's own lint and build scripts do, and the test target asks for Node 21 or later.

## What It Provides

The threshold for this guide is 378 installs, so the 24 listings at or above it appear below:

| Skill | Installs | Use For |
|---|---|---|
| owasp-audit | 698 | Source-code sweep against OWASP Top 10:2025 with a coverage ledger and per-finding refutation |
| web-pentest | 628 | Authorized black-box or grey-box testing of a live web application |
| api-audit | 575 | REST, GraphQL and RPC endpoints against the OWASP API Security Top 10 |
| dependency-audit | 545 | CVE and supply-chain review of packages, runtimes and toolchain |
| secrets-audit | 531 | Leaked keys in source, Git history, build artifacts and CI |
| threat-modeling | 476 | STRIDE, attack trees and abuse cases before a feature ships |
| recon | 472 | Attack surface enumeration for authorized tests, bug bounties and CTFs |
| mobile-audit | 444 | iOS and Android apps against OWASP MASVS and MASTG |
| osint-recon | 441 | Public-source intelligence for authorized investigations |
| prompt-injection | 431 | LLM permission boundaries, indirect injection and MCP tool poisoning |
| finding-triage | 426 | One finding to a defensible disposition with ticket-ready fields |
| incident-triage | 414 | NIST SP 800-61 response while an incident is live |
| disk-forensics | 410 | Disk images, file systems and memory captures for evidence |
| privacy-engineering | 409 | GDPR, CCPA and DSAR implementation across product and infrastructure |
| crypto-audit | 409 | Algorithm choice, KDF parameters, IV and nonce handling, TLS posture |
| vuln-research | 406 | One CVE end to end: versions, reachability, public PoC, patch path |
| cloud-audit | 404 | AWS, GCP, Azure and PaaS misconfiguration, including stale deploys |
| iam-audit | 403 | Least privilege across cloud IAM, identity providers and app authorization |
| container-audit | 397 | Dockerfiles, container images and Kubernetes manifests |
| red-team-engagement | 391 | Authorized adversary emulation with rules of engagement |
| threat-hunting | 386 | Hypothesis-driven hunts across SIEM, EDR and logs |
| siem-detection | 382 | Sigma, KQL and SPL rules mapped to MITRE ATT&CK |
| security-comms | 380 | Board, customer and legal writeups of technical security work |
| breach-patterns | 378 | Public breach disclosures turned into checks for your own stack |

The remaining 18 indexed listings range from 40 to 377 installs.

The shape of the catalog matters more than any single row. The README groups the skills into seven families (appsec and supply chain, offensive and recon, detect and respond, cloud and infrastructure, AI security, design and governance, compliance and privacy) and documents the crossovers between them: `owasp-audit` hands a dependency question to `dependency-audit`, one confirmed bug goes to `variant-analysis` to find its siblings, and `finding-triage` and `security-comms` close the loop on output from every audit skill.

Two pieces of shared machinery run underneath. `findings.json` is a schema with a validator, severity calibration and coverage rules, and `shared/manifest.json` copies those reference files into each skill's `references/` directory because the installer fetches one skill folder at a time. That is why a single skill installed on its own still carries the verification guide it needs. The `examples/` directory holds real runs of five audit skills against a deliberately vulnerable app, which is the cheapest way to see the report format before running anything against your own code.

## Why This Matters for Hermes Agents

Most agent security work fails in one of two ways: the agent reports a list of plausible vulnerabilities it never verified, or it reports a clean result for code it never read. This catalog addresses both directly. Audit skills keep a coverage ledger per surface and trust boundary, and every candidate finding goes through a refutation pass before it earns a verdict. An agent working from these files produces a report with a defensible disposition per item rather than a wall of maybes.

The second fit is the authorization check. `web-pentest` asks for written authorization, current scope, credentials and out-of-scope items before touching a target, and `recon` and `red-team-engagement` carry the same posture. For a Hermes agent that can run shell commands and fetch URLs, that written gate is worth more than any amount of prompt-level caution, because it turns an ambiguous request into a question instead of a scan.

The third is that the catalog covers the operational layer Hermes already lives in. `log-watch` describes a scheduled agent that reads existing production logs, applies starter detections and pages a human, which is the same shape as a Hermes cron with a notification target. `agent-supply-chain-audit` audits the skills, plugins, MCP servers and instruction files an agent loads, including hidden instructions and unpinned servers, which is directly useful before adopting any catalog entry, this one included. `prompt-injection` covers the indirect case where a browsing agent or inbox assistant is hijacked by what it reads.

The honest counterweight: these are markdown instructions, not a scanner or a sandbox. A skill can tell an agent to be careful and to verify, and it cannot enforce either. Where deterministic coverage matters, `scanner-pipeline` wires gitleaks, semgrep, osv-scanner, trivy and checkov into CI and normalizes their output, and that is the part of this catalog that produces evidence you can diff over time.

## Usage

| You say | What happens |
|---|---|
| "Where do I start with security?" | `security-start` asks two or three questions about what you have and what is happening, then routes to one to three skills in order and audits nothing itself |
| "Run an OWASP audit on this codebase" | `owasp-audit` does recon, walks the Top 10:2025 categories with grep patterns, refutes each candidate, and writes findings plus a coverage ledger |
| "Check our API for BOLA and mass assignment" | `api-audit` tests endpoints against the OWASP API Top 10 with paired owner and non-owner evidence, then verifies before reporting |
| "A CVE just dropped, are any of our apps affected?" | `patch-sweep` maps repos to platform projects and live domains, finds each production branch, decides affectedness, mitigates, patches and confirms production |
| "Something is happening right now" | `incident-triage` declares and prioritizes, contains, preserves evidence, scopes, extracts IOCs and starts the notification clocks |
| "We have logs but no SIEM and no security staff" | `log-watch` inventories the logs you already have, sets starter detections with thresholds, and pages a human on suspicious activity |
| "I have written authorization to test our staging app" | `web-pentest` runs the authorization check first, then OWASP WSTG phases with baseline and attack evidence per proof of concept |
| "Write the board update about this incident" | `security-comms` picks the audience archetype and drafts the narrative, the risk justification and the customer-facing wording |

## Verification

The default branch is `main`, so raw paths resolve directly. This one should print the `owasp-audit` frontmatter, including its `allowed-tools` line:

```bash
curl -fsSL https://raw.githubusercontent.com/briiirussell/cybersecurity-skills/main/skills/owasp-audit/SKILL.md | head -5
```

After install, confirm the installer sees the whole catalog. The list should return 42 skill names, with `owasp-audit` and `web-pentest` among them:

```bash
npx skills add briiirussell/cybersecurity-skills --list
```

For a local check of frontmatter, size, cross-references and links, the repository ships its own linter. From a clone:

```bash
git clone https://github.com/briiirussell/cybersecurity-skills.git
cd cybersecurity-skills
node scripts/lint-skills.mjs
npm test
```

`npm test` runs the findings and coverage validators, the SARIF export and the build, and the README states it needs Node 21 or later with no dependencies. A green run means the shared schema and the skill files agree with each other.

Before trusting the catalog on a machine with credentials, run the same scanner the maintainer runs on every pull request. It is static, recursive and does not send the repo to a model:

```bash
skillspector scan https://github.com/briiirussell/cybersecurity-skills --recursive --no-llm
```

One practical acceptance test after installing `owasp-audit`: point it at a small repository with a known issue and check that the report carries a per-finding verdict and a coverage ledger. If the output is a bare list of suspicions with no verdict or coverage section, the skill did not load and the agent was improvising.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-08) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| owasp-audit | Pass | Pass | Pass |
| finding-triage | Pass | Pass | Pass |
| siem-detection | Pass | Pass | Pass |
| scanner-pipeline | Pass | Pass | Warn |
| variant-analysis | Pass | Pass | Pass |

The offensive skills (`recon`, `osint-recon`, `web-pentest`, `red-team-engagement`) require documented authorization for the target and refuse ambiguous requests; `web-pentest` will not proceed without written authorization, current scope, credentials and a documented out-of-scope list, and `red-team-engagement` carries the strongest refusal posture in the catalog.

The catalog also includes its own agent-supply-chain audit skill (`agent-supply-chain-audit`), which inventories the skills, plugins, hooks, settings, MCP servers and instruction files an agent loads and greps them for hidden instructions and exfiltration. That skill is not covered by the sampled verdicts table above, and a Warn verdict on any skill should be re-checked before production use rather than assumed to be a scanner false positive.

Two structural details belong in a security review. `allowed-tools` lists tools pre-approved to run without a prompt in Claude Code, and the README states plainly that it is not a sandbox, while the Cursor and Codex adapters carry no tool restrictions at all. And a security skill has to name things like `~/.aws/credentials` and show what an injection looks like, so the repository suppresses intentional example payloads through narrow reasoned rules in `.skillspector-baseline.yaml`; that baseline is never applied to your own scan.

## Limitations

- Snapshot data, verified 2026-11-08: 13,252 combined installs across 42 indexed listings; 513 GitHub stars; MIT license; last pushed 2026-11-02. Counts drift over time.
- The tier is Yellow because Snyk returned a Warn on `scanner-pipeline` in the sampled set, while the other four sampled skills passed all three scanners. The other 37 skills were not sampled, so the verdicts cover a small fraction of the catalog.
- 513 stars is a repository-level figure. It says nothing about how many of the 42 skills are actually used, and install counts measure installer runs rather than audits performed.
- The catalog was first documented in a single sweep on 2026-11-08, so there is no install history to show which skills are growing and which are new.
- `allowed-tools` is a pre-approval list, not a security boundary. Cursor and Codex users get no tool restrictions from the adapters.
- The offensive skills rely on the agent asking for authorization. A markdown file cannot stop someone from copying a skill body into a prompt that skips the check, so authorization discipline stays with the operator.

## Related

- [Anthropic Cybersecurity Skills Setup Guide](/hermes/skills/catalog/anthropic-cybersecurity-skills-setup)
- [CTF Security Skills - Offensive Security Suite Setup](/hermes/skills/catalog/ctf-security-skills-setup)
- [Ghost Security Skills - AppSec Agent Plugin Setup](/hermes/skills/catalog/ghostsecurity-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install one skill at a time at first. `npx skills add briiirussell/cybersecurity-skills --skill owasp-audit` keeps the trigger surface small, and each skill folder carries its own copies of the shared references.
- Ask for the coverage ledger, not just the findings. A clean audit with no ledger is a claim, while a ledger that names the files and trust boundaries read is something you can check.
- Run `security-start` when the request is vague. It is a routing skill with no audit logic of its own, and it is cheaper than installing the whole catalog into every session.
- Pair `finding-triage` with whatever produced the finding. It accepts a scanner output, an advisory or a `findings.json` record by fingerprint and returns a disposition with ticket fields, which is the difference between a backlog item and a closed one.
- Treat the offensive skills as a scope conversation. Write down the target, the window and the out-of-scope list before the first prompt, because the authorization check will ask for them anyway.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
