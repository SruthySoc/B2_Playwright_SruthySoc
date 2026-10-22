Async Playwright Automation with Pytest

1. Project Overview

This project demonstrates asynchronous browser automation using Python, Playwright, pytest, and pytest-asyncio.

It includes pytest configuration, custom markers, async fixtures, and commands for executing selected tests.

2. Project Structure

Sruthy_Automation_PythonProject/
├── pytest.ini
├── conftest.py
├── README.md
└── tests/
    ├── test_smoke.py
    └── test_regression.py

3. Dependencies

Install the required packages:

pip install pytest pytest-asyncio playwright
playwright install

4. Pytest Configuration

The pytest.ini file contains:

[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts = -v
asyncio_mode = auto
markers =
    smoke: quick tests that verify critical application functionality
    regression: tests that verify existing functionality after code changes

Configuration Options

Option

Description

testpaths = tests

Sets the default directory for test discovery.

python_files = test_*.py

Discovers files beginning with test_.

python_functions = test_*

Discovers functions beginning with test_.

addopts = -v

Enables verbose output by default.

asyncio_mode = auto

Enables automatic async test handling through pytest-asyncio.

markers

Registers custom test markers.

smoke

Groups quick checks of critical functionality.

regression

Groups tests for existing functionality after changes.

5. Async Fixtures

The conftest.py file defines reusable asynchronous fixtures:

browser: launches Chromium.

context: creates an isolated browser context.

page: creates a page within that context.

The fixtures clean up their resources after each test.

6. Test Markers

Smoke Tests

Smoke tests check basic application functionality, such as homepage loading and page title validation.

Example:

@pytest.mark.smoke
@pytest.mark.asyncio
async def test_homepage_title(page):
    await page.goto("https://www.amazon.in/")
    assert "Amazon" in await page.title()

Regression Tests

Regression tests check that existing functionality continues to work, such as search-box visibility and search navigation.

Example:

@pytest.mark.regression
@pytest.mark.asyncio
async def test_search_box_visible(page):
    await page.goto("https://www.amazon.in/")
    await page.locator("#twotabsearchtextbox").wait_for()

7. Test Execution Commands

Run all tests:

python -m pytest -s

Run only smoke tests:

python -m pytest -m smoke -s

Run only regression tests:

python -m pytest -m regression -s

Run smoke or regression tests:

python -m pytest -m "smoke or regression" -s

Run a specific file:

python -m pytest tests/test_smoke.py -s

Run a specific test function:

python -m pytest tests/test_smoke.py::test_homepage_title -s

Run a specific regression function:

python -m pytest tests/test_regression.py::test_search_functionality -s

8. Command-Line Options

Option

Purpose

-v

Displays detailed test names and results.

-s

Displays print() output in the console.

-m smoke

Selects smoke tests.

-m regression

Selects regression tests.

-m "smoke or regression"

Selects tests matching either marker.

::test_function_name

Selects one test function.

9. Expected Results

Pytest discovers tests under the tests directory. Smoke and regression tests can be executed independently using their markers. Individual files and test functions can be selected using command-line arguments.

The tests use async Playwright operations with await, and the fixtures close browser resources after execution.