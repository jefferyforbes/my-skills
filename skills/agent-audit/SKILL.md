---
name: agent-audit
description: >-
  Perform a full agentic audit of the current agent environment (skills, workflows, instructions, knowledge, context, tooling, documentation) to reduce context load, duplication, complexity, and maintenance overhead without degrading capability or behavior.
---

# Agent Audit Skill

## Purpose

Perform a full agentic audit of the current agent environment — including skills, workflows, instructions, knowledge, context, tooling, documentation, and supporting files — with the goal of **reducing context load, duplication, complexity, and maintenance overhead without degrading capability or behaviour**.

The audit should behave like a combination of:

- Architecture review
- Context optimisation
- Knowledge-base deduplication
- Skill refactoring
- Workflow optimisation
- Dependency analysis
- Regression testing

The desired outcome is a **smaller, clearer, more composable agent system that performs at least as well as the original system**.

---

# Core Principle

> **Condense context, not capability.**

Never optimise purely for fewer files, fewer words, or fewer skills.

A successful optimisation must preserve the important behaviours, constraints, decision rules, examples, workflows, and safety mechanisms contained within the original system.

Prefer:

```text
10 overlapping skills
        ↓
3 composable skills
        +
shared knowledge/context
        ↓
same capability
lower context cost
```

over simply deleting content.

---

# Audit Objectives

The audit should attempt to identify:

1. Duplicate skills
2. Overlapping skills
3. Repeated instructions
4. Repeated knowledge
5. Skills that should be merged
6. Skills that should be split
7. Skills that should inherit/reference another skill
8. Knowledge that should become shared context
9. Knowledge that should become reusable references
10. Instructions that can be expressed once instead of repeatedly
11. Workflows that contain unnecessary steps
12. Workflows that can be composed from existing skills
13. Skills containing excessive examples
14. Examples that can be replaced with general rules
15. Stale or contradictory instructions
16. Dead or unused skills
17. Skills with unclear activation criteria
18. Skills that duplicate capabilities already provided by tooling
19. Context that is loaded unnecessarily
20. Information that can be deferred until needed
21. Large files that should be split into core instructions + references
22. Small files that should be consolidated
23. Conflicting sources of truth
24. Repeated domain knowledge
25. Opportunities for hierarchical skill composition

---

# Audit Philosophy

## 1. Understand Before Changing

Never modify anything immediately.

First construct an understanding of the system.

Determine:

- What skills exist
- What each skill does
- What triggers each skill
- What tools each skill depends on
- What other skills it references
- What knowledge it assumes
- What workflows it implements
- Which skills overlap
- Which skills are foundational
- Which skills are specialised
- Which skills are rarely needed

Create an internal dependency map before proposing changes.

---

## 2. Treat Skills as Software

Skills should be analysed like software modules.

Evaluate:

- Cohesion
- Coupling
- Duplication
- Dependency direction
- Single responsibility
- Reusability
- Composability
- Discoverability
- Maintainability
- Context cost

A skill should ideally answer:

> "What capability does this provide that another skill does not?"

If the answer is unclear, investigate whether the skill should be merged, split, or removed.

---

# 3. Measure Context Cost

Estimate the context cost of the current system.

For each skill/document/workflow identify approximately:

- Token/word size
- Frequency of use
- Dependencies
- Overlapping content
- Amount of always-loaded information
- Amount of task-specific information
- Amount of repeated information

Prioritise optimisation where:

```text
context_size × usage_frequency
```

is high.

A large skill that is rarely used may be less important than a moderately sized skill loaded on every task.

---

# 4. Separate Core Rules From Supporting Knowledge

Look for opportunities to separate:

### Core instructions

Information that must be available whenever the skill executes.

Examples:

- Behavioural rules
- Required workflow
- Constraints
- Decision logic
- Validation requirements

### Supporting knowledge

Information only required in specific circumstances.

Examples:

