import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='module')
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service_object = Service()
    driver = webdriver.Chrome(service=service_object, options=options)
    driver.maximize_window()
    return driver
