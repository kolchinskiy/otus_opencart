from pages.base_page import BasePage
from locators import AdminPageLocators


class AdminPage(BasePage):
    def login_to_admin_page(self, login, password):
        self.fill_the_field(AdminPageLocators.USERNAME, login)
        self.fill_the_field(AdminPageLocators.PASSWORD, password)
        self.push_the_button(AdminPageLocators.LOGIN_BUTTON)
