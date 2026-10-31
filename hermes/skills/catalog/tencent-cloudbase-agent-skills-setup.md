---
title: "Tencent CloudBase Agent Skills - WeChat Dev"
description: "tencentcloudbase/skills: 30.8K combined installs. 32 CloudBase skills for WeChat mini programs, cloud functions, databases and AI model routing."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/tencent-cloudbase-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "tencent cloudbase", "wechat mini program", "serverless"]
---

# Tencent CloudBase Agent Skills - Setup Guide

**Source:** [tencentcloudbase/skills](https://www.skills.sh/tencentcloudbase/skills) via skills.sh - 30.8K combined installs across 37 indexed listings; first seen 2026-10-31 (morning sweep)

**GitHub:** [tencentcloudbase/skills](https://github.com/tencentcloudbase/skills) - 80 stars, MIT, branch main, last pushed 2026-10-29; 32 `SKILL.md` directories, one per name under `skills/`, most with a `references/` folder beside them

**Category:** Tencent CloudBase and WeChat mini-program development: cloud functions, database and AI model routing

**Quality Tier:** 🟡 Yellow - four of the five sampled skills Pass all three auditors, but `setup-cloudbase-openclaw` carries a Snyk Fail plus a Trust Hub Warn

CloudBase is Tencent's serverless platform, and these 32 skills are the agent-facing half of it: the guidance an agent needs to build a WeChat mini program, a Web frontend, cloud functions, a CloudRun container, a document or PostgreSQL database, and an AI feature that calls a managed model from the browser, from Node.js or from inside a mini program. The repository was extracted from the CloudBase AI ToolKit, and the README says contributions still happen there, in `config/source/skills/`, with this repository as the published copy.

One naming trap first. This guide covers **tencentcloudbase/skills**, the agent-skill repository tracked on skills.sh. It does not cover `tencentcloudbase/cloudbase-skills`, a different repository that the existing [CloudBase Skills - Tencent Full-Stack Apps Setup](/hermes/skills/catalog/cloudbase-skills-setup) guide documents. The two share a maintainer, a topic and a confusingly similar name, and the installation command printed in this repository's README still points at the other one, so read the Installation section below before running anything.

## Installation

The README's install route is the skills CLI, but the command it prints names the sibling repository rather than this one:

```bash
npx skills add tencentcloudbase/cloudbase-skills
```

Treat that as a stale string. The repository you are reading about is `tencentcloudbase/skills`, and the same CLI takes it by its own name:

```bash
npx skills add tencentcloudbase/skills
```

The README's second route assumes you already have the files and copies one skill directory at a time into a client's skills folder:

```bash
# For Claude Desktop
cp -r config/source/skills/auth-tool ~/.config/claude/skills/

# For Cursor
cp -r config/source/skills/auth-tool .cursor/skills/
```

That example points at the ToolKit's internal layout (`config/source/skills/`) and at a name that exists only as `auth-tool-cloudbase` here, so for this profile the durable install is a clone plus a directory copy. The clone holds 32 complete skill directories, so copy the directories rather than the files:

```bash
git clone --depth 1 https://github.com/tencentcloudbase/skills.git /tmp/cloudbase-agent-skills
cp -r /tmp/cloudbase-agent-skills/skills/. ~/.hermes/profiles/corpusiq/skills/
```

Copying all 32 is the safe default because the skills address each other by relative path. Each `SKILL.md` opens with a "Sibling skills (local only)" note and points at `../auth-tool-cloudbase/SKILL.md`, so a single directory lifted out of the set loses the sibling it defers to. If you do want a subset, take the ones that reference each other as a group, for example `miniprogram-development`, `auth-tool-cloudbase`, `auth-wechat-miniprogram` and `cloudbase-document-database-in-wechat-miniprogram`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| miniprogram-development | 4,420 | Building, debugging, previewing, testing and publishing a WeChat mini program: `project.config.json`, appid and routing, the Developer Tools CLI, `miniprogram-ci` upload, console and network debugging, message push, customer service auto-reply and mini program search indexing. |
| auth-wechat-miniprogram | 2,229 | Native mini program identity: OPENID and UNIONID access, and how `wx.cloud` authentication behaves in projects where login is automatic and there is no login UI to build. |
| web-development | 1,793 | Implementing, integrating, debugging, building and deploying a Web frontend once the direction is settled: React, Vue, Vite, browser flows and CloudBase Web integration. |
| ui-design | 1,791 | Choosing visual direction, interface hierarchy, layout and design specification, or a prototype, before any Web or mini program UI is implemented. |
| cloudbase-document-database-in-wechat-miniprogram | 1,543 | Document database from inside a mini program: query, create, update and delete, with pagination, aggregation and geolocation queries. |
| cloud-functions | 1,217 | Writing, deploying and debugging your own Event or HTTP cloud functions, as opposed to calling CloudBase platform APIs. |
| spec-workflow | 1,215 | Forcing requirements, technical design and a task plan before implementation on medium-to-large changes with unclear acceptance criteria. |
| ai-model-wechat | 1,096 | Mini program AI through `wx.cloud.extend.AI`: `generateText` and `streamText` with `onText`, `onEvent` and `onFinish` callbacks, model groups and the two-step preflight before code. |
| cloudbase-platform | 1,088 | Platform orientation before picking a narrower skill: capability selection, console navigation, realtime features (broadcast, presence, live database changes) and cross-platform practice. |
| data-model-creation | 1,034 | No directory in the clone as of 2026-10-31, so there is no `SKILL.md` description to quote; treat the listing as a name to hunt down rather than a skill you can install from the tree. |
| auth-tool-cloudbase | 1,019 | Provider-side auth readiness before any login code: inspecting, enabling and disabling providers, publishable-key prerequisites, login methods, SMS and email senders. |
| cloud-storage-web | 1,013 | Cloud storage from the Web SDK: upload, download, temporary URLs, file management and the practices that keep a bucket tidy. |
| ai-model-nodejs | 1,001 | Node.js backend AI through `@cloudbase/node-sdk`: cloud functions, CloudRun, Express, Koa and NestJS, LLM proxies and agent orchestration, plus the only SDK path to image generation. |
| cloudrun-development | 988 | CloudBase Run in Function or Container mode: long connections, multi-language services, custom environments, VPC access to MySQL, PostgreSQL and Redis, and diagnosing deploy failures. |
| http-api-cloudbase | 982 | Calling CloudBase platform APIs over raw HTTP when a backend, script or non-SDK client cannot use an SDK or the MCP management tools. |
| auth-nodejs-cloudbase | 963 | Server-side identity from the Node SDK: reading caller identity, inspecting end users and bridging an existing user system into CloudBase with custom login tickets. |
| relational-database-mcp-cloudbase | 960 | Existing MySQL only, and marked deprecated in its own frontmatter: the `queryMysqlDatabase` and `manageMysqlDatabase` MCP tools, with permissions and schema work. New relational work routes to PostgreSQL. |
| auth-web-cloudbase | 956 | Web authentication for frontend integration once `auth-tool-cloudbase` has confirmed the providers: login methods and user management in the browser SDK. |
| cloudbase-document-database-web-sdk | 936 | Confirmed NoSQL collection work from the Web SDK: query, create, update and delete, with a redirect to the PostgreSQL skill if the task mentions CloudBase PG or `app.rdb()`. |
| ai-model-web | 916 | Browser and frontend AI through `@cloudbase/js-sdk`: `generateText` and `streamText` called directly from the page, with the explicit instruction not to propose a Node.js proxy. |

The remaining 17 indexed listings range from 2 to 901 installs.

## Why This Matters for Hermes Agents

CloudBase is a platform where the failure mode is confident, plausible code against the wrong SDK. Four different SDKs cover the same three concerns: `wx.cloud` inside a mini program, `@cloudbase/js-sdk` in a browser, `@cloudbase/node-sdk` on a server, and raw HTTP when none of the three is available. The suite keeps those lanes separate and says so in each description, and the AI skills go further, refusing to write code until a two-step preflight has run. That is the kind of rule a Hermes agent needs stated, because an agent asked for "AI in my app" will otherwise pick a lane at random and produce a proxy for a browser call or a browser call for a server job.

The auth split is the second useful part. `auth-tool-cloudbase` handles provider configuration and login readiness, `auth-web-cloudbase` and `auth-wechat-miniprogram` handle the client side per platform, and `auth-nodejs-cloudbase` handles the server side. Four skills for one word, "login", each with an explicit boundary in its description. An agent that respects those boundaries stops conflating "the login button does not work" with "the SMS sender was never configured".

The suite is also cheap to carry. The clone is markdown plus one YAML file, `skills/cloudbase/references/activation-map.yaml`, and nothing else: 210 markdown files, no build step, no postinstall hook. Deep material sits in `references/` folders that the agent opens only when it needs the detail, which keeps each `SKILL.md` short enough to stay routable.

`spec-workflow` is the odd one in the set and the most portable. It is a requirements-first workflow for medium-to-large changes, with nothing CloudBase-specific in it, so a profile that installs the suite for mini program work also gets a planning gate it can use anywhere.

## Usage

| You say | What happens |
|---|---|
| "Add a login screen to my mini program" | The agent starts at `auth-tool-cloudbase` to confirm the provider is enabled, then `auth-wechat-miniprogram` for OPENID handling, rather than writing a login form the platform does not need. |
| "Call DeepSeek from my WeChat mini program" | `ai-model-wechat` takes over: `wx.cloud.extend.AI.createModel`, the data wrapper `streamText` requires, the model id field, and the preflight before any code. |
| "Add streamed AI chat to the marketing site" | `ai-model-web` routes it to `@cloudbase/js-sdk` in the browser and explicitly does not build a Node proxy, which is the usual wrong turn. |
| "My CloudRun container will not start" | `cloudrun-development` walks the deploy failure modes: readiness and probe failures, image start errors and a deploy stuck behind a running task, with a pointer to HTTP functions for stateless work. |
| "Store this order in the database" | The agent picks by platform and by engine: document database from a mini program or the Web SDK, or `postgresql-development-cloudbase` when the project is on CloudBase PG. |
| "Why does this query fail with a permission error" | `cloudbase-document-database-web-sdk` covers the Web SDK side; if the environment already runs MySQL, `relational-database-mcp-cloudbase` covers the MCP query tools, and both say which engine they mean. |
| "This change touches six files across two apps" | `spec-workflow` stops the agent and asks for requirements, a technical design and a task plan before it edits anything. |

## Verification

The raw path for the top skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} miniprogram-development\n" \
  https://raw.githubusercontent.com/tencentcloudbase/skills/main/skills/miniprogram-development/SKILL.md
```

Expect `200`. After the copy lands, confirm the count and the layout:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/miniprogram-development \
      ~/.hermes/profiles/corpusiq/skills/cloud-functions \
      ~/.hermes/profiles/corpusiq/skills/auth-tool-cloudbase | wc -l
head -6 ~/.hermes/profiles/corpusiq/skills/cloud-functions/SKILL.md
```

The count should print 3, and the header should show `name: cloud-functions`, a `description:` that opens with "CloudBase function runtime guide", `version: 2.36.2` and `license: MIT`. Check that `references/` came along, since `cloud-functions` and `miniprogram-development` both lose most of their depth without it:

```bash
find ~/.hermes/profiles/corpusiq/skills/cloud-functions -type f | wc -l
```

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31). The one Fail in the sample is on `setup-cloudbase-openclaw`, which Snyk fails and Gen Agent Trust Hub warns on, while the other four sampled skills Pass all three auditors - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| miniprogram-development | Pass | Pass | Pass |
| data-model-creation | Pass | Pass | Pass |
| cloudbase-document-database-web-sdk | Pass | Pass | Pass |
| setup-cloudbase-openclaw | Warn | Pass | Fail |
| cloudbase-agent-python | Pass | Pass | Pass |

