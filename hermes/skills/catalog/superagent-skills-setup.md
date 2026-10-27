---
title: "Superagent Security Skills - Agent Security Audit Setup"
description: "Superagent's security skills: 17.5K combined installs for skill scanning, GitHub Actions review, supply-chain risk, IDOR checks and IaC audits."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/superagent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skill setup", "security", "supply chain"]
---

# Superagent Security Skills - Setup Guide

Superagent publishes 13 documented security skills for coding agents, each in the Agent Skills format so it loads when a matching task appears. The suite covers the parts of application security an agent is normally bad at: whether a skill or dependency is safe to install, whether a GitHub Actions workflow can be hijacked, whether one tenant can read another tenant's rows, and whether the Terraform about to be applied opens a port to the internet. The README describes the rules as distilled from real security work on codebases that serve 100M+ users a week.

The design choice that matters is that most of these skills audit source code offline. They read your routes, manifests, lockfiles and workflow YAML, report the problem at `file:line` with a severity from P0 to P3, and hand back a corrected snippet, with no running app, no scanning service and often no network. Three of them ship a small dependency-free scanner in `scripts/` for the high-recall first pass and leave judgment to the model. Two others (`hacker` and `recon-security`) are instruction-only orchestration frameworks that never fire a request on their own.

**Source:** [superagent-ai/skills](https://www.skills.sh/superagent-ai/skills) via skills.sh - 17.5K combined installs across 16 indexed listings; first seen Jun 1, 2026 (Oct 26, 2026 sweep)
**GitHub:** [superagent-ai/skills](https://github.com/superagent-ai/skills) (79 stars; MIT License; branch main, pushed 2026-08-15; layout `skills/<name>/SKILL.md` for 14 skill directories, with `references/`, `scripts/` and `rules/` payloads in the skills that need them)
**Category:** Security / AppSec and Supply Chain
**Quality Tier:** 🟡 Beta - 17.5K installs across 16 listings but only 79 GitHub stars; Snyk fails ci-cd-security and warns on the other two sampled skills while Gen Agent Trust Hub and Socket pass all three; two indexed listings have no README entry and no directory; MIT License, last push 2026-08-15

## Installation

Install the whole suite, or one skill at a time:

```bash
# everything
npx skills add superagent-ai/skills

# or pick one
npx skills add superagent-ai/skills --skill skill-security -a cursor -y
npx skills add superagent-ai/skills --skill ci-cd-security -a cursor -y
```

The README's per-skill examples use `-a cursor` to select the agent target and `-y` to skip prompts. Swap `cursor` for whichever agent you install into; the skill files themselves are plain Markdown and do not depend on the target.

Prerequisites depend on the skill rather than the suite. `skill-security`, `crypto-secrets` and `infra-security` ship a pure-stdlib scanner with no `pip install` step. `repo-security-posture` collects GitHub configuration read-only, so it needs the repository access your agent already has. `redteam-autoresearch` writes runs under `.red-team/` and reads the target model key from `.red-team/.env`. `superagent` is the only skill that talks to a Superagent-hosted MCP server, and it is explicit opt-in.

There is no global CLI, no service to register and no license key for the offline auditors.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| skill-security | 8,008 | Decide whether a skill, plugin or cloned repo is safe to install: an offline scanner scores it 0 to 100, then the model checks whether the code does what the description claims |
| ci-cd-security | 7,956 | Review `.github/workflows/` for pull_request_target, workflow_run, template injection, unpinned actions, over-broad GITHUB_TOKEN permissions and cache poisoning, with P0 to P3 findings and rewrites |
| repo-security-posture | 854 | Collect a GitHub repo's branch protection, CODEOWNERS, Actions, publish integrity and collaborator access into a JSON inventory, then produce a prioritized maintainer todo list |
| security-disclosure-triage | 122 | Reporter-side check before disclosure: reproduce the construct, trace the real guard, build an exploit path, run an adversary pass, then emit TRIAGE_REPORT.md and triage-result.json |
| recon-security | 74 | Plan and run an authorized external pentest with free tools: scope and rules of engagement, passive recon, active scanning, triage, Burp or ZAP validation, reporting |
| hacker | 70 | Orchestrate an authorized offensive engagement through phase gates and role handoffs, or run its validate-findings mode to test which defensive findings are actually exploitable |
| authz-security | 68 | Find broken access control in your own source: IDOR and BOLA, missing role checks, mass assignment and multi-tenant leaks, reported at file:line with a framework-correct fix |
| vulnerability-triage | 66 | Decide whether an inbound GHSA, CVE or bug bounty report is real, by-design or noise, with an offline PoC audit and an independently scored severity |
| supply-chain-security | 66 | Review manifests and lockfiles before a dependency lands: malicious install scripts, typosquatting, dependency confusion and maintainer takeover, across npm, PyPI, Go, Cargo, RubyGems, Maven/Gradle, NuGet and Composer |
| crypto-secrets | 59 | Find hardcoded keys, tokens and PEM material plus weak crypto: bad password hashing, static IVs, hardcoded JWT secrets, disabled TLS verification |
| infra-security | 58 | Audit Terraform, Kubernetes, CloudFormation and Docker for open security groups, wildcard IAM, public storage and privileged containers, with blast-radius reasoning |

The remaining 5 indexed listings range from 1 to 45 installs: pr-github-ops at 45, redteam-autoresearch at 43, superagent at 35, offensive-security at 7 and security-suite at 1. pr-github-ops has a directory and no README entry, while offensive-security and security-suite have neither a README entry nor a directory in the current tree.

## Why This Matters for Hermes Agents

An agent that installs other skills is a supply-chain risk to itself. The first question anyone should ask before adding a new skill to a Hermes profile is whether its code does what its description says, and `skill-security` exists to answer exactly that with a deterministic scan followed by a contract check. That is the single most valuable skill in this suite for anyone running an agent with credentials in scope.

The rest of the suite covers the review work that agents are usually asked to do and usually do badly. Ask a bare model to review a GitHub Actions workflow and you get generic advice about pinning actions; `ci-cd-security` names `pull_request_target`, cache poisoning and artifact-borne injection, and returns a rewritten block. The same pattern holds for access control, dependency review and infrastructure: a fixed rule set plus a severity plus a concrete fix, which is what makes a review actionable rather than decorative.

The offline-first design is what makes these safe to run in a locked-down environment. Reading source files and reporting at `file:line` means the agent needs no network, no credentials and no running application, so an audit of a sensitive repository does not require handing the model live access. Where a skill does need reach (`repo-security-posture` reading GitHub config, `superagent` calling a remote MCP server), it says so and runs read-only or opt-in.

The two offensive skills are the ones to gate. `hacker` and `recon-security` are instruction-only: they ship no scanners or exploit runners and they require explicit written scope, falling back to planning or local-only validation when scope is missing. Even so, an agent profile holding production credentials is the wrong place to enable them casually, and the suite's own framing agrees.

## Usage

| You say | What happens |
|---|---|
| "Is this skill safe to install?" | Loads skill-security, runs the offline scanner over the folder or archive, scores it and checks the code against the claimed behaviour |
| "Review this GitHub Actions workflow" | Loads ci-cd-security, reads the YAML and reports each dangerous trigger, permission or pin with a P0 to P3 severity and a rewrite |
| "Can a user read another tenant's data through this controller?" | Loads authz-security, traces the route to the data model and reports the missing ownership check at file:line |
| "Is this dependency safe to add?" | Loads supply-chain-security, reads the manifest and lockfile diff, and checks install scripts, typosquatting and dependency confusion |
| "Audit this repo's security settings" | Loads repo-security-posture, collects a read-only inventory and returns a prioritized maintainer todo list, marking admin-gated settings as not_verified |
| "Is this advisory a real finding or by-design?" | Loads vulnerability-triage, cross-references the project's stated intent, audits the PoC without running it and scores severity independently |
| "Audit this Terraform before we apply it" | Loads infra-security, scans the `.tf` files, then assesses blast radius and cross-resource chains with corrected snippets |
| "Validate these defensive findings" | Loads hacker in validate-findings mode, which requires written scope and asks for a bounded number of cycles before it runs |

## Verification

Confirm what the skills CLI installed:

```bash
npx skills list | grep -iE "skill-security|ci-cd-security|authz-security"
```

Read the skills before installing, especially the two that ship executable scanners. The four URLs below returned 200 with `curl -s -o /dev/null -w "%{http_code}"` when checked on Oct 26, 2026:

```bash
curl -sL https://raw.githubusercontent.com/superagent-ai/skills/main/README.md
curl -sL https://raw.githubusercontent.com/superagent-ai/skills/main/skills/skill-security/SKILL.md
curl -sL https://raw.githubusercontent.com/superagent-ai/skills/main/skills/ci-cd-security/SKILL.md
curl -sL https://raw.githubusercontent.com/superagent-ai/skills/main/skills/repo-security-posture/SKILL.md
```

The directory listing behind the install index also returned 200 on the same date, and shows 14 skill directories:

```bash
curl -s https://api.github.com/repos/superagent-ai/skills/contents/skills | grep '"name"'
```

## Security

skills.sh verdicts for sampled skills (verified Oct 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| skill-security | Pass | Pass | Warn |
| ci-cd-security | Pass | Pass | Fail |
| repo-security-posture | Pass | Pass | Warn |

The suite's security surface is larger than a prompt-only skill set, and it should be read that way. `skill-security` ships `scripts/scan.py` plus a `rules/` directory of YARA signatures, `crypto-secrets` and `infra-security` each ship a stdlib `scripts/scan.py`, `repo-security-posture` ships a collector that runs against your GitHub account, and `redteam-autoresearch` ships a harness that calls a model endpoint. Those are the files to review before you enable them, because they are the ones that execute.

The credential story is reasonable. `redteam-autoresearch` keeps its target keys in `.red-team/.env` and writes runs to an isolated `.red-team/runs/<run_id>/` directory. `superagent` is the only integration that connects outward, to a Superagent MCP server, and the README states it never connects, changes configuration or spends credits without an explicit request and confirmation. Nothing else in the suite needs a key.

The verdict split is the honest caveat: Gen Agent Trust Hub and Socket pass all three sampled listings, while Snyk warns on `skill-security` and `repo-security-posture` and fails `ci-cd-security`. A Snyk failure on a skill that reviews workflows is not automatically disqualifying, and `ci-cd-security` is instruction-only prompt text, but it means the scanner disagreement has to be resolved by reading the skill rather than by trusting the badge.

## Limitations

- Snyk is the outlier. It fails ci-cd-security and warns on skill-security and repo-security-posture, while Gen Agent Trust Hub and Socket pass all three sampled listings; the other 13 listings carry no sampled verdict in this snapshot.
- Index-versus-tree drift. offensive-security (7 installs) and security-suite (1 install) have no README entry and no directory in the current tree, and pr-github-ops (45 installs) has a directory but no README entry.
- Executable payloads. Five skills ship scripts that run in your environment: three scanners over your source tree, a read-only GitHub collector and a red-team harness that calls a model endpoint; read them before use.
- Offensive skills need written scope. hacker and recon-security stay in planning or local-only validation without it, and hacker marks live checks unsafe_to_test rather than guessing.
- Rule freshness is unstated. The last push was 2026-08-15 and nothing in the repo promises a cadence for new vulnerability classes.
- Snapshot data, verified Oct 26, 2026: 17,532 combined installs across 16 indexed listings; 79 GitHub stars; MIT License; last pushed 2026-08-15. Counts drift over time.

## Related

- [Anthropic Cybersecurity Skills Setup Guide](/hermes/skills/catalog/anthropic-cybersecurity-skills-setup) - the closest official counterpart, useful as a second rule set on the same code.
- [Trailofbits Security Setup](/hermes/skills/catalog/trailofbits-security-setup) - deeper static analysis workflows once these skills have triaged the obvious findings.
- [Strix Security Skills - Autonomous Pentesting Suite Setup](/hermes/skills/catalog/strix-security-skills-setup) - dynamic testing to pair with the source-level auditors here.
- [Ghost Security Skills - AppSec Agent Plugin Setup](/hermes/skills/catalog/ghostsecurity-skills-setup) - another AppSec plugin route if you want a second opinion on the same pull requests.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `skill-security` first and use it on every other skill you add, including these. It is the only skill in the suite that audits the install decision itself.
- Ask for the severity band you care about. These skills emit P0 to P3, so "only show P0 and P1" keeps a review of a large repo readable.
- Run the scanners in CI where they support it. The two stdlib scanners are described as CI-friendly with exit codes, which is cheaper than a hosted scanner for the same high-recall pass.
- Keep `repo-security-posture` read-only. It is built to collect configuration and mark admin-gated settings as not_verified rather than to change anything, and that is the right shape for an agent.
- Leave `hacker` and `recon-security` disabled in any profile that holds production credentials. Instruction-only still means an agent that plans offensive actions.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
