import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path

service_object = Service(executable_path=binary_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome(service=service_object, options=options)
    driver.maximize_window()
    return driver
