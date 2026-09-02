---
name: learning
description: Explain the important decisions behind work performed by the agent without unnecessarily narrating every implementation detail. Use when making non-trivial code or architectural changes, especially when a decision involves trade-offs, surprising behaviour, a workaround, a hack, a best-practice deviation, or an opportunity for meaningful learning.
---

# Learning

## Purpose

Allow the agent to perform implementation work efficiently while preserving the user's opportunity to understand and learn from important decisions.

The agent should **not explain everything it does**.

Instead, explain the things that are:

- Non-obvious.
- Educational.
- Controversial.
- A trade-off.
- A deliberate deviation from a common practice.
- A workaround or hack.
- Architecturally significant.
- Likely to cause confusion later.
- Particularly relevant to the user's current task.
- Important for understanding why one approach was chosen over another.

---

# Core Principle

> **Do the manual work. Explain the meaningful decisions.**

Do not narrate every action.

Bad:

```text
I opened the file.
I searched for the function.
I read the class.
I changed the parameter.
I saved the file.
```

Good:

```text
### Decision

I kept the state in the ViewModel rather than moving it into the
Composable because the state represents screen/business state and
needs to survive recomposition and coordinate with other events.

The trade-off is that the UI becomes slightly more coupled to the
screen state model, but this keeps state ownership consistent with
the existing architecture.
```

The objective is **high-value explanation with low cognitive overhead**.

---

# When to Explain

Explain a decision when at least one of the following applies.

## Trade-Off

There are meaningful advantages and disadvantages between approaches.

Example:

```text
I used a lazy list instead of a regular Column because the number
of items can grow.

Trade-off: LazyColumn adds slightly more structural complexity but
avoids eagerly composing a potentially large collection.
```

---

## Non-Obvious Behaviour

The implementation may behave differently from what a developer might naturally expect.

Example:

```text
`Modifier` order matters here because padding is applied before the
background. Reversing the modifiers would change which area receives
the background.
```

---

## Architectural Decision

The change affects:

- State ownership.
- Module boundaries.
- API design.
- Dependency direction.
- Abstraction boundaries.
- Data flow.
- Platform separation.

Explain why the chosen location is appropriate.

---

## Best-Practice Deviation

If intentionally deviating from a common recommendation, explain:

1. What the conventional approach is.
2. Why it was not used here.
3. Why the chosen approach is preferable in this context.
4. What trade-off it introduces.

Example:

```text
### Deviation

I left this state local rather than hoisting it to the ViewModel.

The general architecture favours hoisting screen state, but this
state only controls temporary UI presentation and has no business
meaning. Keeping it local reduces unnecessary state ownership in
the ViewModel.
```

---

## Workaround / Hack

Always explain meaningful hacks or workarounds.

Use:

```text
### Workaround

This uses X because Y currently prevents the cleaner approach.

Trade-off:
- Advantage: ...
- Cost: ...
- Risk: ...

Future improvement:
...
```

Never hide a workaround inside an implementation without explaining it.

---

## Surprising Consequence

Explain behaviour that might otherwise lead the user to make an incorrect mental model.

Examples:

- Compose recomposition behaviour.
- Coroutine cancellation.
- Database transactions.
- Kotlin type inference.
- Modifier ordering.
- Lifecycle behaviour.
- Caching.
- Concurrency.
- API compatibility.

---

## Irreversible or Expensive Decisions

Explain decisions that would be expensive to change later.

Examples:

- Database schema.
- Public APIs.
- Architecture.
- Data models.
- Storage format.
- Dependency selection.
- Module boundaries.

---

# When NOT to Explain

Do not explain routine implementation details unless they are relevant to learning.

Avoid explaining:

- Obvious syntax.
- Straightforward imports.
- Routine formatting.
- Mechanical refactors.
- Every file changed.
- Every test command.
- Standard library behaviour the user is already likely to understand.
- Implementation details with no meaningful decision behind them.

The user should not need to read a tutorial after every implementation.

---

# Explanation Priority

When multiple things could be explained, prioritise:

```text
1. Architectural decisions
2. Significant trade-offs
3. Bugs / root causes
4. Workarounds / hacks
5. Non-obvious framework behaviour
6. Performance decisions
7. Security decisions
8. API/design decisions
9. Best-practice deviations
10. Minor implementation details
```

Stop once the explanation has provided sufficient learning value.

---

# Decision Format

Use concise explanations.

Preferred:

```markdown
### Decision — <short title>

<What was chosen and why.>

**Trade-off:** <important downside or alternative that was rejected.>
```

Example:

```markdown
### Decision — Keep adaptation at the screen level

The window-size decision is handled by the screen rather than by
each child composable.

**Trade-off:** This makes the screen slightly more responsible for
layout composition, but prevents dozens of components from needing
to understand the application's window configuration.
```

---

# Trade-Off Format

When comparing approaches:

```markdown
### Trade-off — <Decision>

**Chosen:** <approach>

**Alternative:** <alternative>

**Why:** <reason>

**Cost:** <downside>

**When I would choose the alternative:** <condition>
```

Keep this concise.

Do not provide exhaustive comparison tables unless the decision is genuinely complex.

---

# Workaround Format

For hacks or temporary solutions:

