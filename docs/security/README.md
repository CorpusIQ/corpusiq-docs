# Security

CorpusIQ is designed with security as a foundational requirement. All access is read-only. We never write to your systems.

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
- Tokens can be revoked from the dashboard at any time

### Data Source Connections
- OAuth 2.0 authorization for each connected source
- Scoped access: CorpusIQ requests minimum required permissions
- Connections can be revoked individually
- No raw API keys stored or exposed

## Data Access

### Read-Only Policy
CorpusIQ is strictly read-only. We:
- Query data from your connected sources
- Normalize and present results
- Never write, modify, or delete data
- Never initiate transactions or changes

### Data Handling
- Data retrieved on-demand, not cached persistently
- Query results delivered directly to the requesting client
- No data warehousing or long-term storage of query results
- Transient processing only

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
