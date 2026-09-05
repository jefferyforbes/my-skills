---
name: code-review
description: Review code for correctness, maintainability, architecture, security, performance, testability, and alignment with existing project conventions. Use when reviewing existing code, evaluating implementation quality, validating code changes, or deciding whether an implementation should be improved before being considered complete.
---

# Code Review

# Operating Contract

This review operates under the root `AGENTS.md`.

Review for meaningful risk, not personal preference. Findings should be grounded in repository evidence and should distinguish observed facts from inference.

Review should prioritise:

1. Correctness
2. Data integrity
3. Security
4. Concurrency / lifecycle safety
5. Regression risk
6. Architecture
7. Maintainability
8. Performance
9. Testability
10. Style

Do not recommend changes solely because another implementation is aesthetically preferable.


## Purpose

Evaluate code based on how well it solves the actual problem within the context of the existing software system.

The objective is not to make code perfect.

The objective is to identify meaningful problems and improvements while preserving:

- Correctness.
- Simplicity.
- Maintainability.
- Appropriate architecture.
- Performance.
- Security.
- Testability.
- Existing project conventions.

---

# Core Principle

> **Review code for meaningful risk and quality, not personal preference.**

A good review asks:

```text
Does it work?
    ↓
Does it solve the intended problem?
    ↓
Could it break existing behaviour?
    ↓
Is it in the right architectural layer?
    ↓
Is it unnecessarily complex?
    ↓
Can it be maintained and tested?
    ↓
Are there meaningful risks?
```

---

# Review Context

Before reviewing non-trivial code, use `code-context`.

Understand:

- What the code does.
- Why it exists.
- Who calls it.
- What it depends on.
- What depends on it.
- Where state is owned.
- Existing project conventions.
- Relevant tests.

Do not evaluate code in isolation when surrounding context materially affects the review.

---

# Review Priorities

Review in this order:

```text
1. Correctness
2. Data integrity
3. Security
4. Concurrency / lifecycle safety
5. Regression risk
6. Architecture
7. Maintainability
8. Performance
9. Testability
10. Style
```

A correctness problem is more important than a formatting preference.

---

# Correctness

Look for:

- Incorrect logic.
- Incorrect assumptions.
- Missing edge cases.
- Incorrect state transitions.
- Nullability problems.
- Incorrect error handling.
- Invalid lifecycle assumptions.
- Incorrect concurrency.
- Incorrect persistence.
- Incorrect API behaviour.

Ask:

> Under what realistic conditions could this produce the wrong result?

---

# Edge Cases

Consider relevant boundaries such as:

- Empty input.
- Null/missing values.
- Zero.
- Negative values.
- Very large values.
- Very long strings.
- Duplicate data.
- Missing data.
- Concurrent operations.
- Retries.
- Partial failure.
- Network failure.
- Database failure.
- Process recreation.
- Configuration differences.

Do not enumerate hypothetical edge cases that cannot realistically occur.

---

# Architecture

Determine whether responsibilities live in the correct layer.

For example:

```text
UI rendering
→ Composable

UI state
→ State holder / ViewModel

Business rule
→ Domain / Use Case

Persistence
→ Repository / Data layer

Network protocol
→ Data/API layer
```

Look for:

- Incorrect dependency direction.
- Business logic in UI.
- Infrastructure leaking into domain code.
- Excessive coupling.
- Inappropriate abstractions.
- Broken module boundaries.

Do not demand architectural purity when the existing project intentionally uses a simpler pattern.

---

# Simplicity

Prefer the simplest implementation that correctly solves the problem.

Look for:

- Unnecessary abstractions.
- Premature generalisation.
- Excessive indirection.
- Overly configurable APIs.
- Duplicate layers.
- Unnecessary dependencies.
- Clever code that is harder to understand.

Ask:

> Is this complexity buying us something we actually need?

Do not simplify code merely to reduce line count.

---

# Abstractions

Before recommending a new abstraction, determine:

- Does the behaviour actually repeat?
- Is the responsibility coherent?
- Does the abstraction reduce meaningful duplication?
- Does it make testing easier?
- Does it clarify ownership?

Avoid abstractions created solely for hypothetical future reuse.

Prefer:

```text
Concrete implementation
        ↓
Actual repetition/problem
        ↓
Extract abstraction
```

over:

```text
Potential future reuse
        ↓
Premature abstraction
```

---

# API Design

Review public APIs for:

- Clear naming.
- Appropriate parameters.
- Sensible defaults.
- State ownership.
- Event ownership.
- Unnecessary coupling.
- Future compatibility.