- Long examples
- Reference documentation
- Edge cases
- Background explanations
- Detailed API references
- Historical decisions

Prefer:

```text
SKILL.md
    ↓
concise operational instructions

references/
    ↓
deep knowledge loaded only when required
```

rather than putting everything into the main skill.

---

# 5. Identify Stackable Skills

Look for skills that can be composed hierarchically.

For example:

```text
coding
├── implementation
├── testing
├── code-review
└── debugging
```

may be better represented as:

```text
engineering
├── implementation
├── testing
├── review
└── debugging
```

where shared engineering principles exist once in the parent skill.

Do not introduce hierarchy purely for organisation.

Only do so when it meaningfully reduces duplication or improves composability.

---

# 6. Find Repeated Instructions

Search for instructions appearing across multiple skills.

Examples:

```text
Always verify your changes.
```

```text
Run tests after making changes.
```

```text
Do not modify unrelated files.
```

```text
Prefer existing abstractions.
```

If the same principle appears repeatedly, determine whether it should become:

- A global rule
- A foundational skill
- A shared reference
- A reusable workflow component

Do not centralise instructions when doing so would make them harder to discover or incorrectly universal.

---

# 7. Preserve Local Specificity

Not all duplication is bad.

This:

```text
All code should be tested.
```

and:

```text
Compose UI changes require screenshot verification.
```

are not equivalent.

The second is specialised behaviour.

When consolidating, preserve the specialised portion.

A useful transformation is:

```text
Shared principle
+
specialised extension
```

rather than deleting the specialised instruction.

---

# 8. Detect Contradictions

Identify instructions that conflict.

Examples:

```text
Skill A:
Always use mocks.

Skill B:
Avoid mocks unless necessary.
```

or:

```text
Workflow A:
Run tests before implementation.

Workflow B:
Implement first, then test.
```

Contradictions must be surfaced before consolidation.

Determine:

1. Whether one rule supersedes another
2. Whether the rules apply in different contexts
3. Whether the contradiction is accidental
4. Whether a hierarchy or explicit precedence rule is required

Never silently resolve meaningful contradictions.

---

# 9. Detect Dead Knowledge

Identify:

- Obsolete instructions
- Deprecated workflows
- References to removed tools
- Old architecture
- Historical decisions no longer relevant
- Duplicate documentation
- Unused examples
- Dead skills
- References to files that no longer exist

Do not automatically delete historical information.

First determine whether it still has operational value.

---

# 10. Optimise Examples

Examples can be disproportionately expensive.

Evaluate every example:

> Does this example teach behaviour that cannot be expressed more cheaply as a rule?

Prefer:

```text
Rule + one representative example
```

over:

```text
Rule + 8 repetitive examples
```

However, retain examples when they clarify:

- Complex behaviour
- Ambiguous edge cases
- Formatting requirements
- Tool invocation patterns
- Important failure modes

---

# Audit Process

Perform the audit in phases.

## Phase 1 — Inventory

Catalogue the available:

- Skills
- Skill directories
- Workflows
- Knowledge files
- References
- Templates
- Agent instructions
- Configuration
- Tool definitions
- Supporting documentation

Produce an inventory before modification.

---

## Phase 2 — Semantic Mapping

For every relevant component determine:

```text
Name
Purpose
Inputs
Outputs
Triggers
Dependencies
Tools
Knowledge required
Other skills referenced
Approximate context cost
Overlap
Unique capabilities
```

Build a conceptual dependency graph.

---

## Phase 3 — Duplication Analysis

Search for:

- Identical instructions
- Semantically equivalent instructions
- Repeated knowledge
- Repeated workflows
- Repeated examples
- Repeated validation procedures
- Repeated tool usage instructions

Classify duplication as:

### Exact

Same information.

### Semantic

Different wording, same meaning.

### Functional

Different wording but same behaviour.

### Intentional

Repeated because local context genuinely requires it.

Only optimise the first three categories.

---

# Phase 4 — Capability Analysis

