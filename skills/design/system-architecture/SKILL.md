---
name: system-architecture
description: Software and system architecture design, subsystem boundaries, API contracts, data modeling, concurrency, resilience, and trade-off analysis. Use when designing distributed systems, modular architectures, or backend services.
---

# System & Software Architecture Design

## Purpose

This skill guides the high-level structural design of software systems, distributed architectures, APIs, and data flows. It ensures components have clear ownership, strong boundaries, resilient failure modes, and well-reasoned trade-offs.

---

## Core Principles

1. **Architecture Manages Complexity**: Do not design sophisticated abstractions for simple problems. Keep boundaries clean and responsibilities unmistakable.
2. **Single Source of Truth**: Every entity and piece of state is authoritatively owned by exactly one system or module. All other usages are replicas or projections.
3. **Isolate Failure Domains**: A failure or slowdown in an optional downstream component must never cascade to take down core critical workflows.
4. **Explicit Contracts**: Systems interact strictly through versioned, typed public contracts, never through shared database state or internal implementation assumptions.

---

## Architectural Design Workflow

### 1. System Decomposition & Bounded Contexts
- **Responsibility**: What is this component's singular business domain responsibility?
- **Data Encapsulation**: Does this component own its private storage schema? (Avoid database-level coupling across service boundaries).
- **Dependency Flow**: Ensure dependencies point inward toward stable core/domain models, keeping transport and infrastructure details at the boundary.

### 2. API & Protocol Contract Design
- **Paradigm Selection**:
  - **REST / HTTP**: Public APIs, broad client ecosystem compatibility, cache-friendly endpoints.
  - **gRPC / Protobuf**: High-throughput inter-service communication, strict binary schemas, bidirectional streaming.
  - **Event-Driven / Pub-Sub**: Decoupled asynchronous tasks, fanout notifications, audit events.
- **Idempotency Invariant**: Ensure all mutating endpoints (`POST`, payments, task creation) accept an `Idempotency-Key` to safely allow automatic network retries without duplicate side-effects.
- **Cursor Pagination**: Use cursor-based pagination for mutable datasets; avoid deep offset pagination (`offset=10000`).
- **Structured Errors**: Return deterministic error schemas containing an error code, user message, field-level validation errors, and a `retryable` boolean.

### 3. State & Consistency Modeling
- **ACID vs. Eventual Consistency**: Restrict two-phase commit and distributed locks to strict financial/ledger invariants. Use eventual consistency and asynchronous events for read models and search indices.
- **Optimistic Concurrency**: Protect against write collisions using version numbers or ETags (`If-Match` / HTTP 412).
- **Caching Discipline**: Use cache-aside with explicit event-driven eviction. Prevent cache stampedes via mutex locks or probabilistic early recomputation.

### 4. Resilience & Concurrency Engineering
- **Timeouts & Deadlines**: Mandate explicit connection and read timeouts on every external network call. Propagate cancellation context.
- **Circuit Breakers**: Trip open when downstream error rates exceed thresholds to prevent caller thread exhaustion.
- **Exponential Backoff with Full Jitter**:
  $$t_{\text{sleep}} = \text{random}(0, \min(M, B \times 2^{\text{attempt}}))$$
- **Bulkheading**: Partition execution thread pools and connection pools so background processes cannot starve interactive user traffic.

---

## Verification & Proof

- [ ] **Contract Compatibility**: Automated contract or schema compatibility tests (e.g. Protobuf backward compatibility, OpenAPI linting).
- [ ] **Boundary Isolation**: Verify downstream service mocks confirm independent failure recovery.
- [ ] **Failure Mode Proof**: Verify behavior under simulated timeouts, retries, and network partitions.

👉 **Deep Reference**: Inspect [references/system-design.md](./references/system-design.md) via `view_file` for distributed patterns, caching strategies, and Architectural Decision Records (ADRs).
