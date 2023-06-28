from playwright.sync_api import Page

from pages.elements_page import ElementsPage


class CheckBoxPage(ElementsPage):

    def __init__(self, page: Page):
        ElementsPage.__init__(self, page)

        self.page = page
        self.__home_chevron = self.page.locator(
            '[class="rct-text"] > [aria-label="Toggle"]')
        self.__desktop_chevron = self.page.locator(
            '.rct-node-collapsed:nth-child(1) .rct-collapse')
        self.__documents_chevron = self.page.locator(
            '.rct-node-parent:nth-child(2) .rct-collapse > .rct-icon')
        self.__downloads_chevron = self.page.locator(
            '.rct-node:nth-child(3) .rct-collapse')
        self.__result = self.page.locator('[class="text-success"]')

    def expand_home_directory(self) -> None:
        self.__home_chevron.click(force=True)

    def expand_desktop_directory(self) -> None:
        self.__desktop_chevron.click()

    def expand_documents_directory(self) -> None:
        self.__documents_chevron.click()

    def expand_downloads_directory(self) -> None:
        self.__downloads_chevron.click()

    def select_checkbox(self, name) -> None:
        checkbox = self.page.locator(
            f'label[for="tree-node-{name.lower()}"] > [class="rct-checkbox"]')
        checkbox.check()
        assert "check" in checkbox.get_attribute("class")

    def get_checkbox_text(self) -> list:
        return [option.text_content() for option in self.__result.all()]
        # results = []
        # for i in range(self.__result.count()):
        #     results.append(self.__result.nth(i).text_content())
        # return results
