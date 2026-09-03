---
name: code-context
description: Build a focused understanding of the existing codebase before making requested code changes. Use when a code change requires understanding surrounding architecture, dependencies, data flow, conventions, state ownership, callers, tests, or existing implementations before deciding how to modify the code.
---

# Code Context

## Purpose

Build enough context around a requested code change to make an informed implementation decision **before modifying code**.

The goal is not to understand the entire codebase.

The goal is to understand the **smallest relevant system surrounding the requested change**.

The output should give the agent a reliable mental model of:

```text
Request
   ↓
Relevant code
   ↓
Dependencies
   ↓
Data / control flow
   ↓
Constraints
   ↓
Existing patterns
   ↓
Implementation options
```

---

# Core Principle

> **Understand before modifying.**

Do not immediately edit the first file that appears relevant.

First determine:

1. Where the behaviour originates.
2. Where it is consumed.
3. What it depends on.
4. What depends on it.
5. What patterns the project already uses.
6. What constraints the requested change introduces.
7. What the smallest appropriate change is.

Do not explore unrelated parts of the codebase.

---

# When to Use

Use this skill when:

- Implementing a new feature in an existing codebase.
- Modifying existing behaviour.
- Fixing a bug.
- Refactoring code.
- Changing an API.
- Changing state management.
- Changing database or network behaviour.
- Modifying UI behaviour.
- Changing architecture.
- Working in an unfamiliar repository.
- The impact of a change is unclear.

For trivial, isolated changes where the relevant implementation is already obvious, extensive context gathering is unnecessary.

---

# Context Depth

Use the **minimum context necessary**.

Start narrow and expand only when required.

```text
Level 1
Requested file / symbol

      ↓ if insufficient

Level 2
Direct callers + dependencies

      ↓ if insufficient

Level 3
Data flow + state + infrastructure

      ↓ if insufficient

Level 4
Wider architecture + cross-module impact
```

Do not inspect the entire repository by default.

---

# Workflow

## 1. Parse the Request

Identify:

- Desired behaviour.
- Current behaviour if known.
- Requested scope.
- Explicit constraints.
- Expected outcome.
- Technologies involved.
- Potentially affected areas.

Convert the request into a concrete change statement:

```text
Current:
<existing behaviour>

Requested:
<new behaviour>

Expected:
<observable result>

Constraints:
<constraints>
```

If the request is ambiguous, determine whether the ambiguity can be resolved from the codebase before asking the user.

---

# 2. Locate the Entry Point

Find the most relevant:

- Screen
- Composable
- Class
- Function
- API
- Repository
- Database operation
- State holder
- Use case
- Service
- Configuration
- Test

Do not assume the file named by the user is necessarily the source of the behaviour.

Trace the implementation until the actual behaviour is understood.

---

# 3. Read the Relevant Implementation

Read enough surrounding code to understand:

- Inputs
- Outputs
- State
- Side effects
- Dependencies
- Error handling
- Lifecycle
- Existing abstractions

Do not immediately propose changes.

First establish how the current implementation works.

---

# 4. Trace Callers

Determine who calls or consumes the relevant code.

For a function:

```text
Caller
  ↓
Function
  ↓
Dependency
```

For UI:

```text
Route
  ↓
Screen
  ↓
Component
  ↓
State / Event
```

For backend:

```text
Endpoint
  ↓
Service / Use Case
  ↓
Repository
  ↓
Data Source
```

Identify whether changing the target could affect existing callers.

---

# 5. Trace Dependencies

Identify important dependencies in the opposite direction.

Ask:

- What does this code depend on?
- Where does its data come from?
- Who owns its state?
- Where are side effects performed?
- Which abstractions does it rely on?

Do not trace every dependency.

Follow only dependencies relevant to the requested change.

---

# 6. Trace Data and Control Flow

Build a small mental model of how information moves through the system.

Example:

```text
User Action
    ↓
Composable
    ↓
Event
    ↓
ViewModel
    ↓
Use Case
    ↓
Repository
    ↓
Database
```

Or:

```text
S3
 ↓
Streaming Upload
 ↓
Background Job
 ↓
Transcription
 ↓
Task Extraction
 ↓
Database
 ↓
UI State
```

Identify where the requested behaviour should actually be implemented.

---

# 7. Inspect Existing Patterns

Before introducing a new approach, search for existing examples.

Look for:

- Similar features.
- Similar components.
- Existing abstractions.
- Naming conventions.
- Error handling patterns.
- State management patterns.
- Testing patterns.
- Dependency injection patterns.
- Networking patterns.
- Database patterns.
- UI patterns.

Prefer established project conventions unless there is a good reason not to.

---

# 8. Inspect Tests

Find relevant:

- Unit tests.
- Integration tests.
- UI tests.
- Screenshot tests.
- Fixtures.
- Test utilities.

Determine:

- What behaviour is already guaranteed?
- What assumptions are encoded?
- What tests should change?
- What new behaviour needs verification?

