---
title: Reflexion — Self-Improving Agent Patterns
description: Building agents that evaluate their own output, detect errors, and adjust strategy — production Reflexion patterns with Hermes
---

# Reflexion — Self-Improving Agent Patterns

Reflexion is the pattern of having an agent evaluate its own output, detect issues, and adjust its approach before delivering a final result. Instead of a human catching mistakes, the agent catches them itself — then fixes them.

This guide covers production Reflexion patterns with Hermes: evaluation loop design, error detection strategies, strategy adjustment mechanisms, and concrete examples you can deploy.

## The Core Loop

Every Reflexion implementation follows the same structure:

```
Task → Execute → Evaluate → Pass? → Return Result
                    ↑           │
                    │    No     │
                    └─ Adjust ──┘
```

**Execute:** The agent attempts the task.
**Evaluate:** A separate evaluation step (often a different model or prompt) judges the output.
**Pass?** If the output meets quality criteria, return it. If not, identify what's wrong.
**Adjust:** Modify the strategy based on the evaluation feedback — then execute again.

The key insight: evaluation is cheaper than execution, and correction is cheaper than starting over. A $0.01 evaluation that catches a mistake saves the cost of a bad output plus the cost of human review.

## Pattern 1: Output Quality Reflexion

The most common pattern. After generating output, evaluate it against criteria, and refine if needed.

### Implementation

```python
def reflexion_loop(task: str, criteria: list[str], max_iterations: int = 3) -> str:
    """
    Execute a task with Reflexion-based quality improvement.

    Args:
        task: The task description
        criteria: List of quality criteria to evaluate against
        max_iterations: Maximum refinement attempts
    """
    strategy_notes = ""  # Accumulated improvement notes

    for iteration in range(max_iterations):
        # Step 1: Execute with current strategy
        output = hermes_llm.complete(
            messages=[
                {"role": "system", "content": f"Complete this task: {task}\n\nStrategy notes from previous attempts:\n{strategy_notes}"},
                {"role": "user", "content": task}
            ],
            tier="standard"
        )

        # Step 2: Evaluate against criteria
        evaluation = hermes_llm.complete(
            messages=[
                {"role": "system", "content": f"""Evaluate this output against the following criteria.
                For each criterion, score PASS or FAIL. If FAIL, explain why.

                Criteria:
                {chr(10).join(f'- {c}' for c in criteria)}

                Output to evaluate:
                {output}"""},
            ],
            tier="lightweight"  # Evaluation is cheap
        )

        # Step 3: Check if all criteria passed
        if "FAIL" not in evaluation:
            return output  # Success!

        # Step 4: Extract improvement notes for next attempt
        strategy_notes += f"\nIteration {iteration + 1} feedback: {evaluation}"

    # Return best attempt if max iterations reached
    return output  # With a warning flag
```

### Criteria Examples

**For blog posts:**
- Contains a clear hook in the first paragraph
- Supports claims with specific examples or data
- Includes a call-to-action at the end
- Appropriate reading level for target audience (8th-10th grade)
- No grammatical errors or typos

**For code generation:**
- Code runs without syntax errors
- Includes error handling for edge cases
- Follows project conventions (naming, structure)
- Contains comments for non-obvious logic
- Passes the provided test cases

**For data analysis:**
- All claims are backed by the data shown
- Calculations are explained step by step
- Limitations or caveats are explicitly stated
- Conclusions don't overstate the evidence
- Format is appropriate for the audience (executive vs. technical)

### Production Config

```yaml
reflexion:
  quality:
    evaluator_model_tier: "lightweight"  # Cheap evaluation
    executor_model_tier: "standard"      # Main work
    max_iterations: 3
    early_exit_threshold: 0.85           # If 85%+ criteria pass, accept
    criteria_weights:                    # Not all criteria are equal
      accuracy: 3
      completeness: 2
      formatting: 1
```

## Pattern 2: Factual Verification Reflexion

For outputs where factual accuracy is critical — claims must be verified against sources.

