from playwright.sync_api import Page


class CheckBox:

    def __init__(self, page: Page):

        self.page = page
        self.__chevron = self.page.locator('[class="rct-text"] > [aria-label="Toggle"]')
        self.__result = self.page.locator('[class="text-success"]')

    def expand_home_directory(self) -> None:
        self.__chevron.click(force=True)

    def select_checkbox(self, name) -> None:
        checkbox = self.page.locator(f'label[for="tree-node-{name.lower()}"] > [class="rct-checkbox"]')
        checkbox.check()

    def check_results(self, name) -> None:
        results = []
        for i in range(self.__result.count()):
            results.append(self.__result.nth(i).text_content())
        assert name.lower() in results, f'Expected {name} to be in {results}'
