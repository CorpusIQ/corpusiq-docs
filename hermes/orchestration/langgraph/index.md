---
title: LangGraph + Hermes Integration
description: Stateful graph-based agent workflows — conditional routing, persistence, and production patterns with LangGraph and Hermes
---

# LangGraph + Hermes Integration

LangGraph brings stateful, graph-based execution to agent workflows. Unlike linear prompt chains or CrewAI's role-based delegation, LangGraph models your agent's decision process as a directed graph — nodes for actions, edges for transitions, and state that persists across steps.

When combined with Hermes, you get deterministic workflow control with Hermes' model routing, tool ecosystem, and memory infrastructure. This guide covers production patterns, persistence strategies, and real workflow examples.

## Why LangGraph?

Linear agent chains have a fundamental limitation: they can't branch. Every input follows the same path. LangGraph solves this by modeling your agent as a state machine:

```
                    ┌──────────┐
                    │  START   │
                    └────┬─────┘
                         │
                    ┌────▼─────┐
                    │ Evaluate │──── condition met? ────┐
                    └────┬─────┘                        │
                         │ condition not met            │
                    ┌────▼─────┐                   ┌────▼─────┐
                    │ Research │                   │  Execute │
                    └────┬─────┘                   └────┬─────┘
                         │                              │
                    ┌────▼─────┐                         │
                    │ Validate │◄────────────────────────┘
                    └────┬─────┘
                         │ valid
                    ┌────▼─────┐
                    │   END    │
                    └──────────┘
```

This enables: conditional routing, loops, parallel execution, human-in-the-loop, and persistent checkpoints.

## Core Concepts

### State

The shared data structure that flows through the graph. Every node reads from state, modifies it, and passes it forward.

```python
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]  # Conversation history (appends)
    research_findings: str                   # Accumulated research
    action_plan: dict                        # Next steps to execute
    retry_count: int                         # Loop guard
    final_output: str                        # Result to return
```

### Nodes

Python functions (or Hermes agent calls) that transform state:

```python
def research_node(state: AgentState) -> AgentState:
    """Research phase — gather information about the topic."""
    query = state["messages"][-1].content
    # Use Hermes tool ecosystem via the MCP bridge
    results = hermes_tools.web_search(query)
    return {
        "research_findings": results,
        "messages": [{"role": "system", "content": f"Research complete: {len(results)} sources found"}]
    }

def analyze_node(state: AgentState) -> AgentState:
    """Analysis phase — synthesize findings."""
    synthesis = hermes_llm.complete(
        messages=[
            {"role": "system", "content": "Synthesize these research findings into key insights."},
            {"role": "user", "content": state["research_findings"]}
        ],
        tier="premium"
    )
    return {"action_plan": {"insights": synthesis, "ready": True}}
```

### Edges

Define how execution moves between nodes:

- **Normal edges:** Always transition from A to B
- **Conditional edges:** Choose next node based on state

```python
def should_retry(state: AgentState) -> str:
    """Decide whether to retry or finish."""
    if state.get("retry_count", 0) < 3 and not state.get("final_output"):
        return "research"  # Go back to research
    return "finish"       # End the workflow
```

## Production Pattern 1: Research-Analyze-Validate Loop

The most common production pattern — research until confident, then proceed.

```python
from langgraph.graph import StateGraph, END

# ── Define nodes ────────────────────────────────────

def research(state):
    """Gather information from multiple sources."""
    topic = state["messages"][-1].content
    web_results = hermes_tools.web_search(topic)
    doc_results = hermes_tools.query_knowledge_base(topic)
    return {
        "research_findings": f"Web: {web_results}\nKnowledge: {doc_results}",
        "retry_count": state.get("retry_count", 0) + 1
    }

def analyze(state):
    """Synthesize findings into insights."""
    analysis = hermes_llm.complete(
        messages=[
            {"role": "system", "content": "Analyze these findings. Return JSON with 'confidence' (0-1) and 'insights' (array)."},
            {"role": "user", "content": state["research_findings"]}
        ],
        tier="premium"
    )
    return {"action_plan": json.loads(analysis)}

def validate(state):
    """Check if confidence threshold is met."""
    confidence = state["action_plan"].get("confidence", 0)
    if confidence >= 0.8:
        return {"final_output": state["action_plan"]["insights"]}
    return {}  # Will trigger retry

# ── Conditional routing ─────────────────────────────

def route_after_validate(state):
    if state.get("final_output"):
        return "finish"
    if state.get("retry_count", 0) >= 3:
        return "force_finish"
    return "research"  # Loop back

# ── Build graph ─────────────────────────────────────

graph = StateGraph(AgentState)

graph.add_node("research", research)
graph.add_node("analyze", analyze)
graph.add_node("validate", validate)

graph.set_entry_point("research")
graph.add_edge("research", "analyze")
graph.add_edge("analyze", "validate")

graph.add_conditional_edges(
    "validate",
    route_after_validate,
    {
        "research": "research",
        "finish": END,
        "force_finish": END
    }
)

workflow = graph.compile()
```

