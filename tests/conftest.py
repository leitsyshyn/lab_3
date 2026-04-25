from __future__ import annotations

import re
import sys
from collections.abc import Generator
from dataclasses import dataclass
from pathlib import Path
from typing import cast

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from pages import WebFormPage


ARTIFACTS_DIR = Path("artifacts")
SCREENSHOTS_DIR = ARTIFACTS_DIR / "screenshots"
PAGE_SOURCES_DIR = ARTIFACTS_DIR / "page-sources"
DEFAULT_BASE_URL = "https://www.selenium.dev/selenium/web/web-form.html"


@dataclass(frozen=True)
class TextFieldsData:
    text_input: str
    password: str
    textarea: str


@dataclass(frozen=True)
class SelectionData:
    dropdown_option: str
    datalist_value: str


@dataclass(frozen=True)
class AdvancedControlsData:
    color: str
    date: str
    range_value: str


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run Chrome in headless mode.",
    )
    parser.addoption(
        "--base-url",
        action="store",
        default=DEFAULT_BASE_URL,
        help="Base URL for the Selenium web form page.",
    )


def pytest_configure(config: pytest.Config) -> None:
    ARTIFACTS_DIR.mkdir(exist_ok=True)


@pytest.fixture
def base_url(request: pytest.FixtureRequest) -> str:
    return str(request.config.getoption("--base-url"))


@pytest.fixture
def driver(request: pytest.FixtureRequest) -> Generator[WebDriver, None, None]:
    options = Options()
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver_instance = webdriver.Chrome(service=Service(), options=options)
    yield driver_instance
    driver_instance.quit()


@pytest.fixture
def web_form_page(driver, base_url: str) -> WebFormPage:
    return WebFormPage(driver, base_url)


@pytest.fixture
def text_fields_data() -> TextFieldsData:
    return TextFieldsData(
        text_input="Selenium student",
        password="clean-password-123",
        textarea="This scenario verifies text fields before form submission.",
    )


@pytest.fixture
def selection_data() -> SelectionData:
    return SelectionData(dropdown_option="Two", datalist_value="Seattle")


@pytest.fixture
def advanced_controls_data() -> AdvancedControlsData:
    return AdvancedControlsData(color="#ff5733", date="04/25/2026", range_value="8")


def _artifact_name(item: pytest.Item) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", item.nodeid)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo[None]):
    outcome = yield
    report = outcome.get_result()

    if report.when not in {"setup", "call"} or not report.failed:
        return

    funcargs = getattr(item, "funcargs", None)
    if not isinstance(funcargs, dict):
        return

    driver = funcargs.get("driver")
    if driver is None:
        return

    driver = cast(WebDriver, driver)

    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    PAGE_SOURCES_DIR.mkdir(parents=True, exist_ok=True)

    artifact_name = _artifact_name(item)
    screenshot_path = SCREENSHOTS_DIR / f"{artifact_name}.png"
    page_source_path = PAGE_SOURCES_DIR / f"{artifact_name}.html"

    driver.save_screenshot(str(screenshot_path))
    page_source_path.write_text(driver.page_source, encoding="utf-8")
