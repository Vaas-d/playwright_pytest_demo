import pytest

from pages.radio_button_page import RadioButtonsPage
from utils.tools import take_screenshot


class TestRadioButtons:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.radio = RadioButtonsPage(self.page)

        # click elements button on the homepage
        self.radio.click_elements_button()

        # click radio buttons section from the sidebar
        self.radio.go_to_radio_button_section()

    def test_radio_buttons(self, test_setup):
        """Test to verify the radio buttons on the page

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.radio.select_radio_button('Yes')
        actual_message = self.radio.get_result_message()
        assert actual_message == 'Yes'

        take_screenshot(self.page, "radio_buttons_result")

        self.radio.select_radio_button('Impressive')
        actual_message = self.radio.get_result_message()
        assert actual_message == 'Impressive'

        take_screenshot(self.page, "radio_buttons_result")
