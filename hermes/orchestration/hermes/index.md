---
title: Hermes Agent  --  Orchestration Engine
description: Hermes Agent as the primary execution kernel  --  capabilities, configuration, and production patterns
---

# Hermes Agent  --  Orchestration Engine

Hermes serves as the platform's primary orchestration framework and execution environment. It is the kernel, not the platform.

## Version History

Deployed from v0.15.1 to v0.16.0, incorporating 426 commits:

- Model switching with fallback chains
- Browser and computer-use tooling
- Skill bundles and marketplace
- Insights dashboards
- Web interfaces
- Gateway integrations

## Core Architecture

Hermes acts as the execution kernel that all other components plug into. CrewAI agents delegate to Hermes for tool execution. LangGraph workflows route through Hermes for final action. Skills load into Hermes as executable workflows.

## Configuration

```yaml
models:
  default:
    provider: ollama
    model: qwen3.6:27b
  fallback:
    - provider: custom
      model: deepseek-r1
    - provider: anthropic
      model: claude-opus-4

tools:
  - terminal
  - file
  - web
  - browser
  - skills
  - mcp

profiles:
  corpusiq:
    skills_dir: ~/.hermes/profiles/corpusiq/skills/
    memory: ~/.hermes/profiles/corpusiq/memory/
    crons: ~/.hermes/profiles/corpusiq/cron/
```

## Production Patterns

Model routing: default to local models, escalate to API only when needed. Skills: load skill for every task matching its trigger. Memory: persistent across sessions via GBrain. Crons: verify execution, never trust `last_status: ok`.

---
title: CrewAI  --  Multi-Agent Orchestration
description: Multi-agent coordination with CrewAI  --  specialized agents, parallel execution, and domain delegation
---

# CrewAI  --  Multi-Agent Orchestration

CrewAI provides multi-agent orchestration. Instead of a single agent managing everything, specialized agents handle specific domains in parallel.

## Agent Roster

| Agent | Domain | Primary Tools |
|-------|--------|---------------|
| Growth | Marketing, social, SEO | Postiz, Ahrefs, Reddit |
| Content | Video, writing, research | HeyGen, YouTube |
| Research | Market intelligence | Web, Firecrawl |
| Operations | Cron, email, infrastructure | Terminal, Gmail |
| Job Search | Applications, monitoring | Web, Email |
| Governance | Registry, audits, improvements | File, Terminal |

## Architecture

CrewAI agents delegate execution to Hermes. Hermes provides tool access, model routing, and error recovery. Agents focus on domain logic. Hermes handles infrastructure.

## Benefits

Parallel execution  --  multiple agents work simultaneously. Specialization  --  each agent has deep domain context. Isolation  --  agent failures don't cascade. Scalability  --  new agents added without refactoring.

## Use Case: Content Pipeline

```
Research Agent → finds trending topics
Content Agent → drafts scripts
Video Agent → generates via HeyGen
Social Agent → distributes via Postiz
Monitoring Agent → tracks engagement
```

Five agents working in sequence, each focused on its domain. Result: end-to-end automation without a single monolithic agent.

---
title: LangGraph  --  Stateful Workflows
description: Graph-based execution with conditional routing, persistent state, and recovery paths for Hermes agents
---

# LangGraph  --  Stateful Workflows

LangGraph introduces stateful graph-based execution  --  conditional routing, multi-step workflows, persistent state management, branching decision trees, and recovery paths. The result: deterministic workflow execution, not linear prompt chains.

## Graph Structure

```
Start → Classify Intent → Route to Domain → Execute → Validate → End
                        ↓                    ↓
                      Retry ←────────── Validation Fail
```

## State Management

State persists across workflow steps. Context doesn't need to be re-loaded. Decision history is tracked. Failed steps can be retried from checkpoint.

## Conditional Routing

Tasks route based on classification: intent detection → domain routing → tool selection → execution. Each node in the graph makes decisions based on prior state.

## Recovery Paths

If execution fails: retry with adjusted parameters → escalate to different model → flag for human review → log for self-improvement cycle.

## Integration

LangGraph workflows execute through Hermes tool calls. Hermes provides the execution environment. LangGraph provides the decision structure. Together: flexible execution with deterministic flow control.

---
title: Reflexion  --  Self-Improving Agents
description: Self-evaluation loops for autonomous agent improvement without human correction
---

# Reflexion  --  Self-Improving Agents

Reflexion introduces self-evaluation loops. Instead of waiting for human correction, agents evaluate their own output and self-correct.

## Execution Loop

```
Task → Execute → Evaluate → Detect Error → Adjust Strategy → Re-execute
```

## Evaluation Criteria

Output quality: does it meet quality standards? Task completion: was the objective achieved? Efficiency: could it be done with fewer calls? Accuracy: are the results correct?

## Strategy Adjustment

When evaluation detects issues: adjust prompt strategy, switch model tier, add more context, break into sub-tasks, or escalate.

## Production Impact

Reduced human intervention by approximately 70% for routine tasks. Agents learn from mistakes within the same conversation rather than requiring external correction.

## Integration

Reflexion wraps existing execution paths. Any agent task can be reflexion-enabled. The improvement loop runs transparently  --  errors are fixed before the user sees the output.

## Daily Cycle

At 23:00, the daily self-improvement cycle analyzes the day's reflexion logs, identifies patterns, and patches skills to prevent recurrence of common errors. This is cumulative: the platform improves daily.

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  406+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes)  --  406+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
