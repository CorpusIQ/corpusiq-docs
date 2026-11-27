---
title: "SonarQube Agent Plugins - Code Quality Skills Setup"
description: "sonarsource/sonarqube-agent-plugins - 4.2K combined installs: Sonar's agent plugins for SonarQube quality gates, issue detection, and coverage."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sonarsource-sonarqube-agent-plugins-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "sonarqube", "code quality", "security"]
---

# SonarQube Agent Plugins - Setup Guide

**Source:** [sonarsource/sonarqube-agent-plugins](https://www.skills.sh/sonarsource/sonarqube-agent-plugins) via skills.sh - 4.2K combined installs across 13 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 evening sweep)
**GitHub:** [sonarsource/sonarqube-agent-plugins](https://github.com/sonarsource/sonarqube-agent-plugins) - 118 stars, license field NOASSERTION (README states SSAL-1.0), last pushed Nov 26, 2026, master branch; 13 skills under skills/<name>/SKILL.md plus per-agent plugin bundles (.claude-plugin, .codex-plugin, .cursor-plugin, .devin-plugin, .factory-plugin, and others).
**Category:** Code Quality and Security Verification (SonarQube/SonarCloud)
**Quality Tier:** 🟠 Orange - 13 of 13 listings sampled: nine pass all three checks, two carry a single Fail each (sonar-fix-issue Gen Agent Trust Hub, sonar-onboard Snyk), and two carry a single Snyk Warn each (sonar-list-issues, sonar-list-projects).

SonarSource publishes sonarqube-agent-plugins, its official plugin suite that wires SonarQube Cloud, Server, and Community Build into the agent coding loop. SonarQube is the code quality and security verification platform, and this suite enforces its standards (7,500+ issue types, secrets scanning, agentic analysis, and quality gates across 40+ languages) at agent time rather than only in CI.

The 13 skills live under skills/<name>/SKILL.md and drive the SonarQube CLI and the SonarQube MCP Server rather than reimplementing them. Several skills are MCP-server oriented: sonar-integrate installs analysis hooks and the MCP server, and each per-agent bundle (Claude Code, Copilot CLI, Codex, Cursor, Devin, Pi, OpenCode, Antigravity, Factory Droid) carries its own manifest. On Claude Code, Copilot CLI, and Cursor the plugin also ships a sonarqube-reviewer agent that composes the skills into a single PR/diff review without editing code.

## Installation

Install is agent-specific. The canonical Claude Code path installs from Anthropic's claude-plugins-official marketplace, then runs a one-time setup:

```bash
/plugin install sonarqube@claude-plugins-official
# or, non-interactive:
claude plugin install sonarqube@claude-plugins-official
```

Authenticate once with sonar auth login (browser flow; credentials stay in the OS keychain), then wire the current agent with sonar integrate:

```bash
sonar auth login
sonar integrate claude      # MCP, hooks, secrets scanning
```

sonar integrate also supports copilot, codex, antigravity, cursor, devin, pi, and opencode. The guided /sonarqube:sonar-integrate skill walks through CLI install, login, and integration in one flow. Prerequisites are a SonarQube Cloud/Server/Community Build account, the SonarQube CLI (sonar) on the machine, and a container runtime (Docker, Podman, or Nerdctl) for the MCP server image.

## What It Provides

skills.sh publishes per-skill install counts for all 13 indexed listings. The 6 most-installed skills (100 or more installs each) are listed below; the remaining 7 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| sonar-quality-gate | 669 | show quality gate status: pass/fail and each condition, plus worst offenders |
| sonar-list-issues | 661 | search and filter issues for a project, branch, or pull request |
| sonar-fix-issue | 658 | fix a specific issue by rule key and location |
| sonar-coverage | 658 | find low-coverage files and inspect uncovered lines |
| sonar-analyze | 656 | analyze a file for quality and security issues |
| sonar-duplication | 649 | find duplicated code and inspect duplication blocks |

The remaining 7 indexed listings range from 2 to 66 installs: sonar-integrate (66), sonar-list-projects (56), sonar-dependency-risks (53), sonar-triage-dependency-risks (23), and sonar-onboard, sonar-login, and sonar-install-cli at 2 each.

## Why This Matters for Hermes Agents

SonarSource is the vendor behind SonarQube, the code quality and security verification platform, and this suite is its official entry point for agent workflows. The 13 skills map cleanly onto the agent coding loop: analyze a file, list and filter issues, fix a specific issue, check quality gate status, coverage, and duplication, then triage dependency risks. Because the plugins wire the SonarQube MCP Server and per-agent hooks, secrets scanning and, when entitled, Vortex analysis can run inside the loop after each edit instead of only in CI. The skills are thin shells over the sonarqube-cli and the MCP server, so results stay consistent with what CI reports. sonar-integrate is the on-ramp that installs the CLI, authenticates, and wires hooks plus the MCP server, while sonar-onboard links the current repository to a SonarQube project. Builders shipping agent review tooling can reuse the per-agent plugin bundles and the sonarqube-reviewer agent, which composes the skills into one composed review that never edits code itself.

## Usage

| You say | What happens |
|---|---|
| Analyze this file for issues | Uses sonar-analyze to run quality and security analysis on the file |
| Show my quality gate status | Uses sonar-quality-gate for pass/fail plus each condition and worst offenders |
| Fix issue java:S1481 in MyClass.java | Uses sonar-fix-issue to fix the issue by rule key and location |
| Check my test coverage | Uses sonar-coverage to list low-coverage files and uncovered lines |
| Find duplicate code in this project | Uses sonar-duplication to inspect duplication blocks |
| Onboard this repo to SonarQube | Uses sonar-onboard to link the repo to a project and report analysis results |
| List SonarQube issues for this PR | Uses sonar-list-issues to search and filter issues for a branch or PR |

## Verification

Confirm the README and a representative skill body resolve on the master branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/sonarsource/sonarqube-agent-plugins/master/README.md | head -60
curl -sL https://raw.githubusercontent.com/sonarsource/sonarqube-agent-plugins/master/skills/sonar-quality-gate/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Fail and Warn verdicts noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sonar-quality-gate | Pass | Pass | Pass |
| sonar-list-issues | Pass | Pass | Warn |
| sonar-fix-issue | Fail | Pass | Pass |
| sonar-coverage | Pass | Pass | Pass |
| sonar-analyze | Pass | Pass | Pass |
| sonar-duplication | Pass | Pass | Pass |
| sonar-integrate | Pass | Pass | Pass |
| sonar-list-projects | Pass | Pass | Warn |
| sonar-dependency-risks | Pass | Pass | Pass |
| sonar-triage-dependency-risks | Pass | Pass | Pass |
| sonar-onboard | Pass | Pass | Fail |
| sonar-login | Pass | Pass | Pass |
| sonar-install-cli | Pass | Pass | Pass |

Across the 13 sampled skills there are 35 Pass, 2 Warn, and 2 Fail cells. Nine skills pass all three checks; two carry a single Fail each (sonar-fix-issue Gen Agent Trust Hub, sonar-onboard Snyk) and two carry a single Snyk Warn each (sonar-list-issues, sonar-list-projects).

## Limitations

- Snapshot data, verified Nov 26, 2026: 4,155 combined installs across 13 indexed listings; 118 GitHub stars; license field NOASSERTION; last pushed Nov 26, 2026. Counts drift over time.
- The README states the code is licensed under SSAL-1.0 (LICENSE), which disagrees with the GitHub NOASSERTION field; treat it as source-available SSAL-1.0 rather than a standard permissive OSI license.
- The default branch is master, not main; keep master in any raw URL or clone, and do not rewrite it to main.
- skills.sh sampled all 13 listings; two carry a Fail cell (sonar-fix-issue, sonar-onboard), so the suite tiers Orange rather than Green.
- Several skills are MCP-server oriented: sonar-integrate installs the SonarQube MCP Server and hooks, and each per-agent bundle carries mcp.json or mcp_config.json; Vortex analysis and secrets scanning depend on SonarQube Cloud organization settings and a container runtime for the MCP server image.

## Related

[Souliane Skills - Python, Django and Codebase Review Setup](/hermes/skills/catalog/souliane-skills-setup) | [GitNexus - Code Intelligence Engine Skills Setup](/hermes/skills/catalog/abhigyanpatwari-gitnexus-setup) | [Bagelhole DevOps Security Skills Setup](/hermes/skills/catalog/bagelhole-devops-security-skills-setup) | [Warp Oz Skills - Agent Skills Collection Setup](/hermes/skills/catalog/warpdotdev-oz-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with /sonarqube:sonar-integrate for the guided CLI-install, login, and hook/MCP wiring flow.
- Prefer sonar integrate <agent> after sonar auth login for scripted, repeatable setup across agents.
- Use the sonarqube-reviewer agent on Claude Code, Copilot CLI, or Cursor for a single composed PR/diff review.
- Add sonar-project.properties in the project root with sonar.projectKey and sources so skills resolve the project key automatically.
- Re-check the security pages on skills.sh for sonar-fix-issue and sonar-onboard, which carry the sample's two Fail cells.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
