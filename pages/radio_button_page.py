from playwright.sync_api import Page

from pages.elements_page import ElementsPage


class RadioButtonsPage(ElementsPage):

    def __init__(self, page: Page):
        ElementsPage.__init__(self, page)

        self.page = page

        self.__result_text_field = self.page.locator('[class="text-success"]')

    def select_radio_button(self, name) -> None:
        radio_button = self.page.locator(f'input[id="{name.lower()}Radio"]')
        radio_button.check(force=True)

    def get_result_message(self) -> str:
        self.__result_text_field.wait_for(state='visible')
        return self.__result_text_field.text_content()
