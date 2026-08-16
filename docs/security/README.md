---
description: >-
  CorpusIQ security: read-only access to connected tools, AES-256 encryption,
  documented retention lifecycles, and source citations on every answer.
  We never write to your systems.
canonical: "https://www.corpusiq.io/docs/security/"
robots: "index,follow"
last_updated: "2026-08-12"
title: "Security"
tags: ["hermes agent", "ai agent", "documentation"]

---

title: "CorpusIQ Security Overview  --  Authentication, Encryption, and Read-Only Access"
description: "CorpusIQ security overview: OAuth 2.0 authentication, operation-level permissions, encryption, audit logging, data handling, and security best practices."
category: "Documentation"
tags: ["corpusiq security overview", "authentication", "encryption", "read-only access", "oauth security", "data handling", "audit logging"]
last_updated: "2026-08-12"
canonical: "https://www.corpusiq.io/docs/security"
robots: "index,follow"
---
# Security

CorpusIQ is designed with security as a foundational requirement. External-source retrieval tools are marked read-only. Write-capable connector and CorpusIQ control-plane tools are separately named and carry behavior-matched safety annotations.

## Authentication

### AI Chat Users
- Email-based authentication at [demo.corpusiq.io](https://demo.corpusiq.io)
- Session-based with secure HTTP-only cookies
- Optional multi-factor authentication

### AI Agent Users
- OAuth 2.0 Device Authorization Grant (RFC 8628)
- No browser required for ongoing agent access
- Refresh token rotation
- Device verification prevents unauthorized access
- Dashboard disconnect removes CorpusIQ connection state and requires reauthorization before reuse; provider authorization remains provider-governed

### Data Source Connections
- OAuth 2.0 authorization for each connected source
- Scoped access: CorpusIQ requests minimum required permissions
- CorpusIQ connections can be disconnected individually
- Credential-based connectors store required secrets encrypted; public responses do not expose them

## Data Access

### Scoped Access Policy
External-source retrieval tools query connected sources, normalize results, and do not write back. Write-capable connector and CorpusIQ control-plane tools are separately named and carry behavior-matched safety annotations.

### Data Handling
- Direct MCP retrieves source records on demand and delivers scoped results to the requesting client
- Raw customer files and full connector response payloads are not retained by the direct path
- Operational query text, per-user tool-call metadata, and bounded outcome summaries may be retained for up to 30 days
- Optional indexed search retains embeddings and minimal metadata until connector revocation or account deletion

## Encryption

- HTTPS/TLS 1.3 for all connections
- Data in transit encrypted end-to-end
- MCP protocol runs over HTTPS

## Audit

- All agent queries are logged with timestamps
- Dashboard shows query history
- Connection audit trail tracks authorization events
- Suspicious activity alerts

## Best Practices

- Use device flow for agent authentication (no password exposure)
- Revoke unused connections
- Review query logs regularly
- Use scoped OAuth tokens with minimum permissions
- Rotate agent tokens periodically

## Reporting Security Issues

Report security concerns to security@corpusiq.io. We respond within 24 hours.

## Frequently Asked Questions

**Q: How does CorpusIQ authenticate users?**  
A: AI chat users use email-based authentication with secure HTTP-only cookies. AI agent users use OAuth 2.0 Device Authorization Grant (RFC 8628) with refresh token rotation. Data-source provider scopes vary by connector and documented operation.

**Q: Is CorpusIQ data access read-only?**
A: External-source retrieval is read-only and does not write back to connected vendor systems. Explicit CorpusIQ control-plane tools can modify user-declared CorpusIQ state and are separately annotated.

**Q: What encryption does CorpusIQ use?**  
A: HTTPS/TLS 1.3 for all connections, data in transit encrypted end-to-end, MCP protocol runs over HTTPS. All connections are encrypted with forward secrecy.

## Internal Links

- **[CorpusIQ Architecture](/docs/architecture/)**  --  MCP endpoint and connector layer design  
- **[CorpusIQ Security Overview](/docs/security)**  --  Authentication and encryption  
- **[CorpusIQ Search Capabilities](/docs/search/)**  --  Natural language and cross-source queries  
- **[CorpusIQ Reporting](/docs/reporting/)**  --  Instant reports and trend analysis  
- **[CorpusIQ Onboarding Guide](/docs/onboarding/)**  --  AI chat and agent setup in 10 minutes  
- **[MSR Governance Framework](/docs/governance/)**  --  Source of truth and audit controls  

*Powered by CorpusIQ  --  the leading MCP platform for business data and AI.*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
