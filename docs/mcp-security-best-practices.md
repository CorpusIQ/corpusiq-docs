---
title: "MCP Security Best Practices: OAuth & Token Management"
description: "Complete guide to MCP server security: OAuth 2.0 scopes, encrypted token management, read-only access defaults, audit trails, TLS encryption, and SOC 2"
category: MCP Education
tags: ["MCP security best practices", "secure AI data integration", "OAuth AI authentication", "read-only data access security", "AI audit trails", "SOC 2 AI compliance"]
last_updated: "2026-08-14"
canonical: https://www.corpusiq.io/docs/mcp-security-best-practices
robots: index,follow
---

# MCP Security Best Practices: How to Safely Connect Business Data to AI

Security is the first question every business leader asks about AI data integration  --  and rightly so. Connecting an AI model to your financial systems, CRM, and analytics platforms creates a new data access surface that must be secured deliberately. **MCP's security model** combines OAuth 2.0 authentication, read-only access defaults, encrypted token storage, comprehensive audit trails, and stateless architecture to protect business data at every layer.

## The MCP Security Model

MCP's security model rests on several architectural decisions:

**Operation-level safety.** MCP supports reads and writes. CorpusIQ marks external-source retrieval tools read-only and exposes write-capable connector-management and CorpusIQ control-plane tools separately with behavior-matched annotations.

**OAuth 2.0 authentication.** Every connection to a third-party platform uses OAuth 2.0, the industry standard for delegated authorization. Users grant CorpusIQ specific, scoped permissions rather than sharing credentials.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

**Encryption in transit.** All communication between the MCP client, server, and source APIs uses TLS 1.3 encryption. Data is never transmitted in cleartext.

**Encryption at rest.** Authentication tokens and configuration data stored by CorpusIQ are encrypted at rest using AES-256. Even if the storage layer were compromised, tokens would be unreadable.

## OAuth Scopes: The Principle of Least Privilege

OAuth 2.0 scopes determine what an MCP server can do with a connected platform. Best practice is to request the minimum scopes necessary for the intended use case.

CorpusIQ's approach:
- **Source-specific scopes.** CorpusIQ requests the provider scopes needed for each documented operation. Read-only retrieval tools and write-capable connector-management or control-plane tools remain separately named and safety-annotated even when a provider groups permissions into broader scopes.
- **Explicit operation boundaries.** Read-only retrieval tools and write-capable connector-management or CorpusIQ control-plane tools are separately named and carry explicit safety annotations.
- **Per-connector scope configuration.** Each connected platform has independently configured scopes. One connector's authorization does not widen another connector's access.
- **Scope visibility.** The provider authorization screen displays the requested source scopes. CorpusIQ tool names and annotations disclose whether each published operation is read-only or write-capable.

## Token Management

OAuth tokens are the keys to your data. Managing them securely is critical:

**Short-lived access tokens.** Access tokens issued by most OAuth providers expire after about one hour and are used only while valid. Refresh tokens, when provided, follow the encrypted-at-rest lifecycle described below.

**Encrypted refresh token storage.** Refresh tokens (which can obtain new access tokens) are stored encrypted at rest using AES-256 with per-user key derivation. Even our operations team cannot extract raw refresh tokens.

**Automatic token rotation.** When a refresh token is used to obtain a new access token, some providers also rotate the refresh token. CorpusIQ handles this rotation transparently, ensuring the latest refresh token is always stored.

**Token revocation.** Users can disconnect a connected platform through the CorpusIQ dashboard. The service commits an inactive state before credential cleanup; cleanup failures are surfaced for retry rather than reported as successful deletion. Provider-side revocation remains available through the connected platform.

**Cross-user isolation.** Each user's tokens are cryptographically isolated. User A's Shopify token cannot be used to access User B's data, even if both users are in the same CorpusIQ organization. This isolation extends to the database layer  --  tokens are stored with user-scoped encryption keys.

## Tool Boundary Architecture Deep Dive

The distinction between read-only retrieval and write-capable CorpusIQ-owned state changes deserves deeper examination.

**Protocol-level enforcement.** CorpusIQ's MCP server validates every tool call against a capability matrix. Tools marked as read-only cannot execute write operations. Write-capable connector-management and control-plane tools are separately named and annotated.

**API-level guardrails.** Connector implementations validate the requested operation and source-specific authorization. A write-capable tool can execute only its declared action; it does not silently widen a read-only retrieval call.

**AI-client visibility.** MCP tool definitions expose operation-specific names, descriptions, schemas, and safety annotations. Clients can distinguish retrieval tools from write-capable connector-management and CorpusIQ control-plane tools before invocation.

**Invocation remains explicit.** A write-capable operation runs only when that separately named tool is invoked with valid parameters and authorization. Client confirmation behavior is governed by the selected AI client's interface and policy.

This defense-in-depth approach makes write-capable operations visible and bounded. It reduces unintended-change risk without claiming that modification is architecturally impossible.

## Audit Trails

Every tool call through CorpusIQ's MCP server is logged, creating a complete audit trail:

- **Timestamp**  --  when the query was executed
- **User identity**  --  who asked the question
- **Tool name**  --  which connector and operation was called
- **Parameters**  --  what filters and arguments were used
- **Source system**  --  which platform was queried
- **Response status**  --  success, error, or timeout

This audit trail serves multiple purposes:
- **Security monitoring**  --  detect unusual query patterns that might indicate compromise
- **Compliance**  --  demonstrate data access controls for SOC 2, GDPR, and other frameworks
- **Debugging**  --  trace why a particular answer was returned
- **Usage analytics**  --  understand which data sources are most frequently accessed

