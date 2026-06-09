---
title: LangGraph Stateful Workflows
description: Building stateful agent workflows with LangGraph. Graph construction, node design, conditional routing, checkpoint persistence.
---

# LangGraph Stateful Workflows

[LangGraph](https://langchain-oss.github.io/langgraph/) (34K+ stars) provides graph-based state machines for agent workflows. Every step persists state, enabling complex multi-step reasoning with recovery points.

## Architecture

```
START → Node A → Node B → (conditional) → Node C → END
                    ↑                         ↓
              State Checkpoint          State Checkpoint
```

## Setup

```bash
pip install langgraph langchain-core
```

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Literal

class AgentState(TypedDict):
    messages: list
    research_done: bool
    draft: str
    needs_revision: bool

def research_node(state: AgentState) -> AgentState:
    """Run web research, return findings"""
    findings = run_web_search(state["messages"][-1])
    state["research_done"] = True
    state["messages"].append(f"Research: {findings}")
    return state

def draft_node(state: AgentState) -> AgentState:
    """Draft content from research"""
    draft = generate_draft(state["messages"])
    state["draft"] = draft
    return state

def review_router(state: AgentState) -> Literal["publish", "revise"]:
    if state["needs_revision"]:
        return "revise"
    return "publish"

graph = StateGraph(AgentState)
graph.add_node("research", research_node)
graph.add_node("draft", draft_node)
graph.add_node("publish", publish_node)
graph.add_node("revise", revise_node)

graph.set_entry_point("research")
graph.add_edge("research", "draft")
graph.add_conditional_edges("draft", review_router, {
    "publish": "publish",
    "revise": "revise"
})
graph.add_edge("publish", END)
graph.add_edge("revise", "draft")  # Loop back

app = graph.compile()
result = app.invoke({"messages": ["Research: operator pain points in data eng"], "research_done": False, "draft": "", "needs_revision": True})
```

## CorpusIQ Usage

LangGraph powers stateful operations:
- **Content generation with review loops** — draft → review → revise → publish
- **Multi-step lead qualification** — capture → enrich → score → route
- **Error recovery in automation** — checkpoint at each step, resume from failure
- **Cron pipeline orchestration** — chain multiple cron jobs with state handoff

## Key Concepts

| Concept | Description |
|----------|------------|
| StateGraph | Typed state machine with nodes and edges |
| Node | Function that takes and returns state |
| Edge | Unconditional transition between nodes |
| Conditional Edge | Routes to different nodes based on state |
| Checkpointer | Persists state for recovery and history |
| Compile | Builds the runnable graph |

## Patterns

1. **Human-in-the-loop** — pause at review nodes, resume with feedback
2. **Self-healing** — catch errors, route to recovery nodes
3. **Streaming output** — yield intermediate results as nodes execute
4. **Parallel execution** — fan-out to multiple nodes, then join

## Resources

- [LangGraph Docs](https://langchain-oss.github.io/langgraph/)
- [LangGraph GitHub](https://github.com/langchain-ai/langgraph)
- [LangGraph Studio](https://github.com/langchain-ai/langgraph-studio)

---

*← [CrewAI](/hermes/orchestration/crewai/) | [Reflexion](/hermes/orchestration/reflexion/) →*
*↑ [Orchestration](/hermes/orchestration/)*
