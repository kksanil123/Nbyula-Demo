import pytest
from page_objects.home_page import HomePage
from utilities.custom_logger import Loggen
from selenium.common.exceptions import ElementClickInterceptedException

logger = Loggen.get_logger()

@pytest.fixture(scope='module')
def home_page_object(driver):
    HomePage(driver).move_to()
    yield HomePage(driver)
    driver.close()


def test_click_logo(home_page_object):
    logger.log(20, 'Home page test started')
    try:
        home_page_object.click_study_abroad_btn()
        home_page_object.click_logo_btn()
    except ElementClickInterceptedException as e:
        pytest.fail('Buttons clicking failed', True)

    assert home_page_object.get_page_title() == 'https://nbl.one/'
    logger.log(20, 'Home page test ended')

