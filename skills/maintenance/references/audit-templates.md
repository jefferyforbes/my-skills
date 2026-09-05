# Agent System Audit: Templates, Severity & Schemas

## Purpose

This reference provides the formal schema, severity classification criteria, and reporting templates for executing system-wide agent audits.

---

# 1. Audit Severity Classification

Findings must be classified under four discrete tiers:

### Critical
- Potential capability loss
- Contradictory behavioral rules
- Broken execution scripts or severed critical routes
- Security, privacy, or safety constraint bypass

### High
- Significant duplication across multiple core files
- Massive prompt context waste (>1,500 words in an active execution router)
- Workflow inefficiencies causing looping or repeated failed tool executions

### Medium
- Moderate duplication between related sub-skills
- Unclear responsibility boundaries between sibling skills
- Unnecessary structural complexity

### Low
- Minor wording duplication
- Purely cosmetic organization or naming conventions
- Small optimization opportunities (<200 words)

---

# 2. Audit Output Schema & Format

Every formal audit report must conclude with:

## 2.1 Executive Summary
- Current system shape (number of skills, root routers, nested references)
- Major identified issues
- Largest context burdens
- High-value optimization opportunities
- Expected impact

## 2.2 Finding Schema
For each finding:

```markdown
### [FINDING-###] <Descriptive Title>
- **Severity**: Critical | High | Medium | Low
- **Category**: Duplication | Context Burden | Broken Route | Boundary Leak
- **Affected Files**:
  - `path/to/file1.md`
  - `path/to/file2.md`
- **Problem**: Concise description of defect, overlap, or context cost.
- **Recommendation**: Exact structural refactoring or reference extraction proposed.
- **Expected Benefit**: Context token reduction or capability clarification.
- **Risk Assessment**: Potential impact and required verification.
```

## 2.3 Proposed Target Architecture
Show the proposed file hierarchy before and after refactoring:

```text
skills/
├── domain/
│   ├── SKILL.md (<600 words router)
│   └── references/ (deep guides)
```

## 2.4 Capability Preservation Verification
Include the completed Capability Preservation Matrix proving 0% accidental loss.
