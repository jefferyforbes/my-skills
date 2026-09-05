---
name: testing
description: Determine and implement the appropriate testing strategy for code changes. Use when adding features, fixing bugs, refactoring code, or validating behaviour to decide what should be tested, at which level, and how to create meaningful, deterministic, maintainable tests whose names clearly describe the behaviour they protect.
---

# Testing

## Purpose

Create tests that protect **important behaviour**, not tests that merely increase test count or code coverage.

The goal is to establish confidence that the implementation:

- Works as intended.
- Handles important edge cases.
- Does not regress existing behaviour.
- Fails appropriately.
- Remains maintainable.
- Clearly communicates the behaviour being protected.

---

# Core Principle

> **Test behaviour, not implementation.**

A good test answers:

> "What important behaviour would become unsafe if this test disappeared?"

If there is no meaningful answer, the test may not provide enough value.

A good test should make it easy to understand:

```text
What behaviour matters?
        ↓
Under what conditions?
        ↓
What should happen?
```

---

# Testing Workflow

```text
Understand requirement
        ↓
Identify behaviour
        ↓
Identify risks / edge cases
        ↓
Choose test level
        ↓
Define expected behaviour
        ↓
Write meaningful test
        ↓
Run test
        ↓
Verify test validates the intended behaviour
        ↓
Implement / modify code
        ↓
Run again
        ↓
Review test quality
```

For bug fixes, prefer:

```text
Reproduce bug
      ↓
Write regression test
      ↓
Confirm test captures failure
      ↓
Fix implementation
      ↓
Verify test passes
```

---

# Understand Before Testing

Before writing tests, understand:

- The requested behaviour.
- Existing behaviour.
- Important invariants.
- State transitions.
- Failure conditions.
- Existing tests.
- Existing project testing conventions.

Use `code-context` when the relevant behaviour cannot be understood from the immediate code.

Do not write tests based solely on assumptions about what the code should do.

---

# Choose the Smallest Appropriate Test

Prefer the lowest test level that can reliably verify the behaviour.

```text
Unit
  ↓
Integration
  ↓
UI
  ↓
End-to-End
```

Use:

### Unit Tests

For:

- Business rules.
- State transformations.
- Pure functions.
- ViewModel logic.
- Validation.
- Mapping.
- Deterministic calculations.

### Integration Tests

For:

- Database interaction.
- Repository behaviour.
- Network integration.
- Serialization.
- Multiple components interacting.
- Real infrastructure boundaries where meaningful.

### Compose UI Tests

For:

- User-visible behaviour.
- Interaction.
- Semantics.
- UI state.
- Navigation behaviour where appropriate.

### Screenshot Tests

For:

- Visual appearance.
- Layout regression.
- Design fidelity.
- Responsive UI differences.

### End-to-End Tests

For:

- Critical workflows spanning multiple system boundaries.

Do not use E2E tests when a lower-level test provides equivalent confidence.

---

# Test Behaviour

Tests should verify **observable behaviour or meaningful contracts**.

Prefer:

```kotlin
assertThat(result).isEqualTo(expected)
```

over testing internal implementation details.

Avoid tests that depend unnecessarily on:

- Private methods.
- Exact internal class structure.
- Specific implementation algorithms.
- Internal variable names.
- Exact call sequences.

Unless those details are themselves part of the contract.

---

# Behaviour Over Implementation

Prefer:

```text
createsTaskWhenValidTaskIsSubmitted
```

over:

```text
callsRepositoryInsert
```

Prefer:

```text
showsLoadingStateWhileTasksAreLoading
```

over:

```text
setsIsLoadingToTrue
```

Prefer:

```text
completeTaskRemovesItFromActiveTasks
```

over:

```text
updatesTaskStateToCompleted
```

The implementation may change while the behaviour remains the same.

Tests should not unnecessarily prevent reasonable refactoring.

---

# Test Naming

Test names must be **self-explanatory and describe the behaviour or functionality being verified**.

A developer should be able to understand what behaviour is protected by reading the test name without needing to inspect the test body.

A strong test name communicates:

```text
What is being tested?
        +
Under what condition?
        +
What behaviour is expected?
```

---

## Good Test Names

Prefer names such as:

```text
showsErrorWhenNetworkRequestFails
createsTaskWhenValidTaskIsSubmitted
doesNotCreateTaskWhenTitleIsEmpty
preservesSelectedTaskAfterScreenRecreation
retriesTranscriptionWhenTheInitialRequestFails
showsEmptyStateWhenNoTasksExist
displaysLongTaskTitleWithoutClipping
```

These names communicate meaningful behaviour.

---

## Poor Test Names

Avoid vague names such as:

```text
testRequest
testTask
testViewModel
worksCorrectly
handlesError
test1
```

These provide little information about what behaviour is protected.

