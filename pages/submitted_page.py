from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class SubmittedPage(BasePage):
    PAGE_TITLE = (By.XPATH, "//h1[normalize-space()='Form submitted']")
    MESSAGE = (By.ID, "message")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def wait_until_loaded(self) -> None:
        self.find_visible(self.PAGE_TITLE)
        self.find_visible(self.MESSAGE)

    def get_submission_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    def get_submission_message(self) -> str:
        return self.get_text(self.MESSAGE)
