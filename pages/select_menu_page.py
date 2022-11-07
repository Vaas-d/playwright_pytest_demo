import random

from playwright.sync_api import Page


class SelectMenu:

    def __init__(self, page: Page):

        self.page = page
        self.__select_value_dropdown = self.page.locator('[id="withOptGroup"]')
        self.__group_1_option_1 = self.page.locator('//div[text()="Group 1, option 1"]')
        self.__one_select_dropdown = self.page.locator('[id="selectOne"]')
        self.__old_select_dropdown = self.page.locator('select[id="oldSelectMenu"]')
        self.__professor = self.page.locator('//div[text()="Prof."]')
        self.__multiselect_menu = self.page.locator('(//div[@class=" css-1hwfws3"])[3]')
        self.__volvo = self.page.locator('option[value="volvo"]')
        self.__audi = self.page.locator('option[value = "audi"]')

    def select_group_1_option_1(self) -> None:
        self.__select_value_dropdown.click()
        self.__group_1_option_1.click()

    def select_professor(self) -> None:
        self.__one_select_dropdown.click()
        self.__professor.click()

    def select_multiple_colors(self, colors) -> None:
        self.__multiselect_menu.click()
        for color in colors:
            option = self.page.locator(f'//div[text()="{color}"]')
            option.click()

    def select_multiple_cars(self) -> None:
        self.__volvo.drag_to(self.__audi)

    def select_color_old(self) -> None:
        option = str(random.randint(1, 10))
        self.__old_select_dropdown.select_option(option)