For reusable Compose components, consider whether the API:

- Accepts a `Modifier`.
- Separates state from rendering.
- Emits events upward.
- Avoids ViewModel coupling.
- Avoids navigation coupling.
- Avoids unnecessary configuration.

Do not add parameters simply to make a component theoretically reusable.

---

# State

Check:

- Who owns state?
- Who can mutate it?
- Does the state have the correct lifecycle?
- Is state duplicated unnecessarily?
- Can multiple sources modify it incorrectly?
- Does state survive the lifecycle it needs to survive?

Prefer a single clear source of truth.

---

# Concurrency

When asynchronous work is involved, inspect:

- Cancellation.
- Structured concurrency.
- Race conditions.
- Duplicate operations.
- Ordering.
- Shared mutable state.
- Retry behaviour.
- Idempotency.

Ask:

> What happens if this operation runs twice, fails halfway through, or is cancelled?

---

# Error Handling

Review whether failures are:

- Detected.
- Propagated appropriately.
- Recoverable where appropriate.
- Presented to the correct layer.
- Logged appropriately.
- Avoiding sensitive information.

Avoid:

- Swallowing exceptions.
- Catching overly broad exceptions without reason.
- Treating every failure as recoverable.
- Hiding meaningful failures.

---

# Performance

Look for meaningful performance problems:

- Unnecessary allocations.
- Repeated expensive computation.
- Excessive database queries.
- Excessive network requests.
- Blocking operations.
- Unbounded memory usage.
- Inefficient algorithms.
- Unnecessary UI recomposition.

Do not raise micro-optimisations without evidence of meaningful impact.

---

# Compose Review

When reviewing Jetpack Compose code, additionally evaluate:

### State

- Correct state ownership.
- Appropriate state hoisting.
- Correct use of `remember`.
- Correct use of `rememberSaveable`.
- Avoidance of unnecessary duplicated state.

### Recomposition

Check for:

- Expensive work during composition.
- Incorrect side effects.
- Unnecessary recomposition.
- Misuse of `derivedStateOf`.
- Stability problems where they materially affect performance.

Do not add `@Stable` or `@Immutable` simply to silence analysis without understanding the underlying model.

### Side Effects

Review use of:

- `LaunchedEffect`.
- `DisposableEffect`.
- `SideEffect`.
- `rememberCoroutineScope`.

Ensure effects have appropriate keys and lifecycle.

### Layout

Check:

- Modifier ordering.
- Constraint behaviour.
- Intrinsic measurement.
- Weight.
- `fillMaxWidth`.
- Nested scrolling.
- Adaptive behaviour.

### Reusable Components

Prefer components that:

- Are appropriately stateless.
- Accept `Modifier`.
- Expose meaningful state/events.
- Are not unnecessarily tied to a specific screen.
- Do not directly depend on ViewModels.

---

# Device and Window Agnostic Code

For UI code, avoid:

- Hardcoded device dimensions.
- Device model checks.
- Layout assumptions tied to a single emulator.
- Fixed screen sizes where responsive sizing is appropriate.

Prefer layouts that respond to:

```text
Available window space
        ↓
Layout decision
```

rather than:

```text
Specific device
        ↓
Layout decision
```

---

# Kotlin Review

Review for idiomatic Kotlin where it improves clarity.

Consider:

- Null-safety.
- Sealed types.
- Data classes.
- Value classes.
- Extension functions.
- Scope functions.
- Collection operations.
- Coroutines.
- Flow.
- Smart casts.
- Exhaustive `when`.

Do not rewrite working code merely to make it look more idiomatic.

Clarity is more important than stylistic cleverness.

---

# Testability

Ask:

> Can the important behaviour be tested without requiring the entire application?

Look for:

- Hidden dependencies.
- Hardcoded infrastructure.
- Global state.
- Time dependencies.
- Randomness.
- Direct network/database access.
- UI/business logic coupling.

Prefer dependency boundaries that make meaningful behaviour easy to test.

---

# Security

Where relevant, inspect:

- Authentication.
- Authorisation.
- Input validation.
- Sensitive data handling.
- Secrets.
- Logging.
- File access.
- Network requests.
- Injection risks.

Only raise security findings when there is a plausible issue.

Do not manufacture theoretical vulnerabilities.

---

# Dependencies

When new dependencies are introduced, consider:

- Necessity.
- Existing alternatives.
- Maintenance cost.
- Compatibility.
- Security.
- Build impact.
- Application size.

Do not reject dependencies simply because an alternative exists.

