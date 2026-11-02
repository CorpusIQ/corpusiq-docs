---
title: "Web AI Agent Skills - Browser AI APIs and WebMCP"
description: "webmaxru/web-ai-agent-skills: 5.3K combined installs across 11 listings. Skills for browser Prompt API, Translator, Proofreader, WebMCP and WebNN."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/web-ai-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "webmcp", "prompt api", "browser ai", "webnn"]
---

# Web AI Agent Skills - Setup Guide

**Source:** [webmaxru/web-ai-agent-skills](https://www.skills.sh/webmaxru/web-ai-agent-skills) via skills.sh - 5.3K combined installs across 11 indexed listings; first seen 2026-11-01 (evening sweep)

**GitHub:** [webmaxru/web-ai-agent-skills](https://github.com/webmaxru/web-ai-agent-skills) - 53 stars, no license file in the repo root, branch main, last pushed 2026-09-29; 11 `SKILL.md` directories, 7 product skills under `skills/` and 4 repository-maintenance skills under `.github/skills/`

**Category:** Browser AI APIs for agents: Prompt API, Translator, Writing Assistance, Proofreader, WebMCP and WebNN

**Quality Tier:** 🟡 Yellow - no LICENSE file in the repository root, so the code stays unlicensed by default until the maintainer adds one, and one of the five sampled skills carries a Snyk warn

The repository is maintained by Maxim Salnikov, listed as author in `apm.yml`, and it exists because the browser AI surface moves faster than the examples that describe it. Seven skills cover the current web AI APIs: Prompt API, Language Detector API, Translator API, Writing Assistance APIs (Summarizer, Writer, Rewriter), Proofreader API, WebMCP and WebNN. Four more skills under `.github/skills/` maintain the repository itself and are indexed on skills.sh alongside the product skills.

Each skill follows the agentskills.io layout the README describes: a lean `SKILL.md` procedure, `references/` files for API surface and compatibility, `assets/` templates in TypeScript, and one deterministic `.mjs` scanner per skill that inventories candidate frontend files before any code is written. The procedures carry explicit stop conditions, so a skill that finds no browser app, no secure context or no permissions-policy allowance says so instead of generating code that cannot run.

What makes the set worth reading, even if you never install it, is that the `references/compatibility.md` files track preview behaviour per Chrome milestone. WebMCP alone records the `modelContext` getter moving from `Navigator` to `Document` in Chrome 150, `registerTool()` returning a promise from Chrome 151, the `execute` signal from Chrome 153 and the `consequentialHint` annotation from Chrome 154, with the spec links behind each change.

## Installation

The README's recommended path is the plugin marketplace, which installs all 11 skills as one plugin named `web-ai-skills` from the `webmaxru/ai-native-dev` marketplace. GitHub Copilot CLI and Claude Code use the same two commands:

```bash
> /plugin marketplace add webmaxru/ai-native-dev
> /plugin install web-ai-skills@webmaxru-ai-native-dev
```

VS Code takes the marketplace through settings instead, then installs from the Extensions sidebar:

```jsonc
"chat.plugins.marketplaces": [
    "webmaxru/ai-native-dev"
]
```

Search `@agentPlugins` in that sidebar for **web-ai-skills**, or run **Chat: Install Plugin From Source** and enter `https://github.com/webmaxru/ai-native-dev`.

Per-skill installs go through Agent Package Manager:

```bash
apm init                                                   # once per project
apm install webmaxru/web-ai-agent-skills/skills/webmcp
```

The npm route installs the same thing one skill at a time:

```bash
npx skills add webmaxru/web-ai-agent-skills --skill webmcp
```

For Hermes the documented routes do not apply, since none of them target a Hermes skills directory. Copy the directories instead, and read the skill you want before the copy lands:

```bash
git clone https://github.com/webmaxru/web-ai-agent-skills.git
cp -R web-ai-agent-skills/skills/* ~/.hermes/profiles/corpusiq/skills/
```

That copies the 7 product skills. The 4 repository-maintenance skills stay behind unless you copy `.github/skills/*` as well, which is usually the right default: they exist to create, validate and release skills in this repository, not to work on your app.

Nothing here needs an API key, an account or a hosted service. The skills edit browser code in your workspace, and the only runtime dependency in the root `package.json` is the `skills` CLI itself, pinned there as `^1.4.5` with no install or postinstall script.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| webmcp | 530 | Exposing page tools to agents: choosing imperative `document.modelContext` registration with a `navigator.modelContext` fallback against declarative form annotations, tool annotations such as `readOnlyHint` and `consequentialHint`, and cleanup through the `AbortSignal` passed to `registerTool()`. |
| language-detector-api | 489 | Language Detector work: secure-context and permissions-policy checks, `availability()` and `create()` with download progress, confidence-aware `detect()` results with `und` handling, and quota-aware `measureInputUsage()` preflight. |
| writing-assistance-apis | 488 | Summarizer, Writer and Rewriter integrations: availability checks, model download UX, batch and streaming output, abort handling, and `destroy()` cleanup. |
| github-agentic-workflows | 485 | Authoring and debugging GitHub Agentic Workflows: workflow markdown and frontmatter, `gh aw` compile and run flows, safe outputs, and security guardrails for the automation. |
| proofreader-api | 484 | Proofreader integrations: monitored model downloads, `proofread()` result handling, correction types and explanations, and quota-aware input measurement before a long proofread. |
| translator-api | 482 | On-device translation for a fixed language pair: `translate()` and `translateStreaming()`, cancellation, input-usage checks, and edge cases such as identity translation returning unchanged text. |
| webnn | 476 | Local inference with the Web Neural Network API: `navigator.ml` checks, `MLContext` and `MLGraphBuilder` flows, device intent through `powerPreference` or `accelerated: false`, tensor readback, and explicit fallback to another local runtime. |
| skill-creator | 475 | Writing skills to the agentskills.io spec: naming rules, routing descriptions with negative triggers, a lean `SKILL.md`, bulky detail moved to `references/` or `assets/`, plus a metadata validator script. |
| agent-package-manager | 474 | Operating APM: initialising `apm.yml`, installing and updating packages, validating manifests, managing lockfiles, compiling agent context, and packaging resolved context for CI. |
| agent-skill-deploy | 470 | Releasing a skill collection to GitHub releases, the Claude Code marketplace, and the VS Code and Copilot CLI plugin marketplaces, with pre-flight validation, version bumps across surface configs, and dry runs. |
| prompt-api | 464 | Browser Prompt API work: `LanguageModel` availability checks, session shapes across `prompt()`, `promptStreaming()`, `initialPrompts`, `append()` and `responseConstraint`, structured output, download UX, and iframe permissions-policy handling. |

All 11 indexed listings appear in the table above; the smallest is 464 installs.

## Why This Matters for Hermes Agents

Most browser automation for an agent means the model reading a DOM and guessing which element to click. WebMCP inverts that. The page registers tools, and the agent calls a named tool with a typed `inputSchema` and an `execute` callback instead of inferring intent from markup. The skill in this repo is written against that contract at the level of detail that decides whether an integration survives a browser milestone: resolve the context as `document.modelContext || navigator.modelContext`, await `registerTool()` inside a try and catch because only Chrome 151 and later return a promise, and unregister by aborting the signal rather than calling the removed `unregisterTool()`.

The annotations are the part that maps onto agent safety. `readOnlyHint` marks tools that do not change state, `consequentialHint` marks irreversible or real-world actions such as a purchase or a transfer so the agent knows to ask for confirmation first, and `untrustedContentHint` marks output that may carry text from an untrusted source. The skill still tells you not to treat any of them as enforcement: the page has to keep its own authorization checks and visible confirmation, because the annotation informs the agent and cannot constrain it.

The limits are stated as plainly as the capabilities. WebMCP needs a secure window browsing context, has no headless tool-calling mode, and currently runs only in the Chrome preview behind `chrome://flags/#enable-webmcp-testing` from Chrome 146. A Hermes browser session that drives a real visible page can use it; a headless scrape cannot, and knowing that before you write the integration saves a debugging afternoon.

For the rest of the suite the gain is narrower but real. Each skill opens by locating the frontend surface with its own scanner script, for example `node skills/webmcp/scripts/find-webmcp-targets.mjs .`, then reads the matching reference file before writing code. That ordering is the difference between an agent that edits the right entry point and one that appends a demo snippet to whatever file it found first.

## Usage

| You say | What happens |
|---|---|
| "Add a language detection step before we translate user reviews" | language-detector-api scans the workspace for the frontend surface, confirms secure context and the `language-detector` permissions-policy, then wires `availability()`, download progress and a confidence-aware `detect()` call. |
| "Expose our order lookup as a tool agents can call" | webmcp picks the imperative shape, adapts `assets/model-context-registry.template.ts`, registers a tool with an explicit schema and a `readOnlyHint` where nothing changes, and notes the Chrome version that awaits the registration promise. |
| "Book flow needs an agent to fill the form" | webmcp switches to declarative annotations: `toolname` and `tooldescription` on the form, `toolparamdescription` on its fields, and `toolautosubmit` only if the page should submit without a human step. |
| "Stream summaries of long support threads in the browser" | writing-assistance-apis chooses `Summarizer`, wires monitored creation, streams output, aborts cleanly on cancel and destroys the session when the component unmounts. |
| "Run our small classifier on device instead of the server" | webnn checks `navigator.ml`, builds the graph, sets `powerPreference` or `accelerated: false` deliberately, and keeps an explicit fallback instead of silently switching to remote inference. |
| "Why does the Prompt API call fail inside the iframe" | prompt-api reads `references/compatibility.md` and `references/troubleshooting.md`, checks the `language-model` permissions-policy on the embedding frame, and reports the missing allowance rather than rewrapping the call. |
| "Add a maintainer workflow for our own skills repo" | skill-creator validates the name and description, starts from `assets/SKILL.template.md`, and keeps the procedure in `SKILL.md` with bulky rules in `references/`. |

## Verification

Every `SKILL.md` path below returned 200 on the `main` branch when this guide was written, including the four `.github/skills/` entries:

```bash
for p in skills/webmcp skills/prompt-api skills/translator-api skills/webnn \
         skills/proofreader-api skills/language-detector-api skills/writing-assistance-apis \
         .github/skills/skill-creator .github/skills/agent-package-manager \
         .github/skills/agent-skill-deploy .github/skills/github-agentic-workflows; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/webmaxru/web-ai-agent-skills/main/$p/SKILL.md"
done
```

Read two of them before installing anything, because they set the pattern the rest follow: the WebMCP skill for how the tool contract is described, and the Prompt API skill for how a session wrapper is scoped.

- https://raw.githubusercontent.com/webmaxru/web-ai-agent-skills/main/skills/webmcp/SKILL.md
- https://raw.githubusercontent.com/webmaxru/web-ai-agent-skills/main/skills/prompt-api/SKILL.md

After the copy, confirm what landed and that the frontmatter name matches the directory, which is rule one of the repository conventions:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -E '^(webmcp|prompt-api|translator-api|webnn|proofreader-api|language-detector-api|writing-assistance-apis)$'
head -4 ~/.hermes/profiles/corpusiq/skills/webmcp/SKILL.md
```

Run a scanner against a real app before trusting the skill's focus. It prints candidate entry points and existing API markers, and takes no action:

```bash
node ~/.hermes/profiles/corpusiq/skills/webmcp/scripts/find-webmcp-targets.mjs ~/path/to/app
```

One path in the repository documentation is stale. The README and `AGENTS.md` both point at `.agents/skills/skill-creator/scripts/validate-metadata.py`, which returns 404, while `.github/skills/skill-creator/scripts/validate-metadata.py` returns 200. Use the second path:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/webmaxru/web-ai-agent-skills/main/.github/skills/skill-creator/scripts/validate-metadata.py
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| webmcp | Pass | Pass | Pass |
| writing-assistance-apis | Pass | Pass | Pass |
| translator-api | Pass | Pass | Pass |
| agent-package-manager | Pass | Pass | Warn |
| prompt-api | Pass | Pass | Pass |

The repository has no LICENSE file at its root, and that is the finding to fix before you depend on it: with no licence, the default is all rights reserved, whatever the per-skill frontmatter says. Ten of the eleven `SKILL.md` files in the clone declare `license: MIT` in their own YAML, and `skill-creator` declares no licence at all, so the maintainer's intent is clear but intent in a skill file is not a grant. Treat the repository as unlicensed until a root LICENSE appears, and if you plan to redistribute the skills inside a product, ask first.

One of the five sampled skills, agent-package-manager, carries a Snyk Warn. It is also the skill with the widest reach, since it initialises manifests, resolves packages and compiles agent context from remote sources, so read that `SKILL.md` before running it against a repository you care about.

What executes on install is small. The root `package.json` declares no `scripts` block, so cloning and copying run nothing. The helper scripts are Node file walkers: `find-webmcp-targets.mjs` reads the workspace tree and prints candidate paths, with no network call, no `exec` and no `spawn`. The `assets/` files are TypeScript templates that only run if you paste them into an app.

The risk sits in the code these skills help write, and in one place the WebMCP skill is explicit about it. Cross-origin iframes need `allow="tools"` from the embedding document, otherwise `registerTool()` throws `NotAllowedError`, and a page that registers a tool is inviting an agent to act on it. Keep authorization and confirmation inside the page, use `consequentialHint` for anything irreversible, and do not let a tool description become the only thing standing between an agent and a purchase.

## Limitations

- Snapshot data, verified 2026-11-01: 5,317 combined installs across 11 indexed listings; 53 GitHub stars; no LICENSE file in the repo root; last pushed 2026-09-29. Counts drift over time.
- Unlicensed by default. The root has no LICENSE file, while ten of the eleven `SKILL.md` files declare `license: MIT` in their frontmatter and `skill-creator` declares none, so the repository's legal status depends on a file that is not there.
- The index is wider than the product. Four of the 11 indexed skills live under `.github/skills/` and exist to create, validate and release skills in this repository. Installing all 11 puts their trigger phrases, including skill authoring and marketplace deployment, into the same skill index your app work uses.
- The repository's own documentation points at a path that does not exist. The README and `AGENTS.md` both cite `.agents/skills/skill-creator/scripts/validate-metadata.py`, which returns 404, while the file at `.github/skills/skill-creator/scripts/validate-metadata.py` returns 200.
- The skills only apply to browser JavaScript or TypeScript. Each one stops and says so when the workspace is not a web app, and none of them covers server-side SDKs, REST AI providers or worker contexts where the API forbids them.
- Preview behaviour dominates. WebMCP is a Community Group draft in a Chrome-only preview behind a flag from Chrome 146, the imperative surface has changed across six milestones, and the declarative surface is not fully specified.

## Related

- [Web Access Skill - Unified Browsing & Scraping Setup](/hermes/skills/catalog/web-access-skill-setup)
- [Modern Web Guidance - Google Chrome Agent Skill Setup](/hermes/skills/catalog/googlechrome-modern-web-guidance-setup)
- [Hermes Client Web Ui Setup](/hermes/skills/catalog/hermes-client-web-ui-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Copy the 7 skills under `skills/`, not the whole tree. The `.github/skills/` four are maintenance tooling for this repository, and `agent-skill-deploy` in particular is about publishing marketplaces you probably do not run.
- Read `references/compatibility.md` before the code, not after it fails. The WebMCP file records which Chrome milestone changed which call, and it is the fastest way to tell a browser regression from your own bug.
- Ask which annotation each tool should carry. `readOnlyHint` for lookups, `consequentialHint` for anything that spends money or deletes data, `untrustedContentHint` when output echoes scraped text, and `debugging` only for tools aimed at developer tooling.
- Test the tool lifecycle, not just the first call. register, route change, abort, re-register, and a duplicate name are where these integrations usually break.
- If the target is a headless Hermes browser session, plan for the fallback early. WebMCP needs a visible secure window, so the DOM path or a server-side tool is still the only option there.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
