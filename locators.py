from selenium.webdriver.common.by import By


class GlobalLocators:
    TEXT = (By.ID, "content")


class MainPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "#header-cart > div > button")
    SEARCH_FIELD = (By.CSS_SELECTOR, "#search > input")
    FOOTER_LINK = (By.CSS_SELECTOR, "body > footer > div > p > a")


class CatalogPageLocators:
    WISH_LIST_BUTTON = (By.CSS_SELECTOR, "div:nth-child(1) form div.button-group button:nth-child(2)")
    HOME_ICON = (By.CSS_SELECTOR, "#product-category > ul > li:nth-child(1) > a > i")
    CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency > div > a > span")


class ProductPageLocators:
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(1) > div img.mb-3")
    BUTTON_CART = (By.ID, "button-cart")
    COMPANY_LOGO = (By.CSS_SELECTOR, "#logo > a > img")

class LoginPageLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, "#input-email")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#form-login > button")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#content > div > div:nth-child(1) .btn")


class RegistrationPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#content > p > a")
    FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    NEWS_TUMBLER = (By.CSS_SELECTOR, "#input-newsletter")