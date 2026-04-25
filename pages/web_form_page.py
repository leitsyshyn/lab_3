from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class WebFormPage(BasePage):
    PAGE_HEADING = (By.XPATH, "//h1[normalize-space()='Web form']")
    TEXT_INPUT = (By.ID, "my-text-id")
    PASSWORD_INPUT = (By.NAME, "my-password")
    TEXTAREA = (By.NAME, "my-textarea")
    SELECT_DROPDOWN = (By.NAME, "my-select")
    DATALIST_INPUT = (By.NAME, "my-datalist")
    DEFAULT_CHECKBOX = (By.ID, "my-check-2")
    DEFAULT_RADIO = (By.ID, "my-radio-2")
    COLOR_PICKER = (By.NAME, "my-colors")
    DATE_PICKER = (By.NAME, "my-date")
    RANGE_SLIDER = (By.NAME, "my-range")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver: WebDriver, base_url: str) -> None:
        super().__init__(driver)
        self.base_url = base_url

    def load(self) -> None:
        self.open_url(self.base_url)
        self.find_visible(self.PAGE_HEADING)

    def fill_text_fields(self, text: str, password: str, textarea: str) -> None:
        self.type_text(self.TEXT_INPUT, text)
        self.type_text(self.PASSWORD_INPUT, password)
        self.type_text(self.TEXTAREA, textarea)

    def choose_dropdown_option(self, option_text: str) -> None:
        self.select_dropdown_by_visible_text(self.SELECT_DROPDOWN, option_text)

    def fill_datalist_input(self, value: str) -> None:
        self.type_text(self.DATALIST_INPUT, value)

    def select_checkbox(self) -> None:
        if not self.is_selected(self.DEFAULT_CHECKBOX):
            self.click(self.DEFAULT_CHECKBOX)

    def select_radio_button(self) -> None:
        if not self.is_selected(self.DEFAULT_RADIO):
            self.click(self.DEFAULT_RADIO)

    def fill_color_date_and_range(self, color: str, date: str, range_value: str) -> None:
        self.set_input_value(self.COLOR_PICKER, color)
        self.type_text(self.DATE_PICKER, date)
        self.set_input_value(self.RANGE_SLIDER, range_value)

    def submit_form(self) -> None:
        self.click(self.SUBMIT_BUTTON)

    def get_text_input_value(self) -> str:
        return self.get_input_value(self.TEXT_INPUT)

    def get_password_value(self) -> str:
        return self.get_input_value(self.PASSWORD_INPUT)

    def get_textarea_value(self) -> str:
        return self.get_input_value(self.TEXTAREA)

    def get_datalist_value(self) -> str:
        return self.get_input_value(self.DATALIST_INPUT)

    def get_color_value(self) -> str:
        return self.get_input_value(self.COLOR_PICKER)

    def get_date_value(self) -> str:
        return self.get_input_value(self.DATE_PICKER)

    def get_range_value(self) -> str:
        return self.get_input_value(self.RANGE_SLIDER)

    def get_selected_dropdown_value(self) -> str:
        return self.get_selected_dropdown_text(self.SELECT_DROPDOWN)

    def is_checkbox_selected(self) -> bool:
        return self.is_selected(self.DEFAULT_CHECKBOX)

    def is_radio_button_selected(self) -> bool:
        return self.is_selected(self.DEFAULT_RADIO)
