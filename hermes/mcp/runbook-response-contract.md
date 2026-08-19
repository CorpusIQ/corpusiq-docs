---
title: "runbook.v1 Response Contract: Enforce the Output Format of AI Answers"
description: "How to make AI assistants deliver answers in a required visual format: versioned templates, required elements, fail-closed enforcement. The response contract extension for runbook.v1."
tags: [mcp, runbook, output, format, visual, governance, enterprise]
---

# Enforce the Output Format of AI Answers

An AI assistant can be asked to produce a visual answer. Whether it does is another question.

The model decides how to render its response: a chart, a table, a wall of text. For dashboards, financial reports, and board decks, that discretion is the problem. The format must be a contract, not a preference.

## The two-layer answer

**Layer one: the render tool (works today, every client).**
The MCP server does the visualization. A tool like chart_render or dashboard_render fetches the data, renders the chart server-side, and returns it as an image content block. ChatGPT, Claude, and Perplexity display image blocks natively. The model never touches the pixels, so the visual is deterministic: same data, same template, same output. The server controls the brand kit and the source footer.

**Layer two: the response contract (enforced when the host supports runbooks).**
The runbook manifest declares what the final answer must contain:

```json
{
  "response_contract": {
    "format": "visual_recap",
    "template": "executive-v4",
    "required_elements": ["metric_cards", "trend_chart", "source_footer"],
    "failure_policy": "fail_closed"
  }
}
```

The host validates the final answer against required_elements. Missing elements mean runbook_failed, never a silent text-only answer.

## Why this matters

- Financial reports need a fixed layout that compliance signed off on.
- Dashboards need consistent branding and a provable source line.
- Auditors need to know the format was enforced, not requested.

A format contract is the difference between "an agent that produces a report" and "an agent that produces THE report."

## Reference

- Repository: github.com/CorpusIQ/runbook-spec
- Response contract proposal: spec/response-contract-v1.1.md
- Render tool spec: World B implementation (image content blocks)
- MCP proposal: github.com/modelcontextprotocol/modelcontextprotocol/issues/3270

Prompt compliance is not governance. Output compliance is not optional either.
