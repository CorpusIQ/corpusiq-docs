---
title: "12-Factor Agents - Engineering Standards for AI Agents"
description: The 12-Factor Agents framework applied to Hermes Agent: mostly deterministic software with LLM steps at the right points, mapped factor by factor.
category: best-practices
tags: [hermes-agent, 12-factor-agents, engineering-standards, production-agents, agent-architecture, deterministic-software, agent-reliability]
last_updated: 2026-09-29
canonical: "https://www.corpusiq.io/docs/hermes/best-practices/12-factor-agents/"
robots: "index,follow"

---

# 12-Factor Agents  --  Production Engineering Standards for AI Agents

Most agent demos are a prompt, a bag of tools, and a loop that runs until the goal is reached. Most agent failures in production happen because exactly that pattern was shipped. The [12-Factor Agents](https://github.com/humanlayer/12-factor-agents) framework by Dex and the HumanLayer team, in the spirit of Heroku's 12-Factor App, replaces the demo loop with twelve concrete engineering principles. The core argument: **production-grade agents are mostly deterministic software, with LLM steps placed at exactly the right points** -- not end-to-end LLM reasoning.

This guide maps each of the twelve factors onto Hermes Agent, showing what "mostly deterministic software" looks like on a real production agent stack, which factors are already native to the architecture, and where the honest gaps remain.

## Overview

The twelve factors below read like a checklist for turning a fragile agent prototype into reliable infrastructure. Each factor answers a specific failure mode:

| Factor | Failure Mode It Fixes |
|---|---|
| 1. Natural language to tool calls | Models improvising actions instead of calling typed tools |
| 2. Own your prompts | Prompts living in vendor UIs, unreviewed and unversioned |
| 3. Own your context window | Context assembled by accident, stuffed until it breaks |
| 4. Tools as structured outputs | Tools returning prose that downstream steps cannot parse |
| 5. Unify execution and business state | The agent's state and the business's state drifting apart |
| 6. Launch/pause/resume with simple APIs | Jobs that cannot be stopped or resumed cleanly |
| 7. Contact humans with tool calls | Escalation as an afterthought instead of a tool |
| 8. Own your control flow | Hidden framework loops the operator cannot inspect |
| 9. Compact errors into context | Blind retries and silent failures |
| 10. Small focused agents | God-agents that fail everywhere at once |
| 11. Trigger from anywhere | Agents that can only run inside a chat window |
| 12. Stateless reducer | State that exists only in memory, lost on restart |

## Factor-by-Factor: Hermes Agent Implementation

### 1. Natural Language to Tool Calls

**The principle:** The model's job is to decide *which* tool to call, not to improvise the action itself. Tools are typed functions with schemas; the runtime executes them deterministically.

**How Hermes implements it:** Every capability -- email, search, files, social publishing, monitoring -- is a schema-validated tool. A model output that says "I will send an email" without a tool call does nothing. The execution path is code, the decision step is the LLM, and the two never blur.

### 2. Own Your Prompts

**The principle:** Prompts are code. They live in version control, they are reviewed, and they change deliberately -- not inside a vendor's settings page.

**How Hermes implements it:** The system prompt, operating constitution, and procedural skills are all versioned files in the agent's profile directory. Changing behavior means changing a file with an audit trail, exactly like changing application code. Prompt drift is a code review problem, not a mystery.

### 3. Own Your Context Window

**The principle:** You decide what enters context for each task. Context is assembled deliberately from the right memory tiers, not accumulated as the conversation scrolls.

**How Hermes implements it:** A layered memory stack serves context on demand: a small hot-facts file for per-turn essentials, semantic peer memory for identity and preferences, an organizational knowledge graph for project relationships, and durable disk for raw archives. Each layer is queried for what the current task needs. This factor is also the product thesis behind CorpusIQ itself: businesses deserve the same discipline -- cited answers pulled from their own sources, in the context window of the AI they already use, instead of an ungoverned prompt loop.

### 4. Tools as Structured Outputs

**The principle:** Tools return structured data -- JSON with schemas -- not prose. Downstream steps consume, validate, and log that data without parsing natural language.

**How Hermes implements it:** Tool results carry typed fields that downstream logic branches on. A social post returns a post ID and status; a lead query returns a structured record. Composing tools means composing schemas, which keeps multi-step workflows parseable end to end.

### 5. Unify Execution and Business State

**The principle:** The agent's execution state and the business's state are the same record. There is one ledger, and both sides read it.

**How Hermes implements it:** Append-only event logs are the single source of truth for what ran, what was posted, what was sent, and which leads are where in the pipeline. The agent's "did I do this" question and the operator's "what happened this week" question are answered from the same files. State is a log, not a variable.

### 6. Launch/Pause/Resume with Simple APIs

**The principle:** Every job can be launched, paused, resumed, and listed from the command line. Long-running work survives restarts and operator intervention.

**How Hermes implements it:** The scheduler exposes plain CLI operations for every scheduled job, and durable task records persist work-in-progress across crashes and restarts. A job is never a black box that must run to completion or die trying.

### 7. Contact Humans with Tool Calls

**The principle:** Escalating to a human is a tool call like any other -- logged, traceable, and triggered by policy -- not a side effect the agent happens to perform.

**How Hermes implements it:** Alerts, approval gates, and handoffs are first-class tools. When a workflow needs a human decision, it calls the escalation tool with structured context, and that call lands in the same audit trail as every other action.

### 8. Own Your Control Flow

**The principle:** No hidden framework loop. The operator can read the sequence of steps, the gates, and the fallbacks, because they are explicit and versioned.

**How Hermes implements it:** Workflows are explicit step sequences with pre-flight gates, kill switches, and fallback chains defined in files. If something goes wrong, the failure mode was written down before it happened, and the operator can point at the exact step.

### 9. Compact Errors into Context

**The principle:** When a step fails, the error is summarized and injected into context so the next attempt is informed -- not a blind retry, not a silent crash.

**How Hermes implements it:** Partially. Error reporting is structured and persistent, and recovery paths are explicit. Formal error compaction -- automatically distilling failure context into the next attempt's context window -- is the top gap on this list. Most failures are handled by policy gates rather than by learned correction.

### 10. Small Focused Agents

**The principle:** One agent, one responsibility. Small agents fail small, are easy to review, and compose into larger systems.

**How Hermes implements it:** Procedural skills are single-responsibility by design, and production work is split into focused agent families -- one for email operations, one for social publishing, one for system health. Each family owns a narrow surface and a shared ledger. A god-agent that does everything is an anti-pattern documented in the [best practices overview](index).

### 11. Trigger from Anywhere

**The principle:** The same workflow can start from a schedule, a webhook, an inbox signal, or an API client. Triggers are external events; agents do not self-loop forever.

**How Hermes implements it:** Workflows are entry-point agnostic. The email operation that runs on a schedule is the same logic an MCP client can invoke directly. Triggering is decoupled from execution, so the agent never needs to run continuously to be alive.

### 12. Stateless Reducer

**The principle:** State is derived by reducing an event log. Given the events, any state can be reconstructed -- so nothing critical lives only in memory.

**How Hermes implements it:** Partially. The operational state is event-sourced in append-only logs, which makes most state reconstructable. Formal reducer semantics -- a single pure function that folds events into state, applied uniformly -- is the second gap. The discipline of "state is a log" is in place; the formalism is not yet complete.

## The Two Honest Gaps

Scoring the stack against all twelve factors, two are partially implemented:

1. **Factor 9 -- Compact errors into context.** Failures are logged and gated, but error context is not yet automatically distilled into the next attempt. This is the highest-leverage reliability improvement available.
2. **Factor 12 -- Stateless reducer.** Event sourcing is the default for operational state, but a uniform reducer formalism across all workflows would make replay and recovery fully mechanical.

Both gaps are engineering work items, not architecture flaws -- the current design supports them without rework.

## Adoption Checklist

Adopting 12-factor discipline for your own agent stack, in order of impact:

1. **Version your prompts like code.** System prompts and skills in git, changes reviewed.
2. **Define tool schemas before agent logic.** Every capability gets a typed contract first.
3. **Log every external action to an append-only ledger.** State is a log.
4. **Wire escalation as a tool call.** Alerts and approvals flow through the audit trail.
5. **Give every job pause/resume semantics.** No black-box runs.
6. **Summarize errors into context.** Replace blind retries with informed retries.
7. **Split god-agents into focused skills.** Small agents fail small.
8. **Make workflows trigger-agnostic.** Schedule, webhook, inbox, and API should be interchangeable entry points.
9. **Derive state from events.** Where you can replay, you can recover.

## FAQ

### What are the 12-Factor Agents?

A production engineering framework for AI agents, in the spirit of Heroku's 12-Factor App, created by Dex and the HumanLayer team. It replaces the "prompt plus tools plus loop" prototype with twelve concrete principles for deterministic, operable, reliable agent software. Full source: [github.com/humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents).

### Which factor matters most for reliability?

Factors 1 through 4 -- natural language to tool calls, own your prompts, own your context window, and tools as structured outputs. They convert an agent from a language model wrapped in a loop into software with typed contracts, versioned configuration, and deliberate context assembly. Everything after factor 4 builds on that foundation.

### Does Hermes Agent implement all twelve factors?

Ten of the twelve are native to the Hermes architecture and implemented in production. Two are partial: factor 9 (compact errors into context) and factor 12 (stateless reducer). Both are engineering work items on the existing architecture, not redesigns.

### How do I adopt the 12 factors in my own agent stack?

Start with the adoption checklist above: version your prompts, define tool schemas first, log every external action to an append-only ledger, and wire escalation as a tool call. Those four moves eliminate the majority of production agent incidents regardless of which framework you run.

## Related Pages

- [Best Practices Overview](index)  --  The production reliability entry point
- [Cron Design](cron-design)  --  Factor 6 and 11 applied to scheduled automation
- [Memory Management](memory-management)  --  Factor 3: owning the context window
- [Skill Development](skill-development)  --  Factor 10: small focused agents
- [Security](security)  --  Factor 7: escalation and approval gates
- [MCP Server Design](mcp-design)  --  Factor 4: tools as structured outputs

---

Start with factors 1 through 4. They convert the "prompt plus tools plus loop" prototype into software. The rest follows.

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  406+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
