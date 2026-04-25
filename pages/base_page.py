from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_url(self, url: str) -> None:
        self.driver.get(url)

    def find_visible(self, locator: tuple[str, str]):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator: tuple[str, str]):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def type_text(self, locator: tuple[str, str], value: str) -> None:
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(value)

    def set_input_value(self, locator: tuple[str, str], value: str) -> None:
        element = self.find_visible(locator)
        self.driver.execute_script(
            "arguments[0].value = arguments[1];"
            "arguments[0].dispatchEvent(new Event('input', { bubbles: true }));"
            "arguments[0].dispatchEvent(new Event('change', { bubbles: true }));",
            element,
            value,
        )

    def click(self, locator: tuple[str, str]) -> None:
        self.find_clickable(locator).click()

    def get_input_value(self, locator: tuple[str, str]) -> str:
        value = self.find_visible(locator).get_attribute("value")
        return value if value is not None else ""

    def is_selected(self, locator: tuple[str, str]) -> bool:
        return self.find_visible(locator).is_selected()

    def select_dropdown_by_visible_text(self, locator: tuple[str, str], text: str) -> None:
        element = self.find_visible(locator)
        Select(element).select_by_visible_text(text)

    def get_selected_dropdown_text(self, locator: tuple[str, str]) -> str:
        element = self.find_visible(locator)
        return Select(element).first_selected_option.text

    def get_text(self, locator: tuple[str, str]) -> str:
        return self.find_visible(locator).text