```python
def factual_reflexion(claim: str, sources: list[str]) -> dict:
    """
    Verify claims against sources and refine if necessary.
    Returns: {"output": str, "verified": bool, "issues": list}
    """
    for iteration in range(3):
        # Step 1: Generate output with source citations
        output = hermes_llm.complete(
            messages=[
                {"role": "system", "content": "Generate analysis citing specific sources for each claim. Format: [Claim] (Source: [citation])"},
                {"role": "user", "content": f"Analyze: {claim}\nSources: {sources}"}
            ],
            tier="premium"
        )

        # Step 2: Cross-reference each claim against sources
        verification = hermes_llm.complete(
            messages=[
                {"role": "system", "content": """For each claim in the output, verify it against the original sources.
                Return JSON with 'verified' (bool) and 'issues' (array of problematic claims).

                Sources:
                """ + "\n---\n".join(sources)},
                {"role": "user", "content": output}
            ],
            tier="standard"
        )

        verification_data = json.loads(verification)

        if verification_data["verified"]:
            return {"output": output, "verified": True, "issues": []}

        # Step 3: Feed issues back for correction
        sources = sources + [f"CORRECTION NEEDED: {verification_data['issues']}"]

    return {"output": output, "verified": False, "issues": verification_data.get("issues", [])}
```

### When to Use

- Writing reports that cite specific data points
- Generating documentation from API specs
- Creating content that references statistics or studies
- Any output where being wrong has real consequences

### Cost-Benefit

Factual verification adds 1-2 additional LLM calls per iteration. For high-stakes content, this is negligible compared to the cost of publishing incorrect information.

## Pattern 3: Strategy Adjustment Reflexion

Instead of just fixing the output, the agent changes *how* it approaches the task.

```python
class StrategyReflexion:
    """
    The agent maintains a strategy stack. On failure, it doesn't just
    tweak the output — it changes the strategy.
    """

    STRATEGIES = [
        "direct_answer",        # Answer directly from knowledge
        "research_first",       # Research before answering
        "decompose",            # Break into sub-tasks
        "analogy",              # Use analogies to explain
        "step_by_step",         # Chain-of-thought reasoning
        "examples_driven",      # Lead with concrete examples
        "counterfactual",       # Explore what-if scenarios
    ]

    def execute(self, task: str) -> str:
        attempted_strategies = []
        best_output = None
        best_score = 0

        for iteration in range(5):
            # Select strategy based on what hasn't worked
            strategy = self._select_strategy(task, attempted_strategies)

            # Execute with strategy prompt
            output = hermes_llm.complete(
                messages=[
                    {"role": "system", "content": f"Strategy: {strategy}\n\n"
                     f"Previously attempted strategies and their issues:\n"
                     f"{self._format_history(attempted_strategies)}\n\n"
                     f"Try a different approach this time."},
                    {"role": "user", "content": task}
                ],
                tier="premium"
            )

            # Evaluate
            score, feedback = self._evaluate(task, output)
            attempted_strategies.append({
                "strategy": strategy,
                "score": score,
                "feedback": feedback
            })

            if score > best_score:
                best_score = score
                best_output = output

            if score >= 0.9:
                return output

        return best_output
```

### Strategy Selection Logic

```python
def _select_strategy(self, task: str, history: list) -> str:
    tried = {h["strategy"] for h in history}

    # Analyze the task to determine appropriate strategies
    task_analysis = hermes_llm.complete(
        messages=[
            {"role": "system", "content": "Classify this task: simple_factual, complex_reasoning, creative, analytical, instructional"},
            {"role": "user", "content": task}
        ],
        tier="lightweight"
    )

    # Map task types to preferred strategy order
    strategy_order = {
        "simple_factual": ["direct_answer", "research_first"],
        "complex_reasoning": ["step_by_step", "decompose", "analogy"],
        "creative": ["examples_driven", "analogy", "counterfactual"],
        "analytical": ["decompose", "step_by_step", "research_first"],
        "instructional": ["step_by_step", "examples_driven", "analogy"],
    }

    for strategy in strategy_order.get(task_analysis, self.STRATEGIES):
        if strategy not in tried:
            return strategy

    return self.STRATEGIES[len(tried) % len(self.STRATEGIES)]  # Cycle
```

## Pattern 4: Multi-Evaluator Reflexion

Use multiple evaluators with different perspectives for robust quality assessment:

