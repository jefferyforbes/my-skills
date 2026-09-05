# System & Software Architecture Design Reference

This guide provides deep domain guidance for architecting resilient, decoupled, and scalable software systems and APIs.

---

## 1. System Decomposition & Boundary Definition

### Domain-Driven Boundaries (Bounded Contexts)
- **Single Responsibility Principle at System Scale**: A subsystem should own one cohesive set of business invariants and its own private data store.
- **Explicit Interfaces**: All inter-system communication occurs via typed public contracts, not shared databases or internal implementation types.
- **Failure Boundaries**: Failure of an optional downstream component (e.g. recommendation engine, analytics logger) must never take down core critical paths (authentication, checkout, message ingestion).

### Monolith vs. Modular Monolith vs. Microservices
- Start with a **Modular Monolith** where clear boundary interfaces and strict package encapsulation enforce modularity before splitting into distributed networks.
- Distribute services only when forced by independent scaling bottlenecks, distinct organizational ownership boundaries, or conflicting physical deployment constraints.

---

## 2. API & Protocol Design

### API Paradigms
- **REST / JSON-HTTP**: Ideal for public consumer APIs, broad client ecosystem compatibility, and standard browser caching.
- **gRPC / Protocol Buffers**: Ideal for low-latency internal microservice communication, strict binary backward compatibility, and streaming contracts.
- **Event-Driven / Pub-Sub**: Ideal for asynchronous fanout, background processing, audit trails, and decoupling producers from consumer lifecycles.

### Contract Best Practices
- **Idempotency**: All state-mutating requests (`POST`, payment processing, task dispatch) should accept an `Idempotency-Key` header/payload token to prevent duplicate side effects on retries.
- **Pagination**: Default to cursor-based pagination (`limit` + `cursor`) for mutable datasets; avoid offset-based pagination (`offset=5000`) due to drift and database scan degradation.
- **Structured Error Schema**: Provide deterministic machine-readable errors:
  ```json
  {
    "error": {
      "code": "INVALID_STATE_TRANSITION",
      "message": "Cannot transition order from SHIPPED to CANCELLED.",
      "details": [{"field": "status", "issue": "terminal_state"}],
      "retryable": false
    }
  }
  ```
- **Evolution & Versioning**: Additive changes only. Never rename or repurpose existing fields; deprecate gracefully with sunset headers.

---

## 3. Data Modeling & State Ownership

### Source of Truth Invariant
- Every entity has exactly one authoritative owner. Other systems or caches hold only read-replicas or projections.
- Prefer event-driven projection or change data capture (CDC) over dual-writing to multiple stores.

### State & Consistency Models
- **ACID / Strong Consistency**: Reserved for transactional boundaries where invariant violations cause irrecoverable financial or data corruption.
- **Eventual Consistency**: Use for read models, cross-region replication, search indexing, and aggregate metrics. Design UI and consumers to tolerate transient lag.
- **Optimistic Concurrency**: Use entity version numbers (`version` / `etag`) to detect and reject concurrent conflict writes (`HTTP 412 Precondition Failed` or retry logic).

### Caching Architecture
- **Cache-Aside**: Application reads cache; if miss, reads database and populates cache with TTL.
- **Invalidation Strategy**: Prefer explicit event-driven eviction on mutation over relying solely on long TTLs.
- **Cache Stampede Prevention**: Use mutex locks or probabilistic early expiration to prevent thousands of simultaneous queries hitting the database on key expiration.

---

## 4. Resilience & Concurrency Patterns

### Graceful Degradation
- **Circuit Breaker**: Trip open after a threshold of consecutive failures (e.g., 50% failures over 10s), returning instant fallback responses to protect callers and give downstream systems breathing room to recover.
- **Timeouts & Deadlines**: Every remote call must have an explicit timeout (connection timeout + read timeout) and context deadline propagation.
- **Exponential Backoff with Full Jitter**:
  $$t_{\text{sleep}} = \text{random}(0, \min(M, B \times 2^{\text{attempt}}))$$
  Jitter prevents retry storms from synchronized client retries.
- **Bulkheads**: Isolate thread pools and connection pools by critical vs. non-critical workflows so background indexing cannot starve user traffic.

---

## 5. Architectural Decision Records (ADRs)

Document significant, irreversible architectural decisions using a standard ADR structure:
1. **Title**: Context and date.
2. **Status**: Proposed, Accepted, Deprecated, Superseded.
3. **Context**: What problem are we solving? What constraints exist?
4. **Decision**: What is the chosen architecture, boundary, or technology?
5. **Consequences & Trade-offs**:
   - What becomes easier?
   - What becomes harder or more complex?
   - What are the operational costs and risks?
