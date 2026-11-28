---
title: "SFCC B2C Developer Tooling - Setup Guide"
description: "Salesforce B2C Commerce developer tooling: 3.7K combined installs across 89 indexed skills covering the CLI, VS Code extension, MCP and SDK."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/sfcc-b2c-dev-tooling-setup/"
robots: "index,follow"
last_updated: "2026-11-28"
tags: ["hermes skill", "agent skill", "skill setup", "salesforce", "commerce cloud", "b2c"]
---

# SFCC B2C Developer Tooling - Setup Guide

**Source:** [salesforcecommercecloud/b2c-developer-tooling](https://www.skills.sh/salesforcecommercecloud/b2c-developer-tooling) via skills.sh - 3.7K combined installs across 89 indexed listings; first seen Nov 28 2026 (morning sweep)

**GitHub:** [SalesforceCommerceCloud/b2c-developer-tooling](https://github.com/SalesforceCommerceCloud/b2c-developer-tooling) - 58 stars, Apache-2.0 license, branch main, last pushed 2026-11-23. A pnpm monorepo holding b2c-cli, b2c-tooling-sdk and b2c-dx-mcp; agent skills live under skills/b2c-cli/skills/, skills/b2c/skills/ and skills/storefront-next/skills/ plus .agents/skills/, .claude/skills/ and packages/b2c-dx-mcp/skills/.

**Category:** Salesforce Commerce Cloud agent tooling - CLI, VS Code extension, MCP server and agent skills for B2C Commerce development

**Quality Tier:** 🟡 Yellow - Warn cells land on b2c-webdav (Snyk), b2c-slas-auth-patterns (Socket) and b2c-ecdn (Snyk); no Fail cells.

salesforcecommercecloud/b2c-developer-tooling is Salesforce's official developer tooling for B2C Commerce, published as a public repository and indexed on skills.sh. The repo ships a command line interface (b2c-cli), a VS Code extension, an MCP server (b2c-dx-mcp) and a tooling SDK, with agent skills distributed as installable plugins. The README marks the project Generally Available (GA) while noting the VS Code extension is still in Developer Preview.

The 89 indexed listings split across three plugin families: b2c-cli (CLI operations), b2c (storefront and platform development patterns) and Storefront Next (sfnext-*) skills for the SFNext frontend, plus small triage runbooks. Install counts are modest, from b2c-docs at 148 down to single-digit listings, so this is a niche suite for teams actively building on Salesforce B2C Commerce rather than a mass-market skill library.

## Installation

The README distributes the skills as three Claude Code plugins installed from the repo marketplace. In Claude Code, run these in chat:

```text
/plugin marketplace add SalesforceCommerceCloud/b2c-developer-tooling
/plugin install b2c-cli@b2c-developer-tooling
/plugin install b2c@b2c-developer-tooling
/plugin install b2c-dx-mcp@b2c-developer-tooling
```

Claude Code does not auto-update third-party marketplaces by default; run /plugin, open Marketplaces, select b2c-developer-tooling and enable auto-update to pick up new releases. For any supported IDE, the CLI can copy the skills in directly:

```bash
npx @salesforce/b2c-cli setup skills
```

Other editors follow the same marketplace pattern: VS Code via Command Palette (Cmd+Shift+P / Ctrl+Shift+P) -> Chat: Install Plugin From Source, GitHub Copilot CLI via `copilot plugin install b2c-cli@b2c-developer-tooling`, Cursor via Settings -> Plugins, Codex via /plugins, and Gemini via `gemini extensions install https://github.com/SalesforceCommerceCloud/b2c-developer-tooling`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| b2c-docs | 148 | Search and read B2C Commerce docs: Script API, Developer Center guides, job steps and XSD schemas. |
| b2c-scapi-shopper | 133 | Call Shopper Commerce APIs from headless storefronts and composable commerce apps. |
| b2c-webdav | 122 | List, upload, download and manage files on instances over WebDAV. |
| b2c-config | 115 | Configure CLI and MCP authentication, instances and project defaults. |
| b2c-slas-auth-patterns | 113 | Implement SLAS authentication: passwordless login, token refresh and JWT validation. |
| b2c-scapi-schemas | 108 | Browse and retrieve SCAPI OpenAPI schema specifications. |
| b2c-controllers | 102 | Create storefront controllers with SFRA or classic patterns and middleware chains. |
| b2c-logs | 101 | Retrieve and search instance logs with the CLI. |
| b2c-scapi-admin | 97 | Build backend integrations with SCAPI Admin APIs for ERP, OMS, WMS or CRM sync. |
| b2c-slas | 96 | Manage SLAS tenants, clients, identity providers and shopper sessions. |
| b2c-metadata | 96 | Define custom attributes, object types and site preferences in metadata XML. |
| b2c-job | 95 | Run jobs, monitor executions and import or export site archives. |
| b2c-ordering | 94 | Manage the order lifecycle from basket through checkout completion. |
| b2c-isml | 94 | Build ISML templates with standard tags and expression syntax. |
| b2c-hooks | 92 | Register and implement platform hooks declared in hooks.json. |
| b2c-ecdn | 92 | Manage eCDN zones, WAF, certificates and edge configuration. |
| b2c-custom-caches | 92 | Implement custom caching with CacheMgr and cache regions. |
| b2c-custom-api-development | 92 | Develop custom SCAPI REST endpoints with api.json and schema.yaml. |
| b2c-site-import-export | 90 | Author, validate, import and verify site archives and metadata XML. |
| b2c-sandbox | 90 | Create and manage on-demand sandboxes with the CLI. |

The table covers the 20 skills the repository documents with SKILL.md descriptions across the b2c-cli and b2c plugins. The remaining 69 indexed listings range from 1 to 90 installs, spanning the Storefront Next (sfnext-*) skills, the remaining b2c-cli commands and the triage runbooks.

## Why This Matters for Hermes Agents

This is Salesforce's own tooling for B2C Commerce, so it is the authoritative grounding for any agent that works on SFCC, SFRA or Storefront Next code. The skills are split by plugin, which lets a Hermes builder load only the surface an agent needs: b2c-cli for instance and data operations, b2c for platform and storefront development patterns, and Storefront Next for the SFNext frontend. Each skill carries a task-scoped description plus trigger evals under evals/trigger-evals.json, which is the pattern for skills that route reliably. The b2c-dx-mcp server turns the same knowledge into executable tools for code deploy, logs, diagnostics, docs and SCAPI, so an agent gets operations rather than instructions alone. The SDK ships bundled Script API references, XSD schemas and job-step data, letting an agent answer platform questions locally instead of guessing at dw.* APIs. Because the project is Apache-2.0 and Generally Available, it is safe to vendor for a commerce-focused profile.

## Usage

| You say | What happens |
|---|---|
| "Upload this cartridge to my sandbox" | b2c-webdav lists, uploads and manages files over WebDAV. |
| "Search the Script API docs for Basket methods" | b2c-docs reads the bundled Script API reference through the CLI. |
| "Build a headless checkout with SCAPI" | b2c-scapi-shopper covers shopper APIs, baskets and orders. |
| "Add passwordless login to my storefront" | b2c-slas-auth-patterns implements SLAS OTP, passkeys and token refresh. |
| "Create a new route in my SFRA cartridge" | b2c-controllers builds server.get/post controllers and middleware. |
| "My job keeps failing, check the logs" | b2c-logs retrieves and searches instance logs; b2c-job inspects executions. |
| "Spin up a fresh sandbox for testing" | b2c-sandbox creates and manages on-demand sandboxes. |

## Verification

The README's file-copy install is the quickest end-to-end check. Run it, then confirm the skills land in the editor's skills directory:

```bash
npx @salesforce/b2c-cli setup skills
```

To review a skill before installing, fetch its SKILL.md directly from branch main. The layout is skills/<plugin>/skills/<name>/SKILL.md, with plugin roots at skills/b2c-cli/skills/, skills/b2c/skills/ and skills/storefront-next/skills/:

```bash
curl -sL https://raw.githubusercontent.com/SalesforceCommerceCloud/b2c-developer-tooling/main/skills/b2c-cli/skills/b2c-docs/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| b2c-docs | Pass | Pass | Pass |
| b2c-scapi-shopper | Pass | Pass | Pass |
| b2c-webdav | Pass | Pass | Warn |
| b2c-config | Pass | Pass | Pass |
| b2c-slas-auth-patterns | Pass | Warn | Pass |
| b2c-scapi-schemas | Pass | Pass | Pass |
| b2c-controllers | Pass | Pass | Pass |
| b2c-logs | Pass | Pass | Pass |
| b2c-scapi-admin | Pass | Pass | Pass |
| b2c-slas | Pass | Pass | Pass |
| b2c-metadata | Pass | Pass | Pass |
| b2c-job | Pass | Pass | Pass |
| b2c-ordering | Pass | Pass | Pass |
| b2c-isml | Pass | Pass | Pass |
| b2c-hooks | Pass | Pass | Pass |
| b2c-ecdn | Pass | Pass | Warn |
| b2c-custom-caches | Pass | Pass | Pass |
| b2c-custom-api-development | Pass | Pass | Pass |
| b2c-site-import-export | Pass | Pass | Pass |
| b2c-sandbox | Pass | Pass | Pass |

This guide is Yellow because Socket and Snyk each flag skills, but nothing fails outright. The Gen Agent Trust Hub passes all 20 sampled listings, and the Warn cells sit on b2c-webdav (Snyk), b2c-slas-auth-patterns (Socket) and b2c-ecdn (Snyk). Only 20 of the 89 indexed listings were sampled.

## Limitations

- Snapshot data, verified 2026-11-28: 3,669 combined installs across 89 indexed listings; 58 GitHub stars; Apache-2.0 license; last pushed 2026-11-23. Counts drift over time.
- Install counts are uniformly small: the top listing (b2c-docs) has 148 installs, and the long tail of Storefront Next and triage skills carries single-digit installs.
- The VS Code extension is in Developer Preview while the CLI, SDK and MCP server are Generally Available; the project ships as-is without warranty.
- The skills.sh security verdicts cover 20 of the 89 indexed listings (the b2c-cli and b2c plugin skills); the other 69 are not sampled.
- Skills are spread across several plugin roots (skills/b2c-cli, skills/b2c, skills/storefront-next, skills/storefront-next-figma, .agents/skills, .claude/skills and packages/b2c-dx-mcp/skills), so a single skill name does not map to one directory.

## Related

- [Salesforce Skills Library (sf-skills) - 330+ Agent Skills](/hermes/skills/catalog/salesforce-sf-skills-setup)
- [Magento 2 Agent Skills - Adobe Commerce Suite](/hermes/skills/catalog/magento2-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install through the plugin marketplace on Claude Code and enable auto-update so the repo's plugin.json and new releases flow through.
- Read a skill's SKILL.md frontmatter before installing the whole plugin; each skill also ships trigger evals under evals/trigger-evals.json.
- Treat b2c-docs as the first hop for any B2C Commerce question: it grounds the agent in the bundled Script API reference and guides rather than guessing.
- Pair b2c-scapi-shopper with b2c-slas-auth-patterns for headless work, since shopper APIs and SLAS authentication are usually needed together.
- Keep the CLI updated so the SDK's bundled platform data (Script API docs, XSD schemas and job steps) tracks the current platform release.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
