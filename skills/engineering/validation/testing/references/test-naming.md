# Test Naming & Documentation Reference

## Test Naming as a Behavioural Contract

Test names are part of the behavioural contract.

A test name should communicate enough context to answer:

> What behaviour is protected, under what meaningful condition, and what outcome is expected?

If a test cannot be named clearly, consider whether the behaviour, responsibility, or scope being tested is unclear.

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

## Test Names as Documentation

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
