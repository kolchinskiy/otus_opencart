from selenium.webdriver.common.by import By


class GlobalLocators:
    CURRENCY_BUTTON = (By.CSS_SELECTOR, "#form-currency .dropdown-toggle")
    CURRENCY_EURO = (By.CSS_SELECTOR, "#form-currency li:nth-child(1)")
    CURRENCY_POUND = (By.CSS_SELECTOR, "#form-currency li:nth-child(2)")
    CURRENCY_DOLLAR = (By.CSS_SELECTOR, "#form-currency li:nth-child(3)")
    CURRENCY_CHAR = (By.CSS_SELECTOR, "#form-currency strong")


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
    LAST_NAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD_1 = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_2 = (By.CSS_SELECTOR, "#input-confirm")
    PRIVACY_CHECKBOX = (By.CSS_SELECTOR, "input[type=checkbox]:nth-child(2)")
    BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#content > h1")


class AdminPageLocators:
    USERNAME = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn-primary")
    CATALOG_BUTTON = (By.CSS_SELECTOR, ".fa-tags")
    PRODUCTS_BUTTON = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2) > a")
    PLUS_BUTTON = (By.CSS_SELECTOR, ".fa-plus")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name1")
    META_TITLE = (By.CSS_SELECTOR, "#input-meta-title1")
    DATA_BUTTON = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2)")
    MODEL = (By.CSS_SELECTOR, "#input-model")
    SAVE_BUTTON = (By.CSS_SELECTOR, "div.page-header button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    FIRST_CHECKBOX = (By.CSS_SELECTOR, "tbody tr:nth-child(1) > td:nth-child(1) > input")
    TRASH_BUTTON = (By.CSS_SELECTOR, ".fa-trash-o")
