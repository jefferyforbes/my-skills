---
name: room-kmp-migration
description: AndroidX Room Multiplatform database migration, KSP schema generation, bundled SQLite drivers, and migration verification across Android, iOS (Darwin), and Desktop (JVM).
license: Apache-2.0
metadata:
  author: Jeffery Forbes
  last-updated: '2026-09-05'
  keywords:
  - Room KMP
  - AndroidX Room
  - SQLite
  - BundledSQLiteDriver
  - Database Migration
  - AutoMigration
  - KSP
  - Kotlin Multiplatform
---

# AndroidX Room Multiplatform & Database Migration

## Overview

AndroidX Room (2.7.0+) brings first-class Kotlin Multiplatform (KMP) support across Android, iOS (Native/Darwin), and Desktop (JVM).

Unlike legacy Android-only Room:
- Instantiation uses `@ConstructedBy` and `expect/actual RoomDatabaseConstructor`.
- SQLite access uses `androidx.sqlite.driver.bundled.BundledSQLiteDriver` or native platform drivers.
- Linker flags on iOS must include `-lsqlite3`.
- Migrations must be verified multiplatform-wide without relying on Android-specific instrumentation contexts.

---

## 1. Multiplatform Gradle & KSP Setup

In your multiplatform module's `build.gradle.kts`:

```kotlin
plugins {
    alias(libs.plugins.kotlinMultiplatform)
    alias(libs.plugins.androidKmpLibrary)
    alias(libs.plugins.kotlinSerialization)
    alias(libs.plugins.ksp)
    alias(libs.plugins.androidx.room)
}

room {
    schemaDirectory("$projectDir/schemas")
}

kotlin {
    listOf(
        iosArm64(),
        iosX64(),
        iosSimulatorArm64(),
    ).forEach { iosTarget ->
        iosTarget.binaries.framework {
            baseName = "SharedDatabase"
            isStatic = true
            linkerOpts.add("-lsqlite3")
        }
    }

    jvm()

    sourceSets {
        commonMain.dependencies {
            implementation(libs.androidx.room.runtime)
            implementation(libs.androidx.sqlite.bundled)
        }
        androidMain.dependencies {
            implementation(libs.androidx.room.runtime)
        }
        commonTest.dependencies {
            implementation(libs.kotlin.test)
            implementation(libs.kotlinx.coroutines.test)
        }
    }
}

// Ensure KSP runs Room compiler for each target platform
dependencies {
    add("kspAndroid", libs.androidx.room.compiler)
    add("kspIosArm64", libs.androidx.room.compiler)
    add("kspIosX64", libs.androidx.room.compiler)
    add("kspIosSimulatorArm64", libs.androidx.room.compiler)
    add("kspJvm", libs.androidx.room.compiler)
}
```

---

## 2. Database Definition & `@ConstructedBy`

In `commonMain`:

```kotlin
package com.example.app.database

import androidx.room.ConstructedBy
import androidx.room.Database
import androidx.room.RoomDatabase
import androidx.room.RoomDatabaseConstructor

@Database(
    entities = [
        PatientEntity::class,
        SessionEntity::class
    ],
    version = 2,
    exportSchema = true,
    autoMigrations = [
        AutoMigration(from = 1, to = 2)
    ]
)
@ConstructedBy(AppDatabaseConstructor::class)
abstract class AppDatabase : RoomDatabase() {
    abstract fun patientDao(): PatientDao
    abstract fun sessionDao(): SessionDao
}

// Expect object for Room KSP compiler code generation
@Suppress("NO_ACTUAL_FOR_EXPECT")
expect object AppDatabaseConstructor : RoomDatabaseConstructor<AppDatabase>
```

---

## 3. Database Builder & Driver Initialization

Construct the database instance per platform using `BundledSQLiteDriver`:

```kotlin
import androidx.room.Room
import androidx.sqlite.driver.bundled.BundledSQLiteDriver
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.IO

fun createAppDatabase(dbFilePath: String): AppDatabase {
    return Room.databaseBuilder<AppDatabase>(
        name = dbFilePath,
        factory = { AppDatabaseConstructor.initialize() }
    )
    .setDriver(BundledSQLiteDriver())
    .setQueryCoroutineContext(Dispatchers.IO)
    .addMigrations(MIGRATION_2_3)
    .build()
}
```

### Platform Storage Paths:
- **Android**: `context.getDatabasePath("app.db").absolutePath`
- **iOS**: `NSFileManager.defaultManager.URLForDirectory(NSDocumentDirectory, ...).path + "/app.db"`
- **JVM/Desktop**: `System.getProperty("user.home") + "/.app/app.db"`

---

## 4. Manual & Complex Migrations

When altering tables, dropping columns, or modifying foreign keys:

```kotlin
import androidx.room.migration.Migration
import androidx.sqlite.SQLiteConnection
import androidx.sqlite.execSQL

val MIGRATION_2_3 = object : Migration(2, 3) {
    override fun migrate(connection: SQLiteConnection) {
        // SQLiteConnection replaces legacy SupportSQLiteDatabase
        connection.execSQL(
            """
            ALTER TABLE sessions 
            ADD COLUMN clinical_summary TEXT DEFAULT NULL
            """.trimIndent()
        )
        connection.execSQL(
            """
            CREATE INDEX IF NOT EXISTS index_sessions_patient_id 
            ON sessions (patient_id)
            """.trimIndent()
        )
    }
}
```

---

## 5. Multiplatform Schema Verification & Best Practices

1. **Schema Check-in**: Always commit the `$projectDir/schemas/com.example.app.database.AppDatabase/*.json` files to Git. Room uses them to validate AutoMigrations.
2. **Type Converters**: Store complex types (lists, date-time, agent metadata) as JSON strings using `kotlinx.serialization.json.Json`:
   ```kotlin
   class Converters {
       @TypeConverter
       fun fromInstant(value: Instant?): String? = value?.toString()
       
       @TypeConverter
       fun toInstant(value: String?): Instant? = value?.let { Instant.parse(it) }
   }
   ```
3. **No-Actual Expectation**: The `@Suppress("NO_ACTUAL_FOR_EXPECT") expect object DatabaseConstructor` pattern relies on Room's KSP compiler to synthesize the `actual` implementation per platform target at compile time. Never manually create an `actual object DatabaseConstructor`.
