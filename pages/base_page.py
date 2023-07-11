from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def check_text(self, locator, text):
        wait = WebDriverWait(self.browser, 3)
        el = wait.until(EC.visibility_of_element_located(locator))
        assert text in el.text

    def check_title(self, title):
        wait = WebDriverWait(self.browser, 3)
        assert wait.until(EC.title_is(title))

    def check_element(self, element_name):
        wait = WebDriverWait(self.browser, 3)
        return wait.until(EC.visibility_of_element_located(element_name))

    def text_field_is_clickable(self, field_name):
        wait = WebDriverWait(self.browser, 3)
        assert wait.until(EC.element_to_be_clickable(field_name))

    def fill_the_field(self, locator, text):
        input_text = self.browser.find_element(*locator)
        input_text.send_keys(text)

    def push_the_button(self, locator):
        button = self.browser.find_element(*locator)
        button.click()

    def click(self, locator):
        wait = WebDriverWait(self.browser, 3)
        item = wait.until(EC.element_to_be_clickable(locator))
        item.click()

    def accept_alert(self):
        wait = WebDriverWait(self.browser, 3)
        alert = wait.until(expected_conditions.alert_is_present())
        alert.accept()