---

## Include Important Conditions

If a behaviour only occurs under a particular condition, include that condition.

Weak:

```text
showsError
```

Better:

```text
showsErrorWhenTaskCreationFails
```

Weak:

```text
loadsTasks
```

Better:

```text
loadsTasksWhenScreenIsOpened
```

Weak:

```text
displaysTask
```

Better:

```text
displaysTaskTitleAndDescriptionWhenTaskExists
```

---

## State-Based UI Tests

For UI tests, make the expected visible behaviour explicit.

Prefer:

```text
showsLoadingIndicatorWhileTasksAreLoading
showsEmptyStateWhenTaskListIsEmpty
showsTaskListWhenTasksAreAvailable
showsRetryActionWhenTaskLoadingFails
```

rather than:

```text
testLoading
testEmpty
testContent
testError
```

---

## Interaction Tests

For interaction tests, describe:

```text
Action
+
Condition
+
Result
```

Examples:

```text
completesTaskWhenCompleteButtonIsClicked
opensTaskDetailsWhenTaskIsSelected
submitsFormWhenKeyboardDoneActionIsPressed
disablesSubmitButtonWhenFormIsInvalid
```

---

## Regression Tests

Regression tests should make the bug being protected against obvious from the name.

Prefer:

```text
doesNotCreateDuplicateTaskWhenSubmissionIsRetried
```

over:

```text
handlesRetry
```

Prefer:

```text
preservesAudioFileWhenTranscriptionRequestFails
```

over:

```text
testTranscriptionFailure
```

A future developer should be able to understand **why the test exists** from its name.

---

## Parameterised Tests

When using parameterised tests, the name should describe the general behaviour.

Prefer:

```text
rejectsInvalidTaskTitles
```

with cases such as:

```text
empty
whitespace
exceedsMaximumLength
```

Where the testing framework supports descriptive parameter names, use them.

---

# Test Names as Documentation

Treat test names as part of the project's documentation.

A collection of well-named tests should provide a readable description of important system behaviour.

For example:

```text
TaskViewModelTest

createsTaskWhenValidTaskIsSubmitted
doesNotCreateTaskWhenTitleIsEmpty
showsLoadingStateWhileTasksAreLoading
showsErrorWhenTaskCreationFails
retriesTaskCreationAfterTransientFailure
```

This communicates a meaningful portion of the feature's behavioural contract without requiring the implementation to be read.

---

# Naming as a Design Signal

Difficulty naming a test clearly can indicate that the behaviour being tested is poorly defined.

If a test name is difficult to formulate, consider whether:

- The responsibility is unclear.
- The test is testing too many behaviours.
- The production method does too much.
- The expected behaviour is ambiguous.
- The test is coupled to implementation details.

Do not automatically refactor production code because of this, but treat it as a useful signal.

---

# Test Quality

A passing test is not necessarily a good test.

Ask:

> Would this test fail if the bug I care about were introduced?

Also ask:

> Can I understand the behaviour this test protects from its name alone?

A strong test should have:

- A meaningful behavioural assertion.
- A self-explanatory name.
- Deterministic setup.
- A clear reason for existing.
- Minimal coupling to implementation details.
- A focused scope.

A test that is difficult to name clearly may also be a signal that the behaviour or responsibility being tested is poorly defined. That last point is particularly useful: **difficulty naming a test can expose unclear responsibilities in the production code itself.** For an AI agent, that's a nice diagnostic signal rather than merely a naming convention.

---

# Edge Cases

Consider realistic cases such as:

- Empty input.
- Missing input.
- Invalid input.
- Boundary values.
- Duplicate values.
- Very large input.
- Long text.
- Network failure.
- Database failure.
- Retry.
- Cancellation.
- Concurrent operations.
- Partial failure.

Do not invent unrealistic cases simply to increase coverage.

---

# Boundary Testing

Where behaviour depends on limits, test the boundaries.

For example:

```text
Below limit
At limit
Above limit
```

For collections:

```text
Zero items
One item
Typical number
Large number
```

For text:

```text
Empty
Minimum valid
Typical
Maximum valid
Above maximum
```

Only test boundaries relevant to the actual requirement.

---

# Failure Testing

Important failure paths should be tested.

Examples:

```text
Network unavailable
Database unavailable
Invalid input
Permission denied
Timeout
Cancellation
Malformed response
Duplicate request
External service failure
```

Verify both:

1. The failure is handled appropriately.
2. The system remains in a valid state.

---

# State Transition Testing

When behaviour involves state, test meaningful transitions.

Example:

```text
Idle
 ↓
Loading
 ↓
Success
```

and:

```text
Idle
 ↓
Loading
 ↓
Failure
 ↓
Retry
 ↓
Loading
 ↓
Success
```

