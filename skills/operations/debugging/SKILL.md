---
name: debugging
description: Systematically diagnose and fix software defects using reproduction, evidence, hypothesis testing, root-cause analysis, and regression verification. Use when behaviour is incorrect, tests fail, builds fail, runtime errors occur, or the cause of a problem is unclear.
---

# Debugging

## Purpose

Find and fix the **root cause** of a problem rather than repeatedly applying plausible fixes.

---

# Core Principle

> **Do not guess. Reproduce, gather evidence, form a hypothesis, test it, then fix.**

---

# Workflow

```text
Symptom
   ↓
Reproduce
   ↓
Collect evidence
   ↓
Localise problem
   ↓
Form hypothesis
   ↓
Test hypothesis
   ↓
Identify root cause
   ↓
Implement fix
   ↓
Regression test
   ↓
Verify
```

---

# 1. Define the Symptom

Identify:

- What is wrong?
- What should happen?
- What actually happens?
- When does it happen?
- Can it be reproduced consistently?

Separate:

```text
Expected behaviour
Actual behaviour
```

---

# 2. Reproduce

Reproduce the issue before changing code where practical.

Record:

- Inputs.
- Environment.
- Device/configuration.
- State.
- Steps.
- Error output.

If the issue cannot be reproduced, state that explicitly.

---

# 3. Gather Evidence

Use:

- Logs.
- Stack traces.
- Tests.
- Runtime output.
- Screenshots.
- Network traces.
- Database state.
- Build output.
- Existing code.
- Callers.

Prefer observable evidence over assumptions.

---

# 4. Localise

Determine where the failure occurs.

Example:

```text
UI
 ↓
ViewModel / Presenter
 ↓
Use Case / Domain
 ↓
Repository
 ↓
Network / Database
```

Identify the first layer where actual behaviour diverges from expected behaviour.

---

# 5. Form a Hypothesis

Use:

```text
I believe X is causing Y because Z.
```

Example:

```text
I believe the task is duplicated because the retry path creates
a new database record without checking the existing idempotency key.
```

---

# 6. Test the Hypothesis

Change or inspect the smallest thing necessary to determine whether the hypothesis is correct.

Do not modify production code merely to "see if it fixes it" unless the change is reversible and the diagnostic value justifies it.

---

# 7. Root Cause

Do not stop at:

> "This line is wrong."

Determine:

> Why was this line able to produce the wrong behaviour?

Examples:

```text
Symptom:
Duplicate task

Immediate cause:
Duplicate insert

Root cause:
Retry operation is not idempotent
```

---

# 8. Fix

Prefer the smallest correct fix.

Avoid unrelated refactoring during debugging unless it is required to solve the issue safely.

---

# 9. Regression Protection

Add or update a test when practical.

Verify:

```text
Before:
Bug reproduced

After:
Bug fixed

Regression:
Test protects behaviour
```

---

# Failed Attempts

If a fix does not work:

- Do not repeatedly retry the same approach.
- Record what the result tells you.
- Update the hypothesis.
- Gather new evidence.

A failed hypothesis is useful information.

---

# Platform-Specific Debugging

When debugging platform-specific environments (e.g. mobile, web, distributed systems):

- Use appropriate diagnostic tooling:
  - System logs / logcat / browser console.
  - Runtime screenshots or visual captures.
  - Device, emulator, or browser matrix variations.
  - Environment variables and network inspection.
- Distinguish the failure category before touching code:
  - Build failure vs. Packaging / Linking failure.
  - Installation / Deployment failure vs. Launch failure.
  - Runtime failure vs. State failure.
  - Layout / Rendering failure vs. User interaction failure.
- For deep Android / Compose debugging workflows, refer to the specialized `android` and `android-cli` skills.

Do not treat every platform or environment anomaly as an application code defect.

---

# Output

```markdown
## Debugging Summary

### Symptom

...

### Root Cause

...

### Evidence

...

### Fix

...

### Verification

...

### Regression Protection

...

### Remaining Uncertainty

...
```

---

# Guiding Principle

> **A successful debugging session should explain not only what was fixed, but why the failure occurred.**
