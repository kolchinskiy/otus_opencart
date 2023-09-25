import allure

from pages.admin_page import AdminPage
from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.registration_page import RegistrationPage
from elements.currency_element import CurrencyElement


@allure.step("Проверяем главную страницу")
def test_main_page(base_url, browser):
    page = MainPage(browser)
    page.open(base_url)
    page.check_title("Your Store")  # проверка тайтла
    page.check_text_on_main_page()  # Проверка текста на странице
    page.check_elements_on_main_page()  # Проверка наличия 3-х элементов на странице


def test_catalog(base_url, browser):
    """Проверяем страницу каталога"""
    page = CatalogPage(browser)
    page.open(base_url + '/desktops')
    page.check_title("Desktops")  # проверка тайтла
    page.check_text_on_catalog_page()  # Проверка текста на странице
    page.check_elements_on_catalog_page()  # Проверка наличия 3-х элементов на странице


def test_product(base_url, browser):
    """Проверяем страницу товара"""
    page = ProductPage(browser)
    page.open(base_url + '/desktops/palm-treo-pro')
    page.check_title("Palm Treo Pro")  # проверка тайтла
    page.check_text_on_product_page()  # Проверка текста на странице
    page.check_elements_on_product_page()  # Проверка наличия 2-х элементов на странице
    page.check_text_on_cart_button("Add to Cart")  # Проверка текста на кнопке


def test_login(base_url, browser):
    """Проверяем страницу логина"""
    page = LoginPage(browser)
    page.open(base_url + '/index.php?route=account/login')
    page.check_title("Account Login")  # проверка тайтла
    page.check_text_on_login_page()  # Проверка текста на странице
    page.check_elements_on_login_page()  # Проверка наличия 2-х элементов на странице
    page.check_text_on_continue_button("Continue")  # Проверка текста на кнопке


def test_register(base_url, browser):
    """Проверяем страницу регистрации"""
    page = RegistrationPage(browser)
    page.open(base_url + '/index.php?route=account/register')
    page.check_title("Register Account")  # проверка тайтла
    page.check_text_on_registration_page()  # Проверка текста на странице
    page.check_text_in_link("login page")  # Проверка текста ссылки
    page.reg_fields_is_clickable()  # Проверка кликабельности элемента
    page.click_on_checkbox()  # Проверка нажатия галочки


def test_add_new_item(base_url, browser):
    """Проверяем добавление нгового товара админом"""
    page = AdminPage(browser)
    page.open(base_url + '/admin')
    page.login_to_admin_page("user", "bitnami")  # логинимся под админом
    page.add_new_item()  # Создаём новый товар
    page.check_message_about_success()  # Проверяем наличие сообщения об успехе


def test_delete_item(base_url, browser):
    """Проверяем удаление товара админом"""
    page = AdminPage(browser)
    page.open(base_url + '/admin')
    page.login_to_admin_page("user", "bitnami")  # логинимся под админом
    page.delete_first_item()  # Удаляем первый товар из списка
    page.check_message_about_success()  # Проверяем наличие сообщения об успехе


def test_reg_new_customer(base_url, browser):
    """Проверяем регистрацию нового пользователя"""
    page = RegistrationPage(browser)
    page.open(base_url + '/index.php?route=account/register')
    page.reg_new_customer()  # Создаём нового пользователя
    page.check_account_created()  # Проверяем, что аккаунт создан


def test_check_currency(base_url, browser):
    """Проверяем кнопку смены валюты"""
    page = CurrencyElement(browser)
    page.open(base_url)
    page.check_currency()
