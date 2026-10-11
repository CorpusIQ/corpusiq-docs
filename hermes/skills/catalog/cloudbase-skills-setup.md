---
title: "CloudBase Skills - Tencent Full-Stack Apps Setup"
description: "Setup guide for tencentcloudbase/cloudbase-skills - 12.5K combined installs. Official Tencent CloudBase skills for web, mini program, and app."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cloudbase-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "cloud development", "tencent cloudbase", "miniprogram"]
---

# CloudBase Skills - Setup Guide

**Source:** [tencentcloudbase/cloudbase-skills](https://www.skills.sh/tencentcloudbase/cloudbase-skills) via skills.sh - 12.5K combined installs across 33 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [tencentcloudbase/cloudbase-skills](https://github.com/tencentcloudbase/cloudbase-skills) (36 stars, MIT; pushed 2026-10-10; layout `skills/cloudbase/SKILL.md`, with sibling directories for the per-topic slices)
**Category:** Cloud Development / Full-Stack
**Quality Tier:** 🟡 Beta - official Tencent CloudBase; MIT; pushed Oct 10, 2026; one dominant listing; all sampled verdicts Pass

CloudBase is Tencent's platform for building and deploying full-stack apps: serverless cloud functions, document and relational databases, authentication, storage, hosting, and AI model access. This repository is the CloudBase team's own agent-skills collection, so the guidance tracks the product rather than a third party's notes. It sits at 12.5K combined installs across 33 indexed listings on skills.sh, and one skill is doing almost all of that work: `cloudbase` at 12,195 installs covers platform detection, per-platform auth (Web, WeChat Mini Program, Node.js), NoSQL and MySQL operations, cloud functions and CloudRun deployment, storage, AI model integration, and UI guidelines.

The other 32 listings are thin, targeted slices: `miniprogram-development` (14 installs) leads a tail that includes platform auth variants such as `auth-web-cloudbase` and `auth-nodejs-cloudbase` (9 each), database SDK skills such as `cloudbase-document-database-web-sdk` and `relational-database-mcp-cloudbase` (9 each), plus `cloudbase-code-review` (13), `cloudbase-cli` (13), `ops-inspector` (10), and `spec-workflow` (10). The practical pattern is to install the flagship skill and add slices only for the specific stack you are on. The README also recommends pairing the suite with the CloudBase MCP server for live tooling.

---

## Installation

Prerequisites: Node.js for the `npx` skills CLI. The README additionally recommends the CloudBase MCP server for live environment and deployment tools.

```bash
# Skills CLI: installs the CloudBase skill collection
npx skills add TencentCloudBase/cloudbase-skills
```

Once installed, the README notes the skill is applied automatically when the agent detects a relevant CloudBase task. For the MCP pairing, add the server to your agent's MCP config:

```json
{
  "mcpServers": {
    "cloudbase": {
      "command": "npx",
      "args": ["@cloudbase/cloudbase-mcp@latest"]
    }
  }
}
```

Config file locations by editor, per the README: `.cursor/mcp.json` (Cursor), `.mcp.json` (Claude Code), `~/.codeium/windsurf/mcp_config.json` (Windsurf).

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| cloudbase | 12,195 | Platform detection and SDK selection, per-platform auth flows, NoSQL and MySQL operations, cloud functions and CloudRun deployment, storage, AI models, and UI guidelines |

The remaining 32 indexed listings range from 4 to 14 installs.

## Why This Matters for Hermes Agents

CloudBase is where a large share of WeChat-ecosystem and Chinese-market products are built, and official guidance beats model priors: an agent that guesses at CloudBase APIs writes code that fails at deploy time. The flagship skill encodes the platform's real decision tree, including which SDK a Web or Mini Program project needs, how auth flows differ per platform, when to use document versus relational storage, and how functions and CloudRun deploy. Because Tencent maintains it, the material reflects what the platform team actually ships, it is MIT licensed, and it was pushed as recently as Oct 10, 2026. The MCP pairing matters for agents doing ops work: it turns deployment guidance into live calls for environment management and database operations. The 32 tiny listings are best treated as optional add-ons, lightly exercised, so review each SKILL.md before relying on one. For a Hermes agent working in the CloudBase ecosystem, this is the highest-signal skill source in the catalog for that platform.

## Usage

| You say | What happens |
|---|---|
| "Build a WeChat Mini Program with CloudBase login and a document database" | The cloudbase skill selects the Mini Program SDK, sets up the auth flow, and applies document-database patterns |
| "Deploy this cloud function to my CloudBase environment" | Cloud functions and CloudRun deployment guidance; with the CloudBase MCP server installed, live deployment tooling |
| "Add a MySQL-backed API to my web app" | Relational database guidance for the web stack, routed through the matching database slice |
| "Set up Node.js auth for my CloudBase backend" | auth-nodejs-cloudbase (9 installs) covers the Node.js auth pattern end to end |
| "Review this CloudBase code for platform mistakes" | cloudbase-code-review (13 installs) checks for idiomatic API usage |
| "Scaffold this feature from a spec" | spec-workflow (10 installs) turns the spec into a structured build plan |
| "Check my CloudBase environment for problems" | ops-inspector (10 installs) walks the environment for issues |

## Verification

```bash
# Confirm the collection installed (paths depend on your agent)
npx skills list | grep -i cloudbase

# Review the flagship skill straight from GitHub before installing (returns 200)
curl -s https://raw.githubusercontent.com/tencentcloudbase/cloudbase-skills/main/skills/cloudbase/SKILL.md | head -20
```

After install, confirm the layout: `skills/cloudbase/SKILL.md` for the flagship, with per-topic directories alongside it. If the MCP pairing is in play, check that the `cloudbase` server starts from your MCP config.

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| cloudbase | Pass | Pass | Pass |
| cloudbase-database | - | - | - |
| cloudbase-functions | - | - | - |

The flagship skill passed all three engines; the other two sampled listings returned no engine data. The tail is largely unsampled, so review individual SKILL.md files before depending on a small listing in production.

## Limitations

- Small repository: 36 GitHub stars and first indexed Oct 9, 2026; official work, but young, so expect churn.
- One dominant listing: cloudbase holds 12,195 of 12,499 installs; the other 32 listings sit at 4 to 14 installs each and are lightly exercised.
- The 4 to 14-install tail is unsampled by the security engines; review each SKILL.md before depending on it.
- Platform lock-in: everything here targets Tencent CloudBase and does not port to other clouds.
- The recommended CloudBase MCP server is a separate install with its own credentials and trust surface.
- Snapshot data, verified Oct 10, 2026: 12.5K combined installs across 33 indexed listings; 36 GitHub stars; MIT; last pushed Oct 10, 2026. Counts drift over time.

## Related

- [Alibaba Cloud AIOps Skills - 270-Skill Cloud Operations Suite Setup](/hermes/skills/catalog/alibaba-cloud-aiops-skills-setup) - the comparable official suite for the other major Chinese cloud platform
- [Build Mcp Server Setup](/hermes/skills/catalog/build-mcp-server-setup) - for wrapping your own tooling as an MCP server next to CloudBase MCP
- [Hermes Agent Core - Official Skill Setup Guide](/hermes/skills/catalog/hermes-agent-setup) - how Hermes Agent loads and applies skills
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the flagship cloudbase skill alone; it covers the full platform surface and accounts for nearly 98% of installs.
- Add slices only for the stack you are on: auth-nodejs-cloudbase for Node.js auth, cloudbase-document-database-web-sdk for web document DB access, relational-database-mcp-cloudbase for MySQL through MCP.
- Pair with CloudBase MCP when the agent needs to do live operations, not just write code.
- Keep the MCP config in the editor-specific file (.mcp.json, .cursor/mcp.json, or the Windsurf config) and credentials out of version control.
- The repo was pushed Oct 10, 2026; refresh the skill before starting a new CloudBase project so guidance matches the current API surface.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
