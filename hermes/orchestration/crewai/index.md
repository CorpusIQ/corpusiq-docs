---
title: CrewAI Multi-Agent Orchestration
description: Setting up CrewAI for coordinated multi-agent workflows. Agent configuration, task delegation, tool assignment.
---

# CrewAI Multi-Agent Orchestration

[CrewAI](https://crewai.com) (53K+ stars) runs multi-agent coordination where specialized agents collaborate on complex tasks.

## Architecture

```
Agent → Task → Crew → Process → Output
  ↓       ↓       ↓       ↓
 Tools   Context  Delegation  Memory
```

## Setup

```bash
pip install crewai crewai-tools
```

```python
from crewai import Agent, Task, Crew, Process

researcher = Agent(
    role="Market Researcher",
    goal="Find operator pain points on social media",
    backstory="Growth analyst specializing in B2B SaaS",
    tools=[search_tool, scraper_tool],
    verbose=True
)

writer = Agent(
    role="Content Writer",
    goal="Draft helpful responses to operator questions",
    backstory="Technical writer who builds in public",
    tools=[docs_tool],
    verbose=True
)

research_task = Task(
    description="Scan Reddit, X, and HN for operator pain points",
    agent=researcher,
    expected_output="List of 10 pain points with links"
)

writing_task = Task(
    description="Write helpful responses for each pain point",
    agent=writer,
    expected_output="10 draft responses"
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential
)

crew.kickoff()
```

## CorpusIQ Usage

CrewAI handles multi-step growth operations:
- **Lead research**: scout → qualify → draft response → send
- **Content pipeline**: research → draft → edit → schedule → post
- **Competitive analysis**: profile → compare → report → share

## Key Concepts

| Concept | Description |
|---------|-------------|
| Agent | Specialized worker with role, goal, tools |
| Task | Unit of work assigned to an agent |
| Crew | Collection of agents and tasks |
| Process | Sequential or hierarchical execution |
| Tools | Functions agents can call |
| Memory | Persistent context across runs |

## Best Practices

1. **Single responsibility per agent** — don't make one agent do everything
2. **Clear task descriptions** — agents need specific, measurable goals
3. **Verbose mode during development** — you need to see what each agent is doing
4. **Tool design matters** — agents are only as good as the tools they have
5. **Start sequential, go hierarchical** — sequential is easier to debug

## Resources

- [CrewAI Docs](https://docs.crewai.com)
- [CrewAI GitHub](https://github.com/crewAIInc/crewAI)
- [CrewAI Examples](https://github.com/crewAIInc/crewAI-examples)

---

*← [Hermes Agent](/hermes/orchestration/hermes/) | [LangGraph](/hermes/orchestration/langgraph/) →*
*↑ [Orchestration](/hermes/orchestration/)*