Tests are part of the system context, not an afterthought.

---

# 9. Identify Constraints

Look for constraints that may affect implementation.

Examples:

### Architecture

- Module boundaries
- Dependency direction
- Public APIs
- Shared/platform code

### UI

- Existing design system
- Window/adaptive behaviour
- State ownership
- Accessibility

### Backend

- API compatibility
- Idempotency
- Transactions
- Concurrency

### Data

- Schema compatibility
- Migrations
- Existing records
- Serialization

### Product

- Existing user behaviour
- Backwards compatibility
- MVP scope

---

# 10. Identify Change Impact

Classify the expected impact.

### Local

Only one component or file is affected.

### Module

Multiple files within one module are affected.

### Cross-module

Interfaces or dependencies cross module boundaries.

### System-wide

The change affects multiple layers or external contracts.

Use the smallest implementation scope that safely satisfies the requirement.

---

# 11. Determine the Correct Change Location

Before implementing, answer:

> Where should this behaviour live?

Prefer placing behaviour at the layer that owns the responsibility.

Examples:

```text
UI rendering
→ Composable

Screen state
→ State holder / ViewModel

Business rule
→ Domain / Use Case

Persistence
→ Repository / Data layer

Network protocol
→ API / Data layer
```

Do not place logic in a convenient location merely because it is easy to access.

---

# 12. Identify Existing Reusable Code

Before creating anything new, search for:

- Existing components.
- Existing utilities.
- Existing interfaces.
- Existing state models.
- Existing extensions.
- Existing test helpers.
- Existing design-system components.

Prefer reuse when the existing abstraction actually matches the requirement.

Do not force unrelated behaviour into an existing abstraction.

---

# 13. Identify Risks

Before implementation, identify likely risks.

Examples:

- Breaking existing callers.
- Changing public API behaviour.
- Incorrect state ownership.
- Race conditions.
- Lifecycle problems.
- Recomposition problems.
- Database migration issues.
- Backwards compatibility.
- Platform-specific coupling.
- Performance regressions.

Prioritise risks that could materially affect the implementation.

---

# 14. Form an Implementation Hypothesis

Once sufficient context has been gathered, formulate:

```text
The requested change should probably be implemented in
<location>

because
<reason>

It will affect
<affected areas>

and should preserve
<existing behaviour>

The main risk is
<risk>.
```

This is a hypothesis, not a commitment.

If implementation reveals contradictory information, update the hypothesis.

---

# Context Boundary

Stop gathering context when you can confidently answer:

### Behaviour

> How does the current behaviour work?

### Ownership

> Which layer owns the behaviour?

### Dependencies

> What does it depend on?

### Consumers

> What depends on it?

### Patterns

> How does this project normally solve similar problems?

### Impact

> What could this change break?

### Implementation

> Where should the change be made?

If all seven can be answered, additional exploration is unlikely to provide proportional value.

---

# Do Not

Do not:

- Read the entire repository without reason.
- Inspect unrelated modules.
- Rewrite existing architecture unnecessarily.
- Introduce new patterns without checking existing ones.
- Assume the user's suggested implementation location is correct.
- Modify code while still trying to understand the system.
- Claim understanding based only on filenames.
- Ignore tests.
- Ignore callers.
- Ignore backwards compatibility.
- Ask the user for information that can be discovered from the repository.

---

# Output

When context gathering is complete, provide a concise context summary.

Use:

```markdown
## Context

### Current Behaviour

<How it currently works>

### Relevant Flow

<Short data/control flow>

### Key Files

- `<file>` — <responsibility>
- `<file>` — <responsibility>
- `<file>` — <responsibility>

### Existing Pattern

<Relevant project convention>

### Change Location

<Where the change should live and why>

### Impact

<What will be affected>

### Risks

- <risk>
- <risk>

### Implementation Direction

<Concise proposed approach>
```

Do not produce a lengthy repository tour.

Only include information that affects the requested change.

---

# Relationship With Other Skills

This skill should generally happen **before implementation-focused skills**.

Typical workflow:

```text
User Request
     ↓
Code Context
     ↓
Implementation / Debugging / Refactoring
     ↓
Testing
     ↓
Review
```

For example:

```text
code-context
      ↓
compose-ui
      ↓
testing
      ↓
code-review
```

The context skill should not replace specialised skills.

It prepares the context those skills need to operate correctly.

---

# Quality Criteria

Context gathering is successful when:

- [ ] The current behaviour is understood.
- [ ] The relevant entry point is identified.
- [ ] Important callers are known.
- [ ] Important dependencies are known.
- [ ] Data/control flow is understood.
- [ ] Existing project patterns have been checked.
- [ ] Relevant tests have been inspected.
- [ ] Change ownership is identified.
- [ ] Impact is understood.
- [ ] Important risks are identified.
- [ ] Further exploration would provide diminishing returns.

---

# Guiding Principle

> **Don't understand everything. Understand everything necessary to change this safely.**
