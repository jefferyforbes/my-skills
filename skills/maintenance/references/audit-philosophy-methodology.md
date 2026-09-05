# Agent System Audit: Philosophy, Methodology & Safe Refactoring

## Purpose

This reference document provides the architectural philosophy, semantic mapping processes, context cost formulas, and safe refactoring guidelines for conducting comprehensive agent system audits.

---

# 1. Audit Philosophy

## 1.1 Understand Before Changing

Never modify anything immediately. First construct an understanding of the system.

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

## 1.2 Treat Skills as Software

Skills should be analysed like software modules.

Evaluate:
- **Cohesion**: Does the skill focus on a single core responsibility?
- **Coupling**: How tightly bound is this skill to other skills or specific environments?
- **Duplication**: Is the same guidance repeated across multiple files?
- **Dependency Direction**: Do specialist skills depend on foundational skills, avoiding circular dependencies?
- **Single Responsibility**: Does the skill have one clear reason to change?
- **Reusability & Composability**: Can other workflows invoke or reference this skill cleanly?
- **Discoverability**: Can the agent identify when to activate this skill from its metadata?
- **Maintainability**: Is the skill organized so future engineers can safely edit it?
- **Context Cost**: What is the prompt token overhead of loading this skill?

A skill should ideally answer:
> *"What capability does this provide that another skill does not?"*

If the answer is unclear, investigate whether the skill should be merged, split, or removed.

---

# 2. Context Cost Measurement

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
$$\text{Priority} = \text{context\_size} \times \text{usage\_frequency}$$
is high.

A large skill that is rarely used may be less important than a moderately sized skill loaded on every task.

### Core Rules vs Supporting Knowledge
Separate:
1. **Core instructions**: Information that must be available whenever the skill executes (behavioral rules, required workflow, constraints, decision logic, validation requirements).
2. **Supporting knowledge**: Information only required in specific circumstances (long examples, reference documentation, edge cases, background explanations, detailed API references, historical decisions).

Structure:
```text
SKILL.md (concise operational instructions, ~300-600 words)
   └── references/ (deep knowledge loaded via view_file only when required)
```

---

# 3. Duplication & Overlap Classification

Duplication across skills is classified into four categories:
1. **Exact**: Same wording, same information. (Action: Consolidate immediately).
2. **Semantic**: Different wording, identical meaning. (Action: Standardize onto a single source of truth).
3. **Functional**: Different wording, identical resulting behavior. (Action: Compose or unify).
4. **Intentional**: Repeated because local operational context genuinely requires immediate visibility without a tool call. (Action: Preserve).

Only optimize the first three categories.

### Preserve Local Specificity
Not all duplication is bad.
- General rule: *"All code should be tested."*
- Specific rule: *"Compose UI changes require screenshot verification across 9 window sizes."*

The second is specialized domain behavior. When consolidating, preserve the specialized portion:
$$\text{Shared principle} + \text{specialised extension}$$

---

# 4. Safe Refactoring Protocols

When applying structural changes:
1. **Preserve original behavior**: Avoid destructive edits until a replacement exists.
2. **Account for all instructions**: Ensure every removed instruction is mapped to its new location.
3. **Verify dependency resolution**: Ensure all links, imports, and relative paths resolve cleanly.
4. **Enforce Antigravity Discovery Constraints**: Antigravity only discovers root skills at exactly `skills/<skill_name>/SKILL.md`. Ensure that refactoring does NOT hide active skills in nested subdirectories unless they are intentionally designed as unmounted references linked from a top-level routing hub.
5. **Fix Before You Delete**: Do not propose removing a capability solely because it contains broken links or missing scripts. Actively search the filesystem, check for package replacements, or repair the functionality first.
6. **Do Not Optimise Away Critical Rules**:
   - Safety constraints
   - Tool invocation requirements
   - Validation steps
   - Important edge cases
   - Explicit user preferences
   - Error handling & recovery
   - Security requirements

---

# 5. Capability Preservation Matrix

When consolidating or splitting skills, produce a verification matrix:

| Original Capability | New Location | Preserved? | Verification Method |
| :--- | :--- | :---: | :--- |
| Capability A | `skill-x/SKILL.md` | Yes | Code/Doc Review |
| Capability B | `references/ref-b.md` | Yes | Link & view_file test |
| Capability C | `skill-y/SKILL.md` | Yes | Scenario execution |
| Capability D | Removed | No | Explicitly justified |

Every removed capability must be explicitly marked intentional. There should be **no unexplained capability loss**.
