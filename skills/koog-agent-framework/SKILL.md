---
name: koog-agent-framework
description: Authoritative guide for setting up, building, maintaining, and advancing applications using JetBrains Koog AI Agent framework. Use when writing, refactoring, or architecting Kotlin/JVM software that integrates Koog.
---

# JetBrains Koog AI Agent Framework Skill

## Instructions

When working on software that uses or integrates **JetBrains Koog** (`ai.koog:koog-agents`), adhere to these core setup, architectural, maintenance, and observability guidelines.

---

## Operating Contract

This skill operates under the root `AGENTS.md`.

When integrating Koog:

- inspect the project's existing Kotlin, JDK, Gradle, and dependency versions first;
- prefer versions already established by the project when compatible;
- verify current Koog APIs and version requirements from authoritative documentation when the exact version matters;
- do not upgrade the toolchain merely because a newer version is available.

## 1. Environment & Setup

### Prerequisites

Use the project's existing toolchain where possible. Confirm the minimum versions required by the specific Koog version being used before changing the build environment.

### Dependencies Configuration
Ensure `mavenCentral()` is defined in your repository configuration.

```kotlin
// build.gradle.kts
repositories {
    mavenCentral()
}

dependencies {
    // Core Koog Agents library
    implementation("ai.koog:koog-agents:<project-approved-version>")
    
    // Optional extensions / beta functionality
    implementation("ai.koog:koog-agents-additions:<project-approved-version>")
}
```

### Credentials & Security
* Never hardcode LLM provider credentials.
* Fetch API keys dynamically from environment variables:
  * `OPENAI_API_KEY`
  * `GEMINI_API_KEY`
  * `ANTHROPIC_API_KEY`

---

## 2. Architecture & Domain Isolation

### 1. Domain Wrappers (Clean Architecture)
Do NOT leak raw Koog primitives (`AIAgent`, provider classes) directly into presentation or core business domain logic.
* Encapsulate Koog agents inside application-level services (e.g. `AgentOrchestrationService` or custom UseCases).
* Expose pure Kotlin data structures or domain interfaces to the rest of the system.

### 2. Agent Composition & Tool Calling
* Annotate standard Kotlin functions to expose them as safe, typed tools to `AIAgent`.
* Use explicit system prompts to bound agent capabilities.
* Set deterministic limits (e.g., maximum tool invocation loops) to prevent infinite reasoning loops.

### 3. Kotlin Multiplatform (KMP)
* Ensure target platforms match dependency variants (e.g. `koog-agents-jvm` for desktop/backend execution).

---

## 3. Observability & Maintenance

### 1. Telemetry & Tracing
* Enable built-in Koog tracing interfaces (OpenTelemetry, Langfuse, W&B Weave) in production to inspect tool calls, prompt tokens, and model latency.

```kotlin
val agent = AIAgent {
    model = GeminiModel("gemini-1.5-pro")
    tracing {
        enableOpenTelemetry()
    }
}
```

### 2. Versioning & Upgrades
* Core APIs (`ai.koog:koog-agents`) follow strict Semantic Versioning.
* Incubating modules (`koog-agents-additions`) may contain breaking changes; isolate these calls behind abstraction layers.

---

## Checklist for Koog Integration
- [ ] Dependencies added via `mavenCentral()`.
- [ ] Credentials configured via environment variables.
- [ ] Agent interactions wrapped inside isolated service/use-case layers.
- [ ] Max tool execution limits and exception handling configured.
- [ ] Tracing enabled for production observability.
