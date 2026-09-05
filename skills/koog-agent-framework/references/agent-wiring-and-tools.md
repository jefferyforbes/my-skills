# JetBrains Koog Agent Framework: Wiring & Tool Bindings

This reference provides concrete Kotlin recipes for declaring, instantiating, and testing AI agents using the JetBrains Koog framework.

---

## 1. Defining a Koog Agent
\`\`\`kotlin
import ai.koog.agents.core.agent.Agent
import ai.koog.agents.core.agent.AgentDefinition
import ai.koog.prompt.dsl.prompt

val researchAgent = Agent(
    definition = AgentDefinition(
        name = "ResearchAgent",
        description = "Searches repository files and summarizes architecture"
    )
) {
    // Register tools and system prompt
}
\`\`\`

---

## 2. Tool Registration Pattern
Expose tools to Koog by creating strongly-typed parameter schemas:
\`\`\`kotlin
agent.registerTool(
    name = "fetchContext",
    description = "Retrieves file context"
) { params: FetchParams ->
    // Execution body
}
\`\`\`