### Key Design Decisions

**Max iterations:** Always cap loops. Three retries is usually sufficient — beyond that, you're either stuck in a bad pattern or the task is genuinely unsolvable with current information. Log the final state for debugging.

**Confidence thresholds:** 0.8 works well for most use cases. Lower (0.6) for time-sensitive tasks where speed matters more than accuracy. Higher (0.95) for compliance or financial contexts.

**State accumulation:** Every node appends to state. The full execution trace is preserved, which is invaluable for debugging and audit trails.

## Production Pattern 2: Conditional Multi-Path Router

Route incoming requests to different processing paths based on intent classification:

```python
def classify_intent(state):
    """Classify the incoming request to determine processing path."""
    message = state["messages"][-1].content
    classification = hermes_llm.complete(
        messages=[
            {"role": "system", "content": "Classify this request as: analytics, content_creation, system_ops, or general_question. Return only the category."},
            {"role": "user", "content": message}
        ],
        tier="lightweight"  # Classification is cheap
    )
    return {"route": classification.strip().lower()}

def route_by_intent(state):
    return state["route"]

# Add specialized nodes for each path
graph.add_node("classify", classify_intent)
graph.add_node("analytics_handler", analytics_node)
graph.add_node("content_handler", content_node)
graph.add_node("ops_handler", ops_node)
graph.add_node("general_handler", general_node)

graph.set_entry_point("classify")
graph.add_conditional_edges(
    "classify",
    route_by_intent,
    {
        "analytics": "analytics_handler",
        "content_creation": "content_handler",
        "system_ops": "ops_handler",
        "general_question": "general_handler"
    }
)

# All handlers converge to a final formatting node
for handler in ["analytics_handler", "content_handler", "ops_handler", "general_handler"]:
    graph.add_edge(handler, "format_response")
graph.add_edge("format_response", END)
```

## Persistence Strategies

### In-Memory (Development)

Default behavior. State persists only for the duration of the execution. Fast, simple, but no recovery.

```python
workflow = graph.compile()  # No checkpointer = in-memory
```

### SQLite Checkpointer (Production)

State saved to SQLite after every node transition. Survives process restarts.

```python
from langgraph.checkpoint.sqlite import SqliteSaver

checkpointer = SqliteSaver.from_conn_string("hermes_langgraph.db")
workflow = graph.compile(checkpointer=checkpointer)

# Resume from a previous checkpoint
config = {"configurable": {"thread_id": "thread_123"}}
workflow.invoke(initial_state, config)
```

**When to use:** Production deployments where workflows may run for minutes or hours, and you need recovery from crashes or the ability to inspect execution history.

### Postgres Checkpointer (Multi-Node)

For multi-node deployments where multiple Hermes instances share state:

```python
from langgraph.checkpoint.postgres import PostgresSaver

checkpointer = PostgresSaver.from_conn_string(
    "postgresql://user@worker-node.local:5432/hermes_state"
)
workflow = graph.compile(checkpointer=checkpointer)
```

### Thread Management

Each conversation gets a `thread_id`. Different threads have independent state:

```python
# Thread A: Research task
workflow.invoke(
    {"messages": [{"role": "user", "content": "Research quantum computing trends"}]},
    {"configurable": {"thread_id": "research_001"}}
)

# Thread B: Content task (independent state)
workflow.invoke(
    {"messages": [{"role": "user", "content": "Write a blog post about AI agents"}]},
    {"configurable": {"thread_id": "content_042"}}
)
```

