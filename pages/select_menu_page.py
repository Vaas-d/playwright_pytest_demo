import random

from playwright.sync_api import Page

from pages.widgets_page import WidgetsPage


class SelectMenuPage(WidgetsPage):

    def __init__(self, page: Page):
        WidgetsPage.__init__(self, page)

        self.page = page
        self.__select_value_dropdown = self.page.locator('[id="withOptGroup"]')
        self.__select_one_dropdown = self.page.locator('[id="selectOne"]')
        self.__old_style_select_menu = self.page.locator(
            'select[id="oldSelectMenu"]')
        self.__multiselect_drop_down = self.page.locator(
            '(//div[@class=" css-1hwfws3"])[3]')
        self.__standard_multiselect_dropdown = self.page.locator(
            'select[id="cars"]')

        self.__select_value_dropdown_value = self.page.locator(
            'div[id="withOptGroup"] > div > div > div[class*="singleValue"]')
        self.__select_one_dropdown_value = self.page.locator(
            'div[id="selectOne"] > div > div > div[class*="singleValue"]')
        self.__multiselect_drop_down_values = self.page.locator(
            "div[class*='multiValue'] > div:first-child")

    def select_group(self, group) -> None:
        self.__select_value_dropdown.click()
        option = self.page.locator(f'//div[text()="{group}"]')
        option.click()

    def get_selected_group_option_value(self) -> str:
        return self.__select_value_dropdown_value.text_content()

    def select_prefix(self, prefix) -> None:
        self.__select_one_dropdown.click()
        option = self.page.locator(f'//div[text()="{prefix}"]')
        option.click()

    def get_selected_prefix_option_value(self) -> str:
        return self.__select_one_dropdown_value.text_content()

    def select_multiple_colors(self, colors) -> None:
        self.__multiselect_drop_down.click()
        for color in colors:
            option = self.page.locator(f'//div[text()="{color}"]')
            option.click()

    def get_selected_colors(self) -> list:
        return [
            option.text_content()
            for option in self.__multiselect_drop_down_values.all()
        ]

    def select_cars(self, cars) -> list:
        return [
            ' '.join(self.__standard_multiselect_dropdown.select_option(car))
            for car in cars
        ]

    def select_color_from_old_style_select_menu(self, option) -> list:
        return self.__old_style_select_menu.select_option(option)