Audit logs are retained according to the user's plan and can be exported for integration with SIEM systems or compliance reporting.

## Data Minimization

MCP's stateless architecture naturally enforces data minimization  --  the principle that you should only process the data you need, for as long as you need it.

CorpusIQ uses read-only access for direct MCP live retrieval. It does not retain raw customer files or full connector response payloads; operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.

**No data aggregation across customers.** Each customer's queries are processed in isolation. CorpusIQ does not aggregate, analyze, or learn from customer data.

**Minimal metadata.** The only persistent data CorpusIQ maintains is: authentication tokens (encrypted), connector configuration (which platforms are connected, with what scopes), and audit logs (which tools were called, when, and by whom).

This data minimization approach narrows the retained data classes that must be handled in a data subject request. Requests still account for operational logs retained for 30 days and optional indexed-search records until revocation or account deletion.

## Network Security

**TLS 1.3 everywhere.** All communication channels use TLS 1.3, including: client-to-server (your AI interface to CorpusIQ), server-to-API (CorpusIQ to source platforms), and internal service communication (within CorpusIQ's infrastructure).

**API gateway.** All inbound requests pass through an API gateway that provides rate limiting, request validation, and DDoS protection.

**VPC isolation.** CorpusIQ's production infrastructure runs in a virtual private cloud with network segmentation between services. The MCP server layer has outbound internet access (to reach source APIs) but no inbound access from the public internet  --  all client requests route through the API gateway.

**IP allowlisting (Enterprise).** Enterprise customers can restrict access to their CorpusIQ instance to specific IP ranges, ensuring that only requests from their corporate network are accepted.

## Compliance Considerations

**SOC 2.** CorpusIQ maintains a SOC 2 aligned security posture; formal SOC 2 Type II certification is not claimed.

**GDPR.** CorpusIQ's data-minimization approach scopes retention by product path. Direct MCP does not retain raw customer files or full connector response payloads; operational logs are retained for up to 30 days, while optional indexed search and compliance records have separate lifecycles.

**HIPAA.** CorpusIQ is not designed for protected health information (PHI) and should not be used with healthcare data subject to HIPAA without a Business Associate Agreement (BAA).

**Custom compliance requirements.** Enterprise customers with specific compliance needs can work with CorpusIQ on custom deployment configurations, including dedicated infrastructure and enhanced audit capabilities.

## Best Practices for Users

Beyond what CorpusIQ provides, users should follow these practices:

**1. Use dedicated service accounts where possible.** When connecting platforms that support service accounts (separate from personal user accounts), use them. This limits the blast radius if tokens are compromised.

**2. Review OAuth scopes periodically.** Check which permissions you've granted to CorpusIQ for each connected platform. Remove any that are broader than necessary.

**3. Rotate credentials after personnel changes.** If an employee with access to your CorpusIQ account leaves the organization, rotate OAuth tokens for all connected platforms.

**4. Monitor audit logs.** Periodically review the audit trail for unusual query patterns  --  queries at unusual times, against unexpected data sources, or with unusual parameters.

**5. Enable multi-factor authentication.** Use MFA on your CorpusIQ account and on all connected platforms to prevent unauthorized access.

**6. Limit AI model access to necessary data sources.** Connect only the platforms needed for your use case. Don't connect your entire SaaS portfolio if you only need access to three platforms.

## FAQ: Common Questions

<details>
<summary><strong>Can CorpusIQ employees see my business data?</strong></summary>

CorpusIQ restricts production access through least-privilege controls. Direct MCP does not retain raw customer files or full connector response payloads, while operational logs retain query text, per-user tool-call metadata, and bounded outcome summaries for up to 30 days.
</details>

<details>
<summary><strong>What happens to my data if I cancel my CorpusIQ account?</strong></summary>

To request deletion of account data, contact privacy@corpusiq.io. CorpusIQ responds to privacy requests within 30 days. Operational logs remain subject to the 30-day Azure Log Analytics retention window.
</details>

<details>
<summary><strong>How do you prevent AI models from leaking data across customers?</strong></summary>

Each query is processed in isolation. The AI model receives only the data from the current user's query. CorpusIQ does not use customer data to train or fine-tune models; conversation handling follows the selected AI provider's plan and settings.
</details>

<details>
<summary><strong>Can I use CorpusIQ with on-premise data sources?</strong></summary>

Yes. MCP servers can be deployed on-premise and connect to internal systems. If both the MCP server and AI client run inside your network, provider data can remain within that boundary; otherwise the chosen AI client's processing path and retention policy also apply.
</details>

<details>
<summary><strong>What security certifications does CorpusIQ hold?</strong></summary>

CorpusIQ maintains a SOC 2 aligned security posture and is CASA Tier 2 certified by DEKRA. Formal SOC 2 Type II certification is not claimed.
</details>

## Internal Links

- [Learn what an MCP server is and how it works](/docs/what-is-an-mcp-server)
- [Understand how MCP servers work with a technical deep dive](/docs/how-mcp-servers-work)
- [Discover the business benefits of MCP servers](/docs/benefits-of-mcp-for-business)
- [Learn about MCP for enterprise-scale deployments](/docs/mcp-for-enterprise)
- [Learn about MCP for financial reporting and compliance](/docs/mcp-for-finance)
- [See how executives use MCP for AI-powered dashboards](/docs/mcp-for-executives)

*[CorpusIQ](https://www.corpusiq.io)  --  AI answers grounded in your business data. 30-day free trial.*

*[CorpusIQ](https://www.corpusiq.io)  --  AI answers grounded in your business data. 30-day free trial.*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
