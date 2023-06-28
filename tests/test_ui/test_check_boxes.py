import pytest

from pages.check_box_page import CheckBoxPage
from utils.test_data import Data
from utils.tools import take_screenshot


class TestCheckBoxes:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.checkboxes = CheckBoxPage(self.page)

        # click elements button on the homepage
        self.checkboxes.click_elements_button()

        # click checkboxes section from the sidebar
        self.checkboxes.go_to_check_box_section()

    def test_checkboxes(self, test_setup):
        """Test to verify the checkboxes on the page

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.checkboxes.expand_home_directory()

        self.checkboxes.expand_desktop_directory()

        self.checkboxes.expand_documents_directory()

        self.checkboxes.expand_downloads_directory()

        for item in Data.checkboxes:
            self.checkboxes.select_checkbox(item)

        results = self.checkboxes.get_checkbox_text()

        for item in Data.checkboxes:
            assert item.lower(
            ) in results, f'Expected {item} to be in {results}'

        take_screenshot(self.page, "checkboxes_result")
