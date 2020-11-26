import pytest
from selenium import webdriver
from base.web_driver_generator import WebDriverFactory
import logging
import utilities.custom_logger as cl

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser='chrome'):
    global driver
    log = cl.customLogger(logging.DEBUG)
    log.info("***********************STARTING TEST RUN*****************************")
    print("Running one time setUp")
    wdg = WebDriverFactory(browser)
    driver = wdg.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")
    log.info("*********************** TEST RUN END *****************************")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")