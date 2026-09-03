# Knowledge Base: JetBrains Koog AI Agent Framework

## Executive Overview
**JetBrains Koog** is an open-source, JVM-native (and Kotlin Multiplatform ready) AI Agent framework. It allows developers to build, orchestrate, trace, and maintain deterministic as well as LLM-driven autonomous agents in Kotlin/JVM applications.

---

## 1. Setup & Installation

### Prerequisites
* **JDK:** 17 or higher (JDK 21 recommended for modern concurrency support)
* **Kotlin:** 2.2.0+ (2.3.10+ recommended)
* **Build Tool:** Gradle 8.0+ with Kotlin DSL (`build.gradle.kts`) or Maven 3.8+

### Dependency Configuration

#### Gradle (Kotlin DSL)
Ensure `mavenCentral()` is present in your repository sources:

```kotlin
// build.gradle.kts
repositories {
    mavenCentral()
}

dependencies {
    // Core Koog Agents library
    implementation("ai.koog:koog-agents:1.2.0")
    
    // Optional extensions / beta functionality
    implementation("ai.koog:koog-agents-additions:1.2.0-beta")
}
```

#### Maven (`pom.xml`)
```xml
<dependency>
    <groupId>ai.koog</groupId>
    <artifactId>koog-agents</artifactId>
    <version>1.2.0</version>
</dependency>
```

### Environment & Authentication Setup
Koog delegates model invocations to LLM providers (e.g., OpenAI, Google Gemini, Anthropic, Ollama). Always configure API keys using environment variables rather than hardcoded credentials.

```bash
export OPENAI_API_KEY="sk-..."
export GEMINI_API_KEY="AIzaSy..."
export ANTHROPIC_API_KEY="sk-ant-..."
```

---

## 2. Core Architecture & Key Abstractions

### 1. Agents (`AIAgent`)
An agent in Koog encapsulates:
* **System Prompt / Persona:** Instructions governing output style and boundary constraints.
* **LLM Model Provider:** Binding to a target LLM engine (e.g., `OpenAIModel`, `GeminiModel`).
* **Tool Set:** Executable Kotlin functions or native tools exposed to the agent.
* **Execution Loop / Graph:** The control flow driving reasoning and action calls.

### 2. Tools & Tool Calling
Koog leverages Kotlin reflection and standard annotations to turn standard Kotlin functions into LLM-accessible tools:
* Type-safe parameter parsing.
* Automatic JSON schema generation for function arguments.
* Exception handling and feedback loops returned directly to the agent.

### 3. Kotlin Multiplatform (KMP) Architecture
Koog is structured as a multiplatform library supporting:
* **JVM / Android**
* **iOS / Native**
* **JS / WasmJS**

*Note: Platform-specific extensions or OS integrations should target the appropriate artifact dependencies (e.g., `koog-agents-jvm`).*

---

## 3. Maintenance & Advancing a Software Using Koog

### Versioning & Upgrade Strategies
Koog adopts standard **Semantic Versioning (SemVer)**:
* `ai.koog:koog-agents:x.y.z`: Stable releases with strict API guarantees.
* `ai.koog:koog-agents-additions:x.y.z-beta`: Experimental features and incubations.

#### Upgrade Guidelines:
1. **Isolate Koog Wrappers:** Wrap `AIAgent` definitions and tool invocations inside your application's domain services (e.g., `AgentOrchestratorService`). Avoid leaking raw Koog interfaces across your core business domain.
2. **Track Breaking Changes:** Monitor Koog release notes for signature updates, especially around beta features or LLM provider adaptors.

### Observability & Tracing
Koog provides built-in tracing interfaces that export agent execution paths, prompt inputs, tool calls, and model latency.
* **OpenTelemetry:** Integration options for standards-compliant telemetry.
* **Third-Party Observability:** Native adapters for platforms like Langfuse and W&B Weave.

```kotlin
// Example Tracing Initialization Pattern
val agent = AIAgent {
    model = GeminiModel("gemini-1.5-pro")
    tracing {
        enableOpenTelemetry()
    }
}
```

---

## 4. Best Practices & Design Patterns

1. **Deterministic Guardrails:** Use Koog tool execution limits (max tool iterations) to prevent runaway LLM loops.
2. **Context Window Management:** Prune or summarize long multi-turn conversations before re-invoking agents.
3. **Structured Outputs:** Leverage typed data schemas for LLM responses to ensure reliable downstream parsing.
4. **Environment Isolation:** Use mock model providers during unit testing to avoid network latency and API costs.

---

## 5. Helpful Resources
* **Official Documentation:** [docs.koog.ai](https://docs.koog.ai/)
* **API Reference:** [api.koog.ai](https://api.koog.ai/)
* **GitHub Repository:** [JetBrains/koog](https://github.com/JetBrains/koog)
* **Issue Tracker:** [YouTrack (KG)](https://youtrack.jetbrains.com/issues/KG/)
