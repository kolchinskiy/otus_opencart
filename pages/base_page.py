from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import GlobalLocators


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def check_title(self, title):
        wait = WebDriverWait(self.browser, 3)
        assert wait.until(EC.title_is(title))

    def check_text(self, text):
        wait = WebDriverWait(self.browser, 3)
        el_2 = wait.until(EC.visibility_of_element_located(GlobalLocators.TEXT))
        assert text in el_2.text

    def check_element(self, element_name):
        wait = WebDriverWait(self.browser, 3)
        return wait.until(EC.visibility_of_element_located(element_name))

    def text_field_is_clickable(self, field_name):
        wait = WebDriverWait(self.browser, 3)
        assert wait.until(EC.element_to_be_clickable(field_name))
