---
title: "Jorge Alves Agent Skills - Security Setup Guide"
description: "jorgealves/agent_skills: 38 compliance and security skills for AI coding agents - 7.7K combined installs for GDPR, PII, HIPAA and code review."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/jorgealves-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "security", "compliance", "code review"]
---

# Jorge Alves Agent Skills - Security Setup Guide

**Source:** [jorgealves/agent_skills](https://www.skills.sh/jorgealves/agent_skills) via skills.sh - 7.7K combined installs across 38 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 evening sweep)
**GitHub:** [jorgealves/agent_skills](https://github.com/jorgealves/agent_skills) - 2 stars, GPL-3.0 license, main branch, last pushed Oct 27, 2026; a deliberately small library of two canonical skills under `skills/<name>/SKILL.md` plus `.codex/` subagent profiles.
**Category:** Compliance and Security
**Quality Tier:** 🟡 Yellow - sampled skills.sh verdicts are mostly Pass with Warn cells on gdpr-ccpa-privacy-auditor (Socket and Snyk) and code-review-assistant (Snyk); no Fails.

The skills.sh index for `jorgealves/agent_skills` reads as a compliance and security workbench: GDPR/CCPA privacy auditing, PII sanitizing, secret leak detection, HIPAA safeguards, prompt injection scanning, and license compliance, alongside a run of Python engineering helpers covering data pipelines, performance profiling, dependency resolution, and code review. Combined, the 38 indexed listings carry 7,669 installs, with gdpr-ccpa-privacy-auditor leading at 408.

The repository behind the source is deliberately the opposite of that index. It is a minimal, technology-agnostic Agent Skills library containing exactly two canonical skills, code-review and security-review, each with a SKILL.md, a skill.yaml, and a fixture test suite, plus two Codex subagent profiles that compose those skills. The other 36 indexed listings carry install counts but have no matching directories in the current tree, so their guidance cannot be reviewed against repository files here.

## Installation

The repository does not document a CLI installer in its README or AGENTS.md. It is listed on skills.sh, so the standard skills.sh path applies where your agent host supports that source:

```bash
npx skills add jorgealves/agent_skills
```

For hosts without skills.sh source support, clone the repository and point the agent at the two skill directories, which are the only skills in the tree:

```bash
git clone https://github.com/jorgealves/agent_skills
ls skills/    # code-review  security-review
```

Two Codex subagent profiles ship under `.codex/agents/` (code-reviewer.toml and security-reviewer.toml) and are registered in `.codex/config.toml`; each is a thin wrapper that references its skill by path instead of duplicating review logic.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| gdpr-ccpa-privacy-auditor | 408 | GDPR and CCPA privacy auditing with remediation findings |
| python-security-scanner | 315 | Python code security scanning for unsafe patterns |
| prompt-injection-scanner | 270 | scanning prompts and inputs for injection attempts |
| python-data-pipeline-designer | 258 | designing Python data pipelines and ETL structure |
| pii-sanitizer | 258 | stripping or redacting personally identifiable information |
| documentation-generator | 255 | generating code and API documentation |
| license-compliance-auditor | 243 | auditing dependencies for license compliance |
| hipaa-compliance-guard | 238 | checking health-data handling against HIPAA safeguards |
| secret-leak-detector | 230 | finding hardcoded credentials, keys and tokens |
| agent-capability-discovery | 226 | mapping what an agent and its skills can do |
| module-learning-path-generator | 222 | generating learning paths through a codebase module |
| code-review-assistant | 221 | multi-perspective review of a diff or pull request |
| python-performance-profiler | 220 | profiling Python hot paths and regressions |

The remaining 25 indexed listings range from 18 to 216 installs.

The repository tree contains exactly two skills, code-review and security-review, which are the two smallest listings in that tail (18 and 19 installs). The other 36 indexed listings carry install counts but have no matching directories in the current repository tree.

## Why This Matters for Hermes Agents

The two in-tree skills encode two high-stakes review disciplines that agents often do badly: code-review separates readability, test coverage, performance, security, documentation and best practices into independent passes with severity-ranked, evidence-based findings, and security-review applies the same discipline to PII exposure, HIPAA technical safeguards, general security posture and secret leaks. Both are read-only and local by contract, which keeps agent review from mutating code or exfiltrating the secrets it finds. The security-review skill's rule of never reproducing the secret or PII value, only its type and location, is a practice worth copying into any agent that touches credentials or personal data. Each skill ships fixture test cases with planted issues, so an agent can validate a skill's output before trusting it on real diffs. The repository's philosophy of few, broad, technology-agnostic skills over many narrow ones is also a useful sizing discipline for an agent skills library: extend an existing skill before adding a new one.

## Usage

| You say | What happens |
|---|---|
| Review this diff for readability, tests and performance | code-review runs its six perspectives and reports P0-P3 findings with file and line references |
| Audit this repo for leaked secrets and PII | security-review scans its four areas and reports only the type and location of any finding, never the secret value |
| Check this health-data pipeline against HIPAA safeguards | security-review checks encryption at rest and in transit, access controls and audit logging |
| Is this PR ready to merge? | code-review returns severity-ranked findings across readability, tests, performance, security, documentation and best practices |
| Sanity-check the code-review skill before relying on it | runs the fixture cases under skills/code-review/tests/ to validate the skill's output |

## Verification

```bash
# confirm the two skill directories landed, then review one skill before relying on it
ls skills/
curl -sL https://raw.githubusercontent.com/jorgealves/agent_skills/main/skills/code-review/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200. Each skill pairs a SKILL.md with a skill.yaml, and ships fixture cases under `skills/<name>/tests/`.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gdpr-ccpa-privacy-auditor | Pass | Warn | Warn |
| python-security-scanner | Pass | Pass | Pass |
| prompt-injection-scanner | Pass | Pass | Pass |
| python-data-pipeline-designer | Pass | Pass | Pass |
| pii-sanitizer | Pass | Pass | Pass |
| documentation-generator | Pass | Pass | Pass |
| license-compliance-auditor | Pass | Pass | Pass |
| hipaa-compliance-guard | Pass | Pass | Pass |
| secret-leak-detector | Pass | Pass | Pass |
| agent-capability-discovery | Pass | Pass | Pass |
| module-learning-path-generator | Pass | Pass | Pass |
| code-review-assistant | Pass | Pass | Warn |
| python-performance-profiler | Pass | Pass | Pass |
| skill-validator | Pass | Pass | Pass |
| python-venv-manager | Pass | Pass | Pass |
| k8s-resource-optimizer | Pass | Pass | Pass |
| pytest-optimizer | Pass | Pass | Pass |
| python-dependency-resolver | Pass | Pass | Pass |
| python-async-advisor | Pass | Pass | Pass |
| industry-standard-reviewer | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 20, 2026: 7,669 combined installs across 38 indexed listings; 2 GitHub stars; GPL-3.0 license; last pushed Oct 27, 2026. Counts drift over time.
- GPL-3.0 is a copyleft license: if you modify these skills or distribute them in a larger work, you must release your changes under GPL-3.0, so review those obligations before redistribution.
- The skills.sh index outruns the repository tree: 36 of the 38 indexed listings have no matching directories in the current tree, so only code-review and security-review can be reviewed against repository files.
- Only 20 of the 38 listings carry skills.sh verdicts; the other 18 are unverified on that platform.
- The two Warn cells (gdpr-ccpa-privacy-auditor on Socket and Snyk, and code-review-assistant on Snyk) mean those two listings deserve a re-check on skills.sh before production use.

## Related

- [Security and Hardening - Agent Security Setup](/hermes/skills/catalog/security-and-hardening-setup)
- [Anthropic Cybersecurity Skills - Security Review Setup](/hermes/skills/catalog/anthropic-cybersecurity-skills-setup)
- [Trail of Bits Security Skills - Audit Tooling Setup](/hermes/skills/catalog/trailofbits-security-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run the fixture cases under `skills/code-review/tests/` and `skills/security-review/tests/` before trusting either skill on real PRs; the repository itself flags this as a next step.
- Treat the 36 indexed listings without tree counterparts as unverifiable here; re-check their skills.sh pages individually before relying on them.
- Both in-tree skills are read-only and local by contract, so confirm your agent host honors the never-print-the-secret-value rule before running security-review on real data.
- The repository favors extending an existing skill over adding a new one, so extend code-review or security-review when a review need is not already covered.
- Since the source is GPL-3.0, check the license before forking or redistributing the skills.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
