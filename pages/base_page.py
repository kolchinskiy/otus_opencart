import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 3)
        self.logger = browser.logger
        self.class_name = type(self).__name__

    @allure.step("Открываем страницу {url}")
    def open(self, url):
        self.browser.get(url)

    @allure.step("Проверяем соответствие текста '{text}'")
    def check_text(self, locator, text):
        self.logger.info("%s: Check text \"%s\" in %s" % (self.class_name, text, locator))
        el = self.wait.until(EC.visibility_of_element_located(locator))
        assert text in el.text

    @allure.step("Проверяем заголовок '{title}'")
    def check_title(self, title):
        self.logger.info("%s: Check title \"%s\"" % (self.class_name, title))
        assert self.wait.until(EC.title_is(title))

    @allure.step("Проверяем наличие элемента {element_name}")
    def check_element(self, element_name):
        self.logger.info("%s: Check element %s" % (self.class_name, element_name))
        return self.wait.until(EC.visibility_of_element_located(element_name))

    @allure.step("Проверяем на кликабельность {field_name}")
    def text_field_is_clickable(self, field_name):
        self.logger.info("%s: Check that element %s is clickable" % (self.class_name, field_name))
        assert self.wait.until(EC.element_to_be_clickable(field_name))

    @allure.step("Заполняем поле '{locator} текстом '{text}'")
    def fill_the_field(self, locator, text):
        self.logger.info(f"{self.class_name}: Input \"{text}\" in input {locator}")
        input_text = self.browser.find_element(*locator)
        input_text.send_keys(text)

    @allure.step("Нажимаем кнопку {locator}")
    def push_the_button(self, locator):
        self.logger.info(f"{self.class_name}: Push the button {locator}")
        button = self.browser.find_element(*locator)
        button.click()

    @allure.step("Кликаем на {locator}")
    def click(self, locator):
        self.logger.info("%s: Clicking element: %s" % (self.class_name, str(locator)))
        item = self.wait.until(EC.element_to_be_clickable(locator))
        item.click()

    @allure.step("Подтверждаем алерт")
    def accept_alert(self):
        self.logger.info("Accept current alert")
        alert = self.wait.until(expected_conditions.alert_is_present())
        alert.accept()
