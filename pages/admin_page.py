from pages.base_page import BasePage
from locators import AdminPageLocators


class AdminPage(BasePage):
    def login_to_admin_page(self, login, password):
        self.fill_the_field(AdminPageLocators.USERNAME, login)
        self.fill_the_field(AdminPageLocators.PASSWORD, password)
        self.push_the_button(AdminPageLocators.LOGIN_BUTTON)

    def add_new_item(self):
        self.click(AdminPageLocators.CATALOG_BUTTON)
        self.click(AdminPageLocators.PRODUCTS_BUTTON)
        self.click(AdminPageLocators.PLUS_BUTTON)
        self.fill_the_field(AdminPageLocators.PRODUCT_NAME, "Название продукта")
        self.fill_the_field(AdminPageLocators.META_TITLE, "Какая-то мета")
        self.click(AdminPageLocators.DATA_BUTTON)
        self.fill_the_field(AdminPageLocators.MODEL, "Какая-то модель")
        self.click(AdminPageLocators.SAVE_BUTTON)

    def check_message_about_success(self):
        assert self.check_element(AdminPageLocators.SUCCESS_MESSAGE)

    def delete_first_item(self):
        self.click(AdminPageLocators.CATALOG_BUTTON)
        self.click(AdminPageLocators.PRODUCTS_BUTTON)
        self.click(AdminPageLocators.FIRST_CHECKBOX)
        self.click(AdminPageLocators.TRASH_BUTTON)
        self.accept_alert()
