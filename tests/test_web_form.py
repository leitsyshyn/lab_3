import pytest

from pages import SubmittedPage


def assert_successful_submission(driver) -> None:
    submitted_page = SubmittedPage(driver)
    submitted_page.wait_until_loaded()

    assert submitted_page.get_submission_title() == "Form submitted"
    assert submitted_page.get_submission_message() == "Received!"


@pytest.mark.smoke
@pytest.mark.web_form
def test_text_fields_submission(web_form_page, text_fields_data) -> None:
    web_form_page.load()
    web_form_page.fill_text_fields(
        text=text_fields_data.text_input,
        password=text_fields_data.password,
        textarea=text_fields_data.textarea,
    )

    assert web_form_page.get_text_input_value() == text_fields_data.text_input
    assert web_form_page.get_password_value() == text_fields_data.password
    assert web_form_page.get_textarea_value() == text_fields_data.textarea

    web_form_page.submit_form()
    assert_successful_submission(web_form_page.driver)


@pytest.mark.smoke
@pytest.mark.web_form
def test_dropdown_and_datalist_submission(web_form_page, selection_data) -> None:
    web_form_page.load()
    web_form_page.choose_dropdown_option(selection_data.dropdown_option)
    web_form_page.fill_datalist_input(selection_data.datalist_value)

    assert web_form_page.get_selected_dropdown_value() == selection_data.dropdown_option
    assert web_form_page.get_datalist_value() == selection_data.datalist_value

    web_form_page.submit_form()
    assert_successful_submission(web_form_page.driver)


@pytest.mark.smoke
@pytest.mark.web_form
def test_checkbox_and_radio_submission(web_form_page) -> None:
    web_form_page.load()
    web_form_page.select_checkbox()
    web_form_page.select_radio_button()

    assert web_form_page.is_checkbox_selected() is True
    assert web_form_page.is_radio_button_selected() is True

    web_form_page.submit_form()
    assert_successful_submission(web_form_page.driver)


@pytest.mark.smoke
@pytest.mark.web_form
def test_color_date_and_range_submission(web_form_page, advanced_controls_data) -> None:
    web_form_page.load()
    web_form_page.fill_color_date_and_range(
        color=advanced_controls_data.color,
        date=advanced_controls_data.date,
        range_value=advanced_controls_data.range_value,
    )

    assert web_form_page.get_color_value() == advanced_controls_data.color
    assert web_form_page.get_date_value() == advanced_controls_data.date
    assert web_form_page.get_range_value() == advanced_controls_data.range_value

    web_form_page.submit_form()
    assert_successful_submission(web_form_page.driver)
