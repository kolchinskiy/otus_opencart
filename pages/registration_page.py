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

    def push_continue_button(self):
        self.push_the_button(RegistrationPageLocators.BUTTON)


