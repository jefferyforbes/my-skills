---
name: security
description: Evaluate and implement security controls for software changes, focusing on realistic threats, trust boundaries, sensitive data, authentication, authorisation, validation, secrets, and secure handling of external input. Use when changes affect users, data, authentication, APIs, storage, files, networking, or permissions.
---

# Security

## Purpose

Identify and prevent meaningful security risks without turning every theoretical possibility into a blocker.

---

# Core Principle

> **Security review should be threat-driven and evidence-based.**

---

# Trust Boundaries

Identify where untrusted data enters the system.

Examples:

```text
User input
 ↓
API
 ↓
Application
 ↓
Database
```

or:

```text
External service
 ↓
Deserializer
 ↓
Domain model
```

Treat external boundaries carefully.

---

# Authentication

Check:

- Credentials.
- Tokens.
- Sessions.
- Expiration.
- Authentication state.

Do not assume authentication implies authorisation.

---

# Authorisation

Ask:

> Is this user allowed to perform this operation on this resource?

Check:

- Ownership.
- Roles.
- Permissions.
- Resource-level access.

---

# Input Validation

Validate untrusted input at appropriate boundaries.

Consider:

- Type.
- Format.
- Size.
- Range.
- Allowed values.

Do not rely solely on UI validation.

---

# Sensitive Data

Identify:

- Personal data.
- Credentials.
- Tokens.
- Financial data.
- Private content.

Check:

- Storage.
- Transmission.
- Logging.
- Caching.
- Deletion.

---

# Secrets

Never hardcode:

- API keys.
- Passwords.
- Private keys.
- Tokens.

Check configuration and secret-management mechanisms.

---

# Logging

Ensure sensitive information is not accidentally logged.

Review:

- Request bodies.
- Authentication headers.
- Exceptions.
- Debug output.

---

# Files

For file operations consider:

- Path traversal.
- File type.
- File size.
- Permissions.
- Temporary files.
- Cleanup.

---

# Networking

Consider:

- TLS.
- Certificate validation.
- Authentication.
- Request validation.
- Response validation.
- Sensitive data exposure.

---

# Dependencies

For security-sensitive dependencies consider:

- Maintenance.
- Known vulnerabilities.
- Source.
- Required permissions.
- Dependency scope.

Do not introduce a dependency merely to solve a trivial problem.

---

# Evidence

For security findings establish:

```text
Threat
 ↓
Reachability
 ↓
Exploit / failure path
 ↓
Impact
```

Do not report theoretical vulnerabilities without a plausible path.

---

# Severity

Prioritise based on:

- Exploitability.
- Data sensitivity.
- Scope.
- User impact.
- Persistence.

---

# Security Output

```markdown
## Security Review

### Findings

#### [Severity] <Finding>

**Threat**

...

**Evidence**

...

**Impact**

...

**Recommendation**

...

**Confidence**

...

### Security Positives

...

### Remaining Risk

...
```

---

# Guiding Principle

> **Protect real trust boundaries and sensitive assets; do not create security theatre.**
