---
title: "OpenTelemetry Agent Skills - Instrumentation and SDK Setup"
description: "ollygarden/opentelemetry-agent-skills - 2.5K combined installs: vendor-neutral OpenTelemetry SDK, Collector, and semantic convention agent skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ollygarden-opentelemetry-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "opentelemetry", "observability", "instrumentation"]
---

# OpenTelemetry Agent Skills - Setup Guide

**Source:** [ollygarden/opentelemetry-agent-skills](https://www.skills.sh/ollygarden/opentelemetry-agent-skills) via skills.sh - 2.5K combined installs across 29 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 evening sweep)
**GitHub:** [ollygarden/opentelemetry-agent-skills](https://github.com/ollygarden/opentelemetry-agent-skills) - 126 stars, Apache-2.0 license, last pushed Nov 26, 2026, main branch; 20 skill directories under skills/<name>/SKILL.md, each with references/, evals/, or bundled scripts, plus a Go-based reference generator under tools/otel-agent-tools.
**Category:** Observability and Instrumentation (OpenTelemetry)
**Quality Tier:** 🟠 Orange - 20 of 29 listings sampled: eight pass all three checks, four carry a Fail (otel-declarative-config, otel-telemetrygen, otel-browser, otel-profiles), and eight carry Warn cells only.

ollygarden/opentelemetry-agent-skills is OllyGarden's vendor-neutral collection of agent skills that give coding agents accurate, current OpenTelemetry knowledge, published under the Apache-2.0 license. The skills target Claude Code, Cursor, Codex, and GitHub Copilot and follow the Agent Skills specification, so they work with any agent that supports it. The README describes the set as non-opinionated by design and built for token-efficient retrieval: small fetch tables, lookup indexes, and scripts that point at upstream sources of truth instead of copying docs into context.

Twenty skill directories live under skills/<name>/SKILL.md: seven language-specific skills (otel-go, otel-java, otel-js, otel-python, otel-dotnet, otel-ruby, otel-browser) and thirteen language-agnostic skills, including otel-collector, otel-declarative-config, otel-ottl, otel-sdk-versions, otel-semantic-conventions, and otel-weaver. The install index outruns the tree: ten indexed names have no matching directory in the current tree (telemetrygen, semantic-conventions, sdk-versions, sdk-setup, manual-instrumentation, span-events-to-logs-migration, go-sdk, otel-component-telemetry, otel-components-telemetry, weaver), while otel-cicd sits in the tree but carries no indexed install count.

## Installation

The README documents several install paths. The skills.sh CLI installs the whole suite into the detected agent's skills directory:

```bash
npx skills add https://github.com/ollygarden/opentelemetry-agent-skills
```

A single skill installs by pointing at its folder:

```bash
npx skills add https://github.com/ollygarden/opentelemetry-agent-skills/tree/main/skills/otel-go
```

Claude Code registers the repository as a plugin marketplace, then installs a skill by name:

```
/plugin marketplace add ollygarden/opentelemetry-agent-skills
/plugin install otel-go@opentelemetry-agent-skills
```

For Cursor, Codex, GitHub Copilot, and other agents, pass the agent with -a:

```bash
npx skills add ollygarden/opentelemetry-agent-skills -a cursor
```

Each merge to main that changes skills/ publishes @ollygarden/opentelemetry-agent-skills@1.0.<run> to GitHub Packages without evals/; installing it needs a token with read:packages and an .npmrc pointing at the GitHub Packages registry.

## What It Provides

skills.sh publishes per-skill install counts for all 29 indexed listings. The band is flat rather than top-heavy: the most-installed skill (otel-semantic-conventions) sits at 178, and the 29 listings total 2,525 installs. The 18 skills at 50 or more installs are listed below; the remaining 11 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| otel-semantic-conventions | 178 | semantic convention lookup and naming: select released groups, attributes, and span naming rules, and check which semconv version a language SDK exposes |
| otel-collector | 175 | author, review, or debug Collector component YAML (receivers, processors, exporters, connectors, extensions) with config keys, defaults, and stability levels |
| otel-sdk-versions | 162 | look up the latest compatible released SDK, package, or component version across languages, the Collector, the config schema, semantic conventions, and Weaver |
| otel-declarative-config | 159 | configure SDK providers (tracer, meter, logger) via declarative YAML: OTLP exporters, sampling, and otel config files |
| otel-go | 156 | OpenTelemetry in Go: SDK setup, API surface, contrib libraries, compile-time zero-code instrumentation (otelc), performance, breaking changes |
| otel-js | 149 | OpenTelemetry in Node.js, JavaScript, and TypeScript: NodeSDK, declarative YAML config, auto-instrumentations, and ESM vs CJS imports |
| otel-ottl | 148 | author and debug OTTL statements for transform, filter, tail_sampling, and routing in the Collector |
| otel-telemetrygen | 147 | build safe, version-pinned telemetrygen commands for synthetic OTLP traces, metrics, and logs to verify pipelines |
| otel-java | 141 | OpenTelemetry in Java: Javaagent zero-code, Spring Boot Starter, autoconfigure SDK, BOM management, and sensitive-data redaction |
| otel-span-events-to-logs-migration | 141 | migrate span events (AddEvent, RecordException) to the Logs API following the OTEP 4430 migration plan |
| otel-browser | 138 | browser and RUM mechanics for SPAs and MPAs: sdk-trace-web, WebTracerProvider, Web Vitals, sessions, and frontend-to-backend correlation |
| otel-python | 131 | OpenTelemetry in Python: SDK setup, declarative config, zero-code and auto-instrumentation, performance, breaking changes |
| otel-weaver | 127 | author a Weaver registry, write Jinja2 templates, generate bindings, and wire registry check/generate/diff into CI |
| otel-collector-builder | 125 | build custom Collector distributions with OCB: builder manifests, component and provider versions, and CI/Docker builds |
| otel-dotnet | 118 | OpenTelemetry in .NET: DI/builder SDK setup, ActivitySource and Meter, CLR-profiler zero-code, and contrib packages |
| otel-telemetry-emissions | 95 | look up which spans, metrics, logs, and attributes a Collector component or SDK package emits at a given version |
| otel-upgrade | 84 | assess OpenTelemetry package and Collector upgrades: version selection, compatibility, required changes, and rollout risk |
| otel-ruby | 56 | OpenTelemetry in Ruby: SDK and Bundler setup, manual tracing, metrics and logs, and Rails/Rack/Sinatra/Sidekiq instrumentation |

The remaining 11 indexed listings range from 1 to 32 installs.

## Why This Matters for Hermes Agents

OpenTelemetry is the vendor-neutral standard for traces, metrics, logs, and profiles, and this suite encodes its setup and migration knowledge into skills an agent can run. The seven language-specific skills each bundle task-focused references plus breaking-change audits, so an agent adding or debugging instrumentation gets version-accurate guidance rather than stale trained knowledge. otel-semantic-conventions and otel-sdk-versions are the lookup skills that keep attribute naming and package versions pinned to upstream releases. otel-collector and otel-declarative-config cover the two configuration surfaces (Collector component YAML and SDK declarative YAML), while otel-telemetrygen and otel-telemetry-emissions support verification: generate synthetic traffic and check exactly what a component emits at a given version. otel-span-events-to-logs-migration and otel-weaver target migrations, from span events to logs and from hand-maintained constants to Weaver codegen. The set is designed for token-efficient retrieval and points at upstream sources of truth, which suits non-interactive agent use. Four of the sampled skills carry a Fail verdict (see Security), so review those before production use.

## Usage

| You say | What happens |
|---|---|
| Set up OpenTelemetry in my Go service | Uses otel-go for SDK setup, contrib libraries, and zero-code otelc instrumentation |
| Configure my OpenTelemetry Collector | Uses otel-collector for receiver, processor, exporter, and connector YAML |
| Which semantic convention should I use | Uses otel-semantic-conventions for released groups, attributes, and span naming rules |
| Instrument my Node.js app | Uses otel-js for NodeSDK setup, declarative config, and auto-instrumentation |
| What is the latest compatible SDK version | Uses otel-sdk-versions to look up released SDK, Collector, and Weaver versions |
| Send sample traces to my collector | Uses otel-telemetrygen to build safe, version-pinned synthetic OTLP traffic |
| Migrate my span events to logs | Uses otel-span-events-to-logs-migration to follow the OTEP 4430 plan |

## Verification

Confirm the README and representative skill bodies resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/ollygarden/opentelemetry-agent-skills/main/README.md | head -60
curl -sL https://raw.githubusercontent.com/ollygarden/opentelemetry-agent-skills/main/skills/otel-go/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/ollygarden/opentelemetry-agent-skills/main/skills/otel-semantic-conventions/SKILL.md | head -40
```

All three URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Fail and Warn verdicts noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| otel-semantic-conventions | Pass | Pass | Pass |
| otel-collector | Pass | Pass | Warn |
| otel-sdk-versions | Pass | Pass | Pass |
| otel-declarative-config | Pass | Fail | Fail |
| otel-go | Pass | Pass | Pass |
| otel-js | Pass | Pass | Warn |
| otel-ottl | Pass | Pass | Pass |
| otel-telemetrygen | Pass | Pass | Fail |
| otel-java | Pass | Pass | Warn |
| otel-span-events-to-logs-migration | Pass | Pass | Pass |
| otel-browser | Pass | Warn | Fail |
| otel-python | Pass | Pass | Warn |
| otel-weaver | Pass | Pass | Pass |
| otel-collector-builder | Pass | Pass | Pass |
| otel-dotnet | Pass | Pass | Warn |
| otel-telemetry-emissions | Pass | Pass | Pass |
| otel-upgrade | Pass | Pass | Warn |
| otel-ruby | Pass | Pass | Warn |
| otel-profiles | Pass | Pass | Fail |
| telemetrygen | Warn | Pass | Pass |

Across the 20 sampled skills there are 46 Pass, 9 Warn, and 5 Fail cells. Eight skills pass all three checks; four carry a Fail (otel-declarative-config, otel-telemetrygen, otel-browser, otel-profiles) and eight carry Warn cells only.

## Limitations

- Snapshot data, verified Nov 26, 2026: 2,525 combined installs across 29 indexed listings; 126 GitHub stars; Apache-2.0 license; last pushed Nov 26, 2026. Counts drift over time.
- The install index outruns the tree: ten indexed names (telemetrygen, semantic-conventions, sdk-versions, sdk-setup, manual-instrumentation, span-events-to-logs-migration, go-sdk, otel-component-telemetry, otel-components-telemetry, weaver) have no matching directory in the current skills/ tree, while otel-cicd sits in the tree but carries no indexed install count.
- skills.sh sampled 20 of the 29 indexed listings; the other nine carry no published verdict.
- The sample includes five Fail cells (Snyk Fail on otel-declarative-config, otel-telemetrygen, otel-browser, otel-profiles, and a Socket Fail on otel-declarative-config), so the suite tiers Orange rather than Green.
- Install counts are flat: the top listing sits at 178 and no skill dominates the 2,525-install total, so per-skill counts are a weak ranking signal.
- The npm distribution publishes each main-branch change to GitHub Packages without evals/ and requires a read:packages token.

## Related

[Datadog Agent Skills - Observability & Monitoring Setup](/hermes/skills/catalog/datadog-agent-skills-setup) | [Monitoring Expert - Observability & Monitoring Setup](/hermes/skills/catalog/monitoring-expert-setup) | [Langfuse Agent Skills - LLM Observability Setup](/hermes/skills/catalog/langfuse-agent-skills-setup) | [Sentry AI Monitoring - Agent Error Tracking Setup](/hermes/skills/catalog/sentry-ai-monitoring-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with otel-semantic-conventions and otel-sdk-versions to pin attribute names and package versions before touching instrumentation code.
- Install a single language skill with npx skills add .../tree/main/skills/otel-go when you only need one SDK.
- Pair otel-telemetrygen with otel-collector to verify a pipeline end to end before wiring real services.
- Use otel-upgrade plus the per-language breaking-changes references to assess an SDK or Collector upgrade's rollout risk.
- Re-check the security pages on skills.sh for the four Fail-carrying skills (otel-declarative-config, otel-telemetrygen, otel-browser, otel-profiles).

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
