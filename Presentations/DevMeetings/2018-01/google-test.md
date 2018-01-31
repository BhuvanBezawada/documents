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
