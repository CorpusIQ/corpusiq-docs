---
title: "MCP Apps Stateless Design Pattern: Surviving ChatGPT and Claude Hosts"
description: "Practical pattern for building stateless MCP Apps that render correctly on every host. Why host state replay fails, and how to design apps that re-render from the tool result."
canonical: "/hermes/mcp/mcp-apps-stateless-design/"
robots: "index, follow"
tags: [mcp, apps, stateless, design, pattern, chatgpt, claude, ui]
last_updated: "2026-08-21"
---

# MCP Apps Stateless Design Pattern

MCP Apps lets tools return interactive UIs that render inside the AI
conversation. The pattern is powerful, but host implementations differ.
One rule makes the app work everywhere: design it stateless.

## Why stateless

Two host behaviors break stateful apps:

1. Metadata stripping. Some clients do not pass the full tool result
   metadata to the app layer. If your app depends on data carried in
   `_meta`, it silently breaks on those hosts.
2. No replay after refresh. When the user refreshes the app view, the
   host does not replay the original tool call. A widget that waits for
   a second round trip gets stuck loading forever.

A stateless app never depends on either behavior. It renders
completely from the data already present in the tool result.

## The pattern

1. Return everything the UI needs in the tool result itself. Values,
   labels, deltas, and source references live in the result payload,
   not in a follow-up call.
2. Render from the result. The app receives the result and renders.
   No state initialization call, no re-fetch, no host round trip.
3. Treat refresh as re-render. A refresh just re-renders from the same
   result data. It cannot hang because there is nothing to wait for.
4. Keep navigation internal. Drill-downs filter the data already in
   the result. Do not call back to the server for sub-views.

## Example flow

User asks a business question.

1. The tool executes and returns the answer: metrics, deltas, sources,
   and a reconciliation summary, all in one structured result.
2. The app view renders the dashboard from that result.
3. The user clicks a metric card. The app expands the detail from the
   same result payload. No server call.
4. The user refreshes. The host re-renders the view from the last
   result. Nothing to replay, nothing to wait for.

## Why this matters for business answers

For business intelligence the pattern is not just a compatibility
trick. A stateless, result-driven app makes every answer reproducible.
The rendered dashboard is a direct function of the verified tool
result, so the same question always renders the same answer, on any
host, after any refresh.

## Related pages

- [MCP Apps: Interactive UIs](/hermes/mcp/mcp-apps-interactive-ui/)
- [MCP Apps Enterprise Adoption](/hermes/mcp/mcp-apps-enterprise-adoption/)
- [MCP 2026-07-28 Spec](/hermes/mcp/mcp-spec-2026-07-28/)
