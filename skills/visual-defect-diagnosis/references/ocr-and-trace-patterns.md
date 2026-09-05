# Visual Defect Diagnosis: OCR Extraction & Trace Patterns

This reference catalogs common visual error signatures from IDEs, terminal screen grabs, and Android logcat captures.

---

## 1. Common Stack-Trace Signatures
- **NullPointerException**: \`java.lang.NullPointerException at com.package.Class.method(Class.kt:42)\`
  - *Action*: Trace caller nullability contracts and state hoisting.
- **Compose State Mutated Off-Main**: \`IllegalStateException: Reading a state that was created after snapshot was taken\`
  - *Action*: Inspect coroutine context and background thread emissions into Compose state.
- **Unresolved Reference**: \`e: file:///... Unresolved reference: xyz\`
  - *Action*: Inspect module dependency declarations in \`build.gradle.kts\`.

---

## 2. Visual UI Layout Failure Signatures
- **Text Truncation**: Missing ellipsis (\`TextOverflow.Ellipsis\`) or missing \`weight(1f)\` inside a \`Row\`.
- **Overlapping Elements**: Missing vertical scroll modifier on small screens.
