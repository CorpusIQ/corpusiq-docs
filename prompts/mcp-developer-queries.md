---
title: MCP Developer Query Prompts
description: CorpusIQ prompts for MCP developers — build, debug, and deploy Model Context Protocol servers connected to business data
---

# MCP Developer Queries

Ask these in Claude or ChatGPT with CorpusIQ connected. Each prompt targets a real MCP development task.

## Build a New MCP Server

> I need to build an MCP server for [platform]. Show me the OAuth flow documentation, API rate limits, and data schema. Generate a starter server in TypeScript that exposes [specific endpoints].

## Debug Connector Auth

> The [connector] OAuth is failing with a 401. Check my token scopes, verify the redirect URI, and compare against the vendor's current OAuth requirements.

## Compare API Approaches

> Compare the REST API vs GraphQL endpoint for [platform]. Which one gives me better query flexibility for business data? Show rate limits and pagination differences.

## Schema Design

> I'm building a connector for [platform]. Analyze its API documentation and recommend a normalized data schema. What fields should I expose as tools vs return in structured responses?

## Performance Optimization

> My MCP server for [platform] is timing out on queries with more than 30 days of data. Show me pagination strategies, cursor-based vs offset, and batch request patterns that work for this API.

## Rate Limit Strategy

> What's the optimal rate-limit handling for [platform]? Show me their current limits, recommended backoff strategy, and how to implement request queuing with priority levels.

## Testing MCP Endpoints

> Generate a test suite for my MCP server. I need: connection test, auth token refresh test, rate-limit handling test, and a full query-by-query validation against the vendor's sandbox.

## Multi-Source Query Design

> How do I design a multi-source query that pulls from Shopify orders, Stripe payments, and QuickBooks invoices — then reconciles them into a single response? Show the dependency graph and error handling for partial failures.

## Security Audit

> Audit my MCP server configuration for security issues. Check: token storage, scope minimization, input sanitization, error message leakage, and transport security.

## Deploy to Production

> I'm ready to deploy my MCP server. Show me the hosting options (Docker, Cloudflare Workers, AWS Lambda), environment variable management, and monitoring setup for production traffic.

## Custom

Combine any of these queries. CorpusIQ handles multi-source analysis natively — just describe what you need to build or debug.

---

*← [Prompt Library](/prompts/) | [MCP Architecture →](/docs/how-it-works/mcp-architecture.html)*
