from playwright.sync_api import Page


class RadioButton:

    def __init__(self, page: Page):

        self.page = page

        self.__result = self.page.locator('[class="text-success"]')

    def select_radio_button(self, name) -> None:
        radio_button = self.page.locator(f'input[id="{name.lower()}Radio"]')
        radio_button.check(force=True)

    def check_result(self, text) -> None:
        self.__result.wait_for(state='visible')
        assert self.__result.text_content() == text, f'Expected {text}, got {self.__result.text_content()} instead'
