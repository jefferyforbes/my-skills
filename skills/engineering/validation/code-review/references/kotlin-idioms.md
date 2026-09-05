# Kotlin & Modern Language Idioms Review Reference

This reference provides focused criteria for reviewing Kotlin, modern language idioms, and concurrency patterns.

---

## 1. Type Safety & Modeling

- **Sealed Interfaces / Classes**: Are domain states (e.g. `UiState.Loading`, `UiState.Success`, `UiState.Error`) represented via sealed hierarchies with exhaustive `when` expressions?
- **Null Safety**: Are force-unwrap operators (`!!`) avoided? Prefer safe calls (`?.`), Elvis operators (`?:`), or structured preconditions (`checkNotNull`, `requireNotNull`).
- **Data & Value Classes**: Use `data class` for immutable models and `@JvmInline value class` for type-safe primitive wrappers (e.g. `UserId`, `Token`).

---

## 2. Concurrency & Coroutines

- **Structured Concurrency**: Are coroutines launched within bounded lifecycle scopes (`viewModelScope`, `coroutineScope`) rather than `GlobalScope`?
- **Dispatcher Switching**: Do repository and data source functions switch dispatchers internally via `withContext(Dispatchers.IO)`, making them safe to call from any thread?
- **Cold vs Hot Streams**: Are `Flow` transformations cold until collected? Are `StateFlow` and `SharedFlow` configured with appropriate replay and sharing policies?
