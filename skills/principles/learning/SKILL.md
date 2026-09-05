---
name: learning
description: Explain the important decisions behind work performed by the agent without unnecessarily narrating every implementation detail. Use when making non-trivial code or architectural changes, especially when a decision involves trade-offs, surprising behaviour, a workaround, a hack, a best-practice deviation, or an opportunity for meaningful learning.
---

# Learning

## Purpose

Allow the agent to perform implementation work efficiently while preserving the user's opportunity to understand and learn from important decisions.

---

## Core Principle

> **Do the manual work. Explain the meaningful decisions.**

Do not narrate routine steps ("I opened file X, edited line Y"). Explain decisions that are non-obvious, controversial, architectural, or involve trade-offs.

---

## When to Explain

Explain a decision when at least one applies:
1. **Trade-off**: There are meaningful advantages and disadvantages between valid approaches.
2. **Non-Obvious Behaviour**: Implementation behaves differently than typical intuition (e.g. modifier ordering, recomposition pitfalls, coroutine scopes).
3. **Architectural Decision**: State ownership, module boundaries, data flow, API contracts.
4. **Best-Practice Deviation**: Deliberately diverging from common conventions with a justified context.
5. **Workaround / Hack**: Temporary solutions or external issue mitigations (must never be silently hidden).
6. **Irreversible / High-Cost Decisions**: Database schemas, public interfaces, persistence strategies.

---

## When NOT to Explain

Avoid explaining routine implementation details:
- Obvious syntax or standard library methods.
- Routine file imports, formatting, or mechanical refactorings.
- Standard unit test execution commands.
- Implementation details with no meaningful architectural decisions behind them.

---

## Explanation Priority & Formats

When reporting, prioritize:
1. Architectural decisions & state ownership
2. Significant trade-offs
3. Root cause discoveries & bug fixes
4. Workarounds / hacks
5. Non-obvious framework quirks

### Decision Reporting Formats
Keep explanations concise and evidence-based:
- **Standard Decision**: State choice, rationale, and specific trade-off.
- **Trade-off Comparison**: Approach chosen vs rejected alternative, reason, and downside.
- **Workarounds**: Explicitly identify problem, temporary solution, trade-off, and future cleanup.

---

## Deep References

Load on-demand via `view_file`:
- **[Decision Reporting Formats & Illustrative Examples](./references/decision-examples.md)**: Concrete code examples (Compose state, modifier order, LazyColumn, architecture boundaries) and domain checklists.