For every skill ask:

> What capability would disappear if this skill were removed?

Classify each skill:

- **Unique** — preserve
- **Foundational** — potentially promote
- **Composable** — potentially reuse
- **Overlapping** — consolidate
- **Redundant** — candidate for removal
- **Obsolete** — candidate for removal
- **Too broad** — candidate for splitting
- **Too narrow** — candidate for merging

Never remove a skill simply because another skill appears similar.

Prove capability coverage first.

---

# Phase 5 — Optimisation Proposals

Generate proposed changes such as:

```text
MERGE
A + B → C

MOVE
knowledge X → shared reference

EXTRACT
section Y → references/Y.md

PROMOTE
instruction X → foundational skill

SPLIT
large skill A → A-core + A-reference

REMOVE
obsolete skill B

REWRITE
skill C → condensed equivalent
```

For every proposed change explain:

```text
Current problem
Proposed change
Context reduction
Capability preserved
Potential risk
Verification required
```

---

# Phase 6 — Safe Refactoring

When making changes:

1. Preserve the original behaviour.
2. Avoid destructive edits until a replacement exists.
3. Keep a clear mapping between old and new capabilities.
4. Ensure every removed instruction has been accounted for.
5. Ensure every dependency still resolves.
6. **Verify Antigravity Directory Discovery Constraints:** Antigravity only discovers skills at exactly `skills/<skill_name>/SKILL.md`. Ensure that refactoring does NOT hide active skills in nested subdirectories (e.g., `skills/category/skill/SKILL.md`) unless they are intentionally designed as unmounted references linked from a top-level routing hub.
7. Ensure skill discovery remains understandable.
8. Ensure activation conditions remain clear.
9. **Fix Before You Delete:** Do not propose removing a capability solely because it contains broken links or missing scripts. You must actively search the filesystem, check for package replacements, or ask the user a clarifying question to restore the functionality before deciding to delete it.

Prefer incremental refactoring over a complete rewrite.

---

# Phase 7 — Regression Audit

After optimisation, perform a second audit.

Compare:

```text
BEFORE
↓
capabilities
workflows
rules
dependencies
context cost

AFTER
↓
capabilities
workflows
rules
dependencies
context cost
```

Verify that:

- No unique capability disappeared
- Important constraints survived
- Tool usage remains correct
- Workflows remain executable
- Skill triggers remain understandable
- References still resolve
- No contradictions were introduced
- No important edge cases disappeared
- No specialised behaviour was flattened into generic rules

---

# Capability Preservation Matrix

When consolidating skills, create a matrix similar to:

| Original Capability | New Location        | Preserved? | Verification |
| ------------------- | ------------------- | ---------: | ------------ |
| Capability A        | skill-x.md          |        Yes | Review       |
| Capability B        | shared/reference.md |        Yes | Test         |
| Capability C        | skill-y.md          |        Yes | Scenario     |
| Capability D        | Removed             |         No | Intentional  |

Every removed capability must be explicitly marked intentional.

There should be **no unexplained capability loss**.

---

# Context Optimisation Strategies

Prefer the following strategies in roughly this order:

### 1. Remove duplication

Highest confidence optimisation.

### 2. Extract shared knowledge

Create a single source of truth.

### 3. Consolidate overlapping skills

Reduce competing instructions.

### 4. Move deep knowledge to references

Keep operational skills concise.

### 5. Replace repetitive examples with rules

Reduce token cost while preserving understanding.

### 6. Introduce composition

Allow smaller skills to work together.

### 7. Introduce hierarchy

Only when shared behaviour genuinely exists.

### 8. Remove dead content

Delete only when confidently obsolete.

---

# Do Not Optimise These Away

Be especially careful with:

- Safety constraints
- Tool invocation requirements
- Validation steps
- Important edge cases
- Explicit user preferences
- Error handling
- Failure recovery
- Security requirements
- Domain-specific constraints
- Preconditions
- Postconditions
- Examples that disambiguate behaviour
- Instructions required for reliable tool use

