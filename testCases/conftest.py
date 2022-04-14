import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.ie.service import Service
from webdriver_manager.microsoft import IEDriverManager


@pytest.fixture()
def setUpFixture(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Launching Chrome Browser.........................")
    elif browser == "edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        print("Launching Edge Browser.........................")
    else:
        driver = webdriver.Ie(service=Service(IEDriverManager().install()))
        print("Launching Ie Browser.........................")
    return driver


def pytest_addoption(parser):       # This will get the value from CLI / hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):       # This will return the Browser value to the setUpFixture Method
    return request.config.getoption("--browser")

######################## PyTest HTML Reports ########################


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Sourabh'


# It is hook for Delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
