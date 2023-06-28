import random

import pytest

from pages.practice_form_page import PracticeFormPage

from utils.test_data import Data


class TestPracticeForm:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.form = PracticeFormPage(self.page)

        # click elements button on the homepage
        self.form.click_forms_button()

        # click select menu section from the sidebar
        self.form.go_to_practice_form_section()

    def test_practice_form(self, test_setup):

        self.form.set_first_name(Data.user_form_data[0][:4])

        self.form.set_last_name(Data.user_form_data[0][5:])

        self.form.set_email(Data.user_form_data[1])

        Data.user_form_data[2] = random.choice(Data.gender_list)

        self.form.select_gender(Data.user_form_data[2])

        self.form.set_mobile_number(Data.user_form_data[3])

        self.form.select_date_of_birth(Data.user_form_data[4])

        self.form.set_subject(Data.user_form_data[5])

        self.form.select_hobbies()

        self.form.set_address(Data.user_form_data[8])

        self.form.select_state(Data.user_form_data[9][:3])

        self.form.select_city(Data.user_form_data[9][4:])

        self.form.submit_form()

        actual_values = self.form.get_table_results(Data.user_form_data)

        assert actual_values == Data.user_form_data
