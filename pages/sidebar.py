

class Sidebar:

    def __init__(self, page):

        self.page = page

        # sidebar
        self.__text_box_section_button = self.page.locator('(//li[@id="item-0"])[1]')
        self.__check_box_section_button = self.page.locator('(//li[@id="item-1"])[1]')
        self.__radiobutton_section_button = self.page.locator('(//li[@id="item-2"])[1]')
        self.__web_tables_section_button = self.page.locator('(//li[@id="item-3"])[1]')
        self.__buttons_section_button = self.page.locator('(//li[@id="item-4"])[1]')
        self.__links_section_button = self.page.locator('(//li[@id="item-5"])[1]')
        self.__broken_links_section_button = self.page.locator('(//li[@id="item-6"])[1]')
        self.__upload_section_button = self.page.locator('(//li[@id="item-7"])[1]')
        self.__dynamic_props_section_button = self.page.locator('(//li[@id="item-8"])[1]')

    def go_to_text_box_section(self) -> None:
        self.__text_box_section_button.click()

    def go_to_check_box_section(self) -> None:
        self.__check_box_section_button.click()

    def go_to_radio_button_section(self) -> None:
        self.__radiobutton_section_button.click()

    def go_to_buttons_section(self) -> None:
        self.__buttons_section_button.click()
