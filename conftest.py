import logging
import datetime
import os
import random
import allure
import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ChromeOptions


def pytest_addoption(parser):
    parser.addoption("--executor", action="store", default="192.168.1.101")
    parser.addoption("--port", action="store", default="8081")
    parser.addoption("--browser", default="chrome")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--bv", default="113.0.5672.63")
    parser.addoption("--video", action="store_true")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--local", action="store", default=False)  # Определяем, локально ли запускаются тесты


@pytest.fixture
def base_url(request):
    return "http://" + request.config.getoption("--executor") + ":" + request.config.getoption("--port")


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    log_level = request.config.getoption("--log_level")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    video = request.config.getoption("--video")
    mobile = request.config.getoption("--mobile")
    local = request.config.getoption("--local")
    logs = request.config.getoption("--logs")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser_name == "chrome":
        options = ChromeOptions()
    elif browser_name == "firefox":
        options = FirefoxOptions()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    if not local:
        executor_url = f"http://host.docker.internal:4444/wd/hub"

        caps = {
            "browserName": browser_name,
            "browserVersion": version,
            "selenoid:options": {
                "enableVNC": vnc,
                "name": os.getenv("BUILD_NUMBER", str(random.randint(9000, 10000))),
                "screenResolution": "1280x2000",
                "enableVideo": video,
                "enableLog": False,
                "timeZone": "Europe/Moscow",
                "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"]
            },
            "acceptInsecureCerts": True,
        }

        options.set_capability('cloud:options', caps)
        driver = webdriver.Remote(command_executor=executor_url, options=options)

    else:
        if browser_name == "chrome":
            driver = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            driver = webdriver.Firefox(options=options)

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    if not mobile:
        driver.maximize_window()

    logger.info("Browser %s started" % browser)

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
