---
title: "Dash0 OpenTelemetry Skills - Setup Guide"
description: "dash0hq/agent-skills on skills.sh: 3.1K combined installs; four OpenTelemetry skills for instrumentation, semantic conventions, Collector and OTTL."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dash0-otel-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "opentelemetry", "observability", "telemetry", "collector"]
---

# Dash0 OpenTelemetry Skills - Setup Guide

**Source:** [dash0hq/agent-skills](https://www.skills.sh/dash0hq/agent-skills) via skills.sh - 3.1K combined installs across 4 indexed listings; first seen 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 99 stars, Apache-2.0 via LICENSE, `main` branch, last pushed 2026-11-03, 4 SKILL.md files under `skills/<name>/` with a `rules/` tree beside each, plus plugin manifests for Claude Code, Cursor and Tessl
**Category:** Observability: OpenTelemetry instrumentation, semantic conventions, Collector pipelines and OTTL transformations
**Quality Tier:** 🟢 Production - Apache-2.0, Pass on all twelve sampled scanner verdicts, vendor-neutral output over standard OTLP, and a rule tree that tracks the upstream specification.

Dash0 is an observability vendor, and this repository is the unusual case of a vendor publishing skills that produce standard OpenTelemetry rather than its own agent format. The README states the position directly: the skills are built around the OpenTelemetry specification, the output is OTLP that any compatible backend can ingest, and the guidance follows the upstream Semantic Conventions for attribute, span and metric naming. Dash0 also credits Tessl with improving the skills and publishes them to the Tessl registry.

Four skills cover the work in layers: instrumenting an application, choosing the attribute names that instrumentation writes, configuring the Collector that receives it, and writing OTTL expressions that transform or redact it in flight. The split matters because those four jobs fail independently. A service can emit correct spans with wrong attribute names, and a Collector can be correctly configured to forward telemetry that is unusable downstream.

The repository carries 60 files under `skills/` and 238 under `evals/`. The `skills/` tree is markdown rules only, with no scripts and no executable payload; the Go code, Dockerfiles and scenario harness live in `evals/` and are not part of what an install puts on disk. Each skill is written as an advisory: the instrumentation skill declares `workflow_type: advisory` in its frontmatter, so the agent reads guidance and applies it rather than running a fixed procedure.

## Installation

The universal route is the skills CLI, which works with any Agent Skills-compatible tool. The README gives the all-at-once form and a single-skill form:

```bash
npx skills add https://github.com/dash0hq/agent-skills --all
# or a single skill:
npx skills add https://github.com/dash0hq/agent-skills --skill otel-semantic-conventions
```

Agent runtimes that embed the skills instead of installing them into a tool can take the npm package, which ships the `skills/` trees verbatim and no code:

```bash
npm install @dash0/agent-skills
```

The package README resolves a skill directory at runtime with `createRequire`, pointing at `@dash0/agent-skills/package.json` and joining `skills/otel-instrumentation` beside it. That path shape is stable because the package carries the directory tree unchanged.

Claude Code has a plugin route through the Dash0 marketplace:

```text
/plugin marketplace add dash0hq/claude-marketplace
/plugin install dash0-agent-skills@dash0
```

Codex, Cursor, Copilot, Gemini CLI, OpenCode, Antigravity, Openclaw and Tessl each get a block in `INSTALL.md`. The Codex and OpenCode block is a clone into the cross-client discovery path:

```bash
git clone https://github.com/dash0hq/agent-skills.git ~/.agents/skills/dash0-agent-skills
```

Cursor uses `~/.cursor/skills/dash0-agent-skills`, Gemini CLI uses `gemini extensions install https://github.com/dash0hq/agent-skills`, and Tessl uses `tessl install dash0/agent-skills`. All of them end with the same four directories under `skills/`, because the skill content is the same and only the discovery path changes.

One repository addition is worth wiring if you use Claude Code in CI. The README suggests a `CLAUDE.md` at the project root stating that the project uses OpenTelemetry and that instrumentation work should follow the installed `dash0hq/agent-skills` guidance. Claude Code loads that file at session start, which makes the skills apply in headless pipelines as well as interactive sessions.

## What It Provides

The threshold for this guide is zero installs, so all 4 indexed listings appear below with the install integers exactly as skills.sh reports them:

| Skill | Installs | Use For |
|---|---|---|
| otel-instrumentation | 1,011 | Configuring trace spans, custom metrics, log exporters and sampling, including auto-instrumentation for Node.js, Go, Python, Java, .NET, Ruby, PHP, browsers and Next.js |
| otel-semantic-conventions | 725 | Selecting, applying and reviewing attribute names, span names, span kinds and status codes, including migration between convention versions |
| otel-collector | 692 | Configuring receivers, processors, exporters and pipelines, and deploying the Collector to Kubernetes or Docker with telemetry forwarded to any OTLP backend |
| otel-ottl | 629 | Writing and debugging OTTL expressions for transform and filter processors, including redaction, enrichment, sampling policies and routing |

The four listings clear the threshold, so nothing falls below it. The install order also matches the order the work happens in, which is rare enough to note: instrumentation first at 1,011, then the naming layer at 725, then the Collector at 692, then OTTL at 629.

The instrumentation skill is the largest of the four at 26 files. Its `rules/` tree splits into signal rules (`telemetry.md`, `spans.md`, `metrics.md`, `logs.md`, `resources.md`), safety rules (`sensitive-data.md`, `capture-database-query-parameters.md`), a validation rule and a dependency check, plus ten SDK files under `rules/sdks/` for browser, .NET, Go, Java, Next.js, Node.js, PHP, Python, Ruby and Scala. Note that Scala has a rule file and does not appear in the README's platform list, so the rule tree runs slightly ahead of the documentation.

The collector skill carries 16 files. The rules cover receivers, processors, exporters, pipelines, sampling, custom distributions and RED metrics, with a `rules/deployment/` subtree for the Collector Helm chart, the OpenTelemetry Operator, the Dash0 Operator and raw manifests. The OTTL skill carries 8 files, including a function reference, patterns, cardinality, enrichment and a dedicated `redaction.md`. The semantic conventions skill is the smallest at 5 files and covers attributes, versioning, and one Dash0-specific file for derived attributes and feature dependencies.

## Why This Matters for Hermes Agents

An agent that adds observability to a service is writing two things at once: code that emits telemetry, and the attribute names that make that telemetry queryable two years later. The first is easy and the second is where most of the value sits, which is why the semantic conventions skill exists as a separate install rather than a section inside the instrumentation skill.

The failure mode these skills address is silent. The README states it plainly: when conventions are missing or inconsistent, service maps, operation grouping, error tracking and cross-service queries degrade with no errors, just incomplete data and fragmented views. An agent asked to add tracing will happily invent `http.status` where the convention is `http.response.status_code`, and nothing breaks until someone tries to build a dashboard on it.

The second fit is that the work is configuration with a large search space. Collector pipelines have memory limiters, batchers, resource detection, retry and queue settings, and the order of processors changes the result. The `rules/processors.md` file states that ordering determines execution order and that incorrect ordering causes memory exhaustion or data loss, then shows the correct list and the broken one side by side.

The third is redaction. The OTTL skill has a dedicated redaction rule file, and the instrumentation skill has `sensitive-data.md` and `capture-database-query-parameters.md`. Those are the two places where an agent adding telemetry can leak credentials, customer identifiers or query text into a backend, and having the rules as files means the agent reads a policy instead of guessing.

The honest counterweight: these skills advise, they do not operate. Nothing in the four installs starts a Collector, validates a running pipeline or checks whether your spans actually landed in the backend. They make an agent better at writing the configuration, and the verification is still yours.

## Usage

| You say | What happens |
|---|---|
| "Add OpenTelemetry instrumentation to my app" | Picks the SDK rule for the language in the tree, sets up the SDK and exporter, adds resource attributes for service identity and environment, then wires context propagation so spans join into one trace |
| "My traces are broken, spans show up as separate roots instead of a connected trace" | Works from the context propagation rules for the detected runtime and the server correlation guidance for the browser case, where the fix is usually a missing trace header rather than a broken exporter |
| "Set up a Collector pipeline that forwards to Dash0" | Builds the service section with an OTLP receiver, a batch and memory limiter in the correct order, and an OTLP exporter with authentication, retry and queuing, then picks a deployment shape from the Helm chart, Operator or raw manifest rules |
| "Write an OTTL expression to redact credit card numbers from log bodies" | Uses `rules/redaction.md` for the statement shape, the target context for log bodies and the pattern matching functions, with the cost of regex over every log record called out |
| "Make sure my HTTP server spans have the right attributes" | Checks the span rules and the attribute registry for the exact `http.*` names, span kind and status mapping, and moves span names onto the low-cardinality route template rather than the raw path |
| "Help me fix high-cardinality metrics that are blowing up my costs" | Uses the cardinality rules in both the instrumentation and OTTL skills: identify the offending attribute, drop or hash it in the Collector, and prefer bucket boundaries over unbounded attribute values |
| "Deploy the Collector to Kubernetes" | Chooses between the Collector Helm chart, the OpenTelemetry Operator, the Dash0 Operator and raw manifests using `rules/deployment/`, including the agent versus gateway decision |

## Verification

The skill layout is `skills/<name>/SKILL.md`, so raw paths carry the skill name twice. This one returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/dash0hq/agent-skills/main/skills/otel-instrumentation/SKILL.md | head -20
```

It opens with YAML frontmatter holding `name: 'otel-instrumentation'`, the full description with its trigger phrases, `license: Apache-2.0`, and a `metadata` block with `author: dash0`, `version: '2.0.0'` and `workflow_type: 'advisory'`. Below the delimiter the heading is `# OpenTelemetry Instrumentation Guide`. The other three skills carry the same shape with their own versions, and `otel-ottl` has no `license` key in its frontmatter, so a missing key there is not a download failure.

The rules are what make the skill useful, so check that one arrives:

```bash
curl -fsSL https://raw.githubusercontent.com/dash0hq/agent-skills/main/skills/otel-ottl/rules/redaction.md | head -5
```

That should return the redaction rule heading and the start of its OTTL guidance. A 404 means the `rules/` layout moved and every relative reference inside the skill body is broken.

The listing count is a one-line check against the repository:

```bash
curl -fsSL "https://api.github.com/repos/dash0hq/agent-skills/git/trees/main?recursive=1" | grep -c '"path": ".*SKILL.md"'
```

That returns 4, which matches the four indexed listings exactly. There is no page-cap problem on this repository.

After the Codex or OpenCode clone, confirm the skills landed one level inside the clone rather than at its root:

```bash
test -f ~/.agents/skills/dash0-agent-skills/skills/otel-collector/SKILL.md && echo ok
```

For an npm install, resolve the package path and list the directories beside it, which should show the same four names.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| otel-instrumentation | Pass | Pass | Pass |
| otel-semantic-conventions | Pass | Pass | Pass |
| otel-collector | Pass | Pass | Pass |
| otel-ottl | Pass | Pass | Pass |

All twelve verdicts are Pass, and the install is markdown: the `skills/` tree is 60 files of rules and reference text with no scripts, no install hooks and no network calls of its own. The Go programs and Dockerfiles in the repository sit under `evals/`, which is the maintainers' scenario harness and not part of what `npx skills add` or the npm package puts in front of an agent.

What the skill writes into a codebase is the real surface. The instrumentation skill adds SDK initialisation, exporter configuration, resource attributes and span or metric calls to application source, and it may edit build files to add packages. The collector and OTTL skills write YAML: the Collector config carries receiver endpoints, exporter endpoints and credentials, and processors can rewrite or drop telemetry for every service behind that Collector. Review those diffs the way you would review a change to a logging library, because that is what they are.

Telemetry leaves the machine. Whatever exporter the agent configures decides where traces, metrics and logs go, and the default path is OTLP over gRPC or HTTP to an endpoint taken from configuration or an environment variable. A Collector deployed with an open OTLP receiver and no auth accepts telemetry from anything that can reach the port, and an exporter pointed at the wrong host ships production data to someone else's backend. Pin the endpoint explicitly, keep the receiver on a private network, and set `insecure: true` only on a hop you control.

Attribute content is the other half. Spans and logs routinely pick up URLs with query strings, user identifiers, email addresses, SQL text and request headers, and the instrumentation skill's `sensitive-data.md` and `capture-database-query-parameters.md` rules exist because of it. Read those two before pointing an agent at a production service, and use the OTTL redaction rule as the enforcement layer rather than trusting every call site to be careful.

The plugin and npm routes add a supply-chain step rather than a code surface. `/plugin marketplace add dash0hq/claude-marketplace` trusts a third-party marketplace, and `npm install @dash0/agent-skills` pulls a published tarball, so pin a version and read the diff between releases if the skills are part of a compliance path.

## Limitations

- Snapshot data, verified 2026-11-09: 3,057 combined installs across 4 indexed listings; 99 GitHub stars; Apache-2.0; last pushed 2026-11-03. Counts drift over time.
- Adoption is small relative to the other observability skills in this catalog: 3,057 installs against 99 stars means the numbers come from a narrow base, and four listings give no second source to cross-check them.
- The skills are advisory markdown. They do not run a Collector, validate a live pipeline, or confirm that spans reached a backend, so every claim an agent makes about working telemetry still needs an external check.
- Vendor-neutral in output, Dash0-maintained in authorship. Two files are Dash0-specific by design: `rules/dash0.md` in the semantic conventions skill covers derived attributes and feature dependencies, and `rules/deployment/dash0-operator.md` covers a Dash0 deployment path. The guidance is portable, the examples lean toward one backend.
- The rule tree tracks a moving specification. Semantic conventions carry stability levels and rename attributes between versions, so a rule that is correct at one commit can name an attribute that has since been replaced. Pin a commit if you need reproducible output.
- Documentation drift is present in small ways: the README platform list omits Scala, which has a rule file at `rules/sdks/scala.md`, and the README describes skills as instructions and scripts while the installed tree contains no scripts at all.

## Related

- [Datadog Agent Skills - Observability & Monitoring Setup](/hermes/skills/catalog/datadog-agent-skills-setup)
- [Monitoring Expert - Observability & Monitoring Setup](/hermes/skills/catalog/monitoring-expert-setup)
- [Langfuse Agent Skills - LLM Observability Setup](/hermes/skills/catalog/langfuse-agent-skills-setup)
- [Arize Phoenix Skills - LLM Observability for Agents](/hermes/skills/catalog/arize-phoenix-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install all four, not just the instrumentation skill. The naming rules in the semantic conventions skill are what make the spans queryable, and they are the cheapest of the four to apply.
- Answer questions about attribute names from `rules/attributes.md` rather than from the model's memory. Attribute renames across convention versions are exactly the kind of detail a model recalls from an older version.
- For a Collector problem, name the signal first (traces, metrics or logs) and then the component. The `rules/pipelines.md` file is organised per signal, and a mixed answer is usually a misread of which pipeline is at fault.
- Put `memory_limiter` first in the processor list of every pipeline. `rules/processors.md` marks that ordering GOOD and the version with the limiter after another processor BAD, and the failure it prevents is the Collector running out of memory under load.
- Reach for OTTL redaction at the Collector rather than editing every call site. One `redaction.md` pattern covers all services behind that Collector, and it can be audited in one file instead of in a hundred.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
