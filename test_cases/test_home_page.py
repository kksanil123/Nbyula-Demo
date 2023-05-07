import pytest
from page_objects.home_page import HomePage
from selenium.common.exceptions import ElementClickInterceptedException


@pytest.fixture(scope='module')
def home_page_object(driver):
    yield HomePage(driver)
    driver.close()


def test_click_logo(home_page_object):
    try:
        home_page_object.get_logo()
    except ElementClickInterceptedException as e:
        print(e)
        assert False

    assert True

