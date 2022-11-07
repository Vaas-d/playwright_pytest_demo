import pytest

from pages.radio_button_page import RadioButton


class TestRadioButtons:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.radio = RadioButton(self.page)

        self.page.goto('https://demoqa.com/radio-button')

    @pytest.mark.one
    def test_radio_buttons(self, test_setup):
        """Test to verify the radio buttons on the page

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.radio.select_radio_button('Yes')
        self.radio.check_result('Yes')

        self.radio.select_radio_button('Impressive')
        self.radio.check_result('Impressive')
