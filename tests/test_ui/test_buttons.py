import pytest

from pages.buttons_page import Buttons
from pytest import mark
from utils.tools import take_screenshot


class TestButtons:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.buttons = Buttons(self.page)

        self.page.goto('https://demoqa.com/buttons')

    @mark.one
    def test_double_click_button(self, test_setup):
        """Test to verify the functionality of the double click button

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.buttons.perform_double_click()

        self.buttons.check_double_click_result()
        take_screenshot(self.page, "double_click")

    @mark.two
    def test_rmb_click_button(self, test_setup):
        """Test to verify the functionality of the Right Mouse Button click button
        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.buttons.perform_rmb_click()

        self.buttons.check_rmb_click_result()
        take_screenshot(self.page, "rmb_click")

    def test_dynamic_button(self, test_setup):
        """Test to verify the functionality of the dynamic button

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.buttons.click_the_button()

        self.buttons.check_click_result()
        take_screenshot(self.page, "dynamic_click")

    def test_buttons(self, test_setup):
        """Test to verify the functionality of the double click button, Right Mouse Button click button and
        dynamic button

        :param test_setup:
        :return: None
        """
        self.buttons.perform_double_click()

        self.buttons.check_double_click_result()
        take_screenshot(self.page, "double_click")

        self.buttons.perform_rmb_click()

        self.buttons.check_rmb_click_result()
        take_screenshot(self.page, "rmb_click")

        self.buttons.click_the_button()

        self.buttons.check_click_result()
        take_screenshot(self.page, "dynamic_click")
