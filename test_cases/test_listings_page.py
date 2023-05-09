import pytest
from utilities.custom_logger import Loggen
from page_objects.listings_page import ListingsPage

logger = Loggen.get_logger()


@pytest.fixture(scope='module')
def listings_page_object(driver):
    ListingsPage(driver).move_to()
    yield ListingsPage(driver)
    driver.close()


def test_ielts_listing(listings_page_object):
    logger.log(20, 'Ielts listings Test started.')
    listings_page_object.window_scroll()
    listings_page_object.click_ielts_listing_btn()
    if len(listings_page_object.get_ielts_listing_details()) > 0:
        assert True
    else:
        pytest.fail('Test failed. No Ielts listings found.')
    logger.log(20, 'Ielts listings Test ended.')


def test_popular_service_listings(listings_page_object):
    logger.log(20, 'Popular services listings Test started.')
    listings_page_object.get_popular_services()
    if len(listings_page_object.get_popular_services()) > 0:
        listings_page_object.print_popular_services()
        assert True
    else:
        pytest.fail('Test failed. No popular services found.')
    logger.log(20, 'Popular services listings Test ended.')
