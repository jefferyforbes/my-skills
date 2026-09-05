---
name: skill-authoring
description: Guidance for creating and maintaining composable agent skills that minimise context cost while preserving capability.
---

# Skill Authoring

## Purpose

Create skills that are composable, discoverable, maintainable, and economical in context.

Skills are capabilities, not essays.

---

## Core Principle

> **Keep operational rules in the skill; defer deep knowledge to references.**

Prefer:

```text
SKILL.md
    ↓
What to do
When to use it
Decision rules
Required verification
    ↓
references/
    ↓
Deep domain knowledge
Examples
API details
Long-form guidance
```

---

## Skill Structure

A useful skill should answer:

1. What capability does this provide?
2. When should it be used?
3. What must the agent understand before acting?
4. What workflow should it follow?
5. What decisions require judgement?
6. How should the result be verified?
7. What should be reported?

---

## Avoid Duplication

Do not repeat rules already defined by:

- root `AGENTS.md`
- parent skills
- shared principles

Add only the specialised behaviour required by the skill.

---

## Context Budget

Prefer concise rules over repeated prose.

Move detailed material into references when:

- it is only needed for specific cases;
- it is large;
- it changes independently;
- it contains examples or API documentation;
- it is useful knowledge but not required for every invocation.

---

## Composition

A skill should have one clear responsibility.

If a skill repeatedly invokes another capability, consider whether it should:

- reference that skill;
- compose with that skill;
- become a higher-level orchestration skill.

Do not create a hierarchy merely for folder organisation.

---

## Verification

Every skill that changes or evaluates something should define its evidence of success.

A skill must never claim work was verified when the verification was not actually performed.

---

## Evolution

When changing a skill:

- preserve useful existing behaviour;
- identify contradictions before resolving them;
- remove duplication carefully;
- prefer consolidation over deletion when capability can be preserved;
- update activation criteria when the skill's responsibility changes.

Treat skills as software modules: cohesive, loosely coupled, and independently understandable.
