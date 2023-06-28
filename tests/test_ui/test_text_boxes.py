import pytest

from pages.text_box_page import TextBoxPage
from utils.test_data import Data
from utils.tools import take_screenshot


class TestTextBoxes:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.text_box = TextBoxPage(self.page)

        # click elements button on the homepage
        self.text_box.click_elements_button()

        # click text boxes section from the sidebar
        self.text_box.go_to_text_box_section()

    def test_text_boxes(self, test_setup):
        """Test to verify the input fields and output form on the page

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.text_box.set_username(Data.username)
        self.text_box.set_email(Data.email)
        self.text_box.set_current_address(Data.current_address)
        self.text_box.set_permanent_address(Data.permanent_address)
        take_screenshot(self.page, "submitted_form")

        self.text_box.submit_form()

        take_screenshot(self.page, "resulting_form")

        # check the result
        actual_username = self.text_box.get_username()
        actual_email = self.text_box.get_user_email()
        actual_current_address = self.text_box.get_current_address()
        actual_permanent_address = self.text_box.get_permanent_address()

        assert actual_username == f'Name:{Data.username}'
        assert actual_email == f'Email:{Data.email}'
        assert actual_current_address == f'Current Address :{Data.current_address} '
        assert actual_permanent_address == f'Permananet Address :{Data.permanent_address}'
