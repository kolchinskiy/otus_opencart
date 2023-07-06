from locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def check_elements_on_login_page(self):
        self.check_element(LoginPageLocators.EMAIL_FIELD)
        self.check_element(LoginPageLocators.LOGIN_BUTTON)

    def check_text_on_continue_button(self, button_text):
        button = self.check_element(LoginPageLocators.CONTINUE_BUTTON)
        assert button.text == button_text