## Production Pattern 3: Human-in-the-Loop

LangGraph supports interrupting execution for human approval:

```python
def sensitive_action(state):
    """Action that requires human approval before execution."""
    # This node will interrupt and wait
    pass

graph.add_node("approval_check", sensitive_action)

# Compile with interrupt before the sensitive node
workflow = graph.compile(
    checkpointer=checkpointer,
    interrupt_before=["approval_check"]
)

# Execution pauses at approval_check
result = workflow.invoke(state, config)

# Human reviews and approves
workflow.invoke(None, config)  # Resumes from checkpoint
```

### Approval Patterns

**Pre-execution approval:** Interrupt before any write operation (publishing, sending emails, modifying data).

**Post-execution review:** Let the agent execute, but flag results for human review before they're final. The agent can continue to the next task while review is pending.

**Threshold-based:** Interrupt only when confidence is below a threshold. High-confidence actions proceed automatically.

## Production Pattern 4: Parallel Fan-Out / Fan-In

Execute multiple independent branches in parallel, then merge:

```python
from langgraph.graph import StateGraph

def fan_out(state):
    """Create parallel tasks from a list."""
    tasks = state["action_plan"]["parallel_tasks"]
    return [{"task": t} for t in tasks]  # One state per parallel branch

def process_task(state):
    """Process a single task (runs in parallel for each task)."""
    result = hermes_llm.complete(
        messages=[{"role": "user", "content": state["task"]}],
        tier="standard"
    )
    return {"result": result}

def fan_in(results):
    """Merge parallel results."""
    merged = "\n\n".join([r["result"] for r in results])
    return {"final_output": merged}

graph.add_node("fan_out", fan_out)
graph.add_node("process_task", process_task)
graph.add_node("fan_in", fan_in)

graph.set_entry_point("fan_out")
# Send class enables parallel execution
graph.add_edge("fan_out", "process_task")
graph.add_edge("process_task", "fan_in")
graph.add_edge("fan_in", END)
```

**Use cases:** Competitor research (research 5 competitors in parallel), multi-platform content adaptation, batch data processing.

## Integration with Hermes Cron

LangGraph workflows can be triggered by Hermes cron jobs:

```yaml
# hermes/cron/daily_research.yaml
name: daily_market_research
schedule: "0 7 * * *"
task: langgraph.workflow.market_research
checkpointer: sqlite
thread_template: "research_{date}"
timeout: 1800
notify_on: ["failure"]
```

With the checkpointer, you can inspect the state of any past execution, see exactly where it branched, and understand the decision path.

## Monitoring and Debugging

### State Inspection

```python
# Inspect historical state for a thread
state = workflow.get_state({"configurable": {"thread_id": "research_001"}})
print(f"Current node: {state.next}")
print(f"Retry count: {state.values.get('retry_count')}")
print(f"Messages: {len(state.values.get('messages', []))}")
```

### Execution Tracing

LangGraph can output execution traces for debugging:

```python
workflow = graph.compile(debug=True)  # Prints every state transition
```

### Common Pitfalls

**Infinite loops without guards:** Always include a max iteration check in your conditional edges. The `retry_count` pattern above is essential.

**State explosion:** Long-running threads accumulate state. Implement state trimming in nodes that run many iterations — keep the last N messages, not all of them.

**Checkpointer performance:** SQLite is fine for single-node, low-throughput deployments. For high-throughput or multi-node, use Postgres. SQLite under concurrent writes will bottleneck.

**Thread leaks:** Threads without an END state consume resources. Implement thread TTL (auto-cleanup after 7 days of inactivity).

## Decision Guide

| Requirement | Recommendation |
|---|---|
| Linear workflows, no branching | Skip LangGraph — use CrewAI or direct Hermes |
| Conditional routing based on state | LangGraph is ideal |
| Loops with state (retry, refinement) | LangGraph is ideal |
| Human approval gates | LangGraph with interrupt |
| Parallel execution branches | LangGraph Send API |
| Cross-session persistence | LangGraph with SQLite/Postgres checkpointer |
| Complex state machines | LangGraph with typed state |

---

*Next: [Reflexion Patterns](/hermes/orchestration/reflexion/) · [CrewAI Integration](/hermes/orchestration/crewai/) · [Architecture](/hermes/architecture/)*
