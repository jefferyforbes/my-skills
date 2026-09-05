# Android Service Testing

## Purpose

Guidance and recipes for testing Android `Service` components in isolation using `ServiceTestRule`.

---

## 1. Overview & Tooling

Android `Service` components should be tested using instrumented tests (in `src/androidTest/`) to verify their lifecycle, interactions, and IPC binding behavior on the Android runtime.

### Dependency

Add `androidx.test:rules` to your module's `build.gradle.kts`:

```kotlin
androidTestImplementation(libs.androidx.test.rules) // e.g. "androidx.test:rules:1.6.1"
```

---

## 2. Testing Local & Bound Services with `ServiceTestRule`

`ServiceTestRule` is an AndroidX JUnit 4 rule that handles starting or binding to a service before a test method, and automatically shuts down or unbinds the service after the test completes (in `@After`).

### 2.1 Bound Service Test Recipe

```kotlin
import android.content.Context
import android.content.Intent
import android.os.IBinder
import androidx.test.core.app.ApplicationProvider
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.rule.ServiceTestRule
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith
import java.util.concurrent.TimeoutException

@RunWith(AndroidJUnit4::class)
class LocalServiceTest {

    @get:Rule
    val serviceRule = ServiceTestRule()

    @Test
    @Throws(TimeoutException::class)
    fun testWithBoundService() {
        val context = ApplicationProvider.getApplicationContext<Context>()
        val serviceIntent = Intent(context, LocalService::class.java).apply {
            putExtra(LocalService.SEED_KEY, 42L)
        }

        // Bind the service; blocks until onBind returns or timeout expires
        val binder: IBinder = serviceRule.bindService(serviceIntent)
        val service: LocalService = (binder as LocalService.LocalBinder).service

        assertNotNull(service)
        assertEquals(42L, service.currentSeed)
    }

    @Test
    @Throws(TimeoutException::class)
    fun testWithStartedService() {
        val context = ApplicationProvider.getApplicationContext<Context>()
        val serviceIntent = Intent(context, LocalService::class.java)

        // Start the service
        serviceRule.startService(serviceIntent)

        // Verify service state or interactions
    }
}
```

---

## 3. Important Rules & Limitations

1. **`IntentService` is Not Supported**: `ServiceTestRule` does not manage `IntentService` lifecycles properly. For legacy `IntentService` logic, decouple the business/processing logic into an independent testable class and verify with standard JVM unit tests.
2. **Timeout Handling**: `bindService` and `startService` on `ServiceTestRule` can throw `TimeoutException`. Methods should declare `@Throws(TimeoutException::class)` or handle expected timeouts.
3. **Isolation**: Because `ServiceTestRule` manages clean shutdown after each `@Test`, do not manually unbind unless testing explicit client disconnection flows.
