---
title: "OrchestKit - Orchestration and DevOps Skills"
description: "yonatangross/orchestkit: 30.4K combined installs. A Claude Code plugin of 115 skills, 36 agents and 161 hooks for orchestration, devops and release."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/orchestkit-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "orchestration", "devops", "release"]
---

# OrchestKit - Setup Guide

**Source:** [yonatangross/orchestkit](https://www.skills.sh/yonatangross/orchestkit) via skills.sh - 30.4K combined installs across 151 indexed listings; first seen 2026-10-31 (morning sweep)

**GitHub:** [yonatangross/orchestkit](https://github.com/yonatangross/orchestkit) - 300 stars, MIT, branch main, last pushed 2026-10-31; 115 skill directories under `plugins/ork/skills/` plus 7 in `plugins/ork-codex/skills/`, with a build mirror of the same 115 under `src/skills/` and a plugin manifest, hooks registry and 36 agents alongside them

**Category:** Multi-agent orchestration and delivery: planning, devops deployment, review and release gates

**Quality Tier:** 🟡 Yellow - three of five sampled skills Pass all three auditors, but `devops-deployment` carries a Socket Warn and `ork-brainstorm` a Snyk Warn

OrchestKit is a Claude Code plugin, not a skills folder that happens to ship with a plugin: the README counts 115 skills, 36 agents and 161 hooks, and the install is a single `ork` plugin rather than a list of names. The 151 listings on skills.sh come from that catalog, spread across frontend patterns (responsive layout, Zustand, shadcn and Radix, animation), backend and data (LangGraph, distributed systems, database patterns, Alembic and SQLAlchemy), delivery (devops deployment, release management, quality gates, CI sentinel, code review playbook) and product work (PRD writing, market sizing, OKRs, competitive analysis).

The architecture matters more than any single skill. `plugins/ork/skills/` holds the 115 skill directories, `plugins/ork-codex/skills/` holds a 7-skill Codex pack, `src/skills/` mirrors the main set for the build, and the hooks registry in `plugins/ork/hooks/hooks.json` declares 151 global hooks plus 10 skill-scoped ones. Only Claude Code gets the hooks; the README's own host matrix says Cursor gets the same plugin minus the hook scripts, and Codex gets a 6-skill pack, though the directory holds 7. A Hermes profile installing the skills gets the knowledge and none of the automation.

## Installation

The primary route is the Claude Code plugin marketplace, which installs skills, agents and hooks together:

```bash
/plugin marketplace add yonatangross/orchestkit
/plugin install ork
```

Then `/ork:setup`, whose wizard scans the repository, recommends skills and writes MCP configuration. The shell equivalent does the same thing without an interactive session:

```bash
claude plugin marketplace add yonatangross/orchestkit && claude plugin install ork@orchestkit
```

The skills-only route is the skills CLI, and the README is emphatic that it should be the starter 12 rather than the whole catalog:

```bash
npx skills add yonatangross/orchestkit -s devops-deployment -s responsive-patterns -s architecture-decision-record -s ui-components -s rag-retrieval -s agent-orchestration -s brainstorm -s expect -s auto -s review-pr -s fix-issue -s commit
```

The full catalog is one flag less, and comes with a warning in the same paragraph that hundreds of `SKILL.md` files should not be read as hundreds of users:

```bash
npx skills add yonatangross/orchestkit
```

None of those routes knows about Hermes, so the durable install for this profile is a directory copy. Take a subset rather than all 115, since each directory competes for the same routing attention:

```bash
git clone --depth 1 https://github.com/yonatangross/orchestkit.git /tmp/orchestkit
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -r /tmp/orchestkit/plugins/ork/skills/devops-deployment \
      /tmp/orchestkit/plugins/ork/skills/quality-gates \
      /tmp/orchestkit/plugins/ork/skills/code-review-playbook \
      /tmp/orchestkit/plugins/ork/skills/architecture-decision-record \
      /tmp/orchestkit/plugins/ork/skills/agent-orchestration \
      ~/.hermes/profiles/corpusiq/skills/
```

Copy directories, not the repository root: the skills live three levels down, the hooks registry sits beside them and is meaningless without the Claude Code runtime, and `src/skills/` is a duplicate of the same 115 names that would otherwise install twice.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| devops-deployment | 1,565 | CI/CD pipelines, containerisation, Kubernetes deploys and infrastructure as code: GitHub Actions, Docker, Helm and Terraform patterns. |
| responsive-patterns | 1,555 | Responsive React layouts with container queries, fluid typography, `cqi` and `cqb` units, subgrid, intrinsic layout and foldable devices. |
| architecture-decision-record | 1,520 | ADRs in the Nygard format with context, decision, consequences and alternatives, for recording a decision or comparing options before one is made. |
| rag-retrieval | 1,509 | RAG pipelines that stay grounded: embeddings, hybrid search, contextual retrieval, HyDE, agentic and multimodal RAG, query decomposition, reranking and pgvector. |
| ui-components | 1,505 | Accessible component libraries on shadcn/ui and Radix primitives: customising shadcn components, using unstyled Radix parts and laying design system foundations. |
| zustand-patterns | 1,454 | Zustand 5.x state work: slices, middleware, Immer, `useShallow`, persistence, selectors and devtools, with seven patterns and the anti-patterns beside each. |
| agent-orchestration | 1,394 | Agentic loops and multi-agent coordination: building autonomous loops, comparing CrewAI, AutoGen and Swarm, and orchestrating multi-step scenarios. |
| domain-driven-design | 1,340 | DDD tactical patterns for complex domains: entities, value objects, aggregates, domain services, repositories, specifications and bounded contexts, in Python with TypeScript alternatives. |
| memory | 729 | Read-side memory over the knowledge graph: search past decisions, load session context, view decision timelines and render Mermaid graphs. Storing new knowledge belongs to `remember`. |
| security-patterns | 708 | Auth flows, defence in depth, input validation, the OWASP Top 10, LLM safety, PII masking, prompt injection defence and data redaction. |
| langgraph | 363 | LangGraph 1.x Python workflows: state and delta channels, node timeouts and error handlers, supervisor-worker routing, checkpointing, human-in-loop, streaming and subgraphs. |
| write-prd | 319 | Product requirements documents: an eight-section template, user stories with INVEST criteria, acceptance criteria and a go/no-go decision frame. |
| distributed-systems | 285 | Distributed locks, circuit breakers, retry policies, idempotency keys, token bucket rate limiters and the rest of the fault tolerance set. |
| ascii-visualizer | 283 | Listed at 283 installs with no directory in the clone on 2026-10-31. `designs/README.md` describes it as the ASCII visual language behind `/ork:visualize-plan`, and the changelog records it as an ork-creative skill, so the name is real but the files are not in the tree. |
| vite-advanced | 260 | Vite 8 build work: Rolldown-powered builds, `advancedChunks`, the Environment API, plugin authoring, SSR configuration, library mode and build optimisation. |
| quality-gates | 254 | Scoring task complexity from 1 to 5 before starting, escalation workflows when stuck after several attempts, and reviewing code against best practice. |
| monitoring-observability | 250 | Prometheus metrics, Grafana dashboards, Langfuse v4 LLM tracing (`as_type`, `score_current_span`, `should_export_span`), drift detection and cost tracking. |
| code-review-playbook | 249 | Structured review process: conventional comments, language-specific checklists and feedback templates for standardising review practice. |
| multimodal-llm | 237 | Image, audio and video pipelines: transcription, speech generation, AI video (Kling v3, Sora 2, Veo 3.1, Runway Gen-4.5) and multimodal integration patterns. |
| memory-fabric | 237 | How memory retrieval works internally: entity extraction, natural language query parsing, deduplication above 85 percent similarity and cross-reference boosting over recency, relevance and authority. |

The remaining 131 indexed listings range from 22 to 228 installs.

## Why This Matters for Hermes Agents

The value here is process, not trivia. `quality-gates` scores a task before work starts and escalates when three attempts have failed; `code-review-playbook` standardises how a review is written; `architecture-decision-record` forces consequences and alternatives next to every decision; `write-prd` will not let a product request through without acceptance criteria. Those are the skills that change agent behaviour rather than adding facts, and they are the reason a profile can carry the suite without carrying all 115.

The delivery skills cover the seam where agents usually go quiet. `devops-deployment`, `release-management`, `release-checklist`, `ci-sentinel` and `ci-debug` sit at different points on the same pipeline, and `distributed-systems` supplies the primitives (idempotency keys, circuit breakers, token buckets) that a service needs before it is safe to deploy twice. An agent that has read those stops writing a retry loop with no jitter and calling it resilient.

Memory is split four ways on purpose, and the descriptions police the split. `memory` is the read side with subcommands `search`, `load`, `history`, `viz` and `status`; `remember` writes; `memory-fabric` explains retrieval internals; `dream` does cleanup. Each one names the others in its own text. That is unusually disciplined for a memory suite, and it is the difference between an agent that recalls a decision and one that re-litigates it.

The install is heavy, so weigh it. 115 skill descriptions and 161 hook declarations compete for a routing budget, which is exactly why the README recommends a starter 12 and why the copy above takes six names instead of the tree.

## Usage

| You say | What happens |
|---|---|
| "Set up CI for this service" | `devops-deployment` takes the pipeline: GitHub Actions workflow shape, Dockerfile and image build, then Helm or Terraform for the deploy target, in that order. |
| "Should we use Postgres or DynamoDB here" | `architecture-decision-record` produces the ADR with context, options, decision and consequences, so the choice is reviewable instead of remembered. |
| "Our RAG answers are vague" | `rag-retrieval` walks the retrieval chain: chunking and embeddings, hybrid search, reranking, then HyDE or query decomposition before anyone blames the model. |
| "Why does this endpoint double-charge on retry" | `distributed-systems` supplies the idempotency key pattern and the retry policy that goes with it, with the token bucket for the rate limit in front. |
| "Review this PR before I merge" | `code-review-playbook` sets the review structure and `quality-gates` scores complexity, which decides whether the change needs one reviewer or an escalation path. |
| "What did we decide about the auth provider last month" | `memory` searches the decision graph and renders the timeline; a new decision goes to `remember` rather than overwriting the old one. |
| "Write the PRD for the new billing page" | `write-prd` works through the eight sections, turns requirements into INVEST stories and refuses to close without acceptance criteria. |

## Verification

The raw path for the top skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} devops-deployment\n" \
  https://raw.githubusercontent.com/yonatangross/orchestkit/main/plugins/ork/skills/devops-deployment/SKILL.md
```

Expect `200`. After the copy lands, confirm what arrived and which skills have supporting files:

```bash
find ~/.hermes/profiles/corpusiq/skills -maxdepth 2 -name SKILL.md | wc -l
head -6 ~/.hermes/profiles/corpusiq/skills/quality-gates/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/quality-gates
```

The count should match the number of directories you copied, and the header should show `name: quality-gates` with a `description:` that opens "Use when assessing task complexity". A full copy of `plugins/ork/skills/` gives 115 `SKILL.md` files, not the 151 listings this guide counts and not the 246 files a recursive `find` sees in the clone, which double-counts the `src/skills/` mirror.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31). Two Warnings sit in the sample, a Socket Warn on `devops-deployment` and a Snyk Warn on `ork-brainstorm`, while the other three Pass all three auditors - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| devops-deployment | Pass | Warn | Pass |
| animation-motion-design | Pass | Pass | Pass |
| figma-design-handoff | Pass | Pass | Pass |
| dev | Pass | Pass | Pass |
| ork-brainstorm | Pass | Pass | Warn |

The larger question is the hooks, not the skills. `plugins/ork/hooks/hooks.json` declares 151 global hooks and 10 skill-scoped ones, each a `node` command with a timeout between 3 and 120 seconds, bound to `PreToolUse`, `PostToolUse` and lifecycle events, so installing the plugin as a Claude Code plugin means 161 programs run around your tool calls on every session. One of them, `lifecycle/webhook-forwarder`, is registered on every event type with `async: true`; its source says it fans events out to pluggable sinks, a local JSONL file and an optional HTTP remote, signs the payload with HMAC-SHA256 in an `X-CC-Hooks-Signature` header, and is a no-op when no sinks are registered. Read that as: nothing leaves the machine until someone configures a sink, and if someone does, tool-call metadata does.

The skills themselves are markdown, but the repository is not. The clone carries 582 shell scripts, 406 of them test fixtures under `tests/`, plus a TypeScript hook build under `src/hooks/`, a Dockerfile, a Python SDK and an npm package, and 59 of the 115 skill frontmatters pin `compatibility: "Claude Code 2.1.277+."`. A Hermes profile that copies only `plugins/ork/skills/` skips all of that, which is the version of this suite with the smallest blast radius.

## Limitations

- Snapshot data, verified 2026-10-31: 30,386 combined installs across 151 indexed listings; 300 GitHub stars; MIT; last pushed 2026-10-31. Counts drift over time.
- The listings outnumber the skills by a wide margin. 151 listings against 115 directories in `plugins/ork/skills/`, and a recursive count of `SKILL.md` files returns 246 because `src/skills/` mirrors the main set. The README badge says 115 skills, so trust the plugin directory and ignore the arithmetic that a clone suggests.
- At least one listed skill has no files. `ascii-visualizer` sits at 283 installs, inside the required range, with no directory anywhere in the clone; only `designs/README.md` and the changelog mention it. An install of the whole catalog cannot deliver it.
- Install counts are not a ranking of what is maintained. `devops-deployment` leads at 1,565 while `release-management` sits at 215 and `quality-gates` at 254, and the small process skills are the ones that change behaviour most.
- The suite was built for Claude Code. Hooks are Claude-only, the Codex pack covers 7 skills (the README matrix says 6) rather than 115, Cursor gets the plugin without the hook scripts, and the commands are namespaced `/ork:<skill>`, none of which a Hermes profile can use as written.
- Four memory skills overlap by design and will mis-route. `memory`, `remember`, `memory-fabric` and `dream` all concern the same knowledge graph, and only their descriptions keep read, write, internals and cleanup apart.
- The repository root is not the install unit. Copying it wholesale drags in 582 shell scripts, a Dockerfile, SDKs and a duplicate skill tree, none of which the skills need.

## Related

- [Lev Nikolaevich Skills - DevOps and Delivery Setup](/hermes/skills/catalog/levnikolaevich-claude-code-skills-setup)
- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [Claude MPM Skills - 96-Skill Dev Toolchain Collection Setup - Setup Guide](/hermes/skills/catalog/claude-mpm-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the starter 12 the README names before anything else. They were chosen from measured installs and cover the ship loop (`review-pr`, `fix-issue`, `commit`), the plan step (`brainstorm`, `architecture-decision-record`) and the front door (`auto`), which is a working baseline at a tenth of the routing cost.
- Take the process skills even if you take nothing else. `quality-gates`, `code-review-playbook` and `write-prd` are short, opinionated and portable across stacks, and they are the ones that stop an agent declaring victory early.
- Do not install the plugin if you only want the knowledge. `/plugin install ork` brings 161 hooks with it; copying directories into a Hermes profile gets the same markdown without 161 node processes running around every tool call.
- Watch the memory quartet. Route reads to `memory`, writes to `remember` and cleanup to `dream`, and read `memory-fabric` only when the retrieval itself is the bug rather than the answer.
- Diff the badge against the tree before trusting a count. The README's `115` is measured by the repository's own tooling, the clone shows 115 in one place and 246 in another, and skills.sh shows 151 listings; the number you want is the one in the directory you copied.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
