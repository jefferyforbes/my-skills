# Code Context Exploration & Navigation Guide

This reference provides deep inspection workflows, dependency tracing techniques, and impact analysis checklists for `code-context`.

---

## 1. Tracing Techniques

### Caller Tracing
- Locate all call-sites using `grep_search(Query="functionOrClassName", SearchPath="...")`.
- Identify entry points: Are callers UI components, background workers, or external API controllers?
- Check if caller expectations (nullability, concurrency dispatchers) match the callee contract.

### Dependency & Data Flow Tracing
- Map where inputs originate: Passed via parameters, injected via DI, read from local database/Room, or fetched via network.
- Trace state mutations: Identify whether state changes are synchronous, emitted through a reactive stream (`Flow`, `LiveData`, `Observable`), or persisted.

---

## 2. Context Depth Levels

```text
Level 1: Requested file & immediate target symbols
   ↓ (expand only if insufficient)
Level 2: Direct callers, immediate dependencies & test fixtures
   ↓ (expand only if insufficient)
Level 3: End-to-end data flow, database schemas, & network contracts
   ↓ (expand only if insufficient)
Level 4: Cross-module boundaries & architectural layer contracts
```

---

## 3. Impact Assessment Matrix

| Change Scope | Boundary Checks Required |
| :--- | :--- |
| **Local Function** | Pure logic, nullability, return values. |
| **Class / Component** | Public methods, internal state encapsulation, thread safety. |
| **Module Boundary** | Public API visibility, DI module bindings, build dependencies. |
| **System-Wide** | Shared schemas, persistence migrations, cross-platform targets. |