Do not test every theoretical state transition unless the state machine is genuinely complex.

---

# Test Doubles

Use:

- Fakes.
- Stubs.
- Mocks.

according to the need.

Prefer fakes when a simple deterministic implementation provides useful behaviour.

Use mocks when interaction itself is important.

Do not mock everything automatically.

---

# Test Double Guidance

Prefer testing through stable boundaries.

For example:

```text
Production behaviour
        ↓
Repository interface
        ↓
Fake repository
        ↓
Test
```

rather than coupling the test to every internal call.

Mocks are appropriate when the interaction is itself part of the contract.

---

# Determinism

Tests should avoid uncontrolled:

- Current time.
- Random values.
- Real network calls.
- Real external services.
- Concurrency.
- Thread scheduling.
- Unstable ordering.

Control these dependencies where practical.

---

# Time

When behaviour depends on time:

- Inject a clock where appropriate.
- Use controlled test time.
- Avoid sleeping in tests.
- Avoid relying on wall-clock timing.

Prefer deterministic advancement of time when supported.

---

# Concurrency

When testing asynchronous behaviour, avoid tests that pass or fail based on timing luck.

Prefer:

- Controlled dispatchers.
- Test schedulers.
- Explicit synchronization.
- Structured coroutine testing.

Avoid arbitrary:

```text
sleep(1000)
```

as a synchronization mechanism.

---

# Test Isolation

Tests should not unnecessarily depend on:

- Other tests.
- Shared mutable state.
- Execution order.
- External environment.
- Developer-specific configuration.

A test should be independently understandable and repeatable.

---

# Test Data

Use data that makes the behaviour obvious.

Prefer:

```text
taskTitle = "Prepare presentation"
```

when testing a task.

Avoid meaningless:

```text
taskTitle = "abc"
```

unless the specific test concerns arbitrary/minimal input.

For edge cases, make the data intentionally represent the edge case.

---

# Fixtures

Use reusable fixtures when they improve clarity.

Avoid giant shared fixtures containing irrelevant data.

A test should make its important inputs obvious.

---

# Compose Testing

For Jetpack Compose:

Use UI tests for:

- User interaction.
- Semantics.
- State transitions.
- User-visible behaviour.

Use screenshot tests for:

- Visual fidelity.
- Layout regression.
- Design consistency.

Use unit tests for:

- UI state transformation.
- ViewModel logic.
- Business behaviour.

Do not test business logic through the UI unless the UI behaviour itself is the requirement.

---

# Compose Test Semantics

Prefer meaningful semantics rather than implementation details.

Prefer:

```kotlin
onNodeWithText("Complete")
```

or meaningful test tags/semantics where appropriate.

Avoid tests that depend unnecessarily on:

- Internal composable hierarchy.
- Layout implementation.
- Exact number of nodes.
- Internal component structure.

Tests should survive reasonable UI refactoring.

---

# Screenshot Testing

Use screenshot testing when visual regression protection provides meaningful value.

Good candidates include:

- Important screens.
- Design-system components.
- Complex layouts.
- Adaptive layouts.
- Regression-prone UI.

Screenshot states may include:

```text
Default
Loading
Empty
Content
Error
Selected
Disabled
Expanded
Collapsed
Long content
```

Do not create screenshot tests for every trivial composable.

---

# Deterministic Screenshots

Screenshot tests should be deterministic.

Control:

- Random data.
- Current time.
- Network responses.
- Animations.
- Dynamic content.
- External dependencies.
- Unstable ordering.

Use fixed test data.

---

# UI State Coverage

For important screens identify meaningful states.

At minimum consider:

```text
Loading
Empty
Content
Error
```

Where relevant:

```text
Partial content
Refreshing
Disabled
Selected
Expanded
Collapsed
Offline
Permission denied
Long content
Large dataset
```

Do not create states that do not exist in the product.

---

# Adaptive UI Testing

Do not validate responsive UI on only one device.

Where relevant test:

```text
Compact
Medium
Expanded
```

Also consider:

- Portrait.
- Landscape.
- Resizable windows.
- Split-screen.
- Large displays.
- Font scaling.

The exact configurations should reflect the application's supported environments.

For detailed Compose visual validation, use `compose-ui-testing`.

---

# Accessibility Testing

Where relevant verify:

- Content descriptions.
- Semantic roles.
- State descriptions.
- Touch target sizes.
- Focus behaviour.
- Traversal order.
- Keyboard interaction.

Accessibility is part of behavioural correctness.

---

# Test Coverage

Code coverage can provide useful information, but coverage percentage is not the objective.

High coverage does not guarantee:

- Correct behaviour.
- Good assertions.
- Good edge-case coverage.
- Meaningful regression protection.

Use coverage to identify potentially untested areas, not as the sole measure of test quality.

---

