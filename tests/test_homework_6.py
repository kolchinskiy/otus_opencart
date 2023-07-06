import time

from pages.admin_page import AdminPage
from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.registration_page import RegistrationPage


def test_main_page(base_url, browser):
    browser.get(base_url)
    page = MainPage(browser)

    page.check_title("Your Store")  # проверка тайтла
    page.check_text_on_main_page()  # Проверка текста на странице
    page.check_elements_on_main_page()  # Проверка наличия 3-х элементов на странице


def test_catalog(base_url, browser):
    browser.get(base_url + '/desktops')
    page = CatalogPage(browser)

    page.check_title("Desktops")  # проверка тайтла
    page.check_text_on_catalog_page()  # Проверка текста на странице
    page.check_elements_on_catalog_page()  # Проверка наличия 3-х элементов на странице


def test_product(base_url, browser):
    browser.get(base_url + '/desktops/palm-treo-pro')
    page = ProductPage(browser)

    page.check_title("Palm Treo Pro")  # проверка тайтла
    page.check_text_on_product_page()  # Проверка текста на странице
    page.check_elements_on_product_page()  # Проверка наличия 2-х элементов на странице
    page.check_text_on_cart_button("Add to Cart")  # Проверка текста на кнопке


def test_login(base_url, browser):
    browser.get(base_url + '/index.php?route=account/login')
    page = LoginPage(browser)

    page.check_title("Account Login")  # проверка тайтла
    page.check_text_on_login_page()  # Проверка текста на странице
    page.check_elements_on_login_page()  # Проверка наличия 2-х элементов на странице
    page.check_text_on_continue_button("Continue")  # Проверка текста на кнопке


def test_register(base_url, browser):
    browser.get(base_url + '/index.php?route=account/register')
    page = RegistrationPage(browser)

    page.check_title("Register Account")  # проверка тайтла
    page.check_text_on_registration_page()  # Проверка текста на странице
    page.check_text_in_link("login page")  # Проверка текста ссылки
    page.reg_fields_is_clickable()  # Проверка кликабельности элемента
    page.push_continue_button()  # Проверка нажатия кнопки


def test_add_new_item(base_url, browser):
    browser.get(base_url + '/admin')
    page = AdminPage(browser)

    page.login_to_admin_page("user", "bitnami")  # логинимся под админом
    time.sleep(10)
