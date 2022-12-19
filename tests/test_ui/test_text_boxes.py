import pytest

from pages.text_box_page import TextBox
from utils.test_data import Data


class TestTextBoxes:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.text_box = TextBox(self.page)

        self.page.goto('https://demoqa.com/text-box', wait_until='networkidle')

    def test_text_boxes(self, test_setup):
        """Test to verify the input fields and output form on the page

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.text_box.set_username(Data.username)
        self.text_box.set_email(Data.email)
        self.text_box.set_current_address(Data.current_address)
        self.text_box.set_permanent_address(Data.permanent_address)
        self.text_box.submit_form()

        # check the result
        self.text_box.check_output_form(Data.username, Data.email, Data.current_address, Data.permanent_address)
