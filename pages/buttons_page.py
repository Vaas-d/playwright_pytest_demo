from playwright.sync_api import Page

from pages.sidebar import Sidebar


class Buttons(Sidebar):

    def __init__(self, page: Page):
        Sidebar.__init__(self, page)

        self.page = page

        self.__double_click_btn = self.page.locator('button[id="doubleClickBtn"]')
        self.__right_click_btn = self.page.locator('button[id="rightClickBtn"]')
        self.__dynamic_btn = self.page.locator('//button[text()="Click Me"]')
        self.__double_click_msg = self.page.locator('p[id="doubleClickMessage"]')
        self.__right_click_msg = self.page.locator('p[id="rightClickMessage"]')
        self.__dynamic_click_msg = self.page.locator('p[id="dynamicClickMessage"]')

    def perform_double_click(self) -> None:
        self.__double_click_btn.click(click_count=2)

    def check_double_click_result(self) -> None:
        self.__double_click_msg.wait_for(state='visible')
        assert self.__double_click_msg.text_content() == 'You have done a double click', \
            f'Expected a double click massage, got {self.__double_click_msg.text_content()} instead'

    def perform_rmb_click(self) -> None:
        self.__right_click_btn.click(button="right")

    def check_rmb_click_result(self) -> None:
        self.__right_click_msg.wait_for(state='visible')
        assert self.__right_click_msg.text_content() == 'You have done a right click', \
            f'Expected a right click massage, got {self.__right_click_msg.text_content()} instead'

    def click_the_button(self) -> None:
        self.__dynamic_btn.click()

    def check_click_result(self) -> None:
        self.__dynamic_click_msg.wait_for(state='visible')
        assert self.__dynamic_click_msg.text_content() == 'You have done a dynamic click', \
            f'Expected a dynamic click massage, got {self.__dynamic_click_msg.text_content()} instead'
