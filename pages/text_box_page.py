from playwright.sync_api import Page

from pages.elements_page import ElementsPage


class TextBoxPage(ElementsPage):

    def __init__(self, page: Page):
        ElementsPage.__init__(self, page)

        self.page = page
        # form
        self.__full_name_input = self.page.locator('[id="userName"]')
        self.__email_input = self.page.locator('[id="userEmail"]')
        self.__current_address_input = self.page.locator(
            'textarea[id="currentAddress"]')
        self.__permanent_address_input = self.page.locator(
            'textarea[id="permanentAddress"]')
        self.__submit_btn = self.page.locator('button[id="submit"]')
        # output form
        self.__output_form = self.page.locator('div[id="output"]')
        self.__name_field = self.page.locator('p[id="name"]')
        self.__email_field = self.page.locator('p[id="email"]')
        self.__current_address_field = self.page.locator(
            'p[id="currentAddress"]')
        self.__permanent_address_field = self.page.locator(
            'p[id="permanentAddress"]')

    def set_username(self, user_name) -> None:
        self.__full_name_input.fill(user_name)

    def set_email(self, email) -> None:
        self.__email_input.fill(email)

    def set_current_address(self, address) -> None:
        self.__current_address_input.type(address)

    def set_permanent_address(self, address) -> None:
        self.__permanent_address_input.type(address)

    def submit_form(self) -> None:
        self.__submit_btn.click()
        self.__output_form.wait_for(state='visible')

    def get_username(self) -> str:
        return self.__name_field.text_content()

    def get_user_email(self) -> str:
        return self.__email_field.text_content()

    def get_current_address(self) -> str:
        return self.__current_address_field.text_content()

    def get_permanent_address(self) -> str:
        return self.__permanent_address_field.text_content()
