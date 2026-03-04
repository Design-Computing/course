# Running Tests with pytest

Welcome to the modernized test system! We now use **pytest** instead of the old custom testing framework.

## Quick Start

From the `course` folder, run:

```bash
# Run all tests
pytest

# Run tests for a specific set
pytest set1/
pytest set2/

# Run a specific test file
pytest set1/test_set1_exercise1.py

# Run tests with more detail
pytest -v

# Run tests and stop at first failure
pytest -x
```

## What You'll See

When you run tests, you'll see **beautiful output** with progress bars and colors thanks to pytest-sugar:

```
 set1/test_set1_exercise1.py ✓✓✓✓✓                                     5% ██
 set1/test_set1_git_setup.py ✗✗✗✗✗                                    10% ███
```

When a test fails, you'll see **exactly what went wrong** with helpful messages and clear diffs showing what you returned vs what was expected.

## Understanding Test Markers

Tests are marked with special tags that tell you what they're testing:

- `@pytest.mark.set1` through `@pytest.mark.set8` - Which exercise set
- `@pytest.mark.mock_input` - Tests that simulate user input
- `@pytest.mark.timeout` - Tests that will stop if they run too long (usually 3-10 seconds)
- `@pytest.mark.api_call` - Tests that make real API calls (might be slower)
- `@pytest.mark.slow` - Optional tests that take longer (like visualizations)

## Running Specific Types of Tests

```bash
# Run only Set 3 tests
pytest -m set3

# Skip slow tests
pytest -m "not slow"

# Run only tests with API calls
pytest -m api_call

# Run tests that use mock input
pytest -m mock_input
```

## When Tests Time Out

If your code has an **infinite loop**, pytest will automatically stop it after a few seconds and show you which test timed out. This prevents your terminal from hanging forever!

## Reading Test Failures

Pytest shows you **three things** when a test fails:

1. **What the test was checking** - The test name and description
2. **What you returned** - Your function's actual output
3. **What was expected** - The correct answer

For example:

```
AssertionError: 
add_5(10)
Expected: 15
Got:      10

💡 Remember: add_5 should ADD 5 to the number, not return it unchanged!
```

## Tips

- **Read the error messages carefully** - They're designed to help you understand what went wrong
- **Run one test file at a time** while working on an exercise: `pytest set2/test_set2_exercise0.py`
- **Use `-v` (verbose)** if you want to see every single test name as it runs
- **Use `-x`** to stop at the first failure so you can focus on one problem at a time
- **Use `--lf`** to re-run only the tests that failed last time

## Common Commands

```bash
# Most useful during development:
pytest set2/ -v -x          # Run Set 2, verbose, stop at first failure

# When you want to see everything:
pytest -v                   # Run all tests with details

# When you're fixing failures:
pytest --lf                 # Run only last failed tests

# To see what tests exist:
pytest --collect-only       # Show all tests without running them

# Check if your code even loads:
python -m py_compile set2/exercise0.py
```

## Need Help?

- Read the test names - they describe what they're testing
- Look at the error messages - they explain what went wrong
- Check the test file itself - it shows what the test expects
- Ask in the course forum if you're stuck!

## What Changed from the Old System?

**Before**: `python tests.py` with custom test framework  
**Now**: `pytest` with industry-standard testing framework

**Why?**

- pytest is what professional developers use in the real world
- Better error messages and diffs
- Faster execution
- More helpful output
- Skills you'll use in your career

The tests themselves check the same things - we just modernized how they run!
