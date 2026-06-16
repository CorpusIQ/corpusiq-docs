# MCP Server Design Guide

Model Context Protocol (MCP) servers extend Hermes with custom tools and data sources. Designing an MCP server well means respecting both the protocol constraints and the human expectations of the Hermes community.

## When to Build vs. When to Buy

Before writing an MCP server, check if one already exists. The MCP ecosystem has hundreds of community and official servers covering common integrations. Search `agentskills.io`, `skills.sh`, GitHub, and the official MCP registry before starting from scratch.

**Build when:** your data source has no existing MCP server, you need custom behavior not available in the official implementation, you have strict security requirements that demand self-hosting, or you're integrating an internal system that will never be shared.

**Use an existing server when:** it covers your use case, it's actively maintained, it has reasonable test coverage, and it follows the standard MCP auth patterns. Contributing improvements to an existing server is often better than maintaining a fork.

**Avoid building when:** a simple REST API call from a skill would work. Not every integration needs an MCP server. If your "server" is a wrapper around one HTTP endpoint with no state, it might be better as a skill step.

## Tool Design Principles

**One tool, one responsibility.** A tool called `get_customer_data` that returns billing, shipping, and support history is doing too much. Split into `get_customer_profile`, `get_customer_billing`, and `get_customer_tickets`. Granular tools compose better and fail more predictably.

**Descriptive names and schemas.** The tool name should make its purpose obvious without reading documentation. `list_recent_orders` is better than `get_data`. Parameter descriptions should include examples and constraints. A developer unfamiliar with your service should be able to use your tool from the schema alone.

**Pagination by default.** Any tool that can return more than 50 items should support pagination (`limit`/`offset` or cursor-based). Unbounded responses consume context and crash downstream processing.

**Consistent error shapes.** Every error response should include: an error code (machine-readable), a message (human-readable), and optionally a `retry_after` hint for rate limits. Consistent error shapes mean consistent error handling across all tools.

**Sort and filter parameters.** Tools that list resources should accept common filter parameters where applicable. `list_users(role="admin", status="active", sort="last_login")` is immediately useful to anyone. A tool without filters is a data dump tool.

## Error Handling Strategies

**Timeouts are not failures.** Network timeouts happen. Your MCP server should have configurable timeouts per tool and retry transient failures with backoff. Log retry attempts so operators can identify persistent issues.

**Graceful degradation.** If your server depends on an upstream API and that API is partially degraded (some endpoints work, some don't), report what's available rather than failing entirely. A `get_customer` tool that can return basic profile data even when the purchases endpoint is down is more useful than one that returns a 500.

**Rate limit awareness.** If your upstream API has rate limits, your MCP server should track them and either queue requests or return clear `retry_after` guidance. Don't pass raw rate-limit errors to the caller — translate them into actionable responses.

**Validation before requests.** Validate parameters before making upstream calls. Catching a missing required field or an invalid date format server-side saves a round trip and a confusing error.

## Performance Considerations

**Connection pooling.** If your server makes HTTP calls, reuse connections. Opening a new TLS connection for every tool invocation adds 100-300ms of latency per call.

**Response size discipline.** Return only what's needed. If the user asked for "top 5 customers by revenue," they don't need the full billing history for each customer. Filter and limit at the server level before returning to Hermes.

**Bulk operations.** When a tool conceptually supports batching (e.g., fetching 50 records by ID), provide a batch endpoint that accepts an array. Fifty individual calls are dramatically slower than one batch call.

**Caching with care.** Cache upstream responses where appropriate, but respect freshness requirements. Stock prices need second-level freshness. Company profiles might be cacheable for hours. Document your caching strategy so callers understand staleness risk.

## Server Lifecycle

**Development.** Local development with mock upstream. All tools should be testable without live credentials. Use a test harness that validates schema compliance.

**Beta.** Deployed with real credentials but limited access. Run for at least a week with real usage before labeling production. Monitor error rates and latency.

**Production.** Full deployment with monitoring, alerting, and documented SLAs. Tools are stable, schemas are unlikely to change, and error handling covers known failure modes.

**Maintenance.** Regular updates for upstream API changes. Deprecate tools gracefully with advance notice and migration guidance. Never silently change a tool's behavior — version the tool or add a new one.

**Sunset.** Remove only after all consumers have migrated. Provide a sunset timeline (minimum 30 days for community servers) and a migration guide.

## Testing Your MCP Server

**Schema compliance.** Every tool must match the MCP specification. Validate with the official MCP validator before publishing.

**Unit tests per tool.** Test each tool with valid inputs, invalid inputs, edge cases (empty results, maximum results, special characters in parameters).

**Integration tests.** Test against a sandbox environment of your upstream service. Verify that tools work end-to-end with realistic data.

**Performance tests.** Measure response time for typical queries. A tool that takes 10 seconds to return will frustrate users regardless of how well it's designed.

**Security review.** Check that your server doesn't expose credentials, doesn't log sensitive data, and properly authenticates callers. Community MCP servers run with real credentials — treat security as a blocker, not an afterthought.
