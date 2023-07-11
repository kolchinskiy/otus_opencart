from locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def check_elements_on_main_page(self):
        self.check_element(MainPageLocators.BASKET_BUTTON)
        self.check_element(MainPageLocators.SEARCH_FIELD)
        self.check_element(MainPageLocators.FOOTER_LINK)

    def check_text_on_main_page(self):
        self.check_text(MainPageLocators.TEXT, "Featured")
