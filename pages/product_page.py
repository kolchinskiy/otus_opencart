from locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):
    def check_elements_on_product_page(self):
        self.check_element(ProductPageLocators.PRODUCT_IMAGE)
        self.check_element(ProductPageLocators.COMPANY_LOGO)

    def check_text_on_cart_button(self, button_text):
        button = self.check_element(ProductPageLocators.BUTTON_CART)
        assert button.text == button_text

    def check_text_on_product_page(self):
        self.check_text(ProductPageLocators.TEXT, "Palm")
