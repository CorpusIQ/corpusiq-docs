---
title: "Security Skills - Pentest and Compliance Suite"
description: "securityskills/skills: 14.5K combined installs. Twenty-one agent skills for pentest, appsec, cloud, forensics, SOC 2, PCI DSS and GDPR work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/securityskills-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "security", "pentest", "compliance", "appsec"]
---

# Security Skills - Setup Guide

**Source:** [securityskills/skills](https://www.skills.sh/securityskills/skills) via skills.sh - 14.5K combined installs across 21 indexed listings; first documented 2026-11-03 (nightly sweep)

**GitHub:** [securityskills/skills](https://github.com/securityskills/skills) - 0 stars, no licence file in the repository, branch main, last pushed 2026-08-26; 21 skill directories, each holding exactly one `SKILL.md`, nested one or two levels below a category such as `cloud-security/aws/aws-security-review`, plus a `README.md` that documents the layout, a Node content scanner in `.github/scripts/` and `audits/results.json`

**Category:** Security assessment, offensive testing methodology and compliance readiness, delivered as Markdown playbooks an agent follows

**Quality Tier:** 🟡 Yellow - all three sampled listings pass every auditor, but no licence file ships with the repository and it has 0 stars

The catalog is a single-maintainer collection of security playbooks, organised by discipline rather than by tool. Twelve category directories carry 19 of the 21 skills: pentest, bug bounty, web appsec, cloud, container, network, recon, forensics, malware analysis, compliance, secure code review and threat modeling. The remaining two sit in an agentic-security group, which the README's category list does not include. Each skill is one `SKILL.md`, between 39 and 81 lines, and the README is explicit that the file is the whole skill: there is nothing to install beyond the directory and nothing that executes.

What the files contain is procedure, not automation. `stride-threat-modeling` walks a workshop: draw the diagram, number every element, apply STRIDE per element, rank the threats, push mitigations into a backlog. `secure-code-review` replaces line-by-line skimming with trust boundary mapping and vulnerability-class checklists. `agentic-sdlc-controls` reviews a pipeline where coding agents hold write access, which is the one listing here that reads as advice for the operator as much as for the agent.

## Installation

The README gives one command:

```bash
npx skills add securityskills/skills
```

For a Hermes profile, install per skill or clone and copy. The directory name is the slug, so the category path is only for browsing:

```bash
npx skills add securityskills/skills
git clone --depth 1 https://github.com/securityskills/skills.git /tmp/sec-skills
cp -r /tmp/sec-skills/threat-modeling/stride-threat-modeling ~/.hermes/profiles/corpusiq/skills/
```

Because each skill is a lone `SKILL.md` with no `references/` tree, a single-file copy is enough here, unlike router-style suites. That also means the install is cheap and reversible: 21 directories, roughly 1,100 lines of Markdown in total, no dependency and no build step.

The category names are load-bearing for anyone editing the catalog rather than using it. The README states that category directories must match an id in `CATEGORIES` (`src/lib/skills.ts`) in the site repository, and that nesting stops two levels below a category, because a directory containing `SKILL.md` is treated as a skill and never descended into.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| stride-threat-modeling | 3,760 | Running a STRIDE workshop: diagram the system, enumerate threats per element, rank them and drive mitigations into the backlog. |
| jwt-security-review | 2,049 | Auditing JWT implementations for algorithm confusion, weak secrets, missing validation and token lifecycle flaws. |
| secure-code-review | 1,608 | Security-focused review of a PR or codebase: trust boundaries, input paths, auth flows and vulnerability-class checklists. |
| agentic-sdlc-controls | 1,151 | Reviewing a pipeline where AI agents write, commit and deploy: permission boundaries, approval gates, credential scope, non-delegable actions. |
| network-segmentation-review | 798 | Verifying segmentation designs: VLANs, firewalls, cloud security groups and zero-trust boundaries. |
| owasp-top10-analysis | 690 | Reviewing a web app against the OWASP Top 10 classes with concrete test cases per category. |
| pci-dss-scoping | 567 | Scoping a PCI DSS environment: cardholder data flows, segmentation validation and requirements mapping for v4.0 assessments. |
| attack-surface-recon | 492 | Mapping external attack surface: domains, subdomains, exposed services, leaked credentials and brand abuse. |
| ai-change-evidence | 490 | Turning agent-authored changes into audit evidence: provenance, authorization and mapping to change-management controls. |
| active-directory-attack-paths | 450 | Enumerating AD misconfigurations such as Kerberoasting, AS-REP roasting, delegation abuse and ACL attacks on authorized internal tests. |
| soc2-readiness | 413 | Preparing for a SOC 2 Type I or II audit: trust services criteria mapping, evidence collection, control implementation and remediation. |
| pentest-engagement-methodology | 285 | Running an authorized penetration test end to end: scoping, rules of engagement, recon, exploitation, post-exploitation and reporting. |
| bug-bounty-report-writing | 202 | Writing reports that triage quickly: impact statements, minimal reproduction steps and a professional tone. |
| aws-security-review | 201 | Auditing AWS for IAM privilege escalation, exposed resources, logging gaps and cross-account misconfiguration. |
| bug-bounty-recon-pipeline | 200 | Building continuous recon for bug bounty programs: subdomain enumeration, service fingerprinting and change detection. |
| incident-response-forensics | 196 | Digital forensics during response: evidence preservation, volatile data collection, artifact analysis and timeline construction. |
| ssrf-hunting | 194 | Finding SSRF in URL-fetching features, including cloud metadata bypasses and blind techniques. |
| gdpr-data-mapping | 192 | Building a GDPR data inventory: record of processing activities, lawful basis mapping, subject rights readiness and breach procedures. |
| container-image-hardening | 188 | Hardening Dockerfiles and images: multi-stage builds, non-root users, minimal base images and vulnerability gates. |
| kubernetes-security-audit | 187 | Auditing clusters for RBAC excesses, pod security gaps, network policy holes and supply-chain risk. |
| malware-triage | 183 | Triaging unknown samples safely: static indicators, sandbox execution, behaviour extraction and reporting. |

No indexed listings fall below the threshold; all 21 appear above.

The distribution is informative. The top three listings, threat modeling, JWT review and secure code review, are the three that apply to ordinary engineering work rather than to a scheduled engagement, and they carry 7,417 of the 14,496 installs between them. The offensive skills sit lower: AD attack paths at 450, SSRF at 194, malware triage at 183. If you are choosing what to install for a general-purpose agent, that ordering matches usefulness.

## Why This Matters for Hermes Agents

Most of what an agent is asked to do on a codebase has a security dimension that never gets named. A PR review that checks style and tests but not trust boundaries is a review with a hole in it, and a threat model written after the sprint is a document nobody reads. These skills give the agent a procedure to follow instead of an opinion to improvise, which is the difference between "this looks risky" and a ranked list of threats per element with the mitigations attached.

The two agentic listings are the unusual ones, and they are the reason this catalog is worth reading even if you never run a pentest. `agentic-sdlc-controls` starts from the position that an agent with write access acts with your credentials at machine speed, then asks what it can actually reach: which identity, which repositories, which environments, which secrets. `ai-change-evidence` takes the next step and frames agent-authored commits as audit evidence with provenance and authorization attached. For anyone running autonomous agents against production repositories, both are directly applicable.

The compliance skills are also a better fit for an agent than for a human. SOC 2 readiness, PCI DSS scoping and GDPR data mapping are exercises in structured enumeration against a framework, which is exactly the shape of work an agent does well and a person does slowly.

## Usage

| You say | What happens |
|---|---|
| "Threat model this new service before we start building" | Runs the STRIDE workshop: diagrams processes, data stores, flows and trust boundaries, then enumerates and ranks threats per element. |
| "Review this PR for security issues" | Applies secure-code-review: maps trust boundaries, audits input paths and auth flows, and works from vulnerability-class checklists. |
| "We use JWTs for auth, is this implementation safe?" | Loads jwt-security-review and checks algorithm handling, secret strength, claim validation and token lifecycle. |
| "Our coding agents can push to main, what should we lock down?" | Reads agentic-sdlc-controls for permission boundaries and approval gates, then ai-change-evidence for what an auditor will accept. |
| "Get us ready for a SOC 2 Type II audit" | Uses soc2-readiness for criteria mapping, evidence collection and remediation planning, with ai-change-evidence for agent-authored changes. |
| "Scope our PCI DSS v4.0 assessment" | Follows pci-dss-scoping: cardholder data flows, segmentation validation and requirement mapping. |
| "What is exposed on our external attack surface?" | Runs attack-surface-recon over domains, subdomains, exposed services and leaked credentials. |

## Verification

The raw path below returned 200 on branch main on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/securityskills/skills/main/threat-modeling/stride-threat-modeling/SKILL.md
```

After a clone, confirm the count and that the frontmatter carries the fields the README describes:

```bash
git clone --depth 1 https://github.com/securityskills/skills.git /tmp/sec-skills
find /tmp/sec-skills -name SKILL.md | wc -l
head -6 /tmp/sec-skills/threat-modeling/stride-threat-modeling/SKILL.md
head -6 /tmp/sec-skills/agentic-security/pipeline/agentic-sdlc-controls/SKILL.md
```

The count should print 21. The first header should show `name` and `description`; the second should also show `phase: harden`, one of the optional phase values the README documents. Phase is derived from the category when it is omitted, so a missing phase is normal and not a broken skill.

On the installed copy:

```bash
ls ~/.hermes/profiles/corpusiq/skills/stride-threat-modeling
grep -c '^## ' ~/.hermes/profiles/corpusiq/skills/stride-threat-modeling/SKILL.md
```

The listing should show a single `SKILL.md`, and the grep should return a handful of numbered procedure sections. If a directory arrives empty, the copy step pointed at a category folder rather than a skill folder.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| stride-threat-modeling | Pass | Pass | Pass |
| jwt-security-review | Pass | Pass | Pass |
| secure-code-review | Pass | Pass | Pass |

Nothing executes when one of these skills loads: every skill is one Markdown file, with no scripts, no hooks and no dependencies inside the skill directories. The repository does contain code, but it lives in `.github/scripts/` and runs in CI or on a contributor's machine, not in an agent that reads a skill.

That scanner is worth knowing about because it is the publisher's own answer to prompt-injection content. `local-scan.mjs` runs without a token and without network access, checking for invisible characters, embedded credentials, exfiltration-capable destinations, instruction-override phrasing and human-checkpoint bypasses. The README splits findings into errors that fail the build and warnings that do not, and says plainly that half the catalog legitimately describes the attacks the rules look for. `audits/results.json` records a scan dated 2026-08-26 naming Trivy 0.54.1, Cisco AI Defense Skill Scanner 2.0.13 and NVIDIA SkillSpector as the scanners used.

The licence gap is the practical concern. No `LICENSE` file ships, and no frontmatter in the sampled skills declares one, so default copyright applies and there is no stated grant to redistribute. Use the skills inside your own agent, and treat republishing them as something to negotiate.

Finally, read the scope language rather than skipping to the commands. The README requires scope and rules-of-engagement framing for every submission and says unframed ones are not merged, and skills such as `active-directory-attack-paths` and `pentest-engagement-methodology` are written for authorized engagements. An agent holding these should be pointed at systems you own or have written permission to test.

## Limitations

- Snapshot data, verified 2026-11-03: 14,496 combined installs across 21 indexed listings; 0 GitHub stars; no licence file; last pushed 2026-08-26. Counts drift over time.
- There is no licence file and no licence field in the sampled frontmatter, so redistribution rights are unstated rather than permissive.
- Every skill is a single page of 39 to 81 lines. These are procedures and checklists, not tooling: nothing here scans a repository, runs a scanner or produces a report file on its own.
- The offensive skills are written for authorized testing and assume the operator has scope. An agent given these without that context can produce advice that is correct in method and unusable in practice.
- The catalog is young in repo terms: 0 stars and a last push more than two months before this snapshot, so expect the methodology to be current rather than the surrounding web site.
- The repository's scan script is a content filter for CI, not a runtime guard. It says nothing about how a skill behaves once an agent loads it.

## Related

- [Bagelhole DevOps Security Skills Setup](/hermes/skills/catalog/bagelhole-devops-security-skills-setup)
- [ClawHub Skill Vetting - Security Scanner Setup](/hermes/skills/catalog/clawhub-skill-vetting-setup)
- [Strix Security Skills - Autonomous Pentesting Suite Setup](/hermes/skills/catalog/strix-security-skills-setup)
- [Supabase Pentest Skills - 24-Skill Audit Suite](/hermes/skills/catalog/supabase-pentest-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the three general-purpose skills. Threat modeling, JWT review and secure code review cover routine engineering work and carry half the install base; the offensive suite is for engagements, not for Tuesday's PR.
- Name the framework when you ask. "Scope this for PCI DSS v4.0" routes to a specific skill and a specific requirements mapping, while "check our compliance" routes nowhere useful.
- Pair `agentic-sdlc-controls` with `ai-change-evidence`. The first tells you what an agent should not be allowed to do; the second is what you show an auditor about what it did.
- Ask for the checklist, not the verdict. These skills are procedures, so "walk the STRIDE steps and show the per-element enumeration" produces a review you can audit.
- Run the repository's own scanner before you fork or extend the catalog. `node .github/scripts/local-scan.mjs .` needs no token and no network, and it catches the invisible-character and instruction-override cases that a human reviewer misses.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