Two things soften that verdict without clearing it. First, `setup-cloudbase-openclaw` has no directory in the clone: it is one of five indexed listings with no matching `SKILL.md`, so there is no file here to read and audit yourself, only the skills.sh report. Second, the rest of the suite is unusually inert. The tree holds markdown, 34 per-skill `LICENSE.md` copies and a single YAML activation map, with no shell script, no package manifest and no postinstall step, so nothing executes at install time.

What carries risk instead is what the instructions tell an agent to run, and those instructions are about credentials. The `cloudbase-cli` skill covers `tcb login`, environment API keys, login policy and safe domains, and the auth skills cover publishable keys and SMS sender configuration, which means an agent following them will be handling live platform settings. Keep `SECRETID` and `SECRETKEY` in the environment or in the CLI's own profile, never pasted into a prompt, and give the agent an environment that is not production before you let it touch environment lifecycle commands.

## Limitations

- Snapshot data, verified 2026-10-31: 30,797 combined installs across 37 indexed listings; 80 GitHub stars; MIT; last pushed 2026-10-29. Counts drift over time.
- The index is bigger than the tree. 37 listings, 32 directories: `cloudbase-agent-python`, `cloudbase-agent-ts`, `cloudbase-guidelines`, `data-model-creation` and `setup-cloudbase-openclaw` have no `SKILL.md` in the clone, and `data-model-creation` still sits at 1,034 installs inside the table above with nothing behind it.
- The README's install command names another repository. `npx skills add tencentcloudbase/cloudbase-skills` resolves to the sibling project, not to this one, and the copy examples use ToolKit-internal paths and a short name (`auth-tool`) that does not exist here. Every command in the README needs reading before running.
- Install counts are not a ranking of quality or freshness. Two of the twenty listed skills, `relational-database-mcp-cloudbase` at 960 and `relational-database-web-cloudbase` at 901, carry a `[Deprecated]` prefix in their own frontmatter telling you not to use MySQL for new relational work, and the skill that replaces them, `postgresql-development-cloudbase`, sits at 79.
- The suite is bilingual. Descriptions and bodies carry Chinese terms beside the English, which is helpful for anyone searching in Chinese and a nuisance for an agent that has to match a trigger phrase, and it makes the descriptions longer than the platform's own routing budget.
- Routing overlap is real inside the AI trio. `ai-model-nodejs`, `ai-model-web` and `ai-model-wechat` each forbid the other two in their own text, so a mis-route produces confident code for the wrong runtime, with the SDK import as the only visible clue.

