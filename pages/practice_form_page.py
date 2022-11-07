import random

from playwright.sync_api import Page


class PracticeForm:

    def __init__(self, page: Page):

        self.page = page

        self.__first_name_input = self.page.locator('[id="firstName"]')
        self.__last_name_input = self.page.locator('[id="lastName"]')
        self.__email_input = self.page.locator('[id="userEmail"]')
        self.__gender_list = ["Male", "Female", "Other"]
        self.__mobile_number_input = self.page.locator('[id="userNumber"]')
        self.__dob_input = self.page.locator('[id="dateOfBirthInput"]')
        self.__subjects_field = self.page.locator('[id="subjectsContainer"]')
        self.__subjects_input = self.page.locator('span[aria-live="polite"]')
        self.__sports_checkbox = self.page.locator('[id="hobbies-checkbox-1"]')
        self.__reading_checkbox = self.page.locator('[id="hobbies-checkbox-2"]')
        self.__music_checkbox = self.page.locator('[id="hobbies-checkbox-3"]')
        self.__address_input = self.page.locator('[id="currentAddress"]')
        self.__state_dropdown = self.page.locator('[id="state"]')
        self.__city_dropdown = self.page.locator('[id="city"]')

        self.__submit_form_btn = self.page.locator('button[id="submit"]')

        # final result form
        self.rows = self.page.locator('tbody > tr')

    def set_first_name(self, text) -> None:
        self.__first_name_input.fill(text)

    def set_last_name(self, text) -> None:
        self.__last_name_input.fill(text)

    def set_email(self, text) -> None:
        self.__email_input.fill(text)

    def select_gender(self) -> str:
        gender = random.choice(self.__gender_list)
        radiobutton = self.page.locator(f'[type="radio"][value="{gender}"]')
        radiobutton.check(force=True)
        return gender

    def set_mobile_number(self, text) -> None:
        self.__mobile_number_input.fill(text)

    def select_date_of_birth(self, text) -> None:
        self.__dob_input.click()
        self.__dob_input.press('Control+A')
        self.__dob_input.fill(text)
        self.__mobile_number_input.click()

    def set_subject(self, text) -> None:
        self.__subjects_field.click()
        self.__subjects_input.type(text)
        self.__subjects_input.press('Enter')

    def select_hobbies(self) -> None:
        self.__sports_checkbox.check(force=True)
        self.__reading_checkbox.check(force=True)
        self.__music_checkbox.check(force=True)

    def set_address(self, text) -> None:
        self.__address_input.fill(text)

    def select_state(self, text) -> None:
        state = self.page.locator(f'//div[text()="{text}"]')
        self.__state_dropdown.click()
        state.click()

    def select_city(self, text) -> None:
        city = self.page.locator(f'//div[text()="{text}"]')
        self.__city_dropdown.click()
        city.click()

    def submit_form(self) -> None:
        self.__submit_form_btn.click()

    def check_table_result(self, list_) -> None:
        for i in range(len(list_)):
            value_row = self.rows.nth(i).locator('td:nth-child(2)')
            value = value_row.text_content()
            assert value == list_[i], f'Expected {list_[i]}, got {value} instead'
