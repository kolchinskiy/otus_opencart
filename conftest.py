import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import FirefoxOptions, ChromeOptions, EdgeOptions


def pytest_addoption(parser):
    parser.addoption("--url", default="http://192.168.1.104:8081")
    parser.addoption("--browser", default="chrome")
    parser.addoption("--maximize", action="store_true")
    parser.addoption("--headless", action="store_true")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    maximize = request.config.getoption("--maximize")
    headless = request.config.getoption("--headless")

    if browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options)
    elif browser_name == "chrome":
        service = Service()
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Driver {browser_name} not supported.")

    if maximize:
        driver.maximize_window()

    yield driver

    driver.quit()
