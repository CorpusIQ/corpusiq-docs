---
title: "SDK Generation Skills - Speakeasy Agent Suite Setup"
description: "speakeasy-api/sdk-generation-skills: OpenAPI authoring, overlays, MCP server generation and multi-target SDK orchestration - 1.5K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sdk-generation-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "sdk", "openapi", "mcp"]
---

# SDK Generation Skills - Speakeasy Agent Suite Setup

**Source:** [speakeasy-api/sdk-generation-skills](https://www.skills.sh/speakeasy-api/sdk-generation-skills) via skills.sh - 1.5K combined installs across 26 indexed listings; first catalogued Nov 21, 2026 (Nov 21, 2026 evening sweep)
**GitHub:** [speakeasy-api/sdk-generation-skills](https://github.com/speakeasy-api/sdk-generation-skills) - 18 stars, Apache-2.0, master branch, last pushed Feb 10, 2026; skills live under `skills/<name>/SKILL.md` with per-skill `content/` and `reference/` subfolders, plus `evals/`, `templates/` and a `.claude-plugin/` directory.
**Category:** SDK Generation and OpenAPI Tooling
**Quality Tier:** 🟡 Yellow - 0 Fail and 2 Warn cells across the 20-skill sample: Snyk Warns on start-new-sdk-project and generate-terraform-provider; 5 sampled listings carry no parsed verdict.

Speakeasy is the company behind the Speakeasy CLI, which generates client SDKs, Terraform providers and MCP servers from OpenAPI specifications. This repository is its collection of Agent Skills for that toolchain: authoring OpenAPI specs, extracting specs from existing code, managing overlays, generating SDKs (single and multi-target), generating MCP servers, and orchestrating cross-repo SDK generation. The README describes the set as working with Claude Code, Cursor, GitHub Copilot, Gemini CLI and 15+ other platforms.

The skills.sh index and the repository tree tell different stories. The index lists 26 skills, but the current tree ships 14 skill directories; the top 13 listings sit in a flat 78 to 171 install band, which reflects one suite installed as a unit rather than independent adoption. This is an older repository - last pushed Feb 10, 2026 - so the Speakeasy CLI release it targets may predate current versions.

## Installation

The README's install line is:

```bash
npx skills add speakeasy-api/skills
```

Note the README spells the source as `speakeasy-api/skills` while the repository is indexed as `speakeasy-api/sdk-generation-skills` on both skills.sh and GitHub; use the `sdk-generation-skills` slug if the skills shorthand does not resolve.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| writing-openapi-specs | 171 | authoring and improving OpenAPI specs: naming conventions, polymorphism, enums, file uploads, server-sent events |
| extract-openapi-from-code | 137 | generating an OpenAPI spec from existing API code in FastAPI, Flask, Django, Spring Boot, NestJS, Rails and more |
| manage-openapi-overlays | 102 | creating, applying and validating overlay files with x-speakeasy extensions, JSONPath targeting, retries, pagination and naming |
| speakeasy-context | 97 | the workflow entry point: run speakeasy agent context first, do the task, run speakeasy agent feedback last |
| generate-mcp-server | 95 | generating a Model Context Protocol server from an OpenAPI spec with Speakeasy |
| setup-sdk-testing | 92 | setting up SDK testing, contract tests, Arazzo test workflows and integration tests |
| improve-sdk-naming | 92 | AI-powered SDK naming improvements via the speakeasy suggest command |
| customize-sdk-hooks | 92 | implementing SDK lifecycle hooks (BeforeRequest, AfterSuccess, AfterError) for headers, telemetry and HMAC signing |
| configure-sdk-options | 92 | configuring an existing SDK: gen.yaml for TypeScript, Python, Go, Java, C#, PHP, Ruby plus runtime overrides |
| start-new-sdk-project | 91 | the primary entry point for generating a new SDK from an OpenAPI spec |
| diagnose-generation-failure | 91 | debugging failed SDK generation and Speakeasy workflow errors |
| orchestrate-multi-target-sdks | 86 | generating SDKs for multiple languages from one spec via workflow.yaml multi-target configuration |
| orchestrate-multi-repo-sdks | 78 | coordinating per-language SDKs across separate repositories: workflow dispatch and PR reconciliation |

The remaining 13 indexed listings range from 1 to 77 installs.

## Why This Matters for Hermes Agents

An agent that generates SDKs from an OpenAPI spec needs the discipline this suite encodes. The speakeasy-context skill routes the agent to `speakeasy agent context` for accurate CLI flags instead of web search, start-new-sdk-project is the primary generation entry point, and diagnose-generation-failure handles the "Step Failed" cases that otherwise stall a build. The suite's stated "overlay over modify" principle matters for teams: never edit a source spec directly, because overlays keep patches portable across spec versions. The multi-target and multi-repo orchestration skills address the real operations problem of shipping one spec to many language SDKs, whether in a monorepo or across separate repositories. For builder-facing agents the MCP server skill is the bridge: it turns an OpenAPI spec into an AI-assistant tool surface. The counterweight is maintenance: the repository's last push predates this snapshot by several months, and 12 of 26 indexed listings have no directory in the current tree, so an agent should rely on the 14 in-tree skills and treat the index tail as historical.

## Usage

| You say | What happens |
|---|---|
| Generate a TypeScript SDK from my OpenAPI spec | Routes to start-new-sdk-project and runs Speakeasy CLI generation from the spec |
| Why did SDK generation fail? | Runs diagnose-generation-failure and reads the Step Failed workflow error |
| Extract an OpenAPI spec from my FastAPI app | Uses extract-openapi-from-code to generate a spec from the existing Python code |
| Add retries and pagination to my spec | Creates an OpenAPI overlay via manage-openapi-overlays without touching the source spec |
| Generate an MCP server from my API | Runs generate-mcp-server to turn the OpenAPI spec into a Model Context Protocol server |
| Generate SDKs for Python, Go and TypeScript at once | Uses orchestrate-multi-target-sdks for a multi-language monorepo build |
| Improve the SDK method names | Runs improve-sdk-naming via speakeasy suggest for AI-powered naming fixes |

## Verification

Review the primary generation skill before install:

```bash
curl -sL https://raw.githubusercontent.com/speakeasy-api/sdk-generation-skills/master/skills/start-new-sdk-project/SKILL.md | head -40
```

Review the OpenAPI authoring reference:

```bash
curl -sL https://raw.githubusercontent.com/speakeasy-api/sdk-generation-skills/master/skills/writing-openapi-specs/SKILL.md | head -40
```

Review the MCP server skill:

```bash
curl -sL https://raw.githubusercontent.com/speakeasy-api/sdk-generation-skills/master/skills/generate-mcp-server/SKILL.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| writing-openapi-specs | Pass | Pass | Pass |
| extract-openapi-from-code | Pass | Pass | Pass |
| manage-openapi-overlays | Pass | Pass | Pass |
| speakeasy-context | Pass | Pass | Pass |
| generate-mcp-server | Pass | Pass | Pass |
| setup-sdk-testing | Pass | Pass | Pass |
| improve-sdk-naming | Pass | Pass | Pass |
| customize-sdk-hooks | Pass | Pass | Pass |
| configure-sdk-options | Pass | Pass | Pass |
| start-new-sdk-project | Pass | Pass | Warn |
| diagnose-generation-failure | Pass | Pass | Pass |
| orchestrate-multi-target-sdks | Pass | Pass | Pass |
| orchestrate-multi-repo-sdks | Pass | Pass | Pass |
| generate-terraform-provider | Pass | Pass | Warn |
| validate-openapi-spec | not parsed | not parsed | not parsed |
| regenerate-sdk | not parsed | not parsed | not parsed |
| merge-openapi-specs | not parsed | not parsed | not parsed |
| improve-operation-ids | Pass | Pass | Pass |
| get-ai-suggestions | not parsed | not parsed | not parsed |
| fix-validation-errors-with-overlays | not parsed | not parsed | not parsed |

The sample is clean on the whole: 15 of 20 skills read Pass across all three scanners, with two Snyk Warns and five listings the scanners could not parse.

## Limitations

- Snapshot data, verified Nov 21, 2026: 1,482 combined installs across 26 indexed listings; 18 GitHub stars; Apache-2.0; last pushed Feb 10, 2026. Counts drift over time.
- The install index outruns the tree: 26 indexed listings against 14 skill directories. Twelve listings (validate-openapi-spec, regenerate-sdk, merge-openapi-specs, improve-operation-ids, get-ai-suggestions, fix-validation-errors-with-overlays, create-openapi-overlay, configure-authentication, check-workspace-status, apply-openapi-overlay, sdk-tf-generation-best-practices and customize-sdk-runtime) have no counterpart directory to install.
- The README's install line points at `speakeasy-api/skills`, a different spelling from the repository name `speakeasy-api/sdk-generation-skills` used on skills.sh and GitHub.
- The repository is an older one: its last push (Feb 10, 2026) predates this snapshot by several months, so the Speakeasy CLI release it targets may not be current.
- The flat install band (78 to 171) is one suite installed as a unit, not independent adoption per skill, so the counts do not signal which individual skills are most used.
- Five of the 20 sampled listings carry "not parsed" on all three scanners, which is a missing verdict rather than a clean or dirty signal.

## Related

- [Awesome Copilot - MCP Server Generators & GitHub Automation Setup](/hermes/skills/catalog/awesome-copilot-setup)
- [Build Mcp Server Setup](/hermes/skills/catalog/build-mcp-server-setup)
- [Decentraland SDK Skills - Scene Building Setup](/hermes/skills/catalog/decentraland-sdk-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `speakeasy agent context` first, as the speakeasy-context skill instructs, so the agent reads accurate CLI flags instead of guessing from web search.
- Prefer overlays over editing source specs: the suite's own principle keeps patches portable across spec versions and avoids corrupting the source.
- Pipe `speakeasy run --output console` through grep or tail to keep generation output out of the context window.
- Route the 12 index-only listings through the overlapping in-tree skills (manage-openapi-overlays covers create-openapi-overlay and apply-openapi-overlay) since those names have no directory to install.
- Treat the suite as stable tooling: verify the Speakeasy CLI version against current docs before scripting around it, given the Feb 10, 2026 last push.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
