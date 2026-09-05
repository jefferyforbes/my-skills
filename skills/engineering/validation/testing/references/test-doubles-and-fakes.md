# Test Doubles, Fakes, Mocks & Determinism Reference

This reference provides architectural guidance on selecting test doubles and ensuring test determinism without brittle coupling.

---

## 1. Test Double Hierarchy

Prefer test doubles in this order:

```text
Real Implementation (Fast, in-memory, deterministic)
         ↓
Fake (Lightweight in-memory implementation of an interface, e.g. InMemoryTaskRepository)
         ↓
Stub (Configured fixed responses for specific test scenarios)
         ↓
Mock / Spy (Verify exact invocation counts — use sparingly)
```

> [!TIP]
> **Why Fakes Over Mocks**: Fakes test meaningful behavior without coupling your test to internal method calls or execution order. When code is refactored, tests backed by in-memory fakes continue to pass, while mock-heavy tests break falsely.

---

## 2. Test Determinism Rules

Flaky tests erode team confidence. Eliminate all non-determinism:
1. **Time & Clocks**: Inject a deterministic `Clock` or `TestDispatcher` (e.g. `StandardTestDispatcher` in Kotlin Coroutines) rather than `System.currentTimeMillis()`.
2. **Concurrency**: Never use `Thread.sleep()`. Use structured awaiting (`advanceUntilIdle()`, `await()`, or test coroutine schedulers).
3. **Randomness**: Use fixed seeds for UUIDs, IDs, and dummy data generators.
4. **Network & Disk**: Isolate network calls behind repository interfaces with in-memory backings during unit/integration tests.
