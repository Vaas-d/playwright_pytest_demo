import pytest

from pages.select_menu_page import SelectMenu
from utils.test_data import Data


class TestSelect:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.menu = SelectMenu(self.page)

        self.page.goto('https://demoqa.com/select-menu', wait_until='networkidle')

    @pytest.mark.two
    def test_select_menu(self, test_setup):
        """Test to verify the dropdown menus on the page

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.menu.select_group_1_option_1()

        self.menu.select_professor()

        self.menu.select_color_old()

        self.menu.select_multiple_colors(Data.colors)

        self.menu.select_multiple_cars()
