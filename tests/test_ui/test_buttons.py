import pytest

from pages.buttons_page import ButtonsPage
from pytest import mark
from utils.tools import take_screenshot
from utils.test_data import Data


class TestButtons:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.buttons = ButtonsPage(self.page)

        # click elements button on the homepage
        self.buttons.click_elements_button()

        # click buttons section from the sidebar
        self.buttons.go_to_buttons_section()

    @mark.one
    def test_double_click_button(self, test_setup):
        """Test to verify the functionality of the double click button

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.buttons.perform_double_click()

        actual_message = self.buttons.get_double_click_message()
        assert actual_message == Data.double_click_message
        take_screenshot(self.page, "double_click")

    @mark.two
    def test_rmb_click_button(self, test_setup):
        """Test to verify the functionality of the Right Mouse Button click button
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.buttons.perform_rmb_click()

        actual_message = self.buttons.get_rmb_click_message()
        assert actual_message == Data.rmb_click_message
        take_screenshot(self.page, "rmb_click")

    def test_dynamic_button(self, test_setup):
        """Test to verify the functionality of the dynamic button

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.buttons.click_the_button()

        actual_message = self.buttons.get_dynamic_click_message()
        assert actual_message == Data.dynamic_click_message
        take_screenshot(self.page, "dynamic_click")
