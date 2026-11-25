---
title: "MuleSoft DX Skills - Anypoint Integration Setup"
description: "mulesoft/mulesoft-dx - 8.7K combined installs across 56 listings: MuleSoft Anypoint agent skills for Mule development, PDK policies and security."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mulesoft-dx-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "mulesoft", "anypoint", "integration"]
---

# MuleSoft DX Skills - Anypoint Integration Setup

**Source:** [mulesoft/mulesoft-dx](https://www.skills.sh/mulesoft/mulesoft-dx) via skills.sh - 8.7K combined installs across 56 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 evening sweep)
**GitHub:** [mulesoft/mulesoft-dx](https://github.com/mulesoft/mulesoft-dx) - 16 stars, Apache-2.0 license, master branch, last pushed Nov 24, 2026; skills live under skills/ (mule-development, omni-gateway, and portal and security groups) and a smaller .claude/skills/ set.
**Category:** Enterprise Integration Skills (MuleSoft Anypoint Platform)
**Quality Tier:** 🟠 Orange - secure-mule-app and generate-bat-tests each fail Snyk; the other 13 sampled skills pass or carry only Warn cells.

mulesoft/mulesoft-dx is MuleSoft's Anypoint Platform developer-experience repository, self-described as the single source of truth for all public Anypoint Platform API specifications. Alongside the OpenAPI specs it ships a large skills tree covering Mule application development, Anypoint governance and security, the Flex Gateway Policy Development Kit (PDK), and the Omni Gateway. skills.sh indexes 56 listings at 8.7K combined installs.

The skills are grouped under skills/ (mule-development, omni-gateway, and portal and security skills) plus a smaller .claude/skills/ set (api-spec-validator, jtbd-generator, jtbd-validator, api-doc-generator, api-schema-inferrer, review-pr, skill-quality-review and validate-imperative-format). The repository README documents the API-specification workflow and its Anypoint CLI tooling; the commands below are the tool prerequisites it lists. Six indexed listings have no matching directory in the current tree (create-project-template, setup-agent-scanner, run-agent-scan-and-view-results, protect-mcp-server-with-policies, protect-api-with-policies and protect-agent-with-policies), and review-pr is a tree skill with no indexed listing.

## Installation

Install Anypoint CLI v4 and its API Project plugin:

```bash
npm install -g anypoint-cli-v4
anypoint-cli-v4 plugins:install anypoint-cli-api-project-plugin
```

Install the Python dependencies for the portal generator and validation scripts:

```bash
pip3 install -r scripts/requirements.txt
```

On a Homebrew-managed macOS Python (PEP 668) the README recommends a local virtual environment instead of a bare pip3 install.

Install the api-spec-validator skill in Claude Code:

```bash
/plugin marketplace add machaval/api-spec-skills
```

Git hooks are configured automatically the first time any make command runs. Common Makefile targets:

```bash
make help
make validate-all-governed
make validate-api API=name
make list-apis
make generate-portal
make test-portal
make report
```

## What It Provides

Use For cells are condensed from the skills' own SKILL.md frontmatter descriptions.

| Skill | Installs | Use For |
|---|---|---|
| build-mule-integration | 439 | the required first workflow before any Mule flow or integration change |
| generate-doc-description | 387 | adding doc:description attributes to Mule XML flows and components |
| secure-mule-app | 381 | encrypting sensitive data with Mule secure properties |
| manage-global-configurations | 365 | creating and consolidating connector configs and global elements |
| build-agent-broker-project | 342 | building, validating and deploying MuleSoft Agent Broker projects |
| generate-connectivity-knowledge | 333 | researching a SaaS API into an OpenAPI connectivity schema |
| generate-bat-tests | 328 | generating Blackbox API Testing (BAT) suites for Mule apps |
| pdk-templates | 326 | vetted Rust templates for Omni Gateway PDK features |
| pdk-unit | 325 | writing and running PDK policy unit tests |
| pdk-test | 325 | writing and running Docker-based PDK integration tests |
| pdk-prerequisites | 325 | installing the PDK toolchain and prerequisites |
| develop-pdk-policy | 325 | building, publishing and releasing a custom Flex Gateway policy |

The remaining 44 indexed listings range from 1 to 323 installs.

## Why This Matters for Hermes Agents

MuleSoft's skills model the full enterprise integration lifecycle: a mandatory pre-flight workflow (build-mule-integration) that requires the agent to load skill instructions before touching a Mule flow, run-configuration management, Blackbox API Testing, secure properties, global configs, Agent Broker projects, and the complete Flex Gateway PDK toolchain. Several skills insist the agent call use_skill as its first and only action, which is a concrete pattern for workflow gating that a prompt cannot skip. The PDK family pairs vetted Rust templates with unit and Docker-based integration test harnesses, showing how compiled policy artifacts can ship with their own verification. The connectivity-knowledge skill generates an OpenAPI spec from a SaaS API and validates it against the live endpoint, a useful reference for grounding agent research in real APIs. Two sampled skills fail Snyk, so treat the suite as a reference for MuleSoft-specific patterns rather than a drop-in.

## Usage

| You say | What happens |
|---|---|
| Create a new Mule integration for this project | Uses build-mule-integration, the required first workflow before any flow change |
| Encrypt the credentials in my Mule app | Uses secure-mule-app to configure Mule secure properties |
| Generate BAT tests for this HTTP API | Uses generate-bat-tests to scaffold a Blackbox API Testing suite |
| Build a custom Flex Gateway policy | Uses develop-pdk-policy to scaffold, build and release a PDK policy |
| Show me a PDK template for JWT validation | Uses pdk-templates to adapt a vetted Rust template |
| Add doc:description to my Mule flows | Uses generate-doc-description to document the Mule XML |
| Research this SaaS API that has no connector | Uses generate-connectivity-knowledge to build a connectivity schema |

## Verification

Confirm the README resolves on the master branch:

```bash
curl -sL https://raw.githubusercontent.com/mulesoft/mulesoft-dx/master/README.md | head -40
```

Review a representative skill body before installing:

```bash
curl -sL https://raw.githubusercontent.com/mulesoft/mulesoft-dx/master/skills/mule-development/build-mule-integration/SKILL.md | head -30
```

Validate a spec with the api-spec-validator ruleset after installing the Anypoint CLI plugin:

```bash
RULESET_PATH=~/.claude/plugins/marketplaces/api-spec-skill/skills/api-spec-validator/scripts/ruleset.yaml
anypoint-cli-v4 api-project validate --location=./path/to/your-service --local-ruleset=$RULESET_PATH
```

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| build-mule-integration | Pass | Pass | Warn |
| generate-doc-description | Pass | Pass | Pass |
| secure-mule-app | Pass | Warn | Fail |
| manage-global-configurations | Pass | Pass | Pass |
| build-agent-broker-project | Pass | Pass | Warn |
| generate-connectivity-knowledge | Pass | Warn | Warn |
| generate-bat-tests | Pass | Warn | Fail |
| pdk-templates | Pass | Warn | Pass |
| pdk-unit | Pass | Pass | Pass |
| pdk-test | Pass | Pass | Pass |
| pdk-prerequisites | Pass | Pass | Warn |
| develop-pdk-policy | Pass | Pass | Pass |
| create-mule-run-config | Pass | Pass | Pass |
| execute-mule-run-config | Pass | Pass | Pass |
| update-mule-run-config | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 24, 2026: 8,731 combined installs across 56 indexed listings; 16 GitHub stars; Apache-2.0 license; last pushed Nov 24, 2026. Counts drift over time.
- The install index outruns the tree: create-project-template, setup-agent-scanner, run-agent-scan-and-view-results, protect-mcp-server-with-policies, protect-api-with-policies and protect-agent-with-policies carry install counts but have no matching directory in the current tree.
- review-pr exists under .claude/skills/ but has no indexed listing.
- The repository README documents the API-specification workflow, not a single install command for the whole skills tree; the skills are consumed through the Anypoint CLI, the Claude Code plugin and the Makefile targets.
- skills.sh publishes per-skill descriptions only for the mule-development group; Use For cells for the remaining listings are name-level.
- Two sampled skills fail Snyk: secure-mule-app and generate-bat-tests.

## Related

- [SAP AI Skills Library - Enterprise Agent Skills Setup](/hermes/skills/catalog/sap-ai-skills-library-setup)
- [Microsoft Power Platform Skills - Setup Guide](/hermes/skills/catalog/microsoft-power-platform-skills-setup)
- [AWS Agent Plugins - Official AWS Plugin Suite Setup](/hermes/skills/catalog/aws-agent-plugins-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the Anypoint CLI plugin and Python dependencies before relying on the make targets; git hooks auto-configure on the first make run.
- Load build-mule-integration before any flow change; the skill insists on being the only tool call in that response.
- Use pdk-templates as a cookbook and develop-pdk-policy for the full scaffold, build and release lifecycle.
- Re-check the Snyk Fail findings for secure-mule-app and generate-bat-tests on skills.sh before production use.
- Treat the drift-flagged listings (create-project-template and the protect-* set) as index-only; confirm they exist before invoking them.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