---

# Evidence

Every substantive finding must have evidence.

For each finding identify:

```text
Evidence
   ↓
Reasoning
   ↓
Impact
   ↓
Confidence
```

Evidence may include:

- Source code.
- Callers.
- Tests.
- Runtime behaviour.
- Tool output.
- Documentation.
- Requirements.

Do not present assumptions as confirmed defects.

---

# Uncertainty

Explicitly identify uncertainty when it affects the conclusion.

Use:

```text
Observed
Inferred
Assumed
Unable to verify
```

Example:

```text
This appears to be safe based on the current callers, but the
external API contract was not available during review.
```

A lack of evidence is not evidence of correctness.

A lack of evidence is also not evidence of a defect.

---

# Findings

A substantive finding should include:

```markdown
#### [Severity] <Finding>

**Evidence**

<What was observed.>

**Impact**

<Why it matters.>

**Recommendation**

<What should change or be investigated.>

**Confidence**

<High / Medium / Low>
```

Keep findings concise.

---

# Severity

### Critical

Potential:

- Data loss.
- Security compromise.
- Severe production failure.
- Corruption.

### High

Potential:

- Significant production bug.
- Major regression.
- Broken core functionality.

### Medium

Potential:

- Realistic incorrect behaviour.
- Important maintainability problem.
- Meaningful performance issue.
- Important missing test coverage.

### Low

Potential:

- Minor maintainability concern.
- Small edge case.
- Non-critical improvement.

Do not use severity to make stylistic preferences appear important.

---

# No Finding Without Impact

Do not report:

```text
This could be cleaner.
```

Instead establish:

```text
This creates duplicate logic across three call sites, which means
future changes must be made in multiple places and can easily become
inconsistent.
```

If there is no meaningful impact, do not raise the finding.

---

# Avoid Nitpicking

Do not flag:

- Personal style preferences.
- Formatting handled by tooling.
- Minor naming preferences without ambiguity.
- Trivial refactors.
- Hypothetical future requirements.
- Code that is merely different from your preferred approach.

Follow the project's conventions.

---

# Don't Rewrite for Preference

Before recommending a change ask:

> Would this materially improve correctness, maintainability, performance, security, or clarity?

If not, it is probably not worth a review comment.

---

# Positive Findings

Meaningful positive observations are encouraged.

Examples:

- Good separation of responsibilities.
- Good state ownership.
- Effective reuse of an existing abstraction.
- Strong test coverage.
- Appropriate error handling.
- Simple solution to a complex problem.

Do not provide generic praise.

---

# Review Result

Conclude with one of:

### Good

No meaningful issues identified.

### Good With Suggestions

No blocking issues, but useful improvements exist.

### Needs Changes

One or more meaningful issues should be addressed.

### Needs Investigation

Important behaviour cannot be confidently evaluated with the available evidence.

---

# Review Output

Use:

```markdown
## Code Review

### Result

<Good | Good With Suggestions | Needs Changes | Needs Investigation>

### Summary

<Concise explanation of the implementation and overall quality.>

### Findings

#### [Severity] <Finding>

**Evidence**
...

**Impact**
...

**Recommendation**
...

**Confidence**
...

### Positive Observations

- <Meaningful positive observation>

### Testing

<Relevant tests reviewed or missing.>

### Uncertainty

- <Important unresolved question>

### Overall Assessment

<Concise final assessment.>
```

If there are no findings:

```text
No substantive issues identified.
```

Do not manufacture findings.

---

# Review Completion Checklist

Before completing a review:

- [ ] Context was understood.
- [ ] Intended behaviour was considered.
- [ ] Correctness was evaluated.
- [ ] Edge cases were considered.
- [ ] Architecture was evaluated.
- [ ] State ownership was evaluated.
- [ ] Concurrency was considered where relevant.
- [ ] Error handling was evaluated.
- [ ] Performance was considered where relevant.
- [ ] Security was considered where relevant.
- [ ] Testability was evaluated.
- [ ] Existing project conventions were considered.
- [ ] Findings have evidence.
- [ ] Findings have appropriate severity.
- [ ] Uncertainty is documented.
- [ ] Personal preferences were not presented as defects.
- [ ] No speculative findings were presented as facts.

---

# Guiding Principle

> **The purpose of code review is to improve the software, not to demonstrate that the reviewer can find things to criticise.**

A successful review leaves the codebase:

```text
More correct
More understandable
More maintainable
More reliable
```

without introducing unnecessary complexity or slowing development for insignificant reasons.
