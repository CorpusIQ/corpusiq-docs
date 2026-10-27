---
title: "Pydantic Skills - Logfire and Pydantic AI Suite Setup"
description: "Pydantic's official suite: 21.2K combined installs. Logfire instrumentation, telemetry queries, evals, and Pydantic AI agent patterns."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/pydantic-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-27"
tags: ["hermes skill", "agent skill", "skill setup", "pydantic", "logfire", "llm observability"]
---

# Pydantic Skills - Setup Guide

**Source:** [pydantic/skills](https://www.skills.sh/pydantic/skills) via skills.sh - 21.2K combined installs across 23 indexed listings; first documented 2026-10-27 (Oct 27 morning sweep)

**GitHub:** [pydantic/skills](https://github.com/pydantic/skills) - 145 stars, MIT, branch main, 43 skill directories in two trees: 21 standalone skills under `skills/`, mirrored into 22 packaged copies under `plugins/<plugin>/skills/` for the Claude Code, Codex and Cursor marketplaces

**Category:** Python data validation and LLM observability

**Quality Tier:** 🟡 Beta - maintained by the vendor, 145 stars, 23 indexed listings against 43 in-tree skill directories

Pydantic Services ships this repository as its first-party answer to agent tooling for the stack it owns. It is not a general purpose skill collection. Everything in it serves one of three surfaces: Pydantic for data validation, Pydantic AI for building LLM agents, and Logfire for the traces, logs and evals those agents produce. The repository packages that material as five host plugins (logfire, logfire-exporter, ai, pydantic-ai-harness, pydantic) for Claude Code, Codex and Cursor, and as standalone `SKILL.md` files that follow the agentskills.io layout for any other agent.

The interesting part is the division of labour inside the suite. `logfire-setup` is a router, not an installer: it inspects the request and hands off to a specialist for application instrumentation, infrastructure metrics, evals, frontend observability, Gateway routing or coding-agent capture. Each specialist then owns its own auth, configuration and verification steps, which is why the skill set reads as a small operating procedure rather than a pile of documentation. A separate family of nine `migrating-*` skills covers moving an existing agent codebase from LangChain, the OpenAI Agents SDK, Vercel AI SDK, Google ADK, Claude Agent SDK, Mastra, Agno, Pi or Deep Agents over to Pydantic AI.

## Installation

The README documents three host paths and one cross-agent path. Claude Code first, adding the repository as a plugin marketplace and then installing the plugins you want:

```bash
claude plugin marketplace add pydantic/skills
claude plugin install logfire@pydantic-skills
claude plugin install ai@pydantic-skills
claude plugin install pydantic-ai-harness@pydantic-skills
claude plugin install pydantic@pydantic-skills
```

Codex uses the same marketplace with a different command, then the plugin UI:

```bash
codex plugin marketplace add pydantic/skills
```

Cursor installs the Logfire plugin from a local clone. The README snippet copies the plugin into the local plugins directory and then reloads the window:

```bash
git clone https://github.com/pydantic/skills.git
mkdir -p ~/.cursor/plugins/local
cp -R skills/plugins/logfire ~/.cursor/plugins/local/logfire
```

For any other agent, the `skills/` directory is the install source, and the skills.sh CLI is the generic path:

```bash
npx skills add pydantic/skills
```

Each directory under `skills/` is self contained, with one `SKILL.md` plus a `references/` folder the agent opens only when a task reaches that depth, so copying a single directory into your agent's skills folder is equivalent to a CLI install of that one skill.

For the Logfire plugin specifically, run `/logfire:connect` inside the host once. It walks through MCP OAuth and, optionally, native session telemetry. `/logfire:status` checks MCP access, native telemetry configuration and delivery evidence separately, and `/logfire:disconnect` stops session capture without removing MCP or the skills.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| building-pydantic-ai-agents | 5,696 | Building LLM agents with Pydantic AI: tools, capabilities including on-demand loading, workspaces, structured output, streaming, testing and multi-agent patterns. |
| pydantic-ai-harness | 2,579 | Extending those agents with harness capabilities: the Coder coding agent, file and shell tools in local or sandboxed workspaces, Code Mode, sub-agents and planning, memory, context compaction, guardrails and spend limits. |
| logfire-instrumentation | 2,316 | Adding Logfire traces, logs, metrics and AI spans to application code, in Python, JS/TS and Rust, including the ordering of `configure()` and `instrument_*()` calls that silently drops traces when wrong. |
| pydantic | 2,169 | Data validation and serialization with Pydantic models: field constraints, model hierarchies and subclasses, custom validators, and modelling untrusted external data such as HTTP API payloads. |
| logfire-query | 1,907 | Querying and analyzing Logfire telemetry in chat: traces, logs, spans, metrics, error counts, slowest traces and root cause analysis, or adding query capability to application code. |
| logfire-ui | 1,601 | Opening or returning Logfire project pages, live views, trace links and Explore filters directly by URL, without querying telemetry first. |
| logfire-setup | 564 | Routing a broad "set up Logfire" request to the right specialist surface: application instrumentation, infrastructure, evals, frontend, Gateway or coding agents. |
| logfire-evals | 563 | Offline evaluation with `pydantic_evals` or `logfire/evals`: test datasets, evaluators, LLM judges, span based checks, and redirecting an existing Braintrust suite to Logfire. |
| logfire-infrastructure | 546 | Monitoring hosts, Docker containers, Kubernetes clusters, database and queue servers, and cloud metrics through the OpenTelemetry Collector, with no application code changes. |

The remaining 14 indexed listings range from 73 to 380 installs. They are the nine `migrating-*` skills (313 to 323 installs, plus `migrating-deep-agents-to-pydantic-ai-harness` at 84), `instrumentation` at 380, and four Logfire edge-case skills: `logfire-codex-connection` (79), `logfire-frontend` (75), `logfire-coding-agents` (75) and `logfire-gateway` (73).

## Why This Matters for Hermes Agents

Observability is the part of agent work that fails quietly. A misordered `configure()` call or a missing instrumentation extra does not raise an error, it produces an empty trace list, and the agent then reports that the application is healthy. `logfire-instrumentation` exists specifically because that failure mode is common: it authenticates against the exact project first, detects the language and framework from the repository, then applies the instrumentation in the order Logfire expects.

Agent frameworks have the same problem one level up. Pydantic AI has moved quickly, and generic advice about building an agent from memory drifts from the current API for tools, capabilities, streaming and testing. `building-pydantic-ai-agents` carries the current patterns, and `pydantic-ai-harness` covers the layer above it: coding, sandboxing, delegation, memory, context compaction and spend limits, each of which is a decision an agent normally improvises.

The suite is also unusually explicit about its own boundaries. Skills declare what they are not for, route to the correct sibling, and in several cases refuse to proceed until authentication and project selection are confirmed. For a Hermes agent running unattended, that reduces the class of mistake where the agent instruments one project and reports on another.

Finally, the migration family is a practical lever. Rewriting an existing LangChain or OpenAI Agents SDK codebase into Pydantic AI is a task an agent can do badly at length; having nine skill documents that describe the target shapes means the conversion follows a written procedure rather than a guess.

## Usage

| You say | What happens |
|---|---|
| "Add Logfire tracing to this FastAPI app" | logfire-instrumentation confirms the Logfire project with `whoami`, detects FastAPI and the instrumentable libraries, then applies `configure()` before the framework instrumentation and picks the right extras. |
| "Why was checkout slow yesterday afternoon" | logfire-query classifies the prompt as a query, searches the traces and spans for the window, and returns the analysis in chat instead of a link. |
| "Open the live view for the payments service" | logfire-ui builds the Logfire URL for the project and time range and opens it without running a query first. |
| "Build an agent with streaming output and tool calls" | building-pydantic-ai-agents scaffolds the agent with tools, capabilities, streaming events and a test for the behavior. |
| "Let the agent edit files and run shell commands safely" | pydantic-ai-harness wires the coding stack: file and shell tools in a sandboxed workspace, sub-agents, guardrails and spend limits. |
| "Evaluate this agent against my test cases" | logfire-evals runs a `pydantic_evals` dataset with evaluators and reports results in Logfire, or redirects an existing Braintrust suite by changing environment variables. |
| "Validate these API payloads with constraints" | pydantic writes the model hierarchy with `Field` constraints and custom validators, and keeps instantiation inside user code on plain classes where validation is not needed. |

## Verification

The repository ships two trees with different roots, so probe the path you plan to use. For the standalone cross-agent skills on main:

```bash
for p in skills/building-pydantic-ai-agents/SKILL.md \
         skills/logfire-instrumentation/SKILL.md \
         skills/pydantic/SKILL.md \
         skills/logfire-query/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/pydantic/skills/main/$p"
done
```

The plugin copies live one level deeper, for example `plugins/ai/skills/building-pydantic-ai-agents/SKILL.md` and `plugins/logfire/skills/logfire-instrumentation/SKILL.md`. Read the two that touch credentials or capture before installing them:

- https://raw.githubusercontent.com/pydantic/skills/main/skills/logfire-instrumentation/SKILL.md
- https://raw.githubusercontent.com/pydantic/skills/main/skills/logfire-setup/SKILL.md

After install, the skills appear in your agent's skills directory, one folder per skill, and the Claude Code plugin exposes the slash commands `/instrument`, `/debug` and `/query` alongside them. `/logfire:status` is the check that matters for the Logfire plugin: it reports MCP access, native telemetry configuration and delivery evidence as three separate answers, so a green MCP result does not imply traces are arriving.

## Security

skills.sh verdicts for the Gen Agent Trust Hub, Socket and Snyk auditors were not sampled for this fire, so every cell below reads Not checked. Open each skill's security page on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| building-pydantic-ai-agents | Not checked | Not checked | Not checked |
| pydantic-ai-harness | Not checked | Not checked | Not checked |
| logfire-instrumentation | Not checked | Not checked | Not checked |
| pydantic | Not checked | Not checked | Not checked |
| logfire-query | Not checked | Not checked | Not checked |
| logfire-ui | Not checked | Not checked | Not checked |
| logfire-setup | Not checked | Not checked | Not checked |
| logfire-evals | Not checked | Not checked | Not checked |
| logfire-infrastructure | Not checked | Not checked | Not checked |

The real risk in this suite is data flow, not code execution. Enabling Logfire telemetry sends traces, logs, model payloads, tool arguments and tool results to a hosted service, and the Logfire plugin README states that full capture can include prompts, code, tool output and secrets inside raw model API bodies, while metadata-only capture excludes message and tool content. Choose the capture policy deliberately for any agent that handles customer data.

Two more boundaries are worth stating. The skills authenticate through the Logfire CLI and can create or use project write tokens, so grant the narrowest scope that satisfies the task and keep the region and project target explicit. And the skill documents themselves instruct agents to treat telemetry as diagnostic data rather than instructions, which is the right posture: a trace containing text that looks like a remediation step is untrusted input.

## Limitations

- Snapshot data, verified 2026-10-27: 21,247 combined installs across 23 indexed listings; 145 GitHub stars; MIT; branch main. Counts drift over time.
- Two trees, one content set: 43 `SKILL.md` directories back 23 indexed listings. The 21 skills under `skills/` are mirrored into `plugins/<plugin>/skills/` for the host marketplaces, except `logfire-codex-connection`, which exists only under `plugins/logfire/skills/`. Install one tree, not both, or you will index the same skill twice.
- `instrumentation` carries 380 installs but has no directory in the current tree. The closest in-tree skill is `logfire-instrumentation`, so the listing reads as a rename rather than a second skill.
- The README's Cross-Agent Skills table lists 12 of the 21 standalone skills. The nine `migrating-*` directories are in the tree and in the install index but not in that table, and the descriptions above for them come from the directory names and their own `SKILL.md` files.
- The Cursor install snippet in the README copies `skills/plugins/logfire`, which does not match the `plugins/logfire` path in the current tree. Check the source path before running the copy.
- The two agent-building skills declare Python 3.11+ in their frontmatter, and the plugin install commands cover Claude Code, Codex and Cursor only. Other agents install from `skills/` and get no slash commands, MCP wiring or hook installation.

## Related

- [Arize Skills - LLM Observability and Evaluation Setup](/hermes/skills/catalog/arize-skills-setup)
- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)
- [Ultracite - Zero-Config Lint Preset Setup](/hermes/skills/catalog/ultracite-skills-setup)
- [Anthony Fu Skills - Vue, Vite and TS Tooling Setup](/hermes/skills/catalog/antfu-skills-setup)

## Pro Tips

- Start with `logfire-setup` and let it route. Installing the six Logfire specialists because they exist costs context on every turn for surfaces you may never touch.
- Authenticate before reading the repository. Every Logfire specialist checks the project target with `whoami` first, and a wrong project from an environment variable is the most common way to lose an hour.
- `logfire-query` and `logfire-ui` are deliberately split. Say "analyze" or "count" when you want an answer, "open" or "link" when you want the UI, or the agent has to ask you which one you meant.
- Read `references/` in the skill you install. The `SKILL.md` carries the routing and the steps, and the long form detail such as collector configuration and auth sequences lives one level down.
- If you are porting from another agent framework, install the matching `migrating-*` skill for the session and remove it after. The target shapes are useful during the rewrite and redundant afterwards.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