# Regression Tests

When fixing a bug:

1. Reproduce the bug.
2. Identify the behaviour that failed.
3. Add a regression test where practical.
4. Confirm the test captures the failure.
5. Fix the implementation.
6. Confirm the test passes.
7. Run relevant existing tests.

The regression test should protect the **behaviour**, not merely reproduce the original implementation.

---

# Refactoring and Tests

When refactoring:

1. Understand existing behaviour.
2. Identify existing test coverage.
3. Add missing tests if meaningful behaviour is unprotected.
4. Refactor in small steps.
5. Run tests after meaningful steps.
6. Confirm behaviour remains unchanged.

Do not use a refactor as an excuse to rewrite unrelated tests.

---

# Testing Changes to Tests

When modifying an existing test, ask:

- Why was the test changed?
- Is the expected behaviour changing?
- Is the test being made less strict?
- Is a regression being removed?
- Is the test being updated because the implementation changed?

Be particularly careful when removing assertions.

Removing an assertion can reduce confidence even if the test still passes.

---

# Test Failures

When a test fails:

Do not immediately modify the test to make it pass.

Determine whether:

```text
Production code is wrong
        ↓
Test is wrong
        ↓
Requirement changed
        ↓
Environment is wrong
        ↓
Test is flaky
```

Use the `debugging` skill when the cause is unclear.

---

# Flaky Tests

Treat flaky tests as defects.

Investigate:

- Timing.
- Concurrency.
- Shared state.
- Randomness.
- Network dependencies.
- Environment dependencies.
- Uncontrolled asynchronous work.

Do not simply increase retries to hide flakiness unless retrying is itself an intentional strategy.

---

# Test Scope

Do not modify unrelated tests simply because they could be improved.

Keep test changes focused on the requested behaviour.

---

# Verification

Run:

1. New or modified tests.
2. Relevant existing tests.
3. Broader checks when the change has wider impact.

Where relevant also run:

- Static analysis.
- Build verification.
- UI verification.
- Screenshot verification.
- Runtime verification.

If a test cannot be run, report why.

Never claim a test passed if it was not executed.

---

# Evidence

Testing conclusions should be based on actual evidence.

Evidence can include:

- Test output.
- Build output.
- Runtime behaviour.
- Screenshots.
- Coverage reports.
- Logs.
- Reproduced failures.

Distinguish:

```text
Test executed and passed
Test executed and failed
Test not executed
Test could not be executed
```

Do not imply verification that did not occur.

---

# Uncertainty

When testing is incomplete, state what remains uncertain.

Examples:

```text
Unit tests pass, but integration tests were not executed.
```

```text
The compact UI configuration was verified, but expanded-window
behaviour remains unverified.
```

```text
The external service was not available, so the integration path
was tested using a fake implementation.
```

Do not hide limitations.

---

# Test Review Checklist

Before considering testing complete:

- [ ] Important behaviour has been identified.
- [ ] The appropriate test level was selected.
- [ ] Happy-path behaviour is covered where relevant.
- [ ] Important edge cases are covered.
- [ ] Important failure paths are covered.
- [ ] Tests are deterministic.
- [ ] Tests are appropriately isolated.
- [ ] Assertions verify behaviour rather than implementation.
- [ ] Test names clearly describe the behaviour being verified.
- [ ] Test names include important conditions where relevant.
- [ ] Regression tests clearly communicate the bug they protect against.
- [ ] UI tests use meaningful semantics.
- [ ] Screenshot tests cover meaningful visual states where appropriate.
- [ ] Adaptive behaviour is tested where relevant.
- [ ] Accessibility has been considered.
- [ ] Tests actually ran.
- [ ] Failures were investigated rather than blindly suppressed.
- [ ] Remaining uncertainty is documented.

---

# Output

When testing work is complete:

```markdown
## Testing

### Added / Updated

- `<test>` — <behaviour protected>

### Verification

- `<test command>` — Passed / Failed / Not run

### Coverage

- Happy path: <status>
- Edge cases: <status>
- Failure cases: <status>
- Regression behaviour: <status>

### Test Quality

<Any meaningful observations about determinism, maintainability,
or implementation coupling.>

### Remaining Risk

<Any behaviour that remains insufficiently verified.>
```

If no tests were necessary, explain why briefly.

For example:

```text
No new automated tests were added because the change only modifies
static styling and existing screenshot coverage already protects
the affected component.
```

---

# Guiding Principles

> **Test behaviour, not implementation.**

> **A test should fail when the behaviour it protects becomes incorrect.**

> **Test names should tell the story of the behaviour being protected.**

> **Prefer the smallest test that provides meaningful confidence.**

> **Treat flaky tests as defects, not inconveniences.**

> **Coverage is a signal, not the goal.**

> **Never claim verification without evidence.**
