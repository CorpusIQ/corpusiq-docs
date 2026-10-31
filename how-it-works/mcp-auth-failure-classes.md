---
title: "MCP Authentication Failure Classes - CorpusIQ Docs"
description: "A field guide to the eight connection and OAuth failures that break MCP servers in production: symptoms, how to tell them apart, and the fix pattern for each."
last_updated: "2026-10-24"
---
# MCP authentication and connection failure classes

Most MCP connection failures are reported as one thing: "it does not
authenticate". In practice the failures split into a small number of
classes, and each class has a different fix. Choosing the wrong class is
why the same bug gets patched three times.

This page lists the eight classes we see most often across MCP servers,
SDKs, and bridges, in the order you should rule them out. Each one gives
the symptom, why it happens, and the fix pattern.

## How to narrow it down first

Before reading further, get four values from the failing run:

1. The HTTP status and error body from the token endpoint.
2. Whether the request reached the resource server at all.
3. Which process mutated the credential store, if any.
4. Whether the failure is local (credential generation) or remote (the
   server rejected what we sent).

A 401 from the token endpoint is not the same event as a 401 from the
resource server, and `invalid_grant` is not the same event as
`invalid_target`. Most misdiagnosis is one of those two conflations.

## 1. `invalid_grant` on refresh: the rotation race

**Symptom.** Two processes share one credential directory. One refreshes,
the other gets `invalid_grant`, and the client wipes the stored
credentials. The user is logged out for no visible reason.

**Why.** RFC 6749 section 5.2 returns `invalid_grant` for an expired, a
revoked, and an already-used refresh token. The client cannot tell
"another process rotated this a second ago" from "this login is dead" by
reading the error. Clearing on the first `invalid_grant` turns a routine
race into a logout. Retrying the same token is worse: servers with reuse
detection treat a second presentation of a retired token as a breach and
revoke the whole token family.

**Fix.** Make a generation counter the correctness mechanism, not a lock
alone:

- The credential record carries `generation`, `rotated_at`, and the
  refresh token, and is written to a temp file that is renamed into
  place, which makes the write atomic.
- A refresh reads generation G, exchanges, and writes G+1.
- On `invalid_grant`, re-read before acting. If the generation moved,
  another process already rotated: adopt the stored tokens and continue.
- Only clear when a re-read shows the same generation and no other
  process has refreshed recently. A writer may be between the token
  response and its rename.

Log the observed generation, the token endpoint status and body, plus the
pid and session id that cleared the login. That last field is what tells
you which process sent the losing request.

## 2. A local credential helper reported as a remote auth failure

**Symptom.** Every session on the machine loses an HTTP server for 15
minutes after a `headersHelper` fails once. Editing the helper does not
help. The failure is fast, not a timeout.

**Why.** The needs-auth cache is keyed by server name and written on the
shared 401 path. A helper-backed server should never reach that path: a
helper that produced nothing is a local credential generation failure,
not a server asking the user to authenticate. The entry is machine-wide,
time-boxed, and not invalidated when the server block changes.

**Fix.**

- Key the cache by `(server, auth_mode)` and never write an entry for a
  `headersHelper` server.
- Separate the local failure reasons. A helper timeout (often a keychain
  or SSO prompt waiting on a human) should retry once with backoff inside
  the session, and should never produce an auth requirement.
- Only treat a 401 as a remote auth failure when the helper did return a
  token. Store a hash of the header value, not the value, so new helper
  output invalidates the entry.
- Put a hash of the server config (url, command, args, env keys) in the
  key, so a fixed helper takes effect on the next start rather than after
  the TTL expires.

This matters beyond the single server: the pattern that makes a header
helper attractive is many HTTP servers with per-tenant credentials, none
of them OAuth. One failing helper disabling the set looks, from outside,
like every connector going unauthenticated at once.

## 3. Metadata validation stricter than RFC 8414

**Symptom.** A conformant authorization server with
`grant_types_supported: ["client_credentials"]` and no
`authorization_endpoint` is rejected at discovery.

**Why.** RFC 8414 section 2 requires `authorization_endpoint` only when a
grant type that uses it is supported, and defaults
`grant_types_supported` to `["authorization_code", "implicit"]` when the
field is absent. `response_types_supported` is still required, so an
empty array there is the correct shape, not a shortcut.

**Fix.** Do not make the field optional outright: that moves the failure
from `connect()` to `startAuthorization()`, after a round trip, where the
error is worse. Make the requirement grant-conditional and enforce it in
one place:

- Require `authorization_endpoint` when `grant_types_supported` is absent
  or contains `authorization_code` or `implicit`.
- Require `token_endpoint` unless the metadata advertises only `implicit`.
- When a provider is selected, assert its grant appears in
  `grant_types_supported` and fail with a typed error naming both the
  provider and the supported grant list. That also catches the inverse
  case: a client-credentials provider pointed at an authorization-code
  server.

Keep the base metadata record permissive. Strict schemas that strip
unknown keys force later features to re-fetch, and the grant checks read
better as a separate validation step.

## 4. Resource binding enforced only when the parameter is present

**Symptom.** A refresh token minted for one audience is accepted when it
is presented against another, or the client silently drops the `resource`
parameter and binding is never checked.

