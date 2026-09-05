---
name: visual-defect-diagnosis
description: Diagnose and resolve UI defects, stack traces, compiler crashes, and layout bugs presented via screenshots, image attachments, or visual logs.
---

# Visual Defect Diagnosis & Screenshot Triage

## Purpose

Systematically diagnose and remediate errors, stack traces, and layout discrepancies provided via visual media (screenshots, terminal screen grabs, emulator captures, or UI mockups).

Use this skill when the user provides a **screenshot**, **image attachment**, or invokes `/debugging the screenshot`.

---

## The Visual Diagnosis Lifecycle

```text
Visual Artifact Ingestion
         ↓
Symbol & Trace Extraction (OCR)
         ↓
Codebase Correlation (grep / search)
         ↓
Root Cause Categorization
         ↓
Remediation & Visual Verification
```

---

## 1. Visual Artifact Ingestion

- Call `view_file` on the provided image path (or inspect multimodal context directly).
- Identify visual regions:
  - **Error Panels / Modals**: Title, message, and error codes.
  - **Log / Terminal Panels**: Stack trace lines, failing task names, or compile errors.
  - **UI Layouts**: Misaligned composables, clipped text, truncated strings, or incorrect themes.

---

## 2. Symbol & Text Extraction (OCR to Codebase)

Do not guess code locations based on visual appearances alone. Extract literal anchor tokens:
1. **Target Symbols**: Exception names (e.g. `IllegalStateException`), class names, or method names visible in the image.
2. **File & Line Indicators**: Locate `(FileName.kt:142)` or `at com.example.package...`.
3. **Log Messages**: Extract exact substrings from error banners (e.g. `Execution failed for task ':app:compileDebugKotlin'`).

---

## 3. Codebase Correlation

Locate the exact source file using targeted workspace search tools:

```text
grep_search(Query="<exact_extracted_symbol>", SearchPath="<workspace_dir>")
find_by_name(Pattern="*<FileName>*", SearchDirectory="<workspace_dir>")
```

Inspect caller contexts and preceding state transformations using `view_file`.

---

## 4. Defect Categorization & Action Runbook

| Category | Typical Visual Indicators | Remediation Flow |
| :--- | :--- | :--- |
| **Build & Gradle Logic** | Task failure banners, missing dependency symbols, unresolved plugins. | Refer to `android-gradle-logic` or build configurations. Check version catalogs (`libs.versions.toml`). |
| **Runtime Crash / Exception** | Red crash dialogs, unhandled coroutine exception traces, null pointers. | Route to `engineering/operations/debugging` to formulate and test a root-cause hypothesis. |
| **UI Layout & Compose Bug** | Truncated text, overlapping elements, wrong colors, broken dark theme. | Inspect Compose modifiers (`fillMaxWidth`, `weight`), padding, state hoisting, and string resources. |
| **API / Network Failure** | HTTP 4xx/5xx dialogs, network error toasts, malformed JSON alerts. | Verify endpoint routing, serializers, and backend services. |

---

## 5. Verification & Completion

Verify the fix using evidence matching the defect category:
1. **Compilation / Build Errors**: Re-run the failing Gradle/build command (`./gradlew assembleDebug` or test task).
2. **Runtime Crashes**: Run the relevant unit or instrumentation test.
3. **UI Defects**: If possible, inspect UI tests or request the user verify the updated rendered screen.

---

## Deep References
Load on-demand using `view_file`:
- **[OCR Extraction & Trace Signatures](./references/ocr-and-trace-patterns.md)**: Common stack-trace signatures, terminal crash patterns, and Compose layout defect remedies.
