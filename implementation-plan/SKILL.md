---
name: implementation-plan
description: Create a concise, evidence-based implementation plan before making non-trivial code changes. Use when a task spans multiple files, layers, states, components, or architectural decisions, or when implementation could otherwise drift from the requested outcome.
---

# Implementation Plan

## Purpose

Create a concise plan that explains **what will change, where, why, and how it will be verified** before implementation begins.

The plan should reduce wasted work without becoming unnecessary bureaucracy.

---

# Core Principle

> **Plan enough to prevent wrong work, but not so much that planning becomes the work.**

---

# When to Plan

Use an implementation plan when a change:

- Spans multiple files.
- Spans multiple architectural layers.
- Changes APIs.
- Changes state ownership.
- Changes database/schema behaviour.
- Requires multiple UI states.
- Requires adaptive UI.
- Has meaningful technical trade-offs.
- Has significant regression risk.
- Is difficult to reverse.

For trivial changes, skip the formal plan.

---

# Inputs

Before planning, use:

- `requirements-analysis` when requirements are ambiguous.
- `code-context` when existing implementation/context matters.
- Relevant specialised skills.

Do not create a plan based solely on the user's description if the repository can answer important questions.

---

# Plan Structure

A good plan should answer:

```text
What?
Where?
Why?
Dependencies?
Risks?
Verification?
```

---

# Plan Format

Use:

```markdown
## Implementation Plan

### Objective

<What the change will accomplish>

### Current State

<Relevant existing behaviour>

### Approach

<Concise implementation strategy>

### Changes

1. `<file/module>` — <change>
2. `<file/module>` — <change>
3. `<file/module>` — <change>

### Tests

- <test / behaviour>

### Verification

- <build>
- <test>
- <runtime/UI verification>

### Risks

- <risk>

### Trade-offs

- <decision and alternative>

### Out of Scope

- <excluded work>
```

---

# Keep Plans Small

Prefer:

```text
1. Update state model.
2. Update ViewModel event.
3. Update composable.
4. Add tests.
5. Runtime verify.
```

over:

```text
1. Open file.
2. Search class.
3. Search function.
4. Edit line.
...
```

The plan describes **engineering work**, not keystrokes.

---

# Implementation Order

Prefer an order that reduces uncertainty.

Typical:

```text
Understand
 ↓
Define / update contract
 ↓
Implement core behaviour
 ↓
Connect layers
 ↓
Add tests
 ↓
Runtime verification
 ↓
Review
```

For risky changes, establish regression protection earlier.

---

# Dependencies

Identify dependencies between changes.

Example:

```text
Data model
    ↓
Repository
    ↓
ViewModel
    ↓
UI
    ↓
UI tests
```

Do not implement downstream code before understanding the contract it depends on.

---

# Risk

Identify only meaningful risks.

Examples:

- Backwards compatibility.
- Existing callers.
- State migration.
- Data migration.
- Concurrency.
- UI regression.
- API compatibility.

---

# Trade-offs

Record meaningful decisions.

Example:

```markdown
### Trade-off

**Chosen:** Keep the state local to the screen.

**Alternative:** Move it into the ViewModel.

**Why:** The state has no business meaning and does not need to
survive beyond the screen lifecycle.

**Cost:** The state cannot be shared with another screen without
changing ownership later.
```

---

# Acceptance Criteria

The plan must identify observable completion criteria.

Example:

```text
- Existing behaviour remains unchanged.
- New state renders correctly.
- Error state is handled.
- Relevant tests pass.
- Screen verified on compact and expanded configurations.
```

---

# Plan vs Implementation

The plan is a guide, not a contract.

If implementation reveals new information:

1. Stop.
2. Update the plan.
3. Explain the meaningful change.
4. Continue.

Do not blindly follow an invalid plan.

---

# Scope Control

The plan should explicitly prevent unrelated work.

Use:

```markdown
### Out of Scope

- Database redesign.
- Unrelated UI refactoring.
- Dependency upgrades.
```

when useful.

---

# Verification-First Planning

Every meaningful plan should answer:

> How will we know this worked?

Possible evidence:

- Unit tests.
- Integration tests.
- UI tests.
- Screenshot comparison.
- Build.
- Runtime behaviour.
- Logs.
- Performance measurements.
- Security checks.

Do not define success solely as:

> "Code compiles."

---

# Final Plan Review

Before implementation verify:

- [ ] Objective is clear.
- [ ] Current behaviour is understood.
- [ ] Relevant files are identified.
- [ ] Implementation approach is clear.
- [ ] Dependencies are understood.
- [ ] Important risks are identified.
- [ ] Tests are identified.
- [ ] Verification is defined.
- [ ] Scope is bounded.
- [ ] Important trade-offs are documented.

---

# Guiding Principle

> **A good implementation plan makes the implementation obvious without pretending the future is completely predictable.**
