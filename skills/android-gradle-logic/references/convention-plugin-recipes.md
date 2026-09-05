# Android Gradle Convention Plugin Recipes

This reference provides production convention plugin implementations and version catalog recipes.

---

## 1. Android Library Convention Plugin
\`\`\`kotlin
// build-logic/convention/src/main/kotlin/AndroidLibraryConventionPlugin.kt
import com.android.build.gradle.LibraryExtension
import org.gradle.api.Plugin
import org.gradle.api.Project
import org.gradle.kotlin.dsl.configure

class AndroidLibraryConventionPlugin : Plugin<Project> {
    override fun apply(target: Project) {
        with(target) {
            with(pluginManager) {
                apply("com.android.library")
                apply("org.jetbrains.kotlin.android")
            }
            extensions.configure<LibraryExtension> {
                defaultConfig.targetSdk = 35
                compileSdk = 35
            }
        }
    }
}
\`\`\`

---

## 2. Compose Multiplatform Plugin Setup
\`\`\`kotlin
with(pluginManager) {
    apply("org.jetbrains.compose")
    apply("org.jetbrains.kotlin.plugin.compose")
}
\`\`\`
