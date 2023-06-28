from playwright.sync_api import Page

from pages.elements_page import ElementsPage


class ButtonsPage(ElementsPage):

    def __init__(self, page: Page):
        ElementsPage.__init__(self, page)

        self.page = page

        self.__double_click_btn = self.page.locator(
            'button[id="doubleClickBtn"]')
        self.__right_click_btn = self.page.locator('button[id="rightClickBtn"]')
        self.__dynamic_btn = self.page.locator('//button[text()="Click Me"]')
        self.__double_click_msg = self.page.locator(
            'p[id="doubleClickMessage"]')
        self.__right_click_msg = self.page.locator('p[id="rightClickMessage"]')
        self.__dynamic_click_msg = self.page.locator(
            'p[id="dynamicClickMessage"]')

    def perform_double_click(self) -> None:
        self.__double_click_btn.click(click_count=2)

    def get_double_click_message(self) -> str:
        self.__double_click_msg.wait_for(state='visible')
        return self.__double_click_msg.text_content()

    def perform_rmb_click(self) -> None:
        self.__right_click_btn.click(button="right")

    def get_rmb_click_message(self) -> str:
        self.__right_click_msg.wait_for(state='visible')
        return self.__right_click_msg.text_content()

    def click_the_button(self) -> None:
        self.__dynamic_btn.click()

    def get_dynamic_click_message(self) -> str:
        self.__dynamic_click_msg.wait_for(state='visible')
        return self.__dynamic_click_msg.text_content()
