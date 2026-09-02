---
name: observability
description: Design and review logging, metrics, tracing, diagnostics, and operational visibility so software behaviour can be understood and debugged in real environments. Use when implementing background work, APIs, distributed flows, important user journeys, or production-sensitive systems.
---

# Observability

## Purpose

Ensure important software behaviour can be understood when something goes wrong.

---

# Core Principle

> **If a production failure cannot be diagnosed, the system is not sufficiently observable.**

---

# Think in Flows

For important operations identify:

```text
Start
 ↓
Important step
 ↓
External dependency
 ↓
State transition
 ↓
Completion
```

Ask:

> If this fails, how would we know where it failed?

---

# Logging

Logs should help answer:

- What happened?
- When?
- To what operation?
- Where?
- Why?

Prefer structured logs where supported.

---

# Do Not Log Sensitive Data

Avoid logging:

- Passwords.
- Tokens.
- Secrets.
- Personal data.
- Sensitive request bodies.

Log identifiers only when appropriate and safe.

---

# Metrics

Use metrics for behaviours that benefit from aggregation.

Examples:

- Request latency.
- Error rate.
- Queue depth.
- Job duration.
- Retry count.
- Cache hit rate.

Do not create metrics merely because they are possible.

---

# Tracing

Use tracing when operations cross meaningful boundaries.

Example:

```text
API
 ↓
Service
 ↓
Queue
 ↓
Worker
 ↓
External API
 ↓
Database
```

Tracing should help connect these operations.

---

# Background Jobs

Important background processes should expose enough information to diagnose:

- Creation.
- Start.
- Retry.
- Failure.
- Completion.
- Permanent failure.

Consider:

- Job ID.
- Correlation ID.
- Attempt count.
- Duration.
- Failure reason.

---

# Error Reporting

Important unexpected failures should be visible through appropriate error reporting.

Do not hide exceptions merely to keep logs clean.

---

# Mobile Observability

For mobile applications consider:

- Crash reporting.
- Important failure events.
- Network errors.
- Background task failures.
- State restoration failures.

Avoid excessive analytics disguised as observability.

---

# Operational Questions

For important features ask:

```text
Can we tell if it is broken?
Can we tell who/what is affected?
Can we identify where it broke?
Can we determine why?
Can we measure recovery?
```

---

# Trade-offs

Observability has costs:

- Storage.
- Performance.
- Noise.
- Privacy.
- Maintenance.

Prefer high-value signals over logging everything.

---

# Output

```markdown
## Observability

### Signals Added

- ...

### Failure Visibility

<What failures can now be diagnosed?>

### Sensitive Data

<What was deliberately excluded?>

### Remaining Blind Spots

...
```

---

# Guiding Principle

> **Collect enough evidence to diagnose important failures without turning the system into a noisy surveillance system.**
