---
title: CrewAI + Hermes Integration
description: Production guide for multi-agent orchestration with CrewAI and Hermes — agent definitions, task delegation, coordination strategies
---

# CrewAI + Hermes Integration

CrewAI provides a multi-agent orchestration framework where specialized agents collaborate on complex workflows. When integrated with Hermes as the execution kernel, you get the best of both worlds: CrewAI's role-based agent architecture and Hermes' model routing, tool ecosystem, and memory infrastructure.

This guide covers production setup, agent design patterns, task delegation strategies, and real workflow examples.

## Architecture Overview

```
┌─────────────────────────────────────────┐
│              CrewAI Layer                │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  │ Growth   │ │ Content  │ │ Research │ │
│  │ Agent    │ │ Agent    │ │ Agent    │ │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ │
│       │            │            │       │
│  ┌────┴────────────┴────────────┴─────┐ │
│  │      Crew Manager (Router)         │ │
│  └────────────────┬───────────────────┘ │
└───────────────────┼─────────────────────┘
                    │
┌───────────────────┼─────────────────────┐
│              Hermes Layer               │
│  ┌────────────────┴───────────────────┐ │
│  │     Multi-Model Router             │ │
│  └────────────────┬───────────────────┘ │
│  ┌────────────────┴───────────────────┐ │
│  │  Tools · MCP · Memory · Browser    │ │
│  └────────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

CrewAI defines *who* does *what*. Hermes provides *how* — model selection, tool access, and execution infrastructure.

## Installation and Setup

### Prerequisites

- Hermes v0.16.0 or later installed and configured
- Python 3.11+
- CrewAI package (`crewai` and `crewai[tools]`)
- At least one configured LLM provider in Hermes

### Configuration

Create a `crew_config.yaml` that maps CrewAI roles to Hermes model tiers:

```yaml
agents:
  growth_agent:
    role: "Growth strategist and marketing analyst"
    goal: "Identify growth opportunities and optimize marketing spend"
    backstory: "You analyze marketing data across channels to find scalable growth levers."
    model_tier: "standard"  # Hermes model tier
    tools:
      - google_ads_connector
      - meta_ads_connector
      - ga4_connector
      - klaviyo_connector

  content_agent:
    role: "Content strategist and creator"
    goal: "Create engaging content that drives audience growth"
    backstory: "You plan and produce content across platforms, optimized for each audience."
    model_tier: "standard"
    tools:
      - browser_use
      - youtube_connector
      - tiktok_connector

  research_agent:
    role: "Deep researcher and analyst"
    goal: "Conduct thorough research and synthesize insights"
    backstory: "You dive deep into topics, gather data from multiple sources, and produce actionable insights."
    model_tier: "premium"  # Needs stronger reasoning
    tools:
      - web_search
      - browser_use
      - notion_connector

  operations_agent:
    role: "Operations and governance specialist"
    goal: "Keep systems running smoothly and detect issues early"
    backstory: "You monitor system health, manage schedules, and ensure compliance."
    model_tier: "lightweight"
    tools:
      - cron_manager
      - slack_connector
      - email_connector

crew:
  process: "sequential"  # or "hierarchical" for manager-led
  verbose: true
  max_rpm: 10  # Rate limit: max requests per minute to LLM provider
```

### Wiring CrewAI to Hermes

Create a custom LLM wrapper that routes CrewAI's model calls through Hermes' multi-model router:

```python
from crewai import Agent, Task, Crew, Process
from hermes.router import ModelRouter

class HermesLLM:
    """Adapter that routes CrewAI LLM calls through Hermes model router."""

    def __init__(self, model_tier: str = "standard"):
        self.router = ModelRouter()
        self.model_tier = model_tier

    def call(self, messages: list[dict], **kwargs) -> str:
        """Route the completion through Hermes with appropriate model tier."""
        response = self.router.complete(
            messages=messages,
            tier=self.model_tier,
            **kwargs
        )
        return response.content

