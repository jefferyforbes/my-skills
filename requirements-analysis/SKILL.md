---
name: requirements-analysis
description: Translate user requests into clear implementation requirements, constraints, acceptance criteria, and edge cases before coding. Use when a request is ambiguous, spans multiple behaviours, involves UI/design requirements, or could be interpreted in multiple ways.
---

# Requirements Analysis

## Purpose

Turn a request into a precise understanding of **what needs to change and what must remain unchanged**.

---

# Core Principle

> **Solve the intended problem, not merely the words in the request.**

---

# Extract

Identify:

- User intent.
- Desired outcome.
- Functional requirements.
- Non-functional requirements.
- Constraints.
- Existing behaviour to preserve.
- Out-of-scope behaviour.
- Acceptance criteria.

---

# Clarify Ambiguity

Before asking the user a question, determine whether the repository, existing behaviour, design, or documentation can resolve it.

Ask only when the ambiguity materially affects implementation.

---

# Requirement Structure

Use:

```text
Goal:
<desired outcome>

Current:
<existing behaviour>

Change:
<required change>

Constraints:
<constraints>

Must preserve:
<existing behaviour>

Out of scope:
<excluded work>

Acceptance:
<observable definition of done>
```

---

# Acceptance Criteria

Prefer observable criteria.

Bad:

```text
Make the screen better.
```

Good:

```text
The screen must display the loading, empty, content and error states.
```

---

# Edge Cases

Identify realistic edge cases relevant to the requirement.

Do not turn every theoretical possibility into a requirement.

---

# Scope

Explicitly identify what should **not** change when useful.

This prevents agent drift.

---

# Design Requirements

For UI requests, identify:

- Visual requirements.
- States.
- Interactions.
- Responsive behaviour.
- Accessibility.
- Assets.
- Content constraints.

When multiple design references exist, establish how they relate.

---

# Technical Constraints

Identify relevant:

- Architecture.
- Platform.
- API compatibility.
- Database compatibility.
- Performance.
- Security.
- Dependency restrictions.

---

# Requirement Confidence

Distinguish:

```text
Explicit
Inferred
Assumed
Unknown
```

Do not turn an inference into a requirement without evidence.

---

# Output

```markdown
## Requirements

### Goal

...

### Requirements

- ...

### Constraints

- ...

### Must Preserve

- ...

### Out of Scope

- ...

### Acceptance Criteria

- ...

### Open Questions

- ...

### Assumptions

- ...
```

---

# Guiding Principle

> **Good requirements reduce wasted implementation.**
