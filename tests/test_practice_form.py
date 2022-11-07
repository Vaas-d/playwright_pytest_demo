from pages.practice_form_page import PracticeForm

test_data = ['Test User', 'email@email.com', 'gender', '5555555555', '24 August,1991', 'Economics',
             'Sports, Reading, Music', '', 'Random test address', 'NCR Delhi']


class TestPracticeForm:

    def test_practice_form(self, page):

        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})

        self.form = PracticeForm(self.page)
        self.page.goto('https://demoqa.com/automation-practice-form')

        self.form.set_first_name(test_data[0][:4])

        self.form.set_last_name(test_data[0][5:])

        self.form.set_email(test_data[1])

        test_data[2] = self.form.select_gender()

        self.form.set_mobile_number(test_data[3])

        self.form.select_date_of_birth(test_data[4])

        self.form.set_subject(test_data[5])

        self.form.select_hobbies()

        self.form.set_address(test_data[8])

        self.form.select_state(test_data[9][:3])

        self.form.select_city(test_data[9][4:])

        self.form.submit_form()

        self.form.check_table_result(test_data)