# Initialize agents with Hermes-routed LLMs
growth_agent = Agent(
    config=config["agents"]["growth_agent"],
    llm=HermesLLM(model_tier="standard"),
    tools=load_hermes_tools(config["agents"]["growth_agent"]["tools"])
)
```

## Agent Design Patterns

### Pattern 1: Domain Specialization

Each agent owns a specific domain. Tasks are routed based on domain classification.

**Use when:** You have clearly separated business functions (marketing, engineering, operations).

**Anti-pattern:** Over-specializing until agents can't handle cross-domain edge cases.

**Example:** A growth agent analyzes ad performance; a content agent creates posts; an operations agent monitors cron jobs. Each has its own tools and model tier.

### Pattern 2: Hierarchical Delegation

A manager agent receives all tasks and delegates to specialists based on task analysis.

**Use when:** Tasks are ambiguous and need classification before execution.

**Trade-off:** Adds one LLM call overhead per task but improves routing accuracy.

```python
crew = Crew(
    agents=[manager_agent, growth_agent, content_agent, research_agent],
    tasks=[],
    process=Process.hierarchical,  # Manager-led
    manager_llm=HermesLLM(model_tier="premium"),  # Manager needs strong reasoning
)
```

### Pattern 3: Sequential Pipeline

Agents execute in a fixed order, each receiving output from the previous agent.

**Use when:** Workflows are deterministic and ordered (research → draft → review → publish).

**Setup:** `process: Process.sequential` in crew config.

### Pattern 4: Parallel Fan-Out

Multiple agents execute simultaneously on independent sub-tasks, then results merge.

**Use when:** Sub-tasks have no dependencies (research competitor A AND competitor B simultaneously).

**Implementation:** Define tasks without dependencies in CrewAI; they'll execute concurrently.

## Task Delegation Strategies

### Explicit Delegation

Define exactly which agent handles which task upfront:

```python
research_task = Task(
    description="Research top 5 competitors in AI agent space",
    agent=research_agent,  # Explicit assignment
    expected_output="Competitor analysis report with market positioning"
)

content_task = Task(
    description="Write a LinkedIn post about our latest feature",
    agent=content_agent,
    expected_output="Engaging LinkedIn post with hook, body, and call-to-action"
)
```

### Dynamic Delegation

Let CrewAI decide which agent handles a task based on role descriptions and capabilities:

```python
ambiguous_task = Task(
    description="Analyze this market data and create a summary post",
    # No agent specified — CrewAI will assign based on agent roles
    expected_output="Analysis summary formatted for social media"
)
```

**Best practice:** Use explicit delegation for production workflows where you know the structure. Use dynamic delegation for ad-hoc tasks where routing flexibility adds value.

### Context Passing

Tasks can pass context forward through the `context` parameter:

```python
research = Task(
    description="Research AI agent market trends Q2 2026",
    agent=research_agent,
    expected_output="Trend report with data sources"
)

content = Task(
    description="Turn the research into a Twitter thread",
    agent=content_agent,
    context=[research],  # Receives research task output
    expected_output="5-tweet thread with key insights"
)

publish = Task(
    description="Post the thread and track engagement",
    agent=operations_agent,
    context=[content],
    expected_output="Confirmation of published thread with post URL"
)
```

## Production Workflow: Content Strategy Pipeline

Here's a complete production example — a weekly content strategy workflow:

```python
from crewai import Agent, Task, Crew, Process

# ── Agents ──────────────────────────────────────────

analyst = Agent(
    role="Content Performance Analyst",
    goal="Analyze content performance and identify winning patterns",
    backstory="You review analytics across platforms to find what resonates.",
    llm=HermesLLM("standard"),
    tools=["ga4_connector", "youtube_connector", "tiktok_connector"]
)

strategist = Agent(
    role="Content Strategist",
    goal="Create data-driven content plans for the week ahead",
    backstory="You translate performance insights into actionable content briefs.",
    llm=HermesLLM("premium"),
    tools=["browser_use", "notion_connector"]
)

creator = Agent(
    role="Content Creator",
    goal="Produce platform-optimized content from briefs",
    backstory="You craft engaging posts, scripts, and captions.",
    llm=HermesLLM("standard"),
    tools=["browser_use"]
)

publisher = Agent(
    role="Content Publisher",
    goal="Schedule and publish content across platforms",
    backstory="You handle multi-platform scheduling and format compliance.",
    llm=HermesLLM("lightweight"),
    tools=["browser_use", "slack_connector"]
)

# ── Tasks ───────────────────────────────────────────

analyze_performance = Task(
    description="""
    Analyze last week's content performance across all platforms.
    Extract: top 3 posts by engagement, worst 3, engagement rate trends,
    audience growth data, and platform-specific patterns.
    """,
    agent=analyst,
    expected_output="Weekly performance report with data-backed insights"
)