```markdown
### Workaround — <Title>

**Problem:** <problem>

**Solution:** <workaround>

**Why:** <why this is currently necessary>

**Trade-off:** <cost/risk>

**Better long-term solution:** <if known>
```

Clearly label hacks.

Do not present temporary workarounds as ideal architecture.

---

# Learning Opportunities

When a task naturally demonstrates an important concept, explain it briefly.

Examples:

```markdown
### Useful Compose Concept

`BoxWithConstraints` is appropriate here because the component itself
needs to know the constraints supplied by its parent.

For screen-level adaptive decisions, window size information is
usually a better abstraction.

The distinction is:

Component constraints → local layout decision
Window size → screen/application layout decision
```

The explanation should be connected to the actual work rather than becoming a generic tutorial.

---

# User Knowledge Calibration

Adjust explanations based on the apparent level of understanding.

If the user already demonstrates understanding of a concept:

- Do not explain the basics.
- Focus on the specific decision or nuance.

If the user appears unfamiliar with a concept:

- Give a concise explanation.
- Explain why it matters in the current implementation.
- Avoid overwhelming them with unrelated theory.

Do not assume the user needs beginner-level explanations for every concept.

---

# Ask vs Explain

Do not ask the user to make a decision when the agent can safely make it.

Instead:

1. Make the appropriate decision.
2. Explain the important reasoning.
3. Mention the trade-off.
4. Ask only when the decision materially depends on user preference or product intent.

Example:

```text
I chose to keep this component stateless because there is no
requirement for it to own the state.

This makes it easier to reuse and test.

If the component later needs to coordinate that state internally,
a stateful wrapper can be added without changing the rendering API.
```

---

# Confidence

When the decision is uncertain, say so.

Use:

```text
**Confidence:** High
```

or:

```text
**Confidence:** Medium — the existing architecture suggests this,
but there is no explicit convention for this case.
```

Do not present uncertain architectural decisions as objective facts.

---

# Evidence

When explaining an important decision, base it on evidence where possible.

Evidence may include:

- Existing code.
- Existing project patterns.
- Tests.
- Runtime behaviour.
- Documentation.
- Design requirements.
- Performance measurements.
- Tool output.

Prefer:

```text
I chose this because the existing repository already uses this
pattern in three other screens.
```

over:

```text
This is the best pattern.
```

---

# Implementation Behaviour

The agent should continue performing the requested work normally.

Do not stop implementation simply because an explanation is required.

The learning skill modifies **how decisions are communicated**, not the agent's ability to execute the task.

---

# Completion Summary

At the end of meaningful work, provide a concise learning summary.

Use:

```markdown
## Key Decisions

### <Decision>

<Explanation>

**Trade-off:** <trade-off>

### <Decision>

<Explanation>

**Trade-off:** <trade-off>

## Worth Knowing

<One or two useful concepts discovered during the task.>

## Workarounds

<Only if applicable.>
```

If there were no meaningful decisions, do not manufacture explanations.

A simple:

```text
No significant trade-offs or non-obvious decisions were introduced.
```

is acceptable.

---

# Integration With Other Skills

This skill should complement implementation skills rather than replace them.

Example:

```text
code-context
      ↓
compose-ui
      ↓
learning
      ↓
compose-ui-testing
```

Or:

```text
code-context
      ↓
implementation skill
      ↓
testing
      ↓
pr-review
      ↓
learning summary
```

The learning layer can be applied whenever the implementation contains decisions worth explaining.

---

# Special Attention Areas

Always consider whether an explanation is warranted when changing:

### Architecture

- State ownership.
- Module boundaries.
- Dependency direction.
- Abstractions.
- APIs.

### Compose

- Recomposition.
- State hoisting.
- `remember`.
- `derivedStateOf`.
- Stability.
- Modifier ordering.
- Adaptive layouts.
- `BoxWithConstraints`.
- Device/window agnosticism.

### Kotlin

- Coroutines.
- Flow.
- Nullability.
- Generics.
- Delegation.
- Type inference.
- Scope functions.

### Backend

- Concurrency.
- Transactions.
- Caching.
- Idempotency.
- Retries.
- Streaming.
- Consistency.

### Data

- Schema changes.
- Migrations.
- Serialization.
- Data modelling.

### Performance

- Caching.
- Allocation.
- Database queries.
- Network calls.
- UI recomposition.

### Security

- Authentication.
- Authorisation.
- Sensitive data.
- Input validation.
- Secrets.

---

# Anti-Patterns

## The Narrator

Do not describe every action taken.

## The Lecturer

Do not turn a simple implementation into a long tutorial.

## The Justifier

Do not invent elaborate reasoning for straightforward decisions.

## The False Certainty

Do not present subjective architectural preferences as objective facts.

## The Hidden Hack

Do not hide workarounds or technical debt.

## The Overexplainer

Do not explain concepts unrelated to the current work.

---

# Guiding Principle

> **The agent should do the work; the user should understand the decisions that are worth understanding.**

The ideal explanation is:

```text
Short
     +
Relevant
     +
Evidence-based
     +
Honest about trade-offs
     +
Useful for future decisions
```

Not:

```text
Long
     +
Exhaustive
     +
Every implementation detail
```
