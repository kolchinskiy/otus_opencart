from locators import GlobalLocators
from pages.base_page import BasePage


class CurrencyElement(BasePage):
    def check_currency(self):
        self.click(GlobalLocators.CURRENCY_BUTTON)
        self.click(GlobalLocators.CURRENCY_EURO)
        self.check_text(GlobalLocators.CURRENCY_CHAR, "€")
        self.click(GlobalLocators.CURRENCY_BUTTON)
        # self.click(GlobalLocators.CURRENCY_POUND)
        # self.check_text(GlobalLocators.CURRENCY_CHAR, "£")
        # self.click(GlobalLocators.CURRENCY_BUTTON)
        self.click(GlobalLocators.CURRENCY_DOLLAR)
        self.check_text(GlobalLocators.CURRENCY_CHAR, "$")
