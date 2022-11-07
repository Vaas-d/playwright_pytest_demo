from playwright.sync_api import Page


class WebTable:

    def __init__(self, page: Page):

        self.page = page

        self.__add_button = self.page.locator('[id="addNewRecordButton"]')

        # registration form
        self.__modal_title = self.page.locator('[id="registration-form-modal"]')
        self.__first_name_input = self.page.locator('[id="firstName"]')
        self.__last_name_input = self.page.locator('[id="lastName"]')
        self.__email_input = self.page.locator('[id="userEmail"]')
        self.__age_input = self.page.locator('[id="age"]')
        self.__salary_input = self.page.locator('[id="salary"]')
        self.__department_input = self.page.locator('id="department"')
        self.__submit_btn = self.page.locator('[id="submit"]')

