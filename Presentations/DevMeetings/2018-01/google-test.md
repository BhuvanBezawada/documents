## Problems of current cxxtest

- `createSuite` and `destroySuite`.
- Only one test suite per file / algorithm supported (apart from performance tests).
- Cannot (temporarily) disable test by commenting / `#if 0`, need to rename it since test discovery is based on string parsing.
- Cannot have free test functions (outside a test suite).
- Tests in `.h` but generates `.cpp`, makes reading debug output harder.

## Advantages of google-test

- Fatal and non-fatal assertions.
- Automatic test discovery.
- Value-parametrized and type-parametrized tests.
- Shuffling of tests helps to avoid dependencies between tests.
- `SCOPED_TRACE` can help to tell where an failing `ASSERT` in a helper function originated, if there are multiple tests calling the same helper function.
- `operator<<` for asserts makes annotating easy, for example with a loop variable (more flexible than `TSM_ASSERT(const char *, ...)`.
- Predicate assertions and custom assertion functions provide flexibility for specialised assertions.

## Disadvantages of google-test

- More advanced features such as parametrized tests feel slightly complicated to use, but would probably be ok once we have a couple of examples or a little experience.
- There does not seem to be a built-in for replacing `TS_ASSERT_THROWS_EQUALS`, would need to provide a replacement ourselves?

## Integration in Mantid

- Setting up `cmake` and `ctest` loks straightforward:
   ```
  add_executable(example example.cpp)
  target_link_libraries(example gtest_main)
  add_test(NAME example_test COMMAND example)
  ```

- If we were to use `google-test`, replacing existing test code is probably not worthwhile. A viable strategy could be to use it for new modules, or use it in a couple of new (still very small) modules.
- Different test frameworks should not be used within the same module.

Relevant links:
- https://github.com/google/googletest/issues/916
- https://cmake.org/cmake/help/v3.9/module/GoogleTest.html