```python
EVALUATORS = {
    "accuracy": "Evaluate factual accuracy. Are all claims correct and supported?",
    "clarity": "Evaluate clarity and readability. Would the target audience understand this?",
    "completeness": "Evaluate completeness. Does this fully answer the question?",
    "bias": "Evaluate for bias or one-sidedness. Are multiple perspectives fairly represented?",
    "actionability": "Evaluate actionability. Can the reader act on this information?",
}

def multi_evaluator_reflexion(task: str, active_evaluators: list[str]) -> str:
    """Run Reflexion with multiple evaluator perspectives."""
    for iteration in range(3):
        output = hermes_llm.complete(
            messages=[{"role": "user", "content": task}],
            tier="standard"
        )

        all_pass = True
        feedback = []

        for evaluator_name in active_evaluators:
            eval_prompt = EVALUATORS[evaluator_name]
            result = hermes_llm.complete(
                messages=[
                    {"role": "system", "content": f"{eval_prompt}\nScore PASS or FAIL with explanation."},
                    {"role": "user", "content": output}
                ],
                tier="lightweight"
            )

            if "FAIL" in result:
                all_pass = False
                feedback.append(f"[{evaluator_name}] {result}")

        if all_pass:
            return output

        task = f"{task}\n\nPrevious attempt feedback:\n" + "\n".join(feedback)

    return output
```

### Evaluator Selection by Task Type

| Task Type | Required Evaluators | Optional |
|---|---|---|
| Technical documentation | accuracy, clarity, completeness | - |
| Marketing copy | clarity, actionability, bias | accuracy |
| Analysis/report | accuracy, completeness, bias | clarity |
| Tutorial/how-to | clarity, completeness, actionability | - |
| Opinion/thought leadership | clarity, bias | accuracy, completeness |

## Production Deployment with Hermes

### Configuration

```yaml
# hermes/config/reflexion.yaml
reflexion:
  default_max_iterations: 3
  cost_ceiling_per_task: 0.50  # USD — hard stop
  
  evaluators:
    default_set: [accuracy, clarity, completeness]
    
  model_mapping:
    execution:
      creative: "standard"
      analytical: "premium"
      simple: "lightweight"
    evaluation:
      default: "lightweight"  # Always use cheapest capable model
    
  failure_handling:
    max_iterations_reached: "return_with_warning"  # or "raise_error"
    cost_ceiling_reached: "return_best_so_far"
    
  logging:
    trace_all_iterations: true
    store_intermediate_outputs: true  # For debugging
```

### Hermes Cron Integration

Schedule Reflexion-based quality checks:

```yaml
# hermes/cron/content_quality_check.yaml
name: content_quality_reflexion
schedule: "0 8,14,20 * * *"  # Three times daily
task: reflexion.quality_check.recent_content
params:
  lookback_hours: 6
  evaluators: [accuracy, clarity, bias]
  auto_fix: true  # Automatically apply corrections
timeout: 600
notify_on: ["failure"]
```

### Monitoring Reflexion Performance

Track these metrics to optimize your Reflexion setup:

- **Pass rate on first attempt:** High (>70%) means your initial prompts are good. Low means you're over-relying on Reflexion.
- **Average iterations to pass:** Should be under 2. Higher means your evaluation criteria might be too strict or your initial execution is weak.
- **Cost per task (with vs. without Reflexion):** Reflexion adds 30-80% to task cost but typically improves quality by 40-60%.
- **False pass rate:** Spot-check outputs that passed evaluation. If >5% have errors, your evaluation criteria or model are insufficient.

## Common Pitfalls

**Over-reliance on Reflexion:** If every task needs 3 iterations, fix your initial prompts. Reflexion is a safety net, not a crutch.

**Too many criteria:** Start with 3 criteria. More than 5 creates evaluation noise and slows convergence.

**Same model for both:** Don't use the same model for execution and evaluation — it's grading its own homework. Use a lightweight model for evaluation.

**No cost ceiling:** Always set a `cost_ceiling_per_task`. Reflexion loops without a ceiling can burn through budget.

**Infinite loops with unclear criteria:** "Make it better" isn't evaluable. Criteria must be specific and falsifiable: "Score PASS or FAIL."

## Decision Tree

```
Need quality improvement on outputs?
├─ Yes, accuracy is critical → Factual Verification Reflexion
├─ Yes, general quality matters → Output Quality Reflexion
├─ Yes, approach keeps failing → Strategy Adjustment Reflexion
├─ Yes, for high-stakes content → Multi-Evaluator Reflexion
└─ No → Direct execution, no Reflexion overhead
```

---

*Next: [LangGraph Integration](/hermes/orchestration/langgraph/) · [CrewAI Integration](/hermes/orchestration/crewai/) · [Architecture](/hermes/architecture/)*


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*


---
*Powered by [CorpusIQ](https://www.corpusiq.io) — Accelerate your business. All your tools in one place.*
