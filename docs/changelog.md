---
title: "CorpusIQ Changelog - CorpusIQ Docs"
description: "Complete CorpusIQ changelog and version history. Track API updates, new endpoints, connector additions, security improvements, and breaking changes. Follows"
category: "Documentation"
tags: ["corpusiq changelog", "api updates", "version history", "release notes", "new features", "breaking changes", "semantic versioning"]
last_updated: "2026-08-12"
canonical: "https://www.corpusiq.io/docs/changelog"
robots: "index,follow"
---
# Changelog

All notable changes to the CorpusIQ API are documented here. This project follows [Semantic Versioning](https://semver.org/).

---

## August 2026  --  Distribution Milestones

### Claude Custom Connector Support

Claude users can add the public CorpusIQ MCP endpoint through Claude's custom connector flow. CorpusIQ is not yet listed in Anthropic's Connector Directory, so setup currently requires entering the endpoint manually.

### MCP Auth Refresh (silent, no re-login)

The MCP server now mints a 30-day refresh token after a successful device or Google OAuth reconnect. Token refresh is silent: expired access tokens rotate automatically without user interaction.

---

## v1.0  --  March 2026

### Initial API Release

The first public release of the CorpusIQ API, providing programmatic access to the platform's core query, archive search, and data management capabilities.

### New Endpoints

- **`POST /v1/query`**  --  Search across all connected business tools with natural-language queries. Supports connector scoping via the `connectors` parameter and returns semantically ranked, cited results from each matching connector.

- **`POST /v1/deep_search`**  --  Search the encrypted archive of previously executed queries and their results. Supports date-range filtering and returns similarity-scored matches.


### Authentication

- Bearer token authentication via `Authorization` header
- 60-minute token expiry with server-side refresh detection
- Token issuance through the CorpusIQ Dashboard and ChatGPT Actions
- Dashboard disconnect commits inactive CorpusIQ connection state; provider-side authorization remains governed by the provider

### OpenAPI Specification

- Complete OpenAPI 3.0.3 spec published at `https://mcp2.corpusiq.io/mcp`
- Importable into Postman, Insomnia, and Swagger UI
- Interactive documentation at `https://mcp2.corpusiq.io/mcp`


### Rate Limiting

- Per-endpoint rate limits with minute and daily windows
- Rate limit headers on every response for self-monitoring
- `retry_after_seconds` field in `429` responses

### Security

- Operation-level safety annotations distinguish external-source retrieval from write-capable management/control-plane tools
- Scoped data handling: direct MCP live retrieval plus optional indexed-search embeddings
- TLS 1.3 for all API traffic
- AES-256-GCM encryption at rest
- SOC 2 Type II compliance program initiated

### Connectors

- 40+ native connectors spanning email, calendar, file storage, analytics, CRM, ecommerce, marketing, financial, social media, and databases
- Provider scopes match each connector's documented operations
- Direct database connectors for PostgreSQL, SQL Server, MySQL, Azure Cosmos DB, and MongoDB

### Documentation

- Published [CorpusIQ Documentation](/docs/) covering API reference, authentication, rate limits, security, and quick start
- Connector catalog with descriptions for all supported integrations
- Code examples in cURL, JavaScript, and Python for all endpoints

---

## Versioning Policy

| Version Component | Change Trigger |
|-------------------|----------------|
| **Major (X.0)** | Breaking changes to endpoint signatures, response schemas, or authentication |
| **Minor (1.X)** | New endpoints, new optional fields, new connector support |
| **Patch (1.0.X)** | Bug fixes, performance improvements, documentation updates |

CorpusIQ will provide at least 90 days' notice before deprecating any API version. Deprecated versions continue to function during the notice period with a `Deprecation` header on responses.

## Frequently Asked Questions

**Q: What versioning scheme does CorpusIQ use?**  
A: CorpusIQ follows Semantic Versioning (SemVer). Major versions (X.0) indicate breaking changes, minor versions (1.X) add new features, and patch versions (1.0.X) are bug fixes and improvements.

**Q: How much notice is given before API deprecation?**  
A: CorpusIQ provides at least 90 days' notice before deprecating any API version. Deprecated versions continue to function with a Deprecation header on responses during the notice period.

**Q: How many connectors does CorpusIQ currently support?**  
A: As of the v1.0 release (March 2026), CorpusIQ supports 40+ native connectors across email, calendar, file storage, analytics, CRM, ecommerce, marketing, financial, social media, and databases.

## Internal Links

- **[CorpusIQ Quick Start Guide](/docs/quick-start)**  --  Go from zero to first query in 5 minutes  
- **[API Reference](/docs/api/overview)**  --  Full REST API documentation  
- **[CorpusIQ Connectors](/docs/connectors)**  --  All 50+ supported integrations  
- **[Enterprise AI Data Access Guide](/docs/enterprise-ai-data-access)**  --  SSO, SOC 2, data residency  
- **[CorpusIQ Security Documentation](/docs/security)**  --  Certifications, encryption, and compliance  
- **[CorpusIQ Changelog](/docs/changelog)**  --  API updates and version history  
- **[Secure AI Data Connectivity](/docs/secure-ai-data-connectivity)**  --  Encryption and network security  

*Powered by CorpusIQ  --  the leading MCP platform for business data and AI.*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
