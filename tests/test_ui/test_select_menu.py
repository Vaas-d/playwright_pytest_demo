import random

import pytest

from pages.select_menu_page import SelectMenuPage
from utils.test_data import Data
from utils.tools import take_screenshot


class TestSelect:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.select = SelectMenuPage(self.page)

        # click elements button on the homepage
        self.select.click_widgets_button()

        # click select menu section from the sidebar
        self.select.go_to_select_menu_section()

    def test_select_value_dropdown(self, test_setup):
        """Test to verify the Select Value dropdown on the select menu page

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        # select random option from the Select Value dropdown
        option = random.choice(Data.groups)
        self.select.select_group(option)

        actual_value = self.select.get_selected_group_option_value()
        assert actual_value == option
        take_screenshot(self.page, "select_value_dropdown")

    def test_select_one_dropdown(self, test_setup):
        """Test to verify the Select One dropdown on the select menu page

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        # select random option from the Select One dropdown
        option = random.choice(Data.prefixes)
        self.select.select_prefix(option)

        actual_value = self.select.get_selected_prefix_option_value()
        assert actual_value == option
        take_screenshot(self.page, "select_one_dropdown")

    def test_old_style_select_menu(self, test_setup):
        """Test to verify the Old Style Select Menu on the select menu page

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        option = "red"
        selected_option = ' '.join(
            self.select.select_color_from_old_style_select_menu(option))
        assert selected_option == option

        index = str(random.randint(1, 10))
        actual_index = ' '.join(
            self.select.select_color_from_old_style_select_menu(index))
        selected_option = Data.old_style_colors[actual_index]
        expected_option = Data.old_style_colors[str(index)]
        assert selected_option == expected_option

        take_screenshot(self.page, "old_style_select_menu")

    def test_multiselect_dropdown(self, test_setup):
        """Test to verify the Multiselect drop down on the select menu page

        :param test_setup: setting up the browser and page objects
        :return: None
        """

        self.select.select_multiple_colors(Data.colors)

        selected_colors = tuple(self.select.get_selected_colors())

        assert selected_colors == Data.colors

        take_screenshot(self.page, "multiselect_dropdown")

    def test_standard_multi_select(self, test_setup):
        """Test to verify the Standard multi select Menu on the select menu page

        :param test_setup: setting up the browser and page objects
        :return: None
        """
        selected_options = tuple(self.select.select_cars(Data.cars))
        assert selected_options == Data.cars

        take_screenshot(self.page, "standard_multi_select")
