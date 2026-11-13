---
title: "Microsoft Security Skills - Defender and Intune Setup"
description: "vinayaklatthe/microsoft-security-skills: 6.5K combined installs across 88 listings, Microsoft security design and review guidance for agents"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/microsoft-security-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-13"
tags: ["hermes skill", "agent skill", "skill setup", "microsoft security", "defender", "entra id", "intune"]
---

# Microsoft Security Skills - Setup Guide

**Source:** [vinayaklatthe/microsoft-security-skills](https://www.skills.sh/vinayaklatthe/microsoft-security-skills) via skills.sh - 6.5K combined installs across 88 indexed listings; first seen Nov 13, 2026
**GitHub:** 180 stars, MIT license, `main` branch, last pushed 2026-10-29, 88 `SKILL.md` files under `skills/`, 254 files in total
**Category:** Microsoft security architecture, identity, compliance and SecOps guidance
**Quality Tier:** 🟢 Green - 88 indexed listings over 88 in-tree skills, an MIT licence, a per-domain README index and a push inside the last month; the only real caveat is that it is one maintainer's work.

The shape of this pack is unusual: 88 skills, one per surface, indexed by product family rather than by task. Defender, Sentinel, Entra, Purview, Intune, Priva, Azure platform security and Security Copilot each get their own files, so the agent picks a topic rather than a workflow.

The README frames the problem as a decision problem rather than a configuration problem. Which control applies here, what has to be validated before a policy goes live, which investigation path to follow, what guardrails matter in this environment. That framing is why the skills are written as decision trees with guardrails instead of as command references, and it is the reason the output is guidance rather than a change.

Everything is grounded in public Microsoft Learn documentation. The README is explicit that there is no proprietary methodology and no customer data in the pack, and the repository ships a validation harness that checks structure, links and evals. The README also claims the skills were behaviourally validated across two frontier models, with the harness in the tree.

## Installation

The README asks for Node.js 18+ on the PATH if you use the skills CLI, plus Git, and a working AI host. Clone the repository and point the agent at `skills/`, or install globally per host:

```bash
git clone https://github.com/vinayaklatthe/microsoft-security-skills.git
```

```bash
# GitHub Copilot (VS Code, Copilot CLI)
npx skills add https://github.com/vinayaklatthe/microsoft-security-skills/tree/main/skills -a github-copilot -g -y

# Claude Code
npx skills add https://github.com/vinayaklatthe/microsoft-security-skills/tree/main/skills -a claude -g -y

# Cursor
npx skills add https://github.com/vinayaklatthe/microsoft-security-skills/tree/main/skills -a cursor -g -y

# Codex CLI
npx skills add https://github.com/vinayaklatthe/microsoft-security-skills/tree/main/skills -a codex -g -y
```

The README also documents two aggregate paths: `apm install vinayaklatthe/microsoft-security-skills` for the APM harness, which its example shows installing all 88 skills into `.agents/skills/`, and `gemini extensions install https://github.com/vinayaklatthe/microsoft-security-skills` for Gemini CLI.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| threat-modelling | 234 | STRIDE threat modelling on the Microsoft SDL: walk a design and produce the threats with mitigations. |
| api-security-design | 161 | Designing secure APIs on Azure: authentication, authorization, gateway controls and input validation. |
| security-architecture | 133 | Zero Trust and the Microsoft Cybersecurity Reference Architecture applied to a target environment. |
| intune-device-mgmt | 111 | Intune device management: enrollment, configuration profiles, compliance and security baselines. |
| defender-for-endpoint | 98 | Defender for Endpoint: next-gen AV, EDR, attack surface reduction and device onboarding. |
| defender-for-apis | 98 | Defender for APIs: discovery of API estate, risk prioritisation and posture findings. |
| conditional-access-mfa | 96 | A Conditional Access baseline and MFA policy framework, with the Zero Trust policy set behind it. |
| entra-id | 93 | Entra ID: users, groups, SSO, hybrid identity and the controls around each. |
| defender-for-office-365 | 93 | Defender for Office 365: email and collaboration protection across Teams and SharePoint. |
| cloud-app-security-posture | 90 | SaaS and cloud posture management, combining Defender for Cloud CSPM with app-level hardening. |
| paw-design | 89 | Privileged Access Workstation design and the Microsoft privileged access strategy around it. |
| purview-audit | 88 | Purview Audit Standard and Premium: what is logged, how to search it, how to retain it. |
| entra-id-protection | 88 | Risk-based identity protection: risky users, risky sign-ins and the response policy behind each. |
| intune-app-protection | 86 | Intune app protection policies (MAM): keeping corporate data inside managed mobile apps. |
| entra-id-governance | 86 | Entitlement management, access packages and identity lifecycle automation. |
| defender-xdr | 86 | Unified XDR: correlating endpoint, identity, email and cloud signals in one investigation. |
| security-copilot | 85 | Security Copilot: where the generative platform fits an analyst workflow and where it does not. |
| azure-security-benchmark | 85 | The Microsoft Cloud Security Benchmark: control families, assessment and mapping to compliance. |
| azure-pim | 85 | Privileged Identity Management: just-in-time, time-bound, approval-based role activation. |
| defender-for-cloud-hardening | 85 | Defender for Cloud: Secure Score, attack path analysis and workload hardening. |

The remaining 68 indexed listings range from 44 to 84 installs.

## Why This Matters for Hermes Agents

Most security advice an agent gives is generic because the agent has no opinion about which control applies to which surface. That is exactly the gap a per-product skill closes: the model already knows what Conditional Access is, and what it does not know is which policy set a mid-size tenant should start from and what to validate first.

The guardrails are the valuable half. A skill that says "here is the policy framework, and here is what breaks if you enable it before you have excluded break-glass accounts" is worth more than a longer description of the feature, because agent failures in security work are failures of sequencing rather than of knowledge.

The coverage also matters for triage. A question that spans endpoint, identity and email lands on `defender-xdr` instead of on three partial answers, which is the difference between an investigation and a reading list.

Be clear about what this is not. These are design and review skills: they produce guidance, checklists and architecture decisions, and they never touch a tenant. That is a feature for anything customer-facing, and it keeps the install inert, but it also means the agent cannot verify a claim about your actual environment.

## Usage

| You say | What happens |
|---|---|
| "Threat model this customer portal design with STRIDE" | Runs `threat-modelling` and returns threats with SDL-aligned mitigations. |
| "Design a Conditional Access baseline for a mid-size organisation" | Runs `conditional-access-mfa` and returns a policy framework with named templates and exclusions. |
| "What Defender XDR controls should a new tenant enable first?" | Runs `defender-xdr` and sequences the controls instead of listing them. |
| "Review my Intune compliance policy for gaps" | Runs `intune-device-mgmt` and reports the missing configuration and compliance settings. |
| "Build a Purview DLP policy for financial data" | Runs `purview-dlp-policy` and returns scoped DLP guidance per workload. |
| "We think an admin account was compromised, what is the recovery order?" | Runs `compromise-recovery` and lays out containment, credential reset and validation. |
| "Which Purview feature do I actually need here?" | Runs `purview-general` and routes to the specific compliance skill. |

## Verification

Probe two skills on `main` before installing. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/vinayaklatthe/microsoft-security-skills/main/skills/threat-modelling/SKILL.md | head -8
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/vinayaklatthe/microsoft-security-skills/main/skills/sentinel/SKILL.md
```

The README's own file check is a folder count after install, expecting around 88 directories with `defender-xdr`, `entra-id`, `sentinel`, `purview-dlp-policy` and `m365-oversharing` among them:

```bash
ls .agents/skills | wc -l
```

A count of zero, or a missing `.agents/skills`, means the install did not complete. The README then suggests three behavioural checks, one per domain, starting with a Defender question for a new tenant.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-13) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| threat-modelling | Pass | Pass | Pass |
| api-security-design | Pass | Pass | Pass |
| security-architecture | Pass | Pass | Pass |
| intune-device-mgmt | Pass | Pass | Pass |
| defender-for-endpoint | - | - | - |

The other 83 indexed listings carry no verdict row yet, so this sample covers five of 88. Each of the 88 skills is a `SKILL.md` with supporting reference text, and the only executables in the tree are five `.mjs` validation scripts. The MIT licence covers the whole tree, and nothing here authenticates to a tenant or holds a credential.

## Limitations

- Snapshot data, verified 2026-11-13: 6,476 combined installs across 88 indexed listings; 180 GitHub stars; MIT license; last pushed 2026-10-29. Counts drift over time.
- These are design and review skills, not tenant operations. The agent cannot read your Secure Score, list your Conditional Access policies or check a device's compliance state.
- No MCP connector is included, so there is no path from a skill to live data. The README pairs the pack with a separate agent toolkit repository that supplies MCP servers, KQL snippets and Logic Apps templates, and you need that for anything acting on a real environment.
- Microsoft product names and portal paths move quickly. Purview in particular has been reorganised more than once, so verify a portal path against current Microsoft Learn before following it in production.
- One maintainer and a single author's reading of the portfolio. The index is thorough, but nothing in the tree is a second opinion.
- Install depth is thin across most of the pack: only 20 of 88 listings clear 85 installs, and 68 sit between 44 and 84. Low installs are not low quality here, but they do mean little independent scrutiny.

## Related

- [Ghost Security Skills - AppSec Agent Plugin Setup](/hermes/skills/catalog/ghostsecurity-skills-setup)
- [Microsoft Learn Agent Skills - Azure and .NET Docs](/hermes/skills/catalog/microsoftdocs-agent-skills-setup)
- [Auth0 Agent Skills - Identity and OAuth Setup](/hermes/skills/catalog/auth0-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask one surface at a time. A prompt that spans Defender, Entra and Purview will load three skills and produce three partial answers; the README's own routing table is the fix.
- Run `threat-modelling` before `security-architecture` on a new design. The threat list is the input the architecture skill expects to justify against.
- Ask for the guardrail, not the setting. "What breaks if I enable this" is the question these files answer best, and it is the one that prevents an outage.
- Install the whole pack rather than a subset. The skills cross-reference each other by product, and a partial install turns a routing answer into a dead end.
- Re-check a portal path against Microsoft Learn before you hand the output to anyone. The skills are grounded in Learn at the time of writing, and the portal moves.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
