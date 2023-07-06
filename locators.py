from selenium.webdriver.common.by import By


class MainPageLocators:
    TEXT = (By.CSS_SELECTOR, "#content > h3")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-inverse")
    SEARCH_FIELD = (By.CSS_SELECTOR, ".form-control")
    FOOTER_LINK = (By.CSS_SELECTOR, "body > footer > div > p > a")


class CatalogPageLocators:
    TEXT = (By.CSS_SELECTOR, "#content > h2")
    WISH_LIST_BUTTON = (By.CSS_SELECTOR, ".product-layout:nth-child(1) .fa-heart")
    HOME_ICON = (By.CSS_SELECTOR, ".fa-home")
    CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency .dropdown-toggle")


class ProductPageLocators:
    TEXT = (By.CSS_SELECTOR, "#content h1")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "li:nth-child(1) .thumbnail img")
    BUTTON_CART = (By.ID, "button-cart")
    COMPANY_LOGO = (By.CSS_SELECTOR, ".img-responsive")


class LoginPageLocators:
    TEXT = (By.CSS_SELECTOR, "#content .col-sm-6:nth-child(1) h2")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#input-email")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".col-sm-6:nth-child(2) .btn")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".col-sm-6:nth-child(1) .btn")


class RegistrationPageLocators:
    TEXT = (By.CSS_SELECTOR, "#content > h1")
    LOGIN_LINK = (By.CSS_SELECTOR, "#content > p > a")
    FIRST_NAME = (By.CSS_SELECTOR, "#input-firstname")
    BUTTON = (By.CSS_SELECTOR, ".btn-primary")


class AdminPageLocators:
    USERNAME = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.CSS_SELECTOR, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