## Related

- [CloudBase Skills - Tencent Full-Stack Apps Setup](/hermes/skills/catalog/cloudbase-skills-setup)
- [WeCom CLI Skills - Enterprise WeChat Agent Suite Setup](/hermes/skills/catalog/wecom-cli-skills-setup)
- [WeRead Skills - Tencent WeChat Reading Agent Skill Setup](/hermes/skills/catalog/weread-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy all 32 directories, not a selection. The "Sibling skills (local only)" header on every `SKILL.md` means the set is addressed as a graph, and a partial install leaves dangling relative links that an agent will follow into nothing.
- Read the deprecation markers before installing. `relational-database-mcp-cloudbase` and `relational-database-web-cloudbase` both describe themselves as existing-MySQL-only and point at `postgresql-development-cloudbase`, which is the skill to install for anything new.
- Trust the frontmatter over the install count for version checks. Every directory pins `version: 2.36.2`, so you can diff a local copy against upstream quickly instead of guessing at drift.
- Give the agent a non-production environment for anything that touches environment lifecycle, API keys or safe domains. The CLI skill documents `env create`, `env modify` and `env destroy` as ordinary operations, and an agent will treat them as ordinary.
- Skip `setup-cloudbase-openclaw` until its Snyk Fail is explained. It has no file in the tree to read, only an audit verdict, and the thing it sets up is not needed for mini program or Web work.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
