from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page

        self.__homepage_page_title = self.page.locator(
            'a[href="https://demoqa.com"]')
        self.__homepage_banner = self.page.locator('img[class="banner-image"]')
        self.__elements_button = self.page.locator(
            'div.home-body > div > div:nth-child(1)')
        self.__forms_button = self.page.locator(
            'div.home-body > div > div:nth-child(2)')
        self.__alerts_button = self.page.locator(
            'div.home-body > div > div:nth-child(3)')
        self.__widgets_button = self.page.locator(
            'div.home-body > div > div:nth-child(4)')
        self.__interactions_button = self.page.locator(
            'div.home-body > div > div:nth-child(6)')
        self.__bookstore_button = self.page.locator(
            'div.home-body > div > div:nth-child(6)')

    def get_homepage_banner_text(self) -> str:
        self.__homepage_banner.wait_for(state="visible")
        return self.__homepage_banner.get_attribute("alt")

    def click_elements_button(self) -> None:
        self.__homepage_page_title.wait_for(state="visible")
        self.__elements_button.click()

    def click_forms_button(self) -> None:
        self.__homepage_page_title.wait_for(state="visible")
        self.__forms_button.click()

    def click_alerts_button(self) -> None:
        self.__homepage_page_title.wait_for(state="visible")
        self.__alerts_button.click()

    def click_widgets_button(self) -> None:
        self.__homepage_page_title.wait_for(state="visible")
        self.__widgets_button.click()

    def click_interactions_button(self) -> None:
        self.__homepage_page_title.wait_for(state="visible")
        self.__interactions_button.click()

    def click_bookstore_button(self) -> None:
        self.__homepage_page_title.wait_for(state="visible")
        self.__bookstore_button.click()
