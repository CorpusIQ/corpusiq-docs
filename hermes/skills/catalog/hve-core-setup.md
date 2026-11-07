---
title: "HVE Core - Microsoft Agentic SDLC Framework"
description: "microsoft/hve-core on skills.sh: 5.8K combined installs across 107 listings; Microsoft's Copilot-first agentic SDLC framework with OWASP packs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hve-core-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "microsoft", "agentic sdlc", "security"]
---

# HVE Core - Setup Guide

**Source:** [microsoft/hve-core](https://www.skills.sh/microsoft/hve-core) via skills.sh - 5.8K combined installs across 107 indexed listings; first seen 2026-11-07 (Nov 7, 2026 morning sweep)
**GitHub:** 1,606 stars, MIT, branch `main`, last pushed 2026-11-06, 93 `SKILL.md` directories under `.github/skills/<group>/<name>/`, with `plugin.json` and a `.mcp.json.sample` at the repository root
**Category:** Agentic SDLC for agents: context management, artefact authoring, code review, data science and MLOps instruction packs
**Quality Tier:** 🟡 Yellow - every sampled skill passes the three scanners, but 107 indexed listings run ahead of 93 in-tree skill directories and the repository describes itself as a fast-moving source of patterns rather than a stable dependency.

HVE Core is Microsoft's Hypervelocity Engineering framework: a deliberately opinionated agentic software development lifecycle that pushes engineering patterns into the workflow itself. The README states the principle it is built on: "AI carries the rules, humans keep the judgment." It claims roughly 80 standards, plus security requirements, compliance processes, architecture reviews and organisational practices, are brought into engineering work through the artefacts.

Skills are one of three artefact types here, alongside agents and instructions. They are grouped by discipline under `.github/skills/`: `security`, `project-planning`, `data-science-engineering`, `design-thinking`, `rpi` (research, plan, implement, review), `hve-core`, `coding-standards`, `accessibility`, `engagement-reporting`, `shared` and `experimental`. Each skill is a `SKILL.md` plus whatever `references/` it needs, and the OWASP packs are one markdown file per risk.

The index runs ahead of the tree. skills.sh lists 107 indexed listings while the current repository holds 93 `SKILL.md` directories, so a few listings have no counterpart on disk. `powerpoint`, at 450 installs, is the clearest example: there is no `powerpoint` directory anywhere in the tree, so its behaviour cannot be checked from the source.

## Installation

The project targets GitHub Copilot, and its install guide is explicit: HVE Core "supports only the Copilot harness". The documented routes are therefore Copilot plugin routes. In GitHub Copilot CLI, verbatim from the README:

```bash
copilot plugin marketplace add microsoft/hve-core
copilot plugin install hve-core@hve-core
```

In VS Code, run **Chat: Open Customizations**, select **Browse**, add the `microsoft/hve-core` marketplace through **Configure Marketplaces**, and install `hve-core`. There is also a [VS Code Marketplace extension](https://marketplace.visualstudio.com/items?itemName=ise-hve-essentials.hve-core), which the README says delivers the agents and skills but may not reach Copilot sessions and carries no canvases. Use one route at a time, because installing two makes every agent appear twice.

There is no `npx skills` command and no Hermes-specific installer in the README, so on any other harness the route is to copy the skill directories you want into the directory your agent scans. Copy the whole folder whenever the skill ships `references/` beside its `SKILL.md`:

```bash
git clone https://github.com/microsoft/hve-core.git
mkdir -p .agents/skills
cp -r hve-core/.github/skills/security/owasp-top-10 .agents/skills/
```

Repeat per skill, for example `.github/skills/security/owasp-llm` or `.github/skills/project-planning/adr-author`. The repository ships its own install helper as a skill: `hve-core-installer` (74 installs), described as a "decision-driven HVE-Core installer for the Copilot harness". It is not a cross-harness installer, so it does not replace the copy step above on Hermes.

## What It Provides

Security dominates the top of the install distribution: eight of the nine listings at or above 100 installs are OWASP or secure-design packs.

| Skill | Installs | Use For |
|---|---|---|
| owasp-top-10 | 1,092 | OWASP Top 10 for web applications (2025): identifying, assessing and remediating web application risk |
| secure-by-design | 718 | Secure by Design principles for assessing security-first design, development and deployment across the lifecycle |
| powerpoint | 450 | Deck listing with no matching directory in the current skills tree, so its behaviour cannot be verified from the repository |
| owasp-docker | 167 | OWASP Docker Top 6 knowledge base for identifying, assessing and remediating container security risk |
| owasp-cicd | 164 | OWASP CI/CD Top 10 knowledge base for CI/CD pipeline security risk |
| owasp-infrastructure | 143 | OWASP Infrastructure Top 10 knowledge base for internal IT infrastructure security risk |
| owasp-agentic | 123 | OWASP Agentic Security Top 10 for AI agent system risk, from goal hijack and tool misuse to memory poisoning and rogue agents |
| owasp-llm | 114 | OWASP Top 10 for LLM Applications (2025): large language model security risk |
| owasp-mcp | 108 | OWASP MCP Top 10 knowledge base for Model Context Protocol security risk |

The remaining 98 indexed listings range from 1 to 81 installs.

What sits behind those rows matters more than the counts. Each OWASP skill carries a `references/` folder with a numbered vulnerability index and one markdown file per risk; `owasp-agentic` ships an index plus ten files, covering goal hijack, tool misuse and exploitation, identity and privilege abuse, agentic supply chain vulnerabilities, unexpected code execution, memory and context poisoning, insecure inter-agent communication, cascading failures, human-agent trust exploitation and rogue agents. The entry file for `owasp-top-10` sets `user-invocable: false`, so the pack is context that other workflows load rather than a slash command you call yourself.

The long tail is where the breadth lives. `code-review` (37) reviews changes from multiple perspectives with depth-tier rigor and structured findings. `jira` (81) and `gitlab` (70) cover tracker and repository work. The `data-science-engineering` group covers experimentation, data catalogs, dataops and notebook authoring. The `design-thinking` group covers workshop methods and UX artefacts, and the `rpi-*` skills cover the research, plan, implement and review loop.

## Why This Matters for Hermes Agents

A Hermes agent asked to review a service for security issues falls back on whatever the model remembers about OWASP. These skills replace that with a file per risk, so the agent can cite the category it is applying instead of gesturing at a checklist. That is the difference between "this looks risky" and "this is A03 injection, and here is the reference".

The second gain is cross-discipline coverage in one clone. Security, project planning, data science and accessibility artefacts share one convention: `SKILL.md` at the top, references underneath, frontmatter that says when to load the file. An agent that already understands the Agent Skills layout can use all of them without new plumbing.

The third is that the framework encodes process, not only knowledge. The RPI group splits research, plan, implement and review into separate skills, and the planning group carries an outcome hypothesis, a feasibility check and a functional planner. That order is exactly what agents skip when they start editing files too early.

The fourth is portability of the parts. Every skill is self-contained markdown, so a Hermes setup can take the seven OWASP packs and skip the Copilot-specific agents and instructions entirely. The repository is MIT overall, with the OWASP-derived skills carrying their own licence text in frontmatter.

## Usage

| You say | What happens |
|---|---|
| "Review this Flask app against the OWASP Top 10" | The agent loads `owasp-top-10`, walks the reference files, and returns findings mapped to categories with remediation per item |
| "Is this agent design vulnerable to prompt injection through tool output?" | `owasp-agentic` supplies the goal hijack, tool misuse and memory poisoning references, and the agent maps each to the design |
| "Threat model our CI pipeline" | `owasp-cicd` covers flow control, identity and access, dependency chain abuse and the rest of the CI/CD Top 10 |
| "We are deploying in containers, what should we fix first?" | `owasp-docker` lists the container risks; the agent ranks them against what it sees in the Dockerfile and compose file |
| "Review this change before I open the PR" | `code-review` runs the multi-perspective pass with structured findings, then `pull-request` and `pr-reference` shape the description |
| "Write an ADR for choosing Postgres over DynamoDB" | `adr-author` supplies the decision-record structure; `architecture-review` can then critique the result |
| "Plan the next sprint from this backlog" | `backlog-plan`, `backlog-management` and `backlog-execute` take the request through planning and execution in the repo's own format |

## Verification

Read a skill before you copy it. These two paths returned HTTP 200 on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/microsoft/hve-core/main/.github/skills/security/owasp-top-10/SKILL.md | head -25
curl -fsSL https://raw.githubusercontent.com/microsoft/hve-core/main/.github/skills/security/secure-by-design/SKILL.md | head -25
```

Each should open with frontmatter whose `description` starts "OWASP Top 10 for Web Applications (2025) knowledge base" or "Secure by Design principles knowledge base", followed by a numbered list of reference files.

Confirm the references landed after copying, because a `SKILL.md` without its `references/` folder is an index of files that do not exist:

```bash
find .agents/skills/owasp-top-10 -name '*.md' | wc -l
```

The count should be above one. If it is 1, only the entry file came across.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| owasp-top-10 | Pass | Pass | Pass |
| telemetry-foundations | Pass | Pass | Pass |
| mcsb | Pass | Pass | Pass |
| architecture-review | Pass | Pass | Pass |
| openvex-spec | Pass | Pass | Warn |

The security surface of the packs sampled here is markdown: the OWASP skill directories contain `SKILL.md` plus reference pages and no scripts at all, which is the cheapest kind of skill to audit. That does not hold for the whole repository. The `experimental` group ships executable helpers, for example `hve-slides/scripts/*.mjs` and the Python tests under `hve-demo-material`, so review those folders before copying them into an agent's workspace.

Two other facts belong here. The licence is MIT with a LICENSE file in the root, but the README states that skill content derived from OWASP Foundation publications is licensed CC BY-SA 4.0 and identifies itself in frontmatter, which matters if you redistribute. And the skills describe security practice; they do not enforce it. Nothing in the copy runs a scanner, so a "Pass" verdict covers the skill files, not your application.

## Limitations

- Snapshot data, verified 2026-11-07: 5,822 combined installs across 107 indexed listings; 1,606 GitHub stars; MIT; last pushed 2026-11-06. Counts drift over time.
- The index outruns the tree: 107 indexed listings against 93 `SKILL.md` directories, and `powerpoint` at 450 installs has no directory in the current tree.
- Copilot only. The install guide states HVE Core "supports only the Copilot harness", so plugin install commands and the VS Code extension do nothing for a Hermes agent; the copy route is the only portable path.
- Licence is split. MIT covers the repository, while OWASP-derived skill content is CC BY-SA 4.0 with attribution sections, so redistribution needs the per-skill licence read first.
- `openvex-spec` drew a Snyk Warn in the sampled set (1 of 5). No Fail verdicts appear in the sample, but the sample is five skills out of 107 listings.
- The README calls the framework rapidly evolving and says it is best treated as a source of patterns rather than a stable platform or production dependency, with breaking changes expected.

## Related

- [Microsoft Azure AI Foundry Skills - Enterprise Agent](/hermes/skills/catalog/microsoft-azure-skills-setup)
- [MLflow Skills - Tracing, Evaluation and LLMOps](/hermes/skills/catalog/mlflow-skills-setup)
- [AI Evals Skills - Product-Specific Evaluations](/hermes/skills/catalog/ai-evals-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with one pack, not the framework. Copy `owasp-top-10`, run a real review, and only then decide whether the planning and RPI groups earn their context cost.
- Ask for the reference file in the answer. "Cite which reference file each finding comes from" turns the skill from a vibe check into an auditable list.
- Prefer the security group for Hermes. It is plain markdown with no scripts and no Copilot-specific frontmatter, so it survives the copy route unchanged.
- Keep the whole folder. `references/` is the product; a lone `SKILL.md` names files the agent will then fail to open.
- Do not stack install routes on a Copilot machine. The install guide warns that plugin plus extension, or plugin plus a declared clone, lists every agent twice.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