A shorter skill is **not** automatically a better skill.

---

# Context Budget Principle

Optimise for:

```text
Capability / Context Cost
```

rather than:

```text
Minimum Context
```

The objective is to maximise:

> **Useful agent capability per token of context.**

A 20% larger skill that prevents major failures is better than a 20% smaller skill that causes regressions.

---

# Skill Quality Test

After optimisation, each skill should ideally satisfy:

### Purpose

Can its purpose be explained in one sentence?

### Activation

Is it clear when the skill should be used?

### Capability

Does it provide a distinct capability?

### Dependencies

Are dependencies explicit?

### Context

Does it avoid unnecessary information?

### Composition

Can it work alongside other skills?

### Consistency

Does it avoid conflicting instructions?

### Verification

Does it define how successful execution should be verified?

### Maintainability

Can a future agent/user understand where to modify it?

---

# Audit Severity

Classify findings:

### Critical

Potential capability loss, contradictory behaviour, broken dependency, or unsafe instruction.

### High

Significant duplication, context waste, or workflow inefficiency.

### Medium

Moderate duplication, unclear boundaries, unnecessary complexity.

### Low

Minor wording duplication, cosmetic organisation, or small optimisation opportunity.

Do not spend significant effort optimising low-impact issues while high-impact problems remain.

---

# Output Format

At the end of the audit produce:

## Executive Summary

Briefly state:

- Current system shape
- Major problems
- Largest context costs
- Biggest optimisation opportunities
- Expected impact

## Findings

For each significant finding:

```text
[FINDING]
Severity:
Type:
Affected:
Problem:
Recommendation:
Expected benefit:
Risk:
```

## Proposed Architecture

Show the recommended skill/knowledge structure.

Example:

```text
skills/
├── engineering/
│   ├── SKILL.md
│   ├── testing/
│   ├── review/
│   └── debugging/
│
├── product/
│   └── SKILL.md
│
└── shared/
    ├── principles.md
    └── verification.md
```

## Before vs After

Compare:

- Number of skills
- Approximate context size
- Duplicate instructions
- Shared knowledge
- Dependencies
- Complexity
- Capability coverage

## Capability Preservation

Provide the capability preservation matrix.

## Recommended Changes

Separate changes into:

### Safe to implement

High-confidence, low-risk improvements.

### Requires review

Changes where intent or behaviour could be ambiguous.

### Do not change

Content that should remain despite apparent duplication.

---

# Operating Rules

1. **Inspect before modifying.**
2. **Never delete unique capability without explicit justification.**
3. **Prefer consolidation over deletion.**
4. **Prefer references over repetition.**
5. **Prefer composition over giant universal skills.**
6. **Prefer one source of truth.**
7. **Preserve specialised behaviour.**
8. **Detect contradictions before merging.**
9. **Verify after refactoring.**
10. **Optimise context cost, not file count.**
11. **Do not sacrifice reliability for brevity.**
12. **Do not assume duplication is accidental.**
13. **Do not introduce abstraction solely for elegance.**
14. **Keep activation criteria explicit.**
15. **Treat every refactor as a potential regression.**

---

# Definition of Done

An audit is complete when:

- The relevant agent environment has been inventoried.
- Skills and knowledge have been semantically mapped.
- Duplication has been identified.
- Overlapping capabilities have been analysed.
- Contradictions have been identified.
- Context-heavy components have been prioritised.
- Consolidation opportunities have been identified.
- Dead/obsolete content has been assessed.
- A proposed architecture exists.
- Capability preservation has been verified.
- Recommended changes have been classified by risk.
- The resulting system is demonstrably simpler, more composable, or more context-efficient.
- No important capability has been lost unintentionally.

## Final Principle

> **The best agent system is not the one with the most skills or the fewest skills. It is the one that exposes the right capability at the right time with the minimum necessary context.**
