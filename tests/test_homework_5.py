from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_main_page(base_url, browser):
    browser.get(base_url)
    wait = WebDriverWait(browser, 3)

    el_1 = wait.until(EC.title_is("Your Store"))
    assert el_1
    el_2 = wait.until(EC.visibility_of_element_located((By.ID, "content")))
    assert "Featured" in el_2.text
    el_3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header-cart > div > button")))
    assert el_3
    el_4 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search > input")))
    assert el_4
    el_5 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > footer > div > p > a")))
    assert el_5


def test_catalog(base_url, browser):
    browser.get(base_url + '/en-gb/catalog/desktops')
    wait = WebDriverWait(browser, 3)

    el_1 = wait.until(EC.title_is("Desktops"))
    assert el_1
    el_2 = wait.until(EC.visibility_of_element_located((By.ID, "content")))
    assert "Desktops" in el_2.text
    el_3 = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#product-list > div:nth-child(1) > form > div > div.content > div.button-group >"
                          "button:nth-child(2)")))
    assert el_3
    el_4 = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#product-category > ul > li:nth-child(1) > a > i")))
    assert el_4
    el_5 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-currency > div > a > span")))
    assert el_5


def test_product(base_url, browser):
    browser.get(base_url + '/en-gb/product/desktops/palm-treo-pro')
    wait = WebDriverWait(browser, 3)

    el_1 = wait.until(EC.title_is("Palm Treo Pro"))
    assert el_1
    el_2 = wait.until(EC.visibility_of_element_located((By.ID, "content")))
    assert "Palm" in el_2.text
    el_3 = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(1) > div > a")))
    assert el_3
    el_4 = wait.until(EC.visibility_of_element_located((By.ID, "button-cart")))
    assert el_4.text == "Add to Cart"
    el_5 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#logo > a > img")))
    assert el_5


def test_login(base_url, browser):
    browser.get(base_url + '/en-gb?route=account/login')
    wait = WebDriverWait(browser, 3)

    el_1 = wait.until(EC.title_is("Account Login"))
    assert el_1
    el_2 = wait.until(EC.visibility_of_element_located((By.ID, "form-login")))
    assert "Returning Customer" in el_2.text
    el_3 = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content > div > div:nth-child(1) > div > div > a")))
    assert el_3.text == "Continue"
    el_4 = wait.until(EC.element_to_be_clickable(
        (By.ID, "input-email")))
    assert el_4
    el_5 = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#form-login > button")))
    assert el_5


def test_register(base_url, browser):
    browser.get(base_url + '/index.php?route=account/register')
    wait = WebDriverWait(browser, 3)

    el_1 = wait.until(EC.title_is("Register Account"))
    assert el_1
    el_2 = wait.until(EC.visibility_of_element_located((By.ID, "content")))
    assert "Register Account" in el_2.text
    el_3 = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content > p > a")))
    assert el_3.text == "login page"
    el_4 = wait.until(EC.element_to_be_clickable((By.ID, "input-firstname")))
    assert el_4
    el_5 = wait.until(EC.element_to_be_clickable((By.ID, "input-newsletter")))
    assert el_5
