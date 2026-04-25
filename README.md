# Selenium Web Form UI Tests

This repository contains automated UI tests for the Selenium demo web form page:

`https://www.selenium.dev/selenium/web/web-form.html`

The tests are implemented in Python with Selenium WebDriver, `pytest`, and `pytest-html`.

## Tested Functionality

The test suite includes the following scenarios:

1. Text fields submission
2. Dropdown and datalist submission
3. Checkbox and radio button submission
4. Color picker, date picker, and range slider submission

Each scenario interacts with at least two page elements, verifies the result of the interaction before form submission, submits the form, and verifies successful submission on the target page.

## Technology Stack

- Python
- Selenium WebDriver
- pytest
- pytest-html
- Chrome

## Project Structure

```text
pages/
  base_page.py
  web_form_page.py
  submitted_page.py
  __init__.py
tests/
  conftest.py
  test_web_form.py
requirements.txt
pytest.ini
README.md
.gitignore
.github/workflows/selenium-tests.yml
```

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Test Execution

Run all tests:

```bash
pytest
```

Run tests in headless mode:

```bash
pytest --headless
```

Run tests against a different base URL:

```bash
pytest --base-url="https://example.com/web-form.html"
```

## Report

The HTML report is generated at:

`artifacts/report.html`

## Failure Artifacts

On test failure, the following artifacts are saved:

- screenshots in `artifacts/screenshots/`
- page source files in `artifacts/page-sources/`

Artifacts are created only for failed tests.
