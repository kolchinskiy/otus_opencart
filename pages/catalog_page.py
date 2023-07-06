from pages.base_page import BasePage
from locators import CatalogPageLocators


class CatalogPage(BasePage):
    def check_elements_on_catalog_page(self):
        self.check_element(CatalogPageLocators.WISH_LIST_BUTTON)
        self.check_element(CatalogPageLocators.HOME_ICON)
        self.check_element(CatalogPageLocators.CURRENCY_BUTTON)