**Why.** If the handler only validates `resource` when the request
carries it, omitting the parameter becomes the bypass. Most clients send
nothing today, so enforcement-by-omission is the common shape of the bug,
not the rare one. String equality instead of URI normalization also
produces false mismatches: `https://as.example/mcp/` and
`https://as.example/mcp` name the same audience.

**Fix.** Compare against the binding already persisted on the grant, not
against the request alone:

- `resource` present and not matching the stored binding for the refresh
  token or authorization code is `invalid_target`, not `invalid_grant`.
  The latter sends integrators to the wrong layer.
- Normalize both sides before comparing, so a trailing slash does not
  change the verdict.
- `resource` absent must fall back to the stored binding and keep
  enforcing it. No parameter is not the same as no constraint.

## 5. Percent-encoding handled in the string domain

**Symptom.** A URI template round-trips fine in the unit test and then
raises `UnicodeEncodeError` when the value is serialized into a JSON-RPC
payload or an HTTP body.

**Why.** `surrogateescape` does not return valid UTF-8. It returns a
string containing lone surrogates in the U+DC80 to U+DCFF range. Those
survive `quote` and `unquote` with the same setting, which is why the
round-trip test passes, and then break the first `.encode("utf-8")`.
`json.dumps` will happily emit `"\udce9"`, and encoding the result
raises.

**Fix.** Keep the value in the byte domain: `unquote_to_bytes` on match,
`quote_from_bytes` on expand. Matching and expansion then never leave
bytes, which is what RFC 3986 section 2.1 describes, and any lossy
decision happens once at the boundary where a handler asks for text. If
`surrogateescape` stays, add the serialization case to the test table:
`json.dumps({"uri": value}).encode("utf-8")` must not raise.

The test that separates a real fix from a passing one: percent-encode a
byte that is illegal in UTF-8, expand it, serialize the way the transport
will, and assert the original octet comes back. String equality alone
passes for both designs.

## 6. Host and Origin validation by string prefix

**Symptom.** A local-only MCP server accepts requests whose `Host` or
`Origin` header is not local.

**Why.** A digits-only port check is necessary but not sufficient. Four
forms still pass it: an empty port (`127.0.0.1:`), an out-of-range or
zero-padded port (`:0080`, `:99999`), userinfo splicing (`127.0.0.1:80@evil.com`),
and an unbracketed IPv6 address (`::1:443` read as host `::1`).
`startsWith` on the raw header also ignores that `Host` is
case-insensitive.

**Fix.** Stop matching the header string. Parse it into an authority and
compare components: host exactly, port present and in range, brackets
mandatory on the IPv6 branch. Parse `Origin` as a full URI and compare
against the allowed origin the same way. One parse per request closes the
whole family instead of one regex per call site.

Test with the inputs that look valid: `127.0.0.1:evil.com`,
`127.0.0.1:80.evil.com`, `127.0.0.1:`, `[::1]:443x`,
`localhost:3000.evil.com`.

## 7. Bridges and proxies: the destination that was not validated

**Symptom.** A bridge or remote-proxy client is allowed to reach internal
addresses, or a token is sent to an endpoint the resource server chose.

**Why.** Three gaps recur:

- Redirects are validated at the first hop only. The bypass is the
  address the redirect resolves to, and a host that answers with a public
  address for the check and a private one for the connection defeats both
  checks.
- `token_endpoint` is attacker-named metadata that receives a secret.
- Proxy environment variables (`HTTPS_PROXY`) decide where the process
  actually connects, so a host allow-list enforced before the proxy is
  chosen can still be routed internally.

**Fix.** Re-validate at each hop and connect to the address that was
validated rather than re-resolving afterwards. Require the token endpoint
to be same-origin with the issuer it was selected from, or require
explicit user confirmation when it is not. State that proxy configuration
is part of the destination the user must be able to inspect.

## 8. Transport teardown on a late protocol notification

**Symptom.** A progress notification written immediately before a result
is reported as an unknown token, and the connection is dropped. The same
call succeeds when the notification is sent earlier.

**Why.** The client keeps an in-flight registry keyed by progress token
and retires the entry when it dispatches the result. When the
notification and the result arrive in the same read, the result can be
handled first, the token retired, and the notification then matches
nothing. Dropping the connection is the real defect: the call succeeded,
and a late notification for a completed request should at most be
ignored. Reusing a JSON-RPC request id as the progress token adds a
second failure, because a completed request's id can collide with a live
token if ids are recycled or both spaces share one map.

**Fix.** Retire the token only after the request completes and every
notification queued for it has been drained, and never let an unmatched
notification tear down the transport. Use an opaque token per request,
distinct from the id space.

## A note on ordering

The classes above are not equally likely, and they are cheap to tell
apart. Token endpoint status first, then whether the resource server was
reached, then which process wrote the credential store. Reaching for the
credential store before reading the token endpoint response is how a
rotation race becomes a logout, and how a broken header helper becomes a
15-minute outage.

If you are connecting CorpusIQ's MCP server and the failure does not fit
one of these, the endpoint is `https://mcp2.corpusiq.io/mcp` and the
[quick start](../quick-start.md) covers the client configuration.
