import faker
from pages.base_page import BasePage
from locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    def check_text_in_link(self, text_in_link):
        link = self.check_element(RegistrationPageLocators.LOGIN_LINK)
        assert link.text == text_in_link

    def reg_fields_is_clickable(self):
        self.text_field_is_clickable(RegistrationPageLocators.FIRST_NAME)

    def check_text_on_registration_page(self):
        self.check_text(RegistrationPageLocators.TEXT, "Register Account")

    def click_on_checkbox(self):
        self.click(RegistrationPageLocators.PRIVACY_CHECKBOX)

    def reg_new_customer(self):
        f = faker.Faker()
        email = f.email()
        self.fill_the_field(RegistrationPageLocators.FIRST_NAME, "Имя")
        self.fill_the_field(RegistrationPageLocators.LAST_NAME, "Фамилия")
        self.fill_the_field(RegistrationPageLocators.EMAIL, email)
        self.fill_the_field(RegistrationPageLocators.TELEPHONE, "1234567890")
        self.fill_the_field(RegistrationPageLocators.PASSWORD_1, "qwerty1234567")
        self.fill_the_field(RegistrationPageLocators.PASSWORD_2, "qwerty1234567")
        self.click(RegistrationPageLocators.PRIVACY_CHECKBOX)
        self.push_the_button(RegistrationPageLocators.BUTTON)

    def check_account_created(self):
        self.check_text(RegistrationPageLocators.SUCCESS_MESSAGE, "Your Account Has Been Created!")
