from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.registration_page import RegistrationPage


def test_main_page(base_url, browser):
    browser.get(base_url)
    page = MainPage(browser)

    page.check_title("Your Store")  # проверка тайтла
    page.check_text("Featured")  # Проверка текста на странице
    page.check_elements_on_main_page()  # Проверка наличия 3-х элементов на странице


def test_catalog(base_url, browser):
    browser.get(base_url + '/en-gb/catalog/desktops')
    page = CatalogPage(browser)

    page.check_title("Desktops")  # проверка тайтла
    page.check_text("Desktops")  # Проверка текста на странице
    page.check_elements_on_catalog_page()  # Проверка наличия 3-х элементов на странице


def test_product(base_url, browser):
    browser.get(base_url + '/en-gb/product/desktops/palm-treo-pro')
    page = ProductPage(browser)

    page.check_title("Palm Treo Pro")  # проверка тайтла
    page.check_text("Palm")  # Проверка текста на странице
    page.check_elements_on_product_page()  # Проверка наличия 2-х элементов на странице
    page.check_text_on_cart_button("Add to Cart")  # Проверка текста на кнопке


def test_login(base_url, browser):
    browser.get(base_url + '/en-gb?route=account/login')
    page = LoginPage(browser)

    page.check_title("Account Login")  # проверка тайтла
    page.check_text("Returning Customer")  # Проверка текста на странице
    page.check_elements_on_login_page()  # Проверка наличия 2-х элементов на странице
    page.check_text_on_continue_button("Continue")  # Проверка текста на кнопке


def test_register(base_url, browser):
    browser.get(base_url + '/index.php?route=account/register')
    page = RegistrationPage(browser)

    page.check_title("Register Account")  # проверка тайтла
    page.check_text("Register Account")  # Проверка текста на странице
    page.check_text_in_link("login page")  # Проверка текста ссылки
    page.reg_fields_is_clickable()  # Проверка кликабельности двух элементов