create_plan = Task(
    description="""
    Using the performance analysis, create a content plan for next week.
    Include: 5 LinkedIn posts, 3 Twitter threads, 2 short-form videos,
    1 long-form article. For each: topic, hook, key points, platform format.
    Prioritize topics that performed well in analysis.
    """,
    agent=strategist,
    context=[analyze_performance],
    expected_output="Weekly content calendar with briefs for each piece"
)

produce_content = Task(
    description="""
    Produce all content pieces from the plan. Write full drafts for each.
    For videos: write scripts. For posts: write complete copy with hooks.
    Ensure each piece is optimized for its platform's format and audience.
    """,
    agent=creator,
    context=[create_plan],
    expected_output="Complete content drafts ready for publishing"
)

schedule_publishing = Task(
    description="""
    Schedule all produced content across platforms using optimal timing.
    LinkedIn: Tue-Thu 8-10am. Twitter: daily 12pm and 5pm.
    Videos: Wed 2pm. Article: Thu 9am.
    Confirm all posts are queued and return the publishing schedule.
    """,
    agent=publisher,
    context=[produce_content],
    expected_output="Confirmed publishing schedule with platform URLs"
)

# ── Crew ────────────────────────────────────────────

content_crew = Crew(
    agents=[analyst, strategist, creator, publisher],
    tasks=[analyze_performance, create_plan, produce_content, schedule_publishing],
    process=Process.sequential,
    verbose=True
)

result = content_crew.kickoff()
```

## Coordination Strategies

### Event-Driven Coordination

Use Hermes cron jobs to trigger CrewAI workflows on a schedule:

```yaml
# hermes/cron/content_strategy.yaml
name: weekly_content_strategy
schedule: "0 9 * * 1"  # Every Monday at 9am
task: crewai.kickoff.weekly_content_strategy
timeout: 3600  # 1 hour max
notify_on: ["complete", "failure"]
```

### Conditional Coordination

Use LangGraph to conditionally invoke CrewAI workflows based on system state:

```python
# In LangGraph, conditionally route to CrewAI
def route_to_crew(state):
    if state["engagement_drop"] > 0.20:
        return "emergency_content_crew"
    elif state["day_of_week"] == "Monday":
        return "weekly_content_crew"
    return "skip"

workflow.add_conditional_edges("evaluate", route_to_crew, {
    "emergency_content_crew": "crew_reactive",
    "weekly_content_crew": "crew_proactive",
    "skip": "end"
})
```

### Human-in-the-Loop

For critical decisions, CrewAI workflows can pause for human approval:

```python
review_task = Task(
    description="Review the content plan before production",
    agent=strategist,
    expected_output="Approved content plan",
    human_input=True  # Requires human approval before proceeding
)
```

## Performance Optimization

### Model Tier Selection

Match model capability to task complexity to control costs:

| Agent Type | Recommended Tier | Rationale |
|---|---|---|
| Strategic planner | Premium | Complex reasoning, multi-variable optimization |
| Content creator | Standard | Creative writing within constraints |
| Data analyst | Standard | Structured analysis, pattern recognition |
| Publisher/scheduler | Lightweight | Deterministic tasks, format compliance |
| Research agent | Premium | Deep reading comprehension, synthesis |
| Operations monitor | Lightweight | Simple checks, status reporting |

### Rate Limiting

Set `max_rpm` in crew config to avoid provider rate limits. For a crew with 4 agents processing sequentially:
- Set `max_rpm: 10` per agent
- Each sequential task typically makes 2-4 LLM calls
- Total: approximately 32-64 calls per crew execution

### Caching

Enable CrewAI's caching for deterministic sub-tasks:

```python
crew = Crew(
    agents=[...],
    tasks=[...],
    cache=True,  # Cache LLM responses
    memory=True  # Enable agent memory across tasks
)
```

## Troubleshooting Common Issues

**Agent uses wrong model tier:** Verify the `model_tier` parameter in your HermesLLM adapter. Check Hermes routing rules aren't overriding.

**Tools not found:** Ensure tool names in agent config match Hermes' registered tool names exactly. Use `hermes tools list` to verify.

**Sequential tasks stall:** Check that each task's `expected_output` is produced. CrewAI won't proceed without it. Add timeout guards.

**Cost overrun:** Set `max_iter` on agents (default is 15 — often too high). Set `max_rpm` on crew. Monitor via Hermes' usage tracking.
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
