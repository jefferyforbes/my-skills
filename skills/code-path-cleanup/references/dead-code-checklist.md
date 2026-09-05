# Dead Code & Obsolete Path Cleanup Checklist

This reference provides exhaustive audit checklists for removing dead implementations, legacy compatibility wrappers, and unused dependencies after refactoring.

---

## 1. The Obsolete Implementation Audit

Check whether changes made any of the following unnecessary:
- **Interfaces**: Single-implementation interfaces that were created purely for obsolete test mocks.
- **Compatibility Wrappers**: `@Deprecated` pass-through methods that no longer have external consumers.
- **Factories / Builders**: Obsolete construction helpers replaced by direct instantiation or modern dependency injection.
- **Data Models / Entities**: Orphaned DTOs, database columns, or JSON fields no longer read or written.
- **DI Bindings**: Unused `@Provides` or `@Binds` declarations in dependency injection modules.
- **Feature Flags**: Staged rollout toggles or transitional fallback branches that are now permanently enabled.

---

## 2. Reference Verification Procedure

Before deleting any code file or symbol:
1. Run `grep_search` across the repository for all occurrences of the symbol name.
2. Check test directories (`src/test/`, `jvmTest/`) for leftover assertions targeting obsolete behavior.
3. Check build scripts (`build.gradle.kts`, `package.json`, `Podfile`) for unneeded dependencies.
4. Verify the build and test suites pass completely after deletion.
